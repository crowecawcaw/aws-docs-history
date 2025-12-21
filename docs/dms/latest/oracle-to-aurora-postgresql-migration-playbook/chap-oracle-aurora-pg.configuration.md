# Oracle instance parameters and Amazon RDS parameter groups

With AWS DMS, you can configure Oracle instance parameters and Amazon RDS parameter groups to optimize database performance, security, and resource utilization. Oracle instance parameters control various aspects of an Oracle database instance, such as memory allocation, logging, and backup settings. Amazon RDS parameter groups act as a container for engine configuration values that can be applied to one or more Amazon RDS database instances.

| Feature compatibility          | AWS SCT / AWS DMS automation level | AWS SCT action code index | Key differences                              |
| ------------------------------ | ---------------------------------- | ------------------------- | -------------------------------------------- |
| One star feature compatibility | N/A                                | N/A                       | Use Cluster and Database/Cluster parameters. |

## Oracle usage

Oracle instance and database-level parameters can be configured using the `ALTER SYSTEM` command. Certain parameters can be configured dynamically and take immediate effect while other parameters require an instance restart.

- All Oracle instance and database-level parameters are stored in a binary file known as the Server Parameter file (SPFILE).
- The binary SPFILE can be exported to a text file using the following command:

```
CREATE PFILE = 'my_init.ora' FROM SPFILE = 's_params.ora';
```

When modifying parameters, you can choose the persistence of the changed values with one of the three following options:

- Make the change applicable only after a restart by specifying `scope=spfile`.
- Make the change dynamically, but not persistent, after a restart by specifying `scope=memory`.
- Make the change both dynamically and persistent by specifying `scope=both`.

**Examples**

Use the `ALTER SYSTEM SET` command to configure a value for an Oracle parameter.

```
ALTER SYSTEM SET QUERY_REWRITE_ENABLED = TRUE SCOPE=BOTH;
```

For more information, see [Initialization Parameters](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/initialization-parameters-2.html#GUID-FD266F6F-D047-4EBB-8D96-B51B1DCA2D61 "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/initialization-parameters-2.html#GUID-FD266F6F-D047-4EBB-8D96-B51B1DCA2D61") and [Changing Parameter Values in a Parameter File](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/changing-parameter-values-in-a-parameter-file.html#GUID-4C578B21-DE2B-4210-8EB7-EF28D36CC1CB "https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/changing-parameter-values-in-a-parameter-file.html#GUID-4C578B21-DE2B-4210-8EB7-EF28D36CC1CB") in the _Oracle documentation_.

## PostgreSQL usage

When running PostgreSQL databases as Amazon Aurora Clusters, Parameter Groups are used to change to cluster-level and database-level parameters.

Most of the PostgreSQL parameters are configurable in an Amazon Aurora PostgreSQL cluster, but some are disabled and can’t be modified. Since Amazon Aurora clusters restrict access to the underlying operating system, modification to PostgreSQL parameters must be made using Parameter Groups.

Amazon Aurora is a cluster of database instances and, as a direct result, some of the PostgreSQL parameters apply to the entire cluster while other parameters apply only to a particular database instance.

| Aurora PostgreSQL parameter class                                                                                                              | Controlled by                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cluster-level parameters**<br>Single cluster parameter group for each Amazon Aurora cluster.                                                 | Managed by cluster parameter groups. For example,<br>• The PostgreSQL `wal_buffers` parameter is controlled by a cluster parameter group.<br>• The PostgreSQL `autovacuum` parameter is controlled by a cluster parameter group.<br>• The `client_encoding` parameter is controlled by a cluster parameter group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Database instance-level parameters**<br>Every instance in an Amazon Aurora cluster can be associated with a unique database parameter group. | Managed by database parameter groups For example,<br>• The PostgreSQL shared_buffers memory cache configuration parameter is controlled by a database parameter group with an AWS-optimized default value based on the configured database class: `{DBInstanceClassMemory/10922}`.<br>• The PostgreSQL `max_connections` parameter which controls maximum number of client connections allowed to the PostgreSQL instance, is controlled by a database parameter group. Default value is optimized by AWS based on the configured database class: `LEAST({DBInstanceClassMemory/9531392},5000)`.<br>• The `authentication_timeout` parameter, which controls the maximum time to complete client authentication, in seconds, is controlled by a database parameter group.<br>• The `superuser_reserved_connections` parameter which determines the number of reserved connection slots for PostgreSQL superusers, is configured by a database parameter group.<br>• The PostgreSQL `effective_cache_size` which informs the query optimizer how much cache is present in the kernel and helps control how expensive large index scans will be, is controlled by a database level parameter group. The default value is optimized by AWS based on database class (RAM): `{DBInstanceClassMemory/10922}`. |

PostgreSQL 10 introduces the following new parameters:

- `enable_gathermerge` — enable run plan gather merge.
- `max_parallel_workers` — maximum number of parallel workers process.
- `max_sync_workers_per_subscription` — maximum number of synchronous workers for subscription.
- `wal_consistency_checking` — check consistency of WAL on the standby instance (can’t be set in Aurora PostgreSQL).
- `max_logical_replication_workers` — maximum number of logical replication worker process.
- `max_pred_locks_per_relation` — Maximum number of records that can be predicate-lock before locking the entire relation (signup).
- `max_pred_locks_per_page` — Maximum number of records that can be predicate-lock before locking the entire page.
- `min_parallel_table_scan_size` — minimum table size to consider parallel table scan.
- `min_parallel_index_scan_size` — minimum table size to consider parallel index scan.

**Examples**

Follow the following steps to create and configure Amazon Aurora database and cluster parameter groups.

1. Sign in to the AWS Management Console and choose **RDS**.
2. Choose **Parameter groups** and choose **Create parameter group**.

You can’t edit the default parameter group. Create a custom parameter group to apply changes to your Amazon Aurora cluster and its database instances.

1. For **Parameter group family**, choose the database family.
2. For **Type**, choose **DB Parameter Group**.
3. Choose **Create**.

Follow the following steps to modify an existing parameter group.

1. Sign in to the AWS Management Console and choose **RDS**.
2. Choose **Parameter groups** and choose the name of the parameter to edit.
3. For **Parameter group actions**, choose **Edit**.
4. Change parameter values and choose **Save changes**.

For more information, see [SET](https://www.postgresql.org/docs/13/sql-set.html "https://www.postgresql.org/docs/13/sql-set.html") in the _PostgreSQL documentation_.
