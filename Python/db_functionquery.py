import pyodbc  # We need the module to connecto the db
def dbquery(statement):
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()

    try:
        if statement.startswith('SELECT'):
            result = cur.execute(statement).fetchall()
        else:
            cur.execute(statement)
            conn.commit()
            result = True
        conn.close()
        return result
    except Exception as e:
        print(e)
        conn.close()
        return None


