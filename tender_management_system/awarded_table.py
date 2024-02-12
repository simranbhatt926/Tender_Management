import mysql.connector
import datetime  # Import the datetime module

# Connect to MySQL
myeb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tender_management_system"
)
cursor = myeb.cursor()

# Function to validate date format
def is_valid_date(date_str):
    try:
        # Attempt to parse the date
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

while True:
    # Input data
    contract_id = int(input("Enter contract_id: "))
    tenderid = int(input("Enter tenderid: "))
    supplier_id = int(input("Enter supplier_id: "))
    bid_id = int(input("Enter bid_id: "))
    awardedDate = input("Enter awardedDate (YYYY-MM-DD): ")

    # Validate date format
    if not is_valid_date(awardedDate):
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
        continue

    # SQL query to insert data
    query = "INSERT INTO awardedcontracts_table (contract_id, tenderid, supplier_id, bid_id, awardedDate) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (contract_id, tenderid, supplier_id, bid_id, awardedDate))
    myeb.commit()

    choice = input("1 -> Enter more\n2 -> Exit\nEnter choice: ")
    if choice == '2':
        break

# Close the cursor and MySQL connection
cursor.close()
myeb.close()
