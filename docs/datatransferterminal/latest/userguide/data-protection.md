# Data protection in AWS Data Transfer Terminal

The AWS
[shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/ "https://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in AWS Data Transfer Terminal. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/ "https://aws.amazon.com/compliance/data-privacy-faq/").For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/ "https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/") blog post on the _AWS Security Blog_.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](../../../awscloudtrail/latest/userguide/cloudtrail-trails.md "../../../awscloudtrail/latest/userguide/cloudtrail-trails.md") in the _AWS CloudTrail User Guide_.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").
  We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Data Transfer Terminal or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## Data encryption

AWS Data Transfer Terminal provides access to a high-speed network connection for you to securely transfer data between self-managed storage systems and AWS storage services. How your storage data is encrypted in transit depends in part on the policies enabled on your devices and the services your data is transfered to. Management of data and it’s encryption in transit are the responsibility of the individual using Data Transfer Terminal.

### Encryption at rest

AWS Data Transfer Terminal encrypts all data at rest.

Data Transfer Terminal only captures data necessary for reservations including the first and last names and email addresses of the individuals specified to both attend and schedule the reservation. The purpose for this data collection is to confirm reservation details and ensure access to the room to perform the data transfer. This transactional information is backed up no more than 35 days, however, AWS account information is retained for 10 years.

## Encryption in transit

AWS Data Transfer Terminal does not encrypt data in transit. Data is encrypted-in-transit when you interact with Data Transfer Terminal API endpoints for setting up Transfer teams, adding personnel, and scheduling reservations in the console. As part of the AWS shared responsibility model, you have choices about how you connect to AWS services through Data Transfer Terminal. We strongly recommend you choose to connect to AWS services using strong encryption-in-transit, such as TLS 1.2 and 1.3.

For example, use only encrypted connections over HTTPS (TLS) by using the [aws:SecureTransport](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md#Conditions_Boolean") condition in your Amazon S3 bucket policies, as illustrated in the bucket policy below.

To learn more about data encryption in transit with other AWS services, such as Amazon S3, see [Protecting data with server-side encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md") in the Amazon S3 User Guide.

## Key management

AWS Data Transfer Terminal does not directly support Customer managed keys. Use the Customer managed key support available for the AWS services you connect to during your Data Transfer Terminal reservation. Learn more about Customer managed keys and how to encrypt your data at rest in the [AWS KMS keys](../../../kms/latest/developerguide/concepts.md#customer-cmk#IMUpdateThresholdFromMap "../../../kms/latest/developerguide/concepts.md#customer-cmk#IMUpdateThresholdFromMap") section of the [AWS Key Management Service Developer Guide](../../../kms/latest/developerguide/overview.md#customer-cmk#IMUpdateThresholdFromMap "../../../kms/latest/developerguide/overview.md#customer-cmk#IMUpdateThresholdFromMap").

## Inter-network traffic privacy

Access to the Data Transfer Terminal console is through published service APIs. Data Transfer Terminal resources are independent of virtual private cloud (VPC).
