from cripy.gevent.protocol.network import types as Network

__all__ = ["Audits"]


class Audits(object):
    """
    Audits domain allows investigation of page violations and possible improvements.
    """

    dependencies = ["Network"]

    def __init__(self, chrome):
        self.chrome = chrome

    def getEncodedResponse(self, requestId, encoding, quality=None, sizeOnly=None):
        """
        :param requestId: Identifier of the network request to get content for.
        :type requestId: str
        :param encoding: The encoding to use.
        :type encoding: str
        :param quality: The quality of the encoding (0-1). (defaults to 1)
        :type quality: Optional[float]
        :param sizeOnly: Whether to only return the size information (defaults to false).
        :type sizeOnly: Optional[bool]
        """
        msg_dict = dict()
        if requestId is not None:
            msg_dict["requestId"] = requestId
        if encoding is not None:
            msg_dict["encoding"] = encoding
        if quality is not None:
            msg_dict["quality"] = quality
        if sizeOnly is not None:
            msg_dict["sizeOnly"] = sizeOnly
        wres = self.chrome.send("Audits.getEncodedResponse", msg_dict)
        res = wres.get()
        return res

    @staticmethod
    def get_event_classes():
        return None