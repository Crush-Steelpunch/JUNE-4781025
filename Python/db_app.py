import db_functionquery

resultvar = db_functionquery.dbquery("SELECT company_no,company_name FROM company WHERE county='London'")

for i in resultvar:
    print(i)
