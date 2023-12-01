import callMethods
import dbconnection
import time


    
def terminalView():
    print("***  WELCOME ***\n1.View Data\n2.Insert Data\n3.Update Data\n4.Delete Data\n")
    
    choice=input("Enter choice : ")

    if choice == "1":
        callMethods.viewData(dbconnection.con)
        
    elif choice == "2":
        callMethods.insertData(dbconnection.con)
    elif choice == "3":
        callMethods.updateData(dbconnection.con)   
    else:
        print("Invalid Input")
        time.sleep(2)
        terminalView()
    11
if __name__ == "__main__":
    terminalView()

  