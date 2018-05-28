from typing import Any, List, Optional, Set, Union
from cripy.helpers import BaseEvent


class AddHeapSnapshotChunkEvent(BaseEvent):

    event: str = "HeapProfiler.addHeapSnapshotChunk"

    def __init__(self) -> None:
        """
        :param chunk: The chunk
        :type str:
        """
        super().__init__()


class HeapStatsUpdateEvent(BaseEvent):
    """If heap objects tracking has been started then backend may send update for one or more fragments"""

    event: str = "HeapProfiler.heapStatsUpdate"

    def __init__(self) -> None:
        """
        :param statsUpdate: An array of triplets. Each triplet describes a fragment. The first integer is the
        fragment index, the second integer is a total count of objects for the fragment, the
        third integer is a total size of the objects for the fragment.
        :type array:
        """
        super().__init__()


class LastSeenObjectIdEvent(BaseEvent):
    """If heap objects tracking has been started then backend regularly sends a current value for last seen object id and corresponding timestamp.
	If the were changes in the heap since last event then one or more heapStatsUpdate events will be sent before a new lastSeenObjectId event."""

    event: str = "HeapProfiler.lastSeenObjectId"

    def __init__(self) -> None:
        """
        :param lastSeenObjectId: The lastSeenObjectId
        :type int:
        :param timestamp: The timestamp
        :type float:
        """
        super().__init__()


class ReportHeapSnapshotProgressEvent(BaseEvent):

    event: str = "HeapProfiler.reportHeapSnapshotProgress"

    def __init__(self) -> None:
        """
        :param done: The done
        :type int:
        :param total: The total
        :type int:
        :param finished: The finished
        :type bool:
        """
        super().__init__()


class ResetProfilesEvent(BaseEvent):

    event: str = "HeapProfiler.resetProfiles"

    def __init__(self) -> None:
        super().__init__()


EVENT_TO_CLASS = {
   "HeapProfiler.addHeapSnapshotChunk": AddHeapSnapshotChunkEvent,
   "HeapProfiler.heapStatsUpdate": HeapStatsUpdateEvent,
   "HeapProfiler.lastSeenObjectId": LastSeenObjectIdEvent,
   "HeapProfiler.reportHeapSnapshotProgress": ReportHeapSnapshotProgressEvent,
   "HeapProfiler.resetProfiles": ResetProfilesEvent,
}

