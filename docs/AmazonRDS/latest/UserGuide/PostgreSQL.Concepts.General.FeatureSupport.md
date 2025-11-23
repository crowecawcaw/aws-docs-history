# Custom data

types and enumerations with RDS for PostgreSQL

PostgreSQL supports creating custom data types and working with enumerations. For
more information about creating and working with enumerations and other data types,
see [Enumerated
types](https://www.postgresql.org/docs/14/datatype-enum.html "https://www.postgresql.org/docs/14/datatype-enum.html") in the PostgreSQL documentation.

The following is an example of creating a type as an enumeration and then
inserting values into a table.

```
`CREATE TYPE rainbow AS ENUM ('red', 'orange', 'yellow', 'green', 'blue', 'purple');`
`CREATE TYPE`
`CREATE TABLE t1 (colors rainbow);`
`CREATE TABLE`
`INSERT INTO t1 VALUES ('red'), ( 'orange');`
`INSERT 0 2`
`SELECT * from t1;`
`colors
--------
red
orange
(2 rows)`
`postgres=>` `ALTER TYPE rainbow RENAME VALUE 'red' TO 'crimson';`
`ALTER TYPE`
`postgres=>` `SELECT * from t1;`
`colors
---------
crimson
orange
(2 rows)`
```
