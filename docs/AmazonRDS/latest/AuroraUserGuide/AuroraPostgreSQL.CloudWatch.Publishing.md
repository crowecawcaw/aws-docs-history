

# Turning on the option to publish logs to Amazon CloudWatch
<a name="AuroraPostgreSQL.CloudWatch.Publishing"></a>

To publish your Aurora PostgreSQL DB cluster's PostgreSQL log to CloudWatch Logs, choose the **Log export** option for the cluster. You can choose the Log export setting when you create your Aurora PostgreSQL DB cluster. Or, you can modify the cluster later on. When you modify an existing cluster, its PostgreSQL logs from each instance are published to CloudWatch cluster from that point on. For Aurora PostgreSQL, the PostgreSQL log (`postgresql.log`) is the only log that gets published to Amazon CloudWatch. 

You can use the AWS Management Console, the AWS CLI, or the RDS API to turn on the Log export feature for your Aurora PostgreSQL DB cluster. 

## Console
<a name="AuroraPostgreSQL.CloudWatch.Console"></a>

You choose the Log exports option to start publishing the PostgreSQL logs from your Aurora PostgreSQL DB cluster to CloudWatch Logs.

**To turn on the Log export feature from the console**

1. Open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Databases**.

1. Choose the Aurora PostgreSQL DB cluster whose log data you want to publish to CloudWatch Logs.

1. Choose **Modify**.

1. In the **Log exports** section, choose **PostgreSQL log**.

1. Choose **Continue**, and then choose **Modify cluster** on the summary page.

## AWS CLI
<a name="AuroraPostgreSQL.CloudWatch.CLI"></a>

You can turn on the log export option to start publishing Aurora PostgreSQL logs to Amazon CloudWatch Logs with the AWS CLI. To do so, run the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) AWS CLI command with the following options: 
+ `--db-cluster-identifier`—The DB cluster identifier.
+ `--cloudwatch-logs-export-configuration`—The configuration setting for the log types to be set for export to CloudWatch Logs for the DB cluster.

You can also publish Aurora PostgreSQL logs by running one of the following AWS CLI commands: 
+ [create-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster.html)
+ [restore-db-cluster-from-s3](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-cluster-from-s3.html)
+ [restore-db-cluster-from-snapshot](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-cluster-from-snapshot.html)
+ [restore-db-cluster-to-point-in-time](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-cluster-to-point-in-time.html)

Run one of these AWS CLI commands with the following options:
+ `--db-cluster-identifier`—The DB cluster identifier.
+ `--engine`—The database engine.
+ `--enable-cloudwatch-logs-exports`—The configuration setting for the log types to be enabled for export to CloudWatch Logs for the DB cluster.

Other options might be required depending on the AWS CLI command that you run.

**Example**  
The following command creates an Aurora PostgreSQL DB cluster to publish log files to CloudWatch Logs.  
For Linux, macOS, or Unix:  

```
1. aws rds create-db-cluster \
2.     --db-cluster-identifier {{my-db-cluster}} \
3.     --engine aurora-postgresql \
4.     --enable-cloudwatch-logs-exports postgresql
```
For Windows:  

```
1. aws rds create-db-cluster ^
2.     --db-cluster-identifier {{my-db-cluster}} ^
3.     --engine aurora-postgresql ^
4.     --enable-cloudwatch-logs-exports postgresql
```

**Example**  
The following command modifies an existing Aurora PostgreSQL DB cluster to publish log files to CloudWatch Logs. The `--cloudwatch-logs-export-configuration` value is a JSON object. The key for this object is `EnableLogTypes`, and its value is `postgresql`, and `instance`.  
For Linux, macOS, or Unix:  

```
1. aws rds modify-db-cluster \
2.     --db-cluster-identifier {{my-db-cluster}} \
3.     --cloudwatch-logs-export-configuration '{"EnableLogTypes":["postgresql","instance"]}'
```
For Windows:  

```
1. aws rds modify-db-cluster ^
2.     --db-cluster-identifier {{my-db-cluster}} ^
3.     --cloudwatch-logs-export-configuration '{\"EnableLogTypes\":[\"postgresql\",\"instance\"]}'
```
When using the Windows command prompt, make sure to escape double quotation marks (") in JSON code by prefixing them with a backslash (\\).

**Example**  
The following example modifies an existing Aurora PostgreSQL DB cluster to disable publishing log files to CloudWatch Logs. The `--cloudwatch-logs-export-configuration` value is a JSON object. The key for this object is `DisableLogTypes`, and its value is `postgresql` and `instance`.  
For Linux, macOS, or Unix:  

```
aws rds modify-db-cluster \
    --db-cluster-identifier {{mydbinstance}} \
    --cloudwatch-logs-export-configuration '{"DisableLogTypes":["postgresql","instance"]}'
```
For Windows:  

```
aws rds modify-db-cluster ^
    --db-cluster-identifier {{mydbinstance}} ^
    --cloudwatch-logs-export-configuration "{\"DisableLogTypes\":[\"postgresql\",\"instance\"]}"
```
When using the Windows command prompt, you must escape double quotes (") in JSON code by prefixing them with a backslash (\\).

## RDS API
<a name="AuroraPostgreSQL.CloudWatch.API"></a>

You can turn on the log export option to start publishing Aurora PostgreSQL logs with the RDS API. To do so, run the [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) operation with the following options: 
+ `DBClusterIdentifier` – The DB cluster identifier.
+ `CloudwatchLogsExportConfiguration` – The configuration setting for the log types to be enabled for export to CloudWatch Logs for the DB cluster.

You can also publish Aurora PostgreSQL logs with the RDS API by running one of the following RDS API operations: 
+ [CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html)
+ [RestoreDBClusterFromS3](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterFromS3.html)
+ [RestoreDBClusterFromSnapshot](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterFromSnapshot.html)
+ [RestoreDBClusterToPointInTime](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBClusterToPointInTime.html)

Run the RDS API action with the following parameters: 
+ `DBClusterIdentifier`—The DB cluster identifier.
+ `Engine`—The database engine.
+ `EnableCloudwatchLogsExports`—The configuration setting for the log types to be enabled for export to CloudWatch Logs for the DB cluster.

Other parameters might be required depending on the AWS CLI command that you run.