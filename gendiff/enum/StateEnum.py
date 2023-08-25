from enum import Enum


class StateEnum(str, Enum):
    Added = "ADDED"
    Removed = "REMOVED"
    Changed = "CHANGED"
    Unchanged = "UNCHANGED"
    Children = "CHILDREN"
