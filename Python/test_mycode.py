import myfunctions
import db_functionquery


def test_maxthreenumbers():
    assert myfunctions.maxthreenumbers(3,5,9) == 9

def test_reverseastring():
    assert myfunctions.reverseastring('aaabbb') == 'bbbaaa'

def test_isprime():
    assert myfunctions.testisprime(7) == True
    assert myfunctions.testisprime(9) == False
    assert myfunctions.testisprime(11) == True
    assert myfunctions.testisprime(0) == False

def test_dbselect():
    rows =  db_functionquery.dbquery('SELECT * from PeopleTable') 
    assert rows[0][0] == 1
    assert rows[0][1] == 'Leon'
    assert rows[0][2] == 50
    assert rows[0][3] == True
def test_dbinsert():
    assert db_functionquery.dbquery("INSERT INTO PeopleTable (ID,Name,Age,Alive) VALUES (10,'jimjim',1,1)") == True

def test_dbremove():
    assert db_functionquery.dbquery('DELETE FROM PeopleTable WHERE ID=10') == True
