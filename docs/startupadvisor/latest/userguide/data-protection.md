

# Data protection in AWS Startups
<a name="data-protection"></a>

The AWS [shared responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Startups. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. This content includes the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](http://aws.amazon.com/compliance/data-privacy-faq). For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr) blog post on the *AWS Security Blog*.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS Identity and Access Management (IAM). That way each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We recommend TLS 1.2 or later.
+ Set up API and user activity logging with AWS CloudTrail.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-2](http://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put sensitive identifying information, such as your customers' account numbers, into free-form fields such as a **Name** field. This includes when you work with AWS Startups or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into AWS Startups or other services might get picked up for inclusion in diagnostic logs. When you provide a URL to an external server, don’t include credentials information in the URL to validate your request to that server.

## Data and privacy in AWS Startups
<a name="data-protection-privacy"></a>

 AWS Startups is designed to protect your data and your privacy. AWS Startups uses only the following two sources of data to tailor its guidance to your startup:
+ The information in your AWS Activate credit application
+ Your startup’s website

 AWS Startups uses this data solely to tailor the experience to your stack and your stage. AWS Startups protects your data in the following ways:
+  **Your source code is not stored.** AWS Startups does not store your source code.
+  **Your data is not shared with third parties.** AWS Startups does not share your data with third parties.
+  **Your data is used only to tailor your experience.** AWS Startups uses your data solely to tailor its guidance to your startup.

## Encryption at rest
<a name="encryption-rest"></a>

 AWS Startups does not store customer data at rest. Because the service does not store or retain your data, encryption at rest does not apply.

## Encryption in transit
<a name="encryption-transit"></a>

 AWS Startups encrypts all data in transit by using TLS 1.2 or later. This applies both to traffic between you and the service and to traffic between the service and downstream AWS services, such as AWS Cost Explorer and AWS Billing and Cost Management.

For the AWS credits and cost tracker, AWS Startups retrieves your billing and cost data from AWS Cost Explorer and AWS Billing and Cost Management in real time on your behalf. AWS Startups does not store or retain this data.