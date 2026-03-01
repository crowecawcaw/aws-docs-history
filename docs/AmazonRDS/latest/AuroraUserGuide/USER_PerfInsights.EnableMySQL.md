# Turn on the Performance Schema for Aurora MySQL

Assume that Performance Insights is turned on for your DB instance but isn't
currently managing the Performance Schema. If you want to allow Performance Insights to manage the Performance Schema automatically,
complete the following steps.

###### To configure the Performance Schema for automatic management

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. Choose **Parameter groups**.
3. Select the name of the parameter group for your DB instance.
4. Choose **Edit**.
5. Enter `performance_schema` in the search bar.
6. Select the `performance_schema` parameter.
7. Choose **Set to default value**.
8. Confirm by choosing **Set values to default**.
9. Choose **Save
   Changes**.
10. Reboot the DB instance.

###### Important

Whenever you turn the Performance Schema on or off, make sure to reboot the DB instance.
For more information about modifying instance parameters, see [Modifying parameters in a DB parameter group in Amazon Aurora](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). For more information about
the dashboard, see [Analyzing metrics with the Performance Insights dashboard](USER_PerfInsights.md "USER_PerfInsights.md"). For more information about the
MySQL performance schema, see [MySQL
Performance Schema](https://dev.mysql.com/doc/refman/8.0/en/performance-schema.html "https://dev.mysql.com/doc/refman/8.0/en/performance-schema.html") (for 8.0) and [MySQL
Performance Schema](https://dev.mysql.com/doc/refman/8.4/en/performance-schema.html "https://dev.mysql.com/doc/refman/8.4/en/performance-schema.html") (for 8.4) in the MySQL documentation.
