Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Materialized view queries

You can use a materialized view in any SQL query by referencing the materialized view
name as the data source, like a table or standard view.

When a query accesses a materialized view, it sees only the data that is stored in the
materialized view as of its most recent refresh. Thus, the query might not see all the
latest changes from corresponding base tables of the materialized view.

If other users want to query the materialized view, the owner of the materialized
view grants the SELECT permission to those users. The other users don't need to have the
SELECT permission on the underlying base tables. The owner of the materialized view can
also revoke the SELECT permission from other users to prevent them from querying the
materialized view. Note that the other users still need the USAGE permission on the
schemas that contain the base tables of the materialized view.

If the owner of the materialized view no longer has the local SELECT permission on the
underlying base tables:

- The owner can no longer query the materialized view.
- Other users who have the SELECT permission on the materialized view can no longer query the
  materialized view.
  This is limited to local permissions. Changes in permissions managed by Lake Formation are not verified
  on querying the materialized view. This means that if an underlying base table is managed by Lake Formation and select permissions
  on the table are revoked in Lake Formation, you can still query the materialized view.

The following example queries the `tickets_mv` materialized view. For more
information on the SQL command used to create a materialized view, see [CREATE MATERIALIZED VIEW](materialized-view-create-sql-command.md "materialized-view-create-sql-command.md").

```
SELECT sold
FROM tickets_mv
WHERE catgroup = 'Concerts';
```

Because the query results are precomputed, there's no need to access the underlying
tables (`category`, `event`, and `sales`). Amazon Redshift can
return the results directly from `tickets_mv`.
