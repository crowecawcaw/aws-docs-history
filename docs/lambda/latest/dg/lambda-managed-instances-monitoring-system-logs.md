

# Capacity provider system logs for Lambda Managed Instances
<a name="lambda-managed-instances-monitoring-system-logs"></a>

To help you monitor and troubleshoot your Lambda Managed Instances environment, Lambda automatically generates system logs for your capacity providers. You can view logs for capacity providers using the Lambda console, the CloudWatch console, the AWS Command Line Interface (AWS CLI), or the CloudWatch API. You can also route logs to Amazon S3 and Firehose using CloudWatch Logs subscription filters.

As long as your capacity provider's [operator role](lambda-managed-instances-operator-role.md) has the necessary permissions, Lambda captures system logs and sends them to Amazon CloudWatch Logs, which is the default destination.

**Note**  
Capacity provider system logs are enabled by default. Lambda sends system logs to CloudWatch Logs automatically when you create a capacity provider.
+ **CloudWatch Logs** is the default logging destination for capacity provider system logs. CloudWatch Logs provides real-time log viewing and analysis capabilities, with support for creating metrics and alarms based on your log data.
+ **Amazon S3** is economical for long-term storage, and services like Athena can be used to analyze logs. Latency is typically higher.
+ **Firehose** offers managed streaming of logs to various destinations. If you need to send logs to other AWS services (for example, OpenSearch Service or Redshift Data API) or third-party platforms (like Datadog, New Relic, or Splunk), Firehose simplifies that process by providing pre-built integrations.

## Configuring log destinations
<a name="lambda-managed-instances-system-logs-configuring-destinations"></a>

Lambda supports multiple destinations for your capacity provider system logs. Regardless of your chosen destination, Lambda provides options to control log filtering and delivery.

Capacity provider system logs use JSON structured format exclusively. JSON structured logs provide enhanced searchability and enable automated analysis. You can control which logs Lambda sends to your chosen destination by configuring the system log level. Filtering helps you manage storage costs and makes it easier to find relevant log entries during debugging.

For more information about setting up each destination, see the following topics:
+ [Sending capacity provider system logs to CloudWatch Logs](lambda-managed-instances-monitoring-cwl.md)
+ [Sending capacity provider system logs to Firehose](lambda-managed-instances-monitoring-firehose.md)
+ [Sending capacity provider system logs to Amazon S3](lambda-managed-instances-monitoring-s3.md)

## Configuring logging controls for capacity providers
<a name="lambda-managed-instances-system-logs-configuring-controls"></a>

To give you more control over how your capacity provider system logs are captured, processed, and consumed, Lambda offers the following logging configuration options:
+ **Log level** — choose the detail level of system logs Lambda sends to CloudWatch Logs: `DEBUG`, `INFO`, or `WARN`.
+ **Log group** — choose the CloudWatch Logs log group your capacity provider sends logs to.

For more information about configuring logging controls, see the following topics:
+ [Log-level filtering for capacity provider system logs](lambda-managed-instances-monitoring-log-levels.md)
+ [Capacity provider system log format](lambda-managed-instances-monitoring-log-format.md)
+ [Capacity provider system log event reference](lambda-managed-instances-monitoring-system-log-events.md)