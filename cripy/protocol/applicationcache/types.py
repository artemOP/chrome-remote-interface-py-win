from typing import Any, List, Optional, Set, Union, TypeVar
from cripy.helpers import ProtocolType
from cripy.protocol.page import types as Page


class FrameWithManifest(ProtocolType):
    """Frame identifier - manifest URL pair."""

    def __init__(self, frameId: "Page.FrameId", manifestURL: str, status: int) -> None:
        """
        :param frameId: Frame identifier.
        :type frameId: Page.FrameId
        :param manifestURL: Manifest URL.
        :type manifestURL: str
        :param status: Application cache status.
        :type status: int
        """
        super().__init__()
        self.frameId: Page.FrameId = frameId
        self.manifestURL: str = manifestURL
        self.status: int = status


class ApplicationCacheResource(ProtocolType):
    """Detailed application cache resource information."""

    def __init__(self, url: str, size: int, type: str) -> None:
        """
        :param url: Resource url.
        :type url: str
        :param size: Resource size.
        :type size: int
        :param type: Resource type.
        :type type: str
        """
        super().__init__()
        self.url: str = url
        self.size: int = size
        self.type: str = type


class ApplicationCache(ProtocolType):
    """Detailed application cache information."""

    def __init__(
        self,
        manifestURL: str,
        size: float,
        creationTime: float,
        updateTime: float,
        resources: List[Union["ApplicationCacheResource", dict]],
    ) -> None:
        """
        :param manifestURL: Manifest URL.
        :type manifestURL: str
        :param size: Application cache size.
        :type size: float
        :param creationTime: Application cache creation time.
        :type creationTime: float
        :param updateTime: Application cache update time.
        :type updateTime: float
        :param resources: Application cache resources.
        :type resources: array
        """
        super().__init__()
        self.manifestURL: str = manifestURL
        self.size: float = size
        self.creationTime: float = creationTime
        self.updateTime: float = updateTime
        self.resources: List[ApplicationCacheResource] = resources


OBJECT_LIST = {
    "FrameWithManifest": FrameWithManifest,
    "ApplicationCacheResource": ApplicationCacheResource,
    "ApplicationCache": ApplicationCache,
}
