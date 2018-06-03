# -*- coding: utf-8 -*-
import asyncio
import subprocess
from aiohttp import ClientConnectorError
import atexit
import os
import os.path
import shutil
import signal
import sys
import tempfile
import time
import ujson as json
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.error import URLError
from urllib.request import urlopen

from cripy.util import merge_dict, get_free_port
from cripy.client import RemoteClient

# https://peter.sh/experiments/chromium-command-line-switches/
# https://cs.chromium.org/chromium/src/chrome/common/chrome_switches.cc
DEFAULT_ARGS = [
    "--disable-background-networking",
    "--disable-background-timer-throttling",
    "--disable-client-side-phishing-detection",
    "--disable-default-apps",
    "--disable-extensions",
    "--disable-hang-monitor",
    "--disable-prompt-on-repost",
    "--disable-sync",
    "--disable-translate",
    "--metrics-recording-only",
    "--no-first-run",
    "--safebrowsing-disable-auto-update",
    "--password-store=basic",
    "--use-mock-keychain",
    "--mute-audio",
    "--window-size=1920,1080",
    "--disable-domain-reliability",  # no Domain Reliability Monitoring
    "--disable-renderer-backgrounding",
    "--disable-infobars",
    "--disable-translate",
]

TEMP_PROFILE = Path("cripy_temp_profile")


class LauncherError(Exception):
    pass


class Launcher(object):

    def __init__(self, options: Dict[str, Any] = None, **kwargs: Any) -> None:
        self.options: Dict[str, Any] = merge_dict(options, kwargs)
        self.chrome_dead: bool = True
        self.headless: bool = self.options.get("headless", False)
        self._tmp_user_data_dir: Optional[str] = None
        self.args: List[str] = []
        self._args_setup()
        self.chrome: Optional[RemoteClient] = None
        self.proc: Optional = None
        self.cmd = [self.exec] + self.args

    def _args_setup(self) -> None:
        if "port" not in self.options:
            self.port = get_free_port()
        else:
            self.port = self.options.get("port")
        if "url" not in self.options:
            self.url = f"http://localhost:{self.port}"
        else:
            self.url = self.options.get("url")

        if "executablePath" in self.options:
            self.exec = self.options["executablePath"]
        else:
            raise LauncherError("The chrome executable was not supplied")

        if not self.options.get("ignoreDefaultArgs", False):
            self.args.extend(DEFAULT_ARGS)
            self.args.append(f"--remote-debugging-port={self.port}")

        if self.options.get("appMode", False):
            self.options["headless"] = False
        if "headless" not in self.options or self.options.get("headless"):
            self.args.extend(["--headless"])

        if not isinstance(self.options.get("args"), list) or not any(
            opt for opt in self.options["args"] if opt.startswith("--user-data-dir")
        ):
            if "userDataDir" not in self.options:
                if not TEMP_PROFILE.exists():
                    TEMP_PROFILE.mkdir(parents=True)
                self._tmp_user_data_dir = tempfile.mkdtemp(dir=str(TEMP_PROFILE))
            self.args.append(
                "--user-data-dir={}".format(
                    self.options.get("userDataDir", self._tmp_user_data_dir)
                )
            )

    async def _get_ws_endpoint(self) -> str:
        for i in range(100):
            await asyncio.sleep(0.1)
            try:
                data = await RemoteClient.JSON(url=self.url)
                break
            except ClientConnectorError as e:
                print(e)
                continue
        else:
            # cannot connet to browser for 10 seconds
            raise LauncherError(f"Failed to connect to browser port: {self.url}")
        return data[0]["webSocketDebuggerUrl"]

    async def launch(self) -> RemoteClient:
        env = self.options.get("env")
        self.chrome_dead = False
        self.proc = subprocess.Popen(
            self.cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=env
        )
        print(self.proc)

        def _close_process(*args: Any, **kwargs: Any) -> None:
            if not self.chrome_dead:
                asyncio.get_event_loop().run_until_complete(self.kill_chrome())

        atexit.register(_close_process)
        if self.options.get("handleSIGINT", True):
            signal.signal(signal.SIGINT, _close_process)
        if self.options.get("handleSIGTERM", True):
            signal.signal(signal.SIGTERM, _close_process)
        if not sys.platform.startswith("win"):
            # SIGHUP is not defined on windows
            if self.options.get("handleSIGHUP", True):
                signal.signal(signal.SIGHUP, _close_process)

        wsurl = await self._get_ws_endpoint()
        self.chrome = RemoteClient(wsurl=wsurl)
        await self.chrome.connect()

        return self.chrome

    async def kill_chrome(self) -> None:
        """Terminate chromium process."""
        if self.chrome is not None and not self.chrome_dead and self.chrome.connected:
            try:
                await self.chrome.Browser.close()
            except Exception:
                # ignore errors on browser termination process
                pass
        if self._tmp_user_data_dir and os.path.exists(self._tmp_user_data_dir):
            # Force kill chrome only when using temporary userDataDir
            self.wait_for_chrome_death()
            self._cleanup_tmp_user_data_dir()

    def wait_for_chrome_death(self) -> None:
        """Terminate chrome."""
        if self.proc.poll() is None and not self.chrome_dead:
            self.chrome_dead = True
            self.proc.terminate()
            self.proc.wait()

    def _cleanup_tmp_user_data_dir(self) -> None:
        for retry in range(100):
            if self._tmp_user_data_dir and os.path.exists(self._tmp_user_data_dir):
                shutil.rmtree(self._tmp_user_data_dir, ignore_errors=True)
            else:
                break
        else:
            raise IOError("Unable to remove Temporary User Data")


async def launch(options: dict = None, **kwargs) -> RemoteClient:
    return await Launcher(options, **kwargs).launch()