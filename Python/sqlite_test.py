# Download and install the sqlite ODBC driver for your OS here
#
# <http://www.ch-werner.de/sqliteodbc/>
#
# Windows 10 & 11 will need the sqliteodbc_w64.exe one.
# the DATABASE=test.db will create a file of that name in your project directory

import pyodbc

def dbquery(statement):
    connectionString = r"DRIVER={SQLite3 ODBC Driver};SERVER=localhost;DATABASE=leonsqlite.db;Trusted_connection=yes"
    conn = pyodbc.connect(connectionString)
    cur = conn.cursor()
    
    try:
        if 'SELECT' in statement:
            result = cur.execute(statement).fetchall()
        else:
            cur.execute(statement)
            conn.commit()
            result = True
        conn.close()
        return result
    except:
        conn.close()
        return None

droptable = "DROP TABLE Student"

print("Dropping Table",dbquery(droptable))

createtable="""
CREATE TABLE Student (
StudentID int NOT NULL,
FirstName nvarchar(40) NOT NULL,
Surname nvarchar(30) NULL,
Course nvarchar(30) NULL,
City nvarchar(15) NULL)
"""

print("Creating Table:",dbquery(createtable))

students = [
    [1,'Leon','Robinson','Music','Salford'],
    [2,'Jane','Janesson','Physics','Helsinki'],
    [3,'Nur','Mohammed','DevOps','New York'],
    [4,'Jim','Bronkbroke','Corn Studies','Wigan']
    ]
for student in students:
    #breakpoint()
    insertstudents=f"INSERT INTO Student (StudentID,FirstName,Surname,Course,City) VALUES ({student[0]},'{student[1]}','{student[2]}','{student[3]}','{student[4]}')"
    print(f"Inserting {student}",dbquery(insertstudents))

selectstudents="SELECT * FROM Student ORDER BY StudentID DESC"
select = dbquery(selectstudents)
for i in select:
    print(i)