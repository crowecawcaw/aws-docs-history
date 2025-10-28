# Best practice 5.3 – Monitor the infrastructure changes and the user activities against the infrastructure

As the infrastructure changes over time, you should monitor
what has been changed by whom. This is to ensure that such
changes are deliberate and the infrastructure is still
protected.

## Suggestion 5.3.1 – Monitor the infrastructure changes

You want to know every infrastructure change and want to
know that such changes are deliberate. Monitor the
infrastructure changes using available methods on your
team. For example, you can implement an operation
procedure to review the infrastructure configurations every
quarter of the year. Or, you can use AWS services that
assist you to monitor the infrastructure changes with less
effort.

For more details, refer to the following documentation:

- AWS Config Developer Guide:
  [What
  Is AWS Config?](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md")
- Amazon Inspector User Guide:
  [What
  is Amazon Inspector?](../../../inspector/latest/userguide/inspector_introduction.md "../../../inspector/latest/userguide/inspector_introduction.md")
- Amazon GuardDuty User Guide:
  [Amazon S3 protection in Amazon GuardDuty](../../../guardduty/latest/ug/s3_detection.md "../../../guardduty/latest/ug/s3_detection.md")

## Suggestion 5.3.2 – Monitor the user activities against the infrastructure

You want to know who is changing the infrastructure and
when, so that you can see that any given infrastructure
change is performed by an authorized person or system. To
do so, as examples, you can implement an operation
procedure to review the AWS CloudTrail audit logs every
quarter of the year. Or you can implement near real time
trend analysis using AWS services such as Amazon CloudWatch Logs Insights.

For more details, refer to the following information:

- AWS CloudTrail User Guide:
  [Monitoring
  CloudTrail Log Files with Amazon CloudWatch Logs](../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md "../../../awscloudtrail/latest/userguide/monitor-cloudtrail-log-files-with-cloudwatch-logs.md")
- AWS Management and Governance Blog:
  [Analyzing
  AWS CloudTrail in Amazon CloudWatch](https://aws.amazon.com/blogs/mt/analyzing-cloudtrail-in-cloudwatch/ "https://aws.amazon.com/blogs/mt/analyzing-cloudtrail-in-cloudwatch/")
