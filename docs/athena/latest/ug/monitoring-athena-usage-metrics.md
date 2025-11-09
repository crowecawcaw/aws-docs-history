# Monitor Athena usage metrics with

CloudWatch

You can use CloudWatch usage metrics to provide visibility into your how your account uses
resources by displaying your current service usage on CloudWatch graphs and dashboards.

For Athena, usage availability metrics correspond to AWS service quotas for Athena. You
can configure alarms that alert you when your usage approaches a service quota. For more
information about Athena service quotas, see [Service Quotas](service-limits.md "service-limits.md"). For more information about AWS usage metrics, see
[AWS
usage metrics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Service-Quota-Integration.md") in the _Amazon CloudWatch User Guide_.

Athena publishes the following metrics in the `AWS/Usage` namespace.

| Metric name     | Description                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ResourceCount` | The sum of all queued and executing queries per AWS Region per<br>account, separated by query type (DML or DDL). Maximum is the only<br>useful statistic for this metric.<br>This metric publishes periodically every minute. If you are not<br>running any queries, the metric reports nothing (not even 0). The metric<br>publishes only if active queries are running at the time the metric is<br>taken. |

The following dimensions are used to refine the usage metrics that are published by
Athena.

| Dimension  | Description                                                                                                          |
| ---------- | -------------------------------------------------------------------------------------------------------------------- |
| `Service`  | The name of the AWS service containing the resource. For Athena, the<br>value for this dimension is `Athena`.        |
| `Resource` | The type of resource that is running. The resource value for Athena<br>query usage is `ActiveQueryCount`.            |
| `Type`     | The type of entity that's being reported. Currently, the only valid<br>value for Athena usage metrics is `Resource`. |
| `Class`    | The class of resource being tracked. For Athena, `Class` can<br>be `DML` or `DDL`.                                   |

## View Athena resource usage

metrics in the CloudWatch console

You can use the CloudWatch console to see a graph of Athena usage metrics and configure
alarms that alert you when your usage approaches a service quota.

###### To view Athena resource usage metrics

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, **All
   metrics**.
3. Choose **Usage**, and then choose **By AWS
   Resource**.

The list of service quota usage metrics appears. 4. Select the check box that is next to **Athena** and
**ActiveQueryCount**. 5. Choose the **Graphed metrics** tab.

The graph above displays your current usage of the AWS resource.

For information about adding service quotas to the graph and setting an alarm that
notifies you if you approach the service quota, see [Visualizing your service quotas and setting alarms](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Quotas-Visualize-Alarms.md") in the _Amazon CloudWatch User Guide_. For information about setting usage limits
per workgroup, see [Configure per-query and
per-workgroup data usage controls](workgroups-setting-control-limits-cloudwatch.md "workgroups-setting-control-limits-cloudwatch.md").
