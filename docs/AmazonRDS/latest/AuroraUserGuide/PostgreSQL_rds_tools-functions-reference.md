

# rds\_tools functions reference
<a name="PostgreSQL_rds_tools-functions-reference"></a>

The `rds_tools` extension provides a set of utility functions for managing and monitoring your Aurora PostgreSQL DB instance. Using these functions, you can diagnose replication, vacuum, and configuration issues directly from SQL, without separate monitoring tools. These functions are in addition to the standard PostgreSQL functions. For more information about standard PostgreSQL functions, see [Functions and Operators](https://www.postgresql.org/docs/current/functions.html) in the PostgreSQL documentation.

This section describes the `rds_tools` functions available on Aurora PostgreSQL. Each function description notes the `rds_tools` extension version in which the function became available.

To create the extension, run the following command.

```
postgres=> CREATE EXTENSION rds_tools;
CREATE EXTENSION
```

**Topics**
+ [rds\_tools.role\_password\_encryption\_type](#rds_tools.role_password_encryption_type)
+ [rds\_tools.postgres\_get\_av\_diag](#rds_tools.postgres_get_av_diag)

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