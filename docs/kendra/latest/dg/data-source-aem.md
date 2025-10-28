# Adobe Experience Manager

###### Note

Adobe Experience Manager connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the Amazon Kendra Custom Connector Framework[1], designed to support a broader range of enterprise use cases with enhanced flexibility.

Adobe Experience Manager is a content management system that's used for creating
website or mobile app content. You can use Amazon Kendra to connect to
Adobe Experience Manager and index your pages and content assets.

Amazon Kendra supports Adobe Experience Manager (AEM) as a Cloud Service author
instance and Adobe Experience Manager On-Premise author and publish instance.

You can connect Amazon Kendra to your Adobe Experience Manager data source
using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") or the
[TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API.

For troubleshooting your Amazon Kendra Adobe Experience Manager data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-aem "#supported-features-aem")
- [Prerequisites](#prerequisites-aem "#prerequisites-aem")
- [Connection instructions](#data-source-procedure-aem "#data-source-procedure-aem")

## Supported features

Adobe Experience Manager data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- OAuth 2.0 and basic authentication
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Adobe Experience Manager
data source, make these changes in your Adobe Experience Manager and AWS accounts.

**In Adobe Experience Manager, make sure you
have**:

- Access to an account with administrative privileges, or an admin user.
- Copied your Adobe Experience Manager host URL.

###### Note

(On-premise/server) Amazon Kendra checks if the endpoint information included in
AWS Secrets Manager is the same the endpoint information specified in your data source
configuration details. This helps protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"), which is a
security issue where a user doesn’t have permission to perform an action but uses
Amazon Kendra as a proxy to access the configured secret and perform the action. If you
later change your endpoint information, you must create a new secret to sync this
information.

- Noted your basic authentication credentials of admin user name and
  password.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- **Optional**: Configured OAuth 2.0 credentials in
  Adobe Experience Manager (AEM) as a Cloud Service or AEM
  On-Premise. If you use AEM On-Premise, the credentials include client ID,
  client secret, and private key. If you use AEM as a Cloud Service, the
  credentials include client ID, client secret, private key, organization ID,
  technical account ID, and Adobe Identity Management System (IMS)
  host. For more information about how to generate these credentials for AEM as a
  Cloud Service, see [Adobe Experience Manager documentation](https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html "https://experienceleague.adobe.com/docs/experience-manager-learn/getting-started-with-aem-headless/authentication/service-credentials.html"). For AEM
  On-Premise, Adobe Granite OAuth 2.0 server implementation
  (com.adobe.granite.oauth.server) provides the support for OAuth
  2.0 server functionalities in AEM.
- Checked each document is unique in Adobe Experience Manager and across other
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

- Stored your Adobe Experience Manager authentication credentials in an
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
connect your Adobe Experience Manager data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Adobe Experience Manager data source,
you must provide the necessary details of your Adobe Experience Manager data
source so that Amazon Kendra can access your data. If you have not yet configured
Adobe Experience Manager for Amazon Kendra, see [Prerequisites](#prerequisites-aem "#prerequisites-aem").

Console
**To connect Amazon Kendra to
Adobe Experience Manager**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Adobe Experience Manager connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Adobe Experience Manager connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page,
   enter the following information:
   1. **Source**—Choose either
      **AEM On-Premise** or
      **AEM as a Cloud Service**.

   Enter your Adobe Experience Manager host URL.
   For example, if you use AEM On-Premise, you include the
   hostname and port:
   _https://hostname:port_.
   Or, if you use AEM as a Cloud Service, you can use the
   author URL:
   *https://author-xxxxxx-xxxxxxx.adobeaemcloud.com*. 2. **SSL certificate location**—Enter
   the path to the SSL certificate stored in an
   Amazon S3 bucket. You use this to connect to AEM
   On-Premise with a secure SSL connection. 3. **Authorization**—Turn on or off access control list (ACL) information for your
   documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
   and groups can access. The ACL information is used to filter search results based on the user or
   their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources"). 4. **Authentication**—Choose
   **Basic authentication** or
   **OAuth 2.0 authentication**. Then
   choose an existing AWS Secrets Manager secret or
   create a new secret to store your
   Adobe Experience Manager credentials. If
   you choose to create a new secret, an AWS Secrets Manager secret window opens.

   If you chose **Basic
   authentication**, enter a name for the secret,
   the Adobe Experience Manager site user name and
   password. The user must have admin permission or be an
   admin user.

   If you chose **OAuth 2.0
   authentication** and you use AEM
   On-Premise, enter a name for the secret, client ID,
   client secret, and private key. If you use AEM as a
   Cloud Service, enter a name for the secret, client ID,
   client secret, private key, organization ID, technical
   account ID, and Adobe Identity Management
   System (IMS) host.

   Save an add your secret. 5. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
   so, you must add **Subnets** and **VPC security groups**. 6. **Identity crawler**—Specify whether to turn on
   Amazon Kendra’s identity crawler. The identity crawler uses the access control list
   (ACL) information for your documents to filter search results based on the user or their
   group access to documents. If you have an ACL for your documents and choose to use your ACL,
   you can then also choose to turn on Amazon Kendra’s identity crawler to configure
   [user
   context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources") of search results. Otherwise, if identity crawler is turned off,
   all documents can be publicly searched. If you want to use access control for your documents
   and identity crawler is turned off, you can alternatively use the
   [PutPrincipalMapping](../APIReference/API_PutPrincipalMapping.md "../APIReference/API_PutPrincipalMapping.md")
   API to upload user and group access information for user context filtering. 7. **IAM role**—Choose an existing IAM
   role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 8. Choose **Next**.

7. On the **Configure sync settings** page,
   enter the following information:
   1. **Sync scope**—Set limits for
      crawling certain content types, page components, and
      roots paths, and filter content using regex expression
      patterns.
      1. **Content
         types**—Choose whether to crawl
         only pages or assets, or both.
      2. (Optional) **Additional
         configuration**—Configure the
         following settings:
         - **Page
           components**—The specific
           names of page components. The Page Component is
           an extensible page component designed to work
           with the Adobe Experience Manager template
           editor and allows page header/footer and structure
           components to be assembled with the template editor.
         - **Content fragment
           variations**—The specific
           names of content fragment variations. Content Fragments
           allow you to design, create, curate and publish
           page-independent content in Adobe Experience Manager.
           They allow you to prepare content ready for use in multiple
           locations/over multiple channels.
         - **Root paths**—The
           root paths to specific content.
         - **Regex
           patterns**—The regular
           expression patterns to include or exclude certain
           pages and assets.

   2. **Sync mode**—Choose how you want to update
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

   3. **Time zone ID**—If you use
      AEM On-Premise and the time zone of your server is
      different than the time zone of the Amazon Kendra
      AEM connector or index, you can specify the server time
      zone to align with the AEM connector or index. The default
      time zone for AEM On-Premise is the time zone of the
      Amazon Kendra AEM connector or index. The default time
      zone for AEM as a Cloud Service is Greenwich Mean Time.
   4. **Sync run schedule**, for
      **Frequency**—Choose how often to
      sync your data source content and update your index.
   5. Choose **Next**.

8. On the **Set field mappings** page,
   enter the following information:
   1. Select from the Amazon Kendra generated default
      data source fields you want to map to your index. To add
      custom data source fields, create an index field name to
      map to and the field data type.
   2. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to
Adobe Experience Manager**

You must specify a JSON of the [data source
schema](ds-schemas.md#ds-aem-schema "ds-schemas.md#ds-aem-schema") using the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API. You must
provide the following information:

- **Data
  source**—Specify the data source type as
  `AEM` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **AEM host URL**—Specify
  the Adobe Experience Manager host URL. For example, if
  you use AEM On-Premise, you include the hostname and port:
  _https://hostname:port_. Or, if
  you use AEM as a Cloud Service, you can use the author URL:
  *https://author-xxxxxx-xxxxxxx.adobeaemcloud.com*.
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

- **Authentication
  type**—Specify which type of authentication you
  want to use, either `Basic` or `OAuth2`.
- **AEM type**—Specify which
  type of Adobe Experience Manager you use, either
  `CLOUD` or `ON_PREMISE`.
- **Secret Amazon Resource Name
  (ARN)**—If you want to use basic
  authentication for either AEM On-Premise or Cloud, you provide
  a secret that stores your authentication credentials of your user
  name and password. You provide the Amazon Resource Name (ARN) of
  an AWS Secrets Manager secret. The secret is stored in a JSON
  structure with the following keys:

```
{
    "aemUrl": "`Adobe Experience Manager On-Premise host URL`",
    "username": "`user name with admin permissions`",
    "password": "`password with admin permissions`"
}
```

If you want to use OAuth 2.0 authentication for AEM
On-Premise, the secret is stored in a JSON structure with the
following keys:

```
{
    "aemUrl": "`Adobe Experience Manager host URL`",
    "clientId": "`client ID`",
    "clientSecret": "`client secret`",
    "privateKey": "`private key`"
}
```

If you want to use OAuth 2.0 authentication for AEM as a Cloud
Service, the secret is stored in a JSON structure with the
following keys:

```
{
    "clientId": "`client ID`",
    "clientSecret": "`client secret`",
    "privateKey": "`private key`",
    "orgId": "`organization ID`",
    "technicalAccountId": "`technical account ID`",
    "imsHost": "`Adobe Identity Management System (IMS) host`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Adobe Experience Manager connector and Amazon Kendra.
  For more information, see [IAM roles for Adobe Experience Manager
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Time zone ID**—If you
  use AEM On-Premise and the time zone of your server is
  different than the time zone of the Amazon Kendra AEM
  connector or index, you can specify the server time zone to
  align with the AEM connector or index.

The default time zone for AEM On-Premise is the time zone of
the Amazon Kendra AEM connector or index. The default time
zone for AEM as a Cloud Service is Greenwich Mean Time.

For information about the supported time zones IDs, see [Adobe Experience Manager JSON
schema](ds-schemas.md#aem-json "ds-schemas.md#aem-json").

- **Inclusion and exclusion
  filters**—Specify whether to include or
  exclude certain pages and assets.

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
- **Field mappings**—Choose to map your Adobe Experience Manager
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [Adobe Experience Manager template schema](ds-schemas.md#ds-aem-schema "ds-schemas.md#ds-aem-schema").
