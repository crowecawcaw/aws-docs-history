# Disabling backtracking for an Aurora MySQL DB cluster

You can disable the Backtrack feature for a DB cluster.

You can disable backtracking for a DB cluster using the console. After you
turn off backtracking entirely for a cluster, you can't enable it
again for that cluster.

###### To disable the Backtrack feature for a DB cluster using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**.
3. Choose the cluster you want to modify, and choose **Modify**.
4. In the **Backtrack** section, choose **Disable Backtrack**.
5. Choose **Continue**.
6. For **Scheduling of Modifications**, choose one of the following:
   - **Apply during the next scheduled maintenance
     window** – Wait to apply the modification
     until the next maintenance window.
   - **Apply immediately** – Apply the
     modification as soon as possible.

7. Choose **Modify Cluster**.
   You can disable the Backtrack feature for a DB cluster using the AWS CLI by
   setting the target backtrack window to `0` (zero). After you
   turn off backtracking entirely for a cluster, you can't enable it
   again for that cluster.

###### To modify the target backtrack window for a DB cluster using the AWS CLI

- Call the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md")
  AWS CLI command and supply the following values:

      + `--db-cluster-identifier` – The name of the
       DB cluster.
      + `--backtrack-window` – specify `0` to turn off backtracking.

  The following example disables the Backtrack feature for the `sample-cluster` by
  setting `--backtrack-window` to `0`.

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

To disable the Backtrack feature for a DB cluster using the Amazon RDS API, use the
[ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md") operation.
Set the `BacktrackWindow` value to `0` (zero), and specify the DB
cluster in the `DBClusterIdentifier` value. After you turn off backtracking
entirely for a cluster, you can't enable it again for that cluster.
