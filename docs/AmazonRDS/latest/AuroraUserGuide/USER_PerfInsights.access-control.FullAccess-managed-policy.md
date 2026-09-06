

# Attaching the AmazonRDSPerformanceInsightsFullAccess policy to an IAM principal
<a name="USER_PerfInsights.access-control.FullAccess-managed-policy"></a>

`AmazonRDSPerformanceInsightsFullAccess` is an AWS managed policy that grants access to all operations of the Amazon RDS Database Insights API.

If you attach `AmazonRDSPerformanceInsightsFullAccess` to a permission set or role, you must also attach the following CloudWatch permissions:
+ `GetMetricStatistics`
+ `ListMetrics`
+ `GetMetricData`

With these permissions, the recipient can use Database Insights with other console features.

 For more information about CloudWatch permissions, see [Amazon CloudWatch permissions reference](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/permissions-reference-cw.html).

For more information about `AmazonRDSPerformanceInsightsFullAccess`, see [AWS managed policy: AmazonRDSPerformanceInsightsFullAccess](rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSPerformanceInsightsFullAccess).