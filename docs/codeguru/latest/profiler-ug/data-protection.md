# Data protection for CodeGuru Profiler

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Amazon CodeGuru Profiler (CodeGuru Profiler). As described in this model, AWS is
responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are
responsible for maintaining control over your content that is hosted on this infrastructure. This content includes the security configuration and management tasks for the AWS services that you use.
For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq "https://aws.amazon.com/compliance/data-privacy-faq").

For data protection purposes, we recommend that you protect AWS account credentials and
set up individual user accounts with AWS Identity and Access Management (IAM). That way each user is given only the
permissions necessary to fulfill their job duties. We also recommend that you secure your data
in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources.
- Set up API and user activity logging with AWS CloudTrail.
- Use AWS encryption solutions, along with all default security controls within AWS
  services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing personal data that is stored in Amazon S3.
  We strongly recommend that you never put sensitive identifying information, such as your
  customers' account numbers, into free-form fields such as a **Name** field. This includes when you work with CodeGuru Profiler or other AWS
  services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  CodeGuru Profiler or other services might get picked up for inclusion in diagnostic logs. When you
  provide a URL to an external server, don't include credentials information in the URL to
  validate your request to that server.

###### Topics

- [Captured data in CodeGuru Profiler](#data-captured "#data-captured")
- [Data encryption in CodeGuru Profiler](#data-encryption "#data-encryption")
- [Data retention in CodeGuru Profiler](#data-retention "#data-retention")
- [Internetwork Traffic Privacy](#security-inter-network-privacy "#security-inter-network-privacy")

## Captured data in CodeGuru Profiler

The CodeGuru Profiler agent collects stack traces at regular intervals using either the Java virtual
machine or Python interfaces. The data is submitted in batches to CodeGuru Profiler.

A stack trace is a sequence of names of functions or methods in execution, followed by
the names of functions or methods that called them successively, continuing to the root of the
service process. The CodeGuru Profiler profiling agent doesn't have access to the names or values of
function parameters. It also doesn't have access to the values of variables or application
data.

## Data encryption in CodeGuru Profiler

Encryption is an important part of CodeGuru Profiler security. Data in transit and at rest are
provided by default and don't require you to do anything.

- **Encryption of data at rest** - Data collected by CodeGuru Profiler is
  stored using Amazon S3, Amazon Kinesis, and Amazon DynamoDB and their data-at-rest encryption capabilities.
- **Encryption of data in transit** - All communication between
  customers and CodeGuru Profiler and between CodeGuru Profiler and its downstream dependencies is protected using
  TLS connections that are signed using the Signature Version 4 signing process. All CodeGuru Profiler
  endpoints use SHA-256 certificates that are managed by AWS Private Certificate Authority. For more information,
  see [Signature Version 4 Signing
  Process](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md") and [What is ACM PCA](../../../privateca/latest/userguide.md "../../../privateca/latest/userguide.md").

## Data retention in CodeGuru Profiler

Data received from an agent is aggregated into proﬁles representing ﬁve-minute periods.
These are then aggregated into hourly and daily proﬁles. CodeGuru Profiler currently retains ﬁve-minute,
hourly, and daily proﬁles for 15 days, 60 days, and three years, respectively.

## Internetwork Traffic Privacy

An Amazon Virtual Private Cloud (Amazon VPC) endpoint for CodeGuru Profiler is a logical entity within a VPC that allows
connectivity only to CodeGuru Profiler. Amazon VPC routes requests to CodeGuru Profiler and routes responses back to the
VPC. For more information, see [VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the _Amazon
VPC User Guide_. For information about using Amazon VPC endpoints with CodeGuru Profiler see [Using CodeGuru Profiler with VPC Endpoints](private-link.md "private-link.md").
