# DynamoDB preventative security best practices

The following best practices can help you anticipate and prevent security incidents in
Amazon DynamoDB.

**Encryption at rest**

DynamoDB encrypts at rest all user data stored in tables, indexes, streams,
and backups using encryption keys stored in [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/ "https://aws.amazon.com/kms/"). This provides an
additional layer of data protection by securing your data from unauthorized
access to the underlying storage .

You can specify whether DynamoDB should use an AWS owned key (default
encryption type), an AWS managed key, or a customer managed key to encrypt user
data. For more information, see [Amazon DynamoDB Encryption at Rest](EncryptionAtRest.md "EncryptionAtRest.md").

**Use IAM roles to authenticate access to DynamoDB**

For users, applications, and other AWS services to access DynamoDB, they
must include valid AWS credentials in their AWS API requests. You should
not store AWS credentials directly in the application or EC2 instance.
These are long-term credentials that are not automatically rotated, and
therefore could have significant business impact if they are compromised. An
IAM role enables you to obtain temporary access keys that can be used to
access AWS services and resources.

For more information, see [Identity and Access Management for Amazon DynamoDB](security-iam.md "security-iam.md").

**Use IAM policies for DynamoDB base authorization**

When granting permissions, you decide who is getting them, which DynamoDB
APIs they are getting permissions for, and the specific actions you want to
allow on those resources. Implementing least privilege is key in reducing
security risk and the impact that can result from errors or malicious
intent.

Attach permissions policies to IAM identities (that is, users, groups,
and roles) and thereby grant permissions to perform operations on DynamoDB
resources.

You can do this by using the following:

- [AWS Managed (predefined) policies](using-identity-based-policies.md#access-policy-examples-aws-managed "using-identity-based-policies.md#access-policy-examples-aws-managed")
- [Customer managed policies](using-identity-based-policies.md#access-policy-examples-for-sdk-cli "using-identity-based-policies.md#access-policy-examples-for-sdk-cli")

**Use IAM policy conditions for fine-grained access control**

When you grant permissions in DynamoDB, you can specify conditions that
determine how a permissions policy takes effect. Implementing least
privilege is key in reducing security risk and the impact that can result
from errors or malicious intent.

You can specify conditions when granting permissions using an IAM
policy. For example, you can do the following:

- Grant permissions to allow users read-only access to certain items
  and attributes in a table or a secondary index.
- Grant permissions to allow users write-only access to certain
  attributes in a table, based upon the identity of that user.

For more information, see [Using IAM Policy Conditions for Fine-Grained Access
Control](specifying-conditions.md "specifying-conditions.md").

**Use a VPC endpoint and policies to access DynamoDB**

If you only require access to DynamoDB from within a virtual private cloud
(VPC), you should use a VPC endpoint to limit access from only the required
VPC. Doing this prevents that traffic from traversing the open internet and
being subject to that environment.

Using a VPC endpoint for DynamoDB allows you to control and limit access
using the following:

- VPC endpoint policies – These policies are applied on the
  DynamoDB VPC endpoint. They allow you to control and limit API access
  to the DynamoDB table.
- IAM policies – By using the `aws:sourceVpce`
  condition on policies attached to users, groups, or roles, you can
  enforce that all access to the DynamoDB table is via the specified VPC
  endpoint.

For more information, see [Endpoints for Amazon
DynamoDB](../../../vpc/latest/userguide/vpc-endpoints-ddb.md "../../../vpc/latest/userguide/vpc-endpoints-ddb.md").

**Consider client-side encryption**

We recommend that you plan your encryption strategy before implementing
your table in DynamoDB. If you store sensitive or confidential data in DynamoDB,
consider including client-side encryption in your plan. This way you can
encrypt data as close as possible to its origin, and ensure its protection
throughout its lifecycle. Encrypting your sensitive data in transit and at
rest helps ensure that your plaintext data isn’t available to any third
party.

The [AWS Database Encryption SDK for DynamoDB](../../../dynamodb-encryption-client/latest/devguide/what-is-ddb-encrypt.md "../../../dynamodb-encryption-client/latest/devguide/what-is-ddb-encrypt.md") is a software library
that helps you protect your table data before you send it to DynamoDB. It
encrypts, signs, verifies, and decrypts your DynamoDB table items. You control
which attributes are encrypted and signed.

**Primary Key considerations**

Do not use sensitive names or sensitive plaintext data in your [Primary Key](HowItWorks.md "HowItWorks.md") for your table and
Global Secondary Indexes. Key names will show up in your table definition.
For example, the Primary Key names are accessible to anyone with permissions
to call [DescribeTable](WorkingWithTables.md#WorkingWithTables.Basics.DescribeTable "WorkingWithTables.md#WorkingWithTables.Basics.DescribeTable"). Key values can show up in your [AWS
CloudTrail](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md") and other logs. Additionally, DynamoDB uses the key
values to distribute data and route requests and AWS administrators may
observe the values to maintain the health of the service.

If you need to use sensitive data in your table or GSI key values, we
recommend using end-to-end client encryption. This allows you to perform
key-value references to your data while ensuring that it never appears
unencrypted in your DynamoDB related logs. One way to accomplish this is to use
the [AWS Database Encryption SDK for DynamoDB](../../../database-encryption-sdk/latest/devguide/client-server-side.md "../../../database-encryption-sdk/latest/devguide/client-server-side.md"), but that is not
required. If you use your own solution, we should always use a sufficiently
secure encryption algorithm. You should not use a non-cryptographic option
like a hash, as they are not considered sufficiently secure in most
situations.

If your Primary Key key names are sensitive, we recommend using
`pk` and `sk` instead. This is a general best
practice which leaves your Partition Key design flexible.

Always consult your security experts or AWS account team if you are
concerned about what the right choice would be.
