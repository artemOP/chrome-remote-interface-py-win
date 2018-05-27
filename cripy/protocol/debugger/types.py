from typing import Any, List, Optional, Set, Union
from cripy.helpers import PayloadMixin, BaseEvent, ChromeTypeBase
from cripy.protocol.runtime import types as Runtime

BreakpointId = str

CallFrameId = str


class Location(ChromeTypeBase):
    """Location in the source code."""

    def __init__(
        self,
        scriptId: "Runtime.ScriptId",
        lineNumber: int,
        columnNumber: Optional[int] = None,
    ) -> None:
        """
        :param scriptId: Script identifier as reported in the `Debugger.scriptParsed`.
        :param lineNumber: Line number in the script (0-based).
        :param columnNumber: Column number in the script (0-based).
        """
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.lineNumber: int = lineNumber
        self.columnNumber: Optional[int] = columnNumber


class ScriptPosition(ChromeTypeBase):
    """Location in the source code."""

    def __init__(self, lineNumber: int, columnNumber: int) -> None:
        """
        :param lineNumber: The lineNumber
        :param columnNumber: The columnNumber
        """
        super().__init__()
        self.lineNumber: int = lineNumber
        self.columnNumber: int = columnNumber


class CallFrame(ChromeTypeBase):
    """JavaScript call frame. Array of call frames form the call stack."""

    def __init__(
        self,
        callFrameId: "CallFrameId",
        functionName: str,
        location: "Location",
        url: str,
        scopeChain: List["Scope"],
        this: "Runtime.RemoteObject",
        functionLocation: Optional["Location"] = None,
        returnValue: Optional["Runtime.RemoteObject"] = None,
    ) -> None:
        """
        :param callFrameId: Call frame identifier. This identifier is only valid while the virtual machine is paused.
        :param functionName: Name of the JavaScript function called on this call frame.
        :param functionLocation: Location in the source code.
        :param location: Location in the source code.
        :param url: JavaScript script name or url.
        :param scopeChain: Scope chain for this call frame.
        :param this: `this` object for this call frame.
        :param returnValue: The value being returned, if the function is at return point.
        """
        super().__init__()
        self.callFrameId: CallFrameId = callFrameId
        self.functionName: str = functionName
        self.functionLocation: Optional[Location] = functionLocation
        self.location: Location = location
        self.url: str = url
        self.scopeChain: List[Scope] = scopeChain
        self.this: Runtime.RemoteObject = this
        self.returnValue: Optional[Runtime.RemoteObject] = returnValue


class Scope(ChromeTypeBase):
    """Scope description."""

    def __init__(
        self,
        type: str,
        object: "Runtime.RemoteObject",
        name: Optional[str] = None,
        startLocation: Optional["Location"] = None,
        endLocation: Optional["Location"] = None,
    ) -> None:
        """
        :param type: Scope type.
        :param object: Object representing the scope. For `global` and `with` scopes it represents the actual
object; for the rest of the scopes, it is artificial transient object enumerating scope
variables as its properties.
        :param name: The name
        :param startLocation: Location in the source code where scope starts
        :param endLocation: Location in the source code where scope ends
        """
        super().__init__()
        self.type: str = type
        self.object: Runtime.RemoteObject = object
        self.name: Optional[str] = name
        self.startLocation: Optional[Location] = startLocation
        self.endLocation: Optional[Location] = endLocation


class SearchMatch(ChromeTypeBase):
    """Search match for resource."""

    def __init__(self, lineNumber: float, lineContent: str) -> None:
        """
        :param lineNumber: Line number in resource content.
        :param lineContent: Line with match content.
        """
        super().__init__()
        self.lineNumber: float = lineNumber
        self.lineContent: str = lineContent


class BreakLocation(ChromeTypeBase):

    def __init__(
        self,
        scriptId: "Runtime.ScriptId",
        lineNumber: int,
        columnNumber: Optional[int] = None,
        type: Optional[str] = None,
    ) -> None:
        """
        :param scriptId: Script identifier as reported in the `Debugger.scriptParsed`.
        :param lineNumber: Line number in the script (0-based).
        :param columnNumber: Column number in the script (0-based).
        :param type: The type
        """
        super().__init__()
        self.scriptId: Runtime.ScriptId = scriptId
        self.lineNumber: int = lineNumber
        self.columnNumber: Optional[int] = columnNumber
        self.type: Optional[str] = type
