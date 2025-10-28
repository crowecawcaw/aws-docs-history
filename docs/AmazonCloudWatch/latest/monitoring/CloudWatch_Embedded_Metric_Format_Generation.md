# Publishing logs with the embedded metric format

You can generate embedded metric format logs using the following methods:

- Generate and send the logs by using the [open-sourced client libraries](CloudWatch_Embedded_Metric_Format_Libraries.md "CloudWatch_Embedded_Metric_Format_Libraries.md").
- Manually generate the logs using the [embedded metric format specification](CloudWatch_Embedded_Metric_Format_Specification.md "CloudWatch_Embedded_Metric_Format_Specification.md"), and then use the [CloudWatch agent](CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent.md "CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent.md") or the [PutLogEvents API](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md") to send the logs.

The following topics provide more information about embedded metrics.

###### Topics

- [Creating logs in embedded metric format using the client libraries](CloudWatch_Embedded_Metric_Format_Libraries.md "CloudWatch_Embedded_Metric_Format_Libraries.md")
- [Specification: Embedded metric format](CloudWatch_Embedded_Metric_Format_Specification.md "CloudWatch_Embedded_Metric_Format_Specification.md")
- [Using the PutLogEvents API to send manually-created embedded metric format logs](CloudWatch_Embedded_Metric_Format_Generation_PutLogEvents.md "CloudWatch_Embedded_Metric_Format_Generation_PutLogEvents.md")
- [Using the CloudWatch agent to send embedded metric format logs](CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent.md "CloudWatch_Embedded_Metric_Format_Generation_CloudWatch_Agent.md")
- [Using the embedded metric format with AWS Distro for OpenTelemetry](CloudWatch_Embedded_Metric_Format_OpenTelemetry.md "CloudWatch_Embedded_Metric_Format_OpenTelemetry.md")
