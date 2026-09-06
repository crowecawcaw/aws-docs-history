

# Failing over an Amazon Aurora DB cluster
<a name="aurora-failover"></a>

You can perform a manual failover of an Aurora DB cluster, for example, when you want to replace a provisioned writer DB instance with an Aurora serverless writer instance.

Aurora fails over to a new primary DB instance in one of two ways:
+ By promoting an existing reader DB instance to the new primary instance
+ By creating a new primary instance

If the DB cluster has one or more reader instances, then a reader is promoted to the primary instance during a failure event. To increase the availability of your DB cluster, we recommend that you create at least one or more reader instances in two or more different Availability Zones. For more information on the failover mechanism, see [Fault tolerance for an Aurora DB cluster](Concepts.AuroraHighAvailability.md#Aurora.Managing.FaultTolerance).

You can use the AWS Management Console, AWS CLI, or RDS API to perform a manual failover.

## Console
<a name="aurora-failover.CON"></a>

**To fail over a DB cluster**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**, and then select a DB instance in the DB cluster that you want to fail over.

1. For **Actions**, choose **Failover**.

   The confirmation page appears.

1. Choose **Failover**.

   The **Databases** page shows that the DB cluster status is **Failing-over**. The status returns to **Available** when the failover is completed, and the roles for the new and former primary DB instances are displayed.

## AWS CLI
<a name="aurora-failover.CLI"></a>

To fail over a DB cluster using the AWS CLI, call the [failover-db-cluster](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/failover-db-cluster.html) command. Specify the following parameters:
+ `--db-cluster-identifier` – The DB cluster that you want to fail over.
+ `--target-db-instance-identifier` – The name of the DB instance to promote to the primary DB instance.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds failover-db-cluster \
    --db-cluster-identifier {{mydbcluster}} \
    --target-db-instance-identifier {{mydbcluster-instance-2}}
```
For Windows:  

```
aws rds failover-db-cluster ^
    --db-cluster-identifier {{mydbcluster}} ^
    --target-db-instance-identifier {{mydbcluster-instance-2}}
```

## RDS API
<a name="aurora-failover.API"></a>

To modify a DB cluster using the Amazon RDS API, call the [FailoverDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_FailoverDBCluster.html) operation. Specify the following parameters:
+ DBClusterIdentifier
+ TargetDBInstanceIdentifier