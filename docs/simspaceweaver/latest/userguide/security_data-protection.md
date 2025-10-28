End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Data protection in AWS SimSpace Weaver

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS SimSpace Weaver. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with SimSpace Weaver or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Encryption at rest

Data is considered _at rest_ when it is located in non-volatile
(persistent) data storage, such as a disk. Data located in volatile data storage,
such as memory and registers, is not considered to be _at rest_.

When you use SimSpace Weaver, the only data at rest are:

- Apps and schemas that you upload to Amazon Simple Storage Service (Amazon S3)
- Simulation log data stored in Amazon CloudWatch

Other data that SimSpace Weaver uses internally doesn't persist after you stop your simulation.

To learn how to encrypt your data at rest, see:

- [Encrypt your data in Amazon S3](../../../AmazonS3/latest/userguide/bucket-encryption.md "../../../AmazonS3/latest/userguide/bucket-encryption.md")
- [Encrypt your log data](../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md "../../../AmazonCloudWatch/latest/logs/encrypt-log-data-kms.md")

## Encryption in transit

Your connections to the SimSpace Weaver API through the AWS Command Line Interface (AWS CLI), AWS SDK, and SimSpace Weaver app SDK,
use TLS encryption with the
[Signature Version 4 signing process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md").
AWS manages authentication using the IAM-defined access policies for the security credentials you use to connect.

Internally, SimSpace Weaver uses TLS to connect to other AWS services that it uses.

###### Important

Communications between your apps and their clients don't involve SimSpace Weaver.
It's your responsibility to encrypt communications with simulation clients, if required.
We recommend that you create a solution to encrypt all data in transit across client connections.

To learn more about AWS services that can support your encryption solutions,
see [the AWS Security Blog](https://aws.amazon.com/blogs/security/importance-of-encryption-and-how-aws-can-help/ "https://aws.amazon.com/blogs/security/importance-of-encryption-and-how-aws-can-help/").

## Inter-network traffic privacy

SimSpace Weaver compute resources reside within 1 Amazon VPC shared by all SimSpace Weaver customers. All internal
SimSpace Weaver service traffic stays within the AWS network and doesn't travel across the internet. Communication
between simulation clients and your apps travels across the internet.
