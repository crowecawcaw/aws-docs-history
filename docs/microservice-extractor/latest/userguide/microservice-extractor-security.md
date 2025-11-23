AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/ "https://aws.amazon.com/transform/"), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# AWS Microservice Extractor for .NET security

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from
data centers and network architectures that are built to meet the requirements of the most
security-sensitive organizations. Security is a shared responsibility between AWS and you.
The [shared
responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security of the cloud and security in the
cloud:

- **Security of the cloud** – AWS is responsible for
  protecting the infrastructure that runs AWS services in the AWS Cloud. AWS
  also provides you with services that you can use securely. Third-party auditors
  regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/").
  For more information about the compliance programs that apply to Microservice Extractor, see
  [AWS Services in
  Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You are also responsible for other
  factors including the sensitivity of your data, your company’s requirements, and
  applicable laws and regulations.
  This documentation helps you understand how to apply the shared responsibility model when
  using AWS Microservice Extractor for .NET. The following topics show you how to configure Microservice Extractor to meet
  your security and compliance objectives. You also learn how to use other AWS services that
  help you to monitor and secure your Microservice Extractor resources.

###### Security topics

- [Data protection in
  AWS Microservice Extractor for .NET](#microservice-extractor-data-protection "#microservice-extractor-data-protection")
- [Identity and Access Management in
  AWS Microservice Extractor for .NET](#microservice-extractor-security-iam "#microservice-extractor-security-iam")
- [Configuration and vulnerability analysis in AWS Microservice Extractor for .NET](#microservice-extractor-configuration-vulnerability-analysis "#microservice-extractor-configuration-vulnerability-analysis")
- [Security best
  practices](#microservice-extractor-security-best-practices "#microservice-extractor-security-best-practices")

## Data protection in

AWS Microservice Extractor for .NET

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Microservice Extractor for .NET. As described in this model, AWS is
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
customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Microservice Extractor or other AWS services
using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
provide a URL to an external server, we strongly recommend that you do not include credentials
information in the URL to validate your request to that server.

###### Encryption at rest

Microservice Extractor stores data in two locations. The first one is the working directory for
Microservice Extractor on your local system. The data stored here is not encrypted at rest. The
second is the Amazon S3 bucket you have configured in Microservice Extractor where source code
metadata is stored for analysis. This location is encrypted at rest as follows.

Microservice Extractor automatically enables server-side encryption with Amazon managed keys for
new object uploads.

Unless you specify otherwise, objects use SSE-S3 by default to encrypt objects.
However, you can choose to configure the service to use server-side encryption with
AWS Key Management Service (AWS KMS) keys (SSE-KMS) instead. For more information,
see [Specifying
server-side encryption with AWS KMS (SSE-KMS)](../../../AmazonS3/latest/userguide/specifying-kms-encryption.md "../../../AmazonS3/latest/userguide/specifying-kms-encryption.md") in S3 User Guide.

AWS KMS is a service that combines secure, highly available hardware and software
to provide a key management system scaled for the cloud. Microservice Extractor uses server-side
encryption with AWS KMS (SSE-KMS) to encrypt your data. Also, when SSE-KMS is
requested for the object, the object checksum as part of the object's metadata, is
stored in encrypted form. For more information about checksum, see [Checking object integrity](../../../AmazonS3/latest/userguide/checking-object-integrity.md "../../../AmazonS3/latest/userguide/checking-object-integrity.md") in S3 User Guide.

If you use KMS keys, you can use AWS KMS through the AWS Management Console or
the AWS KMS API to centrally create, view, edit, monitor, enable or disable, rotate,
and schedule deletion of KMS keys, and define the policies that control how and by whom
KMS keys can be used.

Audit their usage to prove that they are being used correctly. Auditing is supported
by the AWS KMS API, but not by the AWS KMS management console.

The security controls in AWS KMS can help you meet encryption-related compliance
requirements. You can use these KMS keys to protect your data in Microservice Extractor. When you
use SSE-KMS encryption, the AWS KMS keys must be in the same Region as selected in the
tool.

There are additional charges for using AWS KMS keys. For more information, see
[AWS KMS
key concepts](../../../kms/latest/developerguide/concepts.md "../../../kms/latest/developerguide/concepts.md") in the AWS Key Management Service Developer Guide and [AWS KMS pricing](https://aws.amazon.com//kms/pricing/ "https://aws.amazon.com//kms/pricing/").

###### Encryption in transit

Microservice Extractor makes requests to the server over the Transport Layer Security
protocol (TLS).

###### AWS CloudTrail and Microservice Extractor APIs

If you use CloudTrail, you may find that your CloudTrail logs contain API calls
related to Microservice Extractor. These calls are:

- StartGroupingAssessment
- CancelGroupingAssessment
- GetGroupingAssessment

### Data collected by

AWS Microservice Extractor for .NET

You can choose to share data when you first set up the Microservice Extractor application.
You have the option to turn off usage data sharing by clearing the check box for
usage data sharing on the AWS Microservice Extractor for .NET **Settings** page .

When usage data sharing is turned on, Microservice Extractor collects the following
information when you onboard your source code:

- Success/failure operations performed during onboarding, static code
  analysis, application build, and graph creation.
- Resources consumed during operations, such as CPU and memory usage.
- Number of nodes and dependencies.
- Number of detected islands.
- Project type, as indicated by the project GUID and the presence of files
  having known extensions.
- Programming language used.
- Presence of code that likely implements user-interface, data access,
  and/or service components

Microservice Extractor doesn’t collect proprietary information, such as source code. In the
case of failure, the tool may collect stack traces to improve product
experience.

## Identity and Access Management in

AWS Microservice Extractor for .NET

AWS Identity and Access Management (IAM) is an AWS service that helps an administrator securely control
access to AWS resources. AWS Microservice Extractor for .NET is a standalone application that does not
require IAM access control to use resources.

To use Microservice Extractor, you your user must have the correct permissions. These permissions
are provided in the [Prerequisites](microservice-extractor-prerequisites.md "microservice-extractor-prerequisites.md") section of this guide.

## Configuration and vulnerability analysis in AWS Microservice Extractor for .NET

When AWS Microservice Extractor for .NET requires updates, you are notified and must install the latest
version of the application upon restart. You maintain the system patching
responsibility, per the [shared responsibility
model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/").

## Security best

practices

AWS Microservice Extractor for .NET provides security features to consider as you develop and implement
your own security policies. The following best practice is a general guideline and
doesn’t represent a complete security solution. Because this best practice might not be
appropriate or sufficient for your environment, treat it as a helpful consideration
rather than a prescription.

###### Implement least privilege access

When you attach the [IAM](#microservice-extractor-security-iam "#microservice-extractor-security-iam")
policies as inline policies to your IAM user, grant only the permissions that are
required to perform the specified task. Implementing least privilege access is
fundamental in reducing security risk and the impact that could result from errors
or malicious intent.
