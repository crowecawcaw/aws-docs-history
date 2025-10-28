# Getting started with Amazon Q Developer generative AI chat and

command line tools

###### Note

Powered by Amazon Bedrock: Amazon Q Developer is built on Amazon Bedrock and includes [automated abuse detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md")
implemented in Amazon Bedrock to enforce safety, security, and the responsible use of AI.

In this Getting Started procedure, you will use Amazon SageMaker Unified Studio, SageMaker Catalog, Sagemaker
Lakehouse sample data, and Amazon Q Developer generative AI tools to analyze code in the JupyterLab
IDE. The Amazon Q Developer tools include Q chat and Q CLI.

Amazon Q Developer provides an agentic chat feature supporting read and write operations in the
notebook (Code Editor, JupyterLab) with workspace context awareness. With Amazon Q chat, you can
chat about AWS services, your development project, your data pipelines, and related topics.
The Amazon Q CLI provides intelligent, contextual assistance for error debugging and development
tasks, and it can run complex command line tasks for you.

###### Warning

Generative AI may give inaccurate responses. Avoid sharing sensitive information.
Chats may be visible to others in your organization.

For reference information about implementing Amazon Q Developer in Amazon SageMaker Unified Studio, see [Using Amazon Q Developer with Amazon SageMaker Unified Studio](q-actions.md "q-actions.md").

###### Topics

- [Discover Amazon Q Developer in Amazon SageMaker Unified Studio](#qdeveloper-integration-overview "#qdeveloper-integration-overview")
- [Considerations for using the
  Amazon Q Developer feature](#qdeveloper-integration-considerations "#qdeveloper-integration-considerations")
- [Prerequisites for using the
  Amazon Q Developer feature](#qdeveloper-integration-prerequisites "#qdeveloper-integration-prerequisites")
- [Getting started using Q chat](qdeveloper-integration-start-chat.md "qdeveloper-integration-start-chat.md")
- [Getting started with Q CLI](qdeveloper-integration-start-CLI.md "qdeveloper-integration-start-CLI.md")

## Discover Amazon Q Developer in Amazon SageMaker Unified Studio

You can use Agentic AI tools through Amazon Q Developer tools that use context and agents to
summarize, analyze, perform tasks, and work on your code with you. In your JupyterLab notebook
or Code Editor, you can use the Amazon Q chat and Amazon Q CLI tools to understand and configure
your Amazon SageMaker Unified Studio project files. For more information about Amazon Q Developer, see [What is
Amazon Q Developer](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md") in the _Amazon Q Developer User Guide_.

## Considerations for using the

Amazon Q Developer feature

The following considerations apply for working with Amazon Q Developer in Amazon SageMaker Unified Studio.

- For Q CLI, for domains using the Amazon Q Free Tier, you will be automatically logged
  in. For domains using the Amazon Q Pro Tier, you will be prompted to login. You can use the
  AWS access portal URL (also called the Start URL) associated with the IAM Identity Center login
  attached to the domain and the IDC region for login. Q CLI will then use the profile and
  subscription the admin creates following the steps detailed in [Enable
  Amazon Q Developer Pro](../adminguide/amazonq.md#amazonq-enable "../adminguide/amazonq.md#amazonq-enable").

###### Note

If there is only one profile set up, then that is the profile that Q CLI will use.
If there are multiple profiles set up, then Q CLI prompts you to choose one. Choose the
profile associated with the domain.

- When you enable Amazon Q, you can choose between the Free or Pro tiers of the service.
  JupyterLab in the default space supports both the free and paid tiers. However, in
  additional spaces, JupyterLab and Code Editor support the Free Tier only.
- The level of use for the Q chat and Q CLI are set by the tier availability as detailed
  on the pricing page at [Amazon Q Developer
  Pricing](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/").

###### Note

When using the Free Tier, request limits are shared at the account level, meaning that
one customer can potentially use up all requests. The Pro Tier of Amazon Q is charged at the
user level, with limits set at the user level as well. The Pro Tier also lets you manage
users and policies with enterprise access control.

## Prerequisites for using the

Amazon Q Developer feature

The following prerequisities are required for this getting started procedure.

- You must have access to a SageMaker Unified Studio domain and project. Create a project with an **All capabilities** project profile. This project profile sets up
  your project with access to S3 and Athena resources. For more information, see [Projects](projects.md "projects.md").
- To use the Amazon Q Developer chat and CLI features in Amazon SageMaker Unified Studio feature, you need access to a
  domain where Amazon Q Developer is configured.

If the domain is set to use the Free Tier, you will have access to Q chat and Q CLI in
JupyterLab without any additional login. For the Pro Tier, your administrator must set up
a profile, subscribe users, and attach the profile to the Amazon SageMaker Unified Studio domain. In Q CLI, you
can then use the start URL and IDC region to sign in with a Pro Tier license. See [Enable
Amazon Q Developer Pro](../adminguide/amazonq.md#amazonq-enable "../adminguide/amazonq.md#amazonq-enable").

For more information, see [Using the coding assistant](using-the-coding-assistant.md "using-the-coding-assistant.md").
