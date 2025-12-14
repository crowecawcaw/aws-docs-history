# Turning on the Advanced mode of Database Insights for Amazon Aurora

To turn on the Advanced mode of Database Insights for Amazon Aurora, use the following procedures.

## Turning on the Advanced mode of Database Insights when creating a DB cluster

Turn on the Advanced mode of Database Insights when creating a database for Amazon Aurora.

Console
In the console, you can turn on the Advanced mode of Database Insights when you
create a DB cluster. Settings for Database Insights apply to all DB instances in your DB cluster.

###### To turn on the Advanced mode of Database Insights when creating a DB cluster using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**.
3. Choose **Create database**.
4. In the **Database Insights** section, select **Advanced mode**. Then, choose the following options:
   - **Retention** – The amount of time to retain Performance Insights data. The retention period must be 15 months for the Advanced mode of Database Insights.
   - **AWS KMS key** – Specify your
     KMS key. Performance Insights encrypts all
     potentially sensitive data using your KMS key. Data is
     encrypted in flight and at rest. For more information, see
     [Encrypting Amazon Aurora
     resources](Overview.md "Overview.md").

5. Choose **Create database**.

AWS CLI
To turn on the Advanced mode of Database Insights when creating a DB cluster, call the [create-db-cluster](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md") AWS CLI command and supply the following values:

- `--database-insights-mode advanced` to turn on the Advanced mode of Database Insights.
- `--engine` – The database engine for the DB cluster.
- `--db-cluster-identifier` – The identifier for the DB cluster.
- `--enable-performance-insights` to turn on Performance Insights for Database Insights.
- `--performance-insights-retention-period` – The retention period for data for your DB cluster. To turn on Database Insights, the retention period must be at least 465 days.

The following example enables the Advanced mode of Database Insights when creating a DB cluster.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster \
    --database-insights-mode advanced \
    --engine aurora-postgresql \
    --db-cluster-identifier sample-db-identifier \
    --enable-performance-insights \
    --performance-insights-retention-period 465
```

For Windows:

```
aws rds create-db-cluster ^
    --database-insights-mode advanced ^
    --engine aurora-postgresql ^
    --db-cluster-identifier sample-db-identifier ^
    --enable-performance-insights ^
    --performance-insights-retention-period 465
```

RDS API
To turn on the Advanced mode of Database Insights when you create a DB cluster, specify the following parameters for your [CreateDBCluster](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md") Amazon RDS API operation.

- `DatabaseInsightsMode` to `advanced`
- `EnablePerformanceInsights` to `True`
- `PerformanceInsightsRetentionPeriod` to at least 465 days

## Turning on the Advanced mode of Database Insights when modifying a DB cluster

Turn on Database Insights when modifying a database for Amazon Aurora. Modifying a DB cluster to enable the Advanced mode of Database Insights doesn't cause downtime.

###### Note

To enable Database Insights, each DB instance in a DB cluster must have the same Performance Insights and Enhanced Monitoring settings.

Console
In the console, you can turn on the Advanced mode of Database Insights when you
modify a DB cluster. Settings for Database Insights apply to all DB instances in your DB cluster.

###### To turn on the Advanced mode of Database Insights when modifying a DB cluster using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**.
3. Choose a DB cluster, and choose **Modify**.
4. In the **Database Insights** section, select **Advanced mode**. Then, choose the following options:
   - **Retention** – The amount of time to retain Performance Insights data. The retention period must be 15 months for the Advanced mode of Database Insights.
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
- `PerformanceInsightsRetentionPeriod` to at least 465 days
