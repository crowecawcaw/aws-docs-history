# Deployment SOPs

The AWS MCP Server includes Standard Operating Procedures (SOPs) that deploy applications to AWS. These SOPs analyze your application, generate Infrastructure as Code (IaC) using the [AWS Cloud Development Kit (CDK)](../../../cdk/v2/guide/home.md "../../../cdk/v2/guide/home.md"), and deploy it through [AWS CloudFormation](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md").

Deployment SOPs support single-page applications, static site generators, Supabase-backed applications (such as Lovable.dev and Bolt.new), and static websites. These SOPs can deploy applications with minimal prompting. For complex applications, your coding agent may require additional information or iterations to complete the deployment.

Your coding agent is guided by AWS security best practice recommendations from the SOPs, providing a secure starting point from where you can review and customize for your requirements.

## Quick start

1. Install the AWS MCP Server. For instructions, see [Setting up your AWS MCP Server](getting-started-aws-mcp-server.md "getting-started-aws-mcp-server.md").
2. Log in to the AWS CLI. For instructions, see [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md").
3. Prompt your coding agent: `Deploy my app to AWS`

## Available deployment types

Deploys applications built with modern frontend frameworks to [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") and [Amazon CloudFront](../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md "../../../AmazonCloudFront/latest/DeveloperGuide/Introduction.md"). Generates CDK infrastructure code and deploys it through AWS CloudFormation, providing a shareable preview URL.

Supported application types: React, Vue, Angular, SvelteKit, Next.js (static export), Nuxt 2/3, Gatsby, Hugo, Jekyll, Docusaurus, Astro, Eleventy. Other frameworks may require you to provide additional guidance to your coding agent, or perform manual updates after the deployment.

For more information, see [Frontend applications](agent-sops-deployment-frontend.md "agent-sops-deployment-frontend.md").

Deploys applications built with Supabase to your AWS account. Your database and authentication remain in Supabase, while Edge Functions migrate to [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") and [Amazon API Gateway](../../../apigateway/latest/developerguide/welcome.md "../../../apigateway/latest/developerguide/welcome.md"). Stores secrets in [AWS Secrets Manager](../../../secretsmanager/latest/userguide/intro.md "../../../secretsmanager/latest/userguide/intro.md"). Generates CDK infrastructure code and deploys through CloudFormation, providing a shareable preview URL.

Supported application types: Applications with environment-based Supabase configuration (`supabase/config.toml`), such as Lovable.dev and Bolt.new.

For more information, see [Supabase applications](agent-sops-deployment-supabase.md "agent-sops-deployment-supabase.md").

Creates a CI/CD pipeline using [AWS CodePipeline](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md") that automatically builds, tests, and deploys your application when changes are pushed to your source repository.

Supported application types: All applications deployed using Deployment SOPs.

For more information, see [Set up CodePipeline](agent-sops-deployment-pipeline.md "agent-sops-deployment-pipeline.md").

## How the SOPs work

The SOPs provide step-by-step instructions that your coding agent follows. Your coding agent inspects the application, generates CDK infrastructure code, and deploys using CloudFormation. Application code is modified to support deployment to AWS, which includes changing how secrets are obtained, how edge functions are wrapped for AWS Lambda, and, in some cases, frontend build configurations. The SOPs instruct your coding agent to avoid modifying application code unless required for deployment.

Your coding agent may ask your permission to use a tool or request additional information such as application secret keys. Where possible, your coding agent derives information from available source code.

The SOPs generate documentation in your repository to track deployment progress and provide context for future deployments.

In some situations, you may need to prompt your coding agent to fix inconsistencies, particularly with larger applications or older models with smaller context windows.

## Prerequisites

###### AI model requirements

Testing showed best results with the following models:

- Anthropic Claude Opus 4.6 (200k, 1M)
- Anthropic Claude Opus 4.5 (200k)
- Anthropic Claude Sonnet 4.5
- OpenAI GPT-5.2-Codex
- OpenAI GPT-5.3-Codex
- Google Gemini 3 Pro

###### Tooling prerequisites

Before you begin, ensure that you have an AWS account with appropriate permissions. For instructions, see [Setting up your AWS MCP Server](getting-started-aws-mcp-server.md "getting-started-aws-mcp-server.md").

Additional prerequisites vary depending on your application. The SOP guides your coding agent to verify these automatically:

- AWS MCP Server — configured in your AI coding assistant (such as Kiro or Cursor). For setup instructions see [Setting up your AWS MCP Server](getting-started-aws-mcp-server.md "getting-started-aws-mcp-server.md")
- [Git CLI](https://git-scm.com/install/ "https://git-scm.com/install/") — Installed and configured
- [AWS CLI](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md") — Configured with valid credentials. For setup instructions see [Set up the AWS CLI](../../../streams/latest/dev/setup-awscli.md "../../../streams/latest/dev/setup-awscli.md")
- AWS CDK CLI — Version 2.x configured. For setup instructions see [Getting started with the AWS CDK](../../../cdk/v2/guide/getting-started.md "../../../cdk/v2/guide/getting-started.md")
- Package manager — npm, yarn, pnpm, or bun as required by your project

## Security features

###### Note

The [AWS shared responsibility model](data-protection.md "data-protection.md") applies to data protection when using Deployment SOPs in AWS MCP Server. Always review generated infrastructure code before deploying. Your coding agent may not apply all recommended security defaults. For more information, see [Data protection](data-protection.md "data-protection.md").

Deployment SOPs prompt your coding agent to implement the following security best practices:

- _Private Amazon S3 buckets_ — Blocks all public access to stored content
- _Encryption at rest_ — Enables Amazon S3 managed encryption for all stored content
- _HTTPS enforcement_ — Requires TLS 1.2 or higher with automatic HTTPS redirect
- _Origin Access Control (OAC)_ — Configures Amazon CloudFront to access Amazon S3 through the AWS internal network
- _AWS IAM least privilege_ — Applies minimal required permissions for each service

When you combine it with the CodePipeline SOP, you have access to additional quality controls that include:

- _Security scanning_ — Detects exposed secrets in your codebase during each build
- _Quality gates_ — Runs available unit tests and static code analysis before deployment

## Limitations

The Deployment SOPs work using local code agent capabilities, and depend upon the LLM you select. Large applications, such as those with over 25 APIs functions, may have reliability issues. If that happens, prompt your coding agent to test the application or API and fix the problems it finds.

## Pricing

With Deployment SOPs, you pay only for the AWS resources you use and any applicable data transfer costs. The Deployment SOPs have no additional charges. For more information about AWS pricing, see [AWS Pricing](https://aws.amazon.com/pricing/ "https://aws.amazon.com/pricing/"). If you are new to AWS, you can get started with many services for free. For more information, see [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/").
