

# Initiating the Oracle Data Guard switchover
<a name="oracle-switchover.initiating"></a>

You can switch over an RDS for Oracle read replica to the primary role, and the former primary DB instance to a replica role.

Before initiating a switchover, verify the following:
+ The `ReplicaLag` CloudWatch metric is zero or near zero.
+ No long-running transactions are active on the primary database.
+ Your application connection strings are configured to handle the endpoint change, or you have a plan to update them after the switchover.
+ You have verified that the replica is in a healthy state (status is `available`).

## Console
<a name="USER_ReadRepl.Promote.Console"></a>

**To switch over an Oracle read replica to the primary DB role**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the Amazon RDS console, choose **Databases**.

   The **Databases** pane appears. Each read replica shows **Replica** in the **Role** column.

1. Choose the read replica that you want to switch over to the primary role.

1. For **Actions**, choose **Switch over replica**.

1. Choose **I acknowledge**. Then choose **Switch over replica**.

1. On the **Databases** page, monitor the progress of the switchover.  
![Monitor the progress of the Oracle Data Guard switchover.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/oracle-switchover-progress.png)

   When the switchover completes, the role of the switchover target changes from **Replica** to **Source**.  
![The source and replica databases change roles.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/oracle-switchover-complete.png)

## AWS CLI
<a name="USER_ReadRepl.Promote.CLI"></a>

To switch over an Oracle replica to the primary DB role, use the AWS CLI [`switchover-read-replica`](https://docs.aws.amazon.com/cli/latest/reference/rds/switchover-read-replica.html) command. The following examples make the Oracle replica named {{replica-to-be-made-primary}} into the new primary database.

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
<a name="USER_ReadRepl.Promote.API"></a>

To switch over an Oracle replica to the primary DB role, call the Amazon RDS API [`SwitchoverReadReplica`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_SwitchoverReadReplica.html) operation with the required parameter `DBInstanceIdentifier`. This parameter specifies the name of the Oracle replica that you want to assume the primary DB role.