import sqlite3

class DB:

    #Passo il path nel costruttore
    def __init__(self,pathDatabase):
        self.conn = sqlite3.connect(pathDatabase)
        self.cursore = self.conn.cursor()

    def executeQuery(self,query):
        print query
        self.cursore.execute(query).fetchall()



    def fine(self):
        self.conn.commit()

# Selezionando id per id controllo che ci sia quell'istruzione
    def essiteLaFunzioneInAPKId(self,id,istruzione):
        query = "SELECT * FROM apk_opcode_frequency_map WHERE apk_id="+str(id)+" AND opcode_frequency_map_key='" + istruzione+"'"
        print query
        print self.executeQuery(query)