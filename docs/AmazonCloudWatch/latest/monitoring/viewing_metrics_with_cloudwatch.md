# View available metrics

Metrics are grouped first by namespace, and then by the various dimension combinations
within each namespace. For example, you can view all EC2 metrics, EC2 metrics grouped by
instance, or EC2 metrics grouped by Auto Scaling group.

Only the AWS services that you're using send metrics to Amazon CloudWatch.

For a list of AWS services that send metrics to CloudWatch, see [AWS services that publish CloudWatch metrics](aws-services-cloudwatch-metrics.md "aws-services-cloudwatch-metrics.md").
From this page, you can also see the metrics and dimensions that are published by each of
those services.

###### Note

Metrics that have not had any new data points in the past two weeks do not appear in the
console. They also do not appear when you type their metric name or dimension names in the
search box in the **All metrics** tab in the console, and they are not
returned in the results of a [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") command. The best way to retrieve these metrics is with the [get-metric-data](../../../cli/latest/reference/cloudwatch/get-metric-data.md "../../../cli/latest/reference/cloudwatch/get-metric-data.md") or [get-metric-statistics](../../../cli/latest/reference/cloudwatch/get-metric-statistics.md "../../../cli/latest/reference/cloudwatch/get-metric-statistics.md")
commands in the AWS CLI.

If the old metric you want to view has a current metric with similar dimensions, you can
view that current similar metric and then choose the **Source** tab, and
change the metric name and dimension fields to the ones that you want, and also change the
time range to a time when the metric was being reported.

The following steps help you browse through the metric namespaces to find and view
metrics. You can also search for metrics using targeted search terms. For more information,
see [Search for available metrics](finding_metrics_with_cloudwatch.md "finding_metrics_with_cloudwatch.md").

If you are browsing in an account set up as a monitoring account in CloudWatch cross-account
observability, you can view metrics from the source accounts linked to this monitoring
account. When metrics from source accounts are displayed, the ID or label of the account that
they are from is also displayed. For more information, see [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

###### Note

After the source account stops sharing the metrics with the
_Monitoring_ account, the _Source_ account metrics
data is not accessible to the monitoring account. Source metric names can be visible to the
monitoring account for upto 14 days.

###### To view available metrics by namespace and dimension using the console

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, **All
   metrics**.
3. Select a metric namespace (for example, **EC2** or
   **Lambda**).
4. Select a metric dimension (for example, **Per-Instance Metrics** or
   **By Function Name**).
5. The **Browse** tab displays all metrics for that dimension in the
   namespace. By each metric name is an information button you can choose to see a pop-up
   with the metric definition.

If this is a monitoring account in CloudWatch cross-account observability, you also see the
metrics from the source accounts linked to this monitoring account. The **Account
label** and **Account id** columns in the table display which
account each metric is from.

You can do the following:

    1. To sort the table, use the column heading.
    2. To graph a metric, select the check box next to the metric. To select all metrics,
     select the check box in the heading row of the table.
    3. To filter by account, choose the account label or account ID and then choose
     **Add to search**.
    4. To filter by resource, choose the resource ID and then choose **Add to
     search**.
    5. To filter by metric, choose the metric name and then choose **Add to
     search**.

6. (Optional) To add this graph to a CloudWatch dashboard, choose **Actions**,
   **Add to dashboard**.
   **To view available metrics by account namespace, dimension, or metric
   using the AWS CLI**

Use the [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md")
command to list CloudWatch metrics. For a list of the namespaces, metrics, and dimensions for all
services that publish metrics, see [AWS services that publish CloudWatch metrics](aws-services-cloudwatch-metrics.md "aws-services-cloudwatch-metrics.md").

The following example command lists all the metrics for Amazon EC2.

```
`aws cloudwatch list-metrics --namespace AWS/EC2`
```

The following is example output.

```
{
  "Metrics" : [
    ...
    {
        "Namespace": "AWS/EC2",
        "Dimensions": [
            {
                "Name": "InstanceId",
                "Value": "i-1234567890abcdef0"
            }
        ],
        "MetricName": "NetworkOut"
    },
    {
        "Namespace": "AWS/EC2",
        "Dimensions": [
            {
                "Name": "InstanceId",
                "Value": "i-1234567890abcdef0"
            }
        ],
        "MetricName": "CPUUtilization"
    },
    {
        "Namespace": "AWS/EC2",
        "Dimensions": [
            {
                "Name": "InstanceId",
                "Value": "i-1234567890abcdef0"
            }
        ],
        "MetricName": "NetworkIn"
    },
    ...
  ]
}
```

###### To list all the available metrics for a specified resource

The following example specifies the `AWS/EC2` namespace and the
`InstanceId` dimension to view the results for the specified instance
only.

```
`aws cloudwatch list-metrics --namespace AWS/EC2 --dimensions Name=InstanceId,Value=`i-1234567890abcdef0``
```

###### To list a metric for all resources

The following example specifies the `AWS/EC2` namespace and a metric name to
view the results for the specified metric only.

```
`aws cloudwatch list-metrics --namespace AWS/EC2 --metric-name `CPUUtilization``
```

###### To retrieve metrics from linked source accounts in CloudWatch cross-account

observability

The following example is run in a monitoring account to retrieve metrics from both the
monitoring account and all linked source accounts. If you do not add
`--include-linked-accounts`, the command returns only the monitoring account’s
metrics.

```
`aws cloudwatch list-metrics --include-linked-accounts`
```

###### To retrieve metrics from a source account in CloudWatch cross-account observability

The following example is run in a monitoring account to retrieve metrics from the source
account with the ID 111122223333.

```
`aws cloudwatch list-metrics --include-linked-accounts --owning-account "111122223333"`
```
