

# Data protection in Amazon Connect Health
<a name="data-protection"></a>

The AWS [shared responsibility model](http://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon Connect Health. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](http://aws.amazon.com/compliance/data-privacy-faq). For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](http://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr) blog post on the *AWS Security Blog*.

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint.

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Amazon Connect Health or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names might be used for billing or diagnostic logs.

## Data handled by Amazon Connect Health
<a name="data-handled"></a>

Amazon Connect Health handles a variety of data related to healthcare interactions, including but not limited to the following categories:
+  **Patient data** — Patient information retrieved in real time from EHR systems or other external data sources during each interaction.
+  **Call transcripts** — Retained in the customer’s Amazon Connect instance for the customer-configured retention period.
+  **Contact Trace Records (CTRs)** — Retained in Amazon Connect for up to 24 months.
+  **CloudWatch Logs** — Retained per the customer-configured log group retention policy.
+  **Domain and agent configurations** — Resources and configurations including domains, agents, agent versions, and integrations.

## Encryption at rest
<a name="encryption-rest"></a>

All data stored by Amazon Connect Health is encrypted at rest using AWS Key Management Service (AWS KMS). Contact data classified as PII, or data that represents customer content being stored by Amazon Connect Health, is encrypted at rest using AWS KMS encryption keys. For more information about AWS KMS keys, see [What is AWS Key Management Service?](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) in the *AWS Key Management Service Developer Guide*.

Customers can use AWS managed keys or provide their own customer managed keys for additional control over encryption. AWS KMS charges apply for a customer managed key. For more information about pricing, see [AWS KMS pricing](http://aws.amazon.com/kms/pricing/).

## Encryption in transit
<a name="encryption-transit"></a>

All data exchanged with Amazon Connect Health is protected in transit using industry-standard TLS 1.2 or higher encryption. This includes:
+ Communications between the user’s web browser and Amazon Connect Health
+ Patient calls and agent workspace communications
+ EHR API requests and responses
+ Integrations with AWS services such as AWS Lambda, Amazon Bedrock, and Amazon Connect

When Amazon Connect Health integrates with AWS services, data is always encrypted in transit using TLS.

## PHI handling
<a name="phi-handling"></a>

Amazon Connect Health does not store Patient Health Info (PHI) outside of an active call session — once a patient interaction ends, no PHI is retained within the service layer, minimizing compliance exposure for healthcare customers.

For Amazon Connect Health patient engagement workflows integrated with Amazon Connect contact center features, customers can rely on Connect’s native PHI handling. Amazon Connect provides proactive PHI redaction in chats and transcripts, encrypts data in transit, and manages customer profiles securely. For example, customers can enable Connect Contact Lens sensitive data blocking to prevent PHI from being stored in plain text.

Both services are HIPAA eligible. Together, the two services form a layered approach: Amazon Connect Health handles session-scoped PHI securely at the agentic layer, while Amazon Connect provides PHI protection controls at the contact center infrastructure level.

## Cross-Region Inference (CRIS) disclosure
<a name="cris-disclosure"></a>

Amazon Connect Health uses Amazon Bedrock foundation models to power AI capabilities. Customers need to be aware of the following:
+  **Cross-Region Inference** — Depending on your AWS Region and model availability, inference requests might be processed across AWS Regions to optimize performance and availability. All data transmission occurs within the AWS secure infrastructure with end-to-end encryption. For detailed information about Amazon Bedrock’s cross-region inference capabilities and data handling practices, refer to the [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/).
+  **Compliance considerations** — Organizations using Amazon Connect Health agents need to review their data residency requirements and ensure alignment with their HIPAA Business Associate Agreement (BAA) with AWS. The service maintains HIPAA eligibility across all supported Regions.
+  **Model usage** — The agents use Amazon Bedrock models in accordance with provider license restrictions. All usage complies with the AWS Responsible AI Policy and provider-specific restrictions.

## Service improvement and how to opt out
<a name="service-improvement"></a>

You can opt out of the use of your content for service improvement by contacting the Amazon Connect Health team at [amazon-connecthealth-ai-optout@amazon.com](mailto:amazon-connecthealth-ai-optout@amazon.com) with your AWS Account ID.