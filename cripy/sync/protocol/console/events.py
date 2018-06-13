from types import SimpleNamespace
try:
    from cripy.sync.protocol.console.types import *
except ImportError:
    pass

__all__ = [
    "MessageAddedEvent",
]


class MessageAddedEvent(object):
    """
    Issued when new console message is added.
    """

    event = "Console.messageAdded"

    def __init__(self, message):
        """
        :param message: Console message that has been added.
        :type message: dict
        """
        super().__init__()
        self.message = ConsoleMessage.safe_create(message)

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.message is not None:
            repr_args.append("message={!r}".format(self.message))
        return "MessageAddedEvent(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = MessageAddedEvent(**init)
                return ourselves
            except Exception:
                return init
        else:
            return init

    @staticmethod
    def safe_create_from_list(init):
        if init is not None:
            list_of_self = []
            for it in init:
                list_of_self.append(MessageAddedEvent.safe_create(it))
            return list_of_self
        else:
            return init


EVENT_TO_CLASS = {
   "Console.messageAdded": MessageAddedEvent,
}

EVENT_NS = SimpleNamespace(
  MessageAdded="Console.messageAdded",
)