# Kustomer connector for Amazon AppFlow

Kustomer is a Customer Relationship Management (CRM) service that helps companies
create and maintain operational solutions with customers. If you’re a Kustomer user,
your account contains customer data across a number of digital channels. You can use Amazon AppFlow to
transfer data from Kustomer to certain AWS services or other supported
applications.

## Amazon AppFlow support for Kustomer

Amazon AppFlow supports Kustomer as follows.

**Supported as a data source?**
Yes. You can use Amazon AppFlow to transfer data from Kustomer.

**Supported as a data destination?**
No. You can't use Amazon AppFlow to transfer data to Kustomer.

## Before you begin

To use Amazon AppFlow to transfer data from Kustomer to supported destinations, you must meet these
requirements:

- You have an account with Kustomer that contains the data that you want to transfer. For more
  information about the Kustomer data objects that Amazon AppFlow supports, see [Supported objects](#kustomer-objects "#kustomer-objects").
- In the API keys settings for your account, you've created an API key for Amazon AppFlow, and you
  have the token value. Amazon AppFlow uses the API key token to make authenticated calls to your account
  and securely access your data. For the steps to create a key, see [API keys](https://help.kustomer.com/api-keys-SJs5YTIWX "https://help.kustomer.com/api-keys-SJs5YTIWX") in the Kustomer
  Help Center.

To connect Amazon AppFlow to your Kustomer account, you provide the token of your API key.
You can view and copy this token only when you create the API key. If you don't have the token
value, create a new API key.

## Connecting Amazon AppFlow to your Kustomer account

To connect Amazon AppFlow to your Kustomer account,
provide details from your Kustomer project so that Amazon AppFlow can access your data. If you
haven't yet configured your Kustomer project for Amazon AppFlow integration, see [Before you begin](#kustomer-prereqs "#kustomer-prereqs").

###### To connect to Kustomer

1. Sign in to the AWS Management Console and open the Amazon AppFlow console at [https://console.aws.amazon.com/appflow/](https://console.aws.amazon.com/appflow/ "https://console.aws.amazon.com/appflow/").
2. In the navigation pane on the left, choose **Connections**.
3. On the **Manage connections** page, for **Connectors**,
   choose **Kustomer**.
4. Choose **Create connection**.
5. In the **Connect to Kustomer**
   window, enter the following information:
   - **Access token** – The access token
     that you created earlier.
   - **Instance URL** – The URL of the
     instance where you want to run the operation, for example,
     https://domain.api.kustomerapp.com.

6. Optionally, under **Data encryption**, choose **Customize
   encryption settings (advanced)** if you want to encrypt your data with a customer
   managed key in the AWS Key Management Service (AWS KMS).

By default, Amazon AppFlow encrypts your data with a KMS key that AWS creates, uses, and manages
for you. Choose this option if you want to encrypt your data with your own KMS key instead.

Amazon AppFlow always encrypts your data during transit and at rest. For more information, see
[Data protection in Amazon AppFlow](data-protection.md "data-protection.md").

If you want to use a KMS key from the current AWS account, select this key under
**Choose an AWS KMS key**. If you want to use a KMS key from a different
AWS account, enter the Amazon Resource Name (ARN) for that key. 7. For **Connection name**, enter a name for your connection. 8. Choose **Connect**. 9. In the window that appears, sign in to your Kustomer account, and grant access
to Amazon AppFlow.

On the **Manage connections** page, your new connection appears in the
**Connections** table. When you create a flow
that uses Kustomer as the data source, you can select this connection.

## Transferring data from Kustomer with a flow

To transfer data from Kustomer, create an Amazon AppFlow flow, and choose Kustomer as the data
source. For the steps to create a flow, see [Creating flows in Amazon AppFlow](create-flow.md "create-flow.md").

When you configure the flow, choose the data object that you want to transfer. For the objects
that Amazon AppFlow supports for Kustomer, see [Supported objects](#kustomer-objects "#kustomer-objects").

Also, choose the destination where you want to transfer the data object that you selected.
For more information about how to configure your destination, see [Supported destinations](#kustomer-destinations "#kustomer-destinations").

## Supported destinations

When you create a flow that uses Kustomer as the data source, you can set the destination to any of the following connectors:

- [Amazon Lookout for Metrics](lookout.md "lookout.md")
- [Amazon Redshift](redshift.md "redshift.md")
- [Amazon RDS for PostgreSQL](connectors-amazon-rds-postgres-sql.md "connectors-amazon-rds-postgres-sql.md")
- [Amazon S3](s3.md "s3.md")
- [HubSpot](connectors-hubspot.md "connectors-hubspot.md")
- [Marketo](marketo.md "marketo.md")
- [Salesforce](salesforce.md "salesforce.md")
- [SAP OData](sapodata.md "sapodata.md")
- [Snowflake](snowflake.md "snowflake.md")
- [Upsolver](upsolver.md "upsolver.md")
- [Zendesk](zendesk.md "zendesk.md")
- [Zoho CRM](connectors-zoho-crm.md "connectors-zoho-crm.md")

## Supported objects

When you create a flow that uses Kustomer as the data source, you can transfer any of the
following data objects to supported destinations:

| **Object**                            | **Field**         | **Data type** | **Supported filters** |
| ------------------------------------- | ----------------- | ------------- | --------------------- |
| Apps                                  | ID                | String        |                       |
| actions                               | Struct            |               |
| autoUpdate                            | Boolean           |               |
| cards                                 | Struct            |               |
| commands                              | Struct            |               |
| createdAt                             | DateTime          |               |
| current                               | String            |               |
| dataSubscriptions                     | List              |               |
| disabled                              | Boolean           |               |
| events                                | Struct            |               |
| hooks                                 | Struct            |               |
| inboundHookUris                       | List              |               |
| klasses                               | Struct            |               |
| kviews                                | Struct            |               |
| meta                                  | Struct            |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| outboundWebhooks                      | Struct            |               |
| roles                                 | List              |               |
| settings                              | Struct            |               |
| settingsPageConfig                    | String            |               |
| shortcuts                             | Struct            |               |
| status                                | String            |               |
| statusAt                              | DateTime          |               |
| templates                             | Struct            |               |
| triggers                              | Struct            |               |
| updatedAt                             | DateTime          |               |
| version                               | String            |               |
| widgets                               | List              |               |
| workflows                             | Struct            |               |
| Audit Logs                            | ID                | String        |                       |
| changes                               | Struct            |               |
| client                                | String            |               |
| createdAt                             | DateTime          | BETWEEN       |
| eventName                             | String            |               |
| eventVerb                             | String            |               |
| expiresAt                             | DateTime          |               |
| ip                                    | String            |               |
| objectId                              | String            |               |
| objectType                            | String            |               |
| org                                   | String            |               |
| publishedAt                           | DateTime          |               |
| userId                                | String            |               |
| userType                              | String            |               |
| Auth Customer Settings                | ID                | String        |                       |
| corsWhitelist                         | List              |               |
| createdAt                             | DateTime          |               |
| secret                                | String            |               |
| updatedAt                             | DateTime          |               |
| Auth Roles                            | ID                | String        |                       |
| Auth Tokens                           | CreatedAt         | DateTime      |                       |
| ID                                    | String            |               |
| UpdatedAt                             | DateTime          |               |
| cidr                                  | List              |               |
| expireAt                              | DateTime          |               |
| ipAddress                             | String            |               |
| lastAccessedAt                        | DateTime          |               |
| lastTokenChars                        | String            |               |
| name                                  | String            |               |
| roles                                 | List              |               |
| Brands                                | CreatedAt         | DateTime      |                       |
| ID                                    | String            |               |
| UpdatedAt                             | DateTime          |               |
| default                               | Boolean           |               |
| iconUrl                               | String            |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| Cards                                 | CreatedAt         | DateTime      |                       |
| ID                                    | String            |               |
| UpdatedAt                             | DateTime          |               |
| contexts                              | List              |               |
| description                           | String            |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| url                                   | String            |               |
| Categories                            | CreatedAt         | DateTime      |                       |
| ID                                    | String            |               |
| UpdatedAt                             | DateTime          |               |
| categoryPositions                     | List              |               |
| hash                                  | String            |               |
| langs                                 | Struct            |               |
| modifiedAt                            | DateTime          |               |
| positions                             | List              |               |
| published                             | Boolean           |               |
| root                                  | Boolean           |               |
| Chat Settings                         | autoreply         | String        |                       |
| closableChat                          | Boolean           |               |
| colors                                | Struct            |               |
| default                               | Boolean           |               |
| disableAttachments                    | Boolean           |               |
| embedIconColor                        | String            |               |
| embedIconUrl                          | String            |               |
| enabled                               | Boolean           |               |
| fallbackEmailIntroduction             | String            |               |
| fallbackEmailSubject                  | String            |               |
| greeting                              | String            |               |
| id                                    | String            |               |
| modifiedAt                            | DateTime          |               |
| noHistory                             | Boolean           |               |
| offhoursImageUrl                      | String            |               |
| offhoursMessage                       | String            |               |
| outboundChatEnabled                   | Boolean           |               |
| pushSettings                          | Struct            |               |
| settingsVersion                       | Integer           |               |
| showBrandingIdentifier                | Boolean           |               |
| showEmailInputBanner                  | Boolean           |               |
| showTypingIndicatorCustomerWeb        | Boolean           |               |
| showTypingIndicatorWeb                | Boolean           |               |
| singleSessionChat                     | Boolean           |               |
| suppressConversationReopen            | Boolean           |               |
| teamName                              | String            |               |
| updatedAt                             | DateTime          |               |
| version                               | Integer           |               |
| volumeControl                         | Struct            |               |
| widgetType                            | String            |               |
| Companies                             | CreatedAt         | DateTime      |                       |
| Domains                               | List              |               |
| Emails                                | List              |               |
| Id                                    | String            |               |
| Locations                             | List              |               |
| ModifiedAt                            | DateTime          |               |
| Name                                  | String            |               |
| Phones                                | List              |               |
| Rev                                   | Integer           |               |
| RoleGroupVersions                     | List              |               |
| Socials                               | List              |               |
| Tags                                  | List              |               |
| UpdatedAt                             | DateTime          |               |
| Urls                                  | List              |               |
| Whatsapps                             | List              |               |
| Conversation                          | accessOverride    | List          |                       |
| assignedTeams                         | List              |               |
| assignedUsers                         | List              |               |
| assistant                             | Struct            |               |
| channels                              | List              |               |
| createdAt                             | DateTime          |               |
| direction                             | String            |               |
| ended                                 | Boolean           |               |
| endedAt                               | DateTime          |               |
| endedByType                           | String            |               |
| endedReason                           | String            |               |
| firstDone                             | Struct            |               |
| firstMessageIn                        | Struct            |               |
| firstMessageOut                       | Struct            |               |
| firstResponse                         | Struct            |               |
| firstResponseSinceLastDone            | Struct            |               |
| id                                    | String            |               |
| importedAt                            | String            |               |
| inboundMessageCount                   | Integer           |               |
| lastActivityAt                        | DateTime          |               |
| lastDone                              | Struct            |               |
| lastMessageAt                         | DateTime          |               |
| lastMessageDirection                  | String            |               |
| lastMessageIn                         | Struct            |               |
| lastMessageOut                        | Struct            |               |
| lastMessageUnrespondedTo              | Struct            |               |
| lastMessageUnrespondedToSinceLastDone | Struct            |               |
| lastResponse                          | Struct            |               |
| matchedTimeBasedRules                 | List              |               |
| messageCount                          | Integer           |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| noteCount                             | Integer           |               |
| outboundMessageCount                  | Integer           |               |
| phase                                 | String            |               |
| predictions                           | List              |               |
| preview                               | String            |               |
| priority                              | Integer           |               |
| rev                                   | Integer           |               |
| roleGroupVersions                     | List              |               |
| satisfaction                          | Integer           |               |
| satisfactionLevel                     | Struct            |               |
| sentiment                             | String            |               |
| skills                                | List              |               |
| spam                                  | Boolean           |               |
| status                                | String            |               |
| suggestedShortcuts                    | List              |               |
| suggestedTags                         | List              |               |
| tags                                  | List              |               |
| updatedAt                             | DateTime          |               |
| Customers                             | Display Color     | String        |                       |
| Display Icon                          | String            |               |
| Display Name                          | String            |               |
| ExternalId                            | String            |               |
| ExternalIds                           | List              |               |
| Locale                                | String            |               |
| Name                                  | String            |               |
| accessOverride                        | List              |               |
| activeUsers                           | List              |               |
| companyName                           | String            |               |
| conversationCounts                    | Struct            |               |
| createdAt                             | DateTime          |               |
| defaultLang                           | String            |               |
| deleted                               | Boolean           |               |
| emails                                | List              |               |
| facebookIds                           | List              |               |
| firstName                             | String            |               |
| gender                                | String            |               |
| id                                    | String            |               |
| instagramIds                          | List              |               |
| lastActivityAt                        | DateTime          |               |
| lastConversation                      | Struct            |               |
| lastName                              | String            |               |
| locations                             | List              |               |
| modifiedAt                            | DateTime          |               |
| phones                                | List              |               |
| preview                               | Struct            |               |
| progressiveStatus                     | String            |               |
| recentItems                           | List              |               |
| recentLocation                        | Struct            |               |
| rev                                   | Integer           |               |
| roleGroupVersions                     | List              |               |
| satisfactionLevel                     | Struct            |               |
| sharedEmails                          | List              |               |
| sharedExternalIds                     | List              |               |
| sharedPhones                          | List              |               |
| sharedSocials                         | List              |               |
| socials                               | List              |               |
| tags                                  | List              |               |
| timeZone                              | String            |               |
| updatedAt                             | DateTime          |               |
| urls                                  | List              |               |
| verified                              | Boolean           |               |
| watchers                              | List              |               |
| whatsapps                             | List              |               |
| Customers Searches                    | accessTeams       | List          |                       |
| accessUsers                           | List              |               |
| badgeColor                            | String            |               |
| cacheable                             | Boolean           |               |
| createdAt                             | DateTime          |               |
| data                                  | Struct            |               |
| dataHash                              | String            |               |
| defaultVisibility                     | String            |               |
| icon                                  | String            |               |
| id                                    | String            |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| position                              | Integer           |               |
| private                               | Boolean           |               |
| showBadge                             | Boolean           |               |
| teamVisibilities                      | List              |               |
| updatedAt                             | DateTime          |               |
| userVisibilities                      | List              |               |
| Customers Searches Pinned             | ID                | String        |                       |
| createdAt                             | DateTime          |               |
| search                                | String            |               |
| Customers Searches Positions          | children          | List          |                       |
| createdAt                             | DateTime          |               |
| id                                    | String            |               |
| modifiedAt                            | DateTime          |               |
| positions                             | List              |               |
| rev                                   | Integer           |               |
| updatedAt                             | DateTime          |               |
| Hooks Email                           | createdAt         | DateTime      |                       |
| debug                                 | Boolean           |               |
| description                           | String            |               |
| email                                 | String            |               |
| eventName                             | String            |               |
| hash                                  | String            |               |
| id                                    | String            |               |
| key                                   | String            |               |
| modifiedAt                            | DateTime          |               |
| title                                 | String            |               |
| updatedAt                             | DateTime          |               |
| Hooks Web                             | createdAt         | DateTime      |                       |
| debug                                 | Boolean           |               |
| description                           | String            |               |
| eventName                             | String            |               |
| hash                                  | String            |               |
| id                                    | String            |               |
| modifiedAt                            | DateTime          |               |
| title                                 | String            |               |
| updatedAt                             | DateTime          |               |
| url                                   | String            |               |
| version                               | Integer           |               |
| KB Articles                           | ID                | String        |                       |
| categories                            | List              |               |
| createdAt                             | DateTime          |               |
| deleted                               | Boolean           |               |
| deletedAt                             | DateTime          |               |
| hash                                  | String            |               |
| knowledgeBases                        | List              |               |
| langVersions                          | Struct            |               |
| latestLangs                           | Struct            |               |
| metaDescription                       | String            |               |
| metaKeywords                          | List              |               |
| metaTitle                             | String            |               |
| modifiedAt                            | DateTime          |               |
| publishedAt                           | DateTime          |               |
| scope                                 | String            |               |
| source                                | String            |               |
| status                                | String            |               |
| tags                                  | List              |               |
| title                                 | String            |               |
| updatedAt                             | DateTime          |               |
| KB Forms                              | advanced          | Boolean       |                       |
| body                                  | String            |               |
| channel                               | String            |               |
| componentsV2                          | Struct            |               |
| conditions                            | Struct            |               |
| createdAt                             | DateTime          |               |
| deflection                            | Boolean           |               |
| formHookEnabled                       | Boolean           |               |
| hash                                  | String            |               |
| id                                    | String            |               |
| klass                                 | String            |               |
| layout                                | List              |               |
| layoutV2                              | List              |               |
| modifiedAt                            | String            |               |
| name                                  | String            |               |
| published                             | Boolean           |               |
| publishedAt                           | DateTime          |               |
| recaptcha                             | Boolean           |               |
| replyFrom                             | String            |               |
| slug                                  | String            |               |
| snippets                              | List              |               |
| updatedAt                             | DateTime          |               |
| wcag                                  | Boolean           |               |
| KB Routes                             | ID                | String        |                       |
| createdAt                             | DateTime          |               |
| modifiedAt                            | DateTime          |               |
| routableId                            | String            |               |
| routableType                          | String            |               |
| updatedAt                             | DateTime          |               |
| url                                   | String            |               |
| KB Tags                               | ID                | String        |                       |
| createdAt                             | DateTime          |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| updatedAt                             | DateTime          |               |
| KB Templates                          | ID                | String        |                       |
| beta                                  | Boolean           |               |
| createdAt                             | DateTime          |               |
| description                           | String            |               |
| images                                | List              |               |
| jsxSnippets                           | List              |               |
| manifest                              | Struct            |               |
| title                                 | String            |               |
| updatedAt                             | DateTime          |               |
| version                               | String            |               |
| KB Themes                             | ID                | String        |                       |
| active                                | Boolean           |               |
| configSnippets                        | List              |               |
| createdAt                             | DateTime          |               |
| custom                                | Boolean           |               |
| default                               | Boolean           |               |
| jsxSnippets                           | List              |               |
| lastFileUpdatedAt                     | DateTime          |               |
| manifest                              | Struct            |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| rev                                   | Integer           |               |
| status                                | String            |               |
| templateTitle                         | String            |               |
| templateVersion                       | String            |               |
| templateVersionId                     | String            |               |
| updatedAt                             | DateTime          |               |
| Kviews                                | advanced          | Boolean       |                       |
| appDisabled                           | Boolean           |               |
| components                            | Struct            |               |
| conditions                            | Struct            |               |
| context                               | String            |               |
| createdAt                             | DateTime          |               |
| enabled                               | Boolean           |               |
| id                                    | String            |               |
| layout                                | List              |               |
| meta                                  | Struct            |               |
| modifiedAt                            | DateTime          |               |
| resource                              | String            |               |
| rev                                   | Integer           |               |
| template                              | String            |               |
| updatedAt                             | DateTime          |               |
| Messages                              | app               | String        |                       |
| assignedTeams                         | List              |               |
| assignedUsers                         | List              |               |
| auto                                  | Boolean           |               |
| channel                               | String            |               |
| createdAt                             | DateTime          |               |
| createdByTeams                        | List              |               |
| direction                             | String            |               |
| directionType                         | String            |               |
| errorAt                               | DateTime          |               |
| externalId                            | String            |               |
| id                                    | String            |               |
| intentDetections                      | List              |               |
| meta                                  | Struct            |               |
| modifiedAt                            | DateTime          |               |
| preview                               | String            |               |
| reactions                             | List              |               |
| redacted                              | Boolean           |               |
| rev                                   | Integer           |               |
| sentAt                                | DateTime          |               |
| size                                  | Integer           |               |
| status                                | String            |               |
| subject                               | String            |               |
| updatedAt                             | DateTime          |               |
| Notes                                 | body              | String        | CONTAINS              |
| createdAt                             | DateTime          |               |
| createdByTeams                        | List              |               |
| id                                    | String            |               |
| modifiedAt                            | DateTime          |               |
| updatedAt                             | DateTime          |               |
| Notifications                         | createdAt         | DateTime      |                       |
| event                                 | Struct            |               |
| id                                    | String            |               |
| name                                  | String            |               |
| status                                | String            |               |
| updatedAt                             | DateTime          |               |
| Outbound Accounts                     | account           | String        |                       |
| aliasUsername                         | Boolean           |               |
| app                                   | String            |               |
| channel                               | String            |               |
| name                                  | String            |               |
| Outbound Webhooks                     | appDisabled       | Boolean       |                       |
| consecutiveErrorsCount                | Integer           |               |
| createdAt                             | DateTime          |               |
| enabled                               | Boolean           |               |
| events                                | List              |               |
| headers                               | List              |               |
| id                                    | String            |               |
| isError                               | Boolean           |               |
| name                                  | String            |               |
| token                                 | String            |               |
| updatedAt                             | DateTime          |               |
| url                                   | String            |               |
| Outbound Webhooks Events              | events            | List          |                       |
| Outbound Webhooks Transactions        | ID                | String        |                       |
| eventName                             | String            |               |
| nextRetry                             | String            |               |
| sentAt                                | Long              |               |
| status                                | String            |               |
| webhookId                             | String            |               |
| Routing Queue Rules                   | ID                | String        |                       |
| createdAt                             | String            |               |
| criteria                              | Struct            |               |
| description                           | String            |               |
| enabled                               | Boolean           |               |
| modifiedAt                            | String            |               |
| name                                  | String            |               |
| updatedAt                             | String            |               |
| Routing Queues                        | ID                | String        |                       |
| createdAt                             | DateTime          |               |
| deleted                               | Boolean           |               |
| description                           | String            |               |
| displayName                           | String            |               |
| itemSize                              | Integer           |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| priority                              | Integer           |               |
| restrictTransfersByUsers              | Boolean           |               |
| settings                              | Struct            |               |
| system                                | Boolean           |               |
| updatedAt                             | DateTime          |               |
| Routing Settings                      | capacity          | Struct        |                       |
| createdAt                             | DateTime          |               |
| enabled                               | Boolean           |               |
| externalQueues                        | List              |               |
| id                                    | String            |               |
| modifiedAt                            | DateTime          |               |
| updatedAt                             | DateTime          |               |
| workItemCapacity                      | Integer           |               |
| Routing Statuses                      | ID                | String        |                       |
| createdAt                             | DateTime          |               |
| description                           | String            |               |
| enabled                               | Boolean           |               |
| name                                  | String            |               |
| routable                              | Boolean           |               |
| selectable                            | Boolean           |               |
| statusType                            | String            |               |
| system                                | Boolean           |               |
| updatedAt                             | DateTime          |               |
| Routing Work Items                    | channel           | String        |                       |
| completedAt                           | DateTime          |               |
| createdAt                             | DateTime          |               |
| firstEnterQueueAt                     | DateTime          |               |
| handle                                | Struct            |               |
| hasSkills                             | Boolean           |               |
| id                                    | String            |               |
| itemSize                              | Integer           |               |
| ivr                                   | Struct            |               |
| lastRevision                          | Struct            |               |
| modifiedAt                            | DateTime          |               |
| paused                                | Boolean           |               |
| priority                              | Integer           |               |
| queuedCount                           | Integer           |               |
| resource                              | Struct            |               |
| resourceCreatedAt                     | DateTime          |               |
| resourceDirection                     | String            |               |
| resourceFirstQueueTime                | Integer           |               |
| resourceRev                           | Integer           |               |
| resourceType                          | String            |               |
| rev                                   | Integer           |               |
| skills                                | List              |               |
| status                                | String            |               |
| updatedAt                             | DateTime          |               |
| workItemNumber                        | Integer           |               |
| Routing Work Sessions                 | capacity          | List          |                       |
| capacityRemaining                     | Integer           |               |
| capacityStatus                        | String            |               |
| createdAt                             | DateTime          |               |
| handledConversationCount              | Integer           |               |
| handledItemCount                      | Integer           |               |
| hasPendingItem                        | Boolean           |               |
| hasSkills                             | Boolean           |               |
| id                                    | String            |               |
| idleSince                             | DateTime          |               |
| lastRevision                          | Struct            |               |
| modifiedAt                            | DateTime          |               |
| pausedWorkItemCount                   | Integer           |               |
| rev                                   | Integer           |               |
| routable                              | Boolean           |               |
| signedInAt                            | DateTime          |               |
| signedOutAt                           | DateTime          |               |
| skills                                | List              |               |
| statusType                            | String            |               |
| totalAvailable                        | Struct            |               |
| totalAvailableAtCapacity              | Struct            |               |
| totalAvailableIdleCapacity            | String            |               |
| totalCapacity                         | Integer           |               |
| totalTimeByStatus                     | Struct            |               |
| totalUnavailable                      | Struct            |               |
| totalUnavailableAtCapacity            | Struct            |               |
| updatedAt                             | DateTime          |               |
| workItemCount                         | Integer           |               |
| Satisfaction                          | ID                | String        |                       |
| allQuestions                          | List              |               |
| channel                               | String            |               |
| createdAt                             | DateTime          |               |
| criteria                              | Struct            |               |
| delayTime                             | Double            |               |
| description                           | String            |               |
| enabled                               | Boolean           |               |
| followUpType                          | String            |               |
| formType                              | String            |               |
| from                                  | Struct            |               |
| introduction                          | String            |               |
| metaDescription                       | String            |               |
| metaTitle                             | String            |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| negativeQuestions                     | List              |               |
| positiveQuestions                     | List              |               |
| questions                             | List              |               |
| ratingPrompt                          | String            |               |
| scale                                 | Struct            |               |
| updatedAt                             | DateTime          |               |
| Schedules                             | CreatedAt         | DateTime      |                       |
| ID                                    | String            |               |
| UpdatedAt                             | DateTime          |               |
| default                               | Boolean           |               |
| hours                                 | Struct            |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| timezone                              | String            |               |
| Settings                              | ID                | String        |                       |
| app                                   | String            |               |
| category                              | String            |               |
| createdAt                             | DateTime          |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| type                                  | String            |               |
| value                                 | String            |               |
| Shortcuts                             | appDisabled       | Boolean       |                       |
| conversation                          | Struct            |               |
| createdAt                             | DateTime          |               |
| deleted                               | Boolean           |               |
| draft                                 | Struct            |               |
| id                                    | String            |               |
| isPrivate                             | Boolean           |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| payload                               | Struct            |               |
| rev                                   | Integer           |               |
| updatedAt                             | DateTime          |               |
| Shortcuts Categories                  | categoryPositions | List          |                       |
| createdAt                             | DateTime          |               |
| id                                    | String            |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| root                                  | Boolean           |               |
| shortcutPositions                     | List              |               |
| updatedAt                             | DateTime          |               |
| Snippets                              | app               | String        |                       |
| createdAt                             | DateTime          |               |
| description                           | String            |               |
| id                                    | String            |               |
| key                                   | String            |               |
| langs                                 | Struct            |               |
| name                                  | String            |               |
| source                                | String            |               |
| Snoozes                               | createdAt         | DateTime      |                       |
| enabled                               | Boolean           |               |
| id                                    | String            |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| type                                  | String            |               |
| updatedAt                             | DateTime          |               |
| value                                 | String            |               |
| Spam Senders                          | channel           | String        |                       |
| createdAt                             | DateTime          |               |
| id                                    | String            |               |
| list                                  | String            |               |
| modifiedAt                            | DateTime          |               |
| sender                                | String            |               |
| updatedAt                             | DateTime          |               |
| Teams                                 | createdAt         | DateTime      |                       |
| deleted                               | Boolean           |               |
| displayName                           | String            |               |
| icon                                  | String            |               |
| id                                    | String            |               |
| members                               | List              |               |
| modifiedAt                            | DateTime          |               |
| name                                  | String            |               |
| roleGroups                            | List              |               |
| updatedAt                             | DateTime          |               |
| Users                                 | CreatedAt         | DateTime      |                       |
| DisplayName                           | String            |               |
| Email                                 | String            |               |
| EmailVerifiedAt                       | DateTime          |               |
| FirstEmailVerifiedAt                  | DateTime          |               |
| Id                                    | String            |               |
| ModifiedAt                            | DateTime          |               |
| Name                                  | String            |               |
| Password                              | Struct            |               |
| RoleGroups                            | List              |               |
| Roles                                 | List              |               |
| UpdatedAt                             | DateTime          |               |
| UserType                              | String            |               |
| firstLoginAt                          | DateTime          |               |
| isEmailValid                          | Boolean           |               |
| klasses                               | appDisabled       | Boolean       |                       |
| color                                 | String            |               |
| createdAt                             | DateTime          |               |
| icon                                  | String            |               |
| id                                    | String            |               |
| name                                  | String            |               |
| s3DataUrl                             | String            |               |
| status                                | String            |               |
| updatedAt                             | DateTime          |               |
