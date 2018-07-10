from typing import Any, List, Optional, Union


__all__ = ["DOMStorage"]


class DOMStorage(object):
    """
    Query and modify DOM storage.
    """


    def __init__(self, chrome):
        """
        Construct a new DOMStorage object

        :param chrome: An instance of the devtools protocol client
        """
        self.chrome = chrome

    async def clear(self, storageId: dict) -> Optional[dict]:
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        res = await self.chrome.send('DOMStorage.clear', msg_dict)
        return res

    async def disable(self) -> Optional[dict]:
        """
        Disables storage tracking, prevents storage events from being sent to the client.
        """
        res = await self.chrome.send('DOMStorage.disable')
        return res

    async def enable(self) -> Optional[dict]:
        """
        Enables storage tracking, storage events will now be delivered to the client.
        """
        res = await self.chrome.send('DOMStorage.enable')
        return res

    async def getDOMStorageItems(self, storageId: dict) -> Optional[dict]:
        """
        :param storageId: The storageId
        :type storageId: dict
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        res = await self.chrome.send('DOMStorage.getDOMStorageItems', msg_dict)
        return res

    async def removeDOMStorageItem(self, storageId: dict, key: str) -> Optional[dict]:
        """
        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        if key is not None:
            msg_dict['key'] = key
        res = await self.chrome.send('DOMStorage.removeDOMStorageItem', msg_dict)
        return res

    async def setDOMStorageItem(self, storageId: dict, key: str, value: str) -> Optional[dict]:
        """
        :param storageId: The storageId
        :type storageId: dict
        :param key: The key
        :type key: str
        :param value: The value
        :type value: str
        """
        msg_dict = dict()
        if storageId is not None:
            msg_dict['storageId'] = storageId
        if key is not None:
            msg_dict['key'] = key
        if value is not None:
            msg_dict['value'] = value
        res = await self.chrome.send('DOMStorage.setDOMStorageItem', msg_dict)
        return res

    def domStorageItemAdded(self, fn, once=False) -> None:
        if once:
            self.chrome.once("DOMStorage.domStorageItemAdded", fn)
        else:
            self.chrome.on("DOMStorage.domStorageItemAdded", fn)

    def domStorageItemRemoved(self, fn, once=False) -> None:
        if once:
            self.chrome.once("DOMStorage.domStorageItemRemoved", fn)
        else:
            self.chrome.on("DOMStorage.domStorageItemRemoved", fn)

    def domStorageItemUpdated(self, fn, once=False) -> None:
        if once:
            self.chrome.once("DOMStorage.domStorageItemUpdated", fn)
        else:
            self.chrome.on("DOMStorage.domStorageItemUpdated", fn)

    def domStorageItemsCleared(self, fn, once=False) -> None:
        if once:
            self.chrome.once("DOMStorage.domStorageItemsCleared", fn)
        else:
            self.chrome.on("DOMStorage.domStorageItemsCleared", fn)


