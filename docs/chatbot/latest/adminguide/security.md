AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Security in Amazon Q Developer in chat applications

At AWS, cloud security is our highest priority. As an AWS customer, you benefit from a
data center and network architecture that we build to meet the requirements of the most
security-sensitive organizations.

Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") describes
this as security _of_ the cloud and security _in_ the
cloud:

- **Security of the cloud** – AWS is responsible for
  protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also
  provides you with services that you can use securely. Third-party auditors regularly test
  and verify our security effectiveness as part of the [AWS compliance programs](https://aws.amazon.com/compliance/programs/ "https://aws.amazon.com/compliance/programs/"). To learn about the
  compliance programs that apply to Amazon Q Developer in chat applications, see [AWS Services in Scope by Compliance
  Program](https://aws.amazon.com/compliance/services-in-scope/ "https://aws.amazon.com/compliance/services-in-scope/").
- **Security in the cloud** – Your responsibility is
  determined by the AWS service that you use. You are also responsible for other factors
  including the sensitivity of your data, your company’s requirements, and applicable laws and
  regulations.
  This documentation helps you understand how to apply the shared responsibility model when
  using Amazon Q Developer in chat applications. The following topics show you how to configure Amazon Q Developer in chat applications to meet your security and
  compliance objectives. You also learn how to use other AWS services that help you to monitor and
  secure your Amazon Q Developer in chat applications resources.

###### Topics

- [Data protection in Amazon Q Developer in chat applications](#per-service-security "#per-service-security")
- [Identity and Access Management for Amazon Q Developer in chat applications](security-iam.md "security-iam.md")
- [Connecting to Amazon Q Developer in chat applications with interface VPC endpoints](vpc.md "vpc.md")
- [Compliance validation for Amazon Q Developer in chat applications](chatbot-compliance.md "chatbot-compliance.md")
- [Resilience in Amazon Q Developer in chat applications](disaster-recovery-resiliency.md "disaster-recovery-resiliency.md")
- [Infrastructure security in Amazon Q Developer in chat applications](infrastructure-security.md "infrastructure-security.md")

## Data protection in Amazon Q Developer in chat applications

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in Amazon Q Developer in chat applications. As described in this model, AWS is
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
customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Amazon Q Developer or other AWS services
using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
provide a URL to an external server, we strongly recommend that you do not include credentials
information in the URL to validate your request to that server.

We also strongly recommend that you don't provide secrets or confidential data to Amazon Q Developer in chat applications.
All commands run using Amazon Q Developer in chat applications come through Microsoft Teams and Slack. As such, we recommend that you carefully consider what information you send
Amazon Q Developer in chat applications through Slack. Additionally, all comamnds run using Amazon Q Developer in chat applications can be processed in any commercial AWS Region.

###### Note

Amazon Q Developer in chat applications doesn't modify any event, alarm, or other reporting data when it forwards
Amazon Simple Notification Service (Amazon SNS) notifications to chat rooms. It treats all notifications as read only.
