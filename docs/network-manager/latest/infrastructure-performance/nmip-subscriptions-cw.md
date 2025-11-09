# Amazon CloudWatch subscriptions for Infrastructure Performance

Infrastructure Performance subscriptions publish network performance metrics in five-minute periods to Amazon CloudWatch for any pair of inter Regions, inter-Availability Zones, or intra-Availability Zones that you optionally subscribe to. Once a subscription is enabled, performance metrics continue to publish to CloudWatch for those pairs until you unsubscribe any pair that you no longer want to publish performance metrics for.

###### Note

There's a separate CloudWatch metrics subscription charge for each inter-Region,
inter-Availability Zone, or intra-Availability Zone pair you subscribe to. You won't be charged
for any CloudWatch performance metrics that you unsubscribe from, or for any pair that you've not
enabled subscriptions for. For more information about pricing guidelines, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

## Subscription metrics for CloudWatch

When subscriptions are enabled, you can use CloudWatch to view metrics. For more information on
using CloudWatch for your Infrastructure Performance subscriptions, see [What is CloudWatch Management](../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.md")
in the _Amazon CloudWatch User Guide_.

The following `EC2` namespace metric for Infrastructure Performance is tracked in
CloudWatch:

| Metric                         | Description                                                                               |
| ------------------------------ | ----------------------------------------------------------------------------------------- |
| AggregateAWSNetworkPerformance | The latency between Regions, inter-Availability Zones, or<br>intra-Availability<br>Zones. |

###### Manage Infrastructure Performance tasks

- [Manage CloudWatch subscriptions using the AWS Network Manager
  console](nmip-subscriptions-manage.md "nmip-subscriptions-manage.md")
- [Manage CloudWatch subscriptions using the AWS CLI](getting-started-nmip-cli.md "getting-started-nmip-cli.md")
