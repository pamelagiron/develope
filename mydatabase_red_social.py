import mysql.connector

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect(host="localhost",
        user="root",
        passwd="", database="db_red_social")

        return connection

        def insert_db(self, email, pwd, age):
            my_connection = self.open_connection()
            cursor = my_connection.cursor()
            query = "insert into tbl_usuario(CORREO, PWD, EDAD) VALUES (%s,%s,%s)"
            data = email (email, pwd, age)
            cursor.execute(query, data)
            my_connection.commit()
            my_connection.close()
