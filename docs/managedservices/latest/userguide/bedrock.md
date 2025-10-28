# Use AMS SSP to provision Amazon Bedrock in your AMS account

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Bedrock capabilities directly in your AMS managed account. Amazon Bedrock is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and AWS available for your use through a unified API. You can choose from a wide range of foundation models to find the model that is best suited for your use case. Amazon Bedrock also offers a broad set of capabilities to build generative AI applications with security, privacy, and responsible AI. Using Amazon Bedrock, you can easily experiment with and evaluate top foundation models for your use cases, privately customize them with your data using techniques such as fine-tuning and Retrieval Augmented Generation (RAG), and build agents that execute tasks using your enterprise systems and data sources.

With Amazon Bedrock's serverless experience, you can get started quickly, privately customize foundation models with your own data, and easily and securely integrate and deploy them into your applications using AWS tools without having to manage any infrastructure. For more information, see [Amazon Bedrock](https://aws.amazon.com/bedrock/ "https://aws.amazon.com/bedrock/").

## FAQ: Amazon Bedrock in AMS

**Q: How do I request access to Amazon Bedrock in my AMS account?**

To request access to Amazon Bedrock submit an RFC with the Management | AWS service | Self-provisioned service | Add (managed automation) (ct-3qe6io8t6jtny) change type.
This RFC provisions the following IAM role to your account:
`customer_bedrock_console_role`. After it's provisioned in
your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon Bedrock in my AMS account?**

- Amazon Bedrock knowledge bases aren't supported by default as part of the SSPS role due to its dependency on Amazon OpenSearch Service Serverless which is not currently supported on AMS.
- Bedrock Studio isn't supported due to its dependency on unsupported services such as Amazon DataZone.

**Q: What are the prerequisites or dependencies to using Amazon Bedrock in my AMS account?**

- Third-party model subscriptions that require AWS Marketplace permissions must be done by the default role (`AWSManagedServicesAdminRole` on MALZ and `Customer_ReadOnly_Role` on SALZ). This is because the default role includes AWS Marketplace permissions.
- If data encryption is used, then you must provide the AWS KMS key ARN when you request creation of the console role. Also, the Amazon S3 bucket in use must have “bedrock” in its name.
