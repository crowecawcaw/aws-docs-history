# Visualizing your service quotas and setting
 alarms

For some AWS services, you can use the usage metrics to visualize your current service usage on CloudWatch graphs and
 dashboards. You can use a CloudWatch metric math function to display the service quotas for those
 resources on your graphs. You can also configure alarms that alert you when your usage
 approaches a service quota. For more information about service quotas, see [What Is Service Quotas](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html "https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html")
 in the *Service Quotas User Guide*.

If you are signed in to an account that is set up as a monitoring account in CloudWatch cross-account 
 observability, you can use that monitoring account to visualize service quotas and set alarms for metrics in the 
 source accounts that are linked to that monitoring account. For more information, see
 [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

The following services
 integrate their usage metrics with Service Quotas:


* AWS CloudHSM
* [Amazon Chime SDK](https://docs.aws.amazon.com/chime-sdk/latest/dg/usage-metrics.html "https://docs.aws.amazon.com/chime-sdk/latest/dg/usage-metrics.html")
* [Amazon CloudWatch](CloudWatch-Usage-Metrics.md "CloudWatch-Usage-Metrics.md")
* [Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.html#CloudWatchLogs-Usage-Metrics "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Monitoring-CloudWatch-Metrics.html#CloudWatchLogs-Usage-Metrics")
* [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html "https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/metrics-dimensions.html")
* [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html#service-quota-metrics "https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.html#service-quota-metrics")
* [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/monitoring-usage.html "https://docs.aws.amazon.com/AmazonECR/latest/userguide/monitoring-usage.html")
* Elastic Load Balancing
* AWS Fargate
* [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/monitoring-cloudwatch.html "https://docs.aws.amazon.com/fis/latest/userguide/monitoring-cloudwatch.html")
* [AWS Interactive Video Service](https://docs.aws.amazon.com/ivs/latest/userguide/service-quotas.html#quotas-cloudwatch-integration "https://docs.aws.amazon.com/ivs/latest/userguide/service-quotas.html#quotas-cloudwatch-integration")
* AWS Key Management Service
* [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/monitoring-with-cloudwatch-metrics.html#fh-metrics-usage "https://docs.aws.amazon.com/firehose/latest/dev/monitoring-with-cloudwatch-metrics.html#fh-metrics-usage")
* [Amazon Location Service](https://docs.aws.amazon.com/location/latest/developerguide/monitoring-using-cloudwatch.html#metrics-exported-to-cloudwatch "https://docs.aws.amazon.com/location/latest/developerguide/monitoring-using-cloudwatch.html#metrics-exported-to-cloudwatch")
* [Amazon Managed Blockchain (AMB) Query](https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/cw-usage-metrics.html "https://docs.aws.amazon.com/managed-blockchain/latest/ambq-dg/cw-usage-metrics.html")
* Amazon SageMaker AI
* [Multi-party approval](https://docs.aws.amazon.com/mpa/latest/userguide/monitoring-cloudwatch.html "https://docs.aws.amazon.com/mpa/latest/userguide/monitoring-cloudwatch.html")
###### To visualize a service quota and optionally set an alarm

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**.
3. On the **All metrics** tab, choose **Usage**, and
 then choose **By AWS Resource**.


The list of service quota usage metrics appears.
4. Select the check box next to one of the metrics.


The graph displays your current usage of that AWS resource.
5. To add your service quota to the graph, do the following:


	1. Choose the **Graphed metrics** tab.
	2. Choose **Math expression**, **Start with an empty
	 expression**. In the new row, under **Details**, enter
	 `SERVICE_QUOTA(m1)`.
	
	
	A new line is added to the graph, displaying the service quota for the resource
	 represented in the metric.
6. To see your current usage as a percentage of the quota, add a new expression or change the
 current **SERVICE\_QUOTA** expression. The new expression to use 
 is `m1/SERVICE_QUOTA(m1)*100`.
7. (Optional) To set an alarm that notifies you if you approach the service quota, do the following:


	1. On the row with `m1/SERVICE_QUOTA(m1)*100`, 
	 under **Actions**, choose the alarm icon. It looks like a bell.
	
	
	The alarm creation page appears.
	2. Under **Conditions**, ensure that **Threshold
	 type** is **Static** and **Whenever Expression1
	 is** is set to **Greater**. Under
	 **than**, enter `80`. This creates an alarm
	 that goes into ALARM state when your usage exceeds 80 percent of the quota.
	3. Choose **Next**.
	4. On the next page, select an Amazon SNS topic or create a new one, and then choose
	 **Next**. The topic you select is notified when the alarm goes to
	 ALARM state.
	5. On the next page, enter a name and description for the alarm, and then 
	 choose **Next**.
	6. Choose **Create alarm**.
