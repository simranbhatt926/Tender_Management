import mysql.connector
myab=mysql.connector.connect(host="localhost",
                             user="root",
                             password="root",
                             database="tender_management_system")

cursor = myab.cursor()

while True:
    
    tender_Id = int(input("enter tender_Id: "))
    title = input("enter title: ")
    tender_start = input("enter tender_start (YYYY-MM-DD): ")
    tender_end = input("enter tender_end (YYYY-MM-DD): ")
    discription = input("enter discription: ")

    query = "INSERT INTO tenders_table (tender_Id, title, tender_start, tender_end, discription) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (tender_Id, title, tender_start, tender_end, discription))

    myab.commit()

    choice = input("1 -> Enter more\n2 -> Exit\nEnter choice: ")
    if choice == '2':
        break