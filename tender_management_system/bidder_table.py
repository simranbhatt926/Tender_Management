import mysql.connector

# Connect to MySQL
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tender_management_system"
)
cursor = mydb.cursor()

while True:
    bidder_Id = int(input("Enter bidder_Id: "))
    bidder_name = input("Enter bidder_name: ")
    contact_details = int(input("Enter contact_details: "))
    bid_amount = int(input("Enter bid_amount: "))
    bid_date = input("Enter bid_date (YY-MM-DD): ")
    bid_id = int(input("Enter bid_id: "))

    query = "INSERT INTO bidders_table (bidder_Id, bidder_name, contact_details, bid_amount, bid_date, bid_id) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (bidder_Id, bidder_name, contact_details, bid_amount, bid_date, bid_id))
    mydb.commit()

    choice = input("1 -> Enter more\n2 -> Exit\nEnter choice: ")
    if choice == '2':
        break

# Close the cursor and database connection
cursor.close()
mydb.close()

