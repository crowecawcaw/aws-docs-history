

# View training job metrics
<a name="view-train-metrics"></a>

You can view the metrics emitted from your Amazon SageMaker training jobs in either the Amazon CloudWatch or SageMaker AI console.

## Monitor training job metrics (CloudWatch console)
<a name="view-train-metrics-cw"></a>

You can monitor the metrics that a training job emits in real time in the CloudWatch console.

**To monitor training job metrics (CloudWatch console)**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch](https://console.aws.amazon.com/cloudwatch).

1. Choose **Metrics**, then choose **/aws/sagemaker/TrainingJobs**.

1. Choose **TrainingJobName**.

1. On the **All metrics** tab, choose the names of the training metrics that you want to monitor.

1. On the **Graphed metrics** tab, configure the graph options. For more information about using CloudWatch graphs, see [Graph Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph_metrics.html) in the *Amazon CloudWatch User Guide*.

## Monitor training job metrics (SageMaker AI console)
<a name="view-train-metrics-sm"></a>

You can monitor the metrics that a training job emits in real time by using the SageMaker AI console.

**To monitor training job metrics (SageMaker AI console)**

1. Open the SageMaker AI console at [https://console.aws.amazon.com/sagemaker](https://console.aws.amazon.com/sagemaker).

1. Choose **Training jobs**, then choose the training job whose metrics you want to see.

1. Choose **TrainingJobName**.

1. In the **Monitor** section, you can review the graphs of instance utilization and algorithm metrics.  
![Example graphs in the Monitor section in the console.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/console-metrics.png)