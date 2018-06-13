from cripy.sync.protocol.headlessexperimental import events as Events
from cripy.sync.protocol.headlessexperimental import types as Types

__all__ = ["HeadlessExperimental"] + Events.__all__ + Types.__all__ 


class HeadlessExperimental(object):
    """
    This domain provides experimental commands only supported in headless mode.
    """

    dependencies = ['Page', 'Runtime']

    def __init__(self, chrome):
        self.chrome = chrome

    def beginFrame(self, frameTimeTicks, interval, noDisplayUpdates, screenshot):
        """
        :param frameTimeTicks: Timestamp of this BeginFrame in Renderer TimeTicks (milliseconds of uptime). If not set, the current time will be used.
        :type frameTimeTicks: Optional[float]
        :param interval: The interval between BeginFrames that is reported to the compositor, in milliseconds. Defaults to a 60 frames/second interval, i.e. about 16.666 milliseconds.
        :type interval: Optional[float]
        :param noDisplayUpdates: Whether updates should not be committed and drawn onto the display. False by default. If true, only side effects of the BeginFrame will be run, such as layout and animations, but any visual updates may not be visible on the display or in screenshots.
        :type noDisplayUpdates: Optional[bool]
        :param screenshot: If set, a screenshot of the frame will be captured and returned in the response. Otherwise, no screenshot will be captured. Note that capturing a screenshot can fail, for example, during renderer initialization. In such a case, no screenshot data will be returned.
        :type screenshot: Optional[dict]
        """
        def cb(res):
            self.chrome.emit('HeadlessExperimental.beginFrame', res)
        msg_dict = dict()
        if frameTimeTicks is not None:
            msg_dict['frameTimeTicks'] = frameTimeTicks
        if interval is not None:
            msg_dict['interval'] = interval
        if noDisplayUpdates is not None:
            msg_dict['noDisplayUpdates'] = noDisplayUpdates
        if screenshot is not None:
            msg_dict['screenshot'] = screenshot
        self.chrome.send('HeadlessExperimental.beginFrame', params=msg_dict, cb=cb)


    def disable(self):
        self.chrome.send('HeadlessExperimental.disable')


    def enable(self):
        self.chrome.send('HeadlessExperimental.enable')


    @staticmethod
    def get_event_classes():
        return Events.EVENT_TO_CLASS
