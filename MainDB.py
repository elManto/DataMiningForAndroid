from db import database
import time


database = database("localhost","root"," ", "opcodes")
database.defineFeature(["ADD_DOUBLE_2ADDR","FOULO"])