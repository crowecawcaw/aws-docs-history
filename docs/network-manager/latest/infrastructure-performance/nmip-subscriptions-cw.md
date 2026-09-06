

# Amazon CloudWatch subscriptions for Infrastructure Performance
<a name="nmip-subscriptions-cw"></a>

Infrastructure Performance subscriptions publish network performance metrics in five-minute periods to Amazon CloudWatch for any pair of inter Regions, inter-Availability Zones, or intra-Availability Zones that you optionally subscribe to. Once a subscription is enabled, performance metrics continue to publish to CloudWatch for those pairs until you unsubscribe any pair that you no longer want to publish performance metrics for.

**Note**  
There's a separate CloudWatch metrics subscription charge for each inter-Region, inter-Availability Zone, or intra-Availability Zone pair you subscribe to. You won't be charged for any CloudWatch performance metrics that you unsubscribe from, or for any pair that you've not enabled subscriptions for. For more information about pricing guidelines, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

## Subscription metrics for CloudWatch
<a name="nmip-subscriptions-metrics"></a>

When subscriptions are enabled, you can use CloudWatch to view metrics. For more information on using CloudWatch for your Infrastructure Performance subscriptions, see [What is CloudWatch Management](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) in the *Amazon CloudWatch User Guide*.

 The following `EC2` namespace metric for Infrastructure Performance is tracked in CloudWatch:


| Metric | Description | 
| --- | --- | 
| AggregateAWSNetworkPerformance | The latency between Regions, inter-Availability Zones, or intra-Availability Zones. | 

**Topics**
+ [Manage CloudWatch subscriptions using the AWS Network Manager console](nmip-subscriptions-manage.md)
+ [Manage CloudWatch subscriptions using the AWS CLI](getting-started-nmip-cli.md)