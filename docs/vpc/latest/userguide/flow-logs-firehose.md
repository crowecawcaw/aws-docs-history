# Publish flow logs to Amazon Data Firehose

Flow logs can publish flow log data directly to Amazon Data Firehose. Amazon Data Firehose is a fully
managed service that collects, transforms, and delivers real-time data streams into
various AWS data stores and analytics services. It handles the data ingestion on
your behalf.

When it comes to VPC flow logs, Firehose can be useful. VPC flow logs capture
information about the IP traffic going to and from network interfaces in your VPC. This
data can be crucial for security monitoring, performance analysis, and regulatory
compliance. However, managing the storage and processing of this continuous flow of log
data can be a complex and resource-intensive task.

By integrating Firehose with your VPC flow logs, you can deliver this data to your
preferred destination, such as Amazon S3 or Amazon Redshift. Firehose will scale to handle the ingestion, transformation, and delivery of
your VPC flow logs, relieving you of the operational burden. This allows you to focus on
analyzing the logs and deriving insights, rather than worrying about the underlying
infrastructure.

Additionally, Firehose offers features like data transformation, compression, and
encryption, which can enhance the efficiency and security of your VPC flow log
processing pipeline. Using Firehose for VPC flow logs can simplify your data management
and enable you to gain insights from your network traffic data.

When publishing to Amazon Data Firehose, flow log data is published to a Amazon Data Firehose delivery stream,
in plain text format.

###### Pricing

Standard ingestion and delivery charges apply. For more information, open [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"), select
**Logs** and find **Vended Logs**.

###### Contents

- [IAM roles for cross account delivery](firehose-cross-account-delivery.md "firehose-cross-account-delivery.md")
- [Create a flow log that publishes to Amazon Data Firehose](flow-logs-firehose-create-flow-log.md "flow-logs-firehose-create-flow-log.md")
