

# Accessing Aurora DSQL with PostgreSQL-compatible clients
<a name="accessing"></a>

Aurora DSQL uses the [PostgreSQL wire protocol](https://www.postgresql.org/docs/current/protocol.html). You can connect to PostgreSQL using a variety of tools and clients, such as AWS CloudShell, psql, DBeaver, and DataGrip. The following table summarizes how Aurora DSQL maps common PostgreSQL connection parameters:


| PostgreSQL | Aurora DSQL | Notes | 
| --- | --- | --- | 
| Role (also known as User or Group) | Database Role | Aurora DSQL creates a role for you named admin. When you create custom database roles, you must use the admin role to associate them with IAM roles for authenticating when connecting to your cluster. For more information, see [Using database roles and IAM authentication](using-database-and-iam-roles.md). | 
| Host (also known as hostname or hostspec) | Cluster Endpoint | Aurora DSQL single-Region clusters provide a single managed endpoint and automatically redirect traffic if there is unavailability within the Region. | 
| Port | N/A – use default 5432 | This is the PostgreSQL default. | 
| Database (dbname) | use postgres | Aurora DSQL creates this database for you when you create the cluster. | 
| SSL Mode | SSL is always enabled server-side | In Aurora DSQL, Aurora DSQL supports the require SSL Mode. Connections without SSL are rejected by Aurora DSQL. | 
| Password | Authentication Token | Aurora DSQL requires temporary authentication tokens instead of long-lived passwords. To learn more, see [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md). | 

When connecting, Aurora DSQL requires a signed IAM [authentication token](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/SECTION_authentication-token.html) in place of a traditional password. These temporary tokens are generated using AWS Signature Version 4 and are used only during connection establishment. Once connected, the session remains active until it ends or the client disconnects.

If you attempt to open a new session with an expired token, the connection request fails and a new token must be generated. For more information, see [Generating an authentication token in Amazon Aurora DSQL](SECTION_authentication-token.md).

## Supported session parameters
<a name="accessing-session-parameters"></a>

Aurora DSQL automatically optimizes storage, connection management, and transaction processing, so it supports a focused set of session parameters. Aurora DSQL accepts the parameters listed in the following table. Parameters outside this set return the following error:

```
ERROR: setting configuration parameter "{{parameter_name}}" not supported
```

Aurora DSQL supports the following PostgreSQL session parameters. Unless otherwise noted, you can set these using `SET`, `SET SESSION`, or as connection string options. You can also use `SET LOCAL` to set any of these parameters for the duration of a single transaction. Use `RESET` to restore a parameter to its default value.


**Supported session parameters**  

| Parameter | Category | Description | 
| --- | --- | --- | 
| application\_name | Client identification | Sets the application name reported in connection metadata. Useful for identifying connections in monitoring. | 
| client\_encoding | Localization | Sets the client-side character encoding. The database uses UTF-8 internally. | 
| datestyle | Output formatting | Sets the display format for date and time values (for example, ISO, MDY). | 
| extra\_float\_digits | Output formatting | Sets the number of digits displayed for floating-point values. Some drivers, such as JDBC, use this parameter. | 
| intervalstyle | Output formatting | Sets the display format for interval values. | 
| timezone | Localization | Sets the time zone for the session. Aurora DSQL stores all timezone-aware dates and times internally in UTC. This parameter controls how Aurora DSQL displays values to the client. | 
| search\_path | Schema resolution | Sets the schema search order for unqualified object names. | 
| enable\_bitmapscan | Query planner | Enables or disables the query planner's use of bitmap-scan plan types. | 
| enable\_hashjoin | Query planner | Enables or disables the query planner's use of hash-join plan types. | 
| enable\_indexonlyscan | Query planner | Enables or disables the query planner's use of index-only-scan plan types. | 
| enable\_indexscan | Query planner | Enables or disables the query planner's use of index-scan plan types. | 
| enable\_material | Query planner | Enables or disables the query planner's use of materialization. | 
| enable\_mergejoin | Query planner | Enables or disables the query planner's use of merge-join plan types. | 
| enable\_nestloop | Query planner | Enables or disables the query planner's use of nested-loop join plans. | 
| enable\_seqscan | Query planner | Enables or disables the query planner's use of sequential scan plan types. | 
| disable\_sync\_create\_index | Aurora DSQL-specific | Controls whether CREATE INDEX runs asynchronously. Default is on, meaning Aurora DSQL creates indexes asynchronously. Set to off to create indexes synchronously on empty tables. | 
| role | Session identity | Sets the current role. In Aurora DSQL, you can only set this parameter using SET LOCAL within a transaction block. | 

Aurora DSQL automatically manages the following aspects of your database, so you don't need to configure the corresponding PostgreSQL session parameters:
+ **Connection and network parameters** – Aurora DSQL manages connection lifecycle and TCP settings internally, including `tcp_keepalives_idle`, `tcp_keepalives_interval`, and `tcp_keepalives_count`.
+ **Memory and resource parameters** – Aurora DSQL automatically manages memory allocation, including `work_mem` and `shared_buffers`.
+ **Timeout parameters** – Aurora DSQL enforces its own transaction duration limits, including `statement_timeout`, `lock_timeout`, and `idle_in_transaction_session_timeout`.
+ **Replication and WAL parameters** – Aurora DSQL handles replication automatically through its built-in multi-Region architecture, including `wal_level` and `synchronous_commit`.
+ **Logging parameters** – Aurora DSQL manages logging internally, including `log_statement` and `client_min_messages`.
+ **Transaction parameters** – Aurora DSQL uses a fixed `REPEATABLE READ` isolation level for all transactions. If your driver requires specifying an isolation level, use `BEGIN ISOLATION LEVEL REPEATABLE READ`.

## Access Aurora DSQL using SQL clients
<a name="accessing-sql-clients"></a>

Aurora DSQL supports multiple PostgreSQL-compatible clients for connecting to your cluster. The following sections describe how to connect using PostgreSQL with AWS CloudShell or your local command line, as well as GUI-based tools like DBeaver and JetBrains DataGrip. Each client requires a valid authentication token as described in the previous section.

**Topics**
+ [Supported session parameters](#accessing-session-parameters)
+ [Access Aurora DSQL using SQL clients](#accessing-sql-clients)
+ [Use DBeaver to access Aurora DSQL](accessing-dbeaver.md)
+ [Use JetBrains DataGrip to access Aurora DSQL](accessing-datagrip.md)
+ [Use the PostgreSQL interactive terminal (psql) to access Aurora DSQL](accessing-psql.md)
+ [Use Aurora DSQL driver for SQLTools](accessing-vscode.md)
+ [Troubleshooting](#accessing-troubleshooting)

## Troubleshooting
<a name="accessing-troubleshooting"></a>

**Authentication credentials expiration for the SQL Clients**

Established sessions remain authenticated for a maximum of 1 hour or until an explicit disconnect or a client-side timeout takes place. If new connections need to be established, a new authentication token must be generated and provided in the **Password** field of the connection. Trying to open a new session (for example, to list new tables, or open a new SQL console) forces a new authentication attempt. If the authentication token configured in the **Connection** settings is no longer valid, that new session will fail and all previously opened sessions will become invalid. Keep this in mind when choosing the duration of your IAM authentication token with the `expires-in` option, which can be set to 15 minutes by default and can be set to a maximum value of seven days.

Additionally, see the [Troubleshooting](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/troubleshooting.html) section of the Aurora DSQL documentation.