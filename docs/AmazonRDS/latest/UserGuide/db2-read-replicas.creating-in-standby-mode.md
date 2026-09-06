

# Creating an RDS for Db2 replica in standby mode
<a name="db2-read-replicas.creating-in-standby-mode"></a>

By default, Db2 replicas are created in read-only mode. You can create a replica in standby mode for disaster recovery purposes. Standby replicas don't accept user connections but provide faster failover capabilities for cross-Region scenarios.

Before creating a standby replica, make sure that you have completed the preparation tasks. For more information, see [Preparing to create an RDS for Db2 replica](db2-read-replicas.Configuration.md). After creating a standby replica, you can change the replica mode. For more information, see [Modifying the RDS for Db2 replica mode](db2-replicas-changing-replica-mode.md).

You can create a standby replica using the AWS Management Console, the AWS CLI, or the RDS API. For information about creating a read-only replica, see [Creating a read replica](USER_ReadRepl.Create.md).

## Console
<a name="db2-read-replicas.creating-in-standby-mode.console"></a>

**To create a standby replica from a source RDS for Db2 DB instance**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose the RDS for Db2 DB instance that you want to use as the source for a standby replica.

1. For **Actions**, choose **Create replica**. 

1. For **Replica mode**, choose **Standby**.

1. Choose the settings that you want to use. For **DB instance identifier**, enter a name for the standby replica. Adjust other settings as needed.

1. For **Regions**, choose the AWS Region where the standby replica will be launched. 

1. Choose your instance size and storage type. We recommend that you use the same DB instance class and storage type as the source DB instance for the standby replica.

1. For **Multi-AZ deployment**, choose **Create a standby instance** to create a standby of your replica in another Availability Zone for failover support for the standby replica.

1. Choose the other settings that you want to use.

1. Choose **Create replica**.

In the **Databases** page, the standby replica has the role **Replica**.

## AWS CLI
<a name="db2-read-replicas.creating-in-standby-mode.cli"></a>

To create a Db2 replica in standby mode, use the AWS CLI command [create-db-instance-read-replica](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance-read-replica.html) with `--replica-mode` set to `mounted`.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds create-db-instance-read-replica \
    --db-instance-identifier {{my_standby_replica}} \
    --source-db-instance-identifier {{my_db_instance}} \
    --replica-mode mounted
```
For Windows:  

```
aws rds create-db-instance-read-replica ^
    --db-instance-identifier {{my_standby_replica}} ^
    --source-db-instance-identifier {{my_db_instance}} ^
    --replica-mode mounted
```

## RDS API
<a name="db2-read-replicas.creating-in-standby-mode.api"></a>

To create a Db2 replica in standby mode, specify `ReplicaMode=mounted` in the RDS API operation [CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html).