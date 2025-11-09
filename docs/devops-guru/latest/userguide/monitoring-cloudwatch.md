# Monitoring DevOps Guru with Amazon CloudWatch

You can monitor DevOps Guru using CloudWatch, which collects raw data and processes it into readable,
near real-time metrics. These statistics are kept for 15 months, so that you can access
historical information and gain a better perspective on how your web application or service is
performing. You can also set alarms that watch for certain thresholds and send notifications
or take actions when those thresholds are met. For more information, see the
[Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

For DevOps Guru, you can track metrics for insights and metrics for your DevOps Guru usage. You might
want to watch for a large number of created `Insights` to help you determine if
your operational solutions are experiencing anomalous behavior. Or you might want to watch your
DevOps Guru usage to help track your costs.

The DevOps Guru service reports the following metrics in the `AWS/DevOps-Guru`
namespace.

###### Topics

- [Insight metrics](#insight-metrics "#insight-metrics")
- [DevOps Guru usage metrics](#usage-metrics "#usage-metrics")

## Insight metrics

You can use CloudWatch to track a metric to show you how many insights are created in your AWS
account. You can specify the `Type` dimension to track `proactive` or
`reactive` insights. Do not specify a dimension if you want to track all
insights.

**Metrics**

| Metric    | Description                                                                                                                          |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| `Insight` | The number of insights created in an AWS account.<br>Valid dimensions: `Type`<br>Valid statistics: Sample count, Sum<br>Units: Count |

The following dimension is supported for the DevOps Guru `Insight` metric.

**Dimensions**

| Dimension | Description                                                                                                                                                            |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Type`    | This is the type of the insight. Do not specify a dimension for the `Insights` metric<br>if you want to track all insights. Valid values are: `proactive`, `reactive`. |

## DevOps Guru usage metrics

You can use CloudWatch to track your Amazon DevOps Guru usage.

**Metrics**

| Metric      | Description                                                                                                                                                                                                                                                                                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CallCount` | The number of calls made by one of the following DevOps Guru methods.<br>• `ListInsights`<br>• `ListAnomaliesForInsight`<br>• `ListRecommendations`<br>• `ListEvents`<br>• `SearchInsights`<br>• `DescribeInsight`<br>• `DescribeAnomaly`<br>Valid dimensions: `Service`, `Class`,<br>`Type`, `Resource`<br>Valid statistics: Sample count, Sum<br>Units: Count |

The following dimensions are supported for the DevOps Guru usage metrics.

**Dimensions**

| Dimension  | Description                                                                                                                                                                                                          |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Service`  | This is the name of the AWS service that contains the resource. For example, for<br>DevOps Guru, this value is `DevOps-Guru`.                                                                                        |
| `Class`    | This is the<br>class of the resource that is tracked. DevOps Guru uses this dimension with the value<br>`None`.                                                                                                      |
| `Type`     | This is type<br>of the resource that is tracked. DevOps Guru uses this dimension with the value<br>`API`.                                                                                                            |
| `Resource` | This is the<br>name of the DevOps Guru operation. Valid values are: `ListInsights`,<br>`ListAnomaliesForInsight`, `ListRecommendations`,<br>`ListEvents`, `SearchInsights`,<br>`DescribeInsight`, `DescribeAnomaly`. |
