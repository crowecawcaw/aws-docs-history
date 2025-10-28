# Attaching the

AmazonRDSPerformanceInsightsReadOnly policy to an IAM principal

`AmazonRDSPerformanceInsightsReadOnly` is an AWS managed
policy that grants access to all read-only operations of the Amazon RDS Performance Insights API.

If you attach `AmazonRDSPerformanceInsightsReadOnly` to a permission set or role,
you must also attach the following CloudWatch
permissions:

- `GetMetricStatistics`
- `ListMetrics`
- `GetMetricData`
  With these permissions, the recipient can use
  Performance Insights with other console features.

For more information about CloudWatch permissions, see
[Amazon CloudWatch
permissions reference](../../../AmazonCloudWatch/latest/monitoring/permissions-reference-cw.md "../../../AmazonCloudWatch/latest/monitoring/permissions-reference-cw.md").

For more information about `AmazonRDSPerformanceInsightsReadOnly`, see [AWS managed policy: AmazonRDSPerformanceInsightsReadOnly](rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSPerformanceInsightsReadOnly "rds-security-iam-awsmanpol.md#rds-security-iam-awsmanpol-AmazonRDSPerformanceInsightsReadOnly").
