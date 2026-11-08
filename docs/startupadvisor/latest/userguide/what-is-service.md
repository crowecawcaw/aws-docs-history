

# What is AWS Startup Advisor?
<a name="what-is-service"></a>

 AWS Startup Advisor is an AI-powered build assistant for startups. It provides AWS-vetted, Solutions Architect-curated skills and guidance for startups on account setup, architecture, Activate credits, cost, security, migration, AI, scalability, and operations. AWS Startup Advisor delivers this guidance as skills that founders and their coding agents can use. You receive recommendations directly in your development environment, so you can act on them as you build.

This guide is for startup founders and startup developers who build on AWS. You can use AWS Startup Advisor at any stage, whether you are building your product from scratch, have an existing product or service you are enhancing or scaling, or if you are migrating from another cloud provider to AWS.

**Topics**
+ [Features of AWS Startup Advisor](#servicename-feature-overview)
+ [How AWS Startup Advisor uses your startup context](#how-context-works)
+ [Are you a first-time AWS Startup Advisor user?](#first-time-user)
+ [Accessing AWS Startup Advisor](#acessing-servicename)
+ [AWS Startup Advisor pricing](#pricing)

## Features of AWS Startup Advisor
<a name="servicename-feature-overview"></a>

 AWS Startup Advisor provides a skills-based experience that helps you complete common startup tasks with AWS-vetted guidance. With AWS Startup Advisor, you can:
+  **Set up your AWS environment** – Configure IAM, billing alerts, and security baselines.
+  **Scaffold your infrastructure** – Get AWS-vetted infrastructure recommendations in your editor.
+  **Get stage-aware architecture advice** – Get AWS architecture recommendations tuned to your startup’s stage, team size, runway, and credits, or review an existing architecture before a fundraise.
+  **Deploy local code to AWS ** – Move local code to AWS, from architecture to permissions.
+  **Optimize costs** – Get specific cost-saving actions for your workloads.
+  **Harden security for your stage** – Apply security guidance that fits your stage, whether you build an MVP or sell to enterprises.
+  **Migrate to AWS ** – Move your workloads to AWS from another provider.
+  **Deploy an AI agent** – Deploy an AI agent to AWS.
+  **Operate your workload** – Investigate production incidents and run release-readiness reviews with [AWS DevOps Agent](https://aws.amazon.com/devops-agent/), which proposes fixes for you to review.
+  **Apply for AWS Activate credits** – Prepare and stage your AWS Activate credit application for you to review and submit yourself.
+  **Get answers about AWS Activate and startup programs** – Look up the AWS Activate FAQ, credits guide, programs, partner offers, and sample architectures.
+  **Use AWS-curated prompts and agents** – Copy ready-made prompts for your coding agent and download installable agents for common startup tasks.
+  **Monitor your account** – In the IDE extension, get alerts about security, cost, and scalability issues in your AWS account, and track your spend and credits with Cost & Credits.

For more information about each skill, see [Using AWS Startup Advisor skills](using-skills.md).

## How AWS Startup Advisor uses your startup context
<a name="how-context-works"></a>

 AWS Startup Advisor can pick up where your AWS Activate credit application leaves off. Instead of starting from scratch, if you applied for AWS Activate credits, you start with context about your startup. AWS Startup Advisor uses two sources to understand your tech stack and your startup’s stage:
+ The information in your AWS Activate credit application
+ Your startup’s website

 AWS Startup Advisor combines this context with expertise from AWS Startup Solutions Architects. As a result, the guidance that you receive is tailored to your startup’s stack and stage.

 AWS Startup Advisor also has context about your tech stack from your project. When you work with your AI coding agent in your source code and it invokes an AWS Startup Advisor skill, the skill can use your project to understand your actual tech stack, so the guidance reflects what you are building.

## Are you a first-time AWS Startup Advisor user?
<a name="first-time-user"></a>

If you are a first-time user of AWS Startup Advisor, we recommend that you begin by reading the following sections:
+  [Setting up AWS Startup Advisor](setting-up.md) 
+  [Getting started with AWS Startup Advisor](getting-started.md) 
+  [Using AWS Startup Advisor skills](using-skills.md) 

## Accessing AWS Startup Advisor
<a name="acessing-servicename"></a>

You can access AWS Startup Advisor in any of the following ways. You get the same skills and the same context across all of them.
+  **Web** – Get started on the web at [https://startups.aws.com/](https://startups.aws.com/).
+  **IDE extension** – Install the AWS Startup Advisor IDE extension from the marketplace for your IDE. For VS Code, download and install it from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-startup-advisor). For Cursor and Kiro, download and install it from the [Open VSX Registry](https://open-vsx.org/extension/amazonwebservices/aws-startup-advisor). The IDE extension works inside Kiro or any VS Code-based IDE.
+  **Plugin** – Install the plugin for Claude Code or Codex. Every plugin install includes the skills and configures the `aws-mcp` server.
+  **Standalone skills** – Install just the skills in other coding agents, such as Kiro, fx, or GitHub Copilot.

## AWS Startup Advisor pricing
<a name="pricing"></a>

 AWS Startup Advisor is available at no additional charge. You pay only for the AWS resources you or your agent provisions or interacts with, at standard AWS pricing. For more information, see [AWS Pricing](https://aws.amazon.com/pricing/).