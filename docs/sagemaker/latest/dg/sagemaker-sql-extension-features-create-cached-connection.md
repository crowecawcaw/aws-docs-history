# Create cached

connections

You can create cached connections by specifying a connection name in the
`--connection-name` parameter of your connection string. This is particularly
useful when multiple connection properties are overridden for a specific use case, and
there's a need to reuse the same properties without retyping them.

For example, the code below saves an Athena connection with an overridden schema
connection property using the name `--connection-name
 my_athena_conn_with_schema`, and then reuses it in another cell:

```
%%sm_sql --connection-name my_athena_conn_with_schema --connection-properties '{"schema_name": "sm-sql-private-beta-db"}' --metastore-id sm-sql-private-beta-athena-connection --metastore-type GLUE_CONNECTION
SELECT * FROM "covid_table" LIMIT 2
```

```
%%sm_sql --connection-name my_athena_conn_with_schema
SELECT * FROM "covid_table" LIMIT 2
```
