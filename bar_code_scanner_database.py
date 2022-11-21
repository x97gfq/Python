#hopefully you opened the folder (and not the file directly)
#run "python3 -m venv .venv" to create the python virtual environment

#you should see "venv" in the bottom right, but if not, run Activate.ps1 manualy:
# cd ./.venv/Scripts
# ./Activate.ps1
# then under File -> Add folder to Workspace
#

import mysql.connector
#to import this library, type "pip install mysql.connector" in Terminal (in your .venv)

import geocoder
#to import this library, type "pip install geocoder"

#get the latitude and longtiude from the geocoder library
g = geocoder.ip('me')
latitude = g.latlng[0]
longitude = g.latlng[1]

#add folder to workspace (under the file menu) if you're having trouble with your imports

#ask for user input
barcode = input("Scan a barcode (type 'exit' when done):")
while (barcode != "exit"):
    print("I got: " + barcode)

    #establishing the connection
    conn = mysql.connector.connect(user='root', password='mysql', host='127.0.0.1', database='barcodescanner')

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

    # Closing the connection
    conn.close()

    #ask for user input
    barcode = input("Scan a barcode (type 'exit' when done):")

print("kthx")