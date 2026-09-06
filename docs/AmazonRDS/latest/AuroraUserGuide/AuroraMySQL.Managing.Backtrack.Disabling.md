

# Disabling backtracking for an Aurora MySQL DB cluster
<a name="AuroraMySQL.Managing.Backtrack.Disabling"></a>

You can disable the Backtrack feature for a DB cluster.

## Console
<a name="AuroraMySQL.Managing.Backtrack.Disabling.Console"></a>

You can disable backtracking for a DB cluster using the console. After you turn off backtracking entirely for a cluster, you can't enable it again for that cluster.

**To disable the Backtrack feature for a DB cluster using the console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose **Databases**.

1. Choose the cluster you want to modify, and choose **Modify**.

1. In the **Backtrack** section, choose **Disable Backtrack**.

1. Choose **Continue**.

1. For **Scheduling of Modifications**, choose one of the following:
   + **Apply during the next scheduled maintenance window** – Wait to apply the modification until the next maintenance window.
   + **Apply immediately** – Apply the modification as soon as possible.

1. Choose **Modify Cluster**.

## AWS CLI
<a name="AuroraMySQL.Managing.Backtrack.Disabling.CLI"></a>

You can disable the Backtrack feature for a DB cluster using the AWS CLI by setting the target backtrack window to `0` (zero). After you turn off backtracking entirely for a cluster, you can't enable it again for that cluster.

**To modify the target backtrack window for a DB cluster using the AWS CLI**
+ Call the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) AWS CLI command and supply the following values:
  + `--db-cluster-identifier` – The name of the DB cluster.
  + `--backtrack-window` – specify `0` to turn off backtracking.

  The following example disables the Backtrack feature for the `sample-cluster` by setting `--backtrack-window` to `0`.

  For Linux, macOS, or Unix:

  ```
  aws rds modify-db-cluster \
      --db-cluster-identifier sample-cluster \
      --backtrack-window 0
  ```

  For Windows:

  ```
  aws rds modify-db-cluster ^
      --db-cluster-identifier sample-cluster ^
      --backtrack-window 0
  ```

## RDS API
<a name="AuroraMySQL.Managing.Backtrack.Disabling.API"></a>

To disable the Backtrack feature for a DB cluster using the Amazon RDS API, use the [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) operation. Set the `BacktrackWindow` value to `0` (zero), and specify the DB cluster in the `DBClusterIdentifier` value. After you turn off backtracking entirely for a cluster, you can't enable it again for that cluster.