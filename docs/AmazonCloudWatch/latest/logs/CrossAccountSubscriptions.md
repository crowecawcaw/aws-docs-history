# Cross-account cross-Region

subscriptions

You can collaborate with an owner of a different AWS account and receive their log
events on your AWS resources, such as an Amazon Kinesis or Amazon Data Firehose stream (this is known
as cross-account data sharing). For example, this log event data can be read from a
centralized Kinesis Data Streams or Firehose stream to perform custom processing and analysis. Custom
processing is especially useful when you collaborate and analyze data across many
accounts.

For example, a company's information security group might want to analyze data for
real-time intrusion detection or anomalous behaviors so it could conduct an audit of
accounts in all divisions in the company by collecting their federated production logs
for central processing. A real-time stream of event data across those accounts can be
assembled and delivered to the information security groups, who can use Kinesis Data Streams to attach
the data to their existing security analytic systems.

###### Note

The log group and the destination must be in the same AWS Region. However, the
AWS resource that the destination points to can be located in a different Region.
In the examples in the following sections, all Region-specific resources are created
in US East (N. Virginia)).

If you have configured AWS Organizations and are working with member accounts you can use log
centralization to collect log data from source accounts into a central monitoring
account.

When working with centralized log groups you can use these system fields dimensions
when creating subscription filters:

- `@aws.account` - This dimension represents the AWS account ID
  from which the log event originated.
- `@aws.region` - This dimension represents the AWS region where
  the log event was generated.
  These dimensions help in identifying the source of log data, allowing for more
  granular filtering and analysis of metrics derived from centralized logs.

###### Topics

- [Cross-account cross-Region log
  data sharing using Kinesis Data Streams](CrossAccountSubscriptions-Kinesis.md "CrossAccountSubscriptions-Kinesis.md")
- [Cross-account cross-Region log
  data sharing using Firehose](CrossAccountSubscriptions-Firehose.md "CrossAccountSubscriptions-Firehose.md")
- [Cross-account
  cross-Region account-level subscriptions using Kinesis Data Streams](CrossAccountSubscriptions-Kinesis-Account.md "CrossAccountSubscriptions-Kinesis-Account.md")
- [Cross-account
  cross-Region account-level subscriptions using Firehose](CrossAccountSubscriptions-Firehose-Account.md "CrossAccountSubscriptions-Firehose-Account.md")
