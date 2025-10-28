# Table not found when using

Athena with Amazon Quick Sight

You can receive a "`table not found`" error if the tables in an
analysis are missing from the Athena data source.

In the Athena console ([https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home")), check for your table under the
corresponding schema. You can recreate the table in Athena and then create a new
dataset in Amazon Quick Sight on that table. To investigate how the table was lost in the first
place, you can use the Athena console to check the query history. Doing this helps
you find the queries that dropped the table.

If this error happened when you were editing a custom SQL query in preview, verify
that the name of the table in the query, and check for any other syntax errors.
Amazon Quick Sight can't infer the schema from the query. The schema must be specified in the
query.

For example, the following statement works.

```
select from my_schema.my_table
```

The following statement fails because it's missing the schema.

```
select from my_table
```

If you still have the issue, verify that your tables, columns, and queries comply
with Athena requirements. For more information, see [Names
for Tables, Databases, and Columns](../../../athena/latest/ug/tables-databases-columns-names.md "../../../athena/latest/ug/tables-databases-columns-names.md") and [Troubleshooting](../../../athena/latest/ug/troubleshooting.md "../../../athena/latest/ug/troubleshooting.md") in the _Athena User
Guide_.
