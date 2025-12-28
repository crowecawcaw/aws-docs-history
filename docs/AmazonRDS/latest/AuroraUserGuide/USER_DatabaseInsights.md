# Turning on the Standard mode of Database Insights for Amazon Aurora

To turn on the Standard mode of Database Insights for Amazon Aurora, use the following procedures.

## Turning on the Standard mode of Database Insights when creating a DB cluster

Turn on the Standard mode of Database Insights when creating a database for Amazon Aurora.

Console
In the console, you can turn on the Standard mode of Database Insights when you
create a DB cluster. Settings for Database Insights apply to all DB instances in your DB cluster.

###### To turn on the Standard mode of Database Insights when creating a DB cluster using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**.
3. Choose **Create database**.
4. In the **Database Insights** section, select **Standard mode**. Then, choose from the following options to turn Performance Insights on or off:
   - To turn off Performance Insights, deselect **Enable Performance Insights**.
   - To turn on Performance Insights, select **Enable Performance Insights**. To configure Performance Insights, specify the following options:
     - **Retention** – The amount of time to retain Performance Insights data. The retention period must be at least 7 days.
     - **AWS KMS key** – Specify your
       KMS key. Performance Insights encrypts all
       potentially sensitive data using your KMS key. Data is
       encrypted in flight and at rest. For more information, see
       [Encrypting Amazon Aurora
       resources](Overview.md "Overview.md").

5. Choose **Create database**.

AWS CLI
To turn on the Standard mode of Database Insights when creating a DB cluster, call the [create-db-cluster](../../../cli/latest/reference/rds/create-db-cluster.md "../../../cli/latest/reference/rds/create-db-cluster.md") AWS CLI command and supply the following values:

- `--database-insights-mode standard` to turn on the Standard mode of Database Insights.
- `--engine` – The database engine for the DB cluster.
- `--db-cluster-identifier` – The identifier for the DB cluster.
- `--enable-performance-insights` or `--no-enable-performance-insights` to turn Performance Insights on or off. If you specify `--enable-performance-insights`, you must also specify the `--performance-insights-retention-period` – The retention period for data for your DB cluster. The retention period must be at least 7 days.

The following example enables the Standard mode of Database Insights and Performance Insights when creating a DB cluster.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster \
    --database-insights-mode standard \
    --engine aurora-postgresql \
    --db-cluster-identifier sample-db-identifier \
    --enable-performance-insights \
    --performance-insights-retention-period 7
```

For Windows:

```
aws rds create-db-cluster ^
    --database-insights-mode standard ^
    --engine aurora-postgresql ^
    --db-cluster-identifier sample-db-identifier ^
    --enable-performance-insights ^
    --performance-insights-retention-period 7
```

The following example enables the Standard mode of Database Insights and disables Performance Insights when creating a DB cluster.

For Linux, macOS, or Unix:

```
aws rds create-db-cluster \
    --database-insights-mode standard \
    --engine aurora-postgresql \
    --db-cluster-identifier sample-db-identifier \
    --no-enable-performance-insights
```

For Windows:

```
aws rds create-db-cluster ^
    --database-insights-mode standard ^
    --engine aurora-postgresql ^
    --db-cluster-identifier sample-db-identifier ^
    --no-enable-performance-insights
```

RDS API
To turn on the Standard mode of Database Insights when you create a DB cluster, specify the following parameters for your [CreateDBCluster](../APIReference/API_CreateDBCluster.md "../APIReference/API_CreateDBCluster.md") Amazon RDS API operation.

- `DatabaseInsightsMode` to `standard`
- `EnablePerformanceInsights` to `True` or `False`. If you set `EnablePerformanceInsights` to `True`, you must set `PerformanceInsightsRetentionPeriod` to at least 7 days.

## Turning on the Standard mode of Database Insights when modifying a DB cluster

Turn on Standard mode of Database Insights when modifying a database for Amazon Aurora. Modifying a DB cluster to enable the Standard mode of Database Insights doesn't cause downtime.

###### Note

To enable Database Insights, each DB instance in a DB cluster must have the same Performance Insights and Enhanced Monitoring settings.

Console
In the console, you can turn on the Standard mode of Database Insights when you
modify a DB cluster. Settings for Database Insights apply to all DB instances in your DB cluster.

###### To turn on the Standard mode of Database Insights when modifying a DB cluster using the console

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Databases**.
3. Choose a DB cluster, and choose **Modify**.
4. In the **Database Insights** section, select **Standard mode**. Then, choose from the following options:
   - To turn off Performance Insights, deselect **Enable Performance Insights**.
   - To turn on Performance Insights, select **Enable Performance Insights**. To configure Performance Insights, specify the following options:
     - **Retention** – The amount of time to retain Performance Insights data. The retention period must be at least 7 days.
     - **AWS KMS key** – Specify your
       KMS key. Performance Insights encrypts all
       potentially sensitive data using your KMS key. Data is
       encrypted in flight and at rest. For more information, see
       [Encrypting Amazon Aurora
       resources](Overview.md "Overview.md").

5. Choose **Continue**.
6. For **Scheduling of Modifications**, choose **Apply immediately**. If you
   choose **Apply during the next scheduled maintenance window**, your database
   ignores this setting and turns on the Standard mode of Database Insights immediately.
7. Choose **Modify cluster**.

AWS CLI
To turn on the Standard mode of Database Insights when modifying a DB cluster, call the [modify-db-cluster](../../../cli/latest/reference/rds/modify-db-cluster.md "../../../cli/latest/reference/rds/modify-db-cluster.md") AWS CLI command and supply the following values:

- `--database-insights-mode standard` to turn on the Standard mode of Database Insights.
- `--db-cluster-identifier` – The identifier for the DB cluster.
- `--enable-performance-insights` or `--no-enable-performance-insights` to turn Performance Insights on or off. If you specify `--enable-performance-insights`, you must also specify the `--performance-insights-retention-period` – The retention period for data for your DB cluster. The retention period must be at least 7 days.

The following example enables the Standard mode of Database Insights and enables Performance Insights when modifying a DB cluster.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --database-insights-mode standard \
    --db-cluster-identifier sample-db-identifier \
    --enable-performance-insights \
    --performance-insights-retention-period 7
```

For Windows:

```
aws rds modify-db-cluster ^
    --database-insights-mode standard ^
    --db-cluster-identifier sample-db-identifier ^
    --enable-performance-insights ^
    --performance-insights-retention-period 7
```

The following example enables the Standard mode of Database Insights and disables Performance Insights when modifying a DB cluster.

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
    --database-insights-mode standard \
    --db-cluster-identifier sample-db-identifier \
    --no-enable-performance-insights
```

For Windows:

```
aws rds modify-db-cluster ^
    --database-insights-mode standard ^
    --db-cluster-identifier sample-db-identifier ^
    --no-enable-performance-insights
```

RDS API
To turn on the Standard mode of Database Insights when you modify a DB cluster, specify the following parameters for your [ModifyDBCluster](../APIReference/API_ModifyDBCluster.md "../APIReference/API_ModifyDBCluster.md") Amazon RDS API operation.

- `DatabaseInsightsMode` to `standard`
- `EnablePerformanceInsights` to `True` or `False`. If you set `EnablePerformanceInsights` to `True`, you must set `PerformanceInsightsRetentionPeriod` to at least 7 days.
