

# Switching a blue/green deployment in Amazon RDS
<a name="blue-green-deployments-switching"></a>

A *switchover* transitions the green environment to be the new production environment. When the green DB instance has read replicas, they are also transitioned. Before you switch over, production traffic is routed to the DB instance and read replicas in the blue environment. After you switch over, production traffic is routed to the DB instance and read replicas in the green environment.

*Switching over* a blue/green deployment is not the same as *promoting* the green DB instance within the blue/green deployment. If you manually promote the green DB instance by choosing **Promote** from the **Actions** menu, replication between the blue and green environments breaks and the blue/green deployment enters a state of **Invalid configuration**. 

**Topics**
+ [Switchover timeout](#blue-green-deployments-switching-timeout)
+ [Switchover guardrails](#blue-green-deployments-switching-guardrails)
+ [Switchover actions](#blue-green-deployments-switching-actions)
+ [Switchover when using Amazon RDS Proxy](#blue-green-deployments-switching-rds-proxy)
+ [Switchover best practices](#blue-green-deployments-switching-best-practices)
+ [Verifying CloudWatch metrics before switchover](#blue-green-deployments-switching-over-cloudwatch)
+ [Monitoring replica lag prior to switchover](#blue-green-deployments-monitor-replica-lag)
+ [Switching over a blue/green deployment](#blue-green-deployments-switching-over)
+ [After switchover](#blue-green-deployments-switching-after)

## Switchover timeout
<a name="blue-green-deployments-switching-timeout"></a>

You can specify a switchover timeout period between 30 seconds and 3,600 seconds (one hour). If the switchover takes longer than the specified duration, then any changes are rolled back and no changes are made to either environment. The default timeout period is 300 seconds (five minutes).

## Switchover guardrails
<a name="blue-green-deployments-switching-guardrails"></a>

When you start a switchover, Amazon RDS runs some basic checks to test the readiness of the blue and green environments for switchover. These checks are known as *switchover guardrails*. These switchover guardrails prevent a switchover if the environments aren't ready for it. Therefore, they avoid longer than expected downtime and prevent the loss of data between the blue and green environments that might result if the switchover started.

Amazon RDS runs the following guardrail checks on the green environment:
+ **Replication health** – Checks if green primary DB instance replication status is healthy. The green primary DB instance is a replica of the blue primary DB instance.
+ **Replication lag** – Checks if the replica lag of the green primary DB instance is within allowable limits for switchover. The allowable limits are based on the specified timeout period. Replica lag indicates how far the green primary DB instance is lagging behind its blue primary DB instance. For more information, see [Monitoring replica lag prior to switchover](#blue-green-deployments-monitor-replica-lag).
+ **Active writes** – Makes sure there are no active writes on the green primary DB instance.

Amazon RDS runs the following guardrail checks on the blue environment:
+ **External replication** – For RDS for PostgreSQL, makes sure that the blue environment isn't a self-managed logical source (publisher) or replica (subscriber). If it is, we recommend that you drop the self-managed replication slots and subscriptions across all databases in the blue environment, proceed with switchover, then recreate them to resume replication. For RDS for MySQL and RDS for MariaDB, checks whether the blue database isn't an external binlog replica. If it is, make sure that it is not actively replicating.
+ **Long-running active writes** – Makes sure there are no long-running active writes on the blue primary DB instance because they can increase replica lag.
+ **Long-running DDL statements** – Makes sure there are no long-running DDL statements on the blue primary DB instance because they can increase replica lag.
+ **Unsupported PostgreSQL changes** – For RDS for PostgreSQL blue/green deployments that use logical replication, makes sure that no DDL changes and no additions or modifications of large objects have been performed on the blue environment. For more information, see [Logical replication-specific limitations for blue/green deployments](blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres).

  If Amazon RDS detects unsupported PostgreSQL changes, it changes the replication state to `Replication degraded` and notifies you that switchover is not available for the blue/green deployment. To proceed with switchover, we recommend that you delete and recreate the blue/green deployment and all green databases. To do so, choose **Actions**, **Delete with green databases**.

## Switchover actions
<a name="blue-green-deployments-switching-actions"></a>

When you switch over a blue/green deployment, RDS performs the following actions:

1. Runs guardrail checks to verify if the blue and green environments are ready for switchover.

1. Stops new write operations on the primary DB instance in both environments.

1. Drops connections to the DB instances in both environments and doesn't allow new connections.

1. Waits for replication to catch up in the green environment so that the green environment is in sync with the blue environment.

1. Renames the DB instances in the both environments.

   RDS renames the DB instances in the green environment to match the corresponding DB instances in the blue environment. For example, assume the name of a DB instance in the blue environment is `mydb`. Also assume the name of the corresponding DB instance in the green environment is `mydb-green-abc123`. During switchover, the name of the DB instance in the green environment is changed to `mydb`.

   RDS renames the DB instances in the blue environment by appending `-old{{n}}` to the current name, where `{{n}}` is a number. For example, assume the name of a DB instance in the blue environment is `mydb`. After switchover, the DB instance name might be `mydb-old1`.

   RDS also renames the endpoints in the green environment to match the corresponding endpoints in the blue environment so that application changes aren't required.

1. Allows connections to databases in both environments.

1. Allows write operations on the primary DB instance in the new production environment.

   After switchover, the previous production primary DB instance only allows read operations until you set the `read_only` parameter (for RDS for MySQL) or the `default_transaction_read_only` parameter (for RDS for PostgreSQL) to `0` and reboot the DB instance. 

You can monitor the status of a switchover using Amazon EventBridge. For more information, see [Blue/green deployment events](USER_Events.Messages.md#USER_Events.Messages.BlueGreenDeployments).

During switchover, tags from the blue environment replace all tags on resources in the green environment. Any tags that you added directly to green environment resources are overwritten during this process. For more information about tags, see [Tagging Amazon RDS resources](USER_Tagging.md).

If the switchover starts and then stops before finishing for any reason, then any changes are rolled back, and no changes are made to either environment.

## Switchover when using Amazon RDS Proxy
<a name="blue-green-deployments-switching-rds-proxy"></a>

In addition to the above mentioned switchover actions, if the blue cluster is a target of an Amazon RDS Proxy, the following behavior applies during switchover:
+ Switchover Guardrails
  + Amazon RDS runs additional guardrail checks to validate that the proxy can successfully reach both blue and green environments and is ready for switchover.
+ Application Traffic Routing During Switchover
  + During switchover, the Blue database enters read-only mode before Green environment is promoted. Amazon RDS Proxy continues routing connections to the blue database during this transitional period.
  + Write operations on RDS for MySQL and RDS for MariaDB during this period may return read-only errors. For example, `1290 (HY000): The MySQL server is running with the --read-only option` so it cannot execute this statement. On RDS for PostgreSQL, read and write queries will return `AdminShutdown: terminating connection due to administrator command`.
  + Once the switchover is detected, the proxy routes traffic to the newly promoted green environment.
  + When the Green environment is promoted as the new writer, existing connections to the proxy are dropped. Applications must re-establish connections after the promotion is complete.
  + You can review CloudWatch logs for Amazon RDS Proxy to see when this transitional behavior occurred.
+ RDS Proxy API Behavior
  + Proxy APIs such as `describe-db-proxy-targets` reflect the updated targets only after the switchover is fully complete, even though traffic routing occurs earlier.

## Switchover best practices
<a name="blue-green-deployments-switching-best-practices"></a>

Before you switch over, we strongly recommend that you adhere to best practices by completing the following tasks:
+ Thoroughly test the resources in the green environment. Make sure they function properly and efficiently.
+ Monitor relevant Amazon CloudWatch metrics. For more information, see [Verifying CloudWatch metrics before switchover](#blue-green-deployments-switching-over-cloudwatch).
+ Identify the best time for the switchover.

  During the switchover, writes are cut off from databases in both environments. Identify a time when traﬃc is lowest on your production environment. Long-running transactions, such as active DDLs, can increase your switchover time, resulting in longer downtime for your production workloads.

  If there's a large number of connections on your DB instances, consider manually reducing them to the minimum amount necessary for your application before you switch over the blue/green deployment. One way to achieve this is to create a script that monitors the status of the blue/green deployment and starts cleaning up connections when it detects that the status has changed to `SWITCHOVER_IN_PROGRESS`.
+ Make sure the DB instances in both environments are in `Available` state.
+ Make sure the primary DB instance in the green environment is healthy and replicating.
+ Make sure that your network and client configurations don’t increase the DNS cache Time-To-Live (TTL) beyond five seconds, which is the default for RDS DNS zones. Otherwise, applications will continue to send write traffic to the blue environment after switchover.
+ Make sure data loading is complete before switching over. For more information, see [Lazy loading and storage initialization for blue/green deployments](blue-green-deployments-creating.md#blue-green-deployments-creating-lazy-loading).
+ For RDS for PostgreSQL blue/green deployments that use logical replication, do the following:
  + Review the logical replication limitations and take any required actions prior to switchover. For more information, see [Logical replication-specific limitations for blue/green deployments](blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres).
  + Run the `ANALYZE` operation to refresh the `pg_statistics` table. This reduces the risk of performance issues after switchover.
  + Before initiating a blue/green deployment switchover, verify that your application does not override the `default_transaction_read_only` parameter at the session level. During switchover, this parameter is set to `on` on the green environment writer to prevent writes until promotion completes. If your application or transactions override this configuration to `off`, your application may write data to the green environment during the switchover process. In the event the switchover has to roll back, these writes are not available in the blue environment, requiring you to manually resolve the data inconsistencies. We strongly recommend auditing your application queries to ensure they respect the `default_transaction_read_only` setting before proceeding with switchover.

**Note**  
During a switchover, you can't modify any DB instances included in the switchover.

## Verifying CloudWatch metrics before switchover
<a name="blue-green-deployments-switching-over-cloudwatch"></a>

Before you switch over a blue/green deployment, we recommend that you check the value of the following metric within Amazon CloudWatch.
+ `DatabaseConnections` – Use this metric to estimate the level of activity on the blue/green deployment, and make sure that the value is at an acceptable level for your deployment before you switch over. If Performance Insights is turned on, `DBLoad` is a more accurate metric.

For more information, see [Amazon CloudWatch metrics for Amazon RDS](rds-metrics.md).

## Monitoring replica lag prior to switchover
<a name="blue-green-deployments-monitor-replica-lag"></a>

Before you switch over a blue/green deployment, make sure that replica lag is close to zero in order to reduce downtime.

### RDS for MySQL and RDS for MariaDB
<a name="blue-green-deployments-monitor-replica-lag-ms-mdb"></a>

For MySQL and MariaDB blue/green deployments, check the `ReplicaLag` CloudWatch metric in the green environment to identify the current replica lag. For more information, see [Diagnosing and resolving lag between read replicas](CHAP_Troubleshooting.md#CHAP_Troubleshooting.MySQL.ReplicaLag).

### RDS for PostgreSQL
<a name="blue-green-deployments-monitor-replica-lag-pg"></a>

For PostgreSQL blue/green deployments that use physical replication, see [Monitoring and tuning the replication process](USER_PostgreSQL.Replication.ReadReplicas.Monitor.md) for instructions to identify the current replica lag.

For PostgreSQL blue/green deployments that use logical replication, check the `OldestReplicationSlotLag` CloudWatch metric in the blue environment to identify the current replica lag. For more information, see [Amazon CloudWatch instance-level metrics for Amazon RDS](rds-metrics.md#rds-cw-metrics-instance).

In addition, you can run the following SQL query in the blue environment:

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

The `confirmed_flush_lsn` represents the last log sequence number (LSN) that was sent to the replica. The `pg_current_wal_lsn` represents where the database is now. An `lsn_distance` of 0 means that the replica is caught up.

For an explanation of when blue/green deployments use physical replication versus logical replication, see [PostgreSQL replication methods for blue/green deployments](blue-green-deployments-replication-type.md).

## Switching over a blue/green deployment
<a name="blue-green-deployments-switching-over"></a>

You can switch over a blue/green deployment using the AWS Management Console, the AWS CLI, or the RDS API.

### Console
<a name="blue-green-deployments-switching-console"></a>

**To switch over a blue/green deployment**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then choose the blue/green deployment that you want to switch over.

1. For **Actions**, choose **Switch over**.

   The **Switch over** page appears.  
![Switch over blue-green deployment.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/blue-green-deployment-switch-over.png)

1. On the **Switch over** page, review the switchover summary. Make sure the resources in both environments match what you expect. If they don't, choose **Cancel**.

1. For **Timeout settings**, enter the time limit for switchover.

1. If your instance is running RDS for PostgreSQL, review and acknowledge the pre-switchover recommendations. For more information, see [Logical replication-specific limitations for blue/green deployments](blue-green-deployments-considerations.md#blue-green-deployments-limitations-postgres).

1. Choose **Switch over**.

### AWS CLI
<a name="blue-green-deployments-switching-cli"></a>

To switch over a blue/green deployment by using the AWS CLI, use the [switchover-blue-green-deployment](https://docs.aws.amazon.com/cli/latest/reference/rds/switchover-blue-green-deployment.html) command with the following options:
+ `--blue-green-deployment-identifier` – Specify the resource ID of the blue/green deployment.
+ `--switchover-timeout` – Specify the time limit for the switchover, in seconds. The default is 300.

**Example Switch over a blue/green deployment**  
For Linux, macOS, or Unix:  

```
aws rds switchover-blue-green-deployment \
    --blue-green-deployment-identifier {{bgd-1234567890abcdef}} \
    --switchover-timeout {{600}}
```
For Windows:  

```
aws rds switchover-blue-green-deployment ^
    --blue-green-deployment-identifier {{bgd-1234567890abcdef}} ^
    --switchover-timeout {{600}}
```

### RDS API
<a name="blue-green-deployments-switching-api"></a>

To switch over a blue/green deployment by using the Amazon RDS API, use the [`SwitchoverBlueGreenDeployment`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SwitchoverBlueGreenDeployment.html) operation with the following parameters:
+ `BlueGreenDeploymentIdentifier` – Specify the resource ID of the blue/green deployment.
+ `SwitchoverTimeout` – Specify the time limit for the switchover, in seconds. The default is 300.

## After switchover
<a name="blue-green-deployments-switching-after"></a>

After a switchover, the DB instances in the previous blue environment are retained. Standard costs apply to these resources. Replication between the blue and green environments stops.

RDS renames the DB instances in the blue environment by appending `-old{{n}}` to the current resource name, where `{{n}}` is a number. The DB instances in the old blue environment are read-only until you set the `read_only` parameter (for RDS for MySQL) or the `default_transaction_read_only` parameter (for RDS for PostgreSQL) to `0`.  RDS names the DB instances in the green environment `-new{{n}}`.

If you delete the blue/green deployment resource, RDS retains the `-old{{n}}` and `-new{{n}}` resources.

![After switching over a blue-green deployment.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/blue-green-deployment-after-switchover.png)


### Updating the parent node for consumers
<a name="blue-green-deployments-switching-reparent"></a>

RDS offers fully managed read replicas. However, it also provides the option to set up self-managed replicas, also known as *external replicas.* External replicas allow you to use third-party resources as replication targets.

After you switch over an RDS for MariaDB or RDS for MySQL blue/green deployment, if the blue DB instance had any external replicas or binary log consumers prior to switchover, you must update their parent node after switchover in order to maintain replication continuity. 

**To update the parent node**

1. After switchover, the DB instance that was previously in the green environment emits an event that contains the master log file name and master log position. To locate the event, navigate to the RDS console and choose **Events** from the left navigation pane.

1. Filter by events where the source is the name of the old green DB instance, before switchover.

1. Locate the event that contains the binary log coordinates. The event message is similar to: `Binary log coordinates in green environment after switchover: file mysql-bin-changelog.{{000003}} and position {{40134574}}`.

1. Make sure that the consumer or replica has applied all binary logs from the old blue environment. Then, use the provided binary log coordinates to resume replication on the consumers. For example, if you're running a MySQL replica on EC2, you can use the following commands:

   **MySQL 8.0.22 and lower major and minor versions**

   ```
   CHANGE MASTER TO MASTER_HOST='{{{new-writer-endpoint}}}', MASTER_LOG_FILE='mysql-bin-changelog.{{000003}}', MASTER_LOG_POS={{40134574}};
   ```

   **MySQL 8.0.23 and higher major and minor versions**

   ```
   CHANGE REPLICATION SOURCE TO SOURCE_HOST='{{{new-writer-endpoint}}}', SOURCE_LOG_FILE='mysql-bin-changelog.{{000003}}', SOURCE_LOG_POS={{40134574}};
   ```

If the consumer is another RDS for MySQL or RDS for MariaDB DB instance, run the following stored procedures in order: 

1. [mysql.rds\_stop\_replication](mysql-stored-proc-replicating.md#mysql_rds_stop_replication)

1. [mysql.rds\_reset\_external\_master](mysql-stored-proc-replicating.md#mysql_rds_reset_external_master) (for version 8.0 and lower) or [mysql\_rds\_reset\_external\_source](mysql-stored-proc-replicating.md#mysql_rds_reset_external_source) (for version 8.4 and higher)

1. [mysql.rds\_set\_external\_master](mysql-stored-proc-replicating.md#mysql_rds_set_external_master) (for version 8.0 and lower) or [mysql\_rds\_set\_external\_source](mysql-stored-proc-replicating.md#mysql_rds_set_external_source) (for version 8.4 and higher)

1. [mysql.rds\_start\_replication](mysql-stored-proc-replicating.md#mysql_rds_start_replication)