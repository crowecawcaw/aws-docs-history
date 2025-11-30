# Promoting an RDS Custom for Oracle replica to a standalone DB instance

Just as with RDS for Oracle, you can promote an RDS Custom for Oracle replica to a standalone DB instance. When you promote a Oracle replica, RDS Custom for Oracle
reboots the DB instance before it becomes available. For more information about promoting Oracle replicas, see [Promoting a read replica to be a standalone
DB instance](USER_ReadRepl.md "USER_ReadRepl.md").

When promoting a replica, note the following guidelines:

- Don't initiate a failover while RDS Custom for Oracle is promoting your replica.
  Otherwise, the promotion workflow could become stuck.
- Don't switch over your primary DB instance while RDS Custom for Oracle is promoting your Oracle
  replica. Otherwise, the promotion workflow could become stuck.
- Don't shut down your primary DB instance while RDS Custom for Oracle is promoting your Oracle
  replica. Otherwise, the promotion workflow could become stuck.
- Don't try to restart replication with your newly promoted DB instance as a target.
  After RDS Custom for Oracle promotes your Oracle replica, it becomes a standalone DB instance and
  no longer has the replica role.
  Note the following limitations for RDS Custom for Oracle replica promotion:

- You can't promote a replica while RDS Custom for Oracle is backing it up.
- You can't change the backup retention period to `0` when you
  promote your Oracle replica.
- You can't promote your replica when it isn't in a healthy state.

If you issue `delete-db-instance` on the primary DB instance, RDS Custom for Oracle
validates that each managed Oracle replica is healthy and available for
promotion. A replica might be ineligible for promotion because automation is
paused or it is outside the support perimeter. In such cases, RDS Custom for Oracle
publishes an event explaining the issue so that you can repair your Oracle
replica manually.
The following steps show the general process for promoting a Oracle replica to a DB instance:

1. Stop any transactions from being written to the primary DB instance.
2. Wait for RDS Custom for Oracle to apply all updates to your Oracle replica.
3. Promote your Oracle replica by choosing the **Promote** option on the Amazon RDS console, the AWS CLI command [`promote-read-replica`](../../../cli/latest/reference/rds/promote-read-replica.md "../../../cli/latest/reference/rds/promote-read-replica.md"), or the [`PromoteReadReplica`](../APIReference/API_PromoteReadReplica.md "../APIReference/API_PromoteReadReplica.md") Amazon RDS API operation.
   Promoting a Oracle replica takes a few minutes to complete. During the process,
   RDS Custom for Oracle stops replication and reboots your replica. When the reboot completes, the
   Oracle replica is available as a standalone DB instance. For information about troubleshooting
   replica promotion, see [Troubleshooting replica promotion for RDS Custom for Oracle](custom-troubleshooting.md#custom-troubleshooting-promote "custom-troubleshooting.md#custom-troubleshooting-promote").

###### To promote an RDS Custom for Oracle replica to a standalone DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the Amazon RDS console, choose **Databases**.

The **Databases** pane appears. Each Oracle replica shows **Replica** in the
**Role** column. 3. Choose the RDS Custom for Oracle replica that you want to promote. 4. For **Actions**, choose **Promote**. 5. On the **Promote Oracle replica** page, enter the backup retention period and the backup window for the
newly promoted DB instance. You can't set this value to **0**. 6. When the settings are as you want them, choose **Promote Oracle replica**.
To promote your RDS Custom for Oracle replica to a standalone DB instance, use the AWS CLI [`promote-read-replica`](../../../cli/latest/reference/rds/promote-read-replica.md "../../../cli/latest/reference/rds/promote-read-replica.md") command.

###### Example

For Linux, macOS, or Unix:

```
aws rds promote-read-replica \
--db-instance-identifier `my-custom-read-replica` \
--backup-retention-period 2 \
--preferred-backup-window 23:00-24:00
```

For Windows:

```
aws rds promote-read-replica ^
--db-instance-identifier `my-custom-read-replica` ^
--backup-retention-period 2 ^
--preferred-backup-window 23:00-24:00
```

To promote your RDS Custom for Oracle replica to be a standalone DB instance, call the Amazon RDS API [`PromoteReadReplica`](../APIReference/API_PromoteReadReplica.md "../APIReference/API_PromoteReadReplica.md") operation with the required parameter `DBInstanceIdentifier`.
