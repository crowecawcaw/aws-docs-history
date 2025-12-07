# Step 3: Deploy to AWS

Nova Act provides two deployment approaches depending on your needs.

###### Note

Your deployment to AWS is subject to [AWS Service Terms](https://aws.amazon.com/service-terms/ "https://aws.amazon.com/service-terms/") and/or [Customer Agreement](https://aws.amazon.com/agreement/ "https://aws.amazon.com/agreement/") (or other agreement governing your use of the AWS Service). Deployment creates AWS resources (AgentCore Runtime, ECR repository, S3 bucket) that incur separate charges. See [Amazon Nova Act pricing](https://aws.amazon.com/nova/pricing/ "https://aws.amazon.com/nova/pricing/") for details.

## Quick deployment to AWS with the IDE extension

For rapid deployment of individual workflows, use the Nova Act extension’s built-in deployment capability.

To deploy your workflow:

1. Navigate to the **Deploy** tab in the Nova Act extension.
2. Verify your AWS credentials with **`aws sts get-caller-identity`**. If needed, configure or update your credentials.
3. Ensure your IAM Identity has a policy permitting read and write access to the Nova Act service (see [AWS Managed Policies](security-iam-awsmanpol.md "security-iam-awsmanpol.md")).
4. Enter your workflow name and select your AWS Region.
5. Click **Deploy your workflow**.

The IDE extension uses Amazon Bedrock AgentCore Runtime to automatically package your script into a container image and deploys it to AWS, creating all necessary resources including ECR repositories, S3 buckets, and IAM execution roles.

## Deployment to AWS with CDK templates

For production environments, the [nova-act-samples](http://github.com/amazon-agi-labs/nova-act-samples "http://github.com/amazon-agi-labs/nova-act-samples") GitHub repository contains ready-to-use examples for deploying Nova Act on various AWS compute services. Each example includes a complete CDK construct, Docker configuration, and test scripts.

These examples can serve as a starting point for building production systems tailored to your organization’s needs, including enhanced monitoring, infrastructure management, and security configurations.
