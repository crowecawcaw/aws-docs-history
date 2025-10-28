# Use AMS SSP to provision Amazon Comprehend in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Comprehend capabilities directly in your AMS managed account. Amazon Comprehend is a natural language processing (NLP) service that uses machine learning to find insights and
relationships in text, no machine learning experience is required.
Amazon Comprehend uses machine learning to help you uncover the insights and relationships in your unstructured data.
The service identifies the language of the text; extracts key phrases,
places, people, brands, or events; understands how positive or negative the text is; analyzes text using
tokenization and parts of speech; and automatically organizes a
collection of text files by topic. You can also use AutoML capabilities in Amazon Comprehend to build a custom
set of entities or text classification models that are tailored uniquely to your organization’s needs.
To learn more, see
[Amazon Comprehend](https://aws.amazon.com/comprehend/ "https://aws.amazon.com/comprehend/").

## Amazon Comprehend in AWS Managed Services FAQ

**Q: How do I request access to Amazon Comprehend in my AMS account?**

Amazon Comprehend console and data access roles can be requested through the submission of two AMS Service RFCs:

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account: `customer_comprehend_console_role`. After it's provisioned in
your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon Comprehend in my AMS account?**

Create New IAM Role functionality through the Amazon Comprehend console is restricted. Otherwise, full
functionality of Amazon Comprehend is available in your AMS account.

**Q: What are the prerequisites or dependencies to using Amazon Comprehend in my AMS account?**

Amazon S3 and AWS Key Management Service (AWS KMS) are required in order to use Amazon Comprehend, if Amazon S3 buckets are encrypted with AWS KMS keys.
