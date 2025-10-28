# Dropbox

Dropbox is a file hosting service that offers cloud storage, document
organization, and document templating services. If you are a Dropbox user, you
can use Amazon Kendra to index your Dropbox files, Dropbox Paper,
Dropbox Paper Templates, and stored shortcuts to web pages. You can also
configure Amazon Kendra to index specific Dropbox files, Dropbox
Paper, Dropbox Paper Templates, and stored shortcuts to web pages.

Amazon Kendra supports both Dropbox and Dropbox Advanced for
Dropbox Business.

You can connect Amazon Kendra to your Dropbox data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") and the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API.

For troubleshooting your Amazon Kendra Dropbox data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-dropbox "#supported-features-dropbox")
- [Prerequisites](#prerequisites-dropbox "#prerequisites-dropbox")
- [Connection instructions](#data-source-procedure-dropbox "#data-source-procedure-dropbox")
- [Learn more](#dropbox-learn-more "#dropbox-learn-more")
- [Notes](#dropbox-notes "#dropbox-notes")

## Supported features

Amazon Kendra Dropbox data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Dropbox data source,
make these changes in your Dropbox and AWS accounts.

**In Dropbox, make sure you have:**

- Created a Dropbox Advanced account and set up an admin user.
- Configured a Dropbox app with a unique **App name**,
  activated **Scoped Access**. See [Dropbox documentation on creating an app](https://www.dropbox.com/developers/reference/getting-started#app%20console "https://www.dropbox.com/developers/reference/getting-started#app%20console").
- Activated **Full Dropbox** permissions on the
  Dropbox console and added the following permissions:
  - files.content.read
  - files.metadata.read
  - sharing.read
  - file_requests.read
  - groups.read
  - team_info.read
  - team_data.content.read

- Noted your Dropbox app key, Dropbox app secret, and
  Dropbox access token for basic authentication credentials.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- Configured and copied a temporary Oauth 2.0 access token for your
  Dropbox app. This token is temporary and expires after 4 hours. See
  [Dropbox
  documentation on OAuth authentication](https://developers.dropbox.com/oauth-guide "https://developers.dropbox.com/oauth-guide").

###### Note

It is recommended that you create a Dropbox refresh access
token that never expires, rather that relying on a one-time access token
that expires after 4 hours. A refresh access token is permanent and never
expires so that you can continue to sync your data source in the
future.

- **Recommended:** Configured a Dropbox
  permanent refresh token that never expires to allow Amazon Kendra to
  continue to sync your data source without any disruptions. See [Dropbox documentation on
  refresh tokens](https://developers.dropbox.com/oauth-guide "https://developers.dropbox.com/oauth-guide").
- Checked each document is unique in Dropbox and across other
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

- Stored your Dropbox authentication credentials in an
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
connect your Dropbox data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Dropbox data source, you must provide
the necessary details of your Dropbox data source so that Amazon Kendra can access
your data. If you have not yet configured Dropbox for Amazon Kendra,
see [Prerequisites](#prerequisites-dropbox "#prerequisites-dropbox").

Console
**To connect Amazon Kendra to
Dropbox**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Dropbox connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Dropbox connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page,
   enter the following information:
   1. **Authorization**—Turn on or off access control list (ACL) information for your
      documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
      and groups can access. The ACL information is used to filter search results based on the user or
      their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
   2. **Type of authentication
      token**—Choose either a
      permanent token (recommended)
      or a temporary access token.
   3. **AWS Secrets Manager secret**—Choose an existing secret or create a new
      Secrets Manager secret to store your Dropbox authentication
      credentials. If you choose to create a new secret an AWS Secrets Manager
      secret window opens.
      1. Enter following information in the
         **Create an AWS
         Secrets Manager secret
         window**:
         1. **Secret name**—A
            name for your secret. The prefix
            ‘AmazonKendra-Dropbox-’ is
            automatically added to your secret name.
         2. For **App key**,
            **App secret**, and token
            information (permanent or temporary)—Enter
            the authentication credential values configured
            in Dropbox.

      2. Save and add your secret.

   4. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
      so, you must add **Subnets** and **VPC security groups**.
   5. **Identity crawler**—Specify whether to turn on
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
   6. **IAM role**—Choose an existing IAM
      role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 7. Choose **Next**.

7. On the **Configure sync settings** page,
   enter the following information:
   1. For **Select entities or content
      types**—Choose Dropbox entities or
      content types you want to crawl.
   2. In **Additional configuration** for
      **Regex patterns**—Add
      regular expression patterns to include or exclude
      certain files.
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
   1. **Files**, **Dropbox
      Paper**, and **Dropbox Paper
      templates**—Select from the Amazon Kendra generated default data source fields you
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
Dropbox**

You must specify a JSON of the [data source schema](ds-schemas.md#ds-dropbox-schema "ds-schemas.md#ds-dropbox-schema") using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API. You must provide the following
information:

- **Data
  source**—Specify the data source type as
  `DROPBOX` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
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

- **Access token type**—Specify
  whether you want to use permanent or temporary access token for your
  AWS Secrets Manager secret that stores your authentication crednetials.

###### Note

It's recommended that you create a refresh access token that never
expires in Dropbox rather that relying on a one-time access token that
expires after 4 hours. You create an app and a refresh access token in
the Dropbox developer console and provide the access token in your
secret.

- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your Dropbox account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "appKey": "`Dropbox app key`",
    "appSecret": "`Dropbox app secret`",
    "accesstoken": "`temporary access token or refresh access token`"
}
```

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
- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Dropbox connector and Amazon Kendra.
  For more information, see [IAM roles for Dropbox
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Document/content types**—Specify
  whether to crawl files in your Dropbox, Dropbox Paper documents, Dropbox
  Paper templates, and web page shortcuts stored in your Dropbox.
- **Inclusion and exclusion
  filters**—Specify whether to include or exclude
  certain files.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Access control list (ACL)**—Specify
  whether to crawl ACL information for your documents, if you have an
  ACL and want to use it for access control. The ACL specifies which
  documents that users and groups can access. The ACL
  information is used to filter search results based on the user or
  their group access to documents. For more information, see
  [User
  context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
- **Field mappings**—Choose to map your Dropbox
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [Dropbox template schema](ds-schemas.md#ds-dropbox-schema "ds-schemas.md#ds-dropbox-schema").

## Learn more

To learn more about integrating Amazon Kendra with your Dropbox data source,
see:

- [Index your Dropbox content using the Dropbox connector for
  Amazon Kendra](https://aws.amazon.com/blogs/machine-learning/index-your-dropbox-content-using-the-dropbox-connector-for-amazon-kendra/ "https://aws.amazon.com/blogs/machine-learning/index-your-dropbox-content-using-the-dropbox-connector-for-amazon-kendra/")

## Notes

- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to Dropbox API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.
