import pyodbc  # We need the module to connecto the db
import db_functionquery
def dbupdate(statement):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    try:
        cur.execute(statement)
    except:
        print('error, cannot update for some reason')
    conn.commit()
    conn.close()

updatequery = "UPDATE company SET county='Wigan' WHERE company_no=2000"

selectquery = "SELECT * from company WHERE company_no=2000"
selectquery1 = "SELECT * from company"
# Check the WHERE clause will only change one line
rows = db_functionquery.dbquery(selectquery)
for i in rows:
    print(i)
# Update the row
dbupdate(updatequery)
# Show the database
rows = db_functionquery.dbquery(selectquery1)
for i in rows:
    print(i)
