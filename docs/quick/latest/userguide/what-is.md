# What is Amazon Quick?

###### Note

Amazon QuickSight has been rebranded to Amazon Quick, expanding from a standalone business
intelligence service to a comprehensive analytics and AI platform. QuickSight continues as
Amazon Quick Sight, a core component within the Quick ecosystem. Amazon Quick Sight retains existing functionality including interactive data visualization,
SPICE in-memory analytics, embedded analytics, and dashboard sharing. All existing
QuickSight APIs, SDKs, and integrations continue to work without changes.

Amazon Quick is a comprehensive, generative AI-powered business intelligence platform that
makes it easy to analyze data, create visualizations, automate workflows, and collaborate
across your organization. The service combines traditional business intelligence
capabilities with modern AI assistance, requiring no machine learning expertise to use. You
can connect to diverse data sources, create interactive dashboards, build intelligent
automations, and get immediate insights through natural language conversations with AI
agents.

Quick includes six integrated capabilities that work together: Amazon Quick Sight for
data visualization, Amazon Quick Flows for workflow automation, Amazon Quick Automate for process
optimization, Amazon Quick Index for data discovery, and Amazon Quick Research for
comprehensive analysis. The platform extends beyond traditional BI by bringing AI assistance
directly into your existing tools through extensions for browsers, Slack, and Microsoft
Office applications. You can also build and publish interactive web applications using
apps in Amazon Quick. For more information, see
[Build web applications with apps in Amazon Quick](using-amazon-quick-apps.md "using-amazon-quick-apps.md").

###### Topics

- [Benefits of Quick](#benefits-overview "#benefits-overview")
- [Pricing and availability](#pricing "#pricing")
- [Accessing Quick](#accessing "#accessing")
- [Related services](#related-services "#related-services")
- [Quick user types](#user-personas "#user-personas")
- [Are you a first-time Quick user?](#first-time-user "#first-time-user")

## Benefits of Quick

Some of the benefits of Quick include:

**AI-powered analysis and visualization**

Quick analyzes natural language queries across enterprise
content and creates interactive dashboards from multiple data sources. You
can combine diverse data types including AWS data, third-party data, big
data, spreadsheets, SaaS data, and B2B data within a unified analytical
environment. Custom AI agents provide domain-specific expertise and automate
analytical tasks through conversational interfaces.

**Simple to deploy and manage**

Quick provides all machine learning infrastructure, models,
and pre-built connectors with SPICE in-memory engine for analytics. As a
fully managed service, it requires no infrastructure deployment or
management, allowing you to focus on gaining insights from your data.

**Enterprise-grade security and governance**

Quick supports comprehensive security through granular
permissions and row-level security controls. You can access the system
through federation and single sign-on capabilities. All data is protected
with secure encryption at rest and in transit. The platform integrates with
IAM Identity Center while ensuring all responses and visualizations respect your
permissions.

**Collaboration and workflow automation**

Quick enables seamless sharing of dashboards and insights
across your organization. You can create embedded analytics for applications
and websites, configure AI responses using enterprise data sources, and
automate routine tasks to streamline workflows. Data and resources can be
organized into dedicated project spaces for efficient knowledge sharing and
task completion.

## Pricing and availability

Amazon Quick offers flexible pricing depending on how you access the service.

**Free/Plus accounts (quick.aws.com)**

Standalone accounts offer Free, Free Trial Plus, and Paid Plus plans. For current pricing details, plan limits, and feature comparisons, see [Quick pricing](https://aws.amazon.com/quick/pricing/ "https://aws.amazon.com/quick/pricing/").

**AWS Console accounts**

Console accounts follow standard AWS billing with user subscriptions
and data capacity charges. For information about subscription types and
pricing, see [Quick pricing](https://aws.amazon.com/quicksuite/pricing/ "https://aws.amazon.com/quicksuite/pricing/").

The following table summarizes the features available for each account type.

| Feature                                         | Free and Plus | Professional and Enterprise |
| ----------------------------------------------- | ------------- | --------------------------- |
| Chat with AI                                    | ✓             | ✓                           |
| Chat agents                                     | ✓             | ✓                           |
| Spaces                                          | ✓             | ✓                           |
| Amazon Quick Flows                              | ✓             | ✓                           |
| Research                                        | ✓             | ✓                           |
| Apps                                            | ✓             | ✓                           |
| Extensions                                      | ✓             | ✓                           |
| Desktop application                             | ✓             | ✓                           |
| Integrations and connectors                     | ✓             | ✓                           |
| Amazon Quick Sight dashboards and analytics     | —             | ✓                           |
| Amazon Quick Automate                           | —             | ✓                           |
| API access                                      | —             | ✓                           |
| IAM Identity Center and IAM identity management | —             | ✓                           |
| AWS Management Console administration           | —             | ✓                           |

For a list of Regions where Quick is currently available, see [Quick
endpoints and quotas](../../../general/latest/gr/quicksight.md "../../../general/latest/gr/quicksight.md") and [AWS Regions,
websites, IP address ranges, and endpoints](../../../quicksuite/latest/userguide/regions.md "../../../quicksuite/latest/userguide/regions.md").

## Accessing Quick

You can access Quick in the following ways:

**[Amazon Quick standalone (quick.aws.com)](https://quick.aws.com "https://quick.aws.com")**

You can sign up for Amazon Quick directly at [https://quick.aws.com](https://quick.aws.com "https://quick.aws.com") without an
existing AWS account. You can sign up using your email address or
social login credentials. Accounts are available in Free, Free Trial Plus, and Paid Plus
plan tiers. This is the fastest way to get started with Amazon Quick for
individuals and small teams. For more information, see [Signing up at quick.aws.com](../../../quicksuite/latest/userguide/standalone-signup.md "../../../quicksuite/latest/userguide/standalone-signup.md").

**[AWS Management Console](https://aws.amazon.com/console/ "https://aws.amazon.com/console/")**

If your organization uses AWS, you can access Quick through
the AWS Management Console. Console accounts use IAM Identity Center or IAM for authentication and
follow standard AWS billing. You can perform most Quick
administration tasks using the AWS Management Console. For more information, see [Signing up through the AWS Console](../../../quicksuite/latest/userguide/signing-up.md "../../../quicksuite/latest/userguide/signing-up.md").

**[Amazon Quick API](../../../quicksight/latest/APIReference/Welcome.md "../../../quicksight/latest/APIReference/Welcome.md")**

To access Amazon Quick Sight and some Quick programmatically, you can use
the Amazon Q API. For more information, see the [Quick Sight API Reference](../../../quicksight/latest/APIReference/Welcome.md "../../../quicksight/latest/APIReference/Welcome.md").

**[AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/")**

The AWS Command Line Interface (AWS CLI) is an open source tool. You can use the AWS CLI to
interact with AWS services using commands in your command line shell. If
you want to build task-based scripts, using the command line can be faster
and more convenient than using the console.

**[SDKs](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/")**

AWS SDKs provide language APIs for AWS services to use
programmatically.

## Related services

The following are some of the other AWS services that Quick integrates
with:

**[Amazon Q Business](../../../amazonq/latest/qbusiness-ug/what-is.md "../../../amazonq/latest/qbusiness-ug/what-is.md")**

Amazon Q Business is a fully managed, generative-AI powered
assistant that you can configure to answer questions, provide summaries,
generate content, and complete tasks based on your enterprise data. If
you're already an Amazon Q Business user, you can connect your Amazon Q Business application to Quick.

## Quick user types

There are three user personas that Quick supports—readers, authors, and
admins. Each persona has both standard and Pro subscription types, with Pro
subscriptions providing access to advanced Amazon Quick tools. For detailed information
about subscription types and pricing, see [Quick pricing](https://aws.amazon.com/quicksuite/pricing/ "https://aws.amazon.com/quicksuite/pricing/").

**Readers**

You can use Quick to access company data and find answers
through chat interactions with AI agents. You can upload files, run
automations, create visualizations, and share spaces via direct links. While
you cannot create datasets or agents as a reader, you are the primary
consumer of prepared analytics and AI chat tools.

**Authors**

As a domain expert, you can build and manage Quick resources.
In addition to reader capabilities, you can create datasets, dashboards,
automations, and agents. You have expanded sharing permissions for spaces
and can use AI to create visualizations, enabling you to build the data
infrastructure that supports readers.

**Administrators**

You can oversee the Quick system by managing user access,
monitoring costs, and maintaining data sources. You have full reader and
author capabilities but focus primarily on system administration to ensure
efficient and secure operations for all users.

## Are you a first-time Quick user?

If you're a first-time admin user of Quick, we recommend that you read the
following sections in order:

**[How it
works](../../../quicksuite/latest/userguide/how-quicksuite-works.md "../../../quicksuite/latest/userguide/how-quicksuite-works.md")**

Introduces Quick components and describes how they
work.

**[Key
concepts](../../../quicksuite/latest/userguide/quicksight-terminology.md "../../../quicksuite/latest/userguide/quicksight-terminology.md")**

Explains key concepts and important Quick terminology.

**[Setting up](../../../quicksuite/latest/userguide/setting-up.md "../../../quicksuite/latest/userguide/setting-up.md")**

Outlines how to set up Quick so that you can begin using
it.

If you want to get started with Amazon Quick without an AWS account, you can sign
up directly at [quick.aws.com](https://quick.aws.com "https://quick.aws.com"). See [Signing up at quick.aws.com](../../../quicksuite/latest/userguide/standalone-signup.md "../../../quicksuite/latest/userguide/standalone-signup.md") for step-by-step instructions.
