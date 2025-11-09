AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Data protection in AWS Systems Manager

Data protection refers to protecting data while _in
transit_ (as it travels to and from Systems Manager) and _at rest_ (while it's stored in AWS data centers).

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Systems Manager. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Systems Manager or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Data encryption

### Encryption at rest

###### Parameter Store parameters

The types of parameters you can create in Parameter Store, a tool in AWS Systems Manager,
include `String`, `StringList`, and
`SecureString`.

All parameters, regardless of their type, are encrypted both in transit and at
rest. In transit, parameters are encrypted using transport layer security (TLS)
to create a secure HTTPS connection for API requests. At rest, they are
encrypted with an AWS owned key in AWS Key Management Service (AWS KMS). For more information
about AWS owned key encryption, see [AWS owned keys](../../../kms/latest/developerguide/concepts.md#aws-owned-cmk "../../../kms/latest/developerguide/concepts.md#aws-owned-cmk") in the _AWS Key Management Service Developer Guide_
.

The `SecureString` type offers additional encryption options and is
recommended for all sensitive data. You can choose from the following types of
AWS KMS keys to encrypt and decrypt the value of a `SecureString`
parameter:

- The AWS managed key for your account
- A customer managed key (CMK) that you have created in your account
- A CMK in another AWS account that has been shared with you

For more information about AWS KMS encryption, see the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide.md "../../../kms/latest/developerguide.md").

###### Content in S3 buckets

As part of your Systems Manager operations, you might choose to upload or
store data in one or more Amazon Simple Storage Service (Amazon S3) buckets.

For information about S3 bucket encryption, see [Protecting data using
encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md") and [Data protection in
Amazon S3](../../../AmazonS3/latest/userguide/DataDurability.md "../../../AmazonS3/latest/userguide/DataDurability.md") in the _Amazon Simple Storage Service User Guide_.

The following are types of data you can upload or have stored in S3 buckets as
part of your Systems Manager activities:

- The output of commands in Run Command, a tool in AWS Systems Manager
- Packages in Distributor, a tool in AWS Systems Manager
- Patching operation logs in Patch Manager, a tool in AWS Systems Manager
- Patch Manager patch override lists
- Scripts or Ansible Playbooks to run in a
  runbook workflow in Automation, a tool in AWS Systems Manager
- Chef InSpec profiles for use with scans in Compliance,
  a tool in AWS Systems Manager
- AWS CloudTrail logs
- Session history logs in Session Manager, a tool in AWS Systems Manager
- Reports from Explorer, a tool in AWS Systems Manager
- OpsData from OpsCenter, a tool in AWS Systems Manager
- AWS CloudFormation templates for use with Automation workflows
- Compliance data from a resource data sync scan
- Output of requests to create or edit association in State Manager, a tool
  in AWS Systems Manager, on managed nodes
- Custom Systems Manager documents (SSM documents) that you can run using the
  AWS managed SSM document `AWS-RunDocument`

###### CloudWatch Logs log groups

As part of your Systems Manager operations, you might choose to stream data
to one or more Amazon CloudWatch Logs log groups.

For information about CloudWatch Logs log group encryption, see [Encrypt log
data in CloudWatch Logs using AWS Key Management Service](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md") in the
_Amazon CloudWatch Logs User Guide_.

The following are types of data you might have streamed to a CloudWatch Logs log group
as part of your Systems Manager activities:

- The output of Run Command commands
- The output of scripts run using the `aws:executeScript`
  action in an Automation runbook
- Session Manager session history logs
- Logs from SSM Agent on your managed nodes

### Encryption in transit

We recommend that you use an encryption protocol such as Transport Layer
Security (TLS) to encrypt sensitive data in transit between clients and your
nodes.

Systems Manager provides the following support for encryption of your data in
transit.

**Connections to Systems Manager API endpoints**

Systems Manager API endpoints only support secure connections over
HTTPS. When you manage Systems Manager resources with the AWS Management Console,
AWS SDK, or the Systems Manager API, all communication is encrypted
with Transport Layer Security (TLS). For a full list of API
endpoints, see [AWS service
endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md") in the _Amazon Web Services General Reference_.

**Managed instances**

AWS provides secure and private connectivity between Amazon Elastic Compute Cloud
(Amazon EC2) instances. In addition, we automatically encrypt in-transit
traffic between supported instances in the same virtual private
cloud (VPC) or in peered VPCs, using AEAD algorithms with 256-bit
encryption. This encryption feature uses the offload capabilities of
the underlying hardware, and there is no impact on network
performance. The supported instances are: C5n, G4, I3en, M5dn, M5n,
P3dn, R5dn, and R5n.

**Session Manager sessions**

By default, Session Manager uses TLS 1.3 to encrypt session data
transmitted between the local machines of users in your account and
your EC2 instances. You can also choose to further encrypt the data
in transit using an AWS KMS key that has been created in AWS KMS.
AWS KMS encryption is available for `Standard_Stream`,
`InteractiveCommands`, and
`NonInteractiveCommands` session types.

**Run Command access**

By default, remote access to your nodes using Run Command is
encrypted using TLS 1.3, and requests to create a connection are
signed using SigV4.

## Internetwork traffic privacy

You can use Amazon Virtual Private Cloud (Amazon VPC) to create boundaries between resources in your
managed nodes and control traffic between them, your on-premises network, and the
internet. For details, see [Improve the security of EC2 instances by using VPC endpoints for Systems Manager](setup-create-vpc.md "setup-create-vpc.md").

For more information about Amazon Virtual Private Cloud security, see [Internetwork traffic privacy in
Amazon VPC](../../../vpc/latest/userguide/VPC_Security.md "../../../vpc/latest/userguide/VPC_Security.md") in the _Amazon VPC User Guide_.
