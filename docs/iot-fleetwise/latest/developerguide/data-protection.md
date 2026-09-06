

AWS IoT FleetWise is no longer open to new customers. Existing AWS IoT FleetWise customers can continue using the service. The [Guidance for Connected Mobility on AWS](https://aws.amazon.com/solutions/guidance/connected-mobility-on-aws/) provides guidance on how to develop and deploy modular services for connected mobility solutions that can be used to achieve equivalent capabilities as AWS IoT FleetWise.

# Data protection in AWS IoT FleetWise
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS IoT FleetWise. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS IoT FleetWise or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.



AWS IoT FleetWise is intended to be used with an Edge Agent that you develop and install on supported vehicle hardware in order to transmit vehicle data to the AWS Cloud. Extracting data from vehicles *might* be subject to data privacy regulations in certain jurisdictions. Before using AWS IoT FleetWise and installing your Edge Agent, we strongly recommend that you assess your compliance obligations under applicable law. This includes any applicable legal requirements to provide legally adequate privacy notices and obtain any necessary consents for extracting vehicle data.

## Encryption at rest in AWS IoT FleetWise
<a name="encryption-rest"></a>

The data collected from a vehicle is transmitted to the cloud through an AWS IoT Core message with the MQTT message protocol. AWS IoT FleetWise delivers the data to your Amazon Timestream database. In Timestream, your data is encrypted. All AWS services encrypt data at rest by default. For more information, see [ Protecting data with encryption](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingEncryption.html) in the Amazon S3 User Guide and [Data protection in Timestream for LiveAnalytics](https://docs.aws.amazon.com/timestream/latest/developerguide/data-protection.html). 

Encryption at rest integrates with AWS Key Management Service (AWS KMS) to manage the encryption key that's used to encrypt your data. You can choose to use a customer managed key to encrypt data collected by AWS IoT FleetWise. You can create, manage, and view your encryption key through AWS KMS. For more information, see [What is AWS Key Management Service?](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) in the *AWS Key Management Service Developer Guide*. 

## Encryption in transit
<a name="encryption-transit"></a>

All data exchanged with AWS IoT services is encrypted in transit by using Transport Layer Security (TLS). For more information, see [Transport security](https://docs.aws.amazon.com/iot/latest/developerguide/transport-security.html) in the *AWS IoT Developer Guide*.

Also, AWS IoT Core supports [authentication](https://docs.aws.amazon.com/iot/latest/developerguide/authentication.html) and [authorization](https://docs.aws.amazon.com/iot/latest/developerguide/authorization.html) to help securely control access to AWS IoT FleetWise resources. Vehicles can use X.509 certificates to get authenticated (signed in) to use AWS IoT FleetWise and use AWS IoT Core policies to get authorized (have permissions) to perform specified actions. For more information, see [Provision AWS IoT FleetWise vehicles](provision-vehicles.md).