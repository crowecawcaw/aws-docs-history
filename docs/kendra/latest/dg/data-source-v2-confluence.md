# Confluence connector V2.0

Confluence is a collaborative work-management tool designed for sharing, storing, and working on
project planning, software development, and product management. You can use Amazon Kendra to
index your Confluence spaces, pages (including nested pages), blogs, and comments and attachments to
indexed pages and blogs.

For troubleshooting your Amazon Kendra Confluence data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-v2-confluence "#supported-features-v2-confluence")
- [Prerequisites](#prerequisites-v2-confluence "#prerequisites-v2-confluence")
- [Connection instructions](#data-source-procedure-v2-confluence "#data-source-procedure-v2-confluence")

## Supported features

Amazon Kendra Confluence data source connector supports the following features:

- Field mappings
- User access control
- Inclusion/exclusion patterns
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Confluence data source, make these changes
in your Confluence and AWS accounts.

**In Confluence, make sure you have:**

- Copied your Confluence instance URL. For example:
  `https://example.confluence.com`, or
  `https://www.example.confluence.com/`, or `https://
atlassian.net/`. You need your Confluence instance URL to connect to Amazon Kendra.

If you're using Confluence Cloud, your host URL must end with
`atlassian.net/`.

###### Note

The following URL formats are **not** supported:

    + `https://example.confluence.com/xyz`
    + `https://www.example.confluence.com//wiki/spacekey/xxx`
    + `https://atlassian.net/xyz`

###### Note

(On-premise/server) Amazon Kendra checks if the endpoint information included in
AWS Secrets Manager is the same the endpoint information specified in your data source
configuration details. This helps protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"), which is a
security issue where a user doesn’t have permission to perform an action but uses
Amazon Kendra as a proxy to access the configured secret and perform the action. If you
later change your endpoint information, you must create a new secret to sync this
information.

- Configured basic authentication credentials containing a user name (email ID used to log
  into Confluence) and password (Confluence API token as the password). See [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/#Create-an-API-token "https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/#Create-an-API-token").

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- **Optional:** Configured OAuth 2.0 credentials containing a
  Confluence app key, Confluence app secret, Confluence access token, and Confluence refresh token to allow
  Amazon Kendra to connect to your Confluence instance. If your access token expires, you can
  either use the refresh token to regenerate your access token and refresh token pair. Or, you
  can repeat the authorization process. For more information on access tokens, see [Manage
  OAuth access tokens](https://support.atlassian.com/confluence-cloud/docs/manage-oauth-access-tokens/ "https://support.atlassian.com/confluence-cloud/docs/manage-oauth-access-tokens/").
- (For Confluence Server/Data Center only) **Optional:**
  Configured a Personal Access Token (PAT) in Confluence. See [Using Personal Access Tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html "https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html").

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

- Stored your Confluence authentication credentials in an
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
connect your Confluence data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Confluence data source, you must provide the necessary
details of your Confluence data source so that Amazon Kendra can access your data. If you have
not yet configured Confluence for Amazon Kendra see [Prerequisites](#prerequisites-v2-confluence "#prerequisites-v2-confluence").

Console
**To connect Amazon Kendra to Confluence**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Confluence connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Confluence connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6.  On the **Define access and security** page, enter the following
    information:
    1. In **Source**, choose either **Confluence Cloud** or
       **Confluence Server/Data Center**.
    2. **Confluence URL**—Enter the Confluence host URL. For example,
       `https://example.confluence.com`.
    3. (For Confluence Server/Data Center only) **SSL certificate location -
       _optional_**—Enter the Amazon S3 path to
       your SSL certificate file for Confluence Server.
    4. (For Confluence Server/Data Center only) **Web proxy -
       _optional_**—Enter the web proxy host name (without
       the `http://` or `https://` protocol) and port number (port used
       by the host URL transport protocol). The port number should be a numeric value between 0
       and 65535.
    5. **Authorization**—Turn on or off access control list (ACL) information for your
       documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
       and groups can access. The ACL information is used to filter search results based on the user or
       their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
    6. **Authentication**—Choose either **Basic
       authentication**, **Oauth 2.0 authentication**, or (For
       Confluence Server/Data Center only) **Personal Access Token
       authentication**.
    7. **AWS
       Secrets Manager secret**—Choose an existing secret or create a new
       Secrets Manager secret to store your Confluence authentication credentials. If you
       choose to create a new secret an AWS
       Secrets Manager secret window opens. Enter the following information in the
       window:
       1. **Secret name**—A name for your secret. The prefix
          ‘AmazonKendra-Confluence-’ is automatically added to your secret name.
       2. If using **Basic Authentication**—Enter the secret name,
          user name, and password (Confluence API token as the password) you configured in
          Confluence.

       If using **OAuth2.0 Authentication**—Enter the secret
       name, app key, app secret, access token, and refresh token you configured in
       Confluence.

       (Confluence Server/Data Center only) If using **Personal Access Token
       authentication**—Enter the secret name and Confluence token you
       configured in your Confluence. 3. Save and add your secret.

    8. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
       so, you must add **Subnets** and **VPC security groups**.
    9. **Identity crawler**—Specify whether to turn on
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
    10. **IAM role**—Choose an existing IAM
        role or create a new IAM role to access your repository credentials and index content.

    ###### Note

    IAM roles used for indexes cannot be used for data sources. If you are unsure
    if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
    errors. 11. Choose **Next**.

7.  On the **Configure sync settings** page, enter the following
    information:
    1. In **Sync scope**, for **Sync
       contents**—Choose to sync from the following content types: Pages, page
       comments, page attachments, blogs, blog comments, blog attachments, personal spaces, and
       archived spaces.

    ###### Note

    Page comments and page attachments can only be seleted if you choose to sync
    **Pages**. Blog comments and blog attachments can only be seleted if
    you choose to sync **Blogs**.

    ###### Important

    If you don't specify a space key regex pattern in **Additional
    configuration**, all pages and blogs will be crawled by default. 2. In **Additional configuration**, for **Maximum file
    size**—Specify the file size limit in MBs that Amazon Kendra will
    crawl. Amazon Kendra will crawl only the files within the size limit you define.
    The default file size is 50 MB. The maximum file size should be greater than 0 MB and
    less than or equal to 50 MB.

    For **Spaces regex patterns**—Specify whether to include or
    exclude specific spaces in your index using:

        * Space key (for example, `my-space-123`)


        ###### Note

        If you don't specify a space key regex pattern, all pages and blogs will be
         crawled by default.
        * URL (for example, `.*/MySite/MyDocuments/`)
        * File type (for example, `.*\.pdf, .*\.txt`)

    For **Entity title regex patterns**—Specify regular
    expression patterns to include or exclude certain blogs, pages, comments, and
    attachments by titles.

    ###### Note

    If you want to include or exclude crawling a specific page or subpage, you can use
    page title regex patterns. 3. **Sync mode**—Choose how you want to update your index when
    your data source content changes. When you sync your data source with Amazon Kendra
    for the first time, all content is crawled and indexed by default. You must run a full
    sync of your data if your initial sync failed, even if you don't choose full sync as
    your sync mode option.

        * Full sync: Freshly index all content, replacing existing content each time your
         data source syncs with your index.
        * New, modified, deleted sync: Index only new, modified, and deleted content each
         time your data source syncs with your index. Amazon Kendra can use your data
         source's mechanism for tracking content changes and index content that changed since
         the last sync.

    4. In **Sync run schedule**, for
       **Frequency**—Choose how often to sync your data source content
       and update your index.
    5. Choose **Next**.

8.  On the **Set field mappings** page, enter the following
    information:
    1. Select from the Amazon Kendra generated default data source fields you want to
       map to your index. To add custom data source fields, create an index field name to map
       to and the field data type.
    2. Choose **Next**.

9.  On the **Review and create** page, check that
    the information you have entered is correct and then select
    **Add data source**. You can also choose to edit your information from this page.
    Your data source will appear on the **Data sources** page after the data source has been
    added successfully.

API
**To connect Amazon Kendra to Confluence**

You must specify a JSON of the [data source schema](ds-schemas.md#ds-confluence-schema "ds-schemas.md#ds-confluence-schema")
using the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API. You must provide the following information:

- **Data source**—Specify the data source type as
  `CONFLUENCEV2` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON schema. Also specify the data source
  as `TEMPLATE` when you call the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md")
  API.
- **Host URL**—Specify the Confluence host URL
  instance. For example, `https://example.confluence.com`.
- **Sync mode**—Specify how Amazon Kendra
  should update your index when your data source content changes. When you sync your data
  source with Amazon Kendra for the first time, all content is crawled and indexed by
  default. You must run a full sync of your data if your initial sync failed, even if you
  don't choose full sync as your sync mode option. You can choose between:
  - `FORCED_FULL_CRAWL` to freshly index all content, replacing existing
    content each time your data source syncs with your index.
  - `FULL_CRAWL` to index only new, modified, and deleted content each time
    your data source syncs with your index. Amazon Kendra can use your data source’s
    mechanism for tracking content changes and index content that changed since the last
    sync.

- **Authentication type**—Specify the type of
  authentication, whether `Basic`, `OAuth2`, (Confluence Server only)
  `Personal-token`.
- (Optional–For Confluence Server only) **SSL certificate
  location**—Specificy the `S3bucketName` and
  `s3certificateName` you used to store your SSL certificate.
- **Secret Amazon Resource Name (ARN)**—Provide the
  Amazon Resource Name (ARN) of a Secrets Manager secret that contains the authentication
  credentials you configured in Confluence. If you use basic authentication, the secret is
  stored in a JSON structure with the following keys:

```
{
    "username": "`email ID or user name`",
    "password": "`Confluence API token`"
}
```

If you use OAuth 2.0 authentication, the secret is stored in a JSON structure with
the following keys:

```
{
    "confluenceAppKey": "`app key`",
    "confluenceAppSecret": "`app secret`",
    "confluenceAccessToken": "`access token`",
    "confluenceRefreshToken": "`refresh token`"
}
```

(For Confluence Server only) If you use basic authentication, the secret is stored in a
JSON structure with the following keys:

```
{
    "hostUrl": "`Confluence Server host URL`",
    "username": "`Confluence Server user name`",
    "password": "`Confluence Server password`"
}
```

(For Confluence Server only) If you use Personal Access Token authentication, the secret
is stored in a JSON structure with the following keys:

```
{
    "hostUrl": "`Confluence Server host URL`",
    "patToken": "`personal access token`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Confluence connector and Amazon Kendra.
  For more information, see [IAM roles for Confluence
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **File size**—Specify the maximun file size to
  crawl.
- **Document/content types**—Specify whether to crawl
  pages, page comments, page attachments, blogs, blog comments, blog attachments, spaces and
  archived spaces.
- **Inclusion and exclusion filters**—Specify
  whether to include or exclude certain spaces, pages, blogs, and their comments and
  attachments.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Web proxy**—Specify your web proxy information
  if you want to connect to your Confluence URL instance via a web proxy. You can use this
  option for Confluence Server.
- **Access control list (ACL)**—Specify
  whether to crawl ACL information for your documents, if you have an
  ACL and want to use it for access control. The ACL specifies which
  documents that users and groups can access. The ACL
  information is used to filter search results based on the user or
  their group access to documents. For more information, see
  [User
  context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
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
- **Field mappings**—Choose to map your Confluence
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [Confluence template
schema](ds-schemas.md#ds-confluence-schema "ds-schemas.md#ds-confluence-schema").

### Notes

- Personal Access Token (PAT) is not available for Confluence Cloud.
