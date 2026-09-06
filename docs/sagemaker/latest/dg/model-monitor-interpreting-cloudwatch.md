

# CloudWatch Metrics
<a name="model-monitor-interpreting-cloudwatch"></a>

**Note**  
Amazon SageMaker Model Monitor is no longer open to new customers. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for Model Monitor, but we do not plan to introduce new features. For more information, see [Amazon SageMaker Model Monitor availability change](model-monitor-availability-change.md). 

You can use the built-in Amazon SageMaker Model Monitor container for CloudWatch metrics. When the `emit_metrics` option is `Enabled` in the baseline constraints file, SageMaker AI emits these metrics for each feature/column observed in the dataset in the following namespace:
+ `For real-time endpoints: /aws/sagemaker/Endpoints/data-metric` namespace with `EndpointName` and `ScheduleName` dimensions.
+ `For batch transform jobs: /aws/sagemaker/ModelMonitoring/data-metric` namespace with `MonitoringSchedule` dimension.

For numerical fields, the built-in container emits the following CloudWatch metrics:
+ Metric: Max → query for `MetricName: feature_data_{feature_name}, Stat: Max`
+ Metric: Min → query for `MetricName: feature_data_{feature_name}, Stat: Min`
+ Metric: Sum → query for `MetricName: feature_data_{feature_name}, Stat: Sum`
+ Metric: SampleCount → query for `MetricName: feature_data_{feature_name}, Stat: SampleCount`
+ Metric: Average → query for `MetricName: feature_data_{feature_name}, Stat: Average`

For both numerical and string fields, the built-in container emits the following CloudWatch metrics:
+ Metric: Completeness → query for `MetricName: feature_non_null_{feature_name}, Stat: Sum`
+ Metric: Baseline Drift → query for `MetricName: feature_baseline_drift_{feature_name}, Stat: Sum`