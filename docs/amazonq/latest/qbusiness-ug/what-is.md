# What is Amazon Q Business?

|                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \*_Powered by Amazon Bedrock:_<br>• AWS implements [automated<br>abuse detection](../../../bedrock/latest/userguide/abuse-detection.md "../../../bedrock/latest/userguide/abuse-detection.md"). Because Amazon Q Business is built on Amazon Bedrock, users can take full<br>advantage of the controls implemented in Amazon Bedrock to enforce safety, security, and the<br>responsible use of artificial intelligence (AI). |

Amazon Q Business is a fully managed, generative-AI powered assistant that you can
configure to answer questions, provide summaries, generate content, and complete tasks based on
your enterprise data. It allows end users to receive immediate, permissions-aware responses from
enterprise data sources with citations, for use cases such as IT, HR, and benefits help
desks.

Amazon Q Business also helps streamline tasks and accelerate problem solving. You can
use Amazon Q Business to create and share task automation applications, or perform routine
actions like submitting time-off requests and sending meeting invites.

Amazon Q Business integrates with services like [Amazon Kendra](../../../kendra/latest/dg/what-is-kendra.md "../../../kendra/latest/dg/what-is-kendra.md") and [other
supported data sources](supported-connectors.md "supported-connectors.md") such as [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md"), [Microsoft SharePoint](sharepoint-cloud-connector.md "sharepoint-cloud-connector.md"), and [Salesforce](salesforce-connector.md "salesforce-connector.md").

To get started with Amazon Q Business, visit [Amazon Q Business](https://aws.amazon.com/q/business/ "https://aws.amazon.com/q/business/").

|     |
| --- |
|     |

###### Topics

- [Benefits of Amazon Q Business](#benefits-overview "#benefits-overview")
- [Pricing and availability](#pricing "#pricing")
- [Accessing Amazon Q Business](#accessing "#accessing")
- [Related services](#related-services "#related-services")
- [Are you a first-time Amazon Q Business user?](#first-time-user "#first-time-user")

## Benefits of Amazon Q Business

Some of the benefits of Amazon Q Business include:

**Accurate and comprehensive answers**

Amazon Q Business generates comprehensive responses to natural language
queries from users by analyzing information across all enterprise content that it has
access to. It can avoid incorrect statements by confining its generated responses to
existing enterprise data, and provides citations to the sources that it used to generate
its response. When a query results in conflicting or inconsistent answers, Amazon Q Business lists the details for each answer. With [hallucination mitigation](guardrails-global-controls.md#guardrails-global-response "guardrails-global-controls.md#guardrails-global-response"), Amazon Q Business checks
supported chat responses for inconsistencies and automatically corrects them in
real-time during conversations.

**Simple to deploy and manage**

Amazon Q Business takes care of the complex task of developing and managing
machine learning infrastructure and models so that you can build your chat solution
quickly. Amazon Q Business connects to your data and ingests it for processing
using its pre-built connectors, document retrievers, document upload
capabilities.

**Configurable and customizable**

Amazon Q Business provides you with the flexibility of choosing what sources
should be used to respond to user queries. You can control whether the responses should
only use your enterprise data, or use both enterprise data and model knowledge. For
public-facing scenarios, you can create [anonymous applications](create-anonymous-application.md "create-anonymous-application.md") that don't require user
authentication, allowing you to serve a broader audience. You can [customize your chat interface](customize-web-experience.md "customize-web-experience.md") with your organization's branding, visual
themes, and conversation starters to create a tailored user interface.

**Data and application security**

Amazon Q Business supports access control for your data so that the right
users can access the right content. Its responses to questions are based on the content
that your end user has permissions to access. You can use AWS IAM Identity Center or AWS Identity and Access Management to
manage end user access for Amazon Q Business.

**Broad connectivity**

Amazon Q Business offers out-of-the-box connections to [multiple supported data sources](supported-connectors.md "supported-connectors.md"). You can also connect Amazon Q to
any third-party application using [plugins](plugins.md "plugins.md") to perform actions and query application data.
With [data accessors](data-accessors.md "data-accessors.md"), you can securely share your enterprise data with verified
ISVs, allowing them to retrieve relevant content from your Amazon Q index.
Amazon Q Business
[integrations](integrations.md "integrations.md") bring AI-powered assistance directly into daily workflows
through browser extensions and applications for Slack, Microsoft Teams, and Microsoft
Office. You can also [embed Amazon Q Business](embed-amazon-q-business.md "embed-amazon-q-business.md") directly into your applications and websites to
enhance user productivity.

## Pricing and availability

Amazon Q Business charges you both for user subscriptions to applications, and for
index capacity. For information about what's included in the tiers of user subscriptions and
index capacity, see [Subscription and index pricing](tiers.md "tiers.md").

For pricing information, including examples of charges for index capacity, subscribing and
unsubscribing users to Amazon Q Business tiers, upgrading and downgrading Amazon Q Business tiers, and more, see [Amazon Q Business Pricing](https://aws.amazon.com/q/business/pricing "https://aws.amazon.com/q/business/pricing").

For a list of regions where Amazon Q Business is currently available, see [Supported
regions](quotas-regions.md "quotas-regions.md").

## Accessing Amazon Q Business

You can access Amazon Q Business in the following ways in the AWS Regions that
it's available in:

**[AWS Management Console](https://aws.amazon.com/console/ "https://aws.amazon.com/console/")**

You can use the AWS Management Console—a browser-based interface to interact with
AWS services—to access the Amazon Q Business console and resources. You
can perform most Amazon Q Business tasks using the Amazon Q Business
console.

**[Amazon Q Business API](../api-reference/Welcome.md "../api-reference/Welcome.md")**

To access Amazon Q Business programmatically, you can use the Amazon Q API. For more information, see the [Amazon Q Business API
Reference](../api-reference/Welcome.md "../api-reference/Welcome.md").

**[AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/")**

The AWS Command Line Interface (AWS CLI) is an open source tool. You can use the AWS CLI to interact with
AWS services using commands in your command line shell. If you want to build
task-based scripts, using the command line can be faster and more convenient than using
the console.

**[SDKs](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/")**

AWS SDKs provide language APIs for AWS services to use programmatically.

## Related services

The following are some of the other AWS services that Amazon Q Business integrates
with:

**[Amazon Kendra](../../../kendra/latest/dg/what-is-kendra.md "../../../kendra/latest/dg/what-is-kendra.md")**

Amazon Kendra is an intelligent search service that uses natural language
processing and machine learning algorithms to return specific answers from your data for
end user queries. If you're already an Amazon Kendra user, you can use Amazon Kendra as a data retriever for your Amazon Q Business web application.

**[Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md")**

Amazon S3 is an object storage service. If you're an Amazon S3 user,
you can use Amazon S3 as a data source for your Amazon Q Business
application.

**[Quick](../../../quicksight/latest/user/what-is-quicksight.md "../../../quicksight/latest/user/what-is-quicksight.md")**

Quick is a business intelligence service that helps you create and share
interactive dashboards and reports. You can [integrate Amazon Q Business with Quick](create-application-quicksight.md "create-application-quicksight.md")
to enable users to ask natural language questions about their data and receive
AI-generated insights directly within their dashboards.

## Are you a first-time Amazon Q Business user?

If you're a first-time user of Amazon Q Business, we recommend that you read the
following sections in order:

**[How it
works](how-it-works.md "how-it-works.md")**

Introduces Amazon Q Business components and describes how they work to create
your Retrieval Augmented Generation (RAG) solution.

**[Key
concepts](concepts-terms.md "concepts-terms.md")**

Explains key concepts and important Amazon Q Business terminology.

**[Setting
up](setting-up.md "setting-up.md")**

Outlines how to set up Amazon Q Business so that you can begin creating your
Amazon Q Business application and web experience.

**[Creating an application](create-application.md "create-application.md")**

Explains how to create the Amazon Q Business application integrated with
IAM Identity Center.

**[Connecting Amazon Q Business data source connectors](supported-connectors.md "supported-connectors.md")**

Configuration information for specific connectors to use with your Amazon Q Business web experience.
