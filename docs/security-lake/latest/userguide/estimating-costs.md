# How Security Lake pricing is determined

Amazon Security Lake pricing is based on two dimensions: data ingestion and data conversion. Security Lake also works with other
AWS services to store and share your data, and you may incur separate charges for these activities.

When you turn on log collection for the first time in an AWS account in any AWS Region that Security Lake
supports, that account is automatically enrolled in a 15-day free trial of Security Lake. You may still incur charges
from other services during the free trial.

###### Note

When you continue using Security Lake after the 15-day free trial ends, you will automatically start incurring usage costs.
To prevent incurring charges after the
free trial ends, you must disable Security Lake.

To understand the methodology behind Security Lake pricing, watch the following video:

**Data ingestion**
These costs derive from the volume of ingested AWS CloudTrail logs and other AWS service logs and events
(Amazon Route 53 resolver query logs, AWS Security Hub findings, and Amazon VPC Flow Logs).

**Data conversion**
These costs derive from the volume of AWS service logs and events that Security Lake normalizes to
[Open Cybersecurity Schema Framework (OCSF) in Security Lake](open-cybersecurity-schema-framework.md "open-cybersecurity-schema-framework.md") schema and converts to Apache Parquet format.

**Costs of related services**
Here are some costs you may incur from other AWS services for storing and sharing the data in your security data lake:

- Amazon S3 – These costs derive from maintaining Amazon S3 buckets in your Security Lake account, storing your data there, and evaluating and monitoring your bucket for security and
  access control. For more information, see [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/").
- Amazon SQS – These costs derive from creating an Amazon SQS queue for message delivery. For more information, see [Amazon SQS pricing](https://aws.amazon.com/sqs/pricing/ "https://aws.amazon.com/sqs/pricing/").
- Amazon EventBridge – These costs derive from Amazon EventBridge sending object notifications to
  subscription endpoints. For more information, see [Amazon EventBridge
  pricing](https://aws.amazon.com/eventbridge/pricing/ "https://aws.amazon.com/eventbridge/pricing/").
- AWS Glue – Monthly costs are determined by the volume of log and event data ingested from AWS services per gigabyte. Your data is stored in Amazon Simple Storage Service and standard Amazon S3 charges apply. Security Lake also orchestrates other AWS services on your behalf. You will incur separate charges for AWS services used and resources set up as part of your security data lake. See pricing for [AWS Glue](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/"), [Amazon EventBridge](https://aws.amazon.com/eventbridge/pricing/ "https://aws.amazon.com/eventbridge/pricing/"), [AWS Lambda](https://aws.amazon.com/lambda/pricing/ "https://aws.amazon.com/lambda/pricing/"), [Amazon SQS](https://aws.amazon.com/sqs/pricing/ "https://aws.amazon.com/sqs/pricing/"), and [Amazon Simple Notification Service](https://aws.amazon.com/sns/pricing/ "https://aws.amazon.com/sns/pricing/"). You are responsible for costs that you incur by querying data from Security Lake and storing query results.

Costs that a subscriber incurs by querying data from Security Lake and storing query results are the responsibility of the subscriber.

For a full list of costs and ancillary services, see [Security Lake pricing](https://aws.amazon.com/security-lake/pricing/ "https://aws.amazon.com/security-lake/pricing/").
