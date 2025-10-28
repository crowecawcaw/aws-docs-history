# Use AMS SSP to provision Amazon Textract in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Textract capabilities directly in your AMS managed account. Amazon Textract is a fully managed machine learning service that automatically extracts
printed text, handwriting, and other data from scanned documents that goes beyond simple
optical character recognition (OCR) to identify, understand, and extract data from forms
and tables. To learn more, see
[Amazon Textract](https://aws.amazon.com/textract/ "https://aws.amazon.com/textract/").

## Amazon Textract in AWS Managed Services FAQ

Common questions and answers:

**Q: How do I request Amazon Textract to be set up in my AMS account?**

Request access by submitting a Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type. This RFC
provisions the following IAM roles to your account:
`customer_textract_console_role`,
`customer_textract_human_review_execution_role`, and
`customer_ec2_textract_instance_profile`. Once provisioned in your account,
you must onboard the role `customer_textract_console_role` in your
federation solution.

**Q: What are the restrictions to using Amazon Textract in my AMS account?**

There are no restrictions for the use of Amazon Textract in your AMS account.

**Q: What are the prerequisites or dependencies to using Amazon Textract in my AMS account?**

You must request the creation of an S3 bucket by submitting an RFC Deployment |
Advanced stack components |S3 storage | Create (ct-1a68ck03fn98r).
