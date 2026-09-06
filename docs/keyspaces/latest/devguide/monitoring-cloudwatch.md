

# Monitoring Amazon Keyspaces with Amazon CloudWatch
<a name="monitoring-cloudwatch"></a>

You can monitor Amazon Keyspaces using Amazon CloudWatch, which collects raw data and processes it into readable, near real-time metrics. These statistics are kept for 15 months, so that you can access historical information and gain a better perspective on how your web application or service is performing. 

You can also set alarms that watch for certain thresholds, and send notifications or take actions when those thresholds are met. For more information, see the [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

**Note**  
To get started quickly with a preconfigured CloudWatch dashboard showing common metrics for Amazon Keyspaces, you can use an CloudFormation template available from [https://github.com/aws-samples/amazon-keyspaces-cloudwatch-cloudformation-templates](https://github.com/aws-samples/amazon-keyspaces-cloudwatch-cloudformation-templates).

**Topics**
+ [How do I use Amazon Keyspaces metrics?](#how-to-use-metrics)
+ [Amazon Keyspaces metrics and dimensions](metrics-dimensions.md)
+ [Viewing Amazon Keyspaces metrics in CloudWatch](view-metrics.md)
+ [Creating CloudWatch alarms to monitor Amazon Keyspaces](creating-alarms.md)

## How do I use Amazon Keyspaces metrics?
<a name="how-to-use-metrics"></a>

The metrics reported by Amazon Keyspaces provide information that you can analyze in different ways. The following list shows some common uses for the metrics. These are suggestions to get you started, not a comprehensive list. For more information about metrics and retention, see [Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Metric). 



|  How can I?  |  Relevant metrics  | 
| --- | --- | 
| How can I determine if any system errors occurred? | You can monitor `SystemErrors` to determine whether any requests resulted in a server error code. Typically, this metric should be equal to zero. If it isn't, you might want to investigate. | 
| How can I compare average provisioned read to consumed read capacity? | To monitor average provisioned read capacity and consumed read capacity1.  Set the **Period** for `ConsumedReadCapacityUnits` and `ProvisionedReadCapacityUnits` to the interval you want to monitor. <br />2.  Change the **Statistic** for `ConsumedReadCapacityUnits` from `Average` to `Sum`. <br />3.  Create a new empty **Math expression**. <br />4.  In the **Details** section of the new math expression, enter the **Id** of `ConsumedReadCapacityUnits` and divide the metric by the CloudWatch **PERIOD** function of the metric (metric\_id/(**PERIOD**(metric\_id)). <br />5.  Unselect `ConsumedReadCapacityUnits`. <br />You can now compare your average consumed read capacity to your provisioned capacity. For more information on basic arithmetic functions and how to create a time series see [Using metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html). | 
| How can I compare average provisioned write to consumed write capacity? | To monitor average provisioned write capacity and consumed write capacity1.  Set the **Period** for `ConsumedWriteCapacityUnits` and `ProvisionedWriteCapacityUnits` to the interval you want to monitor. <br />2.  Change the **Statistic** for `ConsumedWriteCapacityUnits` from `Average` to `Sum`. <br />3.  Create a new empty **Math expression**. <br />4.  In the **Details** section of the new math expression, enter the **Id** of `ConsumedWriteCapacityUnits` and divide the metric by the CloudWatch **PERIOD** function of the metric (metric\_id/(**PERIOD**(metric\_id)). <br />5.  Unselect `ConsumedWriteCapacityUnits`. <br />You can now compare your average consumed write capacity to your provisioned capacity. For more information on basic arithmetic functions and how to create a time series see [Using metric math](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/using-metric-math.html).  | 