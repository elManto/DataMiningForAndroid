from db import database
from Util import getListOfOpcode

opcodeList = getListOfOpcode()

database = database("localhost","root"," ", "opcodes")
database.defineFeature(["ADD_DOUBLE_2ADDR"])