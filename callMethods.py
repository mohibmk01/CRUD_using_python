import mysql.connector
from psycopg2 import OperationalError
import dbconnection
import view
import sys



conn=dbconnection.con

def viewData(conn):
    con=conn
    cur=con.cursor()
    try:
        sql="select * from employee"
        cur.execute(sql)
        result=cur.fetchall()
        for x in result:
            print(x)
        
        dbconnection.con.commit()
    
        inp=input("Do you want return main menu (y/n) : ")
        if inp == "y":
            view.terminalView()
        else:
            dbconnection.con.close()
            sys.exit(1)
    except OperationalError as e:
            print(f"Error : {e}")
    
    
    
def insertData(conn):
    con=conn
    id=input("Enter id : ")
    name=input("Enter name : ")
    gender=input("Enter gender : ")
    mobile=input("Enter mobile : ")
    salary=int(input("Enter salary : "))
    age=input("Enter age : ")
    email=input("Enter email : ")
    try:
        sql="insert into employee values (%s,%s,%s,%s,%s,%s,%s)"
        val=(id,name,gender,mobile,salary,age,email)
        cur=con.cursor()
        cur.execute(sql,val)
        dbconnection.con.commit()
        print(cur.rowcount," details inserted successfully !!!")
        
        inp=input("Do you want return main menu (y/n) : ")
        if inp == "y":
            view.terminalView()
        else:
            dbconnection.con.close()
            sys.exit(1)
    except OperationalError as e:
            print(f"Error : {e}")
            
            
            
def updateData(conn):
    con=conn
    cur=con.cursor()
    inp=input("what you want to update :- \n 1.firstname\t2.gender\t3.mobile.\t4.salary\t5.age\t6.email\n enter your choice : ")
    choice = {
        "1":"name",
        "2":"gender",
        "3":"mobile",
        "4":"salary",
        "5":"age",
        "6":"email"
    }
    if inp in choice:
        id=input("enter id : ")
        update=input(f"enter new {choice.get(inp)}: ")
        try:
            sql=f"update employee set {choice.get(inp)} = %s where id=%s"
            val=(update,id)
            cur.execute(sql,val)
            
            dbconnection.con.commit()
            print(cur.rowcount," details update successfully !!!")
            
            inp=input("Do you want return main menu (y/n) : ")
            if inp == "y":
                view.terminalView()
            else:
                dbconnection.con.close()
                sys.exit(1)
        except OperationalError as e:
            print(f"Error : {e}")
