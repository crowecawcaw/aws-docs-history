# List the columns

that specific tables have in common

You can list the columns that specific tables in a database have in common.

- Use the syntax `SELECT column_name FROM
information_schema.columns`.
- For the `WHERE` clause, use the syntax `WHERE table_name IN
('table1', 'table2')`.

###### Example– Listing common columns for two tables in the same database

The following example query lists the columns that the tables `table1`
and `table2` have in common.

```
SELECT column_name
FROM information_schema.columns
WHERE table_name IN ('table1', 'table2')
GROUP BY column_name
HAVING COUNT(*) > 1;
```
