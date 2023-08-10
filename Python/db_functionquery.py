import pyodbc  # We need the module to connecto the db
def dbquery(statement):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    result = cur.execute(statement).fetchall()
    conn.close()
    return result
