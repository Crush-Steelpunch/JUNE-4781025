import db_functionquery

# Drop the table if it exists
sqlStr="""
IF EXISTS(
SELECT TABLE_NAME,TABLE_SCHEMA
FROM INFORMATION_SCHEMA.TABLES
WHERE TABLE_NAME = 'PeopleTable'
AND TABLE_SCHEMA = 'dbo')
BEGIN
DROP TABLE PeopleTable
END
"""
# Example Student Table SQL
StudentTable="""CREATE TABLE Student (
StudentID int NOT NULL,
FirstName nvarchar(40) NOT NULL,
Surname nvarchar(30) NULL,
Course nvarchar(30) NULL,
City nvarchar(15) NULL)"""


retval = db_functionquery.dbquery(sqlStr)
print('Dropped the People Table returned', retval)


createtablevar = "CREATE TABLE PeopleTable (ID INT PRIMARY KEY, Name VARCHAR(50) NOT NULL, AGE INT, Alive BIT NOT NULL)"
# NOTE BOOL is not SQL Server so I used BIT

retval = db_functionquery.dbquery(createtablevar)
print('Create the People Table returned', retval)


insertquery = [
    "INSERT INTO PeopleTable(ID,Name,Age,Alive) VALUES (1,'Leon',50,1)",
    "INSERT INTO PeopleTable(ID,Name,Alive) VALUES (2,'Jane',1)",
    "INSERT INTO PeopleTable(ID,Name,Age,Alive) VALUES (3,'Wasim',21,1)",
    "INSERT INTO PeopleTable(ID,Name,Alive) VALUES (4,'Beethoven',0)",
    "INSERT INTO PeopleTable(ID,Name,Age,Alive) VALUES (3,'Lassie',45,1)"
]
for row in insertquery:
    retval = db_functionquery.dbquery(row)
    print('Inserted',row,retval)

selectquery = "SELECT * FROM PeopleTable"

selquery = db_functionquery.dbquery(selectquery)
for selrow in selquery:
    print(selrow)