import pyodbc  # We need the module to connecto the db
import db_functionquery
def dbinsert(statement):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    try:
        cur.execute(statement)
    except:
        print('error, cannot add for some reason')
    conn.commit()
    conn.close()


insertquery = "INSERT INTO company (company_no,company_name,tel,county,post_code) VALUES (5000,'Leon Corp','01101 110 001','Gtr Manchester','M1 1AA')"

dbinsert(insertquery)


selectquery = "SELECT * FROM company"
rows = db_functionquery.dbquery(selectquery)
for i in rows:
    print(i)
