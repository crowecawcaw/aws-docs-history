# Data protection in AWS ParallelCluster

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS ParallelCluster. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS ParallelCluster or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data encryption

A key feature of any secure service is that information is encrypted when it is not being actively used.

### Encryption at rest

AWS ParallelCluster does not itself store any customer data other than the credentials it needs to interact with
the AWS services on the user's behalf.

For data on the nodes in the cluster, data can be encrypted at rest.

For Amazon EBS volumes, encryption is configured using the
[EbsSettings](SharedStorage-v3.md#SharedStorage-v3-EbsSettings "SharedStorage-v3.md#SharedStorage-v3-EbsSettings")/`Encrypted`
and [EbsSettings](SharedStorage-v3.md#SharedStorage-v3-EbsSettings "SharedStorage-v3.md#SharedStorage-v3-EbsSettings")/`KmsKeyId` settings in the [EbsSettings](SharedStorage-v3.md#SharedStorage-v3-EbsSettings "SharedStorage-v3.md#SharedStorage-v3-EbsSettings") section. For more information,
see [Amazon EBS encryption](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md") in the
Amazon EC2 User Guide.

For Amazon EFS volumes, encryption is configured using the
[EfsSettings](SharedStorage-v3.md#SharedStorage-v3-EfsSettings "SharedStorage-v3.md#SharedStorage-v3-EfsSettings")/`Encrypted`
and [EfsSettings](SharedStorage-v3.md#SharedStorage-v3-EfsSettings "SharedStorage-v3.md#SharedStorage-v3-EfsSettings")/`KmsKeyId` settings in the [EfsSettings](SharedStorage-v3.md#SharedStorage-v3-EfsSettings "SharedStorage-v3.md#SharedStorage-v3-EfsSettings") section. For more information, see [How encryption
at rest works](../../../efs/latest/ug/encryption-at-rest.md#howencrypt "../../../efs/latest/ug/encryption-at-rest.md#howencrypt") in the _Amazon Elastic File System User Guide._

For FSx for Lustre file systems, encryption of data at rest is automatically enabled when creating an Amazon FSx file
system. For more information, see [Encrypting data at rest](../../../fsx/latest/LustreGuide/encryption-at-rest.md "../../../fsx/latest/LustreGuide/encryption-at-rest.md") in the _Amazon FSx for Lustre User Guide_.

For instance types with NVMe volumes, the data on NVMe instance store volumes is encrypted using an XTS-AES-256
cipher implemented on a hardware module on the instance. The encryption keys are generated using the hardware module
and are unique to each NVMe instance storage device. All encryption keys are destroyed when the instance is stopped
or terminated and cannot be recovered. You cannot disable this encryption and you cannot provide your own encryption
key. For more information, see [Encryption at rest](../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-rest "../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-rest") in the
_Amazon EC2 User Guide_.

If you use AWS ParallelCluster to invoke an AWS service that transmits customer data to your local computer for
storage, then refer to the Security and Compliance chapter in that service's User Guide for information on how that
data is stored, protected, and
encrypted.

### Encryption in transit

By default, all data transmitted from the client computer running AWS ParallelCluster and AWS service endpoints
is encrypted by sending everything through a HTTPS/TLS connection. Traffic between the nodes in the cluster can be
automatically encrypted, depending on the instance types selected. For more information, see [Encryption in
transit](../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit "../../../AWSEC2/latest/UserGuide/data-protection.md#encryption-transit") in the
_Amazon EC2 User Guide_.

## See also

- [Data protection in
  Amazon EC2](../../../AWSEC2/latest/UserGuide/data-protection.md "../../../AWSEC2/latest/UserGuide/data-protection.md")
- [Data protection in
  EC2 Image Builder](../../../imagebuilder/latest/userguide/data-protection.md "../../../imagebuilder/latest/userguide/data-protection.md")
- [Data
  protection in CloudFormation](../../../AWSCloudFormation/latest/UserGuide/security-data-protection.md "../../../AWSCloudFormation/latest/UserGuide/security-data-protection.md")
- [Data protection in
  Amazon EFS](../../../efs/latest/ug/efs-backup-solutions.md "../../../efs/latest/ug/efs-backup-solutions.md")
- [Data protection in
  Amazon S3](../../../AmazonS3/latest/dev/DataDurability.md "../../../AmazonS3/latest/dev/DataDurability.md")
- [Data protection in
  FSx for Lustre](../../../fsx/latest/LustreGuide/data-protection.md "../../../fsx/latest/LustreGuide/data-protection.md")
