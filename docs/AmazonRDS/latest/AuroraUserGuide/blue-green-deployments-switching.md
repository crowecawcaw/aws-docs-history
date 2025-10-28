# Switching a blue/green deployment in

Amazon Aurora

A _switchover_ transitions the DB cluster, including its
DB instances, in the green environment to be the production DB cluster. Before you switch over, production
traffic is routed to the cluster in the blue environment. After you switch over, production
traffic is routed to the DB cluster in the green environment.

_Switching over_ a blue/green deployment is not the same as
_promoting_ the green
DB cluster within the blue/green deployment. If you manually
promote the green
DB cluster by choosing **Promote** from the
**Actions** menu, replication between the blue and green environments breaks
and the blue/green deployment enters a state of **Invalid configuration**.

###### Topics

- [Switchover timeout](#blue-green-deployments-switching-timeout "#blue-green-deployments-switching-timeout")
- [Switchover guardrails](#blue-green-deployments-switching-guardrails "#blue-green-deployments-switching-guardrails")
- [Switchover actions](#blue-green-deployments-switching-actions "#blue-green-deployments-switching-actions")
- [Switchover best practices](#blue-green-deployments-switching-best-practices "#blue-green-deployments-switching-best-practices")
- [Verifying CloudWatch metrics
  before switchover](#blue-green-deployments-switching-over-cloudwatch "#blue-green-deployments-switching-over-cloudwatch")
- [Monitoring replica lag prior to
  switchover](#blue-green-deployments-monitor-replica-lag "#blue-green-deployments-monitor-replica-lag")
- [Switching over a blue/green deployment](#blue-green-deployments-switching-over "#blue-green-deployments-switching-over")
- [After switchover](#blue-green-deployments-switching-after "#blue-green-deployments-switching-after")

## Switchover timeout

You can specify a switchover timeout period between 30 seconds and 3,600 seconds
(one hour). If the switchover takes longer than the specified duration, then
any changes are rolled back and no changes are made to either environment. The default timeout
period is 300 seconds (five minutes).

## Switchover guardrails

When you start a switchover, Amazon RDS runs some basic checks to test the readiness of the
blue and green environments for switchover. These checks are known as _switchover
guardrails_. These switchover guardrails prevent a switchover if the environments
aren't ready for it. Therefore, they avoid longer than expected downtime and prevent the loss
of data between the blue and green environments that might result if the switchover started.

Amazon RDS runs the following guardrail checks on the green environment:

- **Replication health** – Checks if green
  DB cluster replication status is healthy. The green DB cluster is
  a replica of the blue DB cluster.
- **Replication lag** – Checks if the replica lag
  of the green
  DB cluster is within allowable limits for switchover. The
  allowable limits are based on the specified timeout period. Replica lag indicates how far
  the green DB cluster is lagging behind its blue DB cluster. For more information, see [Monitoring replica lag prior to
  switchover](#blue-green-deployments-monitor-replica-lag "#blue-green-deployments-monitor-replica-lag").
- **Active writes** – Makes sure there are no
  active writes on the green DB cluster.

Amazon RDS runs the following guardrail checks on the blue environment:

- **External replication** – For Aurora PostgreSQL, makes sure that the blue environment isn't a self-managed
  logical source (publisher) or replica (subscriber). If it is, we recommend that you drop
  the self-managed replication slots and subscriptions across all databases in the blue
  environment, proceed with switchover, then recreate them to resume replication. For
  Aurora MySQL, checks whether the blue database isn't an external binlog
  replica. If it is, make sure that it is not actively replicating.
- **Long-running active writes** – Makes sure
  there are no long-running active writes on the blue DB cluster because they can increase
  replica lag.
- **Long-running DDL statements** – Makes sure
  there are no long-running DDL statements on the blue DB cluster because they can increase
  replica lag.
- **Unsupported PostgreSQL changes** – For Aurora PostgreSQL, makes sure that no DDL
  changes and no additions or modifications of large objects have been performed on the blue
  environment. For more information, see [Logical replication-specific
  limitations for blue/green deployments](blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres "blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres").

If Amazon RDS detects unsupported PostgreSQL changes, it changes the replication state to
`Replication degraded` and notifies you that switchover is not available for
the blue/green deployment. To proceed with switchover, we recommend that you delete and
recreate the blue/green deployment and all green databases. To do so, choose
**Actions**, **Delete with green databases**.

## Switchover actions

When you switch over a blue/green deployment, RDS performs the following actions:

1. Runs guardrail checks to verify if the blue and green environments are ready for switchover.
2. Stops new write operations on the
   DB cluster in both environments.
3. Drops connections to the DB instances in both environments and doesn't allow new connections.
4. Waits for replication to catch up in the green environment so that the green environment
   is in sync with the blue environment.
5. Renames the DB
   cluster and DB instances in the both environments.

RDS renames the DB
cluster and DB instances in the green environment to match the corresponding
DB cluster and DB instances in the
blue environment. For example, assume the name of a DB instance in the blue environment is
`mydb`. Also assume the name of the corresponding DB instance in the green environment is
`mydb-green-abc123`. During switchover, the name of the DB instance in the green environment is
changed to `mydb`.

RDS renames the DB
cluster and DB instances in the blue environment by
appending `-old`n`to the current name, where
`n``is a number. For example, assume the name of
 a DB instance in the blue environment is`mydb`. After switchover, the DB
 instance name might be `mydb-old1`.

RDS also renames the endpoints in the green environment to match the corresponding endpoints in the
blue environment so that application changes aren't required. 6. Allows connections to databases in both environments. 7. Allows write operations on the
DB cluster in the new production environment.

After switchover, the previous production
DB cluster only allows read operations. Even if you enable writes on the DB cluster, it remains read-only until
you delete the blue/green deployment.

You can monitor the status of a switchover using Amazon EventBridge. For more information, see [Blue/green deployment events](USER_Events.md#USER_Events.Messages.BlueGreenDeployments "USER_Events.md#USER_Events.Messages.BlueGreenDeployments").

During switchover, tags from the blue environment replace all tags on resources in the
green environment. Any tags that you added directly to green environment resources are
overwritten during this process. For more information about tags, see [Tagging Amazon Aurora and Amazon RDS resources](USER_Tagging.md "USER_Tagging.md").

If the switchover starts and then stops before finishing for any reason, then any changes are rolled back,
and no changes are made to either environment.

## Switchover best practices

Before you switch over, we strongly recommend that you adhere to best practices by
completing the following tasks:

- Thoroughly test the resources in the green environment. Make sure they function properly
  and efficiently.
- Monitor relevant Amazon CloudWatch metrics. For more information, see [Verifying CloudWatch metrics
  before switchover](#blue-green-deployments-switching-over-cloudwatch "#blue-green-deployments-switching-over-cloudwatch").
- Identify the best time for the switchover.

During the switchover, writes are cut off from databases in both environments.
Identify a time when traﬃc is lowest on your production environment. Long-running
transactions, such as active DDLs, can increase your switchover time, resulting in longer
downtime for your production workloads.

If there's a large number of connections on your DB cluster and DB instances, consider manually
reducing them to the minimum amount necessary for your application before you switch over
the blue/green deployment. One way to achieve this is to create a script that monitors the
status of the blue/green deployment and starts cleaning up connections when it detects
that the status has changed to `SWITCHOVER_IN_PROGRESS`.

- Make sure the DB cluster and DB instances
  in both environments are in `Available` state.
- Make sure the
  DB cluster in the green environment is healthy and replicating.
- Make sure that your network and client configurations don’t increase the DNS cache
  Time-To-Live (TTL) beyond five seconds, which is the default for Aurora DNS zones.

Otherwise, applications will continue to send write traffic to the blue environment after

switchover.

- For Aurora PostgreSQL blue/green deployments, do the following:
  - Review the logical replication limitations and take any required actions prior to
    switchover. For more information, see [Logical replication-specific
    limitations for blue/green deployments](blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres "blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres").
  - Run the `ANALYZE` operation to refresh the `pg_statistics`
    table. This reduces the risk of performance issues after switchover.

###### Note

During a switchover, you can't modify any DB
cluster included in the switchover.

## Verifying CloudWatch metrics

before switchover

Before you switch over a blue/green deployment, we recommend that you check the
values of the following metrics within
Amazon CloudWatch.

- `DatabaseConnections` – Use this metric to estimate the level of
  activity on the blue/green deployment, and make sure that the value is at an acceptable
  level for your deployment before you switch over. If Performance Insights is turned on,
  `DBLoad` is a more accurate metric.
- `ActiveTransactions` – If `innodb_monitor_enable` is set
  to `all` in the DB parameter group for any of your DB instances, use this
  metric to see if there's a high number of active transactions that might block
  switchover.

For more information, see [Amazon CloudWatch metrics for Amazon Aurora](Aurora.AuroraMonitoring.md "Aurora.AuroraMonitoring.md").

## Monitoring replica lag prior to

switchover

Before you switch over a blue/green deployment, make sure that replica lag is close to
zero in order to reduce downtime.

### Aurora MySQL

For MySQL blue/green deployments,
check the `AuroraBinlogReplicaLag` CloudWatch metric in the green
environment to identify the current replica lag. For more information, see [Diagnosing and resolving lag
between read replicas](CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.ReplicaLag "CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.ReplicaLag").

### Aurora PostgreSQL

For PostgreSQL blue/green deployments, check the `OldestReplicationSlotLag` CloudWatch metric in the
blue environment to identify the current replica lag. For more information, see [Instance-level metrics for Amazon Aurora](Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances "Aurora.AuroraMonitoring.md#Aurora.AuroraMySQL.Monitoring.Metrics.instances").

In addition, you can run the following SQL query in the blue
environment:

```
SELECT slot_name,
       confirmed_flush_lsn as flushed,
       pg_current_wal_lsn(),
       (pg_current_wal_lsn() - confirmed_flush_lsn) AS lsn_distance
FROM pg_catalog.pg_replication_slots
WHERE slot_type = 'logical';

slot_name        |    flushed    | pg_current_wal_lsn | lsn_distance
-----------------+---------------+--------------------+------------
logical_replica1 | 47D97/CF32980 | 47D97/CF3BAC8      | 37192
```

The `confirmed_flush_lsn` represents the last log sequence number (LSN) that
was sent to the replica. The `pg_current_wal_lsn` represents where the database
is now. An `lsn_distance` of 0 means that the replica is caught up.

## Switching over a blue/green deployment

You can switch over a blue/green deployment using the AWS Management Console, the AWS CLI, or the RDS API.

###### To switch over a blue/green deployment

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the blue/green deployment that you want
   to switch over.
3. For **Actions**, choose **Switch over**.

The **Switch over** page appears.

![Switch over blue/green deployment](images/blue-green-deployment-switch-over-aurora.png) 4. On the **Switch over** page, review the switchover summary. Make sure
the resources in both environments match what you expect. If they don't, choose
**Cancel**. 5. For **Timeout settings**, enter the time limit for
switchover. 6. If your cluster is running
Aurora PostgreSQL, review and acknowledge the pre-switchover recommendations.
For more information, see [Logical replication-specific
limitations for blue/green deployments](blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres "blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres"). 7. Choose **Switch over**.
To switch over a blue/green deployment by using the AWS CLI, use the [switchover-blue-green-deployment](../../../cli/latest/reference/rds/switchover-blue-green-deployment.md "../../../cli/latest/reference/rds/switchover-blue-green-deployment.md") command with the following options:

- `--blue-green-deployment-identifier` – Specify the resource ID
  of the blue/green deployment.
- `--switchover-timeout` – Specify the time limit for the switchover, in seconds. The default is

300.

###### Example Switch over a blue/green deployment

For Linux, macOS, or Unix:

```
aws rds switchover-blue-green-deployment \
    --blue-green-deployment-identifier `bgd-1234567890abcdef` \
    --switchover-timeout `600`
```

For Windows:

```
aws rds switchover-blue-green-deployment ^
    --blue-green-deployment-identifier `bgd-1234567890abcdef` ^
    --switchover-timeout `600`
```

To switch over a blue/green deployment by using the Amazon RDS API, use the [`SwitchoverBlueGreenDeployment`](../APIReference/API_SwitchoverBlueGreenDeployment.md "../APIReference/API_SwitchoverBlueGreenDeployment.md") operation with the following parameters:

- `BlueGreenDeploymentIdentifier` – Specify the resource ID of
  the blue/green deployment.
- `SwitchoverTimeout` – Specify the time limit for the switchover, in seconds. The default is

300.

## After switchover

After a switchover, the DB cluster and DB instances
in the previous blue environment are retained. Standard costs apply to these resources. Replication and
binary logging between the blue and green environments stops.

RDS renames the DB cluster and DB instances in the blue environment by appending
`-old`n`to the current resource name, where
`n`` is a number. 
 The blue DB cluster is forced into a read-only state. Even if you enable
 write operations, it remains read-only until you delete the blue/green deployment.
 RDS names the DB cluster and DB instances in the green environment
 `-new`n``.

If you delete the blue/green deployment resource, RDS retains the
`-old`n`` and
 `-new`n`` resources.

![After switching over a blue/green deployment](images/blue-green-deployment-after-switchover-aurora.png)

### Updating the parent node for

consumers

RDS offers fully managed read replicas. However, it also provides the option to set up
self-managed replicas, also known as _external replicas._ External
replicas allow you to use third-party resources as replication targets.

After you switch over an Aurora MySQL blue/green deployment,
if the blue
DB cluster had any external replicas or binary log consumers
prior to switchover, you must update their parent node after switchover in order to maintain
replication continuity.

###### To update the parent node

1. After switchover, the writer DB instance that was
   previously in the green environment emits an event that contains the master log file
   name and master log position. To locate the event, navigate to the RDS console and
   choose **Events** from the left navigation pane.
2. Filter by events where the source is the name of the old green writer DB instance, before switchover.
3. Locate the event that contains the binary log coordinates. The event message is
   similar to: `Binary log coordinates in green environment after switchover: file
mysql-bin-changelog.`000003`and position`40134574``.
4. Make sure that the consumer or replica has applied all binary logs from the old blue
   environment. Then, use the provided binary log coordinates to resume replication on the
   consumers. For example, if you're running a MySQL replica on EC2, you can use the
   following commands:

**MySQL 8.0.22 and lower major and minor
versions**

```
CHANGE MASTER TO MASTER_HOST='`{new-writer-endpoint}`', MASTER_LOG_FILE='mysql-bin-changelog.`000003`', MASTER_LOG_POS=`40134574`;
```

**MySQL 8.0.23 and higher major and minor
versions**

```
CHANGE REPLICATION SOURCE TO SOURCE_HOST='`{new-writer-endpoint}`', SOURCE_LOG_FILE='mysql-bin-changelog.`000003`', SOURCE_LOG_POS=`40134574`;
```
