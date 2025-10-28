# Box

Box is a cloud storage service that offers file hosting capabilities. You
can use Amazon Kendra to index content in your Box content, including
comments, tasks, and web links.

You can connect Amazon Kendra to your Box data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") and the [BoxConfiguration](../APIReference/API_BoxConfiguration.md "../APIReference/API_BoxConfiguration.md") API.

For troubleshooting your Amazon Kendra Box data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-box "#supported-features-box")
- [Prerequisites](#prerequisites-box "#prerequisites-box")
- [Connection instructions](#data-source-procedure-box "#data-source-procedure-box")
- [Learn more](#box-learn-more "#box-learn-more")
- [Notes](#box-notes "#box-notes")

## Supported features

Amazon Kendra Box data source connector supports the following
features:

- Field mappings
- User access control
- Inclusion/exclusion filters
- Change log, full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Box data source,
make these changes in your Box and AWS accounts.

**In Box, make sure you have:**

- A Box Enterprise or Box Enterprise Plus
  account.
- Configured a Box custom app in the Box Developer
  Console, with Server-side authentication using JSON Web Tokens (JWT). See [Box documentation on creating a Custom App](https://developer.box.com/guides/applications/app-types/platform-apps/ "https://developer.box.com/guides/applications/app-types/platform-apps/") and [Box documentation
  of configuring JWT Auth](https://developer.box.com/guides/authentication/jwt/ "https://developer.box.com/guides/authentication/jwt/") for more details.
- Set your **App Access Level** to **App + Enterprise
  Access** and allowed it to **Make API calls using the
  as-user header**.
- Used the admin user to add the following **Application
  Scopes** in your Box app:
  - Write all files and folders stored in a Box
  - Manage users
  - Manage groups
  - Manage enterprise properties

- Configured Public/Private key pair including a client ID, a client secret, a
  public key ID, private key ID, a pass phrase, and an enterprise ID to use as
  your authentication credentials. See [Public and private key pair](https://developer.box.com/guides/authentication/jwt/jwt-setup/#public-and-private-key-pair "https://developer.box.com/guides/authentication/jwt/jwt-setup/#public-and-private-key-pair") for more details.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- Copied your Box enterprise ID either from your
  Box Developer Console settings or from your Box
  app. For example, `801234567`.
- Checked each document is unique in Box and across other
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

- Stored your Box authentication credentials in an
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
connect your Box data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Box data source, you must provide
the necessary details of your Box data source so that Amazon Kendra can access
your data. If you have not yet configured Box for Amazon Kendra,
see [Prerequisites](#prerequisites-box "#prerequisites-box").

Console
**To connect Amazon Kendra to
Box**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Box connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Box connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page,
   enter the following information:
   1. **Box enterprise
      ID**—Enter your Box
      Enterprise ID. For example,
      `801234567`.
   2. **Authorization**—Turn on or off access control list (ACL) information for your
      documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
      and groups can access. The ACL information is used to filter search results based on the user or
      their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
   3. **AWS Secrets Manager secret**—Choose an existing secret or create a new
      Secrets Manager secret to store your Box authentication
      credentials. If you choose to create a new secret an AWS Secrets Manager
      secret window opens.
      1. **Secret name**—A name
         for your secret. The prefix
         ‘AmazonKendra-Box-’ is
         automatically added to your secret name.
      2. For **Client ID**,
         **Client Secret**,
         **Public Key ID**,
         **Private Key ID**, and
         **Pass Phrase**—Enter the
         values from the Public/Private Key you configured
         in Box.
      3. Add and save your secret.

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
   1. **Box files**—Choose whether
      to crawl web links, comments, and tasks.
   2. For **Additional
      configuration**—Add regular expression
      patterns to include or exclude certain content.
   3. **Sync mode**—Choose how you
      want to update your index when your data source content
      changes. When you sync your data source with Amazon Kendra for the first time, all content is
      crawled and indexed by default. You must run a full sync
      of your data if your initial sync failed, even if you
      don't choose full sync as your sync mode option.
      - Full sync: Freshly index all content,
        replacing existing content each time your data
        source syncs with your index.
      - New, modified sync: Index only new and
        modified content each time your data source syncs
        with your index. Amazon Kendra can use your
        data source's mechanism for tracking content
        changes and index content that changed since the
        last sync.
      - New, modified, deleted sync: Index only new,
        modified, and deleted content each time your data
        source syncs with your index. Amazon Kendra
        can use your data source's mechanism for tracking
        content changes and index content that changed
        since the last sync.

   4. In **Sync run schedule** for
      **Frequency**—Choose how
      often to sync your data source content and update your
      index.
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
Box**

You must specify the following using the [BoxConfiguration](../APIReference/API_BoxConfiguration.md "../APIReference/API_BoxConfiguration.md") API:

**Box enterprise
ID**—Provide your Box Enterprise ID.
You can find the enterprise ID in the Box Developer
Console settings or when you configure an app in
Box.

- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your Box account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "clientID": "`client-id`",
    "clientSecret": "`client-secret`",
    "publicKeyID": "`public-key-id`",
    "privateKey": "`private-key`",
    "passphrase": "`pass-phrase`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Box connector and Amazon Kendra.
  For more information, see [IAM roles for Box
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify `VpcConfiguration` as
  part of the data source configuration. See [Configuring
  Amazon Kendra to use a VPC](vpc-configuration.md "vpc-configuration.md").
- **Change log**—Whether
  Amazon Kendra should use the Box data
  source change log mechanism to determine if a document must be
  updated in the index.

###### Note

Use the change log if you don’t want Amazon Kendra
to scan all of the documents. If your change log is large,
it might take Amazon Kendra less time to scan the
documents in the Box data source than to
process the change log. If you are syncing your Box
data source with your index for the first time, all documents are scanned.

- **Comments, tasks, web
  links**—Specify whether to crawl these types of
  content.

###### Note

Most data sources use regular expression patterns,
which are inclusion or exclusion patterns referred to as filters.
If you specify an inclusion filter, only content that
matches the inclusion filter is indexed. Any document that
doesn’t match the inclusion filter isn’t indexed. If you
specify an inclusion and exclusion filter, documents that
match the exclusion filter are not indexed, even if they
match the inclusion filter.

- **Inclusion and exclusion
  filters**—Specify whether to include or exclude
  certain Box files and folders.

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
- **Field mappings**—Choose to map your Box
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

## Learn more

To learn more about integrating Amazon Kendra with your Box data
source, see:

- [Getting started with the Amazon Kendra Box connector](https://aws.amazon.com/blogs/machine-learning/getting-started-with-the-amazon-kendra-box-connector/ "https://aws.amazon.com/blogs/machine-learning/getting-started-with-the-amazon-kendra-box-connector/")

## Notes

- When Access Control Lists (ACLs) are enabled, the "Sync only new or modified content" option is not available due to Box API limitations. We recommend using "Full sync" or "New, modified, or deleted content sync" modes instead, or disable ACLs if you need to use this sync mode.
