Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating,

altering, and deleting schemas

Any user can create schemas and alter or drop schemas they own.

You can perform the following actions:

- To create a schema, use the [CREATE SCHEMA](r_CREATE_SCHEMA.md "r_CREATE_SCHEMA.md") command.
- To change the owner of a schema, use the [ALTER SCHEMA](r_ALTER_SCHEMA.md "r_ALTER_SCHEMA.md") command.
- To delete a schema and its objects, use the [DROP SCHEMA](r_DROP_SCHEMA.md "r_DROP_SCHEMA.md") command.
- To create a table within a schema, create the table with the format
  _schema_name.table_name_.
  To view a list of all schemas, query the PG_NAMESPACE system catalog table:

```
select * from pg_namespace;
```

To view a list of tables that belong to a schema, query the PG_TABLE_DEF system
catalog table. For example, the following query returns a list of tables in the
PG_CATALOG schema.

```
select distinct(tablename) from pg_table_def
where schemaname = 'pg_catalog';
```
