

# Publish flow logs to Amazon S3
<a name="flow-logs-s3"></a>

Flow logs can publish flow log data to Amazon S3. Amazon S3 (Simple Storage Service) is a highly scalable and durable object storage service. It is designed to store and retrieve any amount of data, from anywhere on the web. S3 offers industry-leading durability and availability, with built-in features for data versioning, encryption, and access control.

When publishing to Amazon S3, flow log data is published to an existing Amazon S3 bucket that you specify. Flow log records for all of the monitored network interfaces are published to a series of log file objects that are stored in the bucket. If the flow log captures data for a VPC, the flow log publishes flow log records for all of the network interfaces in the selected VPC.

To create an Amazon S3 bucket for use with flow logs, see [Create a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the *Amazon S3 User Guide*.

For more information about how to streamline VPC flow log ingestion, flow log processing, and flow log visualization, see [Centralized Logging with OpenSearch](https://aws.amazon.com/solutions/implementations/centralized-logging-with-opensearch/) in the AWS Solutions Library.

For more information about CloudWatch Logs, see [Logs sent to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html#AWS-logs-infrastructure-S3) in the *Amazon CloudWatch Logs User Guide*.

**Pricing**  
Data ingestion and archival charges for vended logs apply when you publish flow logs to Amazon S3. For more information, open [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/), select **Logs** and find **Vended Logs**.

**Topics**
+ [Flow log files](flow-logs-s3-path.md)
+ [Amazon S3 bucket permissions for flow logs](flow-logs-s3-permissions.md)
+ [Required key policy for use with SSE-KMS](flow-logs-s3-cmk-policy.md)
+ [Amazon S3 log file permissions](flow-logs-file-permissions.md)
+ [Create a flow log that publishes to Amazon S3](flow-logs-s3-create-flow-log.md)
+ [View flow log records with Amazon S3](view-flow-log-records-s3.md)