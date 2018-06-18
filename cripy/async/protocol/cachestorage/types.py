from typing import Any, List, Optional, Union, TypeVar


class Header(object):

    def __init__(self, name: str, value: str) -> None:
        """
        :param name: The name
        :type name: str
        :param value: The value
        :type value: str
        """
        super().__init__()
        self.name = name
        self.value = value

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.name is not None:
            repr_args.append("name={!r}".format(self.name))
        if self.value is not None:
            repr_args.append("value={!r}".format(self.value))
        return "Header(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["Header", dict]]:
        if init is not None:
            try:
                ourselves = Header(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["Header", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Header.safe_create(it))
            return list_of_self
        else:
            return init


class DataEntry(object):
    """
    Data entry.
    """

    def __init__(
        self,
        requestURL: str,
        requestMethod: str,
        requestHeaders: List[Union["Header", dict]],
        responseTime: float,
        responseStatus: int,
        responseStatusText: str,
        responseHeaders: List[Union["Header", dict]],
    ) -> None:
        """
        :param requestURL: Request URL.
        :type requestURL: str
        :param requestMethod: Request method.
        :type requestMethod: str
        :param requestHeaders: Request headers
        :type requestHeaders: List[dict]
        :param responseTime: Number of seconds since epoch.
        :type responseTime: float
        :param responseStatus: HTTP response status code.
        :type responseStatus: int
        :param responseStatusText: HTTP response status text.
        :type responseStatusText: str
        :param responseHeaders: Response headers
        :type responseHeaders: List[dict]
        """
        super().__init__()
        self.requestURL = requestURL
        self.requestMethod = requestMethod
        self.requestHeaders = Header.safe_create_from_list(requestHeaders)
        self.responseTime = responseTime
        self.responseStatus = responseStatus
        self.responseStatusText = responseStatusText
        self.responseHeaders = Header.safe_create_from_list(responseHeaders)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.requestURL is not None:
            repr_args.append("requestURL={!r}".format(self.requestURL))
        if self.requestMethod is not None:
            repr_args.append("requestMethod={!r}".format(self.requestMethod))
        if self.requestHeaders is not None:
            repr_args.append("requestHeaders={!r}".format(self.requestHeaders))
        if self.responseTime is not None:
            repr_args.append("responseTime={!r}".format(self.responseTime))
        if self.responseStatus is not None:
            repr_args.append("responseStatus={!r}".format(self.responseStatus))
        if self.responseStatusText is not None:
            repr_args.append("responseStatusText={!r}".format(self.responseStatusText))
        if self.responseHeaders is not None:
            repr_args.append("responseHeaders={!r}".format(self.responseHeaders))
        return "DataEntry(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["DataEntry", dict]]:
        if init is not None:
            try:
                ourselves = DataEntry(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["DataEntry", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(DataEntry.safe_create(it))
            return list_of_self
        else:
            return init


class CachedResponse(object):
    """
    Cached response
    """

    def __init__(self, body: str) -> None:
        """
        :param body: Entry content, base64-encoded.
        :type body: str
        """
        super().__init__()
        self.body = body

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.body is not None:
            repr_args.append("body={!r}".format(self.body))
        return "CachedResponse(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["CachedResponse", dict]]:
        if init is not None:
            try:
                ourselves = CachedResponse(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["CachedResponse", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(CachedResponse.safe_create(it))
            return list_of_self
        else:
            return init


class Cache(object):
    """
    Cache identifier.
    """

    def __init__(self, cacheId: str, securityOrigin: str, cacheName: str) -> None:
        """
        :param cacheId: An opaque unique id of the cache.
        :type cacheId: str
        :param securityOrigin: Security origin of the cache.
        :type securityOrigin: str
        :param cacheName: The name of the cache.
        :type cacheName: str
        """
        super().__init__()
        self.cacheId = cacheId
        self.securityOrigin = securityOrigin
        self.cacheName = cacheName

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k) -> Any:
        return self.__dict__[k]

    def get(self, what, default=None) -> Any:
        return self.__dict__.get(what, default)

    def __repr__(self) -> str:
        repr_args = []
        if self.cacheId is not None:
            repr_args.append("cacheId={!r}".format(self.cacheId))
        if self.securityOrigin is not None:
            repr_args.append("securityOrigin={!r}".format(self.securityOrigin))
        if self.cacheName is not None:
            repr_args.append("cacheName={!r}".format(self.cacheName))
        return "Cache(" + ", ".join(repr_args) + ")"

    @staticmethod
    def safe_create(init: Optional[dict]) -> Optional[Union["Cache", dict]]:
        if init is not None:
            try:
                ourselves = Cache(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(
        init: Optional[List[dict]]
    ) -> Optional[List[Union["Cache", dict]]]:
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(Cache.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "Header": Header,
    "DataEntry": DataEntry,
    "CachedResponse": CachedResponse,
    "Cache": Cache,
}