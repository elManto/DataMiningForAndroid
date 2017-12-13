import pymysql.cursors
import struct
import enum

class EnumOpcodes(enum.Enum):
    GOTO    = 1
    IF      = 2
    INVOKE  = 3
    SWITCH  = 4
    ADD     = 5



class database:

    #usage Ex: database("localhost", "root", YOUR_PASSWORD, "opcodes")
    def __init__(self, host, user, pwd, db):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=pwd,
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)


    '''
    This function takes as input a list of all the opcodes and checks if that
    opcode is contained in every APK
    '''
    def defineFeature(self):
        # Creates an array which will contain all the id of the different APK
        arrayIdAPK = []

        # ...then, opcodes which are not contained in every APK are removed
        query = "SELECT * FROM apk"
        tuple = self.executeQuery(query)
        for tupla in tuple:
            arrayIdAPK.append(tupla['id'])

        # matrix contained for all apk frequency set of opcodes
        X = []
        apkVector = []
        for apk_id in arrayIdAPK:
            print "processing apk number %s" % apk_id
            for opcode in list(EnumOpcodes):
                name = opcode.name
                if name == "GOTO" or name == "IF" or name == "INVOKE" or name == "ADD":
                    query = "SELECT * FROM apk_opcode_frequency_map WHERE " \
                        "opcode_frequency_map_key LIKE '"+ name +"%' " \
                        "AND  apk_id=" +str(apk_id)
                else:
                    query = "SELECT * FROM apk_opcode_frequency_map WHERE " \
                            "opcode_frequency_map_key LIKE '%" + name + "' " \
                            "AND  apk_id=" + str(apk_id)

                queryResult = self.executeQuery(query)

                # sum of frequency of IF_ ... and other
                sum = 0
                for dictionary in queryResult:
                    sum +=dictionary['opcode_frequency_map']
                exist = len(queryResult)
                if exist == 0:
                    apkVector.append(0)
                else:
                    apkVector.append(sum)
            X.append(apkVector)
            apkVector = []

        return X




    def getNumberOfAPK(self):
        query = "SELECT COUNT(*) FROM apk;"
        dictionary = self.executeQuery(query)[0]
        return dictionary["COUNT(*)"]


    def executeQuery(self, query):
        with self.connection.cursor() as cursor:
            cursor = self.connection.cursor()
            cursor.execute(query)
            res = cursor.fetchall()
            self.connection.commit()
            return res


    def getIsMalware(self):
        query = "SELECT is_malware FROM apk;"
        listOfDictionary = self.executeQuery(query)
        return [struct.unpack('h', field["is_malware"] + "\x00")[0]
               for field in listOfDictionary]


    def getMalwareTypicalOpcodes(self):
        l = []
        f = open('total_opcode_list.txt', 'r')
        while(True):
            s = f.readline()
            if s != "":
                l.append(s[:len(s) - 1])
            else:
                break
        print l
        nonMatchList = []
        status = 0
        for opcode in l:
            print "status-> " + str(status)
            status += 1
            query = "SELECT apk_id FROM apk_opcode_frequency_map WHERE " \
                        "opcode_frequency_map_key ='"+ opcode + "'"
            res = self.executeQuery(query)
            d = dict()
            d["opcode"] = opcode
            d["is_malware"] = 0
            d["is_goodware"] = 0
            for i in res:
                if i['apk_id'] < 1015:
                    d["is_goodware"] += 1
                else:
                    d["is_malware"] += 1
            nonMatchList.append(d)
        for i in nonMatchList:
            print i











