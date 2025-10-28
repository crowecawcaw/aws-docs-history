# Zendesk

Zendesk is a customer relationship management system that helps businesses
automate and enhance customer support interactions. You can use Amazon Kendra to index your
Zendesk support tickets, ticket comments, ticket attachments, help center articles,
article comments, article comment attachments, guide community topics, community posts, and
community post comments.

You can filter by organization name if you want to index tickets that are only within a
specific organization. You can also choose to set a crawl date for when you want to start
crawling data from Zendesk.

You can connect Amazon Kendra to your Zendesk data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") and the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API.

For troubleshooting your Amazon Kendra Zendesk data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-zendesk "#supported-features-zendesk")
- [Prerequisites](#prerequisites-zendesk "#prerequisites-zendesk")
- [Connection instructions](#data-source-procedure-zendesk "#data-source-procedure-zendesk")
- [Learn more](#zendesk-learn-more "#zendesk-learn-more")
- [Notes](#zendesk-notes "#zendesk-notes")

## Supported features

Amazon Kendra Zendesk data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion/exclusion filters
- Change log, full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Zendesk data source, make
these changes in your Zendesk and AWS accounts.

**In Zendesk, make sure you have:**

- Created a Zendesk Suite (Professional/Enterprise) administrative
  account.
- Noted your Zendesk host URL. For example,
  `https://{sub-domain}.zendesk.com/`.

###### Note

(On-premise/server) Amazon Kendra checks if the endpoint information included in
AWS Secrets Manager is the same the endpoint information specified in your data source
configuration details. This helps protect against the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md"), which is a
security issue where a user doesn’t have permission to perform an action but uses
Amazon Kendra as a proxy to access the configured secret and perform the action. If you
later change your endpoint information, you must create a new secret to sync this
information.

- Set up OAuth 2.0 Authentication using the authorization code grant flow:
  1.  In Admin Center, navigate to Apps and integrations > APIs > Zendesk API.
  2.  Select the OAuth Clients tab and click "Add OAuth client".
  3.  Configure the OAuth client details: Set Client Name and Description, Set Client
      Kind to "Confidential", Add appropriate Redirect URLs (e.g., https://localhost/callback for testing), Save and securely store the
      generated Client ID and Client Secret.
  4.  Ensure the OAuth client has the required "read" scope (or "read write" if you need write access).
  5.  Generate an Access Token using the authorization code grant flow:
      - In a browser, navigate to:
        `https://{subdomain}.zendesk.com/oauth/authorizations/new?response_type=code&client_id={your_client_id}&redirect_uri={your_redirect_uri}&scope=read`
      - Authenticate and authorize the application when prompted.
      - After authorization, Zendesk redirects to the redirect_uri with a code parameter (e.g., https://localhost/callback?code={authorization_code}). Copy the authorization code.
      - Exchange the authorization code for an access token by sending a POST request to Zendesk's token endpoint:

      ```
      curl -X POST https://{subdomain}.zendesk.com/oauth/tokens \
        -H "Content-Type: application/x-www-form-urlencoded" \
        -d "grant_type=authorization_code&code={authorization_code}&client_id={your_client_id}&client_secret={your_client_secret}&redirect_uri={your_redirect_uri}&scope=read"
      ```

      - Zendesk responds with a JSON object containing the access_token. Extract and securely store this access token.

  6.  Store the generated access token securely. This access token will be used for Kendra integration.

- ###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- **Optional:** Installed an SSL certificate to allow
  Amazon Kendra to connect.
- Checked each document is unique in Zendesk and across other
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

- Stored your Zendesk authentication credentials in an
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
connect your Zendesk data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Zendesk data source, you must provide
the necessary details of your Zendesk data source so that Amazon Kendra can access
your data. If you have not yet configured Zendesk for Amazon Kendra,
see [Prerequisites](#prerequisites-zendesk "#prerequisites-zendesk").

Console
**To connect Amazon Kendra to
Zendesk**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Zendesk connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Zendesk connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page, enter the
   following information:
   1. **Zendesk URL**—Enter your Zendesk URL.
      For example, `https://{sub-domain}.zendesk.com/`.
   2. **Authorization**—Turn on or off access control list (ACL) information for your
      documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
      and groups can access. The ACL information is used to filter search results based on the user or
      their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
   3. **AWS Secrets Manager secret**—Choose an existing secret or create a new
      Secrets Manager secret to store your Zendesk authentication
      credentials. If you choose to create a new secret an AWS Secrets Manager
      secret window opens.
      1. Create a new secret with the following structure:

      ```
      {
               "hostUrl": "https://yoursubdomain.zendesk.com/",
               "accessToken": "your_access_token"
      }
      ```

      ###### Note

      For Kendra integration, the secret name should start with 'AmazonKendra-Zendesk-' followed by your chosen identifier (e.g., 'AmazonKendra-Zendesk-MyConnector'). 2. Save and add your secret.

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

7. On the **Configure sync settings** page, enter the following
   information:
   1. **Select contents**—Select the types of content
      you want to crawl from tickets, to help center articles, community topics,
      and more.
   2. **Organization name**—Enter the Zendesk
      organization names to filter content.
   3. **Sync start date**—Enter the date from which you want
      to start crawling your content.
   4. **Regex patterns**—Add regular expression patterns to
      include or exclude certain files. You can add up to 100 patterns.
   5. **Sync mode**—Choose how you want to update
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

   6. In **Sync run schedule** for
      **Frequency**—Choose how often to sync
      your data source content and update your index.
   7. Choose **Next**.

8. On the **Set field mappings** page, enter the
   following information:
   1. **Default data source
      fields**—Select from the Amazon Kendra generated
      default data source fields you want to map to your index.
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
Zendesk**

You must specify a JSON of the [data source schema](ds-schemas.md "ds-schemas.md") using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API. You must provide the following
information:

- **Data
  source**—Specify the data source type as
  `ZENDESK` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **Host URL**—Provide your Zendesk host URL
  as part of the connection configuration or repository endpoint details. For
  example, `https://yoursubdomain.zendesk.com`.
- **Change log**—Whether
  Amazon Kendra should use the Zendesk data
  source change log mechanism to determine if a document must be
  updated in the index.

###### Note

Use the change log if you don’t want Amazon Kendra
to scan all of the documents. If your change log is large,
it might take Amazon Kendra less time to scan the
documents in the Zendesk data source than to
process the change log. If you are syncing your Zendesk
data source with your index for the first time, all documents are scanned.

- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your Zendesk account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "hostUrl": "`https://yoursubdomain.zendesk.com`",
    "clientId": "`client ID`",
    "clientSecret": "`Zendesk client secret`",
    "userName": "`Zendesk user name`",
    "password": "`Zendesk password`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Zendesk connector and Amazon Kendra.
  For more information, see [IAM roles for Zendesk
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Document/content types**—Specify
  whether to crawl:
  - Support tickets, ticket comments, and/or ticket comment attachments
  - Help center articles, article attachments, and article comments
  - Guide community topics, posts, or post comments

- **Inclusion and exclusion
  filters**—Specify whether to include or exclude
  certain Slack content. If you use a bot token as part of
  your Slack authentication credentials, you must add the bot
  token to the channel you want to index. You cannot index direct
  messages and group messages using a bot token.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **User context filtering and access control**—Amazon Kendra
  crawls the access control list (ACL) for your documents,
  if you have an ACL for your documents. The ACL
  information is used to filter search results based on the user or their
  group access to documents. For more information, see [User context
  filtering](user-context-filter.md#datasource-context-filter "user-context-filter.md#datasource-context-filter").
- **Field mappings**—Choose to map your Zendesk
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [Zendesk template schema](ds-schemas.md#ds-schema-zendesk "ds-schemas.md#ds-schema-zendesk").

## Learn more

To learn more about integrating Amazon Kendra with your Zendesk data
source, see:

- [Discover insights from Zendesk with Amazon Kendra intelligent
  search](https://aws.amazon.com/blogs/machine-learning/discover-insights-from-zendesk-with-amazon-kendra-intelligent-search/ "https://aws.amazon.com/blogs/machine-learning/discover-insights-from-zendesk-with-amazon-kendra-intelligent-search/")

## Notes

- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to Zendesk API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.
