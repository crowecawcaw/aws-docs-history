# Data protection in AWS Device Farm

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS Device Farm (Device Farm). As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Device Farm or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

## Encryption in transit

The Device Farm endpoints only support signed HTTPS (SSL/TLS) requests except where otherwise noted. All content
retrieved from or placed in Amazon S3 through upload URLs is encrypted using SSL/TLS. For more information on how HTTPS
requests are signed in AWS, see [Signing AWS API requests](../../../general/latest/gr/signing_aws_api_requests.md "../../../general/latest/gr/signing_aws_api_requests.md") in the AWS General
Reference.

It is your responsibility to encrypt and secure any communications that your tested applications make and any
applications installed in the process of running on-device tests.

## Encryption at rest

Device Farm's desktop browser testing feature supports encryption at rest for artifacts generated during
tests.

Device Farm's physical mobile device testing data is not encrypted at rest.

## Data retention

Data in Device Farm is retained for a limited time. After the retention period expires, the data
is removed from Device Farm's backing storage.

| Content type                         | Retention period (days) | Metadata Retention period (days) |
| ------------------------------------ | ----------------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Uploaded applications                | 30                      | 30                               |
| Uploaded test packages               | 30                      | 30                               |
| Logs                                 | 400                     | 400                              |
| Video recordings and other artifacts | 400                     | 400                              | It is your responsibility to archive any content that you want to retain for longer periods. ## Data management Data in Device Farm is managed differently depending on which features are used. This section explains how data is managed while and after you use Device Farm. ### Desktop browser testing Instances used during Selenium sessions are not saved. All data generated as a result of browser interactions is discarded when the session ends. This feature currently supports encryption at rest for artifacts generated during the test. ### Physical device testing The following sections provide information about the steps AWS takes to clean up or destroy devices after you have used Device Farm. Device Farm's physical mobile device testing data is not encrypted at rest. #### Public device fleets After test execution is complete, Device Farm performs a series of cleanup tasks on each device in the public device fleet, including uninstallation of your app. If we cannot verify uninstallation of your app or any of the other cleanup steps, the device receives a factory reset before it is put back into use. ###### Note It is possible for data to persist between sessions in some cases, especially if you make use of the device system outside the context of your app. For this reason, and because Device Farm captures video and logs of activity taking place during your use of each device, we recommend that you do not enter sensitive information (for example, Google account or Apple ID), personal information, and other security-sensitive details during your automated test and remote access sessions. #### Private devices After expiration or termination of your private device contract, the device is removed from use and securely destroyed in accordance with AWS destruction policies. For more information, see [Private devices in AWS Device Farm](working-with-private-devices.md "working-with-private-devices.md"). ## Key management Currently, Device Farm does not offer any external key management for encryption of data, at rest or in transit. ## Internetwork traffic privacy Device Farm can be configured, for private devices only, to use Amazon VPC endpoints to connect to your resources in AWS. Access to any non-public AWS infrastructure associated with your account (for example, Amazon EC2 instances without a public IP address) must use an Amazon VPC endpoint. Regardless of VPC endpoint configuration, Device Farm isolates your traffic from other users throughout the Device Farm network. Your connections outside the AWS network are not guaranteed to be secured or safe, and it is your responsibility to secure any internet connections your applications make. |
