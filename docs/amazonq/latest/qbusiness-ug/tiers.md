# Amazon Q Business subscription tiers and index types

Amazon Q Business offers multiple index types and user subscription tiers. You can
choose any combination of index types and user subscriptions for your Amazon Q Business application environment.

###### Topics

- [Index types](#index-tiers "#index-tiers")
- [User subscription tiers](#user-sub-tiers "#user-sub-tiers")
- [Understanding user subscriptions](#managing-sub-tiers "#managing-sub-tiers")
- [Pricing](#pricing-subs-index "#pricing-subs-index")

## Index types

Amazon Q Business offers two types of indexes: starter index and enterprise index. Each index type has different capacity limits measured in index units, which determine the amount of data storage and processing capacity available for your index. For detailed information about index units and capacity, see [Index capacity](concepts-terminology.md#index-units "concepts-terminology.md#index-units").

The following table outlines the features of both index types.

| Starter index                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Enterprise index                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ideal use case**<br>• Proof-of-concept or developer workloads<br>**Features**<br>• Runs in 1 Availability Zone (AZ) – See [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") (data centers in AWS<br>regions)<br>• Includes up to 20,000 document capacity or 200 MB of total<br>extracted text (whichever is reached first)\*<br>• Includes up to 100 hours of data source connector usage<br>(time that it takes to scan and index new, updated, or<br>deleted documents) | **Ideal use case**<br>• Production workloads<br>**Features**<br>• Runs in 3 Availability Zone (AZ) – See [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/") (data centers in AWS<br>regions)<br>• Includes up to 20,000 document capacity or 200 MB of total<br>extracted text (whichever is reached first)\*<br>• Includes up to 100 hours of data source connector usage<br>(time that it takes to scan and index new, updated, or<br>deleted documents)<br>• Includes customer managed key encryption support |

\*For reference, 5 pages of text that contain approximately 500 words on each page is
equivalent to 10 KB of total extracted text.

For detailed pricing information, including examples of charges for index capacity,
subscribing and unsubscribing users to Amazon Q Business tiers, upgrading and
downgrading Amazon Q Business tiers, and more, see [Amazon Q Business Pricing](https://aws.amazon.com/q/business/pricing "https://aws.amazon.com/q/business/pricing").

## User subscription tiers

Amazon Q Business offers two subscription tiers: the Amazon Q Business Lite Plan and
the Amazon Q Business Pro Plan. The following table outlines the features of
Amazon Q Business Pro and Amazon Q Business Lite.

###### Important

Amazon Q Business Pro tier subscriptions in Europe (Ireland)
(eu-west-1) and Asia Pacific (Sydney) (ap-southeast-2) regions are available with a limited set of features.

###### Important

As of July 1, 2024, Amazon Q Apps only available to Amazon Q Business Pro users. Users with Lite
subscriptions should upgrade to Amazon Q Business Pro.

###### Topics

- [Amazon Q Business Lite users must upgrade to Amazon Q Business Pro to continue using Q Apps](#lite-user-changes "#lite-user-changes")

| Amazon Q Business Lite Plan                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Amazon Q Business Pro Plan                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Ideal use case**<br>• Optimized for enterprise-wide deployment to all employees<br>(frontline and knowledge workers)<br>• Allows end users to ask questions and receive<br>permissions-aware responses from enterprise data sources<br>with citations<br>• Helps employees quickly get answers for use cases such as<br>IT, HR, benefits help desks, and other Q&A chatbot use<br>cases at a low cost<br>**Features**<br>• **Q&A on knowledge<br>bases:\*<br>• Users can ask questions and get<br>answers from enterprise knowledge bases with<br>citations.<br>• **Upload file to chat:**<br>Users can upload documents into a chat session and interact<br>with its contents.<br>• **Permissions-aware<br>responses:_<br>• Users only get answers from<br>content that they have access to.<br>• \*\*Using web experience with<br>single-sign on:_<br>• Users get access to a web<br>experience user interface with support for single sign-on<br>(IAM Identity Center).<br>• **Browser extensions:** Users can access Amazon Q Business through browser extensions for Google Chrome, Mozilla Firefox, and Microsoft Edge.<br>\*_Note:_<br>• Built-in and custom plugins are not available with the Lite Plan. Users must upgrade to the Pro Plan to access plugin functionality. | **Ideal use case**<br>• Best suited for knowledge workers and improves<br>productivity across a wide range of tasks<br>• Provides the full suite of Amazon Q Business<br>capabilities<br>• Includes access to [Amazon Q Apps](purpose-built-qapps.md "purpose-built-qapps.md") \* for creating<br>and sharing task automation applications<br>• Includes access to [integrations](integrations.md "integrations.md") within<br>third-party applications including Slack, Microsoft Teams,<br>and browser extensions for Google Chrome, Mozilla Firefox,<br>and Microsoft Edge<br>• Includes access to [custom plugins](custom-plugin.md "custom-plugin.md") for actions<br>like submitting time off requests and sending meeting<br>invites through Amazon Q Business<br>• Includes Amazon Q integration in Quick Pro for understanding<br>data through executive summaries, context-aware Q&A, and<br>interactive data stories<br>**Features**<br>• **Q&A on LLM knowledge:**<br>Users can ask questions and get answers from the general<br>knowledge that the LLM has.<br>• **Q&A on knowledge<br>bases:\*<br>• Users can ask questions and get<br>answers from enterprise knowledge bases with<br>citations.<br>• **Permissions-aware<br>responses:_<br>• Users only get answers from<br>content that they have access to.<br>• \*\*Using web experience with<br>single-sign on:_<br>• Users get access to a web<br>experience user interface with support for single sign-on<br>(SSO).<br>• **Content generation:** Users<br>can send queries directly to the foundation model to<br>generate content.<br>• **Upload file to chat:**<br>Users can upload documents into a chat session and interact<br>with its contents.<br>• **Amazon Q Apps:** Users can<br>build and share their own purpose-built applications to<br>automate tasks and improve productivity.<br>• **Custom plugins:** Enable<br>users to execute actions in third-party applications.<br>• **Built-in plugins:** Access<br>to pre-built integrations with third-party applications such as<br>Salesforce, Jira, ServiceNow, and others.<br>• **Amazon Q Business in<br>Quicksight (Reader Pro):\*<br>• Users can ask<br>questions to explore data in natural language, view and<br>interact with dashboards, and create compelling stories from<br>insights.<br>• **Chat orchestration:**<br>automatically manage chat requests across configured plugins<br>and data sources in your Amazon Q Business<br>application.<br>• **Integrations with third-party<br>applications:\*<br>• Users can access Amazon Q Business within third-party applications such as<br>Slack and Microsoft Teams,<br>and web browsers through browser extensions for<br>Google Chrome, Mozilla<br>Firefox, and Microsoft Edge. |

For detailed pricing information, including examples of charges for index capacity,
subscribing and unsubscribing users to Amazon Q Business tiers, upgrading and
downgrading Amazon Q Business tiers, and more, see [Amazon Q Business Pricing](https://aws.amazon.com/q/business/pricing "https://aws.amazon.com/q/business/pricing").

### Amazon Q Business Lite users must upgrade to Amazon Q Business Pro to continue using Q Apps

As of July 1, 2024, Amazon Q Apps are available only to
[Amazon Q Business Pro users](tiers.md#managing-sub-tiers "tiers.md#managing-sub-tiers"). Amazon Q Business Lite users will no longer be able to
create, run, or view Q Apps. To access, Q Apps, Lite users must upgrade to Amazon Q Business Pro.

As of August 30, 2024, all Amazon Q Apps created by Lite
users who did not upgrade their account to Amazon Q Business Pro have been deleted.

## Understanding user subscriptions

User subscriptions are created per Amazon Q Business application or Quick account. Each admin can manage subscriptions for users for their specific
Amazon Q Business application or Quick account.

For applications using IAM Identity Center, AWS will deduplicate subscriptions across all Amazon Q Business applications and Quick accounts, and charge each user only once for
their highest subscription level. Note that deduplication will apply only if the Amazon Q Business applications and Quick accounts share the same IAM Identity Center instance.

Users subscribed to Amazon Q Business applications using Identity Federation
through IAM (IAM Federation), will be charged once per OIDC or SAML IAM Identity
Provider. For example, if a user is subscribed to five different Amazon Q Business
applications all associated with the same IAM Identity Provider, that user will be
charged once. However, if the Amazon Q Business applications are associated with
five IAM Identity Providers, the user will be charged five times.

In scenarios where a user is subscribed to a mix of applications, the charging
structure is as follows:

- For applications using IAM Identity Center, users will be charged once across all these
  applications that share the same IAM Identity Center instance.
- For applications using IAM Federation, users will be charged once per IAM
  Identity Provider.

User subscriptions are prorated when created or upgraded based on the number of days
left in the calendar month. Any cancellations or downgrades are not prorated and apply
starting in the next calendar month. The charges for user subscription starts only after
first use by the user. After a user's first use, subscription charges will continue each
month until the user's subscriptions have been removed.

For a consolidated view of all your user subscriptions see the [Amazon Q subscriptions page](https://console.aws.amazon.com/amazonq/subscriptions "https://console.aws.amazon.com/amazonq/subscriptions").
Subscriptions can only be viewed centrally and _not_ be created or
updated from the Amazon Q subscription management console.

## Pricing

You are charged for user subscriptions to application environments and for index capacity. You
can choose any combination of the following subscription tiers and indices for your
application environment.

For detailed pricing information, including examples of charges for index capacity,
subscribing and unsubscribing users to Amazon Q Business tiers, upgrading and
downgrading Amazon Q Business tiers, and more, see [Amazon Q Business Pricing](https://aws.amazon.com/q/business/pricing "https://aws.amazon.com/q/business/pricing").
