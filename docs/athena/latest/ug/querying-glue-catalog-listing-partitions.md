# List partitions for a

specific table

You can use `SHOW PARTITIONS `table_name`` to list
the partitions for a specified table, as in the following example.

```
SHOW PARTITIONS cloudtrail_logs_test2
```

You can also use a `$partitions` metadata query to list the partition
numbers and partition values for a specific table.

###### Example– Querying the partitions for a table using the $partitions syntax

The following example query lists the partitions for the table
`cloudtrail_logs_test2` using the `$partitions`
syntax.

```
SELECT * FROM default."cloudtrail_logs_test2$partitions" ORDER BY partition_number
```

The following table shows sample results.

|     | table_catalog  | table_schema | table_name            | Year | Month | Day |
| --- | -------------- | ------------ | --------------------- | ---- | ----- | --- |
| 1   | awsdatacatalog | default      | cloudtrail_logs_test2 | 2020 | 08    | 10  |
| 2   | awsdatacatalog | default      | cloudtrail_logs_test2 | 2020 | 08    | 11  |
| 3   | awsdatacatalog | default      | cloudtrail_logs_test2 | 2020 | 08    | 12  |
