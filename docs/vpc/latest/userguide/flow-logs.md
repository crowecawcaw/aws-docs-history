

# Logging IP traffic using VPC Flow Logs
<a name="flow-logs"></a>

VPC Flow Logs is a feature that enables you to capture information about the IP traffic going to and from network interfaces in your VPC. Flow log data can be published to the following locations: Amazon CloudWatch Logs, Amazon S3, or Amazon Data Firehose. The configured delivery path and permissions that enable network traffic logs to be sent to a destination like CloudWatch Logs or S3 are referred to as *subscriptions*. After you create a flow log, you can retrieve and view the flow log records in the log group, bucket, or delivery stream that you configured.

Flow logs can help you with a number of tasks, such as:
+ Diagnosing overly restrictive security group rules
+ Monitoring the traffic that is reaching your instance
+ Determining the direction of the traffic to and from the network interfaces

Flow log data is collected outside of the path of your network traffic, and therefore does not affect network throughput or latency. You can create or delete flow logs without any risk of impact to network performance.

**Note**  
This section only talks about flow logs for VPCs. For information about flow logs for transit gateways introduced in version 6, see [Logging network traffic using Transit Gateway Flow Logs](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-flow-logs.html) in the *Amazon VPC Transit Gateways User Guide*.

**Topics**
+ [Flow logs basics](flow-logs-basics.md)
+ [Flow log records](flow-log-records.md)
+ [Flow log record examples](flow-logs-records-examples.md)
+ [Flow log limitations](flow-logs-limitations.md)
+ [Pricing](#flow-logs-pricing)
+ [Work with flow logs](working-with-flow-logs.md)
+ [Publish flow logs to CloudWatch Logs](flow-logs-cwl.md)
+ [Publish flow logs to Amazon S3](flow-logs-s3.md)
+ [Publish flow logs to Amazon Data Firehose](flow-logs-firehose.md)
+ [Query flow logs using Amazon Athena](flow-logs-athena.md)
+ [Identity and access management in VPC Flow Logs](flow-logs-iam.md)
+ [Troubleshoot VPC Flow Logs](flow-logs-troubleshooting.md)

## Pricing
<a name="flow-logs-pricing"></a>

Data ingestion and archival charges for vended logs apply when you publish flow logs. For more information about pricing when publishing vended logs, open [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/), select **Logs** and find **Vended Logs**.

To track charges from publishing flow logs, you can apply cost allocation tags to your destination resource. Thereafter, your AWS cost allocation report includes usage and costs aggregated by these tags. You can apply tags that represent business categories (such as cost centers, application names, or owners) to organize your costs. For more information, see the following:
+ [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html) in the *AWS Billing User Guide*
+ [Tag log groups in Amazon CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#log-group-tagging) in the *Amazon CloudWatch Logs User Guide*
+ [Using cost allocation S3 bucket tags](https://docs.aws.amazon.com/AmazonS3/latest/userguide/CostAllocTagging.html) in the *Amazon Simple Storage Service User Guide*
+ [Tagging Your Delivery Streams](https://docs.aws.amazon.com/firehose/latest/dev/firehose-tagging.html) in the *Amazon Data Firehose Developer Guide*