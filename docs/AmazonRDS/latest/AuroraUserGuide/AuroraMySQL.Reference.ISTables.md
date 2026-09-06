

# Aurora MySQL–specific information\_schema tables
<a name="AuroraMySQL.Reference.ISTables"></a>

Aurora MySQL has certain `information_schema` tables that are specific to Aurora.

## information\_schema.aurora\_global\_db\_instance\_status
<a name="AuroraMySQL.Reference.ISTables.aurora_global_db_instance_status"></a>

The `information_schema.aurora_global_db_instance_status` table contains information about the status of all DB instances in a global database's primary and secondary DB clusters. The following table shows the columns that you can use. The remaining columns are for Aurora internal use only.

**Note**  
This information schema table is only available with Aurora MySQL version 3.04.0 and higher global databases.


| Column | Data type | Description | 
| --- | --- | --- | 
| SERVER\_ID | varchar(100) | The identifier of the DB instance. | 
| SESSION\_ID | varchar(100) | A unique identifier for the current session. A value of MASTER\_SESSION\_ID identifies the Writer (primary) DB instance. | 
| AWS\_REGION | varchar(100) | The AWS Region in which this global database instance runs. For a list of Regions, see [Region availability](Concepts.RegionsAndAvailabilityZones.md#Aurora.Overview.Availability). | 
| DURABLE\_LSN | bigint unsigned | The log sequence number (LSN) made durable in storage. A log sequence number (LSN) is a unique sequential number that identifies a record in the database transaction log. LSNs are ordered such that a larger LSN represents a later transaction. | 
| HIGHEST\_LSN\_RCVD | bigint unsigned | The highest LSN received by the DB instance from the writer DB instance. | 
| OLDEST\_READ\_VIEW\_TRX\_ID | bigint unsigned | The ID of the oldest transaction that the writer DB instance can purge to. | 
| OLDEST\_READ\_VIEW\_LSN | bigint unsigned | The oldest LSN used by the DB instance to read from storage. | 
| VISIBILITY\_LAG\_IN\_MSEC | float(10,0) unsigned | For readers in the primary DB cluster, how far this DB instance is lagging behind the writer DB instance in milliseconds. For readers in a secondary DB cluster, how far this DB instance is lagging behind the secondary volume in milliseconds. | 

## information\_schema.aurora\_global\_db\_status
<a name="AuroraMySQL.Reference.ISTables.aurora_global_db_status"></a>

The `information_schema.aurora_global_db_status` table contains information about various aspects of Aurora global database lag, specifically, lag of the underlying Aurora storage (so called durability lag) and lag between the recovery point objective (RPO). The following table shows the columns that you can use. The remaining columns are for Aurora internal use only.

**Note**  
This information schema table is only available with Aurora MySQL version 3.04.0 and higher global databases.


| Column | Data type | Description | 
| --- | --- | --- | 
| AWS\_REGION | varchar(100) | The AWS Region in which this global database instance runs. For a list of Regions, see [Region availability](Concepts.RegionsAndAvailabilityZones.md#Aurora.Overview.Availability). | 
| HIGHEST\_LSN\_WRITTEN | bigint unsigned | The highest log sequence number (LSN) that currently exists on this DB cluster. A log sequence number (LSN) is a unique sequential number that identifies a record in the database transaction log. LSNs are ordered such that a larger LSN represents a later transaction. | 
| DURABILITY\_LAG\_IN\_MILLISECONDS | float(10,0) unsigned | The difference in the timestamp values between the HIGHEST\_LSN\_WRITTEN on a secondary DB cluster and the HIGHEST\_LSN\_WRITTEN on the primary DB cluster. This value is always 0 on the primary DB cluster of the Aurora global database. | 
| RPO\_LAG\_IN\_MILLISECONDS | float(10,0) unsigned | The recovery point objective (RPO) lag. The RPO lag is the time it takes for the most recent user transaction COMMIT to be stored on a secondary DB cluster after it's been stored on the primary DB cluster of the Aurora global database. This value is always 0 on the primary DB cluster of the Aurora global database.<br />In simple terms, this metric calculates the recovery point objective for each Aurora MySQL DB cluster in the Aurora global database, that is, how much data might be lost if there were an outage. As with lag, RPO is measured in time. | 
| LAST\_LAG\_CALCULATION\_TIMESTAMP | datetime | The timestamp that specifies when values were last calculated for DURABILITY\_LAG\_IN\_MILLISECONDS and RPO\_LAG\_IN\_MILLISECONDS. A time value such as 1970-01-01 00:00:00\+00 means this is the primary DB cluster. | 
| OLDEST\_READ\_VIEW\_TRX\_ID | bigint unsigned | The ID of the oldest transaction that the writer DB instance can purge to. | 

## information\_schema.replica\_host\_status
<a name="AuroraMySQL.Reference.ISTables.replica_host_status"></a>

The `information_schema.replica_host_status` table contains replication information. The columns that you can use are shown in the following table. The remaining columns are for Aurora internal use only.


| Column | Data type | Description | 
| --- | --- | --- | 
| CPU | double | The CPU percentage usage of the replica host. | 
| IS\_CURRENT | tinyint | Whether the replica is current. | 
| LAST\_UPDATE\_TIMESTAMP | datetime(6) | The time the last update occurred. Used to determine whether a record is stale. | 
| REPLICA\_LAG\_IN\_MILLISECONDS | double | The replica lag in milliseconds. | 
| SERVER\_ID | varchar(100) | The ID of the database server. | 
| SESSION\_ID | varchar(100) | The ID of the database session. Used to determine whether a DB instance is a writer or reader instance. | 

**Note**  
When a replica instance falls behind, the information queried from its `information_schema.replica_host_status` table might be outdated. In this situation, we recommend that you query from the writer instance instead.  
While the `mysql.ro_replica_status` table has similar information, we don't recommend that you use it.

## information\_schema.aurora\_forwarding\_processlist
<a name="AuroraMySQL.Reference.ISTables.aurora_forwarding_processlist"></a>

The `information_schema.aurora_forwarding_processlist` table contains information about processes involved in write forwarding.

The contents of this table are visible only on the writer DB instance for a DB cluster with global or in-cluster write forwarding turned on. An empty result set is returned on reader DB instances.


| Field | Data type | Description | 
| --- | --- | --- | 
| ID | bigint | The identifier of the connection on the writer DB instance. This identifier is the same value displayed in the Id column of the SHOW PROCESSLIST statement and returned by the CONNECTION\_ID() function within the thread. | 
| USER | varchar(32) | The MySQL user that issued the statement. | 
| HOST | varchar(255) | The MySQL client that issued the statement. For forwarded statements, this field shows the application client host address that established the connection on the forwarding reader DB instance. | 
| DB | varchar(64) | The default database for the thread. | 
| COMMAND | varchar(16) | The type of command the thread is executing on behalf of the client, or Sleep if the session is idle. For descriptions of thread commands, see the MySQL documentation on [Thread Command Values](https://dev.mysql.com/doc/refman/8.0/en/thread-commands.html) in the MySQL documentation. | 
| TIME | int | The time in seconds that the thread has been in its current state. | 
| STATE | varchar(64) | An action, event, or state that indicates what the thread is doing. For descriptions of state values, see [General Thread States](https://dev.mysql.com/doc/refman/8.0/en/general-thread-states.html) in the MySQL documentation. | 
| INFO | longtext | The statement that the thread is executing, or NULL if it isn't executing a statement. The statement might be the one sent to the server, or an innermost statement if the statement executes other statements. | 
| IS\_FORWARDED | bigint | Indicates whether the thread is forwarded from a reader DB instance. | 
| REPLICA\_SESSION\_ID | bigint | The connection identifier on the Aurora Replica. This identifier is the same value displayed in the Id column of the SHOW PROCESSLIST statement on the forwarding Aurora reader DB instance. | 
| REPLICA\_INSTANCE\_IDENTIFIER | varchar(64) | The DB instance identifier of the forwarding thread. | 
| REPLICA\_CLUSTER\_NAME | varchar(64) | The DB cluster identifier of the forwarding thread. For in-cluster write forwarding, this identifier is the same DB cluster as the writer DB instance. | 
| REPLICA\_REGION | varchar(64) | The AWS Region from which the forwarding thread originates. For in-cluster write forwarding, this Region is the same AWS Region as the writer DB instance. | 