# SQL 

## Organised

- Database
  - Tables
    - Columns: Describe what data we have and it's type
    - Row: Make up our data

## SELECT  - Read information from tables

**Example Table**
PeopleTable

| ID (INTEGER) | Name (VARCHAR) |Age (NUMBER) | Alive (BOOLEAN)|
|----------|---------------|-------------|-------------|
|  1       |  Leon         | 50          | True        |
|  2       |  Bach         | 350         | False       |
|  3       |   Pope        | 72          | True        |


```SQL
SELECT <COLUMNS> FROM <TABLE>
```

```SQL
SELECT Name FROM PeopleTable

| Name |
|------|
| Leon |
| Bach |
| Pope |
```

## Filtering


`SELECT <COL> FROM <TABLE> WHERE <Filtering-Terms>`

```SQL
SELECT Names,Age FROM PeopleTable WHERE Alive=True`
```

- BETWEEN
- LIKE
- IN 

## ORDER BY -- sort by fields


`SELECT <COL> FROM <TABLE> WHERE <Filtering-Terms> ORDER BY <COL> ASC`


```SQL
SELECT Names,Age FROM PeopleTable WHERE Alive=True ORDER BY Age DESC`
```


## INSERT statment

`INSERT INTO <table> (<column_names>,...) VALUES (<values>,...)`

``SQL
INSERT INTO PeopleTable (ID,Name,Age,Alive) VALUES (4,"Jane",40,True)
```


## UPDATE statment

`UPDATE <table> SET <col_name>=<data>,... WHERE <filter query>`


## CREATE TABLE statement

`CREATE TABLE <tablename> (<col_name> <data_type> <constraints>,...)`

| Datatype | Description |
|----------|-------------|
| VARCHAR(<size>)  |  String data  |
| INT(<size>)  |  Integer Data |
| FLOAT(<size>) | Floating point numbers |
| BOOL / BOOLEAN   | Boolean Data |
| DATE | Date `YYYY-MM-DD` |
| TIME | Time `hh:mm:ss` |
| DATETIME  | Date and Time `YYYY-MM-DD hh:mm:ss` |
 



```SQL
CREATE TABLE PeopleTable(
    ID INT PRIMARY KEY,
    Name VARCHAR(50),
    AGE INT,
    Alive BOOL NOT NULL
)
```