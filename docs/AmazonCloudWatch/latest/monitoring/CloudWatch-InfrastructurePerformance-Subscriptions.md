

# CloudWatch subscriptions

Infrastructure Performance subscriptions publish network performance metrics to Amazon CloudWatch in five-minute periods for each inter-Region, inter-Availability Zone, or intra-Availability Zone pair that you subscribe to. The subscription continues publishing metrics until you unsubscribe from the pair.

**Note**  
There's a separate CloudWatch metrics subscription charge for each inter-Region, inter-Availability Zone, or intra-Availability Zone pair you subscribe to. You won't be charged for any CloudWatch performance metrics that you unsubscribe from, or for any pair that you haven't subscribed to. For more information about pricing guidelines, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

**Manage Infrastructure Performance tasks**
+ [Manage subscriptions using the console](CloudWatch-InfrastructurePerformance-Subscriptions-Console.md)
+ [Manage subscriptions using the AWS CLI](CloudWatch-InfrastructurePerformance-Subscriptions-CLI.md)

## Subscription metrics for CloudWatch
<a name="CloudWatch-InfrastructurePerformance-Subscriptions-Metrics"></a>

When subscriptions are enabled, you can use CloudWatch to view metrics. For more information about using CloudWatch for your Infrastructure Performance subscriptions, see [What is Amazon CloudWatch?](WhatIsCloudWatch.md).

The following Amazon EC2 namespace metric for Infrastructure Performance is tracked in CloudWatch:


| Metric | Description | 
| --- | --- | 
| AggregateAWSNetworkPerformance | The latency between Regions, inter-Availability Zones, or intra-Availability Zones. | 