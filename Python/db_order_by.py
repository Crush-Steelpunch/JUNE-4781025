import pyodbc  # We need the module to connecto the db
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
conn = pyodbc.connect(connectionString)
cur = conn.cursor()

# Filtering SELECT statments 
result = cur.execute("SELECT company_no,company_name FROM company WHERE county='London'").fetchall()
result1 = cur.execute("SELECT company_no,company_name FROM company WHERE company_no < 2005 ORDER BY company_no DESC").fetchall()
result2 = cur.execute("SELECT company_no,company_name FROM company WHERE company_no BETWEEN 1500 AND 3500 ORDER BY county ASC").fetchall()
result3 = cur.execute("SELECT company_no,company_name FROM company WHERE company_name LIKE '%PLC'").fetchall()
cur.close()

for i in result:
    print(i)
print('---')
for i in result1:
    print(i)
print('---')
for i in result2:
    print(i)
print('---')
for i in result3:
    print(i)
print('---')