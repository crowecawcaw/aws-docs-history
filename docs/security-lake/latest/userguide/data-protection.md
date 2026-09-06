

# Data protection in Amazon Security Lake
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon Security Lake. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Security Lake or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## Encryption at rest
<a name="encryption-rest"></a>

Amazon Security Lake securely stores your data at rest using AWS encryption solutions. Raw security log and event data is stored in source-specific [multi-tenant Amazon Simple Storage Service (Amazon S3) buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/common-bucket-patterns.html#multi-tenant-buckets) in an account that Security Lake manages. Each log source has its own multi-tenant bucket. Security Lake encrypts this raw data using an [AWS owned key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) from AWS Key Management Service (AWS KMS). AWS owned keys are a collection of AWS KMS keys that an AWS service—in this case Security Lake—owns and manages for use in multiple AWS accounts.

Security Lake runs extract, transform, and load (ETL) jobs on raw log and event data. 

After the ETL jobs are completed, Security Lake creates single-tenant S3 buckets in your account (one bucket for each AWS Region that you've enabled Security Lake in). Data is stored in the multi-tenant S3 buckets only temporarily until Security Lake can reliably deliver the data to the single-tenant S3 buckets. The single-tenant buckets include a resource-based policy that gives Security Lake permission to write log and event data to the buckets. To encrypt data in your S3 bucket, you can choose either an [S3-managed encryption key](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html) or a [customer managed key ](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) (from AWS KMS). Both options use symmetric encryption.

### Using a KMS key for encryption of your data
<a name="customer-managed-key"></a>

By default, the data delivered by Security Lake to your S3 bucket is encrypted by Amazon server-side encryption with [Amazon S3-managed encryption keys (SSE-S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html). To provide a security layer that you manage directly, you can instead use [server-side encryption with AWS KMS keys (SSE-KMS)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html) for your Security Lake data.

SSE-KMS isn't supported in the Security Lake console. To use SSE-KMS with the Security Lake API or CLI, you first [create a KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) or use an existing key. You attach a policy to the key that determines which users can use the key for encrypting and decrypting Security Lake data.

If you use a customer managed key to encrypt data that's written to your S3 bucket, you can't choose a multi-Region key. For customer managed keys, Security Lake creates a [grant](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) on your behalf by sending a `CreateGrant` request to AWS KMS. Grants in AWS KMS are used to give Security Lake access to a KMS key in a customer account.

Security Lake requires the grant to use your customer managed key for the following internal operations:
+ Send `GenerateDataKey` requests to AWS KMS to generate data keys encrypted by your customer managed key.
+ Send `RetireGrant` requests to AWS KMS. When you make updates to your data lake, this operation enables the retirement of the grant that was added to the AWS KMS key for ETL processing.

Security Lake doesn't need `Decrypt` permissions. When authorized users of the key read Security Lake data, S3 manages the decryption, and the authorized users are able to read data in unencrypted form. However, a subscriber needs `Decrypt` permissions to consume source data. For more information about subscriber permissions, see [Managing data access for Security Lake subscribers](subscriber-data-access.md).

If you want to use an existing KMS key to encrypt Security Lake data, you must modify the key policy for the KMS key. The key policy must allow the IAM role associated with the Lake Formation data lake location to use the KMS key to decrypt the data. For instructions on how you can change the key policy for a KMS key, see [Changing a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html) in the AWS Key Management Service Developer Guide.

Your KMS key can accept grant requests, allowing Security Lake to access the key, when you create a key policy or use an existing key policy with the appropriate permissions. For instructions on creating a key policy, see [Creating a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-overview.html) in the *AWS Key Management Service Developer Guide*. 

Attach the following key policy to your KMS key:

```
{
  "Sid": "Allow use of the key",
  "Effect": "Allow",
  "Principal": {"AWS": "arn:aws:iam::111122223333:role/ExampleRole"},
  "Action": [
    "kms:CreateGrant",
    "kms:DescribeKey",
    "kms:GenerateDataKey"
  ],
  "Resource": "*"
}
```

### Required IAM permissions when using a customer managed key
<a name="iam-permissions-key"></a>

See the [Getting started: Prerequisites](get-started-programmatic.md#prerequisites) section for an overview of IAM roles that you need to create to use Security Lake.

When you add a custom source or a subscriber, Security Lake creates IAM roles in your account. These roles are intended to be shared with other IAM identities. They permit a custom source to write data to the data lake and a subscriber to consume data from the data lake. An AWS managed policy called `AmazonSecurityLakePermissionsBoundary` sets the permission boundaries for these roles.

### Encrypting Amazon SQS queues
<a name="encrypt-sqs-queues"></a>

When you create your data lake, Security Lake creates two unencrypted Amazon Simple Queue Service (Amazon SQS) queues in the delegated Security Lake administrator account. You should encrypt these queues to protect your data. The default server-side encryption (SSE) provided by Amazon Simple Queue Service isn't sufficient. You must create a customer managed key in AWS Key Management Service (AWS KMS) to encrypt the queues and the grant the Amazon S3 service principal permissions to work with the encrypted queues. For instructions on granting these permissions, see [Why aren't Amazon S3 event notifications delivered to an Amazon SQS queue that uses server-side encryption?](https://repost.aws/knowledge-center/sqs-s3-event-notification-sse) in the AWS Knowledge Center.

Since Security Lake uses AWS Lambda to support extract, transfer, and load (ETL) jobs on your data, you must also give Lambda permissions to manage messages in your Amazon SQS queues. For information, see [Execution role permissions](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-permissions) in the *AWS Lambda Developer Guide*.

## Encryption in transit
<a name="encryption-transit"></a>

Security Lake encrypts all data in transit between AWS services. Security Lake protects data in transit, as it travels to and from the service, by automatically encrypting all inter-network data using the Transport Layer Security (TLS) 1.2 encryption protocol. Direct HTTPS requests sent to the Security Lake APIs are signed by using the [AWS Signature Version 4 Algorithm](https://docs.aws.amazon.com/general/latest/gr/sigv4_signing.html) to establish a secure connection.