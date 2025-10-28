# Drupal

###### Note

Drupal connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the Amazon Kendra Custom Connector Framework[1], designed to support a broader range of enterprise use cases with enhanced flexibility.

Drupal is an open-source content management system (CMS) that you can use to
create websites and web applications. You can use Amazon Kendra to index the following
in Drupal:

- Content—Articles, Basic pages, Basic blocks, User defined content types,
  User defined block types, Custom content types, Custom block types
- Comment—For any Content type and Block type
- Attachments—For any Content type and Block type
  You can connect Amazon Kendra to your Drupal data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") or the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API.

For troubleshooting your Amazon Kendra Drupal data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-drupal "#supported-features-drupal")
- [Prerequisites](#prerequisites-drupal "#prerequisites-drupal")
- [Connection instructions](#data-source-procedure-drupal "#data-source-procedure-drupal")
- [Notes](#drupal-notes "#drupal-notes")

## Supported features

Amazon Kendra Drupal data source connector supports the following
features:

- Field mappings
- User context filtering
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Drupal data source,
make these changes in your Drupal and AWS accounts.

**In Drupal, make sure you have:**

- Created a Drupal (Standard) Suite account and a user with an
  administrator role.
- Copied your Drupal site name and configured a host url. For
  example,
  `https://<hostname>/<drupalsitename>`.
- Configured basic authentication credentials containing a user name
  (Drupal website login user name) and password (Drupal
  website password).
- **Recommended:** Configured an OAuth 2.0
  credential token. Use this token along with your Drupal password
  grant, client id, client secret, user name (Drupal website login
  user name) and password (Drupal website password) to connect to
  Amazon Kendra.
- Added the following permissions in your Drupal account using an
  administrator role:
  - administer blocks
  - administer block_content display
  - administer block_content fields
  - administer block_content form display
  - administer views
  - view user email addresses
  - view own unpublished content
  - view page revisions
  - view article revisions
  - view all revisions
  - view the administration theme
  - access content
  - access content overview
  - access comments
  - search content
  - access files overview
  - access contextual links

###### Note

If there are user defined content types or user defined block types, or
any views and blocks are added to the Drupal website, they must
be provided with administrator access.

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

- Stored your Drupal authentication credentials in an
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
connect your Drupal data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Drupal data source you must provide
details of your Drupal credentials so that Amazon Kendra can access
your data. If you have not yet configured Drupal for Amazon Kendra see
[Prerequisites](#prerequisites-drupal "#prerequisites-drupal").

Console
**To connect Amazon Kendra to
Drupal**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Drupal connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Drupal connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6.  On the **Define access and security** page,
    enter the following information:
    1. In **Source**, for **Host
       URL**—The host URL of your
       Drupal site. For example,
       `https://<hostname>/<drupalsitename>`.
    2. For **SSL certificate
       location**—Enter the path to the SSL
       certificate stored in your Amazon S3
       bucket.
    3. **Authorization**—Turn on or off access control list (ACL) information for your
       documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
       and groups can access. The ACL information is used to filter search results based on the user or
       their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
    4. For **Authentication**—Choose
       between **Basic authentication** and
       **OAuth 2.0 authentication** based
       on your use case.
    5. **AWS Secrets Manager secret**—Choose an existing secret or create a new
       Secrets Manager secret to store your Drupal authentication
       credentials. If you choose to create a new secret an AWS Secrets Manager
       secret window opens.
       1. Enter following information in the
          **Create an AWS
          Secrets Manager secret
          window**:
          1. If you chose **Basic
             authentication**, enter a
             **Secret Name**, the
             **User name**,
             (Drupal site user name), and
             **Password** (Drupal
             site password) that you copied and choose
             **Save and add secret**.
          2. If you chose **OAuth 2.0
             authentication**, enter a
             **Secret Name**, **User
             name** (Drupal site user
             name), **Password**
             (Drupal site password),
             **Client ID**, and
             **Client secret** generated in
             your Drupal account and choose
             **Save and add secret**.

       2. Choose **Save**.

    6. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
       so, you must add **Subnets** and **VPC security groups**.
    7. **Identity crawler**—Specify whether to turn on
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
    8. **IAM role**—Choose an existing IAM
       role or create a new IAM role to access your repository credentials and index content.

    ###### Note

    IAM roles used for indexes cannot be used for data sources. If you are unsure
    if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
    errors. 9. Choose **Next**.

7.  On the **Configure sync settings** page,
    enter the following information:
    1. For **Sync scope**, choose from the
       following options:

    ###### Note

    When you choose to crawl
    **Articles**, **Basic
    pages**, and **Basic
    blocks**, their default fields will be
    synced automatically. You can also choose to sync
    their comments, attachments, custom fields and other
    custom entities.

        1. For **Select
         entities**:




        	* **Articles**—Choose
        	 whether to crawl **Articles**,
        	 their comments **Comments**, and
        	 their **Attachments**.
        	* **Basic
        	 pages**—Choose whether to crawl
        	 **Basic pages**, their
        	 **Comments**, and their
        	 **Attachments**.
        	* **Basic
        	 blocks**—Choose whether to crawl
        	 **Basic blocks**, their
        	 **Comments**, and their
        	 **Attachments**.
        	* You can also choose to add **Custom
        	 content types** and **Custom
        	 Blocks**.

    2. For **Additional configuration –
       optional**:
       - For **Regex
         pattern**—Add regular expression
         patterns to include or exclude specific entity
         titles and file names. You can add up to 100
         patterns.

    3. **Sync mode**—Choose how you want to update
       your index when your data source content changes. When you sync your
       data source with Amazon Kendra for the first time, all content
       is crawled and indexed by default. You must run a full sync of your
       data if your initial sync failed, even if you don't choose full sync
       as your sync mode option.
       - Full sync: Freshly index all content, replacing existing
         content each time your data source syncs with your index.
       - New, modified, deleted sync: Index only new, modified,
         and deleted content each time your data source syncs with
         your index. Amazon Kendra can use your data source's
         mechanism for tracking content changes and index content
         that changed since the last sync.

    4. In **Sync run schedule**,
       **Frequency**—How often
       Amazon Kendra will sync with your data
       source.
    5. Choose **Next**.

8.  On the **Set field mappings** page, enter the
    following information:
    1. For **Contents**,
       **Comments**, and
       **Attachments**—Select from
       the Amazon Kendra generated default data source
       fields you want to map to your index.
    2. **Add field**—To add custom data
       source fields to create an index field name to map to
       and the field data type.
    3. Choose **Next**.

9.  On the **Review and create** page, check that
    the information you have entered is correct and then select
    **Add data source**. You can also choose to edit your information from this page.
    Your data source will appear on the **Data sources** page after the data source has been
    added successfully.

API
**To connect Amazon Kendra to
Drupal**

You must specify a JSON of the [data source
schema](ds-schemas.md#ds-drupal-schema "ds-schemas.md#ds-drupal-schema") using the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API. You must
provide the following information:

- **Data
  source**—Specify the data source type as
  `DRUPAL` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
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

- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource Name
  (ARN) of a Secrets Manager secret that contains the
  authentication credentials you created in your
  Drupal account.

If you use basic authentication, the secret is stored in a
JSON structure with the following keys:

```
{
    "username": `"user name"`,
    "password": `"password"`
}
```

If you use OAuth 2.0 authentication, the secret is stored in a
JSON structure with the following keys:

```
{
    "username": `"user name"`,
    "password": `"password"`,
    "clientId": `"client id"`,
    "clientSecret": `"client secret"`
}
```

###### Note

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Drupal connector and Amazon Kendra.
  For more information, see [IAM roles for Drupal
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Inclusion and exclusion
  filters**—You can specify whether to include
  contents, comments, and attachments. You can also specify
  regular expression patterns to include or exclude contents,
  comments, and attachments.

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
- **Field mappings**—Choose to map your Drupal
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [Drupal template schema](ds-schemas.md#ds-drupal-schema "ds-schemas.md#ds-drupal-schema").

## Notes

- Drupal APIs have no official throttling limits.
- Java SDKs are not available for Drupal.
- Drupal data can be fetched only using native JSON API’s.
- Content types not associated with any Drupal
  **View** cannot be crawled.
- You need administrator access to crawl data from Drupal
  **Blocks**.
- There is no JSON API available to create the user defined content type using
  HTTP verbs.
- The document body and comments for **Articles**,
  **Basic pages**, **Basic blocks**, user
  defined content type, and user defined block type, are displayed in HTML format.
  If the HTML content is not well-formed, then the HTML related tags will appear
  in the document body and comments and will be visible in Amazon Kendra
  search results.
- Content types and **Block** types without description or body
  will not be ingested into Amazon Kendra. Only **Comments**
  and **Attachments** of such **Content** or
  **Block** types will be ingested into your Amazon Kendra index.
