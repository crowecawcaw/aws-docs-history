This guide documents the new AWS Wickr administration console, released on
March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic
Administration Guide](../adminguide-classic/what-is-wickr.md "../adminguide-classic/what-is-wickr.md").

# Serverless data retention for AWS Wickr

AWS Wickr data retention can retain all conversations in your network, including direct
message conversations and conversations in Groups or Rooms between in-network (internal)
members and those with other teams (external) with whom your network is federated.
Serverless data retention is available only if you have an AWS Wickr Premium plan and opt in. It is not available for AWS Wickr Enterprise.

###### Note

Data retention service is currently only available in the following regions:
US East (N. Virginia), Canada (Central), Asia Pacific (Sydney),
Europe (Frankfurt), Europe (Stockholm), Asia Pacific (Tokyo),
Asia Pacific (Singapore), Europe (Zurich), AWS GovCloud (US-West).

###### Note

AWS does not support configuring Wickr data retention bot using [Wickr Admin SDK](https://us-west-2.console.aws.amazon.com/servicecatalog/home?region=us-west-2#portfolios?activeTab=importedAdminPortfolios "https://us-west-2.console.aws.amazon.com/servicecatalog/home?region=us-west-2#portfolios?activeTab=importedAdminPortfolios"). The configuration has to be performed using the AWS
console.

The serverless data retention service provides a cloud-native alternative to the
traditional Docker container-based data retention bot. This new method offers simplified
deployment, managed infrastructure, automatic scaling, and comprehensive monitoring with
reasonable tradeoffs related to Wickr's end-to-end encryption (E2EE) model.

**Key Benefits of Serverless Method**

- **Simplified Deployment**: Console-guided setup with minimal
  configuration steps, completed in minutes rather than hours
- **Managed Infrastructure**: No need to provision or maintain EC2
  instances, Docker containers, or monitor bot health
- **Automatic Scaling**: Dynamically handles message volume
  fluctuations without manual intervention
- **Enhanced Monitoring**: Pre-configured CloudWatch dashboards,
  metrics, and configurable alerting
- **Improved Reliability**: Fault-tolerant message delivery with
  automatic recovery
  **How It Works**

When you enable the serverless data retention service, all messages and files shared in
your network are retained in accordance with your organization's compliance policies. The
service uses AWS Nitro Enclaves to Wickr decrypt message content and then uses Customer
Managed KMS keys to reencrypt content for transit to your S3 bucket. You can
then decrypt messages on demand to access encrypted content.

###### Note

Wickr never accesses your messages and files. All decryption occurs within secure
Nitro Enclaves using your KMS keys, and decrypted content is stored only in your AWS
account.

## Prerequisites

Before enabling serverless data retention, ensure you have the following:

- **AWS Wickr Premium Plan**: Data retention is only
  available to premium plan subscribers
- **AWS Account**: An active AWS account with appropriate
  permissions on KMS and S3.
- **IAM Permissions**: Ability to import Service Catalog
  portfolios and deploy CloudFormation templates

###### Topics

- [Configure serverless method](configure-serverless-method.md "configure-serverless-method.md")
- [Architecture Overview](architecture.md "architecture.md")
- [Access retained data](retained-data.md "retained-data.md")
- [Monitoring and management](monitor-manage.md "monitor-manage.md")
- [Migration from docker method](migration-process.md "migration-process.md")
- [Security considerations](considerations-security.md "considerations-security.md")
- [Best practices](best-practices.md "best-practices.md")
