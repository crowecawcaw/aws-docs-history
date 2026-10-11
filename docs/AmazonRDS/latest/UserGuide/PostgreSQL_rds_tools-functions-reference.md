

# rds\_tools functions reference
<a name="PostgreSQL_rds_tools-functions-reference"></a>

The `rds_tools` extension provides a set of utility functions for managing and monitoring your RDS for PostgreSQL DB instance. Using these functions, you can diagnose replication, vacuum, and configuration issues directly from SQL, without separate monitoring tools. These functions are in addition to the standard PostgreSQL functions. For more information about standard PostgreSQL functions, see [Functions and Operators](https://www.postgresql.org/docs/current/functions.html) in the PostgreSQL documentation.

This section describes the `rds_tools` functions available on RDS for PostgreSQL. Each function description notes the `rds_tools` extension version in which the function became available.

To create the extension, run the following command.

```
postgres=> CREATE EXTENSION rds_tools;
CREATE EXTENSION
```

**Topics**
+ [rds\_tools.role\_password\_encryption\_type](#rds_tools.role_password_encryption_type)
+ [rds\_tools.blue\_green\_get\_status](#rds_tools.blue_green_get_status)
+ [rds\_tools.postgres\_get\_av\_diag](#rds_tools.postgres_get_av_diag)
+ [rds\_tools.rds\_version](#rds_tools.rds_version)
+ [rds\_tools.logical\_seed\_lsn](#rds_tools.logical_seed_lsn)
+ [rds\_tools.db\_instance\_identifier](#rds_tools.db_instance_identifier)
+ [rds\_tools.dbi\_resource\_id](#rds_tools.dbi_resource_id)
+ [rds\_tools.multi\_az\_db\_cluster\_source\_dbi\_resource\_id](#rds_tools.multi_az_db_cluster_source_dbi_resource_id)
+ [rds\_tools.show\_topology](#rds_tools.show_topology)
+ [rds\_tools.pg\_ls\_multixactdir](#rds_tools.pg_ls_multixactdir)

## rds\_tools.role\_password\_encryption\_type
<a name="rds_tools.role_password_encryption_type"></a>

Returns the password encryption method used for each database role. This set-returning function excludes RDS-protected system roles from the output. Available starting with `rds_tools` extension version 1.0.

For an example of using this function to review password encryption before migrating database users to SCRAM, see [Using SCRAM for PostgreSQL password encryption](PostgreSQL_Password_Encryption_configuration.md).

### Function prototype
<a name="rds_tools.role_password_encryption_type-prototype"></a>

```
rds_tools.role_password_encryption_type()
```

### Arguments
<a name="rds_tools.role_password_encryption_type-arguments"></a>

None.

### Output
<a name="rds_tools.role_password_encryption_type-output"></a>
+ `rolname` – The name of the database role.
+ `encryption_type` – The password encryption method used, such as `md5` or `scram-sha-256`.

### Usage example
<a name="rds_tools.role_password_encryption_type-example"></a>

```
=> SELECT * FROM rds_tools.role_password_encryption_type();
    rolname    | encryption_type
---------------+-----------------
 postgres      | md5
 app_user      | md5
 readonly_user | scram-sha-256
(3 rows)
```

## rds\_tools.blue\_green\_get\_status
<a name="rds_tools.blue_green_get_status"></a>

Checks for restricted commands run during blue/green deployment operations. During blue/green deployments that use logical replication, you can't replicate data definition language (DDL) commands or large object (LO) operations between the blue and green environments. If a restricted command is detected, restart the blue/green deployment, because the data can't be properly replicated to the green environment. Available starting with `rds_tools` extension version 1.3.

### Function prototype
<a name="rds_tools.blue_green_get_status-prototype"></a>

```
rds_tools.blue_green_get_status(command_type)
```

### Arguments
<a name="rds_tools.blue_green_get_status-arguments"></a>
+ `command_type` – The type of restricted command to check. Valid values are `'DDL'` (data definition language commands) and `'LO'` (large object operations).

### Output
<a name="rds_tools.blue_green_get_status-output"></a>

A `boolean` value. Returns `true` if a restricted command of the specified type was run during the deployment, or `false` if no such command was detected.

### Usage example
<a name="rds_tools.blue_green_get_status-example"></a>

```
=> SELECT rds_tools.blue_green_get_status('DDL');
 blue_green_get_status
-----------------------
 f
(1 row)
```

## rds\_tools.postgres\_get\_av\_diag
<a name="rds_tools.postgres_get_av_diag"></a>

Retrieves diagnostic information about autovacuum processes that are blocking or lagging behind, along with suggestions for resolving each issue. Run this set-returning function in the database with the oldest transaction ID for accurate results. For more information, see [Identify and resolve aggressive vacuum blockers](Appendix.PostgreSQL.CommonDBATasks.Autovacuum_Monitoring.md).

Available starting with `rds_tools` extension version 1.9.

### Function prototype
<a name="rds_tools.postgres_get_av_diag-prototype"></a>

```
rds_tools.postgres_get_av_diag()
```

### Arguments
<a name="rds_tools.postgres_get_av_diag-arguments"></a>

None.

### Output
<a name="rds_tools.postgres_get_av_diag-output"></a>
+ `blocker` – The category of database activity blocking the vacuum. The value is one of the following:
  + Active statement
  + Idle in transaction
  + Prepared transaction
  + Logical replication slot
  + Read replica with physical replication slot
  + Read replica with streaming replication
  + Temporary tables
+ `database` – The name of the database where the blocking activity is occurring.
+ `blocker_identifier` – The identifier of the blocking activity. The value depends on the blocker type:
  + For an active statement or idle-in-transaction session, the process ID with its SQL statement.
  + For a prepared transaction, the prepared transaction name.
  + For a read replica, the IP address of the replica.
  + For a replication slot, the replication slot name.
+ `wait_event` – The wait event of the blocking session, where applicable.
+ `autovacuum_lagging_by` – The number of transactions that autovacuum is lagging behind for the category.
+ `suggestion` – A suggestion to resolve the blocker, including the database name, process ID, and the action to take.
+ `suggested_action` – An array of the actions to take to resolve the blocker.

### Usage example
<a name="rds_tools.postgres_get_av_diag-example"></a>

```
=> SELECT *
   FROM rds_tools.postgres_get_av_diag()
   ORDER BY autovacuum_lagging_by DESC;

blocker               | Active statement
database              | my_database
blocker_identifier    | SELECT pg_sleep(20000);
wait_event            | Timeout:PgSleep
autovacuum_lagging_by | 568600871
suggestion            | Connect to database "my_database", review carefully, and consider terminating the process using suggested_action.
suggested_action      | {"SELECT pg_terminate_backend(29621);"}
```

## rds\_tools.rds\_version
<a name="rds_tools.rds_version"></a>

Displays the RDS for PostgreSQL engine version for your DB instance. This function reads the version information from the instance's configuration files. Available starting with `rds_tools` extension version 1.1.

### Function prototype
<a name="rds_tools.rds_version-prototype"></a>

```
rds_tools.rds_version()
```

### Arguments
<a name="rds_tools.rds_version-arguments"></a>

None.

### Output
<a name="rds_tools.rds_version-output"></a>

A character string that contains the engine version.

### Usage example
<a name="rds_tools.rds_version-example"></a>

```
=> SELECT rds_tools.rds_version();
 rds_version
-------------
 18.1.R1
(1 row)
```

## rds\_tools.logical\_seed\_lsn
<a name="rds_tools.logical_seed_lsn"></a>

Returns the logical seed log sequence number (LSN) that represents the point where logical replication diverges from the source instance. Use this function to manage logical replication setups and understand replication consistency points. Available starting with `rds_tools` extension version 1.2.

### Function prototype
<a name="rds_tools.logical_seed_lsn-prototype"></a>

```
rds_tools.logical_seed_lsn()
```

### Arguments
<a name="rds_tools.logical_seed_lsn-arguments"></a>

None.

### Output
<a name="rds_tools.logical_seed_lsn-output"></a>

A `pg_lsn` value.

### Usage example
<a name="rds_tools.logical_seed_lsn-example"></a>

```
=> SELECT rds_tools.logical_seed_lsn();
 logical_seed_lsn
------------------
 0/1677B68
(1 row)
```

## rds\_tools.db\_instance\_identifier
<a name="rds_tools.db_instance_identifier"></a>

Displays the DB instance identifier. You specify this identifier when you create the DB instance, and AWS services use it throughout to identify your database. Available starting with `rds_tools` extension version 1.2.

### Function prototype
<a name="rds_tools.db_instance_identifier-prototype"></a>

```
rds_tools.db_instance_identifier()
```

### Arguments
<a name="rds_tools.db_instance_identifier-arguments"></a>

None.

### Output
<a name="rds_tools.db_instance_identifier-output"></a>

A character string that contains the DB instance identifier.

### Usage example
<a name="rds_tools.db_instance_identifier-example"></a>

```
=> SELECT rds_tools.db_instance_identifier();
 db_instance_identifier
------------------------
 my-postgres-instance
(1 row)
```

## rds\_tools.dbi\_resource\_id
<a name="rds_tools.dbi_resource_id"></a>

Displays the DB instance resource ID (DBI resource ID) of your DB instance. The DBI resource ID is a unique, immutable identifier that AWS generates for the DB instance. It remains constant throughout the instance's lifetime, even if you rename the instance. Use this value to correlate database activity with AWS CloudTrail logs or other AWS monitoring services. This value matches the `DbiResourceId` field returned by the [DBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DBInstance.html) RDS API command. Available starting with `rds_tools` extension version 1.4.

### Function prototype
<a name="rds_tools.dbi_resource_id-prototype"></a>

```
rds_tools.dbi_resource_id()
```

### Arguments
<a name="rds_tools.dbi_resource_id-arguments"></a>

None.

### Output
<a name="rds_tools.dbi_resource_id-output"></a>

A character string that contains the DBI resource ID.

### Usage example
<a name="rds_tools.dbi_resource_id-example"></a>

```
=> SELECT rds_tools.dbi_resource_id();
          dbi_resource_id
-----------------------------------
 db-ABC123DEF456GHI789JKL012MNO345P
(1 row)
```

## rds\_tools.multi\_az\_db\_cluster\_source\_dbi\_resource\_id
<a name="rds_tools.multi_az_db_cluster_source_dbi_resource_id"></a>

Displays the DBI resource ID of the source instance for a Multi-AZ DB cluster deployment. Use this function to understand the relationship between instances in a Multi-AZ configuration and to troubleshoot replication or failover scenarios. Available starting with `rds_tools` extension version 1.4.

### Function prototype
<a name="rds_tools.multi_az_db_cluster_source_dbi_resource_id-prototype"></a>

```
rds_tools.multi_az_db_cluster_source_dbi_resource_id()
```

### Arguments
<a name="rds_tools.multi_az_db_cluster_source_dbi_resource_id-arguments"></a>

None.

### Output
<a name="rds_tools.multi_az_db_cluster_source_dbi_resource_id-output"></a>

A character string that contains the source DBI resource ID. Returns NULL if the instance isn't part of a Multi-AZ DB cluster, the configuration file doesn't exist, or the `dbi_resource_id` field doesn't exist in the configuration.

### Usage example
<a name="rds_tools.multi_az_db_cluster_source_dbi_resource_id-example"></a>

```
=> SELECT rds_tools.multi_az_db_cluster_source_dbi_resource_id();
 multi_az_db_cluster_source_dbi_resource_id
--------------------------------------------
 db-XYZ789ABC123DEF456GHI012JKL345MNO678P
(1 row)
```

## rds\_tools.show\_topology
<a name="rds_tools.show_topology"></a>

Displays topology metadata for RDS Multi-AZ clusters, which enables rapid switchovers by providing connection information for all instances in the cluster. Client libraries such as the AWS Advanced JDBC Wrapper Driver use this set-returning function to connect directly to all instances in an RDS Multi-AZ cluster. To identify the resource ID of the writer instance, use this function together with the `rds_tools.multi_az_db_cluster_source_dbi_resource_id` function. Available starting with `rds_tools` extension version 1.4.

### Function prototype
<a name="rds_tools.show_topology-prototype"></a>

```
rds_tools.show_topology([client_identifier])
```

### Arguments
<a name="rds_tools.show_topology-arguments"></a>
+ `client_identifier` (optional) – An identifier for the client library or proxy that is querying the topology. This parameter is optional but recommended, because it allows Amazon RDS to track which clients are actively querying topology and provides telemetry for support of additional clients.

### Output
<a name="rds_tools.show_topology-output"></a>
+ `id` – The DBI resource ID of each instance in the RDS Multi-AZ cluster.
+ `endpoint` – The endpoint for each node in the cluster.
+ `port` – The port number for each instance in the RDS Multi-AZ cluster.
+ `role` – The role of the node in the cluster, such as writer or reader.
+ `status` – The status of the node.
+ `version` – The version of the topology record.

### Usage example
<a name="rds_tools.show_topology-example"></a>

```
=> SELECT id, endpoint, port, role FROM rds_tools.show_topology('my-jdbc-app');
       id        |                         endpoint                          | port | role
-----------------+-----------------------------------------------------------+------+--------
 db-IDENTIFIER-1 | somedb-instance-1.aaaaaaaaaaaa.us-west-2.rds.amazonaws.com | 5432 | writer
 db-IDENTIFIER-2 | somedb-instance-2.aaaaaaaaaaaa.us-west-2.rds.amazonaws.com | 5432 | reader
 db-IDENTIFIER-3 | somedb-instance-3.aaaaaaaaaaaa.us-west-2.rds.amazonaws.com | 5432 | reader
(3 rows)
```

## rds\_tools.pg\_ls\_multixactdir
<a name="rds_tools.pg_ls_multixactdir"></a>

Lists the contents of the `pg_multixact` directory, which stores multitransaction data in PostgreSQL. Use this set-returning function to monitor multixact usage, troubleshoot multixact-related issues, and understand database storage patterns. Available starting with `rds_tools` extension version 1.7.

### Function prototype
<a name="rds_tools.pg_ls_multixactdir-prototype"></a>

```
rds_tools.pg_ls_multixactdir()
```

### Arguments
<a name="rds_tools.pg_ls_multixactdir-arguments"></a>

None.

### Output
<a name="rds_tools.pg_ls_multixactdir-output"></a>
+ `name` – The name of the file or directory.
+ `size` – The size in bytes.
+ `modification` – The last modification timestamp.

### Usage example
<a name="rds_tools.pg_ls_multixactdir-example"></a>

```
=> SELECT * FROM rds_tools.pg_ls_multixactdir();
           name            | size |      modification
---------------------------+------+------------------------
 pg_multixact/members/     | 4096 | 2026-10-01 19:17:29+00
 pg_multixact/members/0000 | 8192 | 2025-08-22 21:53:46+00
 pg_multixact/offsets/     | 4096 | 2026-10-01 19:17:29+00
 pg_multixact/offsets/0000 | 8192 | 2026-10-01 19:22:38+00
(4 rows)
```