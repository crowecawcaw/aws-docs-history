# Salesforce connector V1.0

Salesforce is a customer relationship management (CRM) tool for managing support,
sales, and marketing teams. You can use Amazon Kendra to index your Salesforce
standard objects and even custom objects.

###### Important

Amazon Kendra uses the Salesforce API version 48. The Salesforce API
limits the number of requests that you can make per day. If Salesforce exceeds those
requests, it retries until it is able to continue.

###### Note

Salesforce connector V1.0 / SalesforceConfiguration API ended in 2023. We recommend
migrating to or using Salesforce connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra Salesforce data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-v1-salesforce "#supported-features-v1-salesforce")
- [Prerequisites](#prerequisites-v1-salesforce "#prerequisites-v1-salesforce")
- [Connection instructions](#data-source-procedure-v1-salesforce "#data-source-procedure-v1-salesforce")

## Supported features

Amazon Kendra Salesforce data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion/exclusion filters

## Prerequisites

Before you can use Amazon Kendra to index your Salesforce data source, make
these changes in your Salesforce and AWS accounts.

**In Salesforce, make sure you have:**

- Created a Salesforce account and have noted the user name and password you use to
  connect to Salesforce.
- Created a Salesforce Connected App account with OAuth activated and have copied
  the consumer key (client ID) and consumer secret (client secret) assigned to your
  Salesforce Connected App. The client ID and client secret are used as your
  authentication credentials stored in an AWS Secrets Manager secret. See [Salesforce documentation on Connected Apps](https://help.salesforce.com/s/articleView?id=sf.connected_app_overview.htm&type=5 "https://help.salesforce.com/s/articleView?id=sf.connected_app_overview.htm&type=5") for more information.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- Copied the Salesforce security token associated with the account used to connect
  to Salesforce.
- Copied the URL of the Salesforce instance that you want to index. Typically, this
  is `https://<company>.salesforce.com/`. The server must be
  running a Salesforce connected app.
- Added credentials to your Salesforce server for a user with read-only access to
  Salesforce by cloning the ReadOnly profile and then adding the View All Data and
  Manage Articles permissions. These credentials identify the user making the connection and the
  Salesforce connected app that Amazon Kendra connects to.
- Checked each document is unique in Salesforce and across other
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

- Stored your Salesforce authentication credentials in an
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
connect your Salesforce data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Salesforce data source, you must provide the
necessary details of your Salesforce data source so that Amazon Kendra can access
your data. If you have not yet configured Salesforce for Amazon Kendra see [Prerequisites](#prerequisites-v1-salesforce "#prerequisites-v1-salesforce").

Console
**To connect Amazon Kendra to Salesforce**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose
   the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control**
settings under **Index settings**. 3. On the **Getting started** page, choose **Add data
source**. 4. On the **Add data source** page, choose **Salesforce
connector V1.0**, and then choose **Add connector**. 5. On the **Specify data source details** page, enter the following
information:

    1. **Data source name**—Enter a name for your data source. You
     can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description
     for your data source.
    3. **Default language**— A language to filter your documents
     for the index. Unless you specify otherwise, the language defaults to English. Language
     specified in metadata overrides selected language.
    4. **Add new tag**—Tags to search and filter your resources or
     track your shared costs.
    5. Choose **Next**.

6. On the **Define access and security** page, enter the following
   information:
   1. **Salesforce URL**—Enter the instance URL for the
      Salesforce site that you want to index.
   2. For **Type of authentication**, choose between
      **Existing** and **New** to store your
      Salesforce authentication credentials. If you choose to create a new secret an
      AWS
      Secrets Manager secret window opens.
      1. Enter following information in the **Create an AWS
         Secrets Manager secret window**:
         1. **Secret name**—A name for your secret. The prefix
            ‘AmazonKendra-Salesforce-’ is automatically added to your secret
            name.
         2. For **User name**, **Password**,
            **Security token**, **Consumer key**,
            **Consumer secret**, and **Authentication
            URL**—Enter the authentication credential values you created in your
            Salesforce account.
         3. Choose **Save authentication**.

   3. **IAM role**—Choose an existing IAM
      role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 4. Choose **Next**.

7. On the **Configure sync settings** page, enter the following
   information:
   1. For **Crawl attachments**—Select to crawl all attached
      objects, articles, and feeds.
   2. For **Standard objects**, **Knowledge articles**,
      and **Chatter feeds**—Select Salesforce entities or
      content types you want to crawl.

   ###### Note

   You must provide configuration information for indexing at least one of standard
   objects, knowledge articles, or chatter feeds. If you choose to crawl
   **Knowledge articles** you must specify the types of knowledge
   articles to index, the name of the articles, and whether to index the standard fields
   of all knowledge articles or only the fields of a custom article type. If you choose to
   index custom articles, you must specify the internal name of the article type. You can
   specify upto 10 article types. 3. **Frequency**—How often Amazon Kendra will sync with
   your data source. 4. Choose **Next**.

8. On the **Set field mappings** page, enter the following
   information:
   1. For **Standard knowledge article**, **Standard object
      attachments**, and **Additional suggested field mappings**
      —Select from the Amazon Kendra generated default data source fields you want
      to map to your index.

   ###### Note

   An index mapping to `_document_body` is required. You can't change the
   mapping between the `Salesforce ID` field and the Amazon Kendra
   `_document_id` field. 2. **Add field**—To add custom data source fields to create an
   index field name to map to and the field data type. 3. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to
Salesforce**

You must specify the following the [SalesforceConfiguration](../APIReference/API_SalesforceConfiguration.md "../APIReference/API_SalesforceConfiguration.md") API:

- **Server URL**—The instance URL for the
  Salesforce site that you want to index.
- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your Salesforce account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "authenticationUrl": "`OAUTH endpoint that Amazon Kendra connects to get an OAUTH token`",
    "consumerKey": "`Application public key generated when you created your Salesforce application`",
    "consumerSecret": "`Application private key generated when you created your Salesforce application.`",
    "password": "`Password associated with the user logging in to the Salesforce instance`",
    "securityToken": "`Token associated with the user account logging in to the Salesforce instance`",
    "username": "`User name of the user logging in to the Salesforce instance`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Salesforce connector and Amazon Kendra.
  For more information, see [IAM roles for Salesforce
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").
- You must provide configuration information for indexing at least one of standard
  objects, knowledge articles, or chatter feeds.
  - **Standard objects**—If you choose to crawl
    **Standard objects**, you must specify the name of the standard object
    and the name of the field in the standard object table that contains the document
    contents.
  - **Knowledge articles**—If you choose to crawl
    **Knowledge articles**, you must specify the types of knowledge
    articles to index, the states of the knowledge articles to index, and whether to index
    the standard fields of all knowledge articles or only the fields of a custom article
    type.
  - **Chatter feeds**—If you choose to crawl
    **Chatter feeds**, you must specify the name of the column in the
    Salesforce FeedItem table that contains the content to index.

You can also add the following optional features:

- **Inclusion and exclusion filters**—Specify whether to
  include or exclude certain file attachments.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Field mappings**—Choose to map your Salesforce
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

- **User context filtering and access control**—Amazon Kendra
  crawls the access control list (ACL) for your documents,
  if you have an ACL for your documents. The ACL
  information is used to filter search results based on the user or their
  group access to documents. For more information, see [User context
  filtering](user-context-filter.md#datasource-context-filter "user-context-filter.md#datasource-context-filter").
