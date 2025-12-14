# Amazon Inspector integrations

Amazon Inspector integrates with other AWS services.
These services can ingest data from Amazon Inspector, so you can view your findings in different ways.
Review the following integration options to learn more.

## Using Amazon Inspector with AWS Organizations

[AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") helps you centrally manage and govern your AWS environment.
You can use AWS Organizations policies to enable and manage Amazon Inspector across multiple accounts in your organization automatically.

Amazon Inspector organization policies allow you to:

- Centrally enable Amazon Inspector scan types (EC2, ECR, Lambda, Code Repository) across your organization
- Automatically apply Amazon Inspector enablement to new accounts joining the organization
- Enforce consistent scanning coverage across organizational units
- Prevent member accounts from disabling required scanning

Organization policies control resource type enablement, while delegated administrators retain control over scan configuration settings.
For information about how organization policies interact with delegated administrator and member account permissions, see [Managing multiple accounts in Amazon Inspector with AWS Organizations](managing-multiple-accounts.md "managing-multiple-accounts.md").
For detailed instructions on creating Amazon Inspector policies, see the AWS Organizations documentation for Amazon Inspector policies.

## Integrating Amazon Inspector with Amazon ECR

[Amazon Elastic Container Registry (Amazon ECR)](../../../AmazonECR/latest/userguide/what-is-ecr.md "../../../AmazonECR/latest/userguide/what-is-ecr.md") is an AWS-managed container image registry that supports private registries.
Amazon ECR private registries host container images in a highly-available and scalable architecture.
You can use Amazon Inspector to scan container images residing in your Amazon ECR repository for vulnerable operating system packages and programming language packages.
For more information, see [Amazon Inspector integration with Amazon Elastic Container Registry (Amazon ECR)](ecr-integration.md "ecr-integration.md").

## Amazon Inspector integration with AWS Security Hub CSPM

[AWS Security Hub CSPM](../../../securityhub/latest/userguide/what-is-securityhub.md "../../../securityhub/latest/userguide/what-is-securityhub.md") provides a comprehensive view of your security state in AWS and helps you check your environment against security industry standards and best practices
Security Hub CSPM collects security data from AWS accounts, services, and supported products.
You can use Security Hub CSPM to ingest Amazon Inspector findings data and create a central location for findings in all of your integrated AWS services and AWS Partner Network products.
For more information, see [Amazon Inspector integration with AWS Security Hub CSPM](securityhub-integration.md "securityhub-integration.md").
