

# Setting up AWS Startup Advisor
<a name="setting-up"></a>

Before you use AWS Startup Advisor, review the following. You can use AWS Startup Advisor without an AWS account, but an AWS account is recommended, and it is required to deploy and build on AWS.

**Topics**
+ [Prerequisites](#setting-up-prerequisites)
+ [Connect your AWS profile](#setting-up-connect-profile)
+ [Local prerequisites for the plugin and skills](#setting-up-local-prerequisites)

## Prerequisites
<a name="setting-up-prerequisites"></a>

You can start using AWS Startup Advisor without an AWS account or an AWS Activate application. The following help you get the most from AWS Startup Advisor:
+  **An AWS account (recommended)** – An AWS account is not required to use AWS Startup Advisor, but we recommend one, and it is required to deploy and build on AWS. If you do not have an AWS account, create one at [the AWS sign-up page](https://portal.aws.amazon.com/billing/signup).
+  ** AWS Activate credits (optional)** – Submitting an AWS Activate Credit application is not required. If you are eligible and want to take advantage of AWS Activate credits, you are welcome to apply. When you have a submitted application, AWS Startup Advisor can use it to seed context about your startup and tailor its guidance. For more information, see [AWS Activate](https://aws.amazon.com/activate/).

## Connect your AWS profile
<a name="setting-up-connect-profile"></a>

 AWS Startup Advisor uses your AWS profile permissions to work with your configured resources.

To use the IDE extension, you sign in with an AWS CLI profile (from `~/.aws/credentials` or `~/.aws/config`), IAM Identity Center (SSO), or IAM access keys. A read-only profile is sufficient for alerts. For the sign-in steps, see [Sign in](getting-started.md#getting-started-ide-signin) in Getting started. The extension also includes **Get started** prompts that can help you set up read-only access or IAM Identity Center (SSO) access for the extension. For more information, see [Prompts](using-ide-extension.md#using-ide-extension-prompts).

The **Cost & Credits** view in the AWS Startup Advisor IDE extension requires AWS billing and cost read permissions. For more information, see [Identity and access management for AWS Startups](security-iam.md).

## Local prerequisites for the plugin and skills
<a name="setting-up-local-prerequisites"></a>

When you use the plugin or the skills in a coding agent, some tools must be present on your machine. You need these only for the skills that use them, so you can start without all of them.
+  ** AWS account and local AWS credentials** – Needed only when a skill inspects or provisions resources. Skills that only search documentation or provide reference guidance need no credentials. We recommend that you start with read-only credentials for discovery, advice, and estimation.
+  ** `uv` ** – Required for the `aws-mcp` server. To install `uv`, see [the uv documentation](https://docs.astral.sh/uv/).
+  **Python 3** – Required for the bundled validation scripts.
+  **Git** – Required because the `llm-to-bedrock` skill delivers its changes on a branch.

The following are optional:
+  **Heroku CLI, Azure CLI, or gcloud CLI (authenticated)** – For live discovery when you migrate from those providers.
+  **Terraform** – To run `fmt`, `init`, and `validate` on generated Terraform.

Setting up AWS DevOps Agent for the **Operate** capabilities needs a one-time IAM setup that your coding agent performs with your credentials, only after you approve it. It is not administrator access, and nothing is enabled or charged before then. For the permissions this setup uses, see [Permissions for AWS DevOps Agent](security-iam-devops-agent.md).