# List or search columns for

a specified table or view

You can list all columns for a table, all columns for a view, or search for a column
by name in a specified database and table.

To list the columns, use a `SELECT *` query. In the `FROM`
clause, specify `information_schema.columns`. In the `WHERE`
clause, use `table_schema='`database_name`'` to
specify the database and `table_name =
 '`table_name`'` to specify the table or view that has
the columns that you want to list.

###### Example – Listing all columns for a specified table

The following example query lists all columns for the table
`rdspostgresqldb1_public_account`.

```
SELECT *
FROM   information_schema.columns
WHERE  table_schema = 'rdspostgresql'
       AND table_name = 'rdspostgresqldb1_public_account'
```

The following table shows sample results.

|     | table_catalog  | table_schema  | table_name                      | column_name | ordinal_position | column_default | is_nullable | data_type | comment | extra_info |
| --- | -------------- | ------------- | ------------------------------- | ----------- | ---------------- | -------------- | ----------- | --------- | ------- | ---------- |
| 1   | awsdatacatalog | rdspostgresql | rdspostgresqldb1_public_account | password    | 1                |                | YES         | varchar   |         |            |
| 2   | awsdatacatalog | rdspostgresql | rdspostgresqldb1_public_account | user_id     | 2                |                | YES         | integer   |         |            |
| 3   | awsdatacatalog | rdspostgresql | rdspostgresqldb1_public_account | created_on  | 3                |                | YES         | timestamp |         |            |
| 4   | awsdatacatalog | rdspostgresql | rdspostgresqldb1_public_account | last_login  | 4                |                | YES         | timestamp |         |            |
| 5   | awsdatacatalog | rdspostgresql | rdspostgresqldb1_public_account | email       | 5                |                | YES         | varchar   |         |            |
| 6   | awsdatacatalog | rdspostgresql | rdspostgresqldb1_public_account | username    | 6                |                | YES         | varchar   |         |            |

###### Example – Listing the columns for a specified view

The following example query lists all the columns in the `default`
database for the view `arrayview`.

```
SELECT *
FROM   information_schema.columns
WHERE  table_schema = 'default'
       AND table_name = 'arrayview'
```

The following table shows sample results.

|     | table_catalog  | table_schema | table_name | column_name     | ordinal_position | column_default | is_nullable | data_type      | comment | extra_info |
| --- | -------------- | ------------ | ---------- | --------------- | ---------------- | -------------- | ----------- | -------------- | ------- | ---------- |
| 1   | awsdatacatalog | default      | arrayview  | searchdate      | 1                |                | YES         | varchar        |         |            |
| 2   | awsdatacatalog | default      | arrayview  | sid             | 2                |                | YES         | varchar        |         |            |
| 3   | awsdatacatalog | default      | arrayview  | btid            | 3                |                | YES         | varchar        |         |            |
| 4   | awsdatacatalog | default      | arrayview  | p               | 4                |                | YES         | varchar        |         |            |
| 5   | awsdatacatalog | default      | arrayview  | infantprice     | 5                |                | YES         | varchar        |         |            |
| 6   | awsdatacatalog | default      | arrayview  | sump            | 6                |                | YES         | varchar        |         |            |
| 7   | awsdatacatalog | default      | arrayview  | journeymaparray | 7                |                | YES         | array(varchar) |         |            |

###### Example – Searching for a column by name in a specified database and table

The following example query searches for metadata for the `sid` column
in the `arrayview` view of the `default` database.

```
SELECT *
FROM   information_schema.columns
WHERE  table_schema = 'default'
       AND table_name = 'arrayview'
       AND column_name='sid'
```

The following table shows a sample result.

|     | table_catalog  | table_schema | table_name | column_name | ordinal_position | column_default | is_nullable | data_type | comment | extra_info |
| --- | -------------- | ------------ | ---------- | ----------- | ---------------- | -------------- | ----------- | --------- | ------- | ---------- |
| 1   | awsdatacatalog | default      | arrayview  | sid         | 2                |                | YES         | varchar   |         |            |
