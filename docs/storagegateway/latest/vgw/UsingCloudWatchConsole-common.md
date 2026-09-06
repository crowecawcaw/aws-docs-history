

# Using Amazon CloudWatch Metrics
<a name="UsingCloudWatchConsole-common"></a>

You can get monitoring data for your gateway using either the AWS Management Console or the CloudWatch API. The console displays a series of graphs based on the raw data from the CloudWatch API. You can also use the CloudWatch API through one of the [AWS Software Development Kits (SDKs)](https://aws.amazon.com/tools) or the [Amazon CloudWatch API](https://aws.amazon.com/cloudwatch) tools. Depending on your needs, you might prefer to use either the graphs displayed in the console or retrieved from the API. 

Regardless of which method you choose to use to work with metrics, you must specify the following information: 
+ The metric dimension to work with. A *dimension* is a name-value pair that helps you to uniquely identify a metric. The dimensions for Storage Gateway are `GatewayId`, `GatewayName`, and `VolumeId`. In the CloudWatch console, you can use the `Gateway Metrics` and `Volume Metrics` views to easily select gateway-specific and volume-specific dimensions. For more information about dimensions, see [Dimensions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch_concepts.html#Dimension) in the *Amazon CloudWatch User Guide*.
+ The metric name, such as `ReadBytes`.

The following table summarizes the types of Storage Gateway metric data that you can use. 



- **`AWS/StorageGateway`**
  - **Dimension:**  GatewayId, GatewayName  / **Description:** These dimensions filter for metric data that describes aspects of the gateway. You can identify a gateway to work with by specifying both the `GatewayId` and the `GatewayName` dimensions.<br />Throughput and latency data of a gateway are based on all the volumes in the gateway.<br />Data is available automatically in 5-minute periods at no charge. 
  - **Dimension:**  VolumeId  / **Description:** This dimension filters for metric data that is specific to a volume. Identify a volume to work with by its `VolumeId` dimension.<br />Data is available automatically in 5-minute periods at no charge. 



Working with gateway and volume metrics is similar to working with other service metrics. You can find a discussion of some of the most common metrics tasks in the CloudWatch documentation listed following: 
+ [Viewing Available Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html)
+ [Getting Statistics for a Metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/US_GetStatistics.html)
+ [Creating CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html)