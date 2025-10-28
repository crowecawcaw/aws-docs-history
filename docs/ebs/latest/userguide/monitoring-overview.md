# Monitoring tools for Amazon EBS

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon Elastic Block Store and your other AWS solutions. AWS provides the following monitoring
tools to watch Amazon EBS, report when something is wrong, and take automatic actions when
appropriate:

- **AWS CloudTrail** captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. The APIs to manage your EBS volumes and snapshots are
  part of the Amazon EC2 API. For more information about CloudTrail and the Amazon EC2 API, see
  [Log Amazon EC2 API calls using AWS CloudTrail](../../../AWSEC2/latest/UserGuide/monitor-with-cloudtrail.md "../../../AWSEC2/latest/UserGuide/monitor-with-cloudtrail.md") in the _Amazon EC2 User Guide_.
- **Amazon CloudWatch** monitors your AWS resources and the applications you
  run on AWS in real time. You can collect and track metrics, create customized dashboards,
  and set alarms that notify you or take actions when a specified metric reaches a threshold
  that you specify. For example, you can have CloudWatch track CPU usage or other metrics of your
  Amazon EC2 instances and automatically launch new instances when needed. For more information,
  see [Amazon CloudWatch metrics for Amazon EBS](using_cloudwatch_ebs.md "using_cloudwatch_ebs.md").
- **Amazon EventBridge** can be used to automate your AWS services
  and respond automatically to system events, such as application availability issues or
  resource changes. Events from AWS services are delivered to EventBridge in near real time. You
  can write simple rules to indicate which events are of interest to you and which automated
  actions to take when an event matches a rule. For more information, see
  [Amazon EventBridge events for Amazon EBS](ebs-cloud-watch-events.md "ebs-cloud-watch-events.md").
- **Amazon EBS detailed performance statistics** provide
  real-time I/O performance statistics for Amazon EBS volumes attached to Nitro-based Amazon EC2
  instances. For more information, [Amazon EBS detailed performance statistics](nvme-detailed-performance-stats.md "nvme-detailed-performance-stats.md").
- **Amazon GuardDuty** helps detect potentially malicious activity in
  your EC2 instances. GuardDuty Malware Protection for EC2 scans the EBS volumes attached to your
  EC2 instances. For more information, see [Amazon GuardDuty for Amazon EBS](monitoring-guardduty.md "monitoring-guardduty.md").
