

# CodePipeline CloudWatch metrics
<a name="metrics-dimensions"></a>

You can use metrics in CloudWatch to measure CodePipeline pipelines. You can use the following metrics to measure pipeline duration and failed pipeline executions. 

You can monitor your pipelines at two levels: 

Pipeline level  
These metrics are at the pipeline level. Choose **By Pipeline** in CloudWatch. Available pipelines will be listed in CloudWatch.

AWS account level  
These metrics are for all pipelines in an account. To see metrics at the AWS account level, choose **Account Metrics** in CloudWatch.

For more information about viewing metrics, see [View available metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html) in the *Amazon CloudWatch User Guide*.

**Topics**
+ [PipelineDuration](#metrics-dimensions-duration)
+ [FailedPipelineExecutions](#metrics-dimensions-failed-pipelines)

## PipelineDuration
<a name="metrics-dimensions-duration"></a>

The `PipelineDuration` metric measures the duration of the pipeline execution. This metric is available for the pipeline level only.

Units: Seconds

## FailedPipelineExecutions
<a name="metrics-dimensions-failed-pipelines"></a>

The `FailedPipelineExecutions` metric measures the number of pipeline executions that failed. This metric is available at the pipeline level and the account level.

This metric includes a separate count for pipeline executions with a retry of a failed action. In other words, when a failed action is retried in a pipeline, this will count as a separate pipeline execution metric. For example, for a pipeline with an S3 source action where the S3 source action fails the first time, that makes one execution, and then the source action is retried and fails again. For this example, the metric will be the following:

```
FailedPipelineExecutionAttempts: 2
```

Units: Count