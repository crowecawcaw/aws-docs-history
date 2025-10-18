# Monitoring AWS Deadline Cloud

Monitoring is an important part of maintaining the reliability, availability, and
 performance of AWS Deadline Cloud (Deadline Cloud) and your AWS solutions. Collect monitoring data from all of
 the parts of your AWS solution so that you can more easily debug a multi-point failure if one
 occurs. Before you start monitoring Deadline Cloud, you should create a monitoring plan that includes
 answers to the following questions:


* What are your monitoring goals?
* Which resources will you monitor?
* How often will you monitor these resources?
* Which monitoring tools will you use?
* Who will perform the monitoring tasks?
* Who should be notified when something goes wrong?
AWS and Deadline Cloud provide tools that you can use to monitor your resources and respond to
 potential incidents. Some of these tools do the monitoring for you, some of the tools require
 manual intervention. You should automate monitoring tasks as much as possible.


* *Amazon CloudWatch* monitors your AWS resources and the applications you run
 on AWS in real time. You can collect and track metrics, create customized dashboards, and
 set alarms that notify you or take actions when a specified metric reaches a threshold that
 you specify. For example, you can have CloudWatch track CPU usage or other metrics of your Amazon EC2
 instances and automatically launch new instances when needed. For more information, see the
 [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").


Deadline Cloud has three CloudWatch metrics.
* *Amazon CloudWatch Logs* enables you to monitor, store, and access your log files
 from Amazon EC2 instances, CloudTrail, and other sources. CloudWatch Logs can monitor information in the log
 files and notify you when certain thresholds are met. You can also archive your log data in
 highly durable storage. For more information, see the [Amazon CloudWatch Logs User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/ "https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/").
* *Amazon EventBridge* can be used to automate your AWS services and respond
 automatically to system events, such as application availability issues or resource changes.
 Events from AWS services are delivered to EventBridge in near real time. You can write simple
 rules to indicate which events are of interest to you and which automated actions to take
 when an event matches a rule. For more information, see [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/ "https://docs.aws.amazon.com/eventbridge/latest/userguide/").
* *AWS CloudTrail* captures API calls and related events made by or on behalf
 of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
 identify which users and accounts called AWS, the source IP address from which the calls
 were made, and when the calls occurred. For more information, see the [AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").
###### Topics

* [Logging Deadline Cloud API calls using
 AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
* [Monitoring with CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
* [Managing Deadline Cloud events using Amazon EventBridge](eventbridge-integration.md "eventbridge-integration.md")
