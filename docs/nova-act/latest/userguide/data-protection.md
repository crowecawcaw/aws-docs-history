# Data protection in Amazon Nova Act

###### Note

This data protection section applies to your deployment on the Nova Act AWS service as an AWS customer.

The AWS
[shared responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/ "http://aws.amazon.com/compliance/shared-responsibility-model/") applies to data protection in Nova Act. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. This content includes the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](http://aws.amazon.com/compliance/data-privacy-faq "http://aws.amazon.com/compliance/data-privacy-faq").

For data protection purposes, we recommend you protect AWS account credentials and set up individual users with AWS Identity and Access Management (IAM). That way each user is given only the permissions necessary to fulfill their job duties. We also recommend you secure your data in the following ways:

- Use multi-factor authentication (MFA) with each account.
- Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
- Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see Working with CloudTrail trails in the AWS CloudTrail User Guide.
- Use AWS encryption solutions, along with all default security controls within AWS services.
- Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
- If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](http://aws.amazon.com/compliance/fips/ "http://aws.amazon.com/compliance/fips/").
  We strongly recommend you never put sensitive identifying information, such as your customers' account numbers, into free-form fields such as a **Name** field. This includes when you work with Amazon Nova Act or other AWS services using the console, API, AWS Command Line Interface, or AWS SDKs. Any data that you enter into Amazon Nova Act or other services might get picked up for inclusion in diagnostic logs. When you provide a URL to an external server, don’t include credentials information in the URL to validate your request to that server.

## Nova Act considerations

The following are special security considerations for Nova Act.

- We recommend you do not provide sensitive information within the act() statements, such as account passwords. Instead, such information should be passed directly to the browser using Playwright keyboard API calls. Note that if you use sensitive information through Playwright, the information could still be collected in screenshots by AWS if it appears unobstructed on the browser when Nova Act is engaged in completing an action.
- Nova Act accepts inputs from customers for tool definitions and service details, which can potentially contain personally identifiable information (PII).
- Usage metrics and logs are stored in the customer account’s CloudWatch.
