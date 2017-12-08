import pymysql.cursors
import struct
import enum

class EnumOpcodes(enum.Enum):
    GOTO    = 1
    IF      = 2
    INVOKE  = 3
    SWITCH  = 4


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
            print "inserisco l pak con id " + str(tupla['id'])
            arrayIdAPK.append(tupla['id'])
        print "lunghezza ->" + str(len(arrayIdAPK))

        X = []
        apkVector = []
        for apk_id in arrayIdAPK:
            print "processing apk number %s" % apk_id
            for opcode in list(EnumOpcodes):
                name = opcode.name
                if name == "GOTO" or name == "IF" or name == "INVOKE":
                    query = "SELECT * FROM apk_opcode_frequency_map WHERE " \
                        "opcode_frequency_map_key LIKE '"+ name +"%' " \
                        "AND  apk_id=" +str(apk_id)
                else:
                    query = "SELECT * FROM apk_opcode_frequency_map WHERE " \
                            "opcode_frequency_map_key LIKE '%" + name + "' " \
                            "AND  apk_id=" + str(apk_id)

                res = self.executeQuery(query)
                sum = 0
                for dictionary in res:
                    sum +=dictionary['opcode_frequency_map']
                exist = len(res)
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
        # type: () -> object
        query = "SELECT is_malware FROM apk;"
        listOfDictionary = self.executeQuery(query)
        return [struct.unpack('h', field["is_malware"] + "\x00")[0]
               for field in listOfDictionary]


    def getSingleAPKfrequency(self, features, index):
        tmp = "SELECT opcode_frequency_map FROM apk_opcode_frequency_map WHERE "
        vectorOfFeatures = []
        for feature in features:
            query = tmp + " apk_id=" + str(index) + \
                    " and opcode_frequency_map_key='" + feature + "';"
            freq = self.executeQuery(query)
            print freq
            map = freq[0]
            vectorOfFeatures.append(map["opcode_frequency_map"])
        print "*****************"
        return vectorOfFeatures


    def retrieveFlowInstructions(self, apkId, flowInstructionList):
        query = "SELECT opcode_frequency_map FROM apk_opcode_frequency_map WHERE " \
                "apk_id=" + str(apkId)

        frequencyList = []
        for key in flowInstructionList:
            tmp = "AND opcode_frequency_map_key='" + key + "'"
            res = self.executeQuery(query + tmp)
            frequencyList.append(res)




