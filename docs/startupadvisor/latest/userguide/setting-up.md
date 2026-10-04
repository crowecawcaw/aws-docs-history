

# Setting up AWS Startup Advisor
<a name="setting-up"></a>

Before you use AWS Startup Advisor, review the following. You can use AWS Startup Advisor without an AWS account, but an AWS account is recommended, and it is required to deploy and build on AWS.

**Topics**
+ [Prerequisites](#setting-up-prerequisites)
+ [Connect your AWS profile](#setting-up-connect-profile)

## Prerequisites
<a name="setting-up-prerequisites"></a>

You can start using AWS Startup Advisor without an AWS account or an AWS Activate application. The following help you get the most from AWS Startup Advisor:
+  **An AWS account (recommended)** – An AWS account is not required to use AWS Startup Advisor, but we recommend one, and it is required to deploy and build on AWS. If you do not have an AWS account, create one at [the AWS sign-up page](https://portal.aws.amazon.com/billing/signup).
+  ** AWS Activate credits (optional)** – Submitting an AWS Activate Credit application is not required. If you are eligible and want to take advantage of AWS Activate credits, you are welcome to apply. When you have a submitted application, AWS Startup Advisor can use it to seed context about your startup and tailor its guidance. For more information, see [AWS Activate](https://aws.amazon.com/activate/).

## Connect your AWS profile
<a name="setting-up-connect-profile"></a>

 AWS Startup Advisor uses your AWS profile permissions to work with your configured resources.

To use the IDE extension, you sign in with an AWS CLI profile (from `~/.aws/credentials` or `~/.aws/config`), IAM Identity Center (SSO), or IAM access keys. A read-only profile is sufficient for alerts. For the sign-in steps, see [Sign in](getting-started.md#getting-started-ide-signin) in Getting started. The extension also includes **Get started** prompts that can help you set up read-only access or IAM Identity Center (SSO) access for the extension. For more information, see [Prompts](using-ide-extension.md#using-ide-extension-prompts).

The AWS credits and cost tracker widget in the AWS Startup Advisor IDE extension requires AWS billing and cost read permissions. For more information, see [Identity and access management for AWS Startups](security-iam.md).