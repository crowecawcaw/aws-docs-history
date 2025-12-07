# Data protection in AWS Clean Rooms

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Clean Rooms. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS Clean Rooms or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Encryption at rest

AWS Clean Rooms always encrypts all service metadata at rest without requiring any additional
configuration. This encryption is automatic when you use AWS Clean Rooms.

Clean Rooms ML encrypts all data stored within the service at rest with AWS KMS. If you choose to
provide your own KMS key, the contents of your lookalike models and lookalike segment
generation jobs are encrypted at rest with your KMS key.

When using AWS Clean Rooms custom ML models, the service encrypts all data stored at rest with AWS KMS. AWS Clean Rooms supports the use of symmetric customer managed keys that you create, own, and manage to encrypt data at rest. If customer managed keys are not specified, AWS owned keys are used by default.

AWS Clean Rooms uses grants and key policies to access customer managed keys. You can revoke access to the grant, or remove the service's access to the customer managed key at any time. If you do, AWS Clean Rooms won't be able to access any of the data encrypted by the customer managed key, which affects operations that are dependent on that data. For example, if you attempt to create a trained model from an encrypted ML input channel that AWS Clean Rooms can't access, then the operation would return a `ValidationException` error.

###### Note

You can use the encryption options in Amazon S3 to protect your data at rest.

For more information, see [Specifying Amazon S3 encryption](../../../AmazonS3/latest/userguide/specifying-s3-encryption.md "../../../AmazonS3/latest/userguide/specifying-s3-encryption.md") in the _Amazon S3 User
Guide_.

When using an ID mapping table within AWS Clean Rooms, the service encrypts all data stored at rest
with AWS KMS. If you choose to provide your own KMS key, the contents of your ID mapping table
are encrypted at rest with your KMS key via AWS Entity Resolution. For more details about the required
permissions for working with encryptions with an ID mapping workflow, see [Create a workflow job role for AWS Entity Resolution](../../../entityresolution/latest/userguide/create-workflow-job-role.md "../../../entityresolution/latest/userguide/create-workflow-job-role.md") in the _AWS Entity Resolution User
Guide_.

## Encryption in transit

AWS Clean Rooms
uses Transport Layer Security (TLS) for encryption in transit. Communication
with AWS Clean Rooms is always done over HTTPS so your data is always encrypted in
transit, regardless of
whether it's stored in Amazon S3, Amazon Athena, or Snowflake. This includes all data
in transit when using Clean Rooms ML.

## Encrypting underlying data

For more information about how to encrypt your underlying data, see [Cryptographic Computing for Clean Rooms](crypto-computing.md "crypto-computing.md").

## Key policy

Key policies control access to your customer managed key. Every customer managed key must have exactly one key policy, which contains statements that determine who can use the key and how they can use it. When you create your customer managed key, you can specify a key policy. For more information, see Managing access to customer managed keys in the AWS Key Management Service Developer Guide.

To use your customer managed key with your AWS Clean Rooms Custom ML models, the following API operations must be permitted in the key policy:

- `kms:DescribeKey` – Provides the customer managed key details to allow AWS Clean Rooms to validate the key.
- `kms:Decrypt` – Provides access to AWS Clean Rooms to decrypt the encrypted data and use it in related jobs.
- `kms:CreateGrant` - Clean Rooms ML encrypts training and inference images at rest in Amazon ECR by creating grants for Amazon ECR. To learn more, see [Encryption at Rest in Amazon ECR](../../../AmazonECR/latest/userguide/encryption-at-rest.md "../../../AmazonECR/latest/userguide/encryption-at-rest.md"). Clean Rooms ML also uses Amazon SageMaker AI to run training and inference jobs, and creates grants for SageMaker AI to encrypt the Amazon EBS volumes attached to the instances as well as the output data in Amazon S3. To learn more, see [Protect Data at Rest Using Encryption in Amazon SageMaker AI](../../../sagemaker/latest/dg/encryption-at-rest.md "../../../sagemaker/latest/dg/encryption-at-rest.md").
- `kms:GenerateDataKey` - Clean Rooms ML encrypts data at rest stored in Amazon S3 using server-side encryption with AWS KMS keys. To learn more, see [Using server-side encryption with AWS KMS keys (SSE-KMS) in Amazon S3](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md").

The following are policy statement examples you can add for AWS Clean Rooms for the following
resources:

**ML input channel with synthetic data**

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow access to principals authorized to use AWS Clean Rooms ML",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`666666666666`:role/`ExampleRole`"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:CreateGrant",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "cleanrooms-ml.`us-east-1`.amazonaws.com"
 },
 "ForAllValues:StringEquals": {
 "kms:GrantOperations": [
 "Decrypt",
 "Encrypt",
 "GenerateDataKeyWithoutPlaintext",
 "ReEncryptFrom",
 "ReEncryptTo",
 "CreateGrant",
 "DescribeKey",
 "RetireGrant",
 "GenerateDataKey"
 ]
 },
 "BoolIfExists": {
 "kms:GrantIsForAWSResource": true
 }
 }
 },
 {
 "Sid": "Allow describe key for principals authorized to use AWS Clean Rooms ML",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`444455556666`:role/`ExampleRole`"
 },
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "cleanrooms-ml.`us-east-1`.amazonaws.com"
 }
 }
 },
 {
 "Sid": "Allow grant operations for AWS Clean Rooms ML service principal",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:CreateGrant",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "kms:GrantOperations": [
 "Decrypt",
 "Encrypt",
 "GenerateDataKeyWithoutPlaintext",
 "ReEncryptFrom",
 "ReEncryptTo",
 "CreateGrant",
 "DescribeKey",
 "RetireGrant",
 "GenerateDataKey"
 ]
 }
 }
 },
 {
 "Sid": "Allow describe key for AWS Clean Rooms ML service principal",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

**ML input channel without synthetic data**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow access to principals authorized to use AWS Clean Rooms ML",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`666666666666`:role/`ExampleRole`"
 },
 "Action": [
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "cleanrooms-ml.`us-east-1`.amazonaws.com"
 }
 }
 },
 {
 "Sid": "Allow access to AWS Clean Rooms ML service principal",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": [
 "kms:DescribeKey",
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Trained model job or Trained model inference job**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Allow grant operations for principals authorized to use AWS Clean Rooms ML",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`666666666666`:role/`ExampleRole`"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:CreateGrant",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "cleanrooms-ml.`us-east-1`.amazonaws.com"
 },
 "ForAllValues:StringEquals": {
 "kms:GrantOperations": [
 "Decrypt",
 "Encrypt",
 "GenerateDataKeyWithoutPlaintext",
 "ReEncryptFrom",
 "ReEncryptTo",
 "CreateGrant",
 "DescribeKey",
 "RetireGrant",
 "GenerateDataKey"
 ]
 },
 "BoolIfExists": {
 "kms:GrantIsForAWSResource": true
 }
 }
 },
 {
 "Sid": "Allow describe key for principals authorized to use AWS Clean Rooms ML",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`444455556666`:role/`ExampleRole`"
 },
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "cleanrooms-ml.`us-east-1`.amazonaws.com"
 }
 }
 },
 {
 "Sid": "Allow grant operations for AWS Clean Rooms ML service principal",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:CreateGrant",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "ForAllValues:StringEquals": {
 "kms:GrantOperations": [
 "Decrypt",
 "Encrypt",
 "GenerateDataKeyWithoutPlaintext",
 "ReEncryptFrom",
 "ReEncryptTo",
 "CreateGrant",
 "DescribeKey",
 "RetireGrant",
 "GenerateDataKey"
 ]
 }
 }
 },
 {
 "Sid": "Allow describe key for AWS Clean Rooms ML service principal",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "*"
 }
 ]
}`

```

Clean Rooms ML does not support specifying service encryption context or source context in customer managed key policies. Encryption context used by the service internally is visible to customers in CloudTrail.
