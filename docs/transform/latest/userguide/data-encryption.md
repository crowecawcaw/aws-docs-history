# Data encryption in AWS Transform

This topic provides information specific to AWS Transform about encryption in transit and
encryption at rest.

AWS Transform provides encryption by default to protect sensitive customer data at rest with
encryption using AWS owned keys.

## Encryption types

### AWS Owned Keys (Default)

###### Note

**AWS owned keys** — AWS Transform uses these keys by
default to automatically encrypt personally identifiable data. You can't view,
manage, or use AWS owned keys, or audit their use. However, you don't have to
take any action or change any programs to protect the keys that encrypt your data.
For more information, see AWS owned keys in the AWSKey Management Service
Developer Guide.

Encryption of data at rest by default helps reduce the operational overhead and
complexity involved in protecting sensitive data. At the same time, it enables you to
build secure applications that meet strict encryption compliance and regulatory
requirements.

While you can't disable this layer of encryption or select an alternate encryption
type, you can add a second layer of encryption over the existing AWS owned
encryption keys by choosing a customer managed key when you create your
transformation:

### Customer managed keys (Optional)

**Customer managed keys** — AWS Transform supports the use of
a symmetric customer managed key that you create, own, and manage to add a second
layer of encryption over the existing encryption using AWS owned keys. Because you
have full control of this layer of encryption, you can perform such tasks as:

- Establishing and maintaining key policies
- Establishing and maintaining IAM policies and grants
- Enabling and disabling key policies
- Rotating key cryptographic material
- Adding tags
- Creating key aliases
- Rotating key cryptographic material
- Adding tags
- Creating key aliases
- Scheduling keys for deletion
- For more information, see [customer managed
  key](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk") in the _AWS Key Management Service Developer
  Guide_.

###### Note

AWS Transform automatically enables encryption at rest using AWS owned keys to
protect personally identifiable data at no charge. However, AWS KMS charges apply
for using a customer managed key. For more information about pricing, see the
[AWS Key Management Service
pricing](../../../kms/pricing.md "../../../kms/pricing.md").

For more information on AWS KMS, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md")

### How AWS Transform uses grants in AWS Key Management Service

AWS Transform requires a grant to use your customer managed key.

When you create a [Resource Name] encrypted with a customer managed key, AWS Transform
creates a grant on your behalf by sending a CreateGrant request to AWS Key Management Service. Grants
in AWS Key Management Service are used to give AWS Transform access to a KMS key in a customer account.

AWS Transform requires the grant to use your customer managed key for the following
internal operations:

- Send [KMS API] requests to AWS KMS to verify that the symmetric customer
  managed KMS key ID entered when creating [Resource Name] is valid.
- Send [KMS API] requests to AWS KMS to generate data keys encrypted by your
  customer managed key.
- Send [KMS API] requests to AWS KMS to decrypt the encrypted data keys so that
  they can be used to encrypt your data.

You can revoke access to the grant, or remove the service's access to the customer
managed key at any time. If you do, AWS Transform won't be able to access any of the data
encrypted by the customer managed key, which affects operations that are dependent on
that data. For example, if you attempt to get [Resource Name] from an encrypted
[Resource Name]that AWS Transform can't access, then the operation would return an
AccessDeniedException error.

## Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management
Console, or the AWS Key Management Service APIs.

To create a symmetric customer managed key, follow the steps for [Creating
symmetric customer managed key](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in the _AWS Key Management Service Developer
Guide_.

### Key policy

Key policies control access to your customer managed key. Every customer managed
key must have exactly one key policy, which contains statements that determine who
can use the key and how they can use it. When you create your customer managed key,
you can specify a key policy. For more information, see [Managing access to customer managed keys](../../../kms/latest/developerguide/control-access-overview.md#managing-access "../../../kms/latest/developerguide/control-access-overview.md#managing-access") in the _AWS Key Management Service
Developer Guide_.

To use your customer managed key with your AWS Transform resources, the following API
operations must be permitted in the key policy:

kms:CreateGrant – Adds a grant to a customer managed key. Grants control access to
a specified KMS key, which allows access to grant operations AWS Transform requires. For more
information about Using Grants, see the
_AWS Key Management Service Developer Guide_.

This allows AWS Transform to do the following:

- Call [KMS API (GenerateDataKeyWithoutPlainText/GenerateDatakey) to generate
  an encrypted data key and store it, because the data key isn't immediately used
  to encrypt.
- Call [KMS API (Decrypt)] to use the stored encrypted data key to access
  encrypted data.
- Set up a retiring principal to allow the service to RetireGrant.
- kms:DescribeKey – Provides the customer managed key details to allow
  [Service Name] to validate the key.

## Encryption in transit

Communication between customers and AWS Transform and between AWS Transform and its downstream
dependencies is protected using TLS 1.2 or higher connections.

###### Important

When you [Connect a discovery account](../../../transform-vmware-connect-discovery-account.md "../../../transform-vmware-connect-discovery-account.md"), AWS Transform creates an Amazon S3 bucket on your behalf in that
account. That bucket does not have `SecureTransport` enabled by
default. If you want the bucket policy to include secure transport you must
update the policy. For more information, see [Security best
practices for Amazon S3](../../../AmazonS3/latest/userguide/security-best-practices.md "../../../AmazonS3/latest/userguide/security-best-practices.md").

## Encryption at rest

AWS Transform stores data at rest using Amazon DynamoDB and Amazon Simple Storage Service (Amazon S3). The data at rest is
encrypted using AWS encryption solutions by default. AWS Transform encrypts your data with
encryption using AWS owned keys from AWS Key Management Service (AWS KMS). You don’t have to take any
action to protect the AWS managed keys that encrypt your data. For more information,
see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk")
in the _AWS Key Management Service Developer Guide_.

| Data type                                                                                                                                    | AWS-owned key encryption | Customer managed key encryption (Optional) |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ | ------------------------------------------ |
| Customer bucket data<br>Customer inputs and outputs such as code and documentation stored in<br>an Amazon S3 bucket                          | Enabled                  | Enabled                                    |
| Artifact Store<br>Intermediate artifacts as part of code transformation stored in an S3<br>bucket                                            | Enabled                  | Enabled                                    |
| Job Objective<br>The customer's intent for the job stored in an Amazon S3 bucket                                                             | Enabled                  | Enabled                                    |
| Chat messages<br>Messages between the customer and AWS Transform stored in an Amazon S3<br>bucket                                            | Enabled                  | Enabled                                    |
| Chat Knowledge Base<br>Indexed data relevant to AWS Transform and customer chat stored in Amazon<br>OpenSearch and processed via AWS Bedrock | Enabled                  | Enabled                                    |

Note: The customer can register their own Customer Managed Key (CMK) to be used for
encrypting all of the above data types.

Customer managed keys are KMS keys in your AWS account that you create, own, and
manage to directly control access to your data by controlling access to the KMS key.
Only symmetric keys are supported. For information on creating your own KMS key, see
[Creating
keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md") in the _AWS Key Management Service Developer Guide_.

When you use a customer managed key, AWS Transform makes use of KMS grants, allowing
authorized users, roles, or applications to use a KMS key. When an AWS Transform administrator
chooses to use a customer managed key for encryption during configuration, a grant is
created for them. This grant is what allows the end user to use the encryption key for
data encryption at rest. For more information on grants, see [Grants in AWS KMS](../../../kms/latest/developerguide/grants.md "../../../kms/latest/developerguide/grants.md").

## Using customer managed KMS keys

After creating a customer managed KMS key, an AWS Transform administrator must provide the
key in the AWS Transform console to use it to encrypt data.

To set up a customer managed key to encrypt data in AWS Transform, administrators need
permissions to use AWS KMS.

To use features that are encrypted with a customer managed key, users need
permissions to allow AWS Transform to access the customer managed key.

If you see an error related to KMS grants while using AWS Transform, you likely need to
update your permissions to allow AWS Transform to create grants. To automatically configure the
needed permissions, go to the AWS Transform console and choose **Update
permissions** in the banner at the top of the page. In order to allow AWS Transform
to create grants, you need to update the permissions on the AWS Transform console page.

## Allow AWS Transform

access to customer managed keys

The following example policy grants users permissions to access features encrypted
with a customer managed key by allowing AWS Transform access to the key. This policy is
required to use AWS Transform if an administrator has set up a customer managed key for
encryption.
