# Use AMS SSP to provision Amazon Kinesis Data Streams in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Kinesis Data Streams (KDS) capabilities directly in your AMS managed account. Amazon Kinesis Data Streams is a highly scalable, and durable, real-time data streaming service. KDS can continuously capture gigabytes of data per second
from hundreds of thousands of sources such as website clickstreams, database event streams, financial transactions, social media feeds, IT logs, and
location-tracking events.
The data collected is available in milliseconds to enable real-time analytics use cases such as real-time dashboards, real-time anomaly detection, dynamic pricing, and more.
To learn more, see [Amazon Kinesis Data Streams](https://aws.amazon.com/kinesis/data-streams/ "https://aws.amazon.com/kinesis/data-streams/").

## Kinesis Data Streams in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Amazon Kinesis Data Streams in my AMS account?**

Request access to Amazon Kinesis Data Streams by submitting an RFC with the Management | AWS
service | Self-provisioned service | Add change type (ct-1w8z66n899dct).
This RFC provisions the following IAM role to your account:
`customer_kinesis_data_streaming_user_role`. After it's
provisioned in your account, you must onboard the role in your federation
solution.

**Q: What are the restrictions to using Amazon Kinesis Data Streams in my AMS account?**

There are no restrictions. Full functionality of Amazon Kinesis Data Streams is available in your AMS account.

**Q: What are the prerequisites or dependencies to using Amazon Kinesis Data Streams in my AMS
account?**

There are no prerequisites or dependencies to use Amazon Kinesis Data Streams in your AMS account.
