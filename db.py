import pymysql.cursors
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












        '''
                with self.connection.cursor() as cursor:
            query = "SELECT * FROM apk;"
            cursor = self.connection.cursor()
            cursor.execute(query)
            res = cursor.fetchall()
            print res
            self.connection.commit() 
        '''

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