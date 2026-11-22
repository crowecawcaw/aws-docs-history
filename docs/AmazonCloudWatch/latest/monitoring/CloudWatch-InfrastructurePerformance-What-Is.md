

# What is Infrastructure Performance?

Infrastructure Performance, a feature of Performance Monitor, provides near real-time and historical network latency across AWS Regions and across or within Availability Zones for a specified time period. Performance metrics are aggregated according to a time period that you choose. Network performance results are returned for that time period, showing whether the performance was healthy or if there was any performance degradation. This helps you evaluate whether network performance might affect your applications. Infrastructure Performance can also publish metrics to Amazon CloudWatch through subscriptions, so that you can view performance metrics in CloudWatch. Infrastructure Performance is available at no additional charge. However, if you use subscriptions to view performance in CloudWatch, additional charges apply. For more information about CloudWatch pricing guidelines, see [Amazon CloudWatch pricing](https://aws.amazon.com/cloudwatch/pricing/).

**Note**  
Infrastructure Performance is designed to give you an overview showing whether network performance is normal or degraded. It doesn't provide details about the specific causes of degradation, such as a hardware failure.

Infrastructure Performance works in the following geographical areas:
+ **Availability Zones**: Generate network performance metrics between two Availability Zones or within a single Availability Zone.
+ **Regions**: Generate network performance metrics to see performance between two Regions.

You can use the Region metrics to evaluate a Region expansion strategy. Infrastructure Performance can help you gather information needed to understand network performance between Regions where you currently have a presence, and Regions that you're considering. For example, you might have a presence in us-west-2 and are looking to expand into eu-central-1. Use Infrastructure Performance to check the latency between these two Regions to help you make a more informed choice for Region expansion. For a list of the Regions that support Infrastructure Performance, see [Region availability](CloudWatch-InfrastructurePerformance-How-It-Works.md#CloudWatch-InfrastructurePerformance-Regions).

**Note**  
Infrastructure Performance doesn't incorporate performance metrics for paths through Amazon VPC networking resources, such as transit gateways, NAT gateways, Amazon VPC endpoints, Elastic Load Balancing, or Amazon EC2 network interfaces.

**Topics**
+ [How Infrastructure Performance works](CloudWatch-InfrastructurePerformance-How-It-Works.md)