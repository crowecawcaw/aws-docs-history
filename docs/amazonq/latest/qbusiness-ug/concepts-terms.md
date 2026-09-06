

Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/qbusiness-availability-change.html).

# Key concepts of Amazon Q Business
<a name="concepts-terms"></a>

This section describes the key concepts and terms related to Amazon Q Business.

**Topics**
+ [Agentic RAG](#agentic-retrieval-augmented-generation)
+ [Application environment](#web-app)
+ [ACLs (Access Control Lists)](#acls)
+ [Amazon Q Apps](#q-apps)
+ [Analytics dashboard](#analytics-dashboard)
+ [Audio and video extraction](#audio-video-extraction)
+ [Browser extensions](#browser-extensions)
+ [Chat orchestration](#chat-orchestration)
+ [Custom document enrichment](#cde)
+ [Data accessors](#data-accessors)
+ [Data source](#data-source)
+ [Data source connector](#connector)
+ [Document](#document)
+ [Document attributes](#doc-attribute)
+ [Field mappings](#mappings)
+ [Filtering using document attributes](#filtering)
+ [Foundation model](#fm)
+ [Guardrails](#guardrails)
+ [Hallucination](#hallucination)
+ [Hallucination mitigation](#hallucination-mitigation)
+ [IAM Identity Center](#sso)
+ [Identity Federation through IAM](#iam)
+ [Identity provider](#idp)
+ [Index](#index)
+ [Index capacity](#index-units)
+ [Integrations](#integrations)
+ [ISV integration](#isv-integration)
+ [Large language model](#llm)
+ [Principal Mapping](#principal-mapping)
+ [Plugins](#plugins)
+ [Quick prompts](#quick-prompt)
+ [Response personalization](#response-personalization)
+ [Retriever](#retriever)
+ [Retrieval Augmented Generation](#retrieval-augmented-generation)
+ [Relevance tuning](#boosting)
+ [Subscription tiers](#subscription-tiers)
+ [Tags](#tags)
+ [Visual content extraction](#visual-content-extraction)
+ [User store](#user-store)
+ [Web experience](#web-exp)

## Agentic RAG
<a name="agentic-retrieval-augmented-generation"></a>

Agentic RAG (Retrieval Augmented Generation) is an advanced natural language processing technique that enhances Amazon Q Business's standard RAG capabilities. Using Agentic RAG, Amazon Q Business employs multiple intelligent agents and specialized tools to process queries and retrieve and generate responses from your enterprise data using its underlying large language model, while continuously monitoring quality.

With Agentic RAG system processes queries through a combination of the following coordinated steps:
+ Analyzes both the user's question and conversation history and determines which retrieval tools to use
+ Intelligently triggers multiple retrieval operations as needed
+ Synthesizes information from various sources, and generate responses using its underlying large language model

For more information, see [Agentic Retrieval Augmented Generation (RAG)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/agentic-rag.html). 

## Application environment
<a name="web-app"></a>

An Amazon Q Business application environment is the primary resource that you use to create a chat solution. To create the application environment, you can use either the Amazon Q Business console or [Amazon Q Business API](https://docs.aws.amazon.com/amazonq/latest/api-reference/Welcome.html) actions. Amazon Q Business offers four distinct methods for creating applications: the standard approach with [IAM Identity Center](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-                 application.html) integration, an [IAM federation](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html) option for AWS-centric environments, an [ anonymous application method](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-anonymous-application.html) for public-facing scenarios, and a specialized [Quick integration](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-                         quicksight.html) for analytics-focused implementations. Each creation pathway provides different authentication mechanisms and integration capabilities, allowing organizations to select the most appropriate solution based on their security requirements and existing infrastructure.

## ACLs (Access Control Lists)
<a name="acls"></a>

ACLs control user and system actions for resources. Users can read, write, execute, or modify data based on ACL permissions.

## Amazon Q Apps
<a name="q-apps"></a>

Amazon Q Business allows web experience users to create lightweight, purpose-built Q Apps to fulfill specific tasks from within their web experience. For example, you can use Amazon Q Business to create an app with a web experience that exclusively generates marketing-related content to improve your marketing team's productivity. Your marketing team members can, in turn, also create their own Amazon Q Apps with its own marketing content-generation capabilities—like writing customer emails and creating promotional content using a certain style of voice, tone, and branding. For more information, see [Amazon Q Apps](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/purpose-built-qapps.html).

## Analytics dashboard
<a name="analytics-dashboard"></a>

The Amazon Q Business analytics dashboard provides comprehensive insights into how users interact with your application. It offers metrics and visualizations on conversation volumes, popular topics, user engagement patterns, and system performance. Administrators can use these analytics to identify trends, understand user needs, measure adoption rates, and make data-driven decisions to improve the application. The dashboard helps track the effectiveness of your Amazon Q Business implementation, identify areas for enhancement, and demonstrate the value it brings to your organization. For more information, see [Using the analytics dashboard](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/analytics-dashboard.html).

## Audio and video extraction
<a name="audio-video-extraction"></a>

Amazon Q Business extracts semantic information from audio and video files, making multimedia content queryable. This allows users to query audio and video content using natural language and explore deeper with follow-up questions, enhancing information retrieval from multimedia sources. For more information, see [Extracting semantic meaning from audio and video content](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html#Audio-video-extraction).

## Browser extensions
<a name="browser-extensions"></a>

The Amazon Q Business browser extension enhances users' web browsing experience by bringing AI-powered assistance directly into their daily workflows. Available for Google Chrome, Microsoft Edge, and Mozilla Firefox browsers, the extension allows users to summarize web pages, ask questions about content, access company knowledge, and use other features available in the Amazon Q Business web experience. This integration requires installation and authentication. For more information, see [Enhancing web browsing with Amazon Q Business](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/browser-extensions.html).

## Chat orchestration
<a name="chat-orchestration"></a>

Chat orchestration is a Amazon Q Business feature that automatically manages chat requests across configured plugins and data sources. When enabled, Amazon Q Business automatically routes chat requests to plugins, integrating enterprise data and relevant actions within a single chat response. This feature provides unified response integration combining RAG workflow with plugin actions, intelligent action detection for read-only vs. write actions, and smart plugin management with user-driven experience through clarification requests when needed. For more information, see [Chat orchestration settings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-global-controls.html#guardrails-global-orchestration).

## Custom document enrichment
<a name="cde"></a>

Document enrichment is an Amazon Q Business feature that you can use to manipulate your document content and document attributes. You can use document enrichment to perform optical character recognition (OCR) or translation. Document enrichment uses basic and Lambda operations. For more information see, [Document attributes and types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html#doc-attributes) and [Document enrichment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-document-enrichment.html).

## Data accessors
<a name="data-accessors"></a>

The Amazon Q Business data accessors feature allows you to securely share your enterprise data with verified independent software vendors (ISVs) using Amazon Q. This feature enables ISVs to retrieve relevant content from your Amazon Q index, enhancing their applications with your organization's knowledge. By granting controlled access to your data, you can leverage third-party tools while maintaining security and data access compliance. Data accessors include verified software providers such as Asana, Miro, Zoom, PagerDuty, and Planview. For more information, see [Share your enterprise data with data accessors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/data-accessors.html).

## Data source
<a name="data-source"></a>

A data source is a document repository.

## Data source connector
<a name="connector"></a>

A data source connector can crawl and synchronize a data source with an Amazon Q Business index at customizable intervals. Amazon Q Business supports multiple connectors so that you can build your generative AI solution with minimal configuring. For a list of Amazon Q Business supported connectors, see [Supported connectors](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connectors-list.html). For an overview of Amazon Q Business connector features, see [Amazon Q Business data source connector features](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connectors-list.html#connector-key-concepts).

## Document
<a name="document"></a>

In Amazon Q Business, a document is a unit of data. Specific document formats supported include .csv, .docx, HTML, JSON, .pdf, plaintext, .ppt, .pptx, .rtf, and .xslx. For more information, see [Supported document types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-types.html).

## Document attributes
<a name="doc-attribute"></a>

Document attributes are structural metadata associated with documents, such as document title, document type, and date and time created. Amazon Q Business extracts document attributes during the document ingestion process to provide customizable chat and data manipulation capabilities for your application environment. Amazon Q Business offers reserved document attributes that you can use. Or, you can create custom attributes. For more information, see [Document attributes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html#doc-attributes), [Filtering using document attributes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/metadata-filtering.html), [Boosting using document attributes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/metadata-boosting.html), and [Custom document enrichment](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/custom-document-enrichment.html).

## Field mappings
<a name="mappings"></a>

An Amazon Q Business index has fields that help you structure data to aid the retrieval process. You can map index fields to your [document attributes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/doc-attributes.html#doc-attributes) when you add documents directly to an index, or use a data source connector.

## Filtering using document attributes
<a name="filtering"></a>

Filtering using document attributes is an Amazon Q Business feature that you can use to filter your Amazon Q Business chat responses for your end user. For example, if you have a document attribute associated with a data source type, you can use the attribute to mandate that chat responses only be generated from a specific data source. For more information, see [Filtering using document attributes](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/metadata-filtering.html).

## Foundation model
<a name="fm"></a>

A foundation model (FM) is a broad, function-based machine learning model (not specific to language systems). An FM is tuned to a large number (billions) of parameters and is trained on a large corpus of documents.

## Guardrails
<a name="guardrails"></a>

An Amazon Q Business feature that lets you define global controls and topic-level controls for your application environment. Using this feature, you can control what sources your application environment will use to generate responses from, and also control what topics it will respond to and how. For more information, see [Guardrails](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html).

## Hallucination
<a name="hallucination"></a>

A hallucination, in the machine learning context, is a confident response by an AI application environment that isn't justified by its training data. Think of a hallucination as instances where the response doesn't make sense in the context of the prompt, or when the responses are out of scope with the documents provided. Amazon Q Business offers you the ability to minimize hallucinations by allowing your retrieval system to [generate responses only from your existing enterprise data](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html).

## Hallucination mitigation
<a name="hallucination-mitigation"></a>

Hallucination mitigation is a Amazon Q Business feature that checks chat responses for hallucinations and corrects inconsistencies in real-time during chat. If a hallucination is detected with high confidence, Amazon Q Business corrects the inconsistencies in its response and generates a new, edited message. This feature is only available for retrieval augmented generation (RAG) responses from data connected to the application and is not supported for chat orchestration, plugin workflows, or responses generated from tabular data or multimedia transcripts. For more information, see [Response settings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-global-controls.html#guardrails-global-response).

## IAM Identity Center
<a name="sso"></a>

You can manage user access to your Amazon Q Business application environment using IAM Identity Center as your AWS gateway to the identity provider of your choice. For more information on creating an Amazon Q Business application environment integrated with IAM Identity Center see [Configuring an IAM Identity Center instance](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/idc-setup.html) and [Configuring an Amazon Q Business application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application.html). For more information about using IAM Identity Center to manage access to applications, see [Manage access to applications](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-applications.html) in the IAM Identity Center User Guide.

## Identity Federation through IAM
<a name="iam"></a>

Amazon Q Business supports identity federation through AWS Identity and Access Management. When you use identity federation, you can manage users with your enterprise identity provider (IdP) and use AWS Identity and Access Management to authenticate users when they sign in to AWS Identity and Access Management. For more information on creating an Amazon Q Business application environment integrated with AWS Identity and Access Management see [Configuring an Amazon Q Business application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-application-iam.html).

## Identity provider
<a name="idp"></a>

An identity provider (IdP) is a service that stores, manages, maintains, and verifies user identities for your application environment (in this case, Amazon Q Business). Some examples of IdPs are IAM Identity Center, Okta, and Microsoft EntraID (formerly Azure Active Directory). 

## Index
<a name="index"></a>

An index is a corpus of documents. Amazon Q Business supports its own index where you can add and sync documents. An index has fields that you can map your document attributes to, to enhance your end user's chat experience. Amazon Q Business creates retriever for you when it creates your Amazon Q Business index. Amazon Q Business provides two types of index: Enterprise and Starter.

You can also use an Amazon Kendra index as a retriever for your generative AI application environment.

## Index capacity
<a name="index-units"></a>

When you use an Amazon Q Business native index for your application environment, you must provision data storage capacity for it. Amazon Q Business provides two types of index: Enterprise and Starter. Both index types include 20,000 documents or 200 MB of total extracted text (whichever is reached first) and 100 hours of data connector usage (time that it takes to scan and index new, updated, or deleted documents) by default. For more information, see [Amazon Q Business Index types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#index-tiers) and [Pricing for subscriptions and indices](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#pricing-subs-index).

## Integrations
<a name="integrations"></a>

Amazon Q Business integrations enhance user productivity by bringing AI-powered assistance directly into daily workflows through third-party enterprise tools. These integrations include browser extensions for Google Chrome, Microsoft Edge, and Mozilla Firefox browsers, as well as applications for Slack, Microsoft Teams, Microsoft Outlook, and Microsoft Word. Each integration must be configured and deployed to bring Amazon Q Business capabilities directly within those enterprise tools, allowing users to access Amazon Q's knowledge without context switching during their work. For more information, see [Integrations](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/integrations.html).

## ISV integration
<a name="isv-integration"></a>

Amazon Q Business enables independent software vendors (ISVs) to leverage customer enterprise data through the Amazon Q index to enhance their applications with generative AI capabilities. ISVs can access this data through two methods: either by being added as a data accessor to an existing customer's Amazon Q index, or by creating a Amazon Q application on behalf of the customer. The `SearchRelevantContent` API operation allows ISVs to retrieve relevant content from the customer's data sources while maintaining security and access controls, ensuring users only see content they have permission to access. This integration enables software providers to build enhanced application experiences without having to directly connect to or index individual data sources. For more information, see [Amazon Q index for independent software vendors (ISVs)](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/isv.html).

## Large language model
<a name="llm"></a>

A large language model (LLM) is a language-based, machine learning model that's tuned to a large number (billions) of parameters and trained on a large corpus of documents.

## Principal Mapping
<a name="principal-mapping"></a>

Principal mapping is used to connect users and groups with their user ids and group membership information in data sources connected to the application.

## Plugins
<a name="plugins"></a>

Amazon Q Business includes a plugins feature that you can use to interact with third-party services such as Jira and Salesforce. With the plugins feature, you can perform actions specific to that service (like creating a ticket) from within your Amazon Q Business web experience chat. For more information, see [Plugins](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins.html).

## Quick prompts
<a name="quick-prompt"></a>

The Amazon Q Business quick prompts feature helps with end user discoverability of the web experience chat features. Use this feature to prompt your end user to engage with their web experience chat in specific ways. For example, you can show the available [configured plugins ](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/querying-structured-data.html) or inform users that they can choose to summarize their chat.

## Response personalization
<a name="response-personalization"></a>

Response personalization is a Amazon Q Business feature that customizes chat responses to end users based on metadata associated with them—specifically address and job-related information—in your SSO instance. This feature enhances the relevance of responses by tailoring them to the user's specific context within the organization. To use response personalization effectively, you must have already added the necessary user information in your SSO instance. For more information, see [Response settings](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails-global-controls.html#guardrails-global-response).

## Retriever
<a name="retriever"></a>

A retriever pulls data from an index in real time during a conversation. Amazon Q Business supports a native index retriever and also a Amazon Kendra index retriever.

## Retrieval Augmented Generation
<a name="retrieval-augmented-generation"></a>

Retrieval Augmented Generation (RAG) is a natural language processing (NLP) technique. Using RAG, generative artificial intelligence (generative AI) is conditioned on specific documents that are retrieved from a dataset. Amazon Q Business has a built-in RAG system. A RAG model has the following two components: 
+ A *retrieval* component retrieves relevant documents for the user query.
+ A *generation* component takes the query and the retrieved documents and then generates an answer to the query using a large language model.

## Relevance tuning
<a name="boosting"></a>

You can choose to use document attributes to boost and tune the relevance of chat responses for end users from specific content. For example, if you have a document attribute associated document creation or updating date, you use these attributes to boost chat responses from more recently created or updated documents. For more information, see [Relevance tuning](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/metadata-boosting.html).

## Subscription tiers
<a name="subscription-tiers"></a>

Amazon Q Business offers multiple user subscription tiers and index types that can be combined to meet your organization's needs. User subscription tiers determine the features available to end users, with both Lite and Pro tier users having access to browser extensions. Index types include starter index and enterprise index, each with different capabilities and storage capacities. You can choose any combination of index types and user subscriptions for your Amazon Q Business application. For more information, see [Amazon Q Business subscription tiers and index types](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html).

**Important**  
Amazon Q Business Pro tier subscriptions in Europe (Ireland) (eu-west-1) and Asia Pacific (Sydney) (ap-southeast-2) regions are available with a limited set of features.

## Tags
<a name="tags"></a>

Manage your Amazon Q Business applications and data sources by assigning tags or labels. You can use tags to categorize your Amazon Q Business resources in various ways. For example, categorize by purpose, owner, or application environment, or any combination. Each tag consists of a key and a value, both of which you define. For more information, see [Tags](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tagging.html).

## Visual content extraction
<a name="visual-content-extraction"></a>

When Amazon Q Business processes your input files from a data source, it uses advanced image understanding capabilities to extract semantic information and insights from images and other visuals. This feature makes visual information in your data sources queryable, allowing end users to find relevant information even when it's conveyed in embedded diagrams, charts, or technical illustrations. Visual content extraction provides additional context and nuance to the information in your data sources and builds a more complete knowledge base from your enterprise data. For more information, see [Extracting semantic meaning from embedded visual content](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html).

## User store
<a name="user-store"></a>

User Store is an Amazon Q Business data source connector feature that streamlines user and group management across all the data sources attached to your application environment. For more information about how this feature works and implementation details, see [Understanding User Store](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/connector-principal-store.html).

## Web experience
<a name="web-exp"></a>

An Amazon Q Business web experience is the chat interface that you create using your Amazon Q Business application environment. Then, your end users can chat with your organization’s Amazon Q Business web experience. You can configure and customize your Amazon Q Business web experience using either the Amazon Q Business console or the Amazon Q Business API. For more information, see [Customizing your web experience](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/customize-web-experience.html).