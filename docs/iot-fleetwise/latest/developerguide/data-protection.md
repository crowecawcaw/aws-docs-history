# Data protection in AWS IoT FleetWise

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/")
applies to data protection in AWS IoT FleetWise. As described in this model, AWS is
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
  customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS IoT FleetWise or other AWS services
  using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into
  tags or free-form text fields used for names may be used for billing or diagnostic logs. If you
  provide a URL to an external server, we strongly recommend that you do not include credentials
  information in the URL to validate your request to that server.

AWS IoT FleetWise is intended to be used with an Edge Agent that you develop and install on
supported vehicle hardware in order to transmit vehicle data to the AWS Cloud. Extracting data
from vehicles _might_ be subject to data privacy regulations in
certain jurisdictions. Before using AWS IoT FleetWise and installing your Edge Agent, we strongly
recommend that you assess your compliance obligations under applicable law. This includes any
applicable legal requirements to provide legally adequate privacy notices and obtain any
necessary consents for extracting vehicle data.

## Encryption at rest in AWS IoT FleetWise

The data collected from a vehicle is transmitted to the cloud through an AWS IoT Core message
with the MQTT message protocol. AWS IoT FleetWise delivers the data to your Amazon Timestream database. In
Timestream, your data is encrypted. All AWS services encrypt data at rest by default. For more information,
see [Protecting
data with encryption](../../../AmazonS3/latest/userguide/UsingEncryption.md "../../../AmazonS3/latest/userguide/UsingEncryption.md") in the Amazon S3 User Guide and [Data protection in Timestream for
LiveAnalytics](../../../timestream/latest/developerguide/data-protection.md "../../../timestream/latest/developerguide/data-protection.md").

Encryption at rest integrates with AWS Key Management Service (AWS KMS) to manage the encryption key that's
used to encrypt your data. You can choose to use a customer managed key to encrypt data
collected by AWS IoT FleetWise. You can create, manage, and view your encryption key through AWS KMS.
For more information, see [What is AWS Key Management Service?](../../../kms/latest/developerguide/overview.md "../../../kms/latest/developerguide/overview.md") in the
_AWS Key Management Service Developer Guide_.

## Encryption in transit

All data exchanged with AWS IoT services is encrypted in transit by using Transport Layer
Security (TLS). For more information, see [Transport security](../../../iot/latest/developerguide/transport-security.md "../../../iot/latest/developerguide/transport-security.md") in the _AWS IoT Developer Guide_.

Also, AWS IoT Core supports [authentication](../../../iot/latest/developerguide/authentication.md "../../../iot/latest/developerguide/authentication.md") and [authorization](../../../iot/latest/developerguide/authorization.md "../../../iot/latest/developerguide/authorization.md") to help securely control access to AWS IoT FleetWise resources. Vehicles can use
X.509 certificates to get authenticated (signed in) to use AWS IoT FleetWise and use AWS IoT Core policies
to get authorized (have permissions) to perform specified actions. For more information, see
[Provision AWS IoT FleetWise vehicles](provision-vehicles.md "provision-vehicles.md").
