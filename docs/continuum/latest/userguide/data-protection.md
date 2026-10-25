

# Data protection in AWS Continuum
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Continuum. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/). 

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with AWS Continuum or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.



**Note**  
The data protection information in this topic applies to AWS Continuum. It does not cover Continuum for Penetration testing (formerly known as Security Agent).

**Note**  
AWS Continuum automatically selects the optimal AWS Region within your geographic area to process your inference requests. This approach maximizes available compute resources and model availability. Your data remains stored only in the Region where the request originated. However, AWS Continuum might process input prompts and output results outside that Region. AWS Continuum encrypts all data in transit across the Amazon secure network.  
AWS Continuum securely routes inference requests to available compute resources within the geographic area where the request originated, as follows:  
Inference requests that originate in the United States are processed within the United States.

## Opting out of using your data for service improvement
<a name="data-protection-opt-out"></a>

You can choose to opt out of having your data (defined as "AWS Continuum Content" in the AWS Continuum service terms) used to develop and improve AWS Continuum and other AWS security services by using the AWS Organizations opt-out policy. You can choose to opt out even if AWS Continuum does not currently collect any such Content. For more information about how to opt out, see [AI services opt-out policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ai-opt-out.html) in the *AWS Organizations User Guide*.

**Note**  
To use the opt-out policy, your AWS accounts must be centrally managed by AWS Organizations. If you haven't already created an organization for your AWS accounts, see [Creating and managing an organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org.html) in the *AWS Organizations User Guide*.

Opting out has the following effects:
+ AWS Continuum deletes the Content that it collected and stored for service-improvement purposes before you opted out, if any.
+ After you opt out, AWS Continuum no longer collects or stores this Content for service-improvement purposes.

### AWS Continuum data usage
<a name="data-protection-opt-out-data-usage"></a>

Currently, AWS Continuum does not collect or store any AWS Continuum Content for service-improvement purposes. However, in the future, AWS Continuum might collect and use AWS Continuum Content that it receives from you or from upstream services, for the purpose of providing AWS Continuum capabilities, to improve AWS Continuum and other AWS security service capabilities.

Your trust, privacy, and the security of your Content are our highest priority. If AWS Continuum begins collecting AWS Continuum Content for service-improvement purposes in the future, this page is updated to reflect those changes and to provide details about what data is collected and how it is used. You can opt out of this AWS Continuum Content collection at any time by using the AWS Organizations opt-out policy described previously. For more information about AWS data privacy practices, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).