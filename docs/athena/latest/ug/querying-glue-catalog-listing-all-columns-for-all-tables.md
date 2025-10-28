# List all

columns for all tables

You can list all columns for all tables in `AwsDataCatalog` or for all
tables in a specific database in `AwsDataCatalog`.

- To list all columns for all databases in `AwsDataCatalog`, use the
  query `SELECT * FROM information_schema.columns`.
- To restrict the results to a specific database, use
  `table_schema='`database_name`'` in
  the `WHERE` clause.

###### Example – Listing all columns for all tables in a specific database

The following example query lists all columns for all tables in the database
`webdata`.

```
SELECT * FROM information_schema.columns WHERE table_schema = 'webdata'
```
