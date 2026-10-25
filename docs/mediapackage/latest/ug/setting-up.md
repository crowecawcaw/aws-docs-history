

# Setting up MediaPackage
<a name="setting-up"></a>

Before you start using AWS Elemental MediaPackage (MediaPackage), you must sign up for AWS (if you don’t already have an AWS account) and create IAM users and roles to allow access to MediaPackage. This includes creating an IAM role for yourself. If you want to use encryption to protect your content, you also must store your encryption keys in AWS Secrets Manager, and then give MediaPackage permission to obtain the keys from your Secrets Manager account.

This section guides you through the steps required to configure users and roles to access MediaPackage. For background and additional information about identity and access management for MediaPackage, see [Identity and Access Management for AWS Elemental MediaPackage](security-iam.md).

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Creating policies and non-administrative roles](setting-up-create-non-admin-iam.md)
+ [Allowing AWS Elemental MediaPackage to access other AWS services](setting-up-create-trust-rel.md)
+ [(Optional) Setting up encryption](set-up-encryption.md)
+ [(Optional) Installing the AWS CLI](setting-up-install-cli.md)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. There are two ways to sign up for AWS. If you want complete control over account configuration and where your content is stored, or if you have regulated workloads such as HIPAA or FedRAMP, use [Sign up for AWS (advanced)](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html). If you are a new user and want to use a login you already own to sign in to AWS and create an AWS environment with preconfigured defaults in select [AWS Regions](https://docs.aws.amazon.com/accounts/latest/reference/project-regions.html), use [Sign up for AWS](https://docs.aws.amazon.com/accounts/latest/reference/sign-in-new.html).