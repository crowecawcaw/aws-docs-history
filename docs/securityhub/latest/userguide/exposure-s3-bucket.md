# Remediating exposures for Amazon S3 buckets

###### Note

Security Hub is in preview release and is subject to change.

AWS Security Hub can generate exposure findings for Amazon Simple Storage Service (S3) buckets.

On the Security Hub console, the Amazon S3 bucket involved in an exposure finding and its identifying information are listed in
the **Resources** section of the finding details. Programmatically, you can retrieve resource
details with the [GetFindingsV2](../../1.0/APIReference/API_GetFindingsV2.md "../../1.0/APIReference/API_GetFindingsV2.md") operation of the Security Hub API.

After identifying the resource involved in an exposure finding, you can delete the resource if you don't need it.
Deleting a nonessential resource can reduce your exposure profile and AWS costs. If the resource is essential,
follow these recommended remediation steps to help mitigate the risk. The remediation topics are
divided based on the type of trait.

A single exposure finding contains issues identified in multiple remediation topics. Conversely, you can address an exposure finding and bring down
its severity level by addressing just one remediation topic. Your approach to risk remediation
depends on your organizational requirements and workloads.

###### Note

The remediation guidance provided in this topic might require additional consultation in other AWS resources.

###### Contents

- [Misconfiguration traits for Amazon S3 buckets](exposure-s3-bucket.md#misconfiguration "exposure-s3-bucket.md#misconfiguration")
  - [The Amazon S3 bucket has versioning disabled](exposure-s3-bucket.md#versioning-disabled "exposure-s3-bucket.md#versioning-disabled")
  - [The Amazon S3 bucket has Object Lock disabled](exposure-s3-bucket.md#object-lock-disabled "exposure-s3-bucket.md#object-lock-disabled")
  - [Amazon S3 bucket is not encrypted at rest with AWS KMS keys](exposure-s3-bucket.md#sse-kms-not-used "exposure-s3-bucket.md#sse-kms-not-used")
  - [Multi-factor authentication (MFA) delete is disabled on a versioned Amazon S3 bucket](exposure-s3-bucket.md#mfa-delete-disabled "exposure-s3-bucket.md#mfa-delete-disabled")
  - [The Amazon S3 bucket allows principals from other AWS accounts to modify bucket permissions](exposure-s3-bucket.md#external-aws-access-allowed "exposure-s3-bucket.md#external-aws-access-allowed")

- [Reachability traits for Amazon S3 buckets](exposure-s3-bucket.md#reachability "exposure-s3-bucket.md#reachability")
  - [Amazon S3 bucket has public access](exposure-s3-bucket.md#s3-bucket-reachability-bucket-public-access "exposure-s3-bucket.md#s3-bucket-reachability-bucket-public-access")
  - [The Amazon S3 bucket has public read access](exposure-s3-bucket.md#public-read-allowed "exposure-s3-bucket.md#public-read-allowed")
  - [The Amazon S3 bucket has write access](exposure-s3-bucket.md#public-write-allowed "exposure-s3-bucket.md#public-write-allowed")
  - [The Amazon S3 access point has public access settings enabled](exposure-s3-bucket.md#s3-bucket-reachability-access-point-public-access "exposure-s3-bucket.md#s3-bucket-reachability-access-point-public-access")

- [Sensitive data traits for Amazon S3 buckets](exposure-s3-bucket.md#sensitive-data "exposure-s3-bucket.md#sensitive-data")
  - [Sensitive data traits for Amazon S3 buckets](exposure-s3-bucket.md#sensitive-data-present "exposure-s3-bucket.md#sensitive-data-present")

## Misconfiguration traits for Amazon S3 buckets

Here are misconfiguration traits for Amazon S3 buckets and suggested remediation steps.

### The Amazon S3 bucket has versioning disabled

Amazon S3 Versioning helps you keep multiple variants of an object in the same bucket.
When versioning is disabled, Amazon S3 stores only the most recent version of each object, meaning that if objects are accidentally or maliciously deleted or overwritten, they cannot be recovered.
Versioning-enabled buckets provide protection against accidental deletion, application failures, and security incidents like ransomware attacks, where unauthorized modification or deletion of data could occur.
Following security best practices, we recommend enabling versioning for buckets containing important data that would be difficult or impossible to recreate if lost.

1. **Enable versioning** –

To enable Amazon S3 Versioning on a bucket, see [Enabling versioning on buckets](../../../AmazonS3/latest/userguide/manage-versioning-examples.md "../../../AmazonS3/latest/userguide/manage-versioning-examples.md") in the _Amazon Simple Storage Service User Guide_.
When enabling versioning, consider implementing lifecycle rules to manage storage, as versioning will maintain multiple copies of objects.

### The Amazon S3 bucket has Object Lock disabled

Amazon S3 Object Lock provides a write-once-read-many (WORM) model for Amazon S3 objects, preventing them from being deleted or overwritten for a fixed period or indefinitely.
When Object Lock is disabled, your objects could be vulnerable to accidental or malicious deletion, modification, or encryption by ransomware.
Object Lock is especially important for compliance with regulatory requirements that demand immutable data storage and for protection against sophisticated threats like ransomware that may attempt to encrypt your data.
By enabling Object Lock, you can enforce retention policies as an added layer of data protection and create an immutable backup strategy for your critical data.
Following security best practices, we recommend you enable Object Lock to prevent malicious modification of your objects.

1. Note that Object Lock can only be enabled when creating a new bucket, so you will need to create a new bucket with Object Lock enabled.
   For large migrations, consider using Batch Operations to copy objects to the new bucket.
   Before you lock any objects, you must also enable Amazon S3 Versioning and Object Lock on a bucket.
   Since Object Lock can only be enabled on new buckets, you’ll need to migrate existing data to a new bucket with Object Lock enabled.
   **Configure Amazon S3 Object Lock** –
   For information about how to configure Object Lock on a bucket, see [ConfiguringAmazon S3Object Lock](../../../AmazonS3/latest/userguide/object-lock-configure.md "../../../AmazonS3/latest/userguide/object-lock-configure.md") in the _Amazon Simple Storage Service User Guide_.
   After setting up Object Lock, choose an appropriate retention mode according to your environment.

### Amazon S3 bucket is not encrypted at rest with AWS KMS keys

Amazon S3 applies server-side encryption with Amazon S3 managed keys as the default level of encryption for all new buckets.
While Amazon S3 managed keys provides strong encryption protection, it doesn't offer the same level of access control and audit capabilities as AWS Key Management Service keys.
When using KMS keys, access to objects requires permissions to both the Amazon S3 bucket and the KMS key that encrypted the object.
This is particularly important for sensitive data where you need granular control over who can access the encrypted objects and comprehensive audit logging of encryption key usage.
Following security best practices, we recommend using KMS keys to encrypt buckets containing sensitive data or for environments with strict compliance requirements.

1. **Configure Amazon S3 bucket key**

To configure a bucket to use an Amazon S3 bucket key for new objects, see [Configuring your bucket to use an Amazon S3 Bucket Key with SSE-KMS for new objects](../../../AmazonS3/latest/userguide/configuring-bucket-key.md "../../../AmazonS3/latest/userguide/configuring-bucket-key.md") in the _Amazon Simple Storage Service User Guide_.
For information about how to encrypt an existing object, see [Encrypting objects with Amazon S3 Batch Operations](https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations/ "https://aws.amazon.com/blogs/storage/encrypting-objects-with-amazon-s3-batch-operations/") in the AWS Storage Blog.

When implementing AWS KMS encryption, consider the following:

- **Key management** –
  Decide on whether to use an AWS managed key or a customer managed key (CMK).
  CMKs offer customers full control over the lifecycle and usage of their keys.
  For more information on the difference between these two types of keys, see [AWS KMS keys](../../../kms/latest/developerguide/concepts.md#key-mgmt "../../../kms/latest/developerguide/concepts.md#key-mgmt") in the _AWS Key Management Service Developer Guide_.
- **Key rotation** –
  For additional security measures, enable automatic key rotation for your KMS keys.
  For more information, see Enable automatic key rotation in the _AWS Key Management Service Developer Guide_.

### Multi-factor authentication (MFA) delete is disabled on a versioned Amazon S3 bucket

Multi-factor authentication (MFA) delete provides an additional layer of security for your Amazon S3 bucket.
It requires multi-factor authentication for destructive Amazon S3 operations.
When MFA delete is disabled, users with appropriate permissions can permanently delete object versions or suspend versioning on your bucket without additional authentication challenges.
Enabling MFA delete helps protect against unauthorized or accidental deletion of your data, providing enhanced protection against ransomware attacks, insider threats, and operational errors.
MFA delete is particularly valuable for buckets containing critical or compliance-sensitive data that must be protected from unauthorized deletion.
Following security best practices, we recommend enabling MFA for your Amazon S3 buckets.

1. **Review MFA types**

AWS supports the following [MFA types](../../../IAM/latest/UserGuide/id_credentials_mfa.md#id_credentials_mfa-types "../../../IAM/latest/UserGuide/id_credentials_mfa.md#id_credentials_mfa-types").
Although authentication with a physical device typically provides more stringent security protection, using any type of MFA is more secure than having MFA disabled. 2. **Enforce MFA at the resource policy level**

Use the `aws:MultiFactorAuthAge` condition key in a bucket policy to require MFA for sensitive operations.
For more information, see see [Requiring MFA](../../../AmazonS3/latest/userguide/example-bucket-policies.md#example-bucket-policies-MFA "../../../AmazonS3/latest/userguide/example-bucket-policies.md#example-bucket-policies-MFA") in the _Amazon Simple Storage Service User Guide_. 3. **Enable MFA**

To enable MFA delete, first, ensure that versioning is enabled on your Amazon S3 bucket.
MFA delete is only supported on buckets that have versioning enabled.
For information about how to enable Amazon S3 versioning, see [Enabling versioning on buckets](../../../AmazonS3/latest/userguide/manage-versioning-examples.md "../../../AmazonS3/latest/userguide/manage-versioning-examples.md") in the _Amazon Simple Storage Service User Guide_.
MFA delete cannot be enabled through the Amazon S3 console.
You must use the Amazon S3 API or the AWS CLI.
For more information, see [Configuring MFA delete](../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md "../../../AmazonS3/latest/userguide/MultiFactorAuthenticationDelete.md") in the _Amazon Simple Storage Service User Guide_.

### The Amazon S3 bucket allows principals from other AWS accounts to modify bucket permissions

Amazon S3 bucket policies control access to buckets and objects.
When bucket policies allow principals from other AWS accounts to modify bucket permissions, unauthorized users can reconfigure your bucket.
If external principal credentials are compromised, unathorized users can gain control over your bucket, leading to data breaches or service disruptions.
Following standard security principles, AWS recommends that you restrict permission management actions to trusted principals only.

1. **Review and identify bucket policies**

In the the exposure, identify the Amazon S3 bucket in the ARN field.
In the Amazon S3 console, select the bucket, and navigate to the **Permissions** tab to review the bucket policy.
Review the permissions policy attached to the bucket.
Look for policy statements that grant actions like `s3:PutBucketPolicy, s3:PutBucketAcl, s3:DeleteBucketPolicy, s3:*` or policy statements that allow access to principals outside your account, as denoted in the principal statement. 2. **Modify the bucket policy**

Modify the bucket policy to remove or restrict actions granted to other AWS accounts:

    * Remove policy statements that grant external accounts permission management actions.
    * If cross-account access is required, replace broad permissions `(s3:*)` with specific actions that don't include bucket permission management.

For information about modifying a bucket policy, see [Adding a bucket policy by using the Amazon S3 console](../../../AmazonS3/latest/userguide/add-bucket-policy.md "../../../AmazonS3/latest/userguide/add-bucket-policy.md") in the _Amazon S3 User Guide_.

## Reachability traits for Amazon S3 buckets

Here are reachability traits for Amazon S3 buckets and suggested remediation steps.

### Amazon S3 bucket has public access

By default, Amazon S3 buckets and objects are private, but they can be made public through various
configurations. If you modify bucket policies, access point policies, or object permissions to allow public access,
you risk exposing sensitive data.

1. **Assess bucket**

Assess whether your bucket can be made private based on your organizational policy, compliance
requirements, or data classification. If you didn't intend to grant bucket access to the public or other AWS accounts,
follow the remaining remediation instructions. 2. **Configure the bucket to be private**

Choose one of the following options to configure private access for your Amazon S3 bucket:

    * **Account level** – To block public access for all buckets in your account using account-level settings, see [Configuring block public access settings for your account](../../../AmazonS3/latest/userguide/configuring-block-public-access-account.md "../../../AmazonS3/latest/userguide/configuring-block-public-access-account.md") in the
     *Amazon Simple Storage Service User Guide*.
    * **Bucket level** –To block public access for a specific bucket, see [Configuring block public access settings for yourAmazon S3buckets](../../../AmazonS3/latest/userguide/configuring-block-public-access-bucket.md "../../../AmazonS3/latest/userguide/configuring-block-public-access-bucket.md") in the
     *Amazon Simple Storage Service User Guide*.
    * **Bucket ACL or policies** –To modify the bucket access control list (ACL), bucket policy, Multi-Region Access Point (MRAP) policy, or
     access point policy to remove public access to the bucket, see [Reviewing and changing bucket access](../../../AmazonS3/latest/userguide/access-analyzer.md#changing-bucket-access "../../../AmazonS3/latest/userguide/access-analyzer.md#changing-bucket-access") in the
     *Amazon Simple Storage Service User Guide*. If you block public access at the account level or bucket level, those blocks
     take precedence over a policy that permits public access.

### The Amazon S3 bucket has public read access

Amazon S3 buckets with public read access allow anyone on the internet to view the contents of your bucket.
While this may be necessary for publicly accessible websites or shared resources, it can create security risks if the bucket contains sensitive data.
Public read access can lead to unauthorized viewing and downloading, which can lead to data breaches if sensitive data is stored in those buckets.
Following standard security principles, AWS recommends restricting access to Amazon S3 buckets to necessary users and systems.

1. **Block public access at the bucket level**

Amazon S3 provides Block Public Access settings that can be configured at both the bucket and account levels to prevent public access regardless of bucket policies or ACLs.
For more information, see [Blocking public access to your Amazon S3 storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") in the _Amazon Simple Storage Service User Guide_.
After blocking public access, review your bucket access control configuration to make sure it aligns with your access requirements.
Then review your Amazon S3 bucket policy to explicitly define who can access your bucket.
For examples of bucket policies see [Examples of Amazon S3 bucket policies](../../../AmazonS3/latest/userguide/example-bucket-policies.md "../../../AmazonS3/latest/userguide/example-bucket-policies.md") in the _Amazon Simple Storage Service User Guide_. 2. **Alternative access methods**

If public read access is required, consider these more secure alternatives:

    * **CloudFront** –
     Use CloudFront with an Origin Access Identity (OAI) or Origin Access Control (OAC) to allow read access from a private Amazon S3 bucket.
     This alternative restricts direct access to your Amazon S3 bucket while allowing content to be publicly accessible through CloudFront.
     For more information, see [Restricting access to an Amazon Amazon S3 origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") in the *Amazon CloudFront Developer Guide*.
    * **Presigned URLs** –
     Use presigned URLs for temporary access to specific objects.
     For more information, see [Sharing objects with presigned URLs](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") in the *AWSAmazon S3User Guide*.

### The Amazon S3 bucket has write access

Amazon S3 buckets with public write access allow anyone on the internet to upload, modify, or delete objects in your bucket.
This creates significant security risks, including the potential for someone to upload malicious files, modify existing files, and delete data.
Public write access creates security vulnerabilities that can be exploited by attackers.
Following standard security principles, AWS recommends restricting write access to your Amazon S3 buckets to only necessary users and systems.

1. **Block public access at the account and bucket level**

Amazon S3 provides block public access settings that can be configured at both the bucket and account levels to prevent public access regardless of bucket policies or ACLs.
For more information, see [Blocking public access to your Amazon S3 storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") in the _Amazon Simple Storage Service User Guide_. 2. **Modify bucket policies**

For a more granular approach to remove public write access, review the bucket policy.
You can look for `s3:PutObject`, `s3:DeleteObject`, or `s3:*`.
For more information on managing bucket policies, see [Bucket policies for Amazon S3](../../../AmazonS3/latest/userguide/bucket-policies.md "../../../AmazonS3/latest/userguide/bucket-policies.md") in the _Amazon Simple Storage Service User Guide_. 3. **Alternative access methods**
If public read access is required, consider these more secure alternatives:

    * **CloudFront** –
     Use CloudFront with an Origin Access Identity (OAI) or Origin Access Control (OAC) to allow read access from a private Amazon S3 bucket.
     This alternative restricts direct access to your Amazon S3 bucket while allowing content to be publicly accessible through CloudFront.
     For more information, see [Restricting access to an Amazon S3 origin](../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md "../../../AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.md") in the *Amazon CloudFront Developer Guide*.
    * **Presigned URLs** –
     Use presigned URLs for temporary access to specific objects.
     For more information, see [Sharing objects with presigned URLs](../../../AmazonS3/latest/userguide/ShareObjectPreSignedURL.md "../../../AmazonS3/latest/userguide/ShareObjectPreSignedURL.md") in the *Amazon Simple Storage Service User Guide*.

### The Amazon S3 access point has public access settings enabled

Amazon S3 access points provide customized access to shared datasets in Amazon S3 buckets.
When you enable public access for an access point, anyone on the internet to access to your data.
Following standard security principles, AWS recommends restricting public access to Amazon S3 access points.

1. **Create a new access point with block public access enabled**

Amazon S3 doesn't support changing an access point’s public access settings after an access point has been created.
For information about creating an access point, see [Managing public access to access points for general purpose buckets](../../../AmazonS3/latest/userguide/creating-access-points.md "../../../AmazonS3/latest/userguide/creating-access-points.md") in the _Amazon S3 User Guide_.
For more information about managing public access to access points, see [Creating access points for general purpose buckets](../../../AmazonS3/latest/userguide/access-points-bpa-settings.md "../../../AmazonS3/latest/userguide/access-points-bpa-settings.md") in the _Amazon S3 User Guide_.

## Sensitive data traits for Amazon S3 buckets

Here are the sensitive data traits for Amazon S3 buckets and suggested remediation steps.

### Sensitive data traits for Amazon S3 buckets

When Macie identifies sensitive data in your Amazon S3 buckets, it indicates potential security and compliance exposures that require immediate attention.

Sensitive data can include:

- Credentials
- Personally identifiable information
- Financial information
- Confidential content requiring protection

If sensitive data is exposed through misconfiguration or unauthorized access, it could lead to compliance violations, data breaches, identity theft, or financial loss.
Following security best practices, AWS recommends proper classification of data and continuous monitoring of sensitive data in your Amazon S3 buckets.

###### Implement controls for sensitive data

In the exposure finding, choose the **Open resource** .
Review the type of sensitive data detected and its location in the bucket.
For help interpreting Macie findings, see [Types of Macie findings](../../../macie/latest/user/findings-types.md "../../../macie/latest/user/findings-types.md") in the _Amazon Macie User Guide_.

Based on the type of sensitive data discovered, implement the appropriate security controls:

- **Restrict access to the bucket** – Review bucket permissions to make sure they follow the principle of least privilege.
  Use IAM policies, bucket policies, and ACLs to restrict access.
  For more information, see [Identity and Access Management for Amazon S3](../../../AmazonS3/latest/userguide/security-iam.md "../../../AmazonS3/latest/userguide/security-iam.md") in the _Amazon Simple Storage Service User Guide_.
- **Enable server-side encryption** – Enable server-side encryption with KMS keys keys for additional protection.
  For more information, see [Using server-side encryption with AWS KMS keys (SSE-KMS)](../../../AmazonS3/latest/userguide/UsingKMSEncryption.md "../../../AmazonS3/latest/userguide/UsingKMSEncryption.md") in the _Amazon Simple Storage Service User Guide_.
- **Use AWS Glue DataBrew** – Use Glue DataBrew for data preparation and cleaning.
  For more information, see[What is AWS Glue DataBrew](../../../databrew/latest/dg/what-is.md "../../../databrew/latest/dg/what-is.md") in the _AWS Glue DataBrew Developer Guide_.
