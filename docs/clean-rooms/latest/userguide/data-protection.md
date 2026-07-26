# Data protection in AWS Clean Rooms

The AWS
[shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")

applies to data protection in AWS Clean Rooms.

As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure.
You are also responsible for the security configuration and management tasks for the AWS services
that you use.

For more information about data privacy, see
[Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/").

For information about data protection in Europe, see the
[General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/ "https://aws.amazon.com/compliance/gdpr-center/").

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

## Encryption for intermediate tables

When using intermediate tables within AWS Clean Rooms, the service encrypts all data stored at rest
with AWS Key Management Service (AWS KMS). By default, the service encrypts intermediate table data with a service-managed
key. If
you choose to provide your own KMS key, the service encrypts your intermediate table at rest
with that key. This uses server-side encryption with AWS KMS keys (SSE-KMS).

AWS Clean Rooms uses key policies and service principals to access customer managed keys for intermediate
tables. The service encrypts intermediate table data at write time when the table is populated,
and decrypts the data transparently when the intermediate table is used in a subsequent
analysis.

The KMS key ARN is provided at intermediate table creation time and applies to all
versions of the table. You can update the KMS key using the **Edit**
action on the intermediate table details page. The new key takes effect on the next populate
– each version is encrypted with the key that was specified at the time of
population.

###### Note

Deleting an intermediate table does not require any AWS KMS operations. The encrypted data
in Amazon S3 is deleted by the managed storage service.

**Required AWS KMS permissions for intermediate tables**

To use your customer managed key with intermediate tables, the following API operations must be
permitted in the key policy:

- `kms:DescribeKey` – Validates the key state when you create or
  update an intermediate table.
- `kms:GenerateDataKey` – Encrypts intermediate table data when the
  table is populated. Amazon S3 calls AWS KMS on behalf of the service to generate data keys for
  SSE-KMS encryption.
- `kms:Decrypt` – Decrypts intermediate table data when the table is
  referenced in a subsequent analysis. Amazon S3 calls AWS KMS on behalf of the service to decrypt
  the data transparently.

**Key policy example for intermediate tables**

The following is an example key policy for using a customer managed key with intermediate
tables:

```
`{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Sid": "Allow Clean Rooms to encrypt and decrypt intermediate table data",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms.amazonaws.com"
 },
 "Action": [
 "kms:GenerateDataKey",
 "kms:Decrypt"
 ],
 "Resource": "*",
 "Condition": {
 "StringLike": {
 "kms:EncryptionContext:aws:cleanrooms:intermediateTableArn": "arn:aws:cleanrooms:`us-east-1`:`666666666666`:membership/`membership-id`/intermediatetable/`intermediate-table-id`"
 },
 "ForAnyValue:ArnEquals": {
 "aws:SourceArn": [
 "arn:aws:cleanrooms:`us-east-1`:`666666666666`:membership/`member-1-membership-id`",
 "arn:aws:cleanrooms:`us-east-1`::membership/`member-2-membership-id`"
 ]
 }
 }
 },
 {
 "Sid": "Allow Clean Rooms to describe key",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms.amazonaws.com"
 },
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "*"
 },
 {
 "Sid": "Allow caller to validate key via Clean Rooms",
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
 "kms:ViaService": "cleanrooms.`us-east-1`.amazonaws.com",
 "kms:CallerAccount": "`666666666666`"
 }
 }
 }
 ]
}`
```

The first statement grants the AWS Clean Rooms service principal access for encrypting data during
population and decrypting data during analysis. The
`kms:EncryptionContext:aws:cleanrooms:intermediateTableArn` condition restricts
which intermediate tables can use the key. The `aws:SourceArn` condition provides
confused deputy protection by restricting access to specific membership ARNs in your
collaboration.

The second statement allows the service to describe the key for validation
purposes.

The third statement allows a specific IAM role in the customer's account to perform key
validation through AWS Clean Rooms. The permitted actions are DescribeKey, GenerateDataKey, and Decrypt.
Access is scoped using `kms:ViaService` and `kms:CallerAccount`
conditions. This role is typically the IAM role that you use to interact with
AWS Clean Rooms.

**Encryption context**

AWS Clean Rooms uses the following encryption context when encrypting intermediate table data:

```
`{
 "aws:cleanrooms:intermediateTableArn": "`arn:aws:cleanrooms:us-east-1:123456789012:membership/membership-id/intermediatetable/intermediate-table-id`"
}`
```

Every AWS KMS operation is logged in CloudTrail with the intermediate table ARN, providing a clear
audit trail of which resource triggered each encrypt or decrypt call. You can use the
`kms:EncryptionContext` condition key in your key policy to restrict which
intermediate tables can use the key.

## Encryption for configured dataset associations

AWS Clean Rooms transparently encrypts all configured dataset association data at rest when
stored in service-managed storage. You do not need any additional configuration. Your data is encrypted at rest during ML training and inference workflows.

AWS Clean Rooms supports server-side encryption using customer managed keys that you create,
own, and manage in AWS Key Management Service. If you provide a symmetric encryption AWS KMS key when
creating a configured dataset association, the service uses that key to encrypt your
data in service-managed storage. If a customer managed key is not specified, Amazon S3
managed encryption (SSE-S3) is used by default.

AWS Clean Rooms supports only symmetric encryption AWS KMS keys for configured dataset
associations. You cannot use an asymmetric AWS KMS key, HMAC AWS KMS key, or AWS KMS key in
an external key store. For help determining whether a AWS KMS key is a symmetric
encryption key, see [Identifying symmetric and
asymmetric KMS keys](../../../kms/latest/developerguide/find-symm-asymm.md "../../../kms/latest/developerguide/find-symm-asymm.md") in the _AWS Key Management Service Developer Guide_.

### How AWS Clean Rooms uses customer managed keys for configured dataset associations

A configured dataset association workflow involves two potential AWS KMS keys:

- **CDA key** – The customer managed AWS KMS
  key you optionally provide when creating the configured dataset association
  (`kmsKeyArn` parameter). AWS Clean Rooms uses this key to encrypt your data in
  service-managed storage during training and inference jobs.
- **Source key** – The AWS KMS key that
  already encrypts your source Amazon S3 objects (if applicable). Your CDA role decrypts
  with this key when the service copies data for processing.

Both keys are optional. They can be the same key or different keys.

The service encrypts all copies of your data stored in service-managed storage
during training and inference job execution. This includes data copied from your
source Amazon S3 bucket for processing by .

AWS Clean Rooms uses your CDA role during the data copy phase. For the
processing phase, AWS Clean Rooms uses a service-managed IAM role. AWS Clean Rooms grants temporary access to your AWS KMS key. After job completion, AWS Clean Rooms automatically revokes the service-managed role's access.

### Configuring permissions to use a customer managed key

To use your customer managed key with configured dataset associations, the
following AWS KMS API operations must be permitted in the key policy:

- `kms:DescribeKey` – Allows AWS Clean Rooms to validate the key at
  configured dataset association creation time.
- `kms:Decrypt` – Allows to decrypt your data
  during training or inference. Also allows your CDA role to decrypt source data
  (if source key = CDA key).
- `kms:GenerateDataKey` – Allows your CDA role to encrypt
  data when copying it to service-managed storage for processing.
- `kms:CreateGrant` – Allows to create grants
  for encrypting Amazon EBS volumes attached to training and inference instances. Grants
  are restricted by the `kms:GrantOperations` condition to a specific
  set of operations, and by `kms:GrantIsForAWSResource` to ensure only
  AWS services can exercise the grant.

#### CDA key – Key policy example

The following key policy grants the minimum permissions needed for AWS Clean Rooms to use
your CDA key during training or inference:

```
`{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Sid": "Allow encrypt and decrypt for principals authorized to use AWS Clean Rooms ML",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`ExampleRole`"
 },
 "Action": [
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
 "Sid": "Allow grant operations for principals authorized to use AWS Clean Rooms ML",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`ExampleRole`"
 },
 "Action": "kms:CreateGrant",
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
 "AWS": "arn:aws:iam::`111122223333`:role/`ExampleRole`"
 },
 "Action": "kms:DescribeKey",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "cleanrooms-ml.`us-east-1`.amazonaws.com"
 }
 }
 },
 {
 "Sid": "Allow decrypt for AWS Clean Rooms ML service principal",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": "kms:Decrypt",
 "Resource": "*"
 },
 {
 "Sid": "Allow grant operations for AWS Clean Rooms ML service principal",
 "Effect": "Allow",
 "Principal": {
 "Service": "cleanrooms-ml.amazonaws.com"
 },
 "Action": "kms:CreateGrant",
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
 "Action": "kms:DescribeKey",
 "Resource": "*"
 }
 ]
}`
```

#### Source key – Key policy example (if source data is SSE-KMS encrypted)

If your source Amazon S3 objects are encrypted with a separate AWS KMS key, add the
following statement to that key's policy to allow your CDA role to decrypt:

```
`{
 "Sid": "Allow CDA role to decrypt source data via S3",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/service-role/`MyCDARole`"
 },
 "Action": "kms:Decrypt",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`us-east-1`.amazonaws.com"
 }
 }
}`
```

#### CDA role – IAM permissions policy (KMS statements)

Your CDA role's IAM permissions policy must include the appropriate AWS KMS
actions scoped to specific key ARNs:

```
`{
 "Sid": "DecryptSourceData",
 "Effect": "Allow",
 "Action": "kms:Decrypt",
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`source-key-id`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`us-east-1`.amazonaws.com"
 }
 }
},
{
 "Sid": "Encrypt and Decrypt Data For Processing",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": "arn:aws:kms:`us-east-1`:`111122223333`:key/`cda-key-id`",
 "Condition": {
 "StringEquals": {
 "kms:ViaService": "s3.`us-east-1`.amazonaws.com"
 }
 }
}`
```

If the source key and CDA key are the same, a single statement with both
`kms:Decrypt` and `kms:GenerateDataKey` is sufficient.

### Creating a configured dataset association with a customer managed key

To encrypt your data with a customer managed key, provide the AWS KMS key ARN in
the `kmsKeyArn` parameter when calling the
`CreateConfiguredDatasetAssociation` API.

At creation time, AWS Clean Rooms validates the key by calling
`kms:DescribeKey` using your credentials to confirm the key exists, is
enabled, and is a symmetric encryption key. If validation fails, the configured
dataset association is not created.

### Changing encryption configuration

The `kmsKeyArn` is immutable after creation. You cannot change the
AWS KMS key on an existing configured dataset association. To use a different AWS KMS
key, delete the existing configured dataset association and create a new one with the
desired key.

Deleting a configured dataset association does not require any AWS KMS
operations.

### Scoping down access to the customer managed key

The following mechanisms are available to scope down access to your customer
managed key:

- **`kms:ViaService` condition**
  – Restricts key usage to requests made through a specific AWS service.
  In the key policy examples, access is scoped to
  `cleanrooms-ml.`region`.amazonaws.com` for
  the service principal path and
  `s3.`region`.amazonaws.com` for the CDA role
  path.
- **`kms:GrantIsForAWSResource`
  condition** – Ensures that `kms:CreateGrant` can only
  be exercised by an AWS service ( for Amazon EBS volume encryption), not
  by arbitrary principals.
- **`kms:GrantOperations`
  condition** – Restricts what operations can be delegated via
  grants.

### Key lifecycle considerations

- **Key validation** – The CDA key is
  validated at configured dataset association creation time via
  `kms:DescribeKey`. This provides fail-fast detection of disabled,
  deleted, or misconfigured keys.
- **Key becomes unusable** – If the CDA
  key is disabled or deleted after creation but before a job runs, the job fails
  with a AWS KMS error when the service attempts to use the key.
- **Key rotation** – Key rotation is
  handled transparently by AWS KMS. Rotated keys can still decrypt data encrypted
  under previous key material. No action is required when a key is rotated.
- **Revoking access** – You can revoke
  the service's access to your AWS KMS key at any time by modifying the key policy
  or disabling the key. If access is revoked while a job is in progress, the job
  fails. Data stored in service-managed storage is deleted after job completion
  regardless of key access status.

### Monitoring AWS Clean Rooms interaction with AWS KMS

You can use CloudTrail to track the requests that AWS Clean Rooms sends to AWS KMS on your behalf.
For more information about monitoring AWS KMS usage, see [Logging AWS KMS API
calls with CloudTrail](../../../kms/latest/developerguide/logging-using-cloudtrail.md "../../../kms/latest/developerguide/logging-using-cloudtrail.md") in the _AWS Key Management Service Developer Guide_.
