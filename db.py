import pymysql.cursors
import struct


class database():

    #usage: database("localhost", "root", "MmscC,eh43a", "opcodes")
    def __init__(self, host, user, pwd, db):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=pwd,
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def defineFeature(self, listOfOpcodes):
        with self.connection.cursor() as cursor:
            query = "SELECT * FROM apk;"
            cursor = self.connection.cursor()
            cursor.execute(query)
            res = cursor.fetchall()
            print res
            self.connection.commit()

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
        count = 0
        for feature in features:
            count += 1
            query = tmp + " apk_id=" + str(index) + \
                    " and opcode_frequency_map_key=" + feature + ";"
            freq = self.executeQuery(query)





''' 
try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()
'''