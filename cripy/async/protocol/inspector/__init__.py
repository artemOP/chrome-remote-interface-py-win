from typing import Any, List, Optional, Union
from cripy.async.protocol.inspector import events as Events


class Inspector(object):

    def __init__(self, chrome):
        self.chrome = chrome

    async def disable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Inspector.disable")
        return mayberes

    async def enable(self) -> Optional[dict]:
        mayberes = await self.chrome.send("Inspector.enable")
        return mayberes

    @staticmethod
    def get_event_classes() -> Optional[dict]:
        return Events.EVENT_TO_CLASS