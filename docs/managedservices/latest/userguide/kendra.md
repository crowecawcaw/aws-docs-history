# Use AMS SSP to provision Amazon Kendra in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Kendra capabilities directly in your AMS managed account. Amazon Kendra is an intelligent search service that uses natural language processing and advanced machine learning algorithms to return specific answers to search questions from your data. Unlike traditional keyword-based search, Amazon Kendra uses its semantic and contextual understanding capabilities to determine if a document is relevant to a search query. Amazon Kendra returns specific answers to questions, so your experience is close to interacting with a human expert.
Amazon Kendra is highly scalable, capable of meeting performance demands, is tightly integrated with other AWS services such as Amazon S3 and Amazon Lex, and offers enterprise-grade security.

To learn more, see [Amazon Kendra;](../../../kendra/latest/dg/what-is-kendra.md "../../../kendra/latest/dg/what-is-kendra.md").

## Amazon Kendra in AWS Managed Services FAQ

**Q: How do I request access to Amazon Kendra in my AMS account?**

To request access to Amazon Inspector Classic, submit an RFC with the Management | AWS service | Self-provisioned service
| Add (ct-3qe6io8t6jtny) change type. This RFC provisions the `customer_kendra_console_role` IAM role to your account. After provisioned in your account, you must onboard the role in your federation solution. **Q: What are the restrictions to using Amazon Kendra in my AMS account?** There are no restrictions. Full functionality of Amazon Kendra is available in your AMS account. **Q: What are the prerequisites or dependencies to using Amazon Kendra in my AMS account?** There are no prerequisites or dependencies to get started with Amazon Kendra. However, depending on your specific use case, you might require access to other AWS services.
