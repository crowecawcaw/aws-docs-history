# Use AMS SSP to provision Amazon Managed Streaming for Apache Kafka in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Managed Streaming for Apache Kafka (Amazon MSK) capabilities directly in your AMS managed account. Amazon Managed Streaming for Apache Kafka is a fully managed AWS streaming data service makes it easy for you to build and
run applications that use Apache Kafka to process streaming data without needing to become
an expert in operating Apache Kafka clusters. Amazon MSK manages the provisioning, configuration,
and maintenance of Apache Kafka clusters and Apache ZooKeeper nodes for you. Amazon MSK also
shows key Apache Kafka performance metrics in the AWS Console.

Amazon MSK provides multiple levels of security for your Apache Kafka clusters, including VPC
network isolation, AWS IAM for control-plane API authorization, encryption at rest, TLS
encryption in-transit, TLS based certificate authentication, SASL/SCRAM authentication secured
by AWS Secrets Manager.
To learn more, see [Amazon MSK](https://aws.amazon.com/msk/ "https://aws.amazon.com/msk/").

## Amazon MSK in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request access to Amazon MSK in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the
following IAM policies and role to your account:

- `customer-msk-admin-policy.json`
- `AmazonMSKFullAccess`
- `customer-msk-admin-role.json`

Once provisioned in your account you must onboard the role in your federation
solution.

**Q: What are the restrictions to using Amazon MSK?**

For Amazon MSK to deliver broker logs to the destinations that you configure, ensure
that the `AmazonMSKFullAccess` policy is attached to your IAM role.
So full access permissions are already in place.

**Q: What are the prerequisites or dependencies to using Amazon MSK?**

Before creating your MSK cluster, you must have a VPC and subnets within that
VPC. By default, AMS has this covered as part of default
[AMS VPC creation](../../../msk/latest/developerguide/msk-create-cluster.md "../../../msk/latest/developerguide/msk-create-cluster.md").

To learn about the limitation of Amazon MSK, refer to
[Amazon MSK Limits](../../../msk/latest/developerguide/limits.md "../../../msk/latest/developerguide/limits.md").
