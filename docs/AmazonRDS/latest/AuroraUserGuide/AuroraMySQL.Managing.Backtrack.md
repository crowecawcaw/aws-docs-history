# Configuring backtracking a Aurora MySQL DB cluster

To use the Backtrack feature, you must enable backtracking and specify a target backtrack window.
Otherwise, backtracking is disabled.

For the target backtrack window, specify the amount of time that you want to be
able to rewind your database using Backtrack. Aurora tries to retain enough change
records to support that window of time.

You can use the console to configure backtracking when you create a new DB cluster. You can also
modify a DB cluster to change the backtrack window for a backtrack-enabled cluster. If you
turn off backtracking entirely for a cluster by setting the backtrack window to 0, you can't
enable backtrack again for that cluster.

###### Topics

- [Configuring backtracking with the console when creating a DB cluster](#AuroraMySQL.Managing.Backtrack.Configuring.Console.Creating "#AuroraMySQL.Managing.Backtrack.Configuring.Console.Creating")
- [Configuring backtrack with the console when modifying a DB cluster](#AuroraMySQL.Managing.Backtrack.Configuring.Console.Modifying "#AuroraMySQL.Managing.Backtrack.Configuring.Console.Modifying")

### Configuring backtracking with the console when creating a DB cluster

When you create a new Aurora MySQL DB cluster, backtracking is configured when
you choose **Enable Backtrack** and specify a **Target Backtrack window** value that is
greater than zero in the **Backtrack** section.

To create a DB cluster, follow the instructions in
[Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md"). The following image
shows the **Backtrack** section.

![Enable Backtrack during DB cluster creation with console](images/aurora-backtrack-create.png)

When you create a new DB cluster, Aurora has no data for the DB cluster's
workload. So it can't estimate a cost specifically for the new DB
cluster. Instead, the console presents a typical user cost for the
specified target backtrack window based on a typical workload. The
typical cost is meant to provide a general reference for the cost of the
Backtrack feature.

###### Important

Your actual cost might not match the typical cost, because your actual cost is based on your
DB cluster's workload.

### Configuring backtrack with the console when modifying a DB cluster

You can modify backtracking for a DB cluster using the console.

###### Note

Currently, you can modify backtracking only for a DB cluster that
has the Backtrack feature enabled. The **Backtrack** section doesn't appear
for a DB cluster that was created with the Backtrack feature
disabled or if the Backtrack feature has been disabled for the DB cluster.

###### To modify backtracking for a DB cluster using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**.
3. Choose the cluster that you want to modify, and choose
   **Modify**.
4. For **Target Backtrack window**, modify the amount of
   time that you want to be able to backtrack. The limit is 72
   hours.

![Modify Backtrack with console](images/aurora-backtrack-modify.png)

The console shows the estimated cost for the amount of time you
specified based on the DB cluster's past workload:

    * If backtracking was disabled on the DB cluster, the cost
     estimate is based on the `VolumeWriteIOPS` metric for the DB
     cluster in Amazon CloudWatch.
    * If backtracking was enabled previously on the DB cluster, the cost
     estimate is based on the `BacktrackChangeRecordsCreationRate`
     metric for the DB cluster in Amazon CloudWatch.

5. Choose **Continue**.
6. For **Scheduling of Modifications**, choose one of
   the following:
   - **Apply during the next scheduled maintenance
     window** – Wait to apply the
     **Target Backtrack window** modification
     until the next maintenance window.
   - **Apply immediately** – Apply the
     **Target Backtrack window** modification
     as soon as possible.

7. Choose **Modify cluster**.

When you create a new Aurora MySQL DB cluster using the
[create-db-cluster](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md") AWS CLI command,
backtracking is configured when you specify a `--backtrack-window` value that is greater than zero.
The `--backtrack-window` value specifies the target backtrack window.
For more information, see [Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

You can also specify the `--backtrack-window` value using the following AWS CLI commands:

- [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md")
- [restore-db-cluster-from-s3](../../../cli/latest/reference/rds/restore-db-cluster-from-s3.md "../../../cli/latest/reference/rds/restore-db-cluster-from-s3.md")
- [restore-db-cluster-from-snapshot](../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md "../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md")
- [restore-db-cluster-to-point-in-time](../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md")
  The following procedure describes how to modify the target backtrack window for a DB cluster using the AWS CLI.

###### To modify the target backtrack window for a DB cluster using the AWS CLI

- Call the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") AWS CLI command and supply
  the following values:

      + `--db-cluster-identifier` – The name of the
       DB cluster.
      + `--backtrack-window` – The maximum number of seconds that you
       want to be able to backtrack the DB cluster.

  The following example sets the target backtrack window for `sample-cluster` to one day (86,400 seconds).

For Linux, macOS, or Unix:

```

aws rds modify-db-cluster \
    --db-cluster-identifier sample-cluster \
    --backtrack-window 86400

```

For Windows:

```

aws rds modify-db-cluster ^
    --db-cluster-identifier sample-cluster ^
    --backtrack-window 86400

```

###### Note

Currently, you can enable backtracking only for a DB cluster that was created with
the Backtrack feature enabled.

When you create a new Aurora MySQL DB cluster using the
[CreateDBCluster](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md") Amazon RDS API operation,
backtracking is configured when you specify a `BacktrackWindow` value that is greater than zero.
The `BacktrackWindow` value specifies the target backtrack window for the DB cluster specified in
the `DBClusterIdentifier` value. For more information, see
[Creating an Amazon Aurora DB cluster](Aurora.md "Aurora.md").

You can also specify the `BacktrackWindow` value using the
following API operations:

- [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md")
- [RestoreDBClusterFromS3](../APIReference/API_RestoreDBClusterFromS3.md "../APIReference/API_RestoreDBClusterFromS3.md")
- [RestoreDBClusterFromSnapshot](../APIReference/API_RestoreDBClusterFromSnapshot.md "../APIReference/API_RestoreDBClusterFromSnapshot.md")
- [RestoreDBClusterToPointInTime](../APIReference/API_RestoreDBClusterToPointInTime.md "../APIReference/API_RestoreDBClusterToPointInTime.md")

###### Note

Currently, you can enable backtracking only for a DB cluster that was created with
the Backtrack feature enabled.
