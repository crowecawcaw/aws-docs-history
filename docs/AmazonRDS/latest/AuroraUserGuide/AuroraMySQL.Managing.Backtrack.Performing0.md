

# Performing a backtrack for an Aurora MySQL DB cluster
<a name="AuroraMySQL.Managing.Backtrack.Performing0"></a>

You can backtrack a DB cluster to a specified backtrack time stamp. If the backtrack time stamp isn't earlier than the earliest possible backtrack time, and isn't in the future, the DB cluster is backtracked to that time stamp. 

Otherwise, an error typically occurs. Also, if you try to backtrack a DB cluster for which binary logging is enabled, an error typically occurs unless you've chosen to force the backtrack to occur. Forcing a backtrack to occur can interfere with other operations that use binary logging.

**Important**  
Backtracking doesn't generate binlog entries for the changes that it makes. If you have binary logging enabled for the DB cluster, backtracking might not be compatible with your binlog implementation.

**Note**  
For database clones, you can't backtrack the DB cluster earlier than the date and time when the clone was created. For more information about database cloning, see [Cloning a volume for an Amazon Aurora DB cluster](Aurora.Managing.Clone.md).

## Console
<a name="AuroraMySQL.Managing.Backtrack.Performing.Console"></a>

The following procedure describes how to perform a backtrack operation for a DB cluster using the console.

**To perform a backtrack operation using the console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Instances**.

1. Choose the primary instance for the DB cluster that you want to backtrack.

1. For **Actions**, choose **Backtrack DB cluster**.

1. On the **Backtrack DB cluster** page, enter the backtrack time stamp to backtrack the DB cluster to.  
![Backtrack DB cluster.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/aurora-backtrack-db-cluster.png)

1. Choose **Backtrack DB cluster**.

## AWS CLI
<a name="AuroraMySQL.Managing.Backtrack.Performing.CLI"></a>

The following procedure describes how to backtrack a DB cluster using the AWS CLI.

**To backtrack a DB cluster using the AWS CLI**
+ Call the [backtrack-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/backtrack-db-cluster.html) AWS CLI command and supply the following values:
  + `--db-cluster-identifier` – The name of the DB cluster.
  + `--backtrack-to` – The backtrack time stamp to backtrack the DB cluster to, specified in ISO 8601 format.

  The following example backtracks the DB cluster `sample-cluster` to March 19, 2018, at 10 a.m.

  For Linux, macOS, or Unix:

  ```
  aws rds backtrack-db-cluster \
      --db-cluster-identifier sample-cluster \
      --backtrack-to 2018-03-19T10:00:00+00:00
  ```

  For Windows:

  ```
  aws rds backtrack-db-cluster ^
      --db-cluster-identifier sample-cluster ^
      --backtrack-to 2018-03-19T10:00:00+00:00
  ```

## RDS API
<a name="AuroraMySQL.Managing.Backtrack.Performing.API"></a>

To backtrack a DB cluster using the Amazon RDS API, use the [BacktrackDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_BacktrackDBCluster.html) operation. This operation backtracks the DB cluster specified in the `DBClusterIdentifier` value to the specified time.