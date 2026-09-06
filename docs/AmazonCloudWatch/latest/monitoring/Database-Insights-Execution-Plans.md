

# Analyzing execution plans with CloudWatch Database Insights
<a name="Database-Insights-Execution-Plans"></a>

You can analyze execution plans for the Amazon Aurora PostgreSQL, RDS for Microsoft SQL Server and RDS for Oracle databases by using the following methods.
+ **Sliced by** dropdown – Choose the **Plans** dimension in the **Database load** chart to view how different plans contribute to DB Load over time.
+ **Top SQL** tab – Choose **DB Load Analysis**, then choose the **Top SQL** tab to view the number of plans for each digest query.

  To analyze execution plans for a digest query, choose the query and then choose the **Plans** tab. For more information, see the following procedure.

## Prerequisites
<a name="Database-Insights-Execution-Plans-prereqs"></a>

To analyze execution plans, you must be using the Advanced mode of Database Insights. For information on how to turn on Advanced mode, see [Turning on the Advanced mode of Database Insights for Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.TurningOnAdvanced.html) and [Turning on the Advanced mode of Database Insights for Amazon Relational Database Service](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.TurningOnAdvanced.html).

If you are using Aurora PostgreSQL, you also have the following prerequisites:
+ Your DB instance must use Aurora PostgreSQL version 14.10, 15.5, or later. For information about upgrading your Aurora PostgreSQL DB cluster, see [Upgrading Amazon Aurora PostgreSQL DB clusters](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_UpgradeDBInstance.PostgreSQL.html) in the *Amazon Aurora User Guide*.
+ You must configure your DB cluster to analyze execution plans by setting the parameter `aurora_compute_plan_id` to `on` with one of the following options.
  + [Creating a DB cluster parameter group in Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CreatingCluster.html) in the *Amazon Aurora User Guide*
  + [Modifying parameters in a DB cluster parameter group in Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.ModifyingCluster.html) in the *Amazon Aurora User Guide*

## Analyze execution plans
<a name="Database-Insights-Execution-Plans-analyze"></a>

To analyze execution plans, use the following procedure.

**To analyze execution plans**

1. Sign in to the AWS Management Console and open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. Choose **Insights**.

1. Choose **Database Insights**.

1. Choose the **Database Instance** view.

1. Choose a DB instance.

1. Choose the **Top SQL** tab. The **Plans Count** column shows the number of plans collected for each digest query.

1. (Optional) If the **Plans Count** column doesn't appear, choose the **Settings** icon on the **Top SQL** table to customize the visibility and order of columns.  
![Settings for the plan details table.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/DBInsights2.png)

1. Choose a digest query to expand it into its component statements.  
![Expand a query into its component statements.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/dbi_did-dbload-expand.png)

1. Scroll down and view the SQL text. Then, choose the **Plans** tab.

   By default, CloudWatch displays the estimated execution plan. For Aurora PostgreSQL, to view actual execution plans, enable the `aurora_stat_plans.with_analyze` parameter for your DB instance. For more information about the parameter `aurora_stat_plans.with_analyze`, see [Monitoring query execution plans and peak memory for Aurora PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraPostgreSQL.Monitoring.Query.Plans.html#aurora.with_analyze) in the *Amazon Aurora User Guide*.

1. To compare plans from the same digest query, choose two **Plans** from the **Plans for digest query** list.

   You can view either one or two plans for a query at a time. In the following example screenshot, both plans are for Aurora PostgreSQL.   
![Compare plans.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/dbi_did-plans.png)

1. You can also view how each plan contributes to DBLoad over time by choosing **Plans** in the **Slice by** drop-down in the DBLoad chart.  
![Top SQL table showing load by plans with query statements, execution metrics, and plan counts.](http://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/images/DBInsights_OverTime.png)