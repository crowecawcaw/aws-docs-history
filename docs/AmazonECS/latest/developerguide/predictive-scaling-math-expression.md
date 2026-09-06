

# Use metric math expressions
<a name="predictive-scaling-math-expression"></a>

The following section provides information about using metric math with predictive scaling policies in your policy. 

## Understand metric math
<a name="predictive-scaling-custom-metrics-math"></a>

If all you want to do is aggregate existing metric data, CloudWatch metric math saves you the effort and cost of publishing another metric to CloudWatch. You can use any metric that AWS provides, and you can also use metrics that you define as part of your applications.

For more information, see [Using metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) in the *Amazon CloudWatch User Guide*. 

If you choose to use a metric math expression in your predictive scaling policy, consider the following points:
+ Metric math operations use the data points of the unique combination of metric name, namespace, and dimension keys/value pairs of metrics. 
+ You can use any arithmetic operator (\+ - \* / ^), statistical function (such as AVG or SUM), or other function that CloudWatch supports. 
+ You can use both metrics and the results of other math expressions in the formulas of the math expression. 
+ Your metric math expressions can be made up of different aggregations. However, it's a best practice for the final aggregation result to use `Average` for the scaling metric and `Sum` for the load metric.
+ Any expressions used in a metric specification must eventually return a single time series.

To use metric math, do the following:
+ Choose one or more CloudWatch metrics. Then, create the expression. For more information, see [Using metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html) in the *Amazon CloudWatch User Guide*. 
+ Verify that the metric math expression is valid by using the CloudWatch console or the CloudWatch [GetMetricData](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricData.html) API.