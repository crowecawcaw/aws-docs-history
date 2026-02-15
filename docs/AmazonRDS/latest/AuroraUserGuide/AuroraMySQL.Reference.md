# Aurora MySQL–specific information_schema tables

Aurora MySQL has certain `information_schema` tables that are specific to Aurora.

## information_schema.aurora_global_db_instance_status

The `information_schema.aurora_global_db_instance_status` table contains information about the status of all DB instances in a global database's primary and secondary DB clusters.
The following table shows the columns that you can use. The remaining columns are for Aurora internal use only.

###### Note

This information schema table is only available with Aurora MySQL version 3.04.0 and higher
global databases.

| Column                  | Data type            | Description                                                                                                                                                                                                                                              |
| ----------------------- | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SERVER_ID               | varchar(100)         | The identifier of the DB instance.                                                                                                                                                                                                                       |
| SESSION_ID              | varchar(100)         | A unique identifier for the current session. A value of `MASTER_SESSION_ID` identifies the Writer (primary) DB instance.                                                                                                                                 |
| AWS_REGION              | varchar(100)         | The AWS Region in which this global database instance runs. For a list of Regions, see [Region availability](Concepts.md#Aurora.Overview.Availability "Concepts.md#Aurora.Overview.Availability").                                                       |
| DURABLE_LSN             | bigint unsigned      | The log sequence number (LSN) made durable in storage.<br>A log sequence number (LSN) is a unique sequential number that identifies a record in the database transaction log.<br>LSNs are ordered such that a larger LSN represents a later transaction. |
| HIGHEST_LSN_RCVD        | bigint unsigned      | The highest LSN received by the DB instance from the writer DB instance.                                                                                                                                                                                 |
| OLDEST_READ_VIEW_TRX_ID | bigint unsigned      | The ID of the oldest transaction that the writer DB instance can purge to.                                                                                                                                                                               |
| OLDEST_READ_VIEW_LSN    | bigint unsigned      | The oldest LSN used by the DB instance to read from storage.                                                                                                                                                                                             |
| VISIBILITY_LAG_IN_MSEC  | float(10,0) unsigned | For readers in the primary DB cluster, how far this DB instance is lagging behind the writer DB instance in milliseconds.<br>For readers in a secondary DB cluster, how far this DB instance is lagging behind the secondary volume in milliseconds.     |

## information_schema.aurora_global_db_status

The `information_schema.aurora_global_db_status` table contains information about various aspects of Aurora global database lag, specifically, lag
of the underlying Aurora storage (so called durability lag) and lag between the recovery point objective (RPO).
The following table shows the columns that you can use. The remaining columns are for Aurora internal use only.

###### Note

This information schema table is only available with Aurora MySQL version 3.04.0 and higher
global databases.

| Column                         | Data type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AWS_REGION                     | varchar(100)         | The AWS Region in which this global database instance runs. For a list of Regions, see [Region availability](Concepts.md#Aurora.Overview.Availability "Concepts.md#Aurora.Overview.Availability").                                                                                                                                                                                                                                                                                                                                                                               |
| HIGHEST_LSN_WRITTEN            | bigint unsigned      | The highest log sequence number (LSN) that currently exists<br>on this DB cluster. A log sequence number (LSN) is a unique sequential number that identifies a record in the database transaction log.<br>LSNs are ordered such that a larger LSN represents a later transaction.                                                                                                                                                                                                                                                                                                |
| DURABILITY_LAG_IN_MILLISECONDS | float(10,0) unsigned | The difference in the timestamp values between the `HIGHEST_LSN_WRITTEN` on a<br>secondary DB cluster and the `HIGHEST_LSN_WRITTEN` on the primary DB cluster. This value is always 0 on the primary DB cluster of the Aurora global database.                                                                                                                                                                                                                                                                                                                                   |
| RPO_LAG_IN_MILLISECONDS        | float(10,0) unsigned | The recovery point objective (RPO) lag. The RPO lag is the time<br>it takes for the most recent user transaction COMMIT to be stored on a secondary DB cluster after it's been stored<br>on the primary DB cluster of the Aurora global database. This value is always 0 on the primary DB cluster of the Aurora global database.<br>In simple terms, this metric calculates the recovery point objective for each Aurora MySQL DB cluster in the Aurora global database, that is, how much data might be lost<br>if there were an outage. As with lag, RPO is measured in time. |
| LAST_LAG_CALCULATION_TIMESTAMP | datetime             | The timestamp that specifies when values were last calculated for<br>`DURABILITY_LAG_IN_MILLISECONDS` and `RPO_LAG_IN_MILLISECONDS`. A time value such as `1970-01-01 00:00:00+00` means<br>this is the primary DB cluster.                                                                                                                                                                                                                                                                                                                                                      |
| OLDEST_READ_VIEW_TRX_ID        | bigint unsigned      | The ID of the oldest transaction that the writer DB instance can purge to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## information_schema.replica_host_status

The `information_schema.replica_host_status` table contains replication information. The columns that you can
use are shown in the following table. The remaining columns are for Aurora internal use only.

| Column                      | Data type    | Description                                                                                             |
| --------------------------- | ------------ | ------------------------------------------------------------------------------------------------------- |
| CPU                         | double       | The CPU percentage usage of the replica host.                                                           |
| IS_CURRENT                  | tinyint      | Whether the replica is current.                                                                         |
| LAST_UPDATE_TIMESTAMP       | datetime(6)  | The time the last update occurred. Used to determine whether a record is stale.                         |
| REPLICA_LAG_IN_MILLISECONDS | double       | The replica lag in milliseconds.                                                                        |
| SERVER_ID                   | varchar(100) | The ID of the database server.                                                                          |
| SESSION_ID                  | varchar(100) | The ID of the database session. Used to determine whether a DB instance is a writer or reader instance. |

###### Note

When a replica instance falls behind, the information queried from its `information_schema.replica_host_status`
table might be outdated. In this situation, we recommend that you query from the writer instance instead.

While the `mysql.ro_replica_status` table has similar information, we don't recommend that you use
it.

## information_schema.aurora_forwarding_processlist

The `information_schema.aurora_forwarding_processlist` table contains information about processes involved in
write forwarding.

The contents of this table are visible only on the writer DB instance for a DB cluster with global or in-cluster write
forwarding turned on. An empty result set is returned on reader DB instances.

| Field                       | Data type    | Description                                                                                                                                                                                                                                                                                                                                                        |
| --------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ID                          | bigint       | The identifier of the connection on the writer DB instance. This<br>identifier is the same value displayed in the `Id` column<br>of the `SHOW PROCESSLIST` statement and returned by the<br>`CONNECTION_ID()` function within the thread.                                                                                                                          |
| USER                        | varchar(32)  | The MySQL user that issued the statement.                                                                                                                                                                                                                                                                                                                          |
| HOST                        | varchar(255) | The MySQL client that issued the statement. For forwarded<br>statements, this field shows the application client host address<br>that established the connection on the forwarding reader DB<br>instance.                                                                                                                                                          |
| DB                          | varchar(64)  | The default database for the thread.                                                                                                                                                                                                                                                                                                                               |
| COMMAND                     | varchar(16)  | The type of command the thread is executing on behalf of the client, or `Sleep` if the session<br>is idle. For descriptions of thread commands, see the MySQL documentation on [Thread Command Values](https://dev.mysql.com/doc/refman/8.0/en/thread-commands.html "https://dev.mysql.com/doc/refman/8.0/en/thread-commands.html") in the<br>MySQL documentation. |
| TIME                        | int          | The time in seconds that the thread has been in its current state.                                                                                                                                                                                                                                                                                                 |
| STATE                       | varchar(64)  | An action, event, or state that indicates what the thread is doing. For descriptions of state values, see<br>[General Thread<br>States](https://dev.mysql.com/doc/refman/8.0/en/general-thread-states.html "https://dev.mysql.com/doc/refman/8.0/en/general-thread-states.html") in the MySQL documentation.                                                       |
| INFO                        | longtext     | The statement that the thread is executing, or `NULL` if it isn't executing a statement. The<br>statement might be the one sent to the server, or an innermost statement if the statement executes other<br>statements.                                                                                                                                            |
| IS_FORWARDED                | bigint       | Indicates whether the thread is forwarded from a reader DB instance.                                                                                                                                                                                                                                                                                               |
| REPLICA_SESSION_ID          | bigint       | The connection identifier on the Aurora Replica. This identifier<br>is the same value displayed in the `Id` column of the<br>`SHOW PROCESSLIST` statement on the forwarding Aurora<br>reader DB instance.                                                                                                                                                          |
| REPLICA_INSTANCE_IDENTIFIER | varchar(64)  | The DB instance identifier of the forwarding thread.                                                                                                                                                                                                                                                                                                               |
| REPLICA_CLUSTER_NAME        | varchar(64)  | The DB cluster identifier of the forwarding thread. For<br>in-cluster write forwarding, this identifier is the same DB cluster<br>as the writer DB instance.                                                                                                                                                                                                       |
| REPLICA_REGION              | varchar(64)  | The AWS Region from which the forwarding thread originates. For<br>in-cluster write forwarding, this Region is the same<br>AWS Region as the writer DB instance.                                                                                                                                                                                                   |
