import mysql.connector
#to import this library, type "pip install mysql.connector" in Terminal (in your .venv)

import geocoder
#to import this library, type "pip install geocoder"

#get the latitude and longtiude from the geocoder library
g = geocoder.ip('me')
latitude = g.latlng[0]
longitude = g.latlng[1]

#ask for user input
barcode = input("Scan a barcode (type 'exit' when done):")
while (barcode != "exit"):
    print("I got: " + barcode)

    #establishing the connection
    conn = mysql.connector.connect(user='root', password='mysql', host='127.0.0.1', database='barcodescanner')

    #check if barcode exists in the master list
    checkcursor = conn.cursor()

    checkcursor.execute("SELECT barcode, details FROM barcode_master WHERE barcode = '" + barcode + "';")

    masterlist_item = checkcursor.fetchone()

    if (masterlist_item is not None):
        print("Item scanned: " + masterlist_item[1])

        #Creating a cursor object using the cursor() method
        cursor = conn.cursor()
        
        # Preparing SQL query to INSERT a record into the database.
        sql = """INSERT INTO barcode_scanned(barcode,latitude,longitude) 
                VALUES('" + barcode +"','" + str(latitude) + "','" + str(longitude) + "');"""

        try:
            # Executing the SQL command
            cursor.execute(sql)

            # Commit your changes in the database
            conn.commit()
        except:
            # Rolling back in case of error
            conn.rollback()
    else:
        print("Item not found in masterlist.")

    # Closing the connection
    conn.close()

    #ask for user input
    barcode = input("Scan a barcode (type 'exit' when done):")

print("kthx")