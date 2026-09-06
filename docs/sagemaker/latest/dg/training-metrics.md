

# Amazon CloudWatch Metrics for Monitoring and Analyzing Training Jobs
<a name="training-metrics"></a>

An Amazon SageMaker training job is an iterative process that teaches a model to make predictions by presenting examples from a training dataset. Typically, a training algorithm computes several metrics, such as training error and prediction accuracy. These metrics help diagnose whether the model is learning well and will generalize well for making predictions on unseen data. The training algorithm writes the values of these metrics to logs, which SageMaker AI monitors and sends to Amazon CloudWatch in real time. To analyze the performance of your training job, you can view graphs of these metrics in CloudWatch. When a training job has completed, you can also get a list of the metric values that it computes in its final iteration by calling the [`DescribeTrainingJob`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrainingJob.html) operation.

**Note**  
Amazon CloudWatch supports [high-resolution custom metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/publishingMetrics.html), and its finest resolution is 1 second. However, the finer the resolution, the shorter the lifespan of the CloudWatch metrics. For the 1-second frequency resolution, the CloudWatch metrics are available for 3 hours. For more information about the resolution and the lifespan of the CloudWatch metrics, see [GetMetricStatistics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetMetricStatistics.html) in the *Amazon CloudWatch API Reference*. 

**Tip**  
If you want to profile your training job with a finer resolution down to 100-millisecond (0.1 second) granularity and store the training metrics indefinitely in Amazon S3 for custom analysis at any time, consider using [Amazon SageMaker Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html). SageMaker Debugger provides built-in rules to automatically detect common training issues; it detects hardware resource utilization issues (such as CPU, GPU, and I/O bottlenecks) and non-converging model issues (such as overfit, vanishing gradients, and exploding tensors). SageMaker Debugger also provides visualizations through Studio Classic and its profiling report. To explore the Debugger visualizations, see [SageMaker Debugger Insights Dashboard Walkthrough](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-on-studio-insights-walkthrough.htm), [Debugger Profiling Report Walkthrough](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-profiling-report.html#debugger-profiling-report-walkthrough), and [Analyze Data Using the SMDebug Client Library](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-analyze-data.html).

**Topics**
+ [Define Training Metrics](define-train-metrics.md)
+ [View training job metrics](view-train-metrics.md)
+ [Example: Viewing a Training and Validation Curve](train-valid-curve.md)