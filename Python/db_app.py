import db_functionquery

resultvar = db_functionquery.dbquery("SELECT company_no,company_name FROM company WHERE county='London'")

for i in resultvar:
    print(i)


showstaff = db_functionquery.dbquery("SELECT * FROM salesperson")
for i in showstaff:
    print(i)

insertquery = "INSERT INTO company (company_no,company_name,tel,county,post_code) VALUES (5000,'Leon Corp','01101 110 001','Gtr Manchester','M1 1AA')"

query = db_functionquery.dbquery(insertquery)
if query == None:
    print('insert failed')
else:
    print('insert succeeded')

resultvar = db_functionquery.dbquery("SELECT * FROM company")
for i in resultvar:
    print(i)

showstaff = db_functionquery.dbquery("SELECT * FROM sale")
for i in showstaff:
    print(i)