# Logging and monitoring in Amazon SES

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon SES and your AWS solutions. AWS provides tools to help you monitor Amazon SES
and respond to potential incidents.

- _Amazon CloudWatch_ monitors your AWS resources and the applications you run
  on AWS in real time. You can collect and track metrics, create customized dashboards, and
  set alarms that notify you or take actions when a specified metric reaches a threshold that
  you specify. For more information, see [Retrieving Amazon SES event data from
  CloudWatch](event-publishing-retrieving-cloudwatch.md "event-publishing-retrieving-cloudwatch.md") and [Creating reputation monitoring alarms
  using CloudWatch](reputationdashboard-cloudwatch-alarm.md "reputationdashboard-cloudwatch-alarm.md").
- _AWS CloudTrail_ captures API calls and related events made by or on behalf
  of your AWS account and delivers the log files to an Amazon S3 bucket that you specify. You can
  identify which users and accounts called AWS, the source IP address from which the calls
  were made, and when the calls occurred. For more information, see [Logging Amazon SES API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
- Amazon SES _email sending events_ can help you fine-tune your email
  sending strategy. Amazon SES captures detailed information, including the numbers of sends,
  deliveries, opens, clicks, bounces, complaints, and rejections. For more information, see
  [Monitoring sending
  activity](monitor-sending-activity.md "monitor-sending-activity.md").
- Amazon SES _reputation metrics_ tracks the bounce and complaint rates for
  your account. For more information, see [Monitoring sender
  reputation](monitor-sender-reputation.md "monitor-sender-reputation.md").
