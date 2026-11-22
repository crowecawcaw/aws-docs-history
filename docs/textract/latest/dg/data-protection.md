

# Data protection in Amazon Textract

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon Textract. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. This content includes the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq). For information about data protection in Europe, see the [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/) blog post on the *AWS Security Blog*.

For data protection purposes, protect your AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. Also secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We recommend TLS 1.2 or later.
+ Set up API and user activity logging with AWS CloudTrail.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com/compliance/fips/).

Never put confidential or sensitive information, such as your customers' email addresses, into free-form text fields such as a `Name` field. This includes when you work with Amazon Textract or other AWS services using the console, API, AWS CLI, or AWS SDKs. It also includes Amazon Textract Insights project names, blueprint names, the field descriptions in a blueprint schema, and tag keys and values. Any data that you enter into free-form text fields might be picked up for inclusion in diagnostic logs. If you provide a URL to an external server, do not include credentials information in the URL to validate your request to that server.

For more information about data protection, see the [AWS Shared Responsibility Model and GDPR](https://aws.amazon.com/blogs/security/the-aws-shared-responsibility-model-and-gdpr/) blog post on the *AWS Security Blog*.

## Internetwork traffic privacy
<a name="internetwork-traffic"></a>

Amazon Textract communicates exclusively through HTTPS endpoints, which are supported in all AWS Regions supported by Amazon Textract. When Amazon Textract Insights routes a request to another AWS Region in the same geography for inference, the data is encrypted in transit across the Amazon network.

## Custom Queries
<a name="custom-queries"></a>

 Any content used for generating adapters is processed internally within Amazon Textract Core for the duration of the training. The content is encrypted at rest and in transit. The content is stored and processed in the AWS Region where you are training the adapter, and is deleted once training completes. By default, the content is encrypted using AWS owned AWS KMS keys. If a KMSKeyId is provided when creating an adapter version, the content is encrypted using the customer managed AWS KMS key provided. Customer content (training images, prelabeling results, annotations) is not logged or retained even for debugging purposes. 

## Data protection in Amazon Textract Insights
<a name="data-protection-insights"></a>

Amazon Textract Insights processes the document that you submit with `StartDocumentInsights` and writes the results to the Amazon S3 output location that you specify.
+ **Processing location** – Amazon Textract Insights uses cross-Region inference to automatically select the optimal AWS Region within your geography to process your inference requests. This maximizes available compute resources and model availability, and delivers the best customer experience. For example, requests that start in the United States are processed in the United States. Input prompts and output results might be processed outside the AWS Region where the request originated. All data is transmitted encrypted across Amazon's secure network. For the AWS Regions involved, see [Cross-Region inference](insights-cross-region.md).
+ **Storage location** – Your input and output Amazon S3 buckets must be in the same AWS Region as the request. Amazon Textract Insights writes results only beneath the output prefix that you specify.
+ **Encryption** – Amazon Textract Insights encrypts your data at rest with AWS owned keys by default, or with a customer managed AWS KMS key that you choose. See [Data protection and encryption](insights-data-protection.md).
+ **Sensitive data** – You can configure a project to detect personally identifiable information (PII) and, optionally, redact it. Redaction writes an additional, redacted copy of the JSON results, and the original results and other output files keep the raw values. See [Detecting and redacting sensitive data](insights-detecting-redacting.md).