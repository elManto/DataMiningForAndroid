import pymysql.cursors
import struct



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
    def defineFeature(self, listOfOpcodes):
        # Creates an array which will contain all the id of the different APK
        arrayIdAPK = []

        # Initializes the array with all the existent opcodes...
        apkFeatures = list(listOfOpcodes)

        # ...then, opcodes which are not contained in every APK are removed
        query = "SELECT * FROM apk LIMIT 2000"
        tuple = self.executeQuery(query)
        for tupla in tuple:
            arrayIdAPK.append(tupla['id'])

        for apk_id in arrayIdAPK:
            print "processing apk number %s" % apk_id
            for opcode in listOfOpcodes:
                query = "SELECT * FROM apk_opcode_frequency_map WHERE " \
                        "opcode_frequency_map_key='"+ opcode +"' AND  apk_id=" +str(apk_id)
                res = self.executeQuery(query)
                exist = len(res)
                if exist == 0 and apkFeatures.__contains__(opcode):
                    apkFeatures.remove(opcode)
        return apkFeatures


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
