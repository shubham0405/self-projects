import mysql.connector
import config

class DatabaseEntry:

    def __init__(self,username,password,database_name):

        self.mydb = mysql.connector.connect(
            host = 'localhost',
            user = username,
            passwd = password,
            database = database_name
        )


    def createTable(self,table_name):
        try:
            mycursor = self.mydb.cursor()
            sqlFormula = "CREATE TABLE {} (name varchar(255), tvseries varchar(255))".format(table_name)

            mycursor.execute(sqlFormula)
            self.mydb.commit()

            return True

        except Exception as e:
            print(e)  
            return False  

        


    def insertInto(self, table, name, tvseries):

        try:
            mycursor = self.mydb.cursor()
            sqlFormula = "insert into " + table + " (name,tvseries) values (%s, %s)"
            entry = (name,tvseries)

            mycursor.execute(sqlFormula,entry)
            self.mydb.commit()        

            print("Entered !!")

        except Exception as e:
            print(e)    

    

