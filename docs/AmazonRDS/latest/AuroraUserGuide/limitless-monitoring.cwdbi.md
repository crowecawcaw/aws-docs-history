# Turning on the Advanced mode of Database Insights for Aurora PostgreSQL Limitless Database

To turn on the Advanced mode of Database Insights for your Aurora PostgreSQL Limitless Database, use the following procedures.

## Turning on the Advanced mode of Database Insights when creating a DB cluster for Aurora PostgreSQL Limitless Database

Turn on the Advanced mode of Database Insights when creating a database for Aurora PostgreSQL Limitless Database.

Console
In the console, you can turn on the Advanced mode of Database Insights when you
create a DB cluster. Settings for Database Insights apply to all DB instances in your DB cluster.

###### To turn on the Advanced mode of Database Insights when creating a DB cluster using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**.
3. Choose **Create database**.
4. In the **Database Insights** section, select **Advanced mode**. Then, choose the following options:
   - **Retention** – The amount of time to retain Performance Insights data. The retention period must be 15-24 months for the Advanced mode of Database Insights.
   - **AWS KMS key** – Specify your
     KMS key. Performance Insights encrypts all
     potentially sensitive data using your KMS key. Data is
     encrypted in flight and at rest. For more information, see
     [Encrypting Amazon Aurora
     resources](Overview.md "Overview.md").

5. Choose **Create database**.

AWS CLI
To turn on the Advanced mode of Database Insights when creating a DB cluster, call the [create-db-cluster](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md") AWS CLI command and supply the following values:

- `--db-cluster-identifier` – The identifier for the DB cluster.
- `--database-insights-mode advanced` to turn on the Advanced mode of Database Insights.
- `--engine` – The DB cluster must use the `aurora-postgresql` DB engine.
- `--engine-version` – The DB cluster must use one of the DB engine versions:
  - `16.4-limitless`
  - `16.6-limitless`

- `--storage-type` – The DB cluster must use the `aurora-iopt1` DB cluster storage
  configuration.
- `--cluster-scalability-type` – Specifies the scalability mode of the Aurora DB cluster. When set to
  `limitless`, the cluster operates as an Aurora PostgreSQL Limitless Database. When set to `standard` (the default), the cluster
  uses normal DB instance creation.

###### Note

You can't modify this setting after you create the DB cluster.

- `--master-username` – The name of the master user for the DB cluster.
- `--master-user-password` – The password for the master user.
- `--enable-performance-insights` to turn on Performance Insights for Database Insights.
- `--performance-insights-retention-period` – The retention period for data for your DB cluster. To turn on Database Insights, the retention period must be at least 465 days.
- `--monitoring-interval` – The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the
  DB cluster. This value can't be `0`.
- `--monitoring-role-arn` – The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring
  metrics to Amazon CloudWatch Logs.
- `--enable-cloudwatch-logs-exports` – You must export `postgresql` logs to CloudWatch Logs.

The following example enables the Advanced mode of Database Insights when creating a DB cluster.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster \
--db-cluster-identifier `my-limitless-cluster` \
--database-insights-mode advanced \
--engine aurora-postgresql \
--engine-version 16.6-limitless \
--storage-type aurora-iopt1 \
--cluster-scalability-type limitless \
--master-username myuser \
--master-user-password mypassword \
--enable-performance-insights \
--performance-insights-retention-period 465 \
--monitoring-interval `5` \
--monitoring-role-arn arn:aws:iam::`123456789012`:role/`EMrole` \
--enable-cloudwatch-logs-exports postgresql
```

For Windows:

```
aws rds create-db-cluster ^
--db-cluster-identifier `my-limitless-cluster` ^
--database-insights-mode advanced ^
--engine aurora-postgresql ^
--engine-version 16.6-limitless ^
--storage-type aurora-iopt1 ^
--cluster-scalability-type limitless ^
--master-username myuser ^
--master-user-password mypassword ^
--enable-performance-insights ^
--performance-insights-retention-period 465 ^
--monitoring-interval `5` ^
--monitoring-role-arn arn:aws:iam::`123456789012`:role/`EMrole` ^
--enable-cloudwatch-logs-exports postgresql
```

RDS API
To turn on the Advanced mode of Database Insights when you create a DB cluster, specify the following parameters for your [CreateDBCluster](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md") Amazon RDS API operation.

- `DatabaseInsightsMode` to `advanced`
- `Engine` to `aurora-postgresql`
- `EngineVersion` to an available engine version for Limitless Database
- `StorageType` to `aurora-iopt1`
- `ClusterScalabilityType` to `limitless`
- `MasterUsername`
- `MasterUserPassword`
- `EnablePerformanceInsights` to `True`
- `PerformanceInsightsRetentionPeriod` to at least `465` days
- `MonitoringInterval` to a value that isn't `0`
- `MonitoringRoleArn` to the Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs

## Turning on the Advanced mode of Database Insights when modifying a DB cluster for Aurora PostgreSQL Limitless Database

Turn on Database Insights when modifying a database for Aurora PostgreSQL Limitless Database.

###### Note

To enable Database Insights, each DB instance in aDB cluster must have the same Performance Insights and Enhanced Monitoring settings.

Console
In the console, you can turn on the Advanced mode of Database Insights when you
modify a DB cluster. Settings for Database Insights apply to all DB instances in your DB cluster.

###### To turn on the Advanced mode of Database Insights when modifying a DB cluster using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**.
3. Choose a DB cluster, and choose **Modify**.
4. In the **Database Insights** section, select **Advanced mode**. Then, choose the following options:
   - **Retention** – The amount of time to retain Performance Insights data. The retention period must be 15-24 months for the Advanced mode of Database Insights.
   - **AWS KMS key** – Specify your
     KMS key. Performance Insights encrypts all
     potentially sensitive data using your KMS key. Data is
     encrypted in flight and at rest. For more information, see
     [Encrypting Amazon Aurora
     resources](Overview.md "Overview.md").

5. Choose **Continue**.
6. For **Scheduling of Modifications**, choose **Apply immediately**. If you
   choose **Apply during the next scheduled maintenance window**, your database
   ignores this setting and turns on the Advanced mode of Database Insights immediately.
7. Choose **Modify cluster**.

AWS CLI
To turn on the Advanced mode of Database Insights when modifying a DB cluster, call the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") AWS CLI command and supply the following values:

- `--database-insights-mode advanced` to turn on the Advanced mode of Database Insights.
- `--db-cluster-identifier` – The identifier for the DB cluster.
- `--enable-performance-insights` to turn on Performance Insights for Database Insights.
- `--performance-insights-retention-period` – The retention period for data for your DB cluster. To turn on the Advanced mode of Database Insights, the retention period must be at least 465 days.

The following example enables the Advanced mode of Database Insights when modifying a DB cluster.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --database-insights-mode advanced \
    --db-cluster-identifier sample-db-identifier \
    --enable-performance-insights \
    --performance-insights-retention-period 465
```

For Windows:

```
aws rds modify-db-cluster ^
    --database-insights-mode advanced ^
    --db-cluster-identifier sample-db-identifier ^
    --enable-performance-insights ^
    --performance-insights-retention-period 465
```

RDS API
To turn on the Advanced mode of Database Insights when you modify a DB cluster, specify the following parameters for your [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md") Amazon RDS API operation.

- `DatabaseInsightsMode` to `advanced`
- `EnablePerformanceInsights` to `True`
- `PerformanceInsightsRetentionPeriod` to at least `465` days
