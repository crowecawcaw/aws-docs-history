# Use query

parameters to provide dynamic values in SQL queries

Query parameters can be used to provide dynamic values in SQL queries.

In the following example, we pass a query parameter to the `WHERE` clause of
the query.

```
# How to use '--query-parameters' with ATHENA as a data store
%%sm_sql --metastore-id `athena-connection-name` --metastore-type GLUE_CONNECTION --query-parameters '{"parameters":{"name_var": "John Smith"}}'
SELECT * FROM my_db.my_schema.my_table WHERE name = (%(name_var)s);
```
