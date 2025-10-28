# Monitoring Amazon Transcribe

Monitoring is an important part of maintaining the reliability, availability, and performance of
Amazon Transcribe and your other AWS solutions. AWS provides the
following monitoring tools to watch Amazon Transcribe, report when something is wrong, and take
automatic actions when appropriate:

- **Amazon CloudWatch** monitors your AWS
  resources and the applications that you run on AWS in real time. You can collect
  and track metrics, create customized dashboards, and set alarms that notify you or take actions
  when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track CPU usage or other metrics on your Amazon EC2 instances and
  automatically launch new instances when needed.
- **Amazon CloudWatch Logs** can monitor, store, and access
  your log files from Amazon EC2 instances, CloudTrail, and other sources.
  CloudWatch Logs can monitor information in the log files and notify you when certain thresholds are
  met. You can also archive your log data in highly durable storage.
- **AWS CloudTrail** captures API calls and related events made by
  or on behalf of your AWS account and delivers the log files to an Amazon S3
  bucket that you specify. You can identify which users and accounts called AWS, the
  source IP address from which the calls were made, and when the calls occurred.
  For more information, see the _[Amazon CloudWatch User
  Guide](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")_.

**Amazon EventBridge** is a serverless service that uses
events to connect application components together, making it easier for you to build scalable
event-driven applications. EventBridge delivers a stream of real-time data from your own
applications, Software as a Service (SaaS) applications, and AWS services and
routes that data to targets such as Lambda. You can monitor events that
happen in services, and build event-driven architectures. For more information, see the
_[Amazon EventBridge User Guide](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")_.

###### Topics

- [Monitoring Amazon Transcribe with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Monitoring Amazon Transcribe
  with AWS CloudTrail](monitoring-transcribe-cloud-trail.md "monitoring-transcribe-cloud-trail.md")
- [Using Amazon EventBridge with Amazon Transcribe](monitoring-events.md "monitoring-events.md")
