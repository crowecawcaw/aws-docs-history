# Data protection and encryption

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in AWS Transfer Family (Transfer Family). As described in this
model, AWS is responsible for protecting the global infrastructure that runs all of the
AWS Cloud. You are responsible for maintaining control over your content that is hosted on
this infrastructure. This content includes the security configuration and management tasks
for the AWS services that you use. For more information about data privacy, see the [Data privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq "https://aws.amazon.com/compliance/data-privacy-faq"). For
information about data protection in Europe, see the [AWS shared
responsibility model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security
Blog_.

For data protection purposes, we recommend that you protect AWS account credentials and
set up individual user accounts with AWS IAM Identity Center. That way each user is given only the
permissions necessary to fulfill their job duties. We also recommend that you secure your
data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We support TLS 1.2.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security controls within
  AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in
  discovering and securing personal data that is stored in Amazon S3.
- If you require FIPS 140-2 validated cryptographic modules when accessing AWS
  through a command line interface or an API, use a FIPS endpoint. For more
  information about the available FIPS endpoints, see [Federal information processing standard (FIPS)
  140-2](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put sensitive identifying information, such as your
  customers' account numbers, into free-form fields such as a **Name** field. This includes when you work with Transfer Family or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any configuration data that you enter into
  Transfer Family service configuration, or other services' configurations, might get picked up for
  inclusion in diagnostic logs. When you provide a URL to an external server, don't
  include credentials information in the URL to validate your request to that server.

In contrast, data from upload and download operations into and out of Transfer Family servers is
treated as completely private and never exists outside of encrypted channels—such as
an SFTP or FTPS connection. This data is only ever accessible to authorized persons.

## Data encryption in Transfer Family

AWS Transfer Family uses the default encryption options you set for your Amazon S3 bucket to encrypt your
data. When you enable encryption on a bucket, all objects are encrypted when they are stored
in the bucket. The objects are encrypted by using server-side encryption with either Amazon S3
managed keys (SSE-S3) or AWS Key Management Service (AWS KMS) managed keys (SSE-KMS). For information about
server-side encryption, see [Protecting data
using server-side encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md") in the _Amazon Simple Storage Service User Guide_.

The following steps show you how to encrypt data in AWS Transfer Family.

###### To allow encryption in AWS Transfer Family

1. Enable default encryption for your Amazon S3 bucket. For instructions, see [Amazon S3
   default encryption for S3 buckets](../../../AmazonS3/latest/dev/bucket-encryption.md "../../../AmazonS3/latest/dev/bucket-encryption.md") in the
   _Amazon Simple Storage Service User Guide_.
2. Update the AWS Identity and Access Management (IAM) role policy that is attached to the user to grant the
   required AWS Key Management Service (AWS KMS) permissions.
3. If you are using a session policy for the user, the session policy must grant the
   required AWS KMS permissions.

The following example shows an IAM policy that grants the minimum permissions required
when using AWS Transfer Family with an Amazon S3 bucket that is enabled for AWS KMS encryption. Include this
example policy in both the user IAM role policy and session policy, if you are using
one.

```
{
   "Sid": "Stmt1544140969635",
   "Action": [
      "kms:Decrypt",
      "kms:Encrypt",
      "kms:GenerateDataKey",
      "kms:GetPublicKey",
      "kms:ListKeyPolicies"
   ],
   "Effect": "Allow",
   "Resource": "arn:aws:kms:`region`:`account-id`:key/`kms-key-id`"
}
```

###### Note

The KMS key ID that you specify in this policy must be the same as the one specified
for the default encryption in step 1.

Root, or the IAM role that is used for the user, must be allowed in the AWS KMS key
policy. For information about the AWS KMS key policy, see [Using key policies in AWS
KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the _AWS Key Management Service Developer Guide_.

## AWS Transfer Family encryption at rest

Because AWS Transfer Family is a file transfer service, it doesn't manage your storage data
at rest. The storage services and systems that AWS Transfer Family supports are responsible for
protecting data in that state. However, there is some service-related data that AWS Transfer Family
manages at rest.

### What's encrypted?

The only data that AWS Transfer Family handles at rest relates to the details it needs to operate
your file transfer servers and process transfers. AWS Transfer Family stores the following data
with full at-rest encryption in Amazon DynamoDB:

- Server configurations (for example, server settings, protocol configurations,
  and endpoint details).
- User authentication data, including SSH public keys and user metadata.
- Workflow execution details and step configurations.
- Connector configurations and authentication credentials for third-party
  systems. These credentials are encrypted using AWS Transfer Family managed encryption
  keys.

#### Key management

You can't manage the encryption keys that AWS Transfer Family uses to store information in
DynamoDB related to running your servers and processing transfers. This information
includes your server configurations, user authentication data, workflow details, and
connector credentials.

### What's not encrypted?

Though AWS Transfer Family doesn't control how your storage data is encrypted at rest, we still
recommend configuring your storage locations with the highest level of security that
they support. For example, you can encrypt objects with Amazon S3 managed encryption
keys (SSE-S3) or AWS KMS keys (SSE-KMS).

Learn more about how AWS storage services encrypt data at rest:

- [Amazon
  S3](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md")
- [Amazon
  EFS](../../../efs/latest/ug/encryption-at-rest.md "../../../efs/latest/ug/encryption-at-rest.md")
