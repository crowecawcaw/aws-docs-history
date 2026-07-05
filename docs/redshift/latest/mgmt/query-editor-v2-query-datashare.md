Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Querying datashare objects

On the consumer cluster, you can query datashare objects using fully qualified
object names expressed with the three-part notation: database, schema, and name of
the object.

1. In the query editor v2 tree-view panel, choose the schema.
2. To view a table definition, choose a table.

The table columns and data types display. 3. To query a table, choose the table and use the context menu (right-click)
to choose **Select table**. 4. Query tables using SELECT commands. For example:

```
select top 10 * from test_db.public.event;
```
