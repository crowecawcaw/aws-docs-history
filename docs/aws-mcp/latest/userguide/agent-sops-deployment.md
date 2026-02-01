# AWS Deployment SOPs

The [AWS MCP Server](getting-started-aws-mcp-server.md "getting-started-aws-mcp-server.md") includes Standard Operating Practices (SOPs) that help you deploy applications to AWS. These workflows analyze your application, make necessary code changes, and generate Infrastructure as Code (IaC) that is deployed using [AWS CloudFormation](https://aws.amazon.com/cloudformation/ "https://aws.amazon.com/cloudformation/") to host your application on AWS.

Deployment SOPs support a variety of web frameworks, including Single-Page Applications (React, Vue, Angular, and SvelteKit), Static Site Generators (Next.js static export, Nuxt 2/3, Gatsby, Hugo, Jekyll, Docusaurus, Astro, and Eleventy).

These SOPs can deploy applications in as little as one prompt. For more complex applications, your coding agent may require additional information or iterations to complete deployment. Your coding agent receives AWS security best practice recommendations from the SOPs, providing a secure starting point that you can review and customize for your requirements.

###### Note

For best results, run these SOPs with the latest AI models that can handle complex, multi-step tasks.

###### Deployment documentation

The SOPs generate documentation files and update `AGENTS.md` in your repository to track deployment progress. This also provides coding agents with context for future deployments and troubleshooting.

## Available Deployment SOPs

| SOP name              | SOP purpose                                                                                                                                                                                                                                                    |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `deploy-web-app`      | Checks if your application type is supported and selects the appropriate deployment SOP                                                                                                                                                                        |
| `deploy-frontend-app` | Generates [AWS Cloud Development Kit (CDK)](https://aws.amazon.com/cdk/ "https://aws.amazon.com/cdk/") infrastructure code and deploys it through AWS CloudFormation, providing a shareable preview URL for your website                                       |
| `setup-pipeline`      | Creates a pipeline using [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") that automatically verifies and deploys your application when changes are pushed to [GitHub](https://github.com "https://github.com") |
| `document-deployment` | Generates deployment documentation and tracks progress                                                                                                                                                                                                         |

## Prerequisites

Before you begin, you must ensure that you have set up an AWS account.

#### Sign up for an AWS account

If you do not have an AWS account, complete the following steps to create one.

###### To sign up for an AWS account

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call or text message and entering
a verification code on the phone keypad.

When you sign up for an AWS account, an _AWS account root user_ is created. The root user has access to all AWS services
and resources in the account. As a security best practice, assign administrative access to a user, and use only the root user to perform [tasks that require root user access](../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks "../../../IAM/latest/UserGuide/id_root-user.md#root-user-tasks").

AWS sends you a confirmation email after the sign-up process is
complete. At any time, you can view your current account activity and manage your account by
going to [https://aws.amazon.com/](https://aws.amazon.com/ "https://aws.amazon.com/") and choosing **My
Account**.

#### Create a user with administrative access

After you sign up for an AWS account, secure your AWS account root user, enable AWS IAM Identity Center, and create an administrative user so that you
don't use the root user for everyday tasks.

###### Secure your AWS account root user

1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as the account owner by choosing **Root user** and entering your AWS account email address. On the next page, enter your password.

For help signing in by using root user, see [Signing in as the root user](../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial "../../../signin/latest/userguide/console-sign-in-tutorials.md#introduction-to-root-user-sign-in-tutorial") in the _AWS Sign-In User Guide_. 2. Turn on multi-factor authentication (MFA) for your root user.

For instructions, see [Enable a virtual MFA device for your AWS account root user (console)](../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md "../../../IAM/latest/UserGuide/enable-virt-mfa-for-root.md") in the _IAM User Guide_.

###### Create a user with administrative access

1. Enable IAM Identity Center.

For instructions, see [Enabling
AWS IAM Identity Center](../../../singlesignon/latest/userguide/get-set-up-for-idc.md "../../../singlesignon/latest/userguide/get-set-up-for-idc.md") in the
_AWS IAM Identity Center User Guide_. 2. In IAM Identity Center, grant administrative access to a user.

For a tutorial about using the IAM Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
_AWS IAM Identity Center User Guide_.

###### Sign in as the user with administrative access

- To sign in with your IAM Identity Center user, use the sign-in URL that was sent to your email address when you created the IAM Identity Center user.

For help signing in using an IAM Identity Center user, see [Signing in to the AWS access portal](../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md "../../../signin/latest/userguide/iam-id-center-sign-in-tutorial.md") in the _AWS Sign-In User Guide_.

###### Assign access to additional users

1. In IAM Identity Center, create a permission set that follows the best practice of applying least-privilege permissions.

For instructions, see [Create a permission set](../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md "../../../singlesignon/latest/userguide/get-started-create-a-permission-set.md") in the _AWS IAM Identity Center User Guide_. 2. Assign users to a group, and then assign single sign-on access to the group.

For instructions, see [Add groups](../../../singlesignon/latest/userguide/addgroups.md "../../../singlesignon/latest/userguide/addgroups.md") in the _AWS IAM Identity Center User Guide_.

Depending on your application, additional prerequisites will vary. The SOP will guide your coding agent to verify these:

- [AWS MCP Server](getting-started.md "getting-started.md") installed and enabled in your AI coding assistant (such as Kiro or Cursor)
- [Git Command Line Interface (CLI)](https://git-scm.com/install/ "https://git-scm.com/install/") installed and configured
- [AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") configured with valid credentials
- Appropriate package manager (such as `npm`, `yarn`, or `pnpm`)

## Supported Use Cases

One-prompt deployment that provides a link (URL) to your website that can be shared with others.

###### Supported application types

- Single-Page Applications (SPAs): React, Vue, Angular, SvelteKit
- Static Site Generators (SSGs): Next.js (static export), Nuxt, Gatsby, Hugo, Jekyll, Docusaurus, Astro, Eleventy
- Static websites

###### Steps the coding agent takes

1. Scans project structure to identify the application framework
2. Detects build configuration and adjusts settings as needed
3. Generates infrastructure code using AWS Cloud Development Kit (CDK)
4. Deploys infrastructure to AWS using AWS CloudFormation
5. Provides a link (URL) for your application on AWS

###### Technical explanation

Your coding agent analyzes your application to determine if it can be deployed as a static website on AWS. It generates AWS CDK code defining the required hosting infrastructure and compiles your application. A personal preview stack is then provisioned using AWS CloudFormation, which uploads your code to [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") and serves it through [Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/"). The SOP prompts your coding agent to apply security best practices to Amazon S3 and Amazon CloudFront resources. Always review the generated configuration before deploying to production environments.

Creates a CI/CD pipeline with GitHub integration and quality gates for deploying to production or staging environments.

###### Requirements

Your application must already be configured as a CDK application. This SOP works best when used after the `deploy-webapp` SOP.

###### Manual steps required

- Requires manual approval of a [AWS CodeConnections](../../../dtconsole/latest/userguide/welcome-connections.md "../../../dtconsole/latest/userguide/welcome-connections.md") resource to GitHub in web browser. This requires appropriate permissions to install and configure GitHub Apps in your repository or organization.

###### Steps the coding agent takes

1. Scans project structure to understand the application
2. Configures CodeConnections to connect AWS to your GitHub repository
3. Generates infrastructure code to create an AWS CodePipeline pipeline
4. Adds quality gates (static code analysis, unit tests, and security scans when available in your application)
5. Deploys the pipeline using a ([CDK Pipeline](../../../cdk/v2/guide/cdk-pipeline.md "../../../cdk/v2/guide/cdk-pipeline.md")) module

###### Technical explanation

The coding agent verifies your application has existing AWS CDK infrastructure code, then generates infrastructure code to create an [AWS CodePipeline](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/") pipeline and supporting resources. Once provisioned, the pipeline automatically builds and deploys your application whenever changes are pushed to the configured branch in GitHub. The SOP prompts your coding agent to apply security best practices to [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") and [Amazon CloudFront](https://aws.amazon.com/cloudfront/ "https://aws.amazon.com/cloudfront/") resources. Always review the generated configuration before deploying to production environments.

## Security Features

###### Note

The AWS shared responsibility model applies to data protection when using the SOPs in AWS MCP Server. Coding Agents can make mistakes and may omit recommended security defaults provided in the SOPs. Double-check responses. Read more about the [shared responsibility model in AWS MCP Server](data-protection.md "data-protection.md").

Deployment SOPs prompt coding agents to implement the following security best practices by default:

- _Private Amazon S3 Buckets:_ Blocks all public access to stored content
- _Encryption at rest:_ Enables Amazon S3 managed encryption for all stored content
- _HTTPS enforcement:_ Requires TLS 1.2 or higher with automatic HTTPS redirect
- _Origin Access Control (OAC):_ Configures Amazon CloudFront to access Amazon S3 through the AWS internal network
- _AWS IAM least privilege:_ Applies minimal required permissions for each service
- _Security scanning:_ Automatically detects exposed secrets in your codebase
- _Quality gates:_ Runs available unit tests and static code analysis before deployment
