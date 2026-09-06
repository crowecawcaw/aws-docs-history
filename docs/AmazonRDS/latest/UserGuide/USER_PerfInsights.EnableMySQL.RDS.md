

# Turn on the Performance Schema for Amazon RDS for MariaDB or MySQL
<a name="USER_PerfInsights.EnableMySQL.RDS"></a>

Assume that Database Insights is turned on for your DB instance or Multi-AZ DB cluster but isn't currently managing the Performance Schema. If you want to allow Database Insights to manage the Performance Schema automatically, complete the following steps.

**To configure the Performance Schema for automatic management**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. Choose **Parameter groups**.

1. Select the name of the parameter group for your DB instance or Multi-AZ DB cluster.

1. Choose **Edit**.

1. Enter **performance\_schema** in the search bar.

1. Select the `performance_schema` parameter.

1. Choose **Set to default value**.

1. Confirm by choosing **Set values to default**.

1. Choose **Save Changes**.

1. Reboot the DB instance or Multi-AZ DB cluster.
**Important**  
Whenever you turn the Performance Schema on or off, make sure to reboot the DB instance or Multi-AZ DB cluster.

For more information about modifying instance parameters, see [Modifying parameters in a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.Modifying.md). For more information about the dashboard, see [Database Insights](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_DatabaseInsights.html). For more information about the MySQL performance schema, see [MySQL Performance Schema](https://dev.mysql.com/doc/refman/8.0/en/performance-schema.html) (for 8.0) and [MySQL Performance Schema](https://dev.mysql.com/doc/refman/8.4/en/performance-schema.html) (for 8.4) in the MySQL documentation.