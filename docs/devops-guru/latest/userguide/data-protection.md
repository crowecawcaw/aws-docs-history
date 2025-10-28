# Data protection in Amazon DevOps Guru

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Amazon DevOps Guru. As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
You are also responsible for the security configuration and management tasks for the AWS services
that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/"). For information about data protection in Europe, see the [AWS Shared
Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

For data protection purposes, we recommend that you protect AWS account
credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through
  a command line interface or an API, use a FIPS endpoint. For more information about the
  available FIPS endpoints, see [Federal
  Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with DevOps Guru or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data encryption in DevOps Guru

Encryption is an important part of DevOps Guru security. Some encryption, such as for data in
transit, is provided by default and does not require you to do anything. Other encryption,
such as for data at rest, you can configure when you create your project or build.

- **Encryption of data in-transit**: All communication between
  customers and DevOps Guru and between DevOps Guru and its downstream dependencies is protected using
  TLS and authenticated using the Signature Version 4 signing process. All DevOps Guru endpoints
  use certificates managed by AWS Private Certificate Authority. For more information, see [Signature Version 4 signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md")
  and [What is ACM PCA](../../../privateca/latest/userguide.md "../../../privateca/latest/userguide.md").
- **Encryption of data at-rest**: For all AWS resources
  analyzed by DevOps Guru, the Amazon CloudWatch metrics and data, resource IDs, and AWS CloudTrail events are
  stored using Amazon S3, Amazon DynamoDB, and Amazon Kinesis. If AWS CloudFormation stacks are used to define the
  analyzed resources, then stack data is also collected. DevOps Guru uses the data retention
  policies of Amazon S3, DynamoDB, and Kinesis. Data stored in Kinesis can be retained for up to one year
  and depends on the policies set. Data stored in Amazon S3 and DynamoDB is stored for one year.

Stored data is encrypted using the data-at-rest encryption capabilities of Amazon S3,
DynamoDB, and Kinesis.

**Customer managed keys**: DevOps Guru supports encrypting customer
content and sensitive metadata such as log anomalies generated from CloudWatch Logs with
customer managed keys. This feature provides you the option of adding a
self-managed security layer to help you meet the compliance and regulatory
requirements of your organization. For information on enabling customer managed
keys in your DevOps Guru settings, see [Updating encryption settings in
DevOps Guru](update-settings.md#update-encryption "update-settings.md#update-encryption").

Because you have full control of this layer of encryption, you can perform such tasks as:

    + Establishing and maintaining key policies
    + Establishing and maintaining IAM policies and grants
    + Enabling and disabling key policies
    + Rotating key cryptographic material
    + Adding tags
    + Creating key aliases
    + Scheduling keys for deletion

For more information, see [Customer managed keys](../../../kms/latest/developerguide/concepts.md#customer-cmk "../../../kms/latest/developerguide/concepts.md#customer-cmk")
in the AWS Key Management Service Developer Guide.

###### Note

DevOps Guru automatically enables encryption at rest using AWS owned keys to protect sensitive metadata at no charge.
However, AWS KMS charges apply for using a customer managed key. For more information about pricing, see the AWS Key Management Service pricing.

## How DevOps Guru uses grants in AWS KMS

DevOps Guru requires a grant to use your customer managed key.

When you choose to enable encryption with a customer managed key, DevOps Guru creates a grant on your behalf by sending
a CreateGrant request to AWS KMS. Grants in AWS KMS are used to give DevOps Guru access to a AWS KMS key in a customer account.

DevOps Guru requires the grant to use your customer managed key for the following internal operations:

- Send DescribeKey requests to AWS KMS to verify that the symmetric customer managed KMS key ID entered
  when creating a tracker or geofence collection is valid.
- Send GenerateDataKey requests to AWS KMS to generate data keys encrypted by your customer managed key.
- Send Decrypt requests to AWS KMS to decrypt the encrypted data keys so that they can be used to encrypt your data.

You can revoke access to the grant, or remove the service's access to the customer managed key at any time.
If you do, DevOps Guru won't be able to access any of the data encrypted by the customer managed key,
which affects operations that are dependent on that data. For example, if you attempt to get encrypted log anomaly information
that DevOps Guru can't access, then the operation would return an AccessDeniedException error.

## Monitoring your encryption keys in DevOps Guru

When you use an AWS KMS customer managed key with your DevOps Guru resources,
you can use AWS CloudTrail or CloudWatch Logs to track requests that DevOps Guru sends to AWS KMS.

## Create a customer managed key

You can create a symmetric customer managed key by using the AWS Management Console or the AWS KMS APIs.

To create a symmetric customer managed key,
see [Creating symmetric encryption KMS keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk").

### Key policy

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements
that determine who can use the key and how they can use it. When you create your customer managed key, you can specify a key policy.
For more information, see [Authentication and access control for AWS KMS](../../../kms/latest/developerguide/control-access.md "../../../kms/latest/developerguide/control-access.md") in the AWS Key Management Service Developer Guide.

To use your customer managed key with your DevOps Guru resources, the following API operations must be permitted in the key policy:

- `kms:CreateGrant` – Adds a grant to a customer managed key. Grants control access to a specified AWS KMS key, which allows access to grant operations
  DevOps Guru requires. For more information about using grants, see the AWS Key Management Service Developer Guide.

This allows DevOps Guru to do the following:

- Call GenerateDataKey to generate an encrypted data key and store it, because the data key isn't immediately used to encrypt.
- Call Decrypt to use the stored encrypted data key to access encrypted data.
- Set up a retiring principal to allow the service to RetireGrant.
- Use kms:DescribeKey to provide the customer managed key details to allow DevOps Guru to validate the key.

The following statement includes policy statement examples you can add for DevOps Guru:

```
  "Statement" : [
    {
      "Sid" : "Allow access to principals authorized to use DevOps Guru",
      "Effect" : "Allow",
      "Principal" : {
        "AWS" : "*"
      },
      "Action" : [
        "kms:DescribeKey",
        "kms:CreateGrant"
      ],
      "Resource" : "*",
      "Condition" : {
        "StringEquals" : {
          "kms:ViaService" : "devops-guru.`Region`.amazonaws.com",
          "kms:CallerAccount" : "111122223333"
        }
    },
    {
      "Sid": "Allow access for key administrators",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::111122223333:root"
       },
      "Action" : [
        "kms:*"
       ],
      "Resource": "arn:aws:kms:region:111122223333:key/key_ID"
    },
    {
      "Sid" : "Allow read-only access to key metadata to the account",
      "Effect" : "Allow",
      "Principal" : {
        "AWS" : "arn:aws:iam::111122223333:root"
      },
      "Action" : [
        "kms:Describe*",
        "kms:Get*",
        "kms:List*"
      ],
      "Resource" : "*"
    }
  ]
```

## Traffic privacy

You can improve the security of your resource analysis and insight generation by configuring DevOps Guru to use an interface
VPC endpoint. To do this, you do not need an internet gateway, NAT device, or virtual
private gateway. It also is not required to configure PrivateLink, though it is
recommended. For more information, see [DevOps Guru and interface VPC endpoints
(AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md"). For more information about
PrivateLink and VPC endpoints, see [AWS
PrivateLink](https://aws.amazon.com/privatelink/ "https://aws.amazon.com/privatelink/") and [Accessing AWS services
through PrivateLink](../../../vpc/latest/userguide/VPC_Introduction.md#what-is-privatelink "../../../vpc/latest/userguide/VPC_Introduction.md#what-is-privatelink").
