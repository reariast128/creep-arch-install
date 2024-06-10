from enum import Enum, auto


class PartitionSchemes(Enum):
    """Enum to represent supported partition schemes. Currently are supported `CLASSIC_SCHEME` and `SEPARATED_HOME_SCHEME`."""
    CLASSIC_SCHEME = auto()
    SEPARATED_HOME_SCHEME = auto()
    SWAP_CLASSIC_SCHEME = auto()
    SWAP_HOME_SCHEME = auto()
    CUSTOM_SCHEME = auto()
