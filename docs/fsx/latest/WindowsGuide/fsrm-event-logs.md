# Event Logs

When you enable FSRM on your file system, AWS FSx for Windows File Server generates event
logs for file management activities and sends them to the destination you configured (AWS
CloudWatch Logs or AWS Kinesis Data Firehose). These logs help you monitor FSRM operations,
troubleshoot issues, and maintain audit trails of file management activities.

## What FSRM logs

When you enable FSRM on your file system, AWS FSx for Windows File Server logs events
and sends them to your configured destination. The following events will be logged:

- File screening violations - When users attempt to save files that are monitored by
  file screens that have event notification actions
- Quota threshold notifications - When quota usage reaches configured thresholds
  that have event notification actions
- FSRM service events – Confirmation of notification settings, service errors, and
  operational failures

## Accessing FSRM logs

The location where you access FSRM logs depends on the destination you configured when
enabling FSRM:

CloudWatch Logs

View logs in the CloudWatch Logs console by navigating to the log group you
specified. You can search, filter, and analyze logs using CloudWatch Logs
Insights, and set up CloudWatch alarms to notify you of specific events.

Kinesis Data Firehose

Logs are delivered to the destination configured in your Kinesis Data Firehose
delivery stream, such as Amazon S3, AWS Redshift, or AWS OpenSearch Service. You
can process and analyze logs using the tools and services integrated with your
delivery stream.
