# Security in Amazon Braket

Cloud security at AWS is the highest priority. As an AWS customer, you benefit from data
centers and network architectures that are built to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes this as security
_of_ the cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is responsible for protecting the
  infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use
  securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that apply to Amazon Braket, see [AWS Services in Scope by Compliance
  Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You are also responsible for other factors
  including the sensitivity of your data, your company's requirements, and applicable laws and
  regulations.
  This documentation helps you understand how to apply the shared responsibility model when
  using Braket. The following topics show you how to configure Braket to meet your
  security and compliance objectives. You also learn how to use other AWS services that help you
  to monitor and secure your Braket resources.

###### In this section:

- [Shared responsibility for security](#braket-shared-security "#braket-shared-security")
- [Data protection](#braket-data-protection "#braket-data-protection")
- [Data retention](#braket-data-retention "#braket-data-retention")
- [Managing access to Amazon Braket](braket-manage-access.md "braket-manage-access.md")
- [Amazon Braket service-linked role](braket-slr.md "braket-slr.md")
- [Compliance validation for Amazon Braket](compliance-validation.md "compliance-validation.md")
- [Infrastructure Security in Amazon Braket](infrastructure-security.md "infrastructure-security.md")
- [Security of Amazon Braket Hardware Providers](third-party-security.md "third-party-security.md")
- [Amazon VPC endpoints for Amazon Braket](braket-privatelink.md "braket-privatelink.md")

## Shared responsibility for security

Security is a shared responsibility between AWS and you. The
[shared responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/ "http://aws.amazon.com/compliance/shared-responsibility-model/")
describes this as security _of_ the cloud and security _in_ the cloud:

- **Security of the cloud** – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](http://aws.amazon.com/compliance/programs/ "http://aws.amazon.com/compliance/programs/"). To learn about the compliance programs that apply to Amazon Braket, see [AWS Services in Scope by Compliance Program](http://aws.amazon.com/compliance/services-in-scope/ "http://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – You are responsible for maintaining control over your content that is hosted on this AWS infrastructure. This content includes the security configuration and management tasks for the AWS services that you use.

## Data protection

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Amazon Braket. As described in this model, AWS is
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
customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Amazon Braket or other AWS services
using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
provide a URL to an external server, we strongly recommend that you do not include credentials
information in the URL to validate your request to that server.

## Data retention

After 90 days, Amazon Braket automatically removes all quantum task IDs and other
metadata associated with your quantum tasks. As a result of this data retention policy,
these tasks and results are no longer retrievable by search from the Amazon Braket
console, although they remain stored in your S3 bucket.

If you need access to historical quantum tasks and results that are stored in your
S3 bucket for longer than 90 days, you must keep a separate record of your task ID
and other metadata associated with that data. Be sure to save the information prior
to 90 days. You can use that saved information to retrieve the historical data.
