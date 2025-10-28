# Incident Detection and Response security and resiliency

The [AWS Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in Support.
As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible
for maintaining control over your content that is hosted on this infrastructure. This content includes the security configuration and management
tasks for the AWS services that you use.

For more information about data privacy, see the
[Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq "https://aws.amazon.com/compliance/data-privacy-faq").

For information about data protection in Europe, see the
[AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the AWS Security Blog.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual user accounts with AWS Identity and Access Management (IAM). That way each
user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use Secure Sockets Layer/Transport Layer Security (SSL/TLS) certificates to communicate with AWS resources.
  We recommend TLS 1.2 or later. For information, see
  [What Is An SSL/TLS Certificate?](https://aws.amazon.com/what-is/ssl-certificate/ "https://aws.amazon.com/what-is/ssl-certificate/").
- Set up API and user activity logging with AWS CloudTrail. For information, see
  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/").
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering
  and securing personal data that is stored in Amazon S3. For information about Amazon Macie, see
  [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/").
- If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line
  interface or an API, use a FIPS endpoint. For information about the available FIPS endpoints, see
  [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form
  fields such as a **Name** field. This includes when you work with Support or other AWS services using the console, API, AWS CLI, or AWS SDKs.
  Any data that you enter into tags or free-form fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server,
  we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## AWS Incident Detection and Response access to your accounts

AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS
resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to
use resources.

## AWS Incident Detection and Response and your alarm data

By default, Incident Detection and Response receives the Amazon resource name (ARN) and state of every CloudWatch alarm in your account and then starts the
incident detection and response process when your onboarded alarm changes into the ALARM state. If you would like to customize
what information incident detection and response receives about alarms from your account, contact your Technical Account Manager.
