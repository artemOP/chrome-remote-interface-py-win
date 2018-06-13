
__all__ = [
    "ScreenOrientation",
]


class ScreenOrientation(object):
    """
    Screen orientation.
    """

    def __init__(self, type, angle):
        """
        :param type: Orientation type.
        :type type: str
        :param angle: Orientation angle.
        :type angle: int
        """
        super().__init__()
        self.type = type
        self.angle = angle

    def __contains__(self, item):
        return item in self.__dict__

    def __getitem__(self, k):
        return self.__dict__[k]

    def get(self, what, default=None):
        return self.__dict__.get(what, default)

    def __repr__(self):
        repr_args = []
        if self.type is not None:
            repr_args.append("type={!r}".format(self.type))
        if self.angle is not None:
            repr_args.append("angle={!r}".format(self.angle))
        return "ScreenOrientation(" + ', '.join(repr_args)+")"

    @staticmethod
    def safe_create(init):
        if init is not None:
            try:
                ourselves = ScreenOrientation(**init)
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
                list_of_self.append(ScreenOrientation.safe_create(it))
            return list_of_self
        else:
            return init


TYPE_TO_OBJECT = {
    "ScreenOrientation": ScreenOrientation,
}