# Considerations for working with Amazon Aurora DSQL

Consider the following behaviors when you work with Amazon Aurora DSQL. For more information about
PostgreSQL compatibility and support, see [SQL feature compatibility in
Aurora DSQL](working-with-postgresql-compatibility.md "working-with-postgresql-compatibility.md"). For quotas and limits, see [Cluster quotas and database limits in Amazon Aurora DSQL](CHAP_quotas.md "CHAP_quotas.md").

- Aurora DSQL doesn't complete `COUNT(*)` operations before transaction timeout for large tables.
  To retrieve table row count from the system catalog, see [Using systems tables
  and commands in Aurora DSQL](working-with-systems-tables.md "working-with-systems-tables.md").
- Drivers calling `PG_PREPARED_STATEMENTS` might provide an inconsistent view
  of cached prepared statements for the cluster. You might see more than the expected number
  of prepared statements per connection for the same cluster and IAM role. Aurora DSQL doesn't
  preserve statement names that you prepare.
- In rare multi-Region linked-cluster impairment scenarios, it might take longer than
  expected for transaction commit availability to resume. In general, automated cluster
  recovery operations can result in transient concurrency control or connection errors. In
  most cases, you will only see the effects for a percentage of your workload. When you see
  these transit errors, retry your transaction or reconnect with your client.
- Some SQL clients, such as Datagrip, make expansive calls to system metadata to populate
  schema information. Aurora DSQL doesn't support all of this information and returns errors. This
  issue doesn't affect SQL query functionality, but it might affect schema display.
- The admin role has a set of permissions related to database management tasks. By
  default, these permissions don't extend to objects that other users create. The admin role
  can't grant or revoke permissions on these user-created objects to other users. The admin
  user can grant itself any other role to get the necessary permissions on these
  objects.
