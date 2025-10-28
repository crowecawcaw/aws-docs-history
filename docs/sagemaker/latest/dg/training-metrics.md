# Amazon CloudWatch Metrics for Monitoring and Analyzing Training Jobs

An Amazon SageMaker training job is an iterative process that teaches a model to make predictions by
presenting examples from a training dataset. Typically, a training algorithm computes
several metrics, such as training error and prediction accuracy. These metrics help diagnose
whether the model is learning well and will generalize well for making predictions on unseen
data. The training algorithm writes the values of these metrics to logs, which SageMaker AI monitors
and sends to Amazon CloudWatch in real time. To analyze the performance of your training job, you can
view graphs of these metrics in CloudWatch. When a training job has completed, you can also get a
list of the metric values that it computes in its final iteration by calling the [`DescribeTrainingJob`](../APIReference/API_DescribeTrainingJob.md "../APIReference/API_DescribeTrainingJob.md")
operation.

###### Note

Amazon CloudWatch supports [high-resolution
custom metrics](../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md "../../../AmazonCloudWatch/latest/monitoring/publishingMetrics.md"), and its finest resolution is 1 second. However, the finer
the resolution, the shorter the lifespan of the CloudWatch metrics. For the 1-second frequency
resolution, the CloudWatch metrics are available for 3 hours. For more information about the
resolution and the lifespan of the CloudWatch metrics, see [GetMetricStatistics](../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md "../../../AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.md") in the _Amazon CloudWatch API
Reference_.

###### Tip

If you want to profile your training job with a finer resolution down to
100-millisecond (0.1 second) granularity and store the training metrics indefinitely in
Amazon S3 for custom analysis at any time, consider using [Amazon SageMaker Debugger](train-debugger.md "train-debugger.md"). SageMaker Debugger provides
built-in rules to automatically detect common training issues; it detects hardware
resource utilization issues (such as CPU, GPU, and I/O bottlenecks) and non-converging
model issues (such as overfit, vanishing gradients, and exploding tensors). SageMaker Debugger
also provides visualizations through Studio Classic and its profiling report. To explore the
Debugger visualizations, see [SageMaker Debugger
Insights Dashboard Walkthrough](debugger-on-studio-insights-walkthrough.md "debugger-on-studio-insights-walkthrough.md"), [Debugger Profiling Report Walkthrough](debugger-profiling-report.md#debugger-profiling-report-walkthrough "debugger-profiling-report.md#debugger-profiling-report-walkthrough"), and [Analyze Data Using the SMDebug Client Library](debugger-analyze-data.md "debugger-analyze-data.md").

###### Topics

- [Define Training Metrics](define-train-metrics.md "define-train-metrics.md")
- [View training job metrics](view-train-metrics.md "view-train-metrics.md")
- [Example: Viewing a Training and Validation
  Curve](train-valid-curve.md "train-valid-curve.md")
