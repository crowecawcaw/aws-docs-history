# Salesforce connector V2.0

Salesforce is a customer relationship management (CRM) tool for managing support,
sales, and marketing teams. You can use Amazon Kendra to index your Salesforce
standard objects and even custom objects.

The Amazon Kendra Salesforce data source connector supports the following
Salesforce editions: Developer Edition and Enterprise Edition.

###### Note

Salesforce connector V1.0 / SalesforceConfiguration API ended in 2023. We recommend
migrating to or using Salesforce connector V2.0 / TemplateConfiguration API.

For troubleshooting your Amazon Kendra Salesforce data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-v2-salesforce "#supported-features-v2-salesforce")
- [Prerequisites](#prerequisites-v2-salesforce "#prerequisites-v2-salesforce")
- [Connection instructions](#data-source-procedure-v2-salesforce "#data-source-procedure-v2-salesforce")
- [Learn more](#salesforce-v2-learn-more "#salesforce-v2-learn-more")
- [Notes](#salesforce-notes "#salesforce-notes")

## Supported features

Amazon Kendra Salesforce data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Salesforce data source, make
these changes in your Salesforce and AWS accounts.

**In Salesforce, make sure you have:**

- Created a Salesforce administrative account and have noted the user name and
  password you use to connect to Salesforce.
- Copied the Salesforce security token associated with the account used to connect
  to Salesforce.
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

- Copied the URL of the Salesforce instance that you want to index. Typically, this
  is `https://<company>.salesforce.com/`. The server must be
  running a Salesforce connected app.
- Added credentials to your Salesforce server for a user with read-only access to
  Salesforce by cloning the ReadOnly profile and then adding the View All Data and
  Manage Articles permissions. These credentials identify the user making the connection and the
  Salesforce connected app that Amazon Kendra connects to.
- Checked each document is unique in Salesforce and across other data sources you
  plan to use for the same index. Each data source that you want to use for an index must not
  contain the same document across the data sources. Document IDs are global to an index and
  must be unique per index.

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
your data. If you have not yet configured Salesforce for Amazon Kendra see [Prerequisites](#prerequisites-v2-salesforce "#prerequisites-v2-salesforce").

Console
**To connect Amazon Kendra to
Salesforce**:

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Salesforce connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Salesforce connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6.  On the **Define access and security** page, enter the following
    information:
    1. **Salesforce URL**—Enter The instance URL for the
       Salesforce site that you want to index.
    2. **Authorization**—Turn on or off access control list (ACL) information for your
       documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
       and groups can access. The ACL information is used to filter search results based on the user or
       their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
    3. Enter an existing secret or if you create a new secret, an AWS
       Secrets Manager secret window opens.
       1. **Authentication**—Enter following information in the
          **Create an AWS
          Secrets Manager secret window**:
          1. **Secret name**—A name for your secret. The prefix
             ‘AmazonKendra-Salesforce-’ is automatically added to your secret
             name.
          2. For **User name**, **Password**,
             **Security token**, **Consumer key**,
             **Consumer secret**, and **Authentication
             URL**—Enter the authentication credential values you generated and
             downloaded from your Salesforce account.

          ###### Note

          If you use Salesforce Developer Edition, use
          `https://login.salesforce.com/services/oauth2/token` or the My Domain
          login URL (for example, `https://MyCompany.my.salesforce.com`) as the **Authentication
          URL**. If you use Salesforce Sandbox Edition, use
          `https://test.salesforce.com/services/oauth2/token` or the My Domain
          login URL (for example, `MyDomainName--SandboxName.sandbox.my.salesforce.com`) as the
          **Authentication URL**. 3. Choose **Save authentication**.

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

7.  On the **Configure sync settings** page, enter the following
    information:
    1. For **Crawl attachments**—Select to crawl all attached
       Salesforce objects.
    2. For **Standard objects**, **Standard objects with
       attachments**, and **Standard object without attachment** and
       **Knowledge Articles**—Select Salesforce entities or
       content types you want to crawl.
    3. You must provide configuration information for indexing at least one of standard
       objects, knowledge articles, or chatter feeds. If you choose to crawl
       **Knowledge articles** you must specify the types of knowledge
       articles to index. You can choose published, archived, drafts and attachments.

    **Regex filter**—Specify a regex pattern to include
    specific catalog items.

8.  For **Additional configuration**:

        * **ACL information** All access control lists are included by
         default. Deselecting an access control list will make all files in that category
         public.
        * **Regex patterns**—Add regular expression patterns to
         include or exclude certain files. You can add up to 100 patterns.

    **Sync mode**—Choose how you want to update your index when
    your data source content changes. When you sync your data source with Amazon Kendra
    for the first time, all content is crawled and indexed by default. You must run a full
    sync of your data if your initial sync failed, even if you don't choose full sync as your
    sync mode option.

        * Full sync: Freshly index all content, replacing existing content each time your
         data source syncs with your index.
        * New, modified sync: Index only new and modified content each time your data source
         syncs with your index. Amazon Kendra can use your data source's mechanism for
         tracking content changes and index content that changed since the last sync.
        * New, modified, deleted sync: Index only new, modified, and deleted content each
         time your data source syncs with your index. Amazon Kendra can use your data
         source's mechanism for tracking content changes and index content that changed since the
         last sync.

9.  Choose **Next**.
10. On the **Set field mappings** page, enter the following
    information:
    1. For **Standard knowledge article**, **Standard object
       attachments**, and **Additional suggested field mappings**
       —Select from the Amazon Kendra generated default data source fields you want
       to map to your index.

    ###### Note

    An index mapping to `_document_body` is required. You can't change the
    mapping between the `Salesforce ID` field and the Amazon Kendra
    `_document_id` field. You can map any Salesforce field to the document title
    or document body Amazon Kendra reserved/default index fields.

    If you map any Salesforce field to Amazon Kendra document title and document body fields,
    Amazon Kendra will use data from the document title and body fields in search responses. 2. **Add field**—To add custom data source fields to create an
    index field name to map to and the field data type. 3. Choose **Next**.

11. On the **Review and create** page, check that
    the information you have entered is correct and then select
    **Add data source**. You can also choose to edit your information from this page.
    Your data source will appear on the **Data sources** page after the data source has been
    added successfully.

API
**To connect Amazon Kendra to
Salesforce**

You must specify a JSON of the [data source schema](ds-schemas.md "ds-schemas.md") using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API. You must provide the following information:

- **Data source**—Specify the data source type as
  `SALESFORCEV2` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON schema. Also specify the data source
  as `TEMPLATE` when you call the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md")
  API.
- **Host URL**—Specify the Salesforce instance host
  URL.
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
  - `CHANGE_LOG` to index only new and modified content each time your data
    source syncs with your index. Amazon Kendra can use your data source’s mechanism
    for tracking content changes and index content that changed since the last sync.

- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your Salesforce account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "authenticationUrl": "`OAUTH endpoint that Amazon Kendra connects to get an OAUTH token`",
    "consumerKey": "`Application public key generated when you created your Salesforce application`",
    "consumerSecret": "`Application private key generated when you created your Salesforce application`",
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

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Inclusion and exclusion filters**—You can
  specify whether to include or exclude certain documents, accounts, campaigns, cases,
  contacts, leads, opportunities, solutions, tasks, groups, chatters, and custom entity
  files.

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

###### Note

An index mapping to `_document_body` is required. You can't change the
mapping between the `Salesforce ID` field and the Amazon Kendra
`_document_id` field. You can map any Salesforce field to the document title
or document body Amazon Kendra reserved/default index fields.

If you map any Salesforce field to Amazon Kendra document title and document body fields,
Amazon Kendra will use data from the document title and body fields in search responses.

For a list of other important JSON keys to configure, see [Salesforce template
schema](ds-schemas.md#ds-salesforce-schema "ds-schemas.md#ds-salesforce-schema").

## Learn more

To learn more about integrating Amazon Kendra with your Salesforce data
source, see:

- [Announcing the updated Salesforce connector (V2) for Amazon Kendra](https://aws.amazon.com/blogs/machine-learning/announcing-the-updated-salesforce-connector-v2-for-amazon-kendra/ "https://aws.amazon.com/blogs/machine-learning/announcing-the-updated-salesforce-connector-v2-for-amazon-kendra/")

## Notes

- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to Salesforce API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.
