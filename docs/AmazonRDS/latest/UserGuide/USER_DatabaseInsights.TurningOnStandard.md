

# Turning on the Standard mode of Database Insights for Amazon RDS
<a name="USER_DatabaseInsights.TurningOnStandard"></a>

To turn on the Standard mode of Database Insights for Amazon RDS, use the following procedures.

## Turning on the Standard mode of Database Insights when creating a DB instance or Multi-AZ DB cluster
<a name="USER_DatabaseInsights.TurnOnCreateDatabaseStandard"></a>

Turn on the Standard mode of Database Insights when creating a database for Amazon RDS.

------
#### [ Console ]

In the console, you can turn on the Standard mode of Database Insights when you create a DB instance or Multi-AZ DB cluster.

**To turn on the Standard mode of Database Insights when creating a DB instance or Multi-AZDB cluster using the console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose **Databases**.

1. Choose **Create database**.

1. In the **Database Insights** section, select **Standard mode**. Then, choose from the following options to turn Performance Insights on or off:
   + To turn off Performance Insights, deselect **Enable Performance Insights**.
   + To turn on Performance Insights, select **Enable Performance Insights**. To configure Performance Insights, specify the following options:
     + **Retention** – The amount of time to retain Performance Insights data. The retention period must be at least 7 days.
     + **AWS KMS key** – Specify your KMS key. Performance Insights encrypts all potentially sensitive data using your KMS key. Data is encrypted in flight and at rest. For more information, see [Encrypting Amazon RDS resources](Overview.Encryption.md).

1. Choose **Create database**.

------
#### [ AWS CLI ]

To turn on the Standard mode of Database Insights when creating a DB instance or Multi-AZ DB cluster, call the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) or [create-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster.html) AWS CLI command and supply the following values:
+ `--database-insights-mode standard` to turn on the Standard mode of Database Insights.
+ `--engine` – The database engine for the DB instance.
+ `--db-instance-identifier` – The identifier for the DB instance or `--db-cluster-identifier` – The identifier for the Multi-AZ DB cluster.
+ `--enable-performance-insights` or `--no-enable-performance-insights` to turn Performance Insights on or off. If you specify `--enable-performance-insights`, you must also specify the `--performance-insights-retention-period` – The retention period for data for your DB instance. The retention period must be at least 7 days.

The following example enables the Standard mode of Database Insights and Performance Insights when creating a DB instance.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --database-insights-mode standard \ 
    --engine postgresql \
    --db-instance-identifier sample-db-identifier \
    --enable-performance-insights \
    --performance-insights-retention-period 7
```

For Windows:

```
aws rds create-db-instance ^
    --database-insights-mode standard ^ 
    --engine postgresql ^
    --db-instance-identifier sample-db-identifier ^
    --enable-performance-insights ^
    --performance-insights-retention-period 7
```

The following example enables the Standard mode of Database Insights and disables Performance Insights when creating a DB instance.

For Linux, macOS, or Unix:

```
aws rds create-db-instance \
    --database-insights-mode standard \ 
    --engine postgresql \
    --db-instance-identifier sample-db-identifier \
    --no-enable-performance-insights
```

For Windows:

```
aws rds create-db-instance ^
    --database-insights-mode standard ^ 
    --engine postgresql ^
    --db-instance-identifier sample-db-identifier ^
    --no-enable-performance-insights
```

------
#### [ RDS API ]

To turn on the Standard mode of Database Insights when you create a DB instance or Multi-AZ DB cluster, specify the following parameters for your [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) or [CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html) Amazon RDS API operation.
+ `DatabaseInsightsMode` to `standard`
+ `EnablePerformanceInsights` to `True` or `False`. If you set `EnablePerformanceInsights` to `True`, you must set `PerformanceInsightsRetentionPeriod` to at least 7 days.

------

## Turning on the Standard mode of Database Insights when modifying a DB instance or Multi-AZ DB cluster
<a name="USER_DatabaseInsights.TurnOnModifyDatabaseStandard"></a>

Turn on Standard mode of Database Insights when modifying a database for Amazon RDS. Modifying a DB instance to enable the Standard mode of Database Insights doesn't cause downtime.

**Note**  
To enable Database Insights, each DB instance in a Multi-AZ DB cluster must have the same Performance Insights and Enhanced Monitoring settings.

------
#### [ Console ]

In the console, you can turn on the Standard mode of Database Insights when you modify a DB instance or Multi-AZ DB cluster.

**To turn on the Standard mode of Database Insights when modifying a DB instance or Multi-AZDB cluster using the console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose **Databases**.

1. Choose a DB instance or Multi-AZ DB cluster, and choose **Modify**.

1. In the **Database Insights** section, select **Standard mode**. Then, choose from the following options:
   + To turn off Performance Insights, deselect **Enable Performance Insights**.
   + To turn on Performance Insights, select **Enable Performance Insights**. To configure Performance Insights, specify the following options:
     + **Retention** – The amount of time to retain Performance Insights data. The retention period must be at least 7 days.
     + **AWS KMS key** – Specify your KMS key. Performance Insights encrypts all potentially sensitive data using your KMS key. Data is encrypted in flight and at rest. For more information, see [Encrypting Amazon RDS resources](Overview.Encryption.md).

1. Choose **Continue**.

1. For **Scheduling of Modifications**, choose **Apply immediately**. If you choose **Apply during the next scheduled maintenance window**, your database ignores this setting and turns on the Standard mode of Database Insights immediately.

1. Choose **Modify instance**.

------
#### [ AWS CLI ]

To turn on the Standard mode of Database Insights when modifying a DB instance or Multi-AZ DB cluster, call the [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) or [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) AWS CLI command and supply the following values:
+ `--database-insights-mode standard` to turn on the Standard mode of Database Insights.
+ `--db-instance-identifier` – The identifier for the DB instance or `--db-cluster-identifier` – The identifier for the Multi-AZ DB cluster.
+ `--enable-performance-insights` or `--no-enable-performance-insights` to turn Performance Insights on or off. If you specify `--enable-performance-insights`, you must also specify the `--performance-insights-retention-period` – The retention period for data for your DB instance or Multi-AZ DB cluster. The retention period must be at least 7 days.

The following example enables the Standard mode of Database Insights and enables Performance Insights when modifying a DB instance.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --database-insights-mode standard \
    --db-instance-identifier sample-db-identifier \
    --enable-performance-insights \
    --performance-insights-retention-period 7
```

For Windows:

```
aws rds modify-db-instance ^
    --database-insights-mode standard ^
    --db-instance-identifier sample-db-identifier ^
    --enable-performance-insights ^
    --performance-insights-retention-period 7
```

The following example enables the Standard mode of Database Insights and disables Performance Insights when modifying a DB instance.

For Linux, macOS, or Unix:

```
aws rds modify-db-instance \
    --database-insights-mode standard \
    --db-instance-identifier sample-db-identifier \
    --no-enable-performance-insights
```

For Windows:

```
aws rds modify-db-instance ^
    --database-insights-mode standard ^
    --db-instance-identifier sample-db-identifier ^
    --no-enable-performance-insights
```

------
#### [ RDS API ]

To turn on the Standard mode of Database Insights when you modify a DB instance or Multi-AZ DB cluster, specify the following parameters for your [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) or [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) Amazon RDS API operation.
+ `DatabaseInsightsMode` to `standard`
+ `EnablePerformanceInsights` to `True` or `False`. If you set `EnablePerformanceInsights` to `True`, you must set `PerformanceInsightsRetentionPeriod` to at least 7 days.

------