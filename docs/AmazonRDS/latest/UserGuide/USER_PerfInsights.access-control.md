# Attaching

the AmazonRDSPerformanceInsightsFullAccess policy to an IAM principal

`AmazonRDSPerformanceInsightsFullAccess` is an AWS managed
policy that grants access to all operations of the Amazon RDS Performance Insights API.

If you attach `AmazonRDSPerformanceInsightsFullAccess` to a permission set
or role, you must also attach the following CloudWatch
permissions:

- `GetMetricStatistics`
- `ListMetrics`
- `GetMetricData`
  With these permissions, the recipient can use
  Performance Insights with other console features.

For more information about CloudWatch permissions, see
[Amazon CloudWatch
permissions reference](../../../AmazonCloudWatch/latest/monitoring/permissions-reference-cw.md "../../../AmazonCloudWatch/latest/monitoring/permissions-reference-cw.md").

For more information about `AmazonRDSPerformanceInsightsFullAccess`, see [AWS managed policy: AmazonRDSPerformanceInsightsFullAccess](rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSPerformanceInsightsFullAccess "rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSPerformanceInsightsFullAccess").
