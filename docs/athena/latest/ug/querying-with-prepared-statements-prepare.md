# PREPARE

Prepares a statement to be run at a later time. Prepared statements are saved
in the current workgroup with the name that you specify. The statement can
include parameters in place of literals to be replaced when the query is run.
Parameters to be replaced by values are denoted by question marks.

## Syntax

```
PREPARE `statement_name` FROM `statement`
```

The following table describes these parameters.

| Parameter        | Description                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------ |
| `statement_name` | The name of the statement to be prepared. The name must<br>be unique within the workgroup. |
| `statement`      | A `SELECT`, `CTAS`, or `INSERT<br>INTO` query.                                             |

## PREPARE examples

The following examples show the use of the `PREPARE` statement.
Question marks denote the values to be supplied by the `EXECUTE`
statement when the query is run.

```
PREPARE **my\_select1** FROM
SELECT * FROM nation
```

```
PREPARE **my\_select2** FROM
SELECT * FROM "my_database"."my_table" WHERE year = **?**
```

```
PREPARE **my\_select3** FROM
SELECT order FROM orders WHERE productid = **?** and quantity < **?**
```

```
PREPARE **my\_insert** FROM
INSERT INTO cities_usa (city, state)
SELECT city, state
FROM cities_world
WHERE country = **?**
```

```
PREPARE **my\_unload** FROM
UNLOAD (SELECT * FROM table1 WHERE productid < **?**)
TO 's3://amzn-s3-demo-bucket/'
WITH (format='PARQUET')
```
