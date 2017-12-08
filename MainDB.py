
import enum

class EnumOpcodes(enum.Enum):
    GOTO    = 1
    IF      = 2
    INVOKE  = 3
    SWITCH  = 4

for i in list(EnumOpcodes):
    print i.name



