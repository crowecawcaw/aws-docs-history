

# Required permissions for in-console monitoring
<a name="monitoring-instance-session-permissions"></a>

To view instance and session performance metrics on the WorkSpaces Applications console, your IAM user or role must have the following CloudWatch permissions:
+ `cloudwatch:GetMetricData` – Retrieves metric data points. This permission is required to display metric graphs (CPU, memory, GPU, frame rate, latency, and so on).
+ `cloudwatch:ListMetrics` – Lists available metrics. This permission is required to discover and populate available metrics for the selected fleet or session.

**Example IAM Policy Example**  

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:GetMetricData",
                "cloudwatch:ListMetrics"
            ],
            "Resource": "*"
        }
    ]
}
```

**Note**  
Without these permissions, the monitoring panels on the WorkSpaces Applications console display an "Insufficient permissions" error or show no data. The fleet and session details are still visible (governed by `appstream:*` permissions), but the metric graphs do not render.