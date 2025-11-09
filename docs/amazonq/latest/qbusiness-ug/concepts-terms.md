# Key concepts of Amazon Q Business

This section describes the key concepts and terms related to Amazon Q Business.

###### Topics

- [Agentic RAG](#agentic-retrieval-augmented-generation "#agentic-retrieval-augmented-generation")
- [Application environment](#web-app "#web-app")
- [ACLs (Access Control Lists)](#acls "#acls")
- [Amazon Q Apps](#q-apps "#q-apps")
- [Analytics dashboard](#analytics-dashboard "#analytics-dashboard")
- [Audio and video extraction](#audio-video-extraction "#audio-video-extraction")
- [Browser extensions](#browser-extensions "#browser-extensions")
- [Chat orchestration](#chat-orchestration "#chat-orchestration")
- [Custom document enrichment](#cde "#cde")
- [Data accessors](#data-accessors "#data-accessors")
- [Data source](#data-source "#data-source")
- [Data source connector](#connector "#connector")
- [Document](#document "#document")
- [Document attributes](#doc-attribute "#doc-attribute")
- [Field mappings](#mappings "#mappings")
- [Filtering using document attributes](#filtering "#filtering")
- [Foundation model](#fm "#fm")
- [Guardrails](#guardrails "#guardrails")
- [Hallucination](#hallucination "#hallucination")
- [Hallucination mitigation](#hallucination-mitigation "#hallucination-mitigation")
- [IAM Identity Center](#sso "#sso")
- [Identity Federation through IAM](#iam "#iam")
- [Identity provider](#idp "#idp")
- [Index](#index "#index")
- [Index capacity](#index-units "#index-units")
- [Integrations](#integrations "#integrations")
- [ISV integration](#isv-integration "#isv-integration")
- [Large language model](#llm "#llm")
- [Principal Mapping](#principal-mapping "#principal-mapping")
- [Plugins](#plugins "#plugins")
- [Quick prompts](#quick-prompt "#quick-prompt")
- [Response personalization](#response-personalization "#response-personalization")
- [Retriever](#retriever "#retriever")
- [Retrieval Augmented Generation](#retrieval-augmented-generation "#retrieval-augmented-generation")
- [Relevance tuning](#boosting "#boosting")
- [Subscription tiers](#subscription-tiers "#subscription-tiers")
- [Tags](#tags "#tags")
- [Visual content extraction](#visual-content-extraction "#visual-content-extraction")
- [User store](#user-store "#user-store")
- [Web experience](#web-exp "#web-exp")

## Agentic RAG

Agentic RAG (Retrieval Augmented Generation) is an advanced natural language
processing technique that enhances Amazon Q Business's standard RAG capabilities.
Using Agentic RAG, Amazon Q Business employs multiple intelligent agents and
specialized tools to process queries and retrieve and generate responses from your
enterprise data using its underlying large language model, while continuously monitoring
quality.

With Agentic RAG system processes queries through a combination of the following
coordinated steps:

- Analyzes both the user's question and conversation history and determines
  which retrieval tools to use
- Intelligently triggers multiple retrieval operations as needed
- Synthesizes information from various sources, and generate responses using its
  underlying large language model

For more information, see [Agentic Retrieval Augmented Generation (RAG)](agentic-rag.md "agentic-rag.md").

## Application environment

An Amazon Q Business application environment is the primary resource that you use to
create a chat solution. To create the application environment, you can use either the Amazon Q Business console or [Amazon Q Business API](../api-reference/Welcome.md "../api-reference/Welcome.md") actions. Amazon Q Business offers four distinct methods for creating applications: the standard
approach with [IAM Identity Center](create- application.md "create- application.md") integration, an [IAM federation](create-application-iam.md "create-application-iam.md") option for AWS-centric environments, an [anonymous
application method](create-anonymous-application.md "create-anonymous-application.md") for public-facing scenarios, and a specialized [Quick Suite integration](create-application- quicksight.md "create-application- quicksight.md") for
analytics-focused implementations. Each creation pathway provides different
authentication mechanisms and integration capabilities, allowing organizations to select
the most appropriate solution based on their security requirements and existing
infrastructure.

## ACLs (Access Control Lists)

ACLs control user and system actions for resources. Users can read, write, execute, or
modify data based on ACL permissions.

## Amazon Q Apps

Amazon Q Business allows web experience users to create lightweight,
purpose-built Q Apps to fulfill specific tasks from within their web experience. For
example, you can use Amazon Q Business to create an app with a web experience that
exclusively generates marketing-related content to improve your marketing team's
productivity. Your marketing team members can, in turn, also create their own
Amazon Q Apps with its own marketing content-generation capabilities—like writing
customer emails and creating promotional content using a certain style of voice, tone,
and branding. For more information, see [Amazon Q Apps](purpose-built-qapps.md "purpose-built-qapps.md").

## Analytics dashboard

The Amazon Q Business analytics dashboard provides comprehensive insights into
how users interact with your application. It offers metrics and visualizations on
conversation volumes, popular topics, user engagement patterns, and system performance.
Administrators can use these analytics to identify trends, understand user needs,
measure adoption rates, and make data-driven decisions to improve the application. The
dashboard helps track the effectiveness of your Amazon Q Business implementation,
identify areas for enhancement, and demonstrate the value it brings to your
organization. For more information, see [Using the analytics dashboard](analytics-dashboard.md "analytics-dashboard.md").

## Audio and video extraction

Amazon Q Business extracts semantic information from audio and video files,
making multimedia content queryable. This allows users to query audio and video content
using natural language and explore deeper with follow-up questions, enhancing
information retrieval from multimedia sources. For more information, see [Extracting semantic meaning from audio and video
content](extracting-meaning-from-images.md#Audio-video-extraction "extracting-meaning-from-images.md#Audio-video-extraction").

## Browser extensions

The Amazon Q Business browser extension enhances users' web browsing experience
by bringing AI-powered assistance directly into their daily workflows. Available for
Google Chrome, Microsoft Edge, and Mozilla Firefox browsers, the extension allows users
to summarize web pages, ask questions about content, access company knowledge, and use
other features available in the Amazon Q Business web experience. This integration
requires installation and
authentication. For more information, see [Enhancing web browsing with Amazon Q Business](browser-extensions.md "browser-extensions.md").

## Chat orchestration

Chat orchestration is a Amazon Q Business feature that automatically manages
chat requests across configured plugins and data sources. When enabled, Amazon Q Business automatically routes chat requests to plugins, integrating
enterprise data and relevant actions within a single chat response. This feature
provides unified response integration combining RAG workflow with plugin actions,
intelligent action detection for read-only vs. write actions, and smart plugin
management with user-driven experience through clarification requests when needed. For
more information, see [Chat orchestration settings](guardrails-global-controls.md#guardrails-global-orchestration "guardrails-global-controls.md#guardrails-global-orchestration").

## Custom document enrichment

Document enrichment is an Amazon Q Business feature that you can use to
manipulate your document content and document attributes. You can use document
enrichment to perform optical character recognition (OCR) or translation. Document
enrichment uses basic and Lambda operations. For more information see,
[Document attributes and types](doc-attributes.md#doc-attributes "doc-attributes.md#doc-attributes") and [Document enrichment](custom-document-enrichment.md "custom-document-enrichment.md").

## Data accessors

The Amazon Q Business data accessors feature allows you to securely share your
enterprise data with verified independent software vendors (ISVs) using Amazon Q. This feature enables ISVs to retrieve relevant content from your
Amazon Q index, enhancing their applications with your organization's
knowledge. By granting controlled access to your data, you can leverage third-party
tools while maintaining security and data access compliance. Data accessors include
verified software providers such as Asana, Miro, Zoom, PagerDuty, and Planview. For more
information, see [Share your enterprise data with data accessors](data-accessors.md "data-accessors.md").

## Data source

A data source is a document repository.

## Data source connector

A data source connector can crawl and synchronize a data source with an Amazon Q Business index at customizable intervals. Amazon Q Business supports
multiple connectors so that you can build your generative AI solution with minimal
configuring. For a list of Amazon Q Business supported connectors, see [Supported connectors](connectors-list.md "connectors-list.md"). For an overview of Amazon Q Business connector
features, see [Amazon Q Business data source connector features](connectors-list.md#connector-key-concepts "connectors-list.md#connector-key-concepts").

## Document

In Amazon Q Business, a document is a unit of data. Specific document formats
supported include .csv, .docx, HTML, JSON,
.pdf, plaintext, .ppt, .pptx,
.rtf, and .xslx. For more information, see [Supported
document types](doc-types.md "doc-types.md").

## Document attributes

Document attributes are structural metadata associated with documents, such as
document title, document type, and date and time created. Amazon Q Business
extracts document attributes during the document ingestion process to provide
customizable chat and data manipulation capabilities for your application environment. Amazon Q Business offers reserved document attributes that you can use. Or, you can
create custom attributes. For more information, see [Document attributes](doc-attributes.md#doc-attributes "doc-attributes.md#doc-attributes"), [Filtering using document attributes](metadata-filtering.md "metadata-filtering.md"), [Boosting using document attributes](metadata-boosting.md "metadata-boosting.md"), and [Custom document enrichment](custom-document-enrichment.md "custom-document-enrichment.md").

## Field mappings

An Amazon Q Business index has fields that help you structure data to aid the
retrieval process. You can map index fields to your [document attributes](doc-attributes.md#doc-attributes "doc-attributes.md#doc-attributes") when you add documents directly to
an index, or use a data source connector.

## Filtering using document attributes

Filtering using document attributes is an Amazon Q Business feature that you can
use to filter your Amazon Q Business chat responses for your end user. For
example, if you have a document attribute associated with a data source type, you can
use the attribute to mandate that chat responses only be generated from a specific data
source. For more information, see [Filtering using document attributes](metadata-filtering.md "metadata-filtering.md").

## Foundation model

A foundation model (FM) is a broad, function-based machine learning model (not
specific to language systems). An FM is tuned to a large number (billions) of parameters
and is trained on a large corpus of documents.

## Guardrails

An Amazon Q Business feature that lets you define global controls and
topic-level controls for your application environment. Using this feature, you can control what
sources your application environment will use to generate responses from, and also control what
topics it will respond to and how. For more information, see [Guardrails](guardrails.md "guardrails.md").

## Hallucination

A hallucination, in the machine learning context, is a confident response by an AI
application environment that isn't justified by its training data. Think of a hallucination as
instances where the response doesn't make sense in the context of the prompt, or when
the responses are out of scope with the documents provided. Amazon Q Business
offers you the ability to minimize hallucinations by allowing your retrieval system to
[generate responses only from your existing enterprise data](guardrails.md "guardrails.md").

## Hallucination mitigation

Hallucination mitigation is a Amazon Q Business feature that checks chat
responses for hallucinations and corrects inconsistencies in real-time during chat. If a
hallucination is detected with high confidence, Amazon Q Business corrects the
inconsistencies in its response and generates a new, edited message. This feature is
only available for retrieval augmented generation (RAG) responses from data connected to
the application and is not supported for chat orchestration, plugin workflows, or
responses generated from tabular data or multimedia transcripts. For more information,
see [Response settings](guardrails-global-controls.md#guardrails-global-response "guardrails-global-controls.md#guardrails-global-response").

## IAM Identity Center

You can manage user access to your Amazon Q Business application environment using IAM Identity Center
as your AWS gateway to the identity provider of your choice. For more information on
creating an Amazon Q Business application environment integrated with IAM Identity Center see [Configuring an
IAM Identity Center instance](idc-setup.md "idc-setup.md") and [Configuring an Amazon Q Business application](create-application.md "create-application.md"). For more information
about using IAM Identity Center to manage access to applications, see [Manage access to
applications](../../../singlesignon/latest/userguide/manage-your-applications.md "../../../singlesignon/latest/userguide/manage-your-applications.md") in the IAM Identity Center User Guide.

## Identity Federation through IAM

Amazon Q Business supports identity federation through AWS Identity and Access Management. When you use
identity federation, you can manage users with your enterprise identity provider (IdP)
and use AWS Identity and Access Management to authenticate users when they sign in to AWS Identity and Access Management. For more
information on creating an Amazon Q Business application environment integrated with
AWS Identity and Access Management see [Configuring an Amazon Q Business
application](create-application-iam.md "create-application-iam.md").

## Identity provider

An identity provider (IdP) is a service that stores, manages, maintains, and verifies
user identities for your application environment (in this case, Amazon Q Business). Some
examples of IdPs are IAM Identity Center, Okta, and Microsoft EntraID
(formerly Azure Active Directory).

## Index

An index is a corpus of documents. Amazon Q Business supports its own index
where you can add and sync documents. An index has fields that you can map your document
attributes to, to enhance your end user's chat experience. Amazon Q Business
creates retriever for you when it creates your Amazon Q Business index. Amazon Q Business provides two types of index: Enterprise and Starter.

You can also use an Amazon Kendra index as a retriever for your generative AI
application environment.

## Index capacity

When you use an Amazon Q Business native index for your application environment, you must
provision data storage capacity for it. Amazon Q Business provides two types of
index: Enterprise and Starter. Both index types include 20,000 documents or 200 MB of
total extracted text (whichever is reached first) and 100 hours of data connector usage
(time that it takes to scan and index new, updated, or deleted documents) by default.
For more information, see [Amazon Q Business Index types](tiers.md#index-tiers "tiers.md#index-tiers") and [Pricing for subscriptions and indices](tiers.md#pricing-subs-index "tiers.md#pricing-subs-index").

## Integrations

Amazon Q Business integrations enhance user productivity by bringing AI-powered
assistance directly into daily workflows through third-party enterprise tools. These
integrations include browser extensions for Google Chrome, Microsoft Edge, and Mozilla
Firefox browsers, as well as applications for Slack, Microsoft Teams, Microsoft Outlook,
and Microsoft Word. Each integration must be configured and deployed to bring Amazon Q Business capabilities directly within those enterprise tools, allowing users
to access Amazon Q's knowledge without context switching during their work.
For more information, see [Integrations](integrations.md "integrations.md").

## ISV integration

Amazon Q Business enables independent software vendors (ISVs) to leverage
customer enterprise data through the Amazon Q index to enhance their
applications with generative AI capabilities. ISVs can access this data through two
methods: either by being added as a data accessor to an existing customer's Amazon Q index, or by creating a Amazon Q application on behalf of the
customer. The `SearchRelevantContent` API operation allows ISVs to retrieve
relevant content from the customer's data sources while maintaining security and access
controls, ensuring users only see content they have permission to access. This
integration enables software providers to build enhanced application experiences without
having to directly connect to or index individual data sources. For more information,
see [Amazon Q index for independent software vendors (ISVs)](isv.md "isv.md").

## Large language model

A large language model (LLM) is a language-based, machine learning model that's tuned
to a large number (billions) of parameters and trained on a large corpus of
documents.

## Principal Mapping

Principal mapping is used to connect users and groups with their user ids and group
membership information in data sources connected to the application.

## Plugins

Amazon Q Business includes a plugins feature that you can use to interact with
third-party services such as Jira and Salesforce. With the
plugins feature, you can perform actions specific to that service (like creating a
ticket) from within your Amazon Q Business web experience chat. For more
information, see [Plugins](plugins.md "plugins.md").

## Quick prompts

The Amazon Q Business quick prompts feature helps with end user discoverability
of the web experience chat features. Use this feature to prompt your end user to engage
with their web experience chat in specific ways. For example, you can show the available
[configured plugins](querying-structured-data.md "querying-structured-data.md") or inform users that they can
choose to summarize their chat.

## Response personalization

Response personalization is a Amazon Q Business feature that customizes chat
responses to end users based on metadata associated with them—specifically address and
job-related information—in your SSO instance. This feature enhances the relevance of
responses by tailoring them to the user's specific context within the organization. To
use response personalization effectively, you must have already added the necessary user
information in your SSO instance. For more information, see [Response settings](guardrails-global-controls.md#guardrails-global-response "guardrails-global-controls.md#guardrails-global-response").

## Retriever

A retriever pulls data from an index in real time during a conversation. Amazon Q Business supports a native index retriever and also a Amazon Kendra
index retriever.

## Retrieval Augmented Generation

Retrieval Augmented Generation (RAG) is a natural language processing (NLP) technique.
Using RAG, generative artificial intelligence (generative AI) is conditioned on specific
documents that are retrieved from a dataset. Amazon Q Business has a built-in RAG
system. A RAG model has the following two components:

- A _retrieval_ component retrieves relevant
  documents for the user query.
- A _generation_ component takes the query and
  the retrieved documents and then generates an answer to the query using a large
  language model.

## Relevance tuning

You can choose to use document attributes to boost and tune the relevance of chat
responses for end users from specific content. For example, if you have a document
attribute associated document creation or updating date, you use these attributes to
boost chat responses from more recently created or updated documents. For more
information, see [Relevance tuning](../business-use-dg/metadata-boosting.md "../business-use-dg/metadata-boosting.md").

## Subscription tiers

Amazon Q Business offers multiple user subscription tiers and index types that
can be combined to meet your organization's needs. User subscription tiers determine the
features available to end users, with both Lite and Pro tier users having access to
browser extensions. Index types include starter index and enterprise index, each
with different capabilities and storage capacities. You can choose any combination of
index types and user subscriptions for your Amazon Q Business application. For
more information, see [Amazon Q Business subscription tiers and index
types](tiers.md "tiers.md").

###### Important

Amazon Q Business Pro tier subscriptions in Europe (Ireland)
(eu-west-1) and Asia Pacific (Sydney) (ap-southeast-2) regions are available with a limited set of features.

## Tags

Manage your Amazon Q Business applications and data sources by assigning tags or
labels. You can use tags to categorize your Amazon Q Business resources in various
ways. For example, categorize by purpose, owner, or application environment, or any combination.
Each tag consists of a key and a value, both of which you define. For more information,
see [Tags](tagging.md "tagging.md").

## Visual content extraction

When Amazon Q Business processes your input files from a data source, it uses
advanced image understanding capabilities to extract semantic information and insights
from images and other visuals. This feature makes visual information in your data
sources queryable, allowing end users to find relevant information even when it's
conveyed in embedded diagrams, charts, or technical illustrations. Visual content
extraction provides additional context and nuance to the information in your data
sources and builds a more complete knowledge base from your enterprise data. For more
information, see [Extracting semantic meaning from embedded visual
content](extracting-meaning-from-images.md "extracting-meaning-from-images.md").

## User store

User Store is an Amazon Q Business data source connector feature that
streamlines user and group management across all the data sources attached to your
application environment. For more information about how this feature works and implementation
details, see [Understanding User Store](connector-principal-store.md "connector-principal-store.md").

## Web experience

An Amazon Q Business web experience is the chat interface that you create using
your Amazon Q Business application environment. Then, your end users can chat with your
organization’s Amazon Q Business web experience. You can configure and customize
your Amazon Q Business web experience using either the Amazon Q Business
console or the Amazon Q Business API. For more information, see [Customizing your web experience](customize-web-experience.md "customize-web-experience.md").
