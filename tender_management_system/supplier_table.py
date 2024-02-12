import mysql.connector
myab=mysql.connector.connect(host="localhost",
                             user="root",
                             password="root",
                             database="tender_management_system")
cursor=myab.cursor()

while True:

    supplier_Id=int(input("Enter supplier_Id:"))
    name=input("Enter name:")
    contact_info=int(input("Enter contact_info:"))

    query="insert into suppliers_table(supplier_Id,name,contact_info) values(%s,%s,%s)"
    cursor.execute(query,( supplier_Id,name,contact_info))

    myab.commit()
    
    choice = input("1 -> Enter more\n2 -> Exit\nEnter choice: ")
    if choice == '2':
        break