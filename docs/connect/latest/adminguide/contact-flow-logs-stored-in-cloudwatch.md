# Flow logs stored in an Amazon CloudWatch log group

Flow logs are stored in an Amazon CloudWatch log group, in the same AWS Region as your Amazon Connect instance. This log group is created
automatically when [Enable flow logging](contact-flow-logs.md#enable-contact-flow-logs "contact-flow-logs.md#enable-contact-flow-logs")
is turned on for your instance.

For example, the following image shows the CloudWatch log groups for two test
instances.

![The Amazon CloudWatch console, log groups, /aws/connect/mytest88 and mytest89.](images/cloudwatch-log-group.png)
A log entry added as each block in your flow is triggered. You can configure CloudWatch to send alerts when unexpected events occur during active flows.

**What happens if my log group is deleted?** You need to
manually re-create the CloudWatch log group. Otherwise, Amazon Connect won't
publish more logs.

## Pricing for flow logging

You are not charged for generating flow logs, but you are charged for using
CloudWatch for generating and storing the logs. Free tier customers are
charged only for usage that exceeds service quotas. For details about Amazon CloudWatch pricing, see [Amazon CloudWatch
Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").
