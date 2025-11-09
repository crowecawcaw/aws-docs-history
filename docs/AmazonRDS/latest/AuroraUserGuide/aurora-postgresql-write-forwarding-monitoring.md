# Monitoring local write forwarding in Aurora PostgreSQL

Using the following sections you can monitor local write forwarding in Aurora PostgreSQL clusters, including relevant CloudWatch metrics and wait events
to track performance and identify potential issues.

## Amazon CloudWatch metrics and Aurora PostgreSQL status variables for write

forwarding

The following Amazon CloudWatch metrics apply to the writer DB instances when you use write forwarding
on one or more read replicas.

| CloudWatch Metric                          | Units and description                                                                                       |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| `AuroraLocalForwardingWriterDMLThroughput` | Count (per second). Number of forwarded DML statements processed each second by<br>this writer DB instance. |
| `AuroraLocalForwardingWriterOpenSessions`  | Count. Number of open sessions on this writer DB instance processing forwarded<br>queries.                  |
| `AuroraLocalForwardingWriterTotalSessions` | Count. Total number of forwarded sessions on this writer DB instance.                                       |

The following CloudWatch metrics apply to each read replica. These metrics are measured on each reader DB
instance in the DB cluster with local write forwarding enabled.

| CloudWatch Metric                           | Unit and description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `AuroraForwardingReplicaCommitThroughput`   | Count (per second). Number of commits in sessions forwarded by this replica each<br>second.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `AuroraForwardingReplicaDMLLatency`         | Milliseconds. Average response time in milliseconds of forwarded DMLs on replica.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `AuroraForwardingReplicaDMLThroughput`      | Count (per second). Number of forwarded DML statements processed on this replica each second.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| `AuroraForwardingReplicaErrorSessionsLimit` | Count. Number of sessions rejected by the writer DB instance because the limit for max connections or max write forward connections was reached.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `AuroraForwardingReplicaOpenSessions`       | Count. The number of sessions that are using local write forwarding on a replica instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| `AuroraForwardingReplicaReadWaitLatency`    | Milliseconds. Average wait time in milliseconds that the replica waits to be consistent with the LSN of the writer DB instance. The<br>degree to which the reader DB instance waits depends on the `apg_write_forward.consistency_mode` setting. For information about this setting, see<br>[Configuration parameters for write forwarding in Aurora PostgreSQL](aurora-global-database-write-forwarding-apg.md#aurora-global-database-write-forwarding-params-apg "aurora-global-database-write-forwarding-apg.md#aurora-global-database-write-forwarding-params-apg"). |

## Wait events for local write forwarding in Aurora PostgreSQL

Amazon Aurora generates the following wait events when you use write forwarding
with Aurora PostgreSQL.

###### Topics

- [IPC:AuroraWriteForwardConnect](#apg-waits.ipcaurorawriteforwardconnect "#apg-waits.ipcaurorawriteforwardconnect")
- [IPC:AuroraWriteForwardConsistencyPoint](#apg-waits.ipcaurorawriteforwardconsistencypoint "#apg-waits.ipcaurorawriteforwardconsistencypoint")
- [IPC:AuroraWriteForwardExecute](#apg-waits.ipc:aurorawriteforwardexecute "#apg-waits.ipc:aurorawriteforwardexecute")
- [IPC:AuroraWriteForwardGetGlobalConsistencyPoint](#apg-waits.ipc:aurorawriteforwardgetglobalconsistencypoint "#apg-waits.ipc:aurorawriteforwardgetglobalconsistencypoint")
- [IPC:AuroraWriteForwardXactAbort](#apg-waits.ipc:aurorawriteforwardxactabort "#apg-waits.ipc:aurorawriteforwardxactabort")
- [IPC:AuroraWriteForwardXactCommit](#apg-waits.ipc:aurorawriteforwardxactcommit "#apg-waits.ipc:aurorawriteforwardxactcommit")
- [IPC:AuroraWriteForwardXactStart](#apg-waits.ipc:aurorawriteforwardxactstart "#apg-waits.ipc:aurorawriteforwardxactstart")

### IPC:AuroraWriteForwardConnect

The `IPC:AuroraWriteForwardConnect` event occurs when a backend process on
the read replica is waiting for a connection to the writer DB instance to be opened.

**Likely causes of increased waits**

This event increases as the number of connection attempts from a read replica to the writer node increases.

**Actions**

Reduce the number of simultaneous connections from a read replica to the writer node.

### IPC:AuroraWriteForwardConsistencyPoint

The `IPC:AuroraWriteForwardConsistencyPoint` event describes how long a query
from a node on the read replica will wait for the results of forwarded write
operations to be replicated to the current Region. This event is only generated if the
session-level parameter `apg_write_forward.consistency_mode` is set to one of
the following:

- `SESSION` – queries on a read replica wait for the results of all changes made in that session.
- `GLOBAL` – queries on a read replica wait for the results of changes made by that session, plus all committed changes from both the writer DB instance and read replica.

For more information about the `apg_write_forward.consistency_mode` parameter settings, see [Configuration parameters for write forwarding in Aurora PostgreSQL](aurora-global-database-write-forwarding-apg.md#aurora-global-database-write-forwarding-params-apg "aurora-global-database-write-forwarding-apg.md#aurora-global-database-write-forwarding-params-apg").

**Likely causes of increased waits**

Common causes for longer wait times include the following:

- Increased replica lag, as measured by the Amazon CloudWatch `ReplicaLag` metric. For more information about this metric, see [Monitoring Aurora PostgreSQL
  replication](AuroraPostgreSQL.md#AuroraPostgreSQL.Replication.Monitoring "AuroraPostgreSQL.md#AuroraPostgreSQL.Replication.Monitoring").
- Increased load on the writer DB instance or read replica.

**Actions**

Change your consistency mode, depending on your application's requirements.

### IPC:AuroraWriteForwardExecute

The `IPC:AuroraWriteForwardExecute` event occurs when a backend process on
the read replica is waiting for a forwarded query to complete and obtain results
from the writer node of the DB cluster.

**Likely causes of increased waits**

Common causes for increased waits include the following:

- Fetching a large number of rows from the writer node.
- Increased network latency between the writer node and read replica increases the time it takes the read replica to receive data from the writer node.
- Increased load on the read replica can delay transmission of the query request from the read replica to the writer node.
- Increased load on the writer node can delay transmission of data from the writer node to the read replica.

**Actions**

We recommend different actions depending on the causes of your wait event.

- Optimize queries to retrieve only necessary data.
- Optimize data manipulation language (DML) operations to only modify necessary data.
- If the read replica or writer node is constrained by CPU or network bandwidth, consider changing it to an instance type with more CPU capacity or more network bandwidth.

### IPC:AuroraWriteForwardGetGlobalConsistencyPoint

The `IPC:AuroraWriteForwardGetGlobalConsistencyPoint` event occurs when a
backend process on the read replica that's using the GLOBAL consistency mode is
waiting to obtain the global consistency point from the writer node before executing a
query.

**Likely causes of increased waits**

Common causes for increased waits include the following:

- Increased network latency between the read replica and writer node increases the time it takes the read replica to receive data from the writer node.
- Increased load on the read replica can delay transmission of the query request from the read replica to the writer node.
- Increased load on the writer node can delay transmission of data from the writer node to the read replica.

**Actions**

We recommend different actions depending on the causes of your wait event.

- Change your consistency mode, depending on your application's requirements.
- If the read replica or writer node is constrained by CPU or network bandwidth, consider changing it to an instance type with more CPU capacity or more network bandwidth.

### IPC:AuroraWriteForwardXactAbort

The `IPC:AuroraWriteForwardXactAbort` event occurs when a backend process on
the read replica is waiting for the result of a remote cleanup query. Cleanup
queries are issued to return the process to the appropriate state after a write-forwarded
transaction is aborted. Amazon Aurora performs them either because an error was found or
because an user issued an explicit `ABORT` command or cancelled a running
query.

**Likely causes of increased waits**

Common causes for increased waits include the following:

- Increased network latency between the read replica and writer node increases the time it takes the read replica to receive data from the writer node.
- Increased load on the read replica can delay transmission of the cleanup query request from the read replica to the writer node.
- Increased load on the writer node can delay transmission of data from the writer node to the read replica.

**Actions**

We recommend different actions depending on the causes of your wait event.

- Investigate the cause of the aborted transaction.
- If the read replica or writer DB instance is constrained by CPU or network bandwidth, consider changing it to an instance type with more CPU capacity or more network bandwidth.

### IPC:AuroraWriteForwardXactCommit

The `IPC:AuroraWriteForwardXactCommit` event occurs when a backend process on
the read replica is waiting for the result of a forwarded commit transaction
command.

**Likely causes of increased waits**

Common causes for increased waits include the following:

- Increased network latency between the read replica and writer node increases the time it takes the read replica to receive data from the writer node.
- Increased load on the read replica can delay transmission of the query request from the read replica to the writer node.
- Increased load on the writer node can delay transmission of data from the writer node to the read replica.

**Actions**

If the read replica or writer node is constrained by CPU or network bandwidth, consider changing it to an instance type with more CPU capacity or more network bandwidth.

### IPC:AuroraWriteForwardXactStart

The `IPC:AuroraWriteForwardXactStart` event occurs when a backend process on
the read replica is waiting for the result of a forwarded start transaction
command.

**Likely causes of increased waits**

Common causes for increased waits include the following:

- Increased network latency between the read replica and writer node increases the time it takes the read replica to receive data from the writer node.
- Increased load on the read replica can delay transmission of the query request from the read replica to the writer node.
- Increased load on the writer node can delay transmission of data from the writer node to the read replica.

**Actions**

If the read replica or writer node is constrained by CPU or network bandwidth, consider changing it to an instance type with more CPU capacity or more network bandwidth.
