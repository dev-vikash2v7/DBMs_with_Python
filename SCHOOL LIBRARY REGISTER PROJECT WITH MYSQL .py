print(25*"*")
print(6*"*","SCHOOL LIBRARY RECORDS","*"*6)
print(25*"*")

import mysql.connector as sqltor,sys

a=True

while a:
    
    password=input('ENTER YOUR PASSWORD : ')
    data=input('ENTER YOUR DATABASE :')
    
    mycon=sqltor.connect(host='localhost',user='root',passwd=password,database=data)
    
    if mycon.is_connected():
        print('SUCCESSFULLY CONNECTED :)')
        a=False
            
    else:
        print('NOT CONNECTD :(')
        
cursor=mycon.cursor()

try:
    cursor.execute('create table library (Student_Name varchar(30), Class integer, Roll_NO integer, Issue_Date date,Book_Name varchar(30),Book_NO integer,Publisher varchar(30))')
    
except Exception:
    pass

#main menu
def menu():
    print("\n")
    entry=int(input('''PRESS
    
    1-  ADD RECORD
    2-  DISPLAY RECORDS
    3-  UPDATE RECORD
    4-  DELETE RECORD
    5-  DELETE ALL RECORD
    6-  EXIT

    ENTER YOUR OPTION : '''))
    
    
    if entry==1:
        add()
        
    elif entry==2:
        display()
        
    elif entry==3:
        update()
        
    elif entry==4:
        delete()
        
    elif entry==5:
        delete_all()
        
    elif entry==6:
        print('THANK YOU')
        sys.exit()

    else:
        print("INVALID ENTRY ! TRY AGAIN.")
        menu()

        
                
#to add data                                
def add():
    
    print('ENTER DEATILS OF STUDENT :\n')
    try:
        name=input('ENTER STUDENT NAME :')
        claas=int(input('ENTER CLASS :'))
        roll=int(input('ENTER ROLL NO. :'))
        date=input('ENTER DATE OF ISSUE :')
        
        print('\n')
        
        book=input('ENTER BOOK NAME :')
        no=int(input('ENTER BOOK NO. :'))
        publisher=input('ENTER PUBLISHER NAME :')
                        
            
        cursor.execute(f'insert into library(Student_Name,Class,Roll_NO,Date_Of_Issue,Book_Name,Book_NO,Publisher) values("{name}","{claas}","{roll}","{date}","{book}","{no}","{publisher}");')  
        mycon.commit()
        
        print("RECORDS ADDED :)")
        
    except Exception as e:
        print(e)
        print("TRY AGAIN !")
        add()
    menu()


#show records
def display():
    print('****SHOWING RECORDS****')
    print('\n')
    
    cursor.execute('select*from library')
    data=cursor.fetchall()
    
    for row in data:
        print(row)
    menu()

        
#update record                        
def update():
    print('***UPDATE RECORD***')
    print('\n')
    
    roll=int(input('ENTER ROLL NO TO BE UPDATED :'))
    
    try:
        name=input('Enter Updated Name :')
        date=input('Enter Updated Issue Date :')
        book=input('Enter Book Name :')
        no=int(input('Enter Book No. :'))
        publisher=input('Enter Updated Publisher Name :')
        
        
        cursor.execute(f'update library set Student_Name="{name}" where Roll_NO="{roll}"; ')
        cursor.execute(f'update library set Date_Of_Issue="{date}" where Roll_NO="{roll}"; ')
        cursor.execute(f'update library set Book_Name="{book}" where Roll_NO="{roll}";')
        cursor.execute(f'update library set Book_NO="{no}" where Roll_NO="{roll}"; ')
        cursor.execute(f'update library set Publisher="{publisher}" where Roll_NO="{roll}"; ')
        
        print("*****RECORDS UPDATED******")
        
        mycon.commit()
        
    except Exception as e:
        print(e)
        print("TRY AGAIN")
        update()
    menu()    

                                                                            #delete record  
def delete():
    roll=int(input('ENTER ROLL NO. TO BE DELETED :'))
    try:
        cursor.execute(f'delete from library where Roll_NO="{roll}";')
        mycon.commit()
        print('(: SUCCESSFULLY DELETED (:')
    except Exception as e:
        print(e)
        print("TRY AGAIN")
        delete()
    menu()

    
#delete all            
def delete_all():
    cursor.execute('delete from library')
    print('(: SUCCESSFULLY DELETED (:')
    mycon.commit()
    menu()
    

menu()

    
    
    









