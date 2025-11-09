# Using write forwarding in an Aurora PostgreSQL global database

###### Topics

- [Region and version availability of write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-regions-versions-apg "#aurora-global-database-write-forwarding-regions-versions-apg")
- [Enabling write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-enabling-apg "#aurora-global-database-write-forwarding-enabling-apg")
- [Checking if a secondary cluster has write forwarding enabled in Aurora PostgreSQL](#aurora-global-database-write-forwarding-describing-apg "#aurora-global-database-write-forwarding-describing-apg")
- [Application and SQL compatibility with write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-compatibility-apg "#aurora-global-database-write-forwarding-compatibility-apg")
- [Isolation and consistency for write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-isolation-apg "#aurora-global-database-write-forwarding-isolation-apg")
- [Transaction access modes with write forwarding](#aurora-global-database-write-forwarding-txns "#aurora-global-database-write-forwarding-txns")
- [Running multipart statements with write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-multipart-apg "#aurora-global-database-write-forwarding-multipart-apg")
- [Configuration parameters for write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-params-apg "#aurora-global-database-write-forwarding-params-apg")
- [Amazon CloudWatch metrics for write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-cloudwatch-apg "#aurora-global-database-write-forwarding-cloudwatch-apg")
- [Wait events for write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-wait-events-apg "#aurora-global-database-write-forwarding-wait-events-apg")

## Region and version availability of write forwarding in Aurora PostgreSQL

In Aurora PostgreSQL version 16 and higher major versions, global write forwarding is supported in all minor versions.
For earlier Aurora PostgreSQL versions, global write forwarding is supported with version 15.4 and higher minor versions,
and version 14.9 and higher minor versions. Write forwarding is available in every AWS Region
where Aurora PostgreSQL-based global databases are available.

For more information on version and Region availability of Aurora PostgreSQL global databases, see
[Aurora global databases with Aurora PostgreSQL](Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.GlobalDatabase.apg "Concepts.Aurora_Fea_Regions_DB-eng.Feature.md#Concepts.Aurora_Fea_Regions_DB-eng.Feature.GlobalDatabase.apg").

## Enabling write forwarding in Aurora PostgreSQL

By default, write forwarding isn't enabled when you add a secondary cluster to an Aurora global database.
You can enable write forwarding for your secondary DB cluster while you're creating it or anytime after you create it. If needed, you can disable it
later. Enabling or disabling write forwarding doesn't cause downtime or a reboot.

###### Note

You can use local write forwarding for your applications that have occasional writes and require read-after-write consistency, which is the ability to read the latest write in a transaction.

In the console, you can enable or disable write forwarding when you create or modify a
secondary DB cluster.

#### Enabling or disabling write forwarding

when creating a secondary DB cluster

When you create a new secondary DB cluster, you enable write forwarding by selecting the
**Turn on global write forwarding** check box under **Read replica write forwarding**.
Or clear the check box to disable it. To create a secondary DB cluster, follow the
instructions for your DB engine in [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

The following screenshot shows the **Read replica write
forwarding** section with the **Turn on global write
forwarding** check box selected.

![The Read replica write forwarding section, showing the Turn on global write forwarding check box selected.](images/aurora-global-db-enable-write-forwarding.png)

#### Enabling or disabling write forwarding when modifying a secondary DB cluster

In the console, you can modify a secondary DB cluster to enable or disable write forwarding.

###### To enable or disable write forwarding for a secondary DB cluster by using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**.
3. Choose the secondary DB cluster, and choose **Modify**.
4. In the **Read replica write forwarding** section, check or clear the **Turn on global write forwarding** check box.
5. Choose **Continue**.
6. For **Schedule modifications**, choose **Apply immediately**. If you
   choose **Apply during the next scheduled maintenance window**, Aurora
   ignores this setting and turns on write forwarding immediately.
7. Choose **Modify cluster**.

To enable write forwarding by using the AWS CLI, use the `--enable-global-write-forwarding` option. This
option works when you create a new secondary cluster using the [create-db-cluster](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md") command.
It also works when you modify an existing secondary cluster using the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") command. It
requires that the global database uses an Aurora version that supports write forwarding. You can disable write
forwarding by using the `--no-enable-global-write-forwarding` option with these same CLI commands.

The following procedures describe how to enable or disable write forwarding for a secondary DB cluster in your
global cluster by using the AWS CLI.

###### To enable or disable write forwarding for an existing secondary DB cluster

- Call the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") AWS CLI command and supply the following
  values:

      + `--db-cluster-identifier` – The name of the DB cluster.
      + `--enable-global-write-forwarding` to turn on or
       `--no-enable-global-write-forwarding` to turn off.

  The following example enables write forwarding for DB cluster
  `sample-secondary-db-cluster`.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier sample-secondary-db-cluster \
    --enable-global-write-forwarding
```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier sample-secondary-db-cluster ^
    --enable-global-write-forwarding
```

To enable write forwarding using the Amazon RDS API, set the `EnableGlobalWriteForwarding` parameter to
`true`. This parameter works when you create a new secondary cluster using the
[CreateDBCluster](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md") operation. It also works when you modify an existing secondary cluster using the
[ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md") operation. It requires that the global database uses an Aurora version that
supports write forwarding. You can disable write forwarding by setting the `EnableGlobalWriteForwarding` parameter to `false`.

## Checking if a secondary cluster has write forwarding enabled in Aurora PostgreSQL

To determine whether you can use write forwarding from a secondary cluster, you can check whether the cluster
has the attribute `"GlobalWriteForwardingStatus": "enabled"`.

In the AWS Management Console, you see `Read replica write forwarding` on the **Configuration**
tab of the details page for the cluster. To see the status of the global write forwarding setting for all of
your clusters, run the following AWS CLI command.

A secondary cluster shows the value `"enabled"` or `"disabled"` to indicate if write
forwarding is turned on or off. A value of `null` indicates that write forwarding isn't
available for that cluster. Either the cluster isn't part of a global database, or is the primary cluster
instead of a secondary cluster. The value can also be `"enabling"` or `"disabling"` if
write forwarding is in the process of being turned on or off.

###### Example

```
aws rds describe-db-clusters --query '*[].{DBClusterIdentifier:DBClusterIdentifier,GlobalWriteForwardingStatus:GlobalWriteForwardingStatus}'
[
    {
        "GlobalWriteForwardingStatus": "enabled",
        "DBClusterIdentifier": "aurora-write-forwarding-test-replica-1"
    },
    {
        "GlobalWriteForwardingStatus": "disabled",
        "DBClusterIdentifier": "aurora-write-forwarding-test-replica-2"
    },
    {
        "GlobalWriteForwardingStatus": null,
        "DBClusterIdentifier": "non-global-cluster"
    }
]

```

To find all secondary clusters that have global write forwarding enabled, run the following command. This
command also returns the cluster's reader endpoint. You use the secondary cluster's reader endpoint
when you use write forwarding from the secondary to the primary in your Aurora global database.

###### Example

```
aws rds describe-db-clusters --query 'DBClusters[].{DBClusterIdentifier:DBClusterIdentifier,GlobalWriteForwardingStatus:GlobalWriteForwardingStatus,ReaderEndpoint:ReaderEndpoint} | [?GlobalWriteForwardingStatus == `enabled`]'
[
    {
        "GlobalWriteForwardingStatus": "enabled",
        "ReaderEndpoint": "aurora-write-forwarding-test-replica-1.cluster-ro-cnpexample.us-west-2.rds.amazonaws.com",
        "DBClusterIdentifier": "aurora-write-forwarding-test-replica-1"
    }
]

```

## Application and SQL compatibility with write forwarding in Aurora PostgreSQL

Certain statements aren't allowed or can produce stale results when you use them in a global database with write forwarding.
In addition, user defined functions and user defined procedures aren't supported. Thus, the `EnableGlobalWriteForwarding` setting is turned off by default for secondary clusters. Before turning it on, check
to make sure that your application code isn't affected by any of these restrictions.

You can use the following kinds of SQL statements with write forwarding:

- Data manipulation language (DML) statements, such as `INSERT`,
  `DELETE`, and `UPDATE`
- `SELECT FOR { UPDATE | NO KEY UPDATE | SHARE | KEY SHARE }` statements
- `PREPARE` and `EXECUTE` statements
- `EXPLAIN` statements with the statements in this list

The following kinds of SQL statements aren't supported with write forwarding:

- Data definition language (DDL) statements
- `ANALYZE`
- `CLUSTER`
- `COPY`
- Cursors – Cursors aren't supported, so make sure to close them before using
  write forwarding.
- `GRANT`|`REVOKE`|`REASSIGN OWNED`|`SECURITY LABEL`
- `LOCK`
- `SAVEPOINT` statements
- `SELECT INTO`
- `SET CONSTRAINTS`
- `TRUNCATE`
- `VACUUM`

## Isolation and consistency for write forwarding in Aurora PostgreSQL

In sessions that use write forwarding, you can use the `REPEATABLE READ` and `READ COMMITTED` isolation levels.
However, the `SERIALIZABLE` isolation level isn't supported.

You can control the degree of read consistency on a secondary cluster. The read
consistency level determines how much waiting the secondary cluster does before each read
operation to ensure that some or all changes are replicated from the primary cluster. You
can adjust the read consistency level to ensure that all forwarded write operations from
your session are visible in the secondary cluster before any subsequent queries. You can
also use this setting to ensure that queries on the secondary cluster always see the most
current updates from the primary cluster. This is so even for those submitted by other
sessions or other clusters. To specify this type of behavior for your application, you
choose the appropriate value for the `apg_write_forward.consistency_mode`
parameter. The `apg_write_forward.consistency_mode` parameter has an effect only
on secondary clusters that have write forwarding enabled.

###### Note

For the `apg_write_forward.consistency_mode` parameter, you can specify the
value `SESSION`, `EVENTUAL`, `GLOBAL`, or `OFF`.
By default, the value is set to `SESSION`. Setting the value to
`OFF` disables write forwarding in the session.

As you increase the consistency level, your application spends more time waiting for
changes to be propagated between AWS Regions. You can choose the balance between fast
response time and ensuring that changes made in other locations are fully available before
your queries run.

With each available consistency mode setting, the effect is as follows:

- `SESSION` – All queries in a secondary AWS Region that uses write
  forwarding see the results of all changes made in that session. The changes are visible regardless of whether
  the transaction is committed. If necessary, the query waits for the results of forwarded write operations to
  be replicated to the current Region. It doesn't wait for updated results from write operations performed
  in other Regions or in other sessions within the current Region.
- `EVENTUAL` – Queries in a secondary AWS Region that uses write
  forwarding might see data that is slightly stale due to replication lag. Results of write operations in the
  same session aren't visible until the write operation is performed on the primary Region and replicated
  to the current Region. The query doesn't wait for the updated results to be available. Thus, it might
  retrieve the older data or the updated data, depending on the timing of the statements and the amount of
  replication lag.
- `GLOBAL` – A session in a secondary AWS Region sees changes made by
  that session. It also sees all committed changes from both the primary AWS Region and other secondary AWS
  Regions. Each query might wait for a period that varies depending on the amount of session lag. The query
  proceeds when the secondary cluster is up-to-date with all committed data from the primary cluster, as of the
  time that the query began.
- `OFF` – Write forwarding is disabled in the session.

For more information about all the parameters involved with write forwarding, see [Configuration parameters for write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-params-apg "#aurora-global-database-write-forwarding-params-apg").

## Transaction access modes with write forwarding

If the transaction access mode is set to read only, write forwarding isn't used. You can set the access mode to
read write only while you’re connected to a DB cluster and session that has write forwarding enabled.

For more information on the transaction access modes, see [SET TRANSACTION](https://www.postgresql.org/docs/current/sql-set-transaction.html "https://www.postgresql.org/docs/current/sql-set-transaction.html").

## Running multipart statements with write forwarding in Aurora PostgreSQL

A DML statement might consist of multiple parts, such as a `INSERT ... SELECT`
statement or a `DELETE ... WHERE` statement. In this case, the entire statement
is forwarded to the primary cluster and run there.

## Configuration parameters for write forwarding in Aurora PostgreSQL

The Aurora cluster parameter groups include settings for the write forwarding feature. Because these
are cluster parameters, all DB instances in each cluster have the same values for these variables. Details
about these parameters are summarized in the following table, with usage notes after the table.

| Name                                                    | Scope   | Type         | Default value | Valid values                           |
| ------------------------------------------------------- | ------- | ------------ | ------------- | -------------------------------------- |
| `apg_write_forward.connect_timeout`                     | Session | seconds      | 30            | 0–2147483647                           |
| `apg_write_forward.consistency_mode`                    | Session | enum         | Session       | `SESSION`, `EVENTUAL`, `GLOBAL`, `OFF` |
| `apg_write_forward.idle_in_transaction_session_timeout` | Session | milliseconds | 86400000      | 0–2147483647                           |
| `apg_write_forward.idle_session_timeout`                | Session | milliseconds | 300000        | 0–2147483647                           |
| `apg_write_forward.max_forwarding_connections_percent`  | Global  | int          | 25            | 1–100                                  |

The `apg_write_forward.max_forwarding_connections_percent` parameter is the upper limit on database connection slots that can be used to handle queries forwarded from readers.
It is expressed as a percentage of the `max_connections` setting for the writer DB instance in the primary cluster. For example, if `max_connections` is `800`
and `apg_write_forward.max_forwarding_connections_percent` is `10`, then the writer allows a maximum of 80 simultaneous forwarded sessions. These connections come from the
same connection pool managed by the `max_connections` setting. This setting applies only on the primary cluster when at least one secondary clusters has write forwarding enabled.

Use the following settings on the secondary cluster:

- `apg_write_forward.consistency_mode` – A session-level parameter
  that controls the degree of read consistency on the secondary cluster. Valid values are
  `SESSION`, `EVENTUAL`, `GLOBAL`, or `OFF`.
  By default, the value is set to `SESSION`. Setting the value to
  `OFF` disables write forwarding in the session. To learn more about
  consistency levels, see [Isolation and consistency for write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-isolation-apg "#aurora-global-database-write-forwarding-isolation-apg"). This
  parameter is relevant only in reader instances of secondary clusters that have write
  forwarding enabled and that are in an Aurora global database.
- `apg_write_forward.connect_timeout` – The maximum number of seconds the
  secondary cluster waits when establishing a connection to the primary cluster before
  giving up. A value of `0` means to wait indefinitely.
- `apg_write_forward.idle_in_transaction_session_timeout` – The number of milliseconds the primary cluster waits for activity on a connection
  that's forwarded from a secondary cluster that has an open transaction before closing it. If the session remains idle in transaction beyond this period, Aurora terminates the session.
  A value of `0` disables the timeout.
- `apg_write_forward.idle_session_timeout` – The number of milliseconds the primary cluster waits for activity on a connection that's forwarded from a
  secondary cluster before closing it. If the session remains idle beyond this period, Aurora terminates the session. A value of `0` disables the timeout.

## Amazon CloudWatch metrics for write forwarding in Aurora PostgreSQL

The following Amazon CloudWatch metrics apply to the primary cluster when you use write forwarding
on one or more secondary clusters. These metrics are all measured on the writer DB instance
in the primary cluster.

| CloudWatch Metric                     | Units and description                                                                                       |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `AuroraForwardingWriterDMLThroughput` | Count (per second). Number of forwarded DML statements processed each second by<br>this writer DB instance. |
| `AuroraForwardingWriterOpenSessions`  | Count. Number of open sessions on this writer DB instance processing forwarded<br>queries.                  |
| `AuroraForwardingWriterTotalSessions` | Count. Total number of forwarded sessions on this writer DB instance.                                       |

The following CloudWatch metrics apply to each secondary cluster. These metrics are measured on each reader DB
instance in a secondary cluster with write forwarding enabled.

| CloudWatch Metric                           | Unit and description                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AuroraForwardingReplicaCommitThroughput`   | Count (per second). Number of commits in sessions forwarded by this replica each<br>second.                                                                                                                                                                                                                                                                                                                                                                               |
| `AuroraForwardingReplicaDMLLatency`         | Milliseconds. Average response time in milliseconds of forwarded DMLs on replica.                                                                                                                                                                                                                                                                                                                                                                                         |
| `AuroraForwardingReplicaDMLThroughput`      | Count (per second). Number of forwarded DML statements processed on this replica each second.                                                                                                                                                                                                                                                                                                                                                                             |
| `AuroraForwardingReplicaErrorSessionsLimit` | Count. Number of sessions rejected by the primary cluster because the limit for max connections or max write forward connections was reached.                                                                                                                                                                                                                                                                                                                             |
| `AuroraForwardingReplicaOpenSessions`       | Count. The number of sessions that are using write forwarding on a replica instance.                                                                                                                                                                                                                                                                                                                                                                                      |
| `AuroraForwardingReplicaReadWaitLatency`    | Milliseconds. Average wait time in milliseconds that the replica waits to be consistent with the LSN of the primary cluster. The<br>degree to which the reader DB instance waits depends on the `apg_write_forward.consistency_mode` setting. For information about this setting, see<br>[Configuration parameters for write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-params-apg "#aurora-global-database-write-forwarding-params-apg"). |

## Wait events for write forwarding in Aurora PostgreSQL

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
the secondary DB cluster is waiting for a connection to the writer node of the primary DB
cluster to be opened.

**Likely causes of increased waits**

This event increases as the number of connection attempts from a secondary Region's reader node to the writer node of the primary DB cluster increases.

**Actions**

Reduce the number of simultaneous connections from a secondary node to the primary Region's writer node.

### IPC:AuroraWriteForwardConsistencyPoint

The `IPC:AuroraWriteForwardConsistencyPoint` event describes how long a query
from a node on the secondary DB cluster will wait for the results of forwarded write
operations to be replicated to the current Region. This event is only generated if the
session-level parameter `apg_write_forward.consistency_mode` is set to one of
the following:

- `SESSION` – queries on a secondary node wait for the results of all changes made in that session.
- `GLOBAL` – queries on a secondary node wait for the results of changes made by that session, plus all committed changes from both the primary Region and other secondary Regions in the global cluster.

For more information about the `apg_write_forward.consistency_mode` parameter settings, see [Configuration parameters for write forwarding in Aurora PostgreSQL](#aurora-global-database-write-forwarding-params-apg "#aurora-global-database-write-forwarding-params-apg").

**Likely causes of increased waits**

Common causes for longer wait times include the following:

- Increased replica lag, as measured by the Amazon CloudWatch `ReplicaLag` metric. For more information about this metric, see [Monitoring Aurora PostgreSQL
  replication](AuroraPostgreSQL.md#AuroraPostgreSQL.Replication.Monitoring "AuroraPostgreSQL.md#AuroraPostgreSQL.Replication.Monitoring").
- Increased load on the primary Region's writer node or on the secondary node.

**Actions**

Change your consistency mode, depending on your application's requirements.

### IPC:AuroraWriteForwardExecute

The `IPC:AuroraWriteForwardExecute` event occurs when a backend process on
the secondary DB cluster is waiting for a forwarded query to complete and obtain results
from the writer node of the primary DB cluster.

**Likely causes of increased waits**

Common causes for increased waits include the following:

- Fetching a large number of rows from the primary Region's writer node.
- Increased network latency between the secondary node and primary Region's writer node increases the time it takes the secondary node to receive data from the writer node.
- Increased load on the secondary node can delay transmission of the query request from the secondary node to the primary Region's writer node.
- Increased load on the primary Region's writer node can delay transmission of data from the writer node to the secondary node.

**Actions**

We recommend different actions depending on the causes of your wait event.

- Optimize queries to retrieve only necessary data.
- Optimize data manipulation language (DML) operations to only modify necessary data.
- If the secondary node or primary Region's writer node is constrained by CPU or network bandwidth, consider changing it to an instance type with more CPU capacity or more network bandwidth.

### IPC:AuroraWriteForwardGetGlobalConsistencyPoint

The `IPC:AuroraWriteForwardGetGlobalConsistencyPoint` event occurs when a
backend process on the secondary DB cluster that's using the GLOBAL consistency mode is
waiting to obtain the global consistency point from the writer node before executing a
query.

**Likely causes of increased waits**

Common causes for increased waits include the following:

- Increased network latency between the secondary node and primary Region's writer node increases the time it takes the secondary node to receive data from the writer node.
- Increased load on the secondary node can delay transmission of the query request from the secondary node to the primary Region's writer node.
- Increased load on the primary Region's writer node can delay transmission of data from the writer node to the secondary node.

**Actions**

We recommend different actions depending on the causes of your wait event.

- Change your consistency mode, depending on your application's requirements.
- If the secondary node or primary Region's writer node is constrained by CPU or network bandwidth, consider changing it to an instance type with more CPU capacity or more network bandwidth.

### IPC:AuroraWriteForwardXactAbort

The `IPC:AuroraWriteForwardXactAbort` event occurs when a backend process on
the secondary DB cluster is waiting for the result of a remote cleanup query. Cleanup
queries are issued to return the process to the appropriate state after a write-forwarded
transaction is aborted. Amazon Aurora performs them either because an error was found or
because an user issued an explicit `ABORT` command or cancelled a running
query.

**Likely causes of increased waits**

Common causes for increased waits include the following:

- Increased network latency between the secondary node and primary Region's writer node increases the time it takes the secondary node to receive data from the writer node.
- Increased load on the secondary node can delay transmission of the cleanup query request from the secondary node to the primary Region's writer node.
- Increased load on the primary Region's writer node can delay transmission of data from the writer node to the secondary node.

**Actions**

We recommend different actions depending on the causes of your wait event.

- Investigate the cause of the aborted transaction.
- If the secondary node or primary Region's writer node is constrained by CPU or network bandwidth, consider changing it to an instance type with more CPU capacity or more network bandwidth.

### IPC:AuroraWriteForwardXactCommit

The `IPC:AuroraWriteForwardXactCommit` event occurs when a backend process on
the secondary DB cluster is waiting for the result of a forwarded commit transaction
command.

**Likely causes of increased waits**

Common causes for increased waits include the following:

- Increased network latency between the secondary node and primary Region's writer node increases the time it takes the secondary node to receive data from the writer node.
- Increased load on the secondary node can delay transmission of the query request from the secondary node to the primary Region's writer node.
- Increased load on the primary Region's writer node can delay transmission of data from the writer node to the secondary node.

**Actions**

If the secondary node or primary Region's writer node is constrained by CPU or network bandwidth, consider changing it to an instance type with more CPU capacity or more network bandwidth.

### IPC:AuroraWriteForwardXactStart

The `IPC:AuroraWriteForwardXactStart` event occurs when a backend process on
the secondary DB cluster is waiting for the result of a forwarded start transaction
command.

**Likely causes of increased waits**

Common causes for increased waits include the following:

- Increased network latency between the secondary node and primary Region's writer node increases the time it takes the secondary node to receive data from the writer node.
- Increased load on the secondary node can delay transmission of the query request from the secondary node to the primary Region's writer node.
- Increased load on the primary Region's writer node can delay transmission of data from the writer node to the secondary node.

**Actions**

If the secondary node or primary Region's writer node is constrained by CPU or network bandwidth, consider changing it to an instance type with more CPU capacity or more network bandwidth.
