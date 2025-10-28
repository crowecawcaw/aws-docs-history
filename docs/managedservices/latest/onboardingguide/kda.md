# Use AMS SSP to provision Amazon Managed Service for Apache Flink in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Managed Service for Apache Flink capabilities directly in your AMS managed account. Managed Service for Apache Flink is the easiest way to analyze streaming data, gain actionable insights, and
respond to your business and customer needs in real time.
Amazon Managed Service for Apache Flink reduces the complexity of building, managing, and integrating streaming applications with
other AWS services.
SQL users can easily query streaming data or build entire streaming applications using templates and an interactive SQL
editor. Java developers can quickly build sophisticated
streaming applications using open source Java libraries and AWS integrations to transform and analyze data in real time.
Amazon Managed Service for Apache Flink takes care of everything required to run your real-time applications continuously and scales
automatically to match the volume and throughput of your incoming data.
With Amazon Managed Service for Apache Flink, you only pay for the resources your streaming applications consume. There is no minimum
fee or setup cost.

To learn more, see [Amazon Managed Service for Apache Flink](https://aws.amazon.com/kinesis/data-analytics/ "https://aws.amazon.com/kinesis/data-analytics/").

## Managed Service for Apache Flink in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Amazon Managed Service for Apache Flink in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account: `customer_kinesis_analytics_application_role`. After it's
provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon Managed Service for Apache Flink in my AMS account?**

- Configurations are limited to resources without ‘AMS-‘ or ’MC-’ prefixes to prevent any
  modifications to AMS infrastructure.
- Permission to delete or create new Kinesis Data Streams or Firehose has been removed from the policy. We have
  another policy that allows that.

**Q: What are the prerequisites or dependencies to using Amazon Kinesis Data Streams in my AMS account?**

There are a few dependencies:

- Amazon Managed Service for Apache Flink requires that Kinesis Data Streams or Firehose must be created prior to configuring an application with Managed Service for Apache Flink.
- The resource-based policy permissions should indicate a particular input data source.
