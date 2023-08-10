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
