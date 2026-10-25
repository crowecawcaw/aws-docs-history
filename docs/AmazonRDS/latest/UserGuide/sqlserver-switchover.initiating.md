

# Initiating the SQL Server switchover
<a name="sqlserver-switchover.initiating"></a>

You can switch over an RDS for SQL Server read replica to the primary role, and the former primary DB instance to a replica role.

Before initiating a switchover, verify the following:
+ The `ReplicaLag` CloudWatch metric is zero or near zero.
+ No long-running transactions are active on the primary database.
+ Your application connection strings are configured to handle the endpoint change, or you have a plan to update them after the switchover.
+ You have verified that the replica is in a healthy state (status is `available`).

You can initiate the switchover using the Amazon RDS console, the AWS CLI, or the Amazon RDS API.

## Console
<a name="sqlserver-switchover.initiating.console"></a>

**To switch over a SQL Server read replica to the primary DB role**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the Amazon RDS console, choose **Databases**.

   The **Databases** pane appears. Each read replica shows **Replica** in the **Role** column.

1. Choose the read replica that you want to switch over to the primary role.

1. For **Actions**, choose **Switch over replica**.

1. Choose **I acknowledge**. Then choose **Switch over replica**.

1. On the **Databases** page, monitor the progress of the switchover.

   When the switchover completes, the role of the switchover target changes from **Replica** to **Source**.

## AWS CLI
<a name="sqlserver-switchover.initiating.cli"></a>

To switch over a SQL Server replica to the primary DB role, use the AWS CLI [switchover-read-replica](https://docs.aws.amazon.com/cli/latest/reference/rds/switchover-read-replica.html) command. The following examples make the SQL Server replica named {{replica-to-be-made-primary}} into the new primary DB instance.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds switchover-read-replica \
    --db-instance-identifier {{replica-to-be-made-primary}}
```
For Windows:  

```
aws rds switchover-read-replica ^
    --db-instance-identifier {{replica-to-be-made-primary}}
```

## RDS API
<a name="sqlserver-switchover.initiating.api"></a>

To switch over a SQL Server replica to the primary DB role, call the [SwitchoverReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SwitchoverReadReplica.html) operation of the Amazon RDS API with the required parameter `DBInstanceIdentifier`. This parameter specifies the name of the SQL Server replica that you want to assume the primary DB role.