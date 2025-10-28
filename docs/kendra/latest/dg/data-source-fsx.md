# Amazon FSx (Windows)

Amazon FSx (Windows) is a fully managed, cloud based file server system that offers shared
storage capabilities. If you're an Amazon FSx (Windows) user, you can use Amazon Kendra
to index your Amazon FSx (Windows) data source.

###### Note

Amazon Kendra now supports an upgraded Amazon FSx (Windows) connector.

The console has been automatically upgraded for you. Any new connectors you create on
the console will use the upgraded architecture. If you use the API, you must now use the
[TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object instead of the
`FSxConfiguration` object to configure your connector.

Connectors configured using the older console and API architecture will continue to
function as configured. However, you won’t be able to edit or update them. If you want
to edit or update your connector configuration, you must create a new connector.

We recommended migrating your connector workflow to the upgraded version. Support for
connectors configured using the older architecture is scheduled to end by June 2024.

You can connect Amazon Kendra to your Amazon FSx (Windows) data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/"), or the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API.

For troubleshooting your Amazon Kendra Amazon FSx (Windows) data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-fsx "#supported-features-fsx")
- [Prerequisites](#prerequisites-fsx "#prerequisites-fsx")
- [Connection instructions](#data-source-procedure-fsx "#data-source-procedure-fsx")
- [Learn more](#fsx-learn-more "#fsx-learn-more")

## Supported features

Amazon Kendra Amazon FSx (Windows) data source connector supports the following
features:

- Field mappings
- User access control
- User identity crawling
- Inclusion and exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Amazon FSx (Windows) data source,
check the details of your Amazon FSx (Windows) and AWS accounts.

**For Amazon FSx (Windows), make sure you have**:

- Set up Amazon FSx (Windows) with read and mounting permissions.
- Noted your file system ID. You can find your file system ID on the File
  Systems dashboard in the Amazon FSx (Windows) console.
- Configured a virtual private cloud using Amazon VPC where your
  Amazon FSx (Windows) file system resides.
- Noted your Amazon FSx (Windows) authentication credentials for an Active
  Directory user account. This includes your Active Directory user
  name with your DNS domain name (for example,
  *user@corp.example.com*) and password.

###### Note

Use only the necessary credentials required for the connector to function.
Do not use privileged credentials like domain admin.

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- Checked each document is unique in Amazon FSx (Windows) and across other
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

- Stored your Amazon FSx (Windows) authentication credentials in an
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
connect your Amazon FSx (Windows) data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Amazon FSx (Windows) data source, you must provide
the necessary details of your Amazon FSx (Windows) data source so that Amazon Kendra can access
your data. If you have not yet configured Amazon FSx (Windows) for Amazon Kendra,
see [Prerequisites](#prerequisites-fsx "#prerequisites-fsx").

Console
**To connect Amazon Kendra to your
Amazon FSx (Windows) file system**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Amazon FSx (Windows) connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Amazon FSx (Windows) connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page,
   enter the following information:
   1. **Amazon FSx (Windows) file system
      ID**—Select from the dropdown your
      existing file system ID, fetched from
      Amazon FSx (Windows). Or, create an [Amazon FSx (Windows) file
      system](https://console.aws.amazon.com/fsx/ "https://console.aws.amazon.com/fsx/"). You can find your file system ID
      on the File Systems dashboard in the Amazon FSx (Windows) console.
   2. **Authorization**—Turn on or off access control list (ACL) information for your
      documents, if you have an ACL and want to use it for access control. The ACL specifies which documents that users
      and groups can access. The ACL information is used to filter search results based on the user or
      their group access to documents. For more information, see [User context filtering](user-context-filter.md#context-filter-user-incl-datasources "user-context-filter.md#context-filter-user-incl-datasources").
   3. **Authentication**—Choose an
      existing AWS Secrets Manager secret, or create a new
      secret to store your file system credentials. If you
      choose to create a new secret, an AWS Secrets Manager
      secret window opens.

   Provide a secret that stores your authentication
   credentials of your user name and password. The user
   name must include your DNS domain name. For example,
   *user@corp.example.com*.

   Save and add your secret. 4. **Virtual Private Cloud
   (VPC)**—You must select an Amazon VPC where your Amazon FSx (Windows) resides.
   You include the VPC subnet and security groups. See
   [Configuring an Amazon VPC](vpc-configuration.md "vpc-configuration.md"). 5. **IAM role**—Choose an existing IAM
   role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 6. Choose **Next**.

7. On the **Configure sync settings** page,
   enter the following information:
   1. **Sync scope, Regex patterns**—Add regular
      expression patterns to include or exclude certain files.
   2. **Sync mode**—Choose how you want to update
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

   3. **Sync run schedule**—For
      **Frequency**, choose how often
      to sync your data source content and update your index.
   4. Choose **Next**.

8. On the **Set field mappings** page, enter the
   following information:
   1. Select from the Amazon Kendra generated default
      fields of your files that you want to map to your index.
      To add custom data source fields, create an index field
      name to map to and the field data type.
   2. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to your
Amazon FSx (Windows) file system**

You must specify a JSON of the [data source
schema](ds-schemas.md#ds-fsx-schema "ds-schemas.md#ds-fsx-schema") using the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API. You must
provide the following information:

- **Data
  source**—Specify the data source type as
  `FSX` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **File system ID**—The
  identifier of the Amazon FSx (Windows) file system. You can find
  your file system ID on the File Systems dashboard in the
  Amazon FSx (Windows) console.
- **File system
  type**—Specify the type of file system as
  `WINDOWS`.
- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").

###### Note

You must select an Amazon VPC
where your Amazon FSx (Windows) resides. You include the VPC
subnet and security groups.

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
- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your Amazon FSx (Windows) account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "username": "`user@corp.example.com`",
    "password": "`password`"
}
```

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Amazon FSx (Windows) connector and Amazon Kendra.
  For more information, see [IAM roles for Amazon FSx (Windows)
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Inclusion and exclusion
  filters**—Specify whether to include or
  exclude certain files.

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

###### Note

To test user context filtering on a user, you must include
the DNS domain name as part of the user name when you issue
the query. You must have administrative permissions of the
Active Directory domain. You can also test user context
filtering on a group name.

- **Field mappings**—Choose to map your Amazon FSx (Windows)
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [Amazon FSx (Windows) template schema](ds-schemas.md#ds-fsx-windows-schema "ds-schemas.md#ds-fsx-windows-schema").

## Learn more

To learn more about integrating Amazon Kendra with your Amazon FSx (Windows) data
source, see:

- [Securely search unstructured data on Windows file systems with the Amazon Kendra connector for Amazon FSx (Windows) for Windows File
  Server](https://aws.amazon.com/blogs/machine-learning/securely-search-unstructured-data-on-windows-file-systems-with-amazon-kendra-connector-for-amazon-fsx-for-windows-file-server/ "https://aws.amazon.com/blogs/machine-learning/securely-search-unstructured-data-on-windows-file-systems-with-amazon-kendra-connector-for-amazon-fsx-for-windows-file-server/").
