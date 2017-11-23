import pymysql.cursors
import struct
import copy



class database:

    #usage: database("localhost", "root", "MmscC,eh43a", "opcodes")
    def __init__(self, host, user, pwd, db):
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=pwd,
            db=db,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    '''
    Tale funzione prende come argomento un insieme di opcode (listOfOpcode)
    e controllo se quell' opcode e' contenuto in tutti gli apk
    
    Torna un array di opcode comunia tutti
    '''

    def defineFeature(self, listOfOpcodes):

        #Creo un'array contenente tutti gli id degli apk

        arrayIdAPK = []

        # Tale array e' inizializzato a tutti gli opcode e poi piano piano
        # tolgo quelli che non sono in tutti gli apk
        listaDegliOpcodesInAlmenoUnAPK = list(listOfOpcodes)

        query = "SELECT * FROM apk"
        cursor = self.connection.cursor()
        cursor.execute(query)
        tuple = cursor.fetchall()
        for tupla in tuple:
            arrayIdAPK.append(tupla['id'])
        # qui ho popolato l'array e controllo nella tabella apk_opcode_frequency_map
        # se l'apk con quell'id ha un l'opcode selezionato
        for apk_id in arrayIdAPK:
            for opcode in listOfOpcodes:
                query = "SELECT * FROM apk_opcode_frequency_map WHERE  opcode_frequency_map_key='"+ opcode +"' AND  apk_id=" +str(apk_id)
                print query
                cursor = self.connection.cursor()
                cursor.execute(query)
                # Questa variabile vale 0 se non e' presente quell'istruzione nell'apk selezionato
                # altrimenti
                esiste = len(cursor.fetchall())
                if esiste == 0 and listaDegliOpcodesInAlmenoUnAPK.__contains__(opcode):
                    listaDegliOpcodesInAlmenoUnAPK.remove(opcode)
        for i in listaDegliOpcodesInAlmenoUnAPK:
            print i


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