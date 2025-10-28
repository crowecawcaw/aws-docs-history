# Modifying the RDS for Db2 replica

mode

You can change the replica mode of an existing Db2 replica between read-only and standby
modes. This flexibility allows you to adapt your replica configuration based on changing
requirements for read workloads or disaster recovery needs.

You might want to change replica modes in the following scenarios:

- **Read-only to standby** – When you no longer
  need read capacity but want to maintain disaster recovery capabilities
- **Standby to read-only** – When you need to
  add read capacity for reporting or analytics workloads
  Before changing replica modes, make sure the following conditions are met:

- The replica is in an available state.
- No active maintenance operations are running on the replica.
- You have the necessary permissions to modify the DB instance.
  The change operation can take a few minutes. During the operation, the DB instance status
  changes to **modifying**. For more information about status changes, see
  [Viewing Amazon RDS DB instance status](accessing-monitoring.md#Overview.DBInstance.Status "accessing-monitoring.md#Overview.DBInstance.Status").
  When you change from read-only to standby mode, the replica disconnects all active
  connections.

###### Important

Because changing replica modes temporarily interrupts service, plan the change during
a maintenance window to minimize impact on your applications.

You can modify the replica mode using the AWS Management Console, the AWS CLI, or the RDS API.

###### To change the replica mode of a Db2 replica

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the replica database that you want to modify.
4. Choose **Modify**.
5. For **Replica mode**, choose the desired mode:
   - **Read-only** – For read workloads
   - **Standby** – For disaster recovery

6. Choose the other settings that you want to change.
7. Choose **Continue**.
8. For **Scheduling of modifications**, choose
   **Apply immediately**.
9. Choose **Modify DB instance**.
10. After the modification completes, verify the replica mode change in the
    **Databases** page. The replica status should show as
    **Available** when the change is complete.
    To change a Db2 replica from read-only mode to standby mode, set
    `--replica-mode` to `mounted` in the AWS CLI command [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"). To change a Db2 replica from standby mode to
    read-only mode, set `--replica-mode` to
    `open-read-only`.

The following example changes a replica from read-only to standby mode:

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my_db2_replica` \
    --replica-mode mounted
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my_db2_replica` ^
    --replica-mode mounted
```

The following example changes a replica from standby to read-only mode:

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `my_db2_replica` \
    --replica-mode open-read-only
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `my_db2_replica` ^
    --replica-mode open-read-only
```

To change a Db2 replica from read-only mode to standby mode, set
`ReplicaMode=mounted` in [ModifyDBInstance](AmazonRDS/latest/APIReference/API_ModifyDBInstance.md "AmazonRDS/latest/APIReference/API_ModifyDBInstance.md"). To change a Db2 replica from standby mode to
read-only mode, set `ReplicaMode=open-read-only`.

The following is an example API call to change the replica mode from read-only to
standby:

```
{
    "DBInstanceIdentifier": "my_db2_replica",
    "ReplicaMode": "mounted",
    "ApplyImmediately": true
}
```

The following is an example API call to change the replica mode from standby to
read-only:

```
{
    "DBInstanceIdentifier": "my_db2_replica",
    "ReplicaMode": "open-read-only",
    "ApplyImmediately": true
}
```

For information about the differences between replica modes, see [Working with replicas for Amazon RDS for Db2](db2-replication.md "db2-replication.md"). For troubleshooting replica
issues, see [Troubleshooting RDS for Db2 replication
issues](db2-troubleshooting-replicas.md "db2-troubleshooting-replicas.md").
