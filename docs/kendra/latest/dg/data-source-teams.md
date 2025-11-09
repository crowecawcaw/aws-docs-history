# Microsoft Teams

Microsoft Teams is an enterprise collaboration tool for messaging, meetings and file
sharing. If you are a Microsoft Teams user, you can use Amazon Kendra to index your
Microsoft Teams data source.

You can connect Amazon Kendra to your Microsoft Teams data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") and the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md")
API.

For troubleshooting your Amazon Kendra Microsoft Teams data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-teams "#supported-features-teams")
- [Prerequisites](#prerequisites-teams "#prerequisites-teams")
- [Connection instructions](#data-source-procedure-teams "#data-source-procedure-teams")
- [Learn more](#teams-learn-more "#teams-learn-more")
- [Notes](#teams-notes "#teams-notes")

## Supported features

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Microsoft Teams data source,
make these changes in your Microsoft Teams and AWS accounts.

**In Microsoft Teams, make sure you have:**

- Created a Microsoft Teams account in Office 365.
- Noted your Microsoft 365 tenant ID. You can find your tenant ID in the
  Properties of your Azure Active Directory Portal or in your OAuth application.
- Configured an OAuth application in the Azure portal and noted the client ID and
  client secret or client credentials. See [Microsoft tutorial](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/walkthrough-register-app-azure-active-directory "https://learn.microsoft.com/en-us/power-apps/developer/data-platform/walkthrough-register-app-azure-active-directory") and [Registered app example](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application "https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application") for more information.

###### Note

When you create or register an app in the Azure portal, the secret ID represents
the actual secret value. You must take note or save the actual secret value
immediately when creating the secret and app. You can access your secret by selecting
the name of your application in the Azure portal and then navigating to the menu option
on certificates and secrets.

You can access your client ID by selecting the name of your
application in the Azure portal and then navigating to the overview page.
The Application (client) ID is the client ID.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- Added the necessary permissions. You can choose to add all permissions, or you
  can limit the scope by selecting fewer permissions based on which entities you'd
  like to crawl. The following table lists the application level permissions by
  corresponding entity:

| Entity             | Required Permissions for Data Sync                                                                                                           | Required Permissions for Identity Sync |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| Channel Post       | + ChannelMessage.Read.All<br>+ Group.Read.All<br>+ User.Read<br>+ User.Read.All                                                              | TeamMember.Read.All                    |
| Channel Attachment | + ChannelMessage.Read.All<br>+ Group.Read.All<br>+ User.Read<br>+ User.Read.All                                                              | TeamMember.Read.All                    |
| Channel Wiki       | + Group.Read.All<br>+ User.Read<br>+ User.Read.All                                                                                           | TeamMember.Read.All                    |
| Chat Message       | + Chat.Read.All<br>+ ChatMessage.Read.All<br>+ ChatMember.Read.All<br>+ User.Read<br>+ User.Read.All<br>+ Group.Read.All                     | TeamMember.Read.All                    |
| Meeting Chat       | + Chat.Read.All<br>+ ChatMessage.Read<br>+ ChatMember.Read.All<br>+ User.Read<br>+ User.Read.All<br>+ Group.Read.All                         | TeamMember.Read.All                    |
| Chat Attachment    | + Chat.Read.All<br>+ ChatMessage.Read<br>+ ChatMember.Read.All<br>+ User.Read<br>+ User.Read.All<br>+ Group.Read.All                         | TeamMember.Read.All                    |
| Meeting File       | + Chat.Read.All<br>+ ChatMessage.Read.All<br>+ ChatMember.Read.All<br>+ User.Read<br>+ User.Read.All<br>+ Group.Read.All<br>+ Files.Read.All | TeamMember.Read.All                    |
| Calendar Meeting   | + Chat.Read.All<br>+ ChatMessage.Read.All<br>+ ChatMember.Read.All<br>+ User.Read<br>+ User.Read.All<br>+ Group.Read.All<br>+ Files.Read.All | TeamMember.Read.All                    |
| Meeting Notes      | + User.Read<br>+ User.Read.All<br>+ Group.Read.All<br>+ Files.Read.All                                                                       | TeamMember.Read.All                    |

- Checked each document is unique in Microsoft Teams and across other
  data sources you plan to use for the same index. Each data source that you
  want to use for an index must not contain the same document across the data
  sources. Document IDs are global to an index and must be unique per index.

**In your AWS account, make sure you
have:**

- [Created
  an Amazon Kendra index](create-index.md "create-index.md") and, if using the API, noted the index
  ID.
- [Created an IAM role](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds") for your data source and, if
  using the API, noted the ARN of the IAM role.

###### Note

If you change your authentication type and credentials, you must
update your IAM role to access the correct AWS Secrets Manager secret ID.

- Stored your Microsoft Teams authentication credentials in an
  AWS Secrets Manager secret and, if using the API, noted the ARN of the
  secret.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

If you don’t have an existing IAM role or secret, you can use the
console to create a new IAM role and Secrets Manager secret when you
connect your Microsoft Teams data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Microsoft Teams data source, you must provide
the necessary details of your Microsoft Teams data source so that Amazon Kendra can access
your data. If you have not yet configured Microsoft Teams for Amazon Kendra,
see [Prerequisites](#prerequisites-teams "#prerequisites-teams").

Console
**To connect Amazon Kendra to
Microsoft Teams**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Microsoft Teams connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Microsoft Teams connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page,
   enter the following information:
   1. **Tenant ID**—Enter your
      Microsoft 365 tenant ID. You can find your tenant ID in
      the Properties of your Azure Active Directory
      Portal or in your OAuth application.
   2. **Authorization**—Turn on or off access control list (ACL) information for your
      documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
      and groups can access. The ACL information is used to filter search results based on the user or
      their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
   3. **AWS Secrets Manager secret**—Choose an existing secret or create a new
      Secrets Manager secret to store your Microsoft Teams authentication
      credentials. If you choose to create a new secret an AWS Secrets Manager
      secret window opens.
      1. Enter following information in the
         **Create an AWS
         Secrets Manager secret
         window**:
         1. **Secret name**—A
            name for your secret. The prefix
            ‘AmazonKendra-Microsoft Teams-’ is
            automatically added to your secret name.
         2. For **Client ID** and
            **Client secret**—Enter
            the authentication credentials configured in
            Microsoft Teams in the Azure portal.

      2. Save and add your secret.

   4. **Payment model**—You can
      choose a licensing and payment model for your
      Microsoft Teams account. Model A payment models are
      restricted to licensing and payment models that require
      security compliance. Model B payment models are suitable
      for licensing and payment models that do not require
      security compliance.
   5. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
      so, you must add **Subnets** and **VPC security groups**.
   6. **Identity crawler**—Specify whether to turn on
      Amazon Kendra’s identity crawler. The identity crawler uses the access control list
      (ACL) information for your documents to filter search results based on the user or their
      group access to documents. If you have an ACL for your documents and choose to use your ACL,
      you can then also choose to turn on Amazon Kendra’s identity crawler to configure
      [user
      context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources") of search results. Otherwise, if identity crawler is turned off,
      all documents can be publicly searched. If you want to use access control for your documents
      and identity crawler is turned off, you can alternatively use the
      [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md")
      API to upload user and group access information for user context filtering.
   7. **IAM role**—Choose an existing IAM
      role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 8. Choose **Next**.

7. On the **Configure sync settings** page,
   enter the following information:
   1. **Sync contents**—Select
      the types of content to crawl. You can
      choose to crawl chat, teams, and calendar content.
   2. **Additional configuration**—Specify
      certain calendar start and end dates, user emails, team names,
      and channel names, attachments, and OneNotes.
   3. **Sync mode**—Choose how you want to update
      your index when your data source content changes. When you sync your
      data source with Amazon Kendra for the first time, all content
      is crawled and indexed by default. You must run a full sync of your
      data if your initial sync failed, even if you don't choose full sync
      as your sync mode option.
      - Full sync: Freshly index all content, replacing existing
        content each time your data source syncs with your index.
      - New, modified sync: Index only new and modified content
        each time your data source syncs with your index. Amazon Kendra
        can use your data source's mechanism for tracking content
        changes and index content that changed since the last sync.
      - New, modified, deleted sync: Index only new, modified,
        and deleted content each time your data source syncs with
        your index. Amazon Kendra can use your data source's
        mechanism for tracking content changes and index content
        that changed since the last sync.

   4. In **Sync run schedule**, for
      **Frequency**—Choose how
      often to sync your data source content and update
      your index.
   5. Choose **Next**.

8. On the **Set field mappings** page, enter the
   following information:
   1. **Default data source
      fields**—Select from the Amazon Kendra generated default data source fields you
      want to map to your index.
   2. **Add field**—To add custom data
      source fields to create an index field name to map to
      and the field data type.
   3. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to
Microsoft Teams**

You must specify a JSON of the [data source schema](ds-schemas.md "ds-schemas.md")
using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API. You must provide the following
information:

- **Data
  source**—Specify the data source type as
  `MSTEAMS` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **Tenant ID**—You can find
  your tenant ID in the Properties of your Azure Active Directory
  Portal or in your OAuth application.
- **Sync mode**—Specify
  how Amazon Kendra should update your index when your data source
  content changes. When you sync your data source with Amazon Kendra
  for the first time, all content is crawled and indexed by default.
  You must run a full sync of your data if your initial sync failed,
  even if you don't choose full sync as your sync mode option. You can
  choose between:
  - `FORCED_FULL_CRAWL` to freshly index all content,
    replacing existing content each time your data source syncs with
    your index.
  - `FULL_CRAWL` to index only new, modified, and deleted
    content each time your data source syncs with your index. Amazon Kendra
    can use your data source’s mechanism for tracking content changes and
    index content that changed since the last sync.
  - `CHANGE_LOG` to index only new and modified
    content each time your data source syncs with your index. Amazon Kendra
    can use your data source’s mechanism for tracking content changes and
    index content that changed since the last sync.

- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your Microsoft Teams account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "clientId": "`client ID`",
    "clientSecret": "`client secret`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Microsoft Teams connector and Amazon Kendra.
  For more information, see [IAM roles for Microsoft Teams
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Document/content types**—Specify
  whether to crawl chat messages and attachments, channel posts and
  attachments, channel wikis, calendar content, meeting chats and
  files and notes.
- **Calendar content**—Specify a
  start and end date-time to crawl calendar content.
- **Inclusion and exclusion
  filters**—Specify whether to include or exclude
  certain content in Microsoft Teams. You can include or exclude
  team names, channel names, file names and file types, user email,
  OneNote sections, and OneNote pages.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Identity crawler**—Specify whether to turn on
  Amazon Kendra’s identity crawler. The identity crawler uses the access control list
  (ACL) information for your documents to filter search results based on the user or their
  group access to documents. If you have an ACL for your documents and choose to use your ACL,
  you can then also choose to turn on Amazon Kendra’s identity crawler to configure
  [user
  context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources") of search results. Otherwise, if identity crawler is turned off,
  all documents can be publicly searched. If you want to use access control for your documents
  and identity crawler is turned off, you can alternatively use the
  [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md")
  API to upload user and group access information for user context filtering.
- **Field mappings**—Choose to map your Microsoft Teams
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [Microsoft Teams template schema](ds-schemas.md#ds-msteams-schema "ds-schemas.md#ds-msteams-schema").

## Learn more

To learn more about integrating Amazon Kendra with your Microsoft Teams data
source, see:

- [Intelligently search your organization’s Microsoft Teams data source with
  the Amazon Kendra connector for Microsoft Teams](https://aws.amazon.com/blogs/machine-learning/intelligently-search-your-organizations-microsoft-teams-data-source-with-the-amazon-kendra-connector-for-microsoft-teams/ "https://aws.amazon.com/blogs/machine-learning/intelligently-search-your-organizations-microsoft-teams-data-source-with-the-amazon-kendra-connector-for-microsoft-teams/")

## Notes

- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to Microsoft Teams API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.
