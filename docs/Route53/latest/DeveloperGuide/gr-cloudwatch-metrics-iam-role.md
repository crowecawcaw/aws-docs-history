

# IAM role for publishing CloudWatch metrics from DNS query logs
<a name="gr-cloudwatch-metrics-iam-role"></a>

The AWS Identity and Access Management (IAM) policy that's attached to your IAM role or user must include at least the following permissions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CloudWatchMetricFilterPermissions",
            "Effect": "Allow",
            "Action": [
                "logs:PutMetricFilter",
                "logs:DescribeMetricFilters",
                "logs:DeleteMetricFilter",
                "logs:TestMetricFilter"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CloudWatchLogsInsightsPermissions",
            "Effect": "Allow",
            "Action": [
                "logs:StartQuery",
                "logs:StopQuery",
                "logs:GetQueryResults",
                "logs:DescribeQueries",
                "logs:DescribeLogGroups"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CloudWatchMetricsNamespacePermissions",
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricData",
                "cloudwatch:GetMetricData",
                "cloudwatch:ListMetrics"
            ],
            "Resource": "*"
        }
    ]
}
```