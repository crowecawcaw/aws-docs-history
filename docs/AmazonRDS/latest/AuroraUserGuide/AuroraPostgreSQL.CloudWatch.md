# Turning on the option to publish logs to Amazon CloudWatch

To publish your Aurora PostgreSQL DB cluster's PostgreSQL log to CloudWatch Logs, choose the
**Log export** option for the cluster. You can choose the Log
export setting when you create your Aurora PostgreSQL DB cluster. Or, you can modify the
cluster later on. When you modify an existing cluster, its PostgreSQL logs from each
instance are published to CloudWatch cluster from that point on. For Aurora PostgreSQL, the
PostgreSQL log (`postgresql.log`) is the only log that gets published to
Amazon CloudWatch.

You can use the AWS Management Console, the AWS CLI, or the RDS API to turn on the Log export feature for your
Aurora PostgreSQL DB cluster.

You choose the Log exports option to start
publishing the PostgreSQL logs from your Aurora PostgreSQL DB cluster to
CloudWatch Logs.

###### To turn on the Log export feature from the console

1. Open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**.
3. Choose the Aurora PostgreSQL DB cluster whose log data you want to publish to
   CloudWatch Logs.
4. Choose **Modify**.
5. In the **Log exports** section, choose
   **PostgreSQL log**.
6. Choose **Continue**, and then choose **Modify
   cluster** on the summary page.
   You can turn on the log export option to start publishing Aurora PostgreSQL logs
   to Amazon CloudWatch Logs with the AWS CLI. To do so,
   run the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") AWS CLI
   command with the following options:

- `--db-cluster-identifier`—The DB cluster
  identifier.
- `--cloudwatch-logs-export-configuration`—The
  configuration setting for the log types to be set for export to CloudWatch Logs
  for the DB cluster.
  You can also publish Aurora PostgreSQL logs by running one of the following AWS CLI
  commands:

- [create-db-cluster](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md")
- [restore-db-cluster-from-s3](../../../cli/latest/reference/rds/restore-db-cluster-from-s3.md "../../../cli/latest/reference/rds/restore-db-cluster-from-s3.md")
- [restore-db-cluster-from-snapshot](../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md "../../../cli/latest/reference/rds/restore-db-cluster-from-snapshot.md")
- [restore-db-cluster-to-point-in-time](../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-cluster-to-point-in-time.md")
  Run one of these AWS CLI commands with the following options:

- `--db-cluster-identifier`—The DB cluster
  identifier.
- `--engine`—The database engine.
- `--enable-cloudwatch-logs-exports`—The configuration
  setting for the log types to be enabled for export to CloudWatch Logs for the DB
  cluster.
  Other options might be required depending on the AWS CLI command that you
  run.

The following command creates an Aurora PostgreSQL DB cluster to publish log files to
CloudWatch Logs.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster \
    --db-cluster-identifier `my-db-cluster` \
    --engine aurora-postgresql \
    --enable-cloudwatch-logs-exports postgresql
```

For Windows:

```
aws rds create-db-cluster ^
    --db-cluster-identifier `my-db-cluster` ^
    --engine aurora-postgresql ^
    --enable-cloudwatch-logs-exports postgresql
```

The following command modifies an existing Aurora PostgreSQL DB cluster to publish
log files to CloudWatch Logs. The `--cloudwatch-logs-export-configuration`
value is a JSON object. The key for this object is `EnableLogTypes`,
and its value is `postgresql`, and `instance`.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier `my-db-cluster` \
    --cloudwatch-logs-export-configuration '{"EnableLogTypes":["postgresql","instance"]}'
```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier `my-db-cluster` ^
    --cloudwatch-logs-export-configuration '{\"EnableLogTypes\":[\"postgresql\",\"instance\"]}'
```

###### Note

When using the Windows command prompt, make sure to escape double
quotation marks (") in JSON code by prefixing them with a backslash
(\).

The following example modifies an existing Aurora PostgreSQL DB cluster to disable publishing log files to CloudWatch Logs.
The `--cloudwatch-logs-export-configuration` value is a JSON object. The key for this object is
`DisableLogTypes`, and its value is `postgresql` and `instance`.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --db-cluster-identifier `mydbinstance` \
    --cloudwatch-logs-export-configuration '{"DisableLogTypes":["postgresql","instance"]}'
```

For Windows:

```
aws rds modify-db-cluster ^
    --db-cluster-identifier `mydbinstance` ^
    --cloudwatch-logs-export-configuration "{\"DisableLogTypes\":[\"postgresql\",\"instance\"]}"
```

###### Note

When using the Windows command prompt, you must escape double quotes (") in JSON code by
prefixing them with a backslash (\).

You can turn on the log export option to start publishing Aurora PostgreSQL logs with
the RDS API. To do so, run the [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md")
operation with the following options:

- `DBClusterIdentifier` – The DB cluster identifier.
- `CloudwatchLogsExportConfiguration` – The configuration
  setting for the log types to be enabled for export to CloudWatch Logs for the DB
  cluster.
  You can also publish Aurora PostgreSQL logs with the RDS API by running one of the
  following RDS API operations:

- [CreateDBCluster](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md")
- [RestoreDBClusterFromS3](../APIReference/API_RestoreDBClusterFromS3.md "../APIReference/API_RestoreDBClusterFromS3.md")
- [RestoreDBClusterFromSnapshot](../APIReference/API_RestoreDBClusterFromSnapshot.md "../APIReference/API_RestoreDBClusterFromSnapshot.md")
- [RestoreDBClusterToPointInTime](../APIReference/API_RestoreDBClusterToPointInTime.md "../APIReference/API_RestoreDBClusterToPointInTime.md")
  Run the RDS API action with the following parameters:

- `DBClusterIdentifier`—The DB cluster identifier.
- `Engine`—The database engine.
- `EnableCloudwatchLogsExports`—The configuration setting
  for the log types to be enabled for export to CloudWatch Logs for the DB
  cluster.
  Other parameters might be required depending on the AWS CLI command that you
  run.
