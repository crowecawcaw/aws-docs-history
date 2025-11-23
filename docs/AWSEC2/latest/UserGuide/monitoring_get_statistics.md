# Statistics for CloudWatch metrics for your

instances

You can get statistics for the CloudWatch metrics for your instances. _Statistics_ are metric data aggregations over
specified periods of time. CloudWatch provides statistics based on the metric data points provided
by your custom data or provided by other services in AWS to CloudWatch. Aggregations are made
using the namespace, metric name, dimensions, and the data point unit of measure, within the
time period you specify. The following table describes the available statistics.

| Statistic     | Description                                                                                                                                                                                                                                                                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Minimum`     | The lowest value observed during the specified period. You can use this value<br>to determine low volumes of activity for your application.                                                                                                                                                                                                         |
| `Maximum`     | The highest value observed during the specified period. You can use this value<br>to determine high volumes of activity for your application.                                                                                                                                                                                                       |
| `Sum`         | All values submitted for the matching metric added together. This statistic<br>can be useful for determining the total volume of a metric.                                                                                                                                                                                                          |
| `Average`     | The value of `Sum` / `SampleCount` during the specified<br>period. By comparing this statistic with the `Minimum` and<br>`Maximum`, you can determine the full scope of a metric and how close<br>the average use is to the `Minimum` and `Maximum`. This<br>comparison helps you to know when to increase or decrease your resources as<br>needed. |
| `SampleCount` | The count (number) of data points used for the statistical calculation.                                                                                                                                                                                                                                                                             |
| `pNN.NN`      | The value of the specified percentile. You can specify any percentile, using<br>up to two decimal places (for example, p95.45).                                                                                                                                                                                                                     |

###### Contents

- [Get statistics for a specific instance](US_SingleMetricPerInstance.md "US_SingleMetricPerInstance.md")
- [Aggregate statistics across instances](GetSingleMetricAllDimensions.md "GetSingleMetricAllDimensions.md")
- [Aggregate statistics by Amazon EC2 Auto Scaling group](GetMetricAutoScalingGroup.md "GetMetricAutoScalingGroup.md")
- [Aggregate statistics by AMI](US_SingleMetricPerAMI.md "US_SingleMetricPerAMI.md")
