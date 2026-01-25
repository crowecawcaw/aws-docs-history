# Creating an RDS for Db2 replica in

standby mode

By default, Db2 replicas are created in read-only mode. You can create a replica in
standby mode for disaster recovery purposes. Standby replicas don't accept user connections
but provide faster failover capabilities for cross-Region scenarios.

Before creating a standby replica, make sure that you have completed the preparation
tasks. For more information, see [Preparing to create an RDS for Db2
replica](db2-read-replicas.md "db2-read-replicas.md"). After creating a standby replica, you
can change the replica mode. For more information, see [Modifying the RDS for Db2 replica
mode](db2-replicas-changing-replica-mode.md "db2-replicas-changing-replica-mode.md").

You can create a standby replica using the AWS Management Console, the AWS CLI, or the RDS API. For
information about creating a read-only replica, see [Creating a read replica](USER_ReadRepl.md "USER_ReadRepl.md").

###### To create a standby replica from a source RDS for Db2 DB instance

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the RDS for Db2 DB instance that you want to use as the source for a
   standby replica.
4. For **Actions**, choose **Create
   replica**.
5. For **Replica mode**, choose
   **Standby**.
6. Choose the settings that you want to use. For **DB instance
   identifier**, enter a name for the standby replica. Adjust
   other settings as needed.
7. For **Regions**, choose the AWS Region where the
   standby replica will be launched.
8. Choose your instance size and storage type. We recommend that you use the
   same DB instance class and storage type as the source DB instance for the
   standby replica.
9. For **Multi-AZ deployment**, choose **Create a standby
   instance** to create a standby of your replica in another
   Availability Zone for failover support for the standby replica.
10. Choose the other settings that you want to use.
11. Choose **Create replica**.
    In the **Databases** page, the standby replica has the role
    **Replica**.

To create a Db2 replica in standby mode, use the AWS CLI command [create-db-instance-read-replica](../../../cli/latest/reference/rds/create-db-instance-read-replica.md "../../../cli/latest/reference/rds/create-db-instance-read-replica.md") with `--replica-mode` set to
`mounted`.

For Linux, macOS, or Unix:

```
aws rds create-db-instance-read-replica \
    --db-instance-identifier `my_standby_replica` \
    --source-db-instance-identifier `my_db_instance` \
    --replica-mode mounted
```

For Windows:

```
aws rds create-db-instance-read-replica ^
    --db-instance-identifier `my_standby_replica` ^
    --source-db-instance-identifier `my_db_instance` ^
    --replica-mode mounted
```

To create a Db2 replica in standby mode, specify `ReplicaMode=mounted`
in the RDS API operation [CreateDBInstanceReadReplica](../APIReference/API_CreateDBInstanceReadReplica.md "../APIReference/API_CreateDBInstanceReadReplica.md").
