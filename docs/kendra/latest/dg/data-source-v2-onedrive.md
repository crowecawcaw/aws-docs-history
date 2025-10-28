# Microsoft OneDrive connector

V2.0

Microsoft OneDrive is cloud-based storage service that you can use to store,
share, and host your content. You can use Amazon Kendra to index your OneDrive
data source.

You can connect Amazon Kendra to your OneDrive data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") and the [OneDriveConfiguration](OneDriveConfiguration.md "OneDriveConfiguration.md") API.

###### Note

Support for OneDrive Connector V1.0 / OneDriveConfiguration API is scheduled to end by June 2023. We recommend using OneDrive Connector V2.0 / TemplateConfiguration API. Version 2.0
provides additional ACLs and identity crawler functionality.

For troubleshooting your Amazon Kendra OneDrive data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-v2-onedrive "#supported-features-v2-onedrive")
- [Prerequisites](#prerequisites-v2-onedrive "#prerequisites-v2-onedrive")
- [Connection instructions](#data-source-procedure-v2-onedrive "#data-source-procedure-v2-onedrive")

## Supported features

Amazon Kendra OneDrive data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your OneDrive data source, make
these changes in your OneDrive and AWS accounts.

**In OneDrive, make sure you have:**

- Created a OneDrive account in Office 365.
- Noted your Microsoft 365 tenant ID. You can find your tenant ID in the Properties of your
  Azure Active Directory Portal or in your OAuth application.
- Created an OAuth application in the Azure portal and noted the client ID and
  client secret or client credentials used for authentication with an AWS Secrets Manager secret. See [Microsoft tutorial](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/walkthrough-register-app-azure-active-directory "https://learn.microsoft.com/en-us/power-apps/developer/data-platform/walkthrough-register-app-azure-active-directory") and [Registered app example](https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application "https://learn.microsoft.com/en-us/azure/healthcare-apis/register-application") for more information.

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

- Used the AD application ID to register a secret key for the application on the AD site.
  The secret key must contain the application ID and a secret key.
- Copied the AD domain of the organization.
- Added the following permissions to your AD application on the Microsoft Graph
  option:
  - Read files in all site collections (File.Read.All)
  - Read all users' full profiles(User.Read.All)
  - Read all groups (Group.Read.All)
  - Read all notes (Notes.Read.All)

- Copied the list of users whose documents must be indexed. You can choose to provide a
  list of user names, or you can provide the user names in a file stored in an Amazon S3. After you create the data source, you can:
  - Modify the list of users.
  - Change from a list of users to a list stored in an Amazon S3 bucket.
  - Change the Amazon S3 bucket location of a list of users. If you change the
    bucket location, you must also update the IAM role for the data source so
    that it has access to the bucket.

  ###### Note

  If you store the list of user names in an Amazon S3 bucket, the IAM policy for the data source must provide access to the bucket and access to the
  key that the bucket was encrypted with, if any.

  The OneDrive connector uses **Email from Contact
  Information** present in the **Onedrive User Properties**. Make
  sure the user whose data you want to crawl has the email field configured in the
  **Contact Information** page as for new users this might be blank.

**In your AWS account, make sure you
have:**

- Created an Amazon Kendra index and, if using the API, noted the index id.
- Created an IAM role for your data source and, if using the API, noted the
  ARN of the IAM role.
- Stored your OneDrive authentication credentials in an AWS
  Secrets Manager secret and, if using the API, noted the ARN of the secret.

If you don’t have an existing IAM role or secret, you can use the console to
create a new IAM role and Secrets Manager secret when you connect your
OneDrive data source to Amazon Kendra. If you are using the API, you must provide
the ARN of an existing IAM role and Secrets Manager secret, and an index
id.

## Connection instructions

To connect Amazon Kendra to your OneDrive data source you must provide
details of your OneDrive credentials so that Amazon Kendra can access your data.
If you have not yet configured OneDrive for Amazon Kendra, see [Prerequisites](#prerequisites-v2-onedrive "#prerequisites-v2-onedrive").

Console
**To connect Amazon Kendra to OneDrive**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **OneDrive connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **OneDrive connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page, enter the following
   information:
   1. **OneDrive tenant ID**—Enter the OneDrive tenant ID without
      the protocol.
   2. **Authorization**—Turn on or off access control list (ACL) information for your
      documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
      and groups can access. The ACL information is used to filter search results based on the user or
      their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
   3. In **Authentication**—Choose between
      **New** and **Existing**.
   4. 1. If you choose **Existing**, select an existing secret for
         **Select secret**.
      2. If you choose **New**, enter following information in the
         **New AWS
         Secrets Manager secret** section:
         1. **Secret name**—A name for your secret. The prefix
            ‘AmazonKendra-OneDrive-’ is automatically added to your secret
            name.
         2. For **Client ID** and **Client
            Secret**—Enter the client ID and client secret.

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

7. On the **Configure sync settings** page, enter the following
   information:
8. 1. For **Sync scope**—Choose which users' OneDrive data to
      index. You can add a maximum of 10 users manually.
   2. For **Additional configurations**—Add regular expression
      patterns to include or exclude certain content. You can add up to 100 patterns.
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
      **Frequency**—Choose how often
      to sync your data source content and update your index.
   5. Choose **Next**.

9. On the **Set field mappings** page, enter the following
   information:
   1. **Default data source fields**—Select from
      the Amazon Kendra generated default data source
      fields that you want to map to your index.
   2. Choose **Next**.

10. On the **Review and create** page, check that
    the information you have entered is correct and then select
    **Add data source**. You can also choose to edit your information from this page.
    Your data source will appear on the **Data sources** page after the data source has been
    added successfully.

API
**To connect Amazon Kendra to
OneDrive**

You must specify a JSON of the [data source schema](ds-schemas.md#ds-onedrive-schema "ds-schemas.md#ds-onedrive-schema") using
the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API. You must provide the following information:

- **Data
  source**—Specify the data source type as
  `ONEDRIVEV2` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **Tenant ID**—Specify the Microsoft 365 tenant
  ID. You can find your tenant ID in the Properties of your Azure Active Directory Portal or
  in your OAuth application.
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

- **Secret Amazon Resource Name (ARN)**—Provide the
  Amazon Resource Name (ARN) of a Secrets Manager secret that contains the authentication
  credentials you created in your OneDrive account.

If you use OAuth 2.0 authentication, the secret is stored in a JSON structure with
the following keys:

```
{
    "clientId": "`client ID`",
    "clientSecret": "`client secret`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the OneDrive connector and Amazon Kendra.
  For more information, see [IAM roles for OneDrive
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Inclusion and exclusion filters**—You can specify
  whether to include or exclude certain files, OneNote sections, and OneNote pages.

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
- **Field mappings**—You can only map built-in or
  common index fields for the Amazon Kendra OneDrive connector. Custom field mapping is not
  available for the OneDrive connector because of API limitations. For more
  information, see [Mapping data source fields](field-mapping.md "field-mapping.md").

For a list of other important JSON keys to configure, see [OneDrive template schema](ds-schemas.md#ds-onedrive-schema "ds-schemas.md#ds-onedrive-schema").
