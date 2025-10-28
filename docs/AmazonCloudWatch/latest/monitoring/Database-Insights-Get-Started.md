# Get started with CloudWatch Database Insights

The Standard mode of Database Insights is enabled by default for your Amazon RDS and Aurora databases. To get started with the Advanced mode of Database Insights, you can create a new database or modify a database.

For information about enabling the Advanced mode or the Standard mode of Database Insights for an Amazon RDS database, see the following topics.

- [Turning on the Advanced mode of Database Insights for Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.md "../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.md") in the _Amazon RDS User Guide_
- [Turning on the Standard mode of Database Insights for Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.md "../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.md") in the _Amazon RDS User Guide_
- [Turning CloudWatch Database Insights on or off when creating a DB instance or Multi-AZ DB cluster for Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.md "../../../AmazonRDS/latest/UserGuide/USER_DatabaseInsights.md") in the _Amazon RDS User Guide_
  For information about enabling the Advanced mode or the Standard mode of Database Insights for an Amazon Aurora database, see the following topics.

- [Turning on the Advanced mode of Database Insights for Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.md") in the _Amazon Aurora User Guide_
- [Turning on the Standard mode of Database Insights for Amazon Aurora](../../../AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.md "../../../AmazonRDS/latest/AuroraUserGuide/USER_DatabaseInsights.md") in the _Amazon Aurora User Guide_
  For information about enabling the Advanced mode or the Standard mode of Database Insights for an Aurora PostgreSQL Limitless Database, see the following topics.

- [Turning on the Advanced mode of Database Insights for Aurora PostgreSQL Limitless Database](../../../AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.cwdbi.md "../../../AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.cwdbi.md") in the _Amazon Aurora User Guide_
- [Turning on the Standard mode of Database Insights for Aurora PostgreSQL Limitless Database](../../../AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.cwdbi.md "../../../AmazonRDS/latest/AuroraUserGuide/limitless-monitoring.cwdbi.md") in the _Amazon Aurora User Guide_

## Required permissions for Database Insights

Certain IAM permissions are required to use Database Insights. Database Insights requires permissions for CloudWatch, CloudWatch Logs, Amazon RDS, and Amazon RDS Performance Insights.
You might not need to provide these permissions to your user or role if you have broader permissions.

The following CloudWatch permissions are required to use Database Insights.

- `cloudwatch:BatchGetServiceLevelIndicatorReport`
- `cloudwatch:DescribeAlarms`
- `cloudwatch:GetDashboard`
- `cloudwatch:GetMetricData`
- `cloudwatch:ListMetrics`
- `cloudwatch:PutDashboard`

The following CloudWatch Logs permissions are required to use Database Insights.

- `logs:DescribeLogGroups`
- `logs:GetQueryResults`
- `logs:StartQuery`
- `logs:StopQuery`

The following Amazon RDS permissions are required to use Database Insights.

- `rds:DescribeDBClusters`
- `rds:DescribeDBInstances`
- `rds:DescribeEvents`
- `rds:DescribeDBShardGroups` (if you are monitoring Aurora PostgreSQL Limitless Databases

The following Performance Insights permissions are required to use Database Insights.

- `pi:ListAvailableResourceMetrics`
- `pi:ListAvailableResourceDimensions`
- `pi:DescribeDimensionKeys`
- `pi:GetDimensionKeyDetails`
- `pi:GetResourceMetrics`
- `pi:ListPerformanceAnalysisReports`
- `pi:GetResourceMetadata`
- `pi:GetPerformanceAnalysisReport`
- `pi:CreatePerformanceAnalysisReport`
- `pi:DeletePerformanceAnalysisReport`
- `pi:ListTagsForResource`
- `pi:TagResource`
- `pi:UntagResource`

The following sample policy contains the permissions required for full access to Database Insights.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Effect" : "Allow",
 "Action" : [
 "cloudwatch:BatchGetServiceLevelIndicatorReport",
 "cloudwatch:DescribeAlarms",
 "cloudwatch:GetMetricStatistics",
 "cloudwatch:GetMetricData",
 "cloudwatch:ListMetrics",
 "cloudwatch:PutDashboard"
 ],
 "Resource" : "*"
 },
 {
 "Effect" : "Allow",
 "Action" : [
 "logs:DescribeLogGroups",
 "logs:GetQueryResults",
 "logs:StartQuery",
 "logs:StopQuery"
 ],
 "Resource" : "*"
 },
 {
 "Effect" : "Allow",
 "Action" : [
 "pi:DescribeDimensionKeys",
 "pi:GetDimensionKeyDetails",
 "pi:GetResourceMetadata",
 "pi:GetResourceMetrics",
 "pi:ListAvailableResourceDimensions",
 "pi:ListAvailableResourceMetrics",
 "pi:CreatePerformanceAnalysisReport",
 "pi:GetPerformanceAnalysisReport",
 "pi:ListPerformanceAnalysisReports",
 "pi:DeletePerformanceAnalysisReport",
 "pi:TagResource",
 "pi:UntagResource",
 "pi:ListTagsForResource"
 ],
 "Resource" : "arn:aws:pi:*:*:*/rds/*"
 },
 {
 "Effect" : "Allow",
 "Action" : [
 "rds:DescribeDBInstances",
 "rds:DescribeDBClusters",
 "rds:DescribeEvents"
 ],
 "Resource" : "*"
 }
 ]
}`

```
