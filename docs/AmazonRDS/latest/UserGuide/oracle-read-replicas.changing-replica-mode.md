# Modifying the RDS for Oracle replica mode

To change the replica mode of an existing replica, use the console, AWS CLI, or RDS API. When you change to
mounted mode, the replica disconnects all active connections. When you change to read-only mode, Amazon RDS
initializes Active Data Guard.

The change operation can take a few minutes. During the operation, the DB instance status changes to
**modifying**. For more information about status changes, see [Viewing Amazon RDSDB instance status](accessing-monitoring.md#Overview.DBInstance.Status "accessing-monitoring.md#Overview.DBInstance.Status").

###### To change the replica mode of an Oracle replica from mounted to read-only

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the mounted replica database.
4. Choose **Modify**.
5. For **Replica mode**, choose **Read-only**.
6. Choose the other settings that you want to change.
7. Choose **Continue**.
8. For **Scheduling of modifications**, choose **Apply
   immediately**.
9. Choose **Modify DB instance**.
   To change a read replica to mounted mode, set `--replica-mode` to `mounted` in
   the AWS CLI command [modify-db-instance](../../../cli/latest/reference/rds/modify-db-instance.md "../../../cli/latest/reference/rds/modify-db-instance.md"). To
   change a mounted replica to read-only mode, set `--replica-mode` to
   `open-read-only`.

###### Example

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --db-instance-identifier `myreadreplica` \
    --replica-mode `open-read-only`
```

For Windows:

```
aws rds modify-db-instance ^
    --db-instance-identifier `myreadreplica` ^
    --replica-mode `open-read-only`
```

To change a read-only replica to mounted mode, set `ReplicaMode=mounted` in [ModifyDBInstance](../APIReference/API_ModifyDBInstance.md "../APIReference/API_ModifyDBInstance.md"). To change a mounted
replica to read-only mode, set `ReplicaMode=open-read-only`.
