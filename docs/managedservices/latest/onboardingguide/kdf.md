# Use AMS SSP to provision Amazon Data Firehose in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Data Firehose capabilities directly in your AMS managed account. Firehose is the easiest way to reliably load streaming data into data lakes, data stores, and analytics tools.
It can capture, transform, and load streaming data into Amazon S3,
Amazon Redshift, Amazon OpenSearch Service, and
[Splunk](https://aws.amazon.com/kinesis/data-firehose/splunk/ "https://aws.amazon.com/kinesis/data-firehose/splunk/"), enabling near real-time analytics with existing business intelligence
tools and dashboards you’re already using today. It is a fully managed service that automatically scales to match
the throughput of your data and requires no ongoing administration.
It can also batch, compress, transform, and encrypt the data before loading it, minimizing the amount of storage
used at the destination and increasing security.
To learn more, see
[What Is Amazon Data Firehose?](../../../firehose/latest/dev/what-is-this-service.md "../../../firehose/latest/dev/what-is-this-service.md")

## Firehose in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Amazon Data Firehose in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account:
`customer_kinesis_firehose_user_role`. After it's provisioned
in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Firehose in my AMS account?**

There are no restrictions. Full functionality of Amazon Data Firehose is available in your AMS account.

**Q: What are the prerequisites or dependencies to using Firehose in my AMS account?**

New service-linked IAM roles must be requested for each delivery stream.
You can also re-use a single service-linked role for all streams by updating
the role policy with the required resource permissions (including S3
buckets/ KMS Keys / Lambda Functions / Kinesis streams).

After you have submitted the RFC to add Firehose, an AMS
Operations engineer will reach out to you through a Service Request for the
ARNs of resources that you would like to connect with Data Firehose (for example, AWS KMS, S3, Lambda, and Kinesis Streams).
