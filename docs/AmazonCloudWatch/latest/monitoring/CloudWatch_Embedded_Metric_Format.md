# Embedding metrics within logs

The CloudWatch embedded metric format allows you to generate custom metrics asynchronously in the form of logs 
 written to CloudWatch Logs. You can embed custom metrics alongside detailed log event data, and CloudWatch automatically 
 extracts the custom metrics so that you can visualize and alarm on them, for real-time incident detection. Additionally, 
 the detailed log events associated with the extracted metrics can be queried using CloudWatch Logs Insights to provide deep 
 insights into the root causes of operational events. 

Embedded metric format helps you generate actionable custom metrics from ephemeral resources such as Lambda functions and containers. 
 By using the embedded metric format to send logs from these ephemeral resources, you can now easily create custom metrics without having to 
 instrument or maintain separate code, while gaining powerful analytical capabilities on your log data.

No setup is required to use the embedded metric format. Either structure your logs by following the 
 [Embedded metric format specification](CloudWatch_Embedded_Metric_Format_Specification.md "CloudWatch_Embedded_Metric_Format_Specification.md"), or generate 
 them using our client libraries and send them to CloudWatch Logs using the 
 [PutLogEvents API](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html "https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html") or 
 the [CloudWatch agent](CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent.md "CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent.md").

 

To generate metrics from logs with embedded metric format, you need the `logs:PutLogEvents` permission but you don't need to also have the `cloudwatch:PutMetricData` permission.

Charges are incurred for logs ingestion and archival, and custom metrics that are generated. For more information, see [Amazon CloudWatch
 Pricing](http://aws.amazon.com/cloudwatch/pricing "http://aws.amazon.com/cloudwatch/pricing").

###### Note

Be careful when configuring your metric extraction as it impacts your custom metric usage and corresponding bill. 
 If you unintentionally create metrics based on high-cardinality dimensions (such as `requestId`), the embedded metric format will by design create 
 a custom metric corresponding to each unique dimension combination. For more information, see [Dimensions](cloudwatch_concepts.md#Dimension "cloudwatch_concepts.md#Dimension").


 The following topics describe how to publish logs using the embedded metric format, view your metrics and logs in the console, and set alarms on metrics created with the embedded metric format.
 

###### Topics

* [Publishing logs with the embedded metric format](CloudWatch_Embedded_Metric_Format_Generation.md "CloudWatch_Embedded_Metric_Format_Generation.md")
* [Viewing your metrics and logs in the console](CloudWatch_Embedded_Metric_Format_View.md "CloudWatch_Embedded_Metric_Format_View.md")
* [Setting alarms on metrics created with the embedded metric format](CloudWatch_Embedded_Metric_Format_Alarms.md "CloudWatch_Embedded_Metric_Format_Alarms.md")
