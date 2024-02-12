import mysql.connector
mybb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="root",
                             database="tender_management_system")
cursor=mybb.cursor()

while True:

    tender_Id=int(input("Enter tender_Id:"))
    name=input("Enter name:")
    discription=input("Enter discription:")
    quantity=int(input("Enter quantity"))

    query="insert into item_id(tender_Id,name,discription,quantity) values(%s,%s,%s,%s)"
    cursor.execute(query,(tender_Id,name,discription,quantity))
    
    mybb.commit()
    
    choice = input("1 -> Enter more\n2 -> Exit\nEnter choice: ")
    if choice == '2':
        break