

# Pricing and data retention for Database Insights
<a name="USER_PerfInsights.Overview.cost"></a>

By default, Database Insights includes 7 days of performance data history and 1 million API requests per month. You can also purchase longer retention periods. For complete pricing information, see [Database Insights Pricing](https://aws.amazon.com/cloudwatch/pricing/).

In the RDS console, you can choose any of the following retention periods for your Database Insights data:
+ **Default (7 days)**
+ **{{n}} months**, where **{{n}}** is a number from 1–24

![The retention period options for Database Insights data.](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/images/pi-retention-periods.png)


To learn how to set a retention period using the AWS CLI, see [Enabling and disabling detailed per-query and database counter metrics](USER_PerfInsights.Enabling.md).

**Note**  
Stopping a DB instance or Multi-AZ DB cluster with Database Insights enabled doesn't affect data retention. While a DB instance or Multi-AZ DB cluster is stopped, Database Insights won't collect any data.