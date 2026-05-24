# Setting up HealthOmics

To set up AWS HealthOmics, sign up for an AWS account,
create an administrative user, and securely manage access for additional users.

###### Topics

- [Sign up for an AWS account](#sign-up-for-aws "#sign-up-for-aws")
- [Create IAM permissions for HealthOmics](#setting-up-create-iam-user "#setting-up-create-iam-user")
- [Connect with external code repositories](#setting-up-omics-repository "#setting-up-omics-repository")
- [Using Kiro CLI with HealthOmics](#setting-up-omics-kiro-cli "#setting-up-omics-kiro-cli")
- [Using Kiro IDE with HealthOmics](#setting-up-omics-kiro-ide "#setting-up-omics-kiro-ide")

## Sign up for an AWS account

To get started with AWS, you need an AWS account. For information about creating an AWS account, see
[Getting started with an AWS account](../../../accounts/latest/reference/getting-started.md "../../../accounts/latest/reference/getting-started.md")
in the _AWS Account Management Reference Guide_.

## Create IAM permissions for HealthOmics

To use HealthOmics, configure the following IAM permissions:

- IAM identity-based policies for users in your account to access HealthOmics.
- An IAM service role for HealthOmics to access resources on your behalf.
- Permissions in other services (such as Lake Formation and Amazon ECR) for your users and the HealthOmics service to access
  resources.

For more information about configuring IAM permissions for HealthOmics, see [IAM permissions for HealthOmics](omics-permissions.md "omics-permissions.md").

## Connect with external code repositories

With AWS HealthOmics, you can manage your workflows using Git-based repositories through AWS CodeConnections. HealthOmics
uses this connection to access your source code repositories.

Before working with external code repositories, follow the
[Setting up connections](../../../dtconsole/latest/userguide/setting-up-connections.md "../../../dtconsole/latest/userguide/setting-up-connections.md")
guide to start working with AWS CodeConnections. Verify that you have created the proper IAM policies and
permissions for your AWS account. For a list of supported Git providers and more information, see
[What third-party providers can I create connections for?](../../../dtconsole/latest/userguide/welcome-connections-supported-providers.md "../../../dtconsole/latest/userguide/welcome-connections-supported-providers.md").

**Create a connection**

To create a connection with your preferred repository provider, follow the
[Create a connection](../../../dtconsole/latest/userguide/connections-create.md "../../../dtconsole/latest/userguide/connections-create.md") tutorial.

## Using Kiro CLI with HealthOmics

Kiro CLI provides natural language interactions with AWS HealthOmics, allowing you to perform complex
genomic workflows and analysis tasks using conversational commands. To use Kiro CLI, be sure to
configure IAM permissions for HealthOmics and other services (such as CloudWatch, Amazon ECR, or Amazon S3) for Kiro to
access their resources.

The [HealthOmics Agentic
generative AI tutorial](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai "https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai") provides a step-by-step guidance for configuring context files and enabling
Kiro CLI to create, run, and optimize your AWS HealthOmics workflows.

## Using Kiro IDE with HealthOmics

In addition to Kiro CLI, you can use the Kiro IDE with HealthOmics:

- [Kiro Power for HealthOmics](https://kiro.dev/powers/ "https://kiro.dev/powers/") – A curated and pre-packaged
  MCP server with steering files and agent hooks that gives the Kiro agent expertise in HealthOmics workflow
  creation and optimization.
- [Kiro IDE extension for HealthOmics](https://open-vsx.org/ "https://open-vsx.org/") – Provides syntax
  highlighting, code completion, and troubleshooting guidance for HealthOmics workflows, along with engine
  compatibility checking, performance optimization recommendations, automated run analysis with failure
  diagnostics, and workflow import/export capabilities.
