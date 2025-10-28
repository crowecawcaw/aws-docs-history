# Monitoring sensitive data discovery jobs with

CloudWatch Logs

In addition to [monitoring the overall
status](discovery-jobs-status-check.md "discovery-jobs-status-check.md") of a sensitive data discovery job, you can monitor and analyze specific
events that occur as a job progresses. You can do this by using near real-time logging data
that Amazon Macie automatically publishes to Amazon CloudWatch Logs. The data in these logs provides a
record of changes to a job's progress or status. For example, you can use the data to
determine the exact date and time when a job started to run, was paused, or finished
running.

The log data also provides details about any account- or bucket-level errors that occur while
a job runs. For example, Macie logs an event if the permissions settings for an Amazon Simple Storage Service
(Amazon S3) bucket prevent a job from analyzing objects in the bucket. The event indicates when
the error occurred, and it identifies the affected bucket and the AWS account that owns
the bucket. The data for these types of events can help you identify, investigate, and
address errors that prevent Macie from analyzing the data that you want.

With Amazon CloudWatch Logs, you can monitor, store, and access log files from multiple systems,
applications, and AWS services, including Macie. You can also query and analyze log data,
and configure CloudWatch Logs to notify you when certain events occur or thresholds are met. CloudWatch Logs also
provides features for archiving log data and exporting the data to Amazon S3. To learn more about
CloudWatch Logs, see the [Amazon CloudWatch Logs User
Guide](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md").

###### Topics

- [How logging works
  for jobs](discovery-jobs-monitor-cw-logs-configure.md "discovery-jobs-monitor-cw-logs-configure.md")
- [Reviewing logs for
  jobs](discovery-jobs-monitor-cw-logs-review.md "discovery-jobs-monitor-cw-logs-review.md")
- [Understanding log
  events for jobs](discovery-jobs-monitor-cw-logs-ref.md "discovery-jobs-monitor-cw-logs-ref.md")
