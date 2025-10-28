# Data protection in AWS B2B Data Interchange

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS B2B Data Interchange. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS B2B Data Interchange or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data encryption in Amazon S3

AWS B2B Data Interchange uses the default encryption options you set for your Amazon S3 bucket to encrypt
your data. When you enable encryption on a bucket, all objects are encrypted when they
are stored in the bucket. The objects are encrypted by using server-side encryption with
either Amazon S3 managed keys (SSE-S3) or AWS Key Management Service (AWS KMS) managed keys (SSE-KMS). For
information about server-side encryption, see [Protecting data
using server-side encryption](../../../AmazonS3/latest/dev/serv-side-encryption.md "../../../AmazonS3/latest/dev/serv-side-encryption.md") in the
_Amazon Simple Storage Service User Guide_.

The following steps show you how to encrypt data in AWS B2B Data Interchange.

###### To allow encryption in AWS B2B Data Interchange

1. Enable default encryption for your Amazon S3 bucket. For instructions, see [Amazon
   S3 default encryption for S3 buckets](../../../AmazonS3/latest/dev/bucket-encryption.md "../../../AmazonS3/latest/dev/bucket-encryption.md") in the
   _Amazon Simple Storage Service User Guide_.
2. Update the AWS Identity and Access Management (IAM) role policy that is attached to the user to grant
   the required AWS Key Management Service (AWS KMS) permissions.
3. If you are using a session policy for the user, the session policy must grant
   the required AWS KMS permissions.

The following example shows an IAM policy that grants the minimum permissions
required when using AWS B2B Data Interchange with an Amazon S3 bucket that is enabled for AWS KMS encryption.
Include this example policy in both the user IAM role policy and session policy, if
you are using one.

```
{
	"Sid": "Stmt1544140969635",
	"Action": [
		"kms:Decrypt",
		"kms:Encrypt",
		"kms:GenerateDataKey"
	],
	"Effect": "Allow",
	"Resource": "arn:aws:kms:`region`:`account-id`:key/`kms-key-id`"
}
```

###### Note

The KMS key ID that you specify in this policy must be the same as the one
specified for the default encryption in step 1.

Root, or the IAM role that is used for the user, must be allowed in the AWS KMS
key policy. For information about the AWS KMS key policy, see [Using key
policies in AWS KMS](../../../kms/latest/developerguide/key-policies.md "../../../kms/latest/developerguide/key-policies.md") in the
_AWS Key Management Service Developer Guide_.

## No data used for service improvement

Generative AI-assisted EDI mapping uses Amazon Bedrock to assist customers with creating mapping templates. With
Amazon Bedrock, your content is not used to improve the base models, and is not shared with any
model providers. For more information, see [https://aws.amazon.com/bedrock/faqs](https://aws.amazon.com/bedrock/faqs "https://aws.amazon.com/bedrock/faqs").

## Deleting AWS B2B Data Interchange resources

You can delete the resources that you create in B2B Data Interchange. See the guidance for each
resource type in following sections of the _AWS B2B Data Interchange API
Reference_.

- [Deleting a trading
  capability](../APIReference/API_DeleteCapability.md "../APIReference/API_DeleteCapability.md")
- [Deleting a
  partnership](../APIReference/API_DeletePartnership.md "../APIReference/API_DeletePartnership.md")
- [Deleting a
  profile](../APIReference/API_DeleteProfile.md "../APIReference/API_DeleteProfile.md")
- [Deleting a
  transformer](../APIReference/API_DeleteTransformer.md "../APIReference/API_DeleteTransformer.md")
