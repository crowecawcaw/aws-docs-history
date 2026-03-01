# Considerations for working with Amazon Aurora DSQL

Consider the following behaviors when you work with Amazon Aurora DSQL. For more information about
PostgreSQL compatibility and support, see [SQL feature compatibility in Aurora DSQL](working-with-postgresql-compatibility.md "working-with-postgresql-compatibility.md"). For quotas and limits, see [Cluster quotas and database limits in Amazon Aurora DSQL](CHAP_quotas.md "CHAP_quotas.md").

- Storage limit calculations may take time to reflect freed storage after running a `DROP
TABLE` command. If you need additional storage capacity, see
  [Cluster quotas](CHAP_quotas.md#SECTION_cluster-quotas "CHAP_quotas.md#SECTION_cluster-quotas") to request quota updates.
- For large tables in Aurora DSQL, use the system catalog to retrieve table row counts instead of `COUNT(*)` operations.
  For more information, see [Using systems tables and
  commands in Aurora DSQL](working-with-systems-tables.md "working-with-systems-tables.md").
- Aurora DSQL manages permissions through schema-level grants. Admin users create schemas using
  `CREATE SCHEMA` and grant access to other roles using `GRANT USAGE ON SCHEMA`.
  Admin users manage objects in the public schema, while non-admin users create objects in user-created
  schemas. The admin role can grant itself any other role to obtain permissions on user-created objects.
  For more information, see [Authorizing database roles to use SQL in your database](using-database-and-iam-roles.md#using-database-and-iam-roles-custom-database-roles-sql "using-database-and-iam-roles.md#using-database-and-iam-roles-custom-database-roles-sql").
- When drivers call `PG_PREPARED_STATEMENTS`, Aurora DSQL provides a cluster-wide view of
  cached prepared statements. You may see more prepared statements per connection
  than expected for the same cluster and IAM role. Aurora DSQL manages statement names dynamically
  during preparation.
- When connecting from IPv4-only instances, ensure your client is configured for IPv4 connections.
  Some PostgreSQL clients attempt both IPv4 and IPv6 connections in dualstack mode. If the IPv4 connection
  experiences throttling, the client may attempt IPv6 and return a `NetworkUnreachable` error
  on IPv4-only hosts. Configure your client to use IPv4 explicitly to avoid this behavior.
- After an admin user creates a new schema, `GRANT` and `REVOKE` changes
  propagate to existing connections within the connection lifetime (up to one hour). For immediate
  effect, establish a new connection after permission changes.
- During rare multi-Region linked-cluster recovery scenarios, automated cluster
  recovery operations maintain high availability, but you may experience transient concurrency control or connection errors.
  In most cases, only a percentage of your workload is affected. When you encounter
  these transient errors, retry your transaction or reconnect with your client.
- Some SQL clients, such as Datagrip, request extensive system metadata to populate
  schema information. Aurora DSQL provides core metadata for SQL query functionality. Schema display
  in these clients may show limited information compared to their full feature set.
- To ensure queries recognize newly created schemas and tables, refresh your connection after
  creating or dropping database objects. This includes scenarios where you see `Schema Already Exists`
  errors after dropping a schema, or when querying objects created in another connection. Disconnect and
  reconnect, or run `SET search_path` again to refresh the catalog cache.
- For complex queries, use `EXPLAIN ANALYZE VERBOSE` to identify high-latency operations
  and optimize query plans. Covering indexes can significantly reduce DPU costs by enabling index-only scans
  instead of full table scans. For more information, see
  [Working with Aurora DSQL EXPLAIN plans](working-with-explain-plans.md "working-with-explain-plans.md").
- Connection limits are managed at the cluster level. See
  [Cluster quotas](CHAP_quotas.md#SECTION_cluster-quotas "CHAP_quotas.md#SECTION_cluster-quotas") to request quota updates.
