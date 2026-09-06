

# Enabling and disabling detailed per-query and database counter metrics
<a name="USER_PerfInsights.Enabling"></a>

Detailed per-query and database counter metrics are enabled by default when you select Database Insights Advanced mode. If you select Database Insights Standard mode, you can enable them when you create your DB cluster, and turn them off later by modifying your DB cluster from the console. Enabling detailed per-query and database counter metrics doesn't cause downtime, a reboot, or a failover.

**Note**  
Performance Schema is an optional performance tool used by Aurora MySQL. If you turn Performance Schema on or off, you need to reboot. If you enable or disable detailed per-query and database counter metrics, however, you don't need to reboot. For more information, see [Overview of the Performance Schema for Database Insights in Aurora MySQL](USER_PerfInsights.EnableMySQL.md).

If you use detailed per-query and database counter metrics with Aurora global databases, turn them on individually for the databases in each AWS Region. For details, see [Monitoring an Amazon Aurora global database with Amazon RDS Performance Insights](aurora-global-database-monitoring.md#aurora-global-database-pi). 

The Database Insights agent consumes limited CPU and memory on the DB host. When the DB load is high, the agent limits the performance impact by collecting data less frequently.

------
#### [ Console ]

In the console, you can enable collecting detailed per-query and database counter metrics for Database Insights Standard mode when you create or modify a DB cluster. Enabling detailed per-query and database counter metrics allows you to manage Database Insights settings and options for your DB cluster. Cluster level settings apply to all DB instances in the cluster.

**Enabling or disabling detailed per-query and database counter metrics when creating a DB cluster**

After creating a new DB cluster, Amazon RDS enables detailed per-query and database counter metrics by default. To turn it off, choose the option **Database Insights – Standard** and deselect the option **Enable collecting detailed per-query and database counter metrics**.

 To create a DB cluster, follow the instructions for your DB engine in [Creating an Amazon Aurora DB cluster](Aurora.CreateInstance.md). 

The following screenshot shows the **Database Insights** section.

![Database Insights section on the DB cluster creation page, with the option to enable detailed database metrics.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/db_insights_enabling.png)


If you choose **Enable collecting detailed per-query and database counter metrics**, you have the following options:
+ **Retention** – The amount of time to retain Database Insights data. The retention setting is **Default (7 days)**. To retain your performance data for longer, specify 1–24 months. For more information about retention periods, see [Pricing and data retention for Database Insights](USER_PerfInsights.Overview.cost.md).
+ **AWS KMS key** – Specify your AWS KMS key. Database Insights encrypts all potentially sensitive data using your KMS key. Data is encrypted in flight and at rest. For more information, see [Changing an KMS key policy for Database Insights](USER_PerfInsights.access-control.cmk-policy.md).

**Enabling or disabling detailed per-query and database counter metrics when modifying a DB cluster**

In the console, you can modify a DB cluster to manage detailed per-query and database counter metrics for Database Insights.

**To manage detailed per-query and database counter metrics for a DB cluster using the console**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose **Databases**.

1. Choose a DB cluster, and choose **Modify**.

1. Select **Enable collecting detailed per-query and database counter metrics** to enable it. To turn it off for your DB cluster, choose the option **Database Insights – Standard** and deselect the option **Enable collecting detailed per-query and database counter metrics**.

   If you choose **Enable collecting detailed per-query and database counter metrics**, you have the following options:
   + **Retention** – The amount of time to retain Database Insights data. The retention setting is **Default (7 days)**. To retain your performance data for longer, specify 1–24 months. For more information about retention periods, see [Pricing and data retention for Database Insights](USER_PerfInsights.Overview.cost.md).
   + **AWS KMS key** – Specify your KMS key. Database Insights encrypts all potentially sensitive data using your KMS key. Data is encrypted in flight and at rest. For more information, see [Encrypting Amazon Aurora resources](Overview.Encryption.md).  
![Database Insights section on the modify DB cluster page, with the option to enable detailed database metrics.](http://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/images/db_insights_enabling.png)

1. Choose **Continue**.

1. For **Scheduling of Modifications**, choose Apply immediately. If you choose Apply during the next scheduled maintenance window, your instance ignores this setting and turns on collecting detailed per-query and database counter metrics immediately.

1. Choose **Modify instance**.

------
#### [ AWS CLI ]

When you use the [create-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance.html) AWS CLI command, turn on detailed per-query and database counter metrics by specifying `--enable-performance-insights` and set `--database-insights-mode` to either `advanced` or `standard`. To turn them off, specify `--no-enable-performance-insights` and set `database-insights-mode` to `standard`.

You can also specify these values using the following AWS CLI commands:
+  [create-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-cluster.html) 
+  [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) 
+  [create-db-instance-read-replica](https://docs.aws.amazon.com/cli/latest/reference/rds/create-db-instance-read-replica.html) 
+  [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) 
+  [restore-db-instance-from-s3](https://docs.aws.amazon.com/cli/latest/reference/rds/restore-db-instance-from-s3.html) 

**To manage detailed per-query and database counter metrics for a DB cluster using the AWS CLI**
+ Call the [modify-db-cluster](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-cluster.html) AWS CLI command and supply the following values:
  + `--db-cluster-identifier` – The name of the DB instance in your DB cluster.
  + `--enable-performance-insights` to turn on or `--no-enable-performance-insights` to turn off
  + `database-insights-mode` – The mode of Database Insights for the DB cluster. To turn off detailed per-query and database counter metrics, set this value to `standard`.

  The following example turns on detailed per-query and database counter metrics for `sample-db-cluster`.

  For Linux, macOS, or Unix:

  ```
  aws rds modify-db-cluster \
  	--database-insights-mode standard \
      --db-cluster-identifier sample-db-instance \
      --enable-performance-insights
  ```

  For Windows:

  ```
  aws rds modify-db-cluster ^
  	--database-insights-mode standard ^
      --db-cluster-identifier sample-db-instance ^
      --enable-performance-insights
  ```

When you turn on detailed per-query and database counter metrics in the CLI, you can optionally specify the number of days to retain the data with the `--performance-insights-retention-period` option. You can specify `7`, {{month}} \* 31 (where {{month}} is a number from 1–23), or `731`. For example, if you want to retain your performance data for 3 months, specify `93`, which is 3 \* 31. The default is `7` days. For more information about retention periods, see [Pricing and data retention for Database Insights](USER_PerfInsights.Overview.cost.md).

The following example turns on detailed per-query and database counter metrics for `sample-db-cluster` and specifies that the data is retained for 93 days (3 months).

For Linux, macOS, or Unix:

```
aws rds modify-db-cluster \
	--database-insights-mode standard \
    --db-cluster-identifier sample-db-instance \
    --enable-performance-insights \
    --performance-insights-retention-period 93
```

For Windows:

```
aws rds modify-db-cluster ^
	--database-insights-mode standard ^
    --db-cluster-identifier sample-db-instance ^
    --enable-performance-insights ^
    --performance-insights-retention-period 93
```

If you specify a retention period such as 94 days, which isn't a valid value, RDS issues an error.

```
An error occurred (InvalidParameterValue) when calling the CreateDBInstance operation: 
Invalid Performance Insights retention period. Valid values are: [7, 31, 62, 93, 124, 155, 186, 217, 
248, 279, 310, 341, 372, 403, 434, 465, 496, 527, 558, 589, 620, 651, 682, 713, 731]
```

**Note**  
You can only toggle detailed per-query and database counter metrics for an instance in a DB cluster where they are not managed at the cluster level.

------
#### [ RDS API ]

When you create a new DB instance in your DB cluster using the [CreateDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstance.html) operation Amazon RDS API operation, turn on detailed per-query and database counter metrics by setting `EnablePerformanceInsights` to `True`. To turn them off, set `EnablePerformanceInsights` to `False` and set `DatabaseInsightsMode` to `standard`.

You can also specify the `EnablePerformanceInsights` value using the following API operations:
+  [CreateDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBCluster.html) 
+  [ModifyDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBCluster.html) 
+  [ModifyDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyDBInstance.html) 
+  [CreateDBInstanceReadReplica](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateDBInstanceReadReplica.html) 
+  [RestoreDBInstanceFromS3](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RestoreDBInstanceFromS3.html) 

When you turn on detailed per-query and database counter metrics, you can optionally specify the amount of time, in days, to retain the data with the `PerformanceInsightsRetentionPeriod` parameter. You can specify `7`, {{month}} \* 31 (where {{month}} is a number from 1–23), or `731`. For example, if you want to retain your performance data for 3 months, specify `93`, which is 3 \* 31. The default is `7` days. For more information about retention periods, see [Pricing and data retention for Database Insights](USER_PerfInsights.Overview.cost.md).

------