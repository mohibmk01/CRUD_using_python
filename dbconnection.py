import mysql.connector

DB_NAME = "Employee"
DB_USER = "root"
DB_PASS = "root"
DB_HOST = "localhost"


def dbconnect(db_name,db_user,db_pwd,db_host):
    try:
        connection = mysql.connector.connect(
            database=db_name,
            user=db_user,
            password=db_pwd,
            host=db_host,
          
            
        )
        print("connection established !!!")
        return connection 
    except OperationalError as e:
        print(f"error : {e}")
        return None

con=dbconnect(DB_NAME,DB_USER,DB_PASS,DB_HOST)