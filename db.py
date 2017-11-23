import pymysql.cursors


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