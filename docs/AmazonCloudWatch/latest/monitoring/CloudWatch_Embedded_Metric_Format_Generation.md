

# Publishing logs with the embedded metric format
<a name="CloudWatch_Embedded_Metric_Format_Generation"></a>

 You can generate embedded metric format logs using the following methods: 
+  Generate and send the logs by using the [open-sourced client libraries](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Libraries.html). 
+  Manually generate the logs using the [embedded metric format specification](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html), and then use the [CloudWatch agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent.html) or the [PutLogEvents API](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html) to send the logs. 

 The following topics provide more information about embedded metrics. 

**Topics**
+ [Creating logs in embedded metric format using the client libraries](CloudWatch_Embedded_Metric_Format_Libraries.md)
+ [Specification: Embedded metric format](CloudWatch_Embedded_Metric_Format_Specification.md)
+ [Using the PutLogEvents API to send manually-created embedded metric format logs](CloudWatch_Embedded_Metric_Format_Generation_PutLogEvents.md)
+ [Using the CloudWatch agent to send embedded metric format logs](CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent.md)
+ [Using the embedded metric format with AWS Distro for OpenTelemetry](CloudWatch_Embedded_Metric_Format_OpenTelemetry.md)