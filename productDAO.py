 
# Python Database Access Object
# This programe perfoms CRUD operation on MySQL datase
# using python to control database

import mysql.connector
import dbconfig as cfg

# Define an Object class
class CoffeeDAO:

    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""

    # Initialize the class
    def __init__(self):
        # reading from config file
        self.host = cfg.mysql['host']
        self.user = cfg.mysql['user']
        self.password = cfg.mysql['password']
        self.database = cfg.mysql['database']
        self.table = cfg.mysql['table']
        self.connection = None
        self.cursor = None
    
    # Function to define the cursor to interact with the database
    def getCursor(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password,
            database = self.database,
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    # Function to create a new record in the database
    def create(self, data):
        cursor = self.getCursor()
        sql =  f"insert into {self.table} (CoffeeName,Origin,Variety,Roast,Price) values (%s,%s,%s,%s,%s)"
        values = [
            data["CoffeeName"],
            data["Origin"],
            data["Variety"],
            data["Roast"],
            data["Price"]
        ]
        cursor.execute(sql,values)
        
        self.connection.commit()
        self.closeAll
        return cursor.lastrowid
              
    # Function to get all records from the database rows
    def getAll(self):
        cursor = self.getCursor()
        sql = f"select * from {self.table}"
        cursor.execute(sql)
        results = cursor.fetchall()
        returnArray = []
        for result in results:
            resultAsDict= self.convertToDict(result)
            returnArray.append(resultAsDict)
        self.closeAll()
        return returnArray

    # Function to find a specific record by id
    def findById(self,id):
        cursor = self.getCursor()
        sql = f"select * from {self.table} where id = %s"
        values = (id,)
        cursor.execute(sql,values)
        result = cursor.fetchone()
        self.closeAll()
        return self.convertToDict(result)

    # Function to update existing record
    def update(self,data):
        cursor= self.getCursor()
        sql = f"update {self.table} set CoffeeName = %s, Origin = %s, Variety = %s, Roast = %s, Price = %s where id = %s;"
        values = [          
            data["CoffeeName"],
            data["Origin"],
            data["Variety"],
            data["Roast"],
            data["Price"],
            data["id"]          
        ]
        cursor.execute(sql,values)
        self.connection.commit()
        self.closeAll()
        return data

    # Function to delete a record
    def delete(self,id):
        cursor = self.getCursor()
        sql = f"delete from {self.table} where id = %s"
        values = (id,)

        cursor.execute(sql,values)

        self.connection.commit()
        print("Deletion complete")
        self.closeAll
        return {}

    # Function to convert a record to a dict object
    def convertToDict(self,result):
        colnames = ["id","CoffeeName","Origin","Variety","Roast","Price"]

        coffee = {}
        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                coffee[colName]= value
            return coffee

    # This function creates a table. It can be used, although a sql query was written to load all data into the table
    def createTable(self):
            cursor = self.getCursor()
            sql = f"create table {self.table} (id int AUTO_INCREMENT NOT NULL PRIMARY KEY, CoffeeName varchar(250), Origin varchar(250), Variety varchar (250), Roast varchar(250), Price float)"
            cursor.execute(sql)

            self.connection.commit()
            self.closeAll()
    # Function to create a database. It can be used, although a sql query was written to create a database and load all data into the table
    def createDatabase(self):
        self.connection = mysql.connector.connect(
            host = self.host,
            user = self.user,
            password = self.password   
        )
        self.cursor = self.connection.cursor()
        sql= f"create database {self.database}"
        self.cursor.execute(sql)
        self.connection.commit()
        self.closeAll()

# creates a new class
coffeeDAO = CoffeeDAO()    

if __name__== "__main__":

    #coffeeDAO.createDatabase()
    #coffeeDAO.createTable()
    print("The Coffee Shop")
