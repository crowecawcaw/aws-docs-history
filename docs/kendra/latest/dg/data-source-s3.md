# Amazon S3

Amazon S3 is an object storage service that stores data as objects within buckets.
You can use Amazon Kendra to index your Amazon S3 bucket repository of
documents.

###### Warning

Amazon Kendra doesn't use a bucket policy that grants permissions to an Amazon Kendra principal to interact with an S3 bucket. Instead, it uses IAM roles. Make sure that Amazon Kendra isn't included as a trusted
member in your bucket policy to avoid any data security issues in accidentally granting
permissions to arbitrary principals. However, you can add a bucket policy to use an
Amazon S3 bucket across different accounts. For more information, see [Policies to use
Amazon S3 across accounts](iam-roles.md#iam-roles-ds-s3-cross-accounts "iam-roles.md#iam-roles-ds-s3-cross-accounts") (within the S3 IAM
roles tab, under **IAM roles for data sources**). For
information about IAM roles for S3 data sources, see [IAM roles](iam-roles.md#iam-roles-ds-s3 "iam-roles.md#iam-roles-ds-s3").

###### Note

Amazon Kendra now supports an upgraded Amazon S3 connector.

The console has been automatically upgraded for you. Any new connectors you create in
the console will use the upgraded architecture. If you use the API, you must now use the
[TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") object instead of the
`S3DataSourceConfiguration` object to configure your
connector.

Connectors configured using the older console and API architecture will continue to
function as configured. However, you won’t be able to edit or update them. If you want
to edit or update your connector configuration, you must create a new connector.

We recommended migrating your connector workflow to the upgraded version. Support for
connectors configured using the older architecture is scheduled to end by June 2024.

You can connect to your Amazon S3 data source using the the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") or the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API.

###### Note

To generate a sync status report for your Amazon S3 data source, see [Troubleshooting data sources](troubleshooting-data-sources.md#troubleshooting-data-sources-sync-status-manifest "troubleshooting-data-sources.md#troubleshooting-data-sources-sync-status-manifest").

For troubleshooting your Amazon Kendra S3 data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-s3 "#supported-features-s3")
- [Prerequisites](#prerequisites-s3 "#prerequisites-s3")
- [Connection instructions](#data-source-procedure-s3 "#data-source-procedure-s3")
- [Creating an Amazon S3 data source](create-ds-s3.md "create-ds-s3.md")
- [Amazon S3 document metadata](s3-metadata.md "s3-metadata.md")
- [Access control for Amazon S3 data sources](s3-acl.md "s3-acl.md")
- [Using Amazon VPC with an Amazon S3
  data source](s3-vpc-example-1.md "s3-vpc-example-1.md")

## Supported features

- Field mappings
- User access control
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your S3 data source,
make these changes in your S3 and AWS accounts.

**In S3, make sure you have:**

- Copied the name of your Amazon S3 bucket.

###### Note

Your bucket must be in the same region as your Amazon Kendra index
and your index must have permission to access the bucket that contains your
documents.

- Checked each document is unique in S3 and across other
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

If you don’t have an existing IAM role, you can use the console to
create a new IAM role when you connect your S3 data
source to Amazon Kendra. If you are using the API, you must provide the ARN of an
existing IAM role and an index ID.

## Connection instructions

To connect Amazon Kendra to your S3 data source, you must provide
the necessary details of your S3 data source so that Amazon Kendra can access
your data. If you have not yet configured S3 for Amazon Kendra,
see [Prerequisites](#prerequisites-s3 "#prerequisites-s3").

Console
**To connect Amazon Kendra to Amazon S3**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **S3 connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **S3 connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page,
   enter the following optional information:
   1. **IAM role**—Choose an existing IAM
      role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 2. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
   so, you must add **Subnets** and **VPC security groups**. 3. Choose **Next**.

7. On the **Configure sync settings** page,
   enter the following information:
   1. For **Data
      source location**—Specify the path to the
      Amazon S3 bucket where your data is stored.
      Select **Browse S3** to choose your
      S3 bucket.
   2. For **Maximum file size**—Specify
      a limit in MB to only crawl files under this limit. The
      maximum file size Amazon Kendra can allow is 50 MB.
   3. For (Optional) **Metadata files prefix folder
      location**—Specify the path to the folder in
      which your fields/attributes and other document metadata is
      stored. Select **Browse S3** to locate your
      metadata folder.
   4. For (Optional) **Access control list configuration
      file location**—Specify the path to the
      file that contains a JSON structure of your users and their
      access to documents. Select **Browse S3** to
      locate your ACL file.
   5. (Optional) **Select decryption
      key**—Select to use a decryption key.
      You can choose to use an existing AWS KMS
      key.
   6. For (Optional) **Additional
      configuration**—Add patterns to
      include or exclude certain files. All paths
      are relative to the data source location S3 bucket.
   7. **Sync mode**—Choose how you want to update
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

   8. In **Sync run schedule**, for
      **Frequency**—Choose how often to sync
      your data source content and update your index.
   9. Choose **Next**.

8. On the **Set field mappings** page, enter the
   following optional information:
   1. **Default field mappings**—Select
      from the Amazon Kendra generated default data
      source fields you want to map to your index.
   2. **Add field**—Choose to add
      custom data source fields to create an index field name
      to map to and the field data type.
   3. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to Amazon S3**

You must specify a JSON of the [data source schema](ds-schemas.md "ds-schemas.md")
using the [TemplateConfiguration](../APIReference/API_TemplateConfiguration.md "../APIReference/API_TemplateConfiguration.md") API. You must provide the following
information:

- **Data
  source**—Specify the data source type as
  `S3` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **BucketName**—The name of
  the bucket that contains the documents.
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

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the S3 connector and Amazon Kendra.
  For more information, see [IAM roles for S3
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Inclusion and exclusion
  filters**—Specify whether to include or exclude
  certain file names, file types, file paths. You use glob
  patterns (patterns that can expand a wildcard pattern into a
  list of path names that match the given pattern). For examples, see [Use of Exclude and
  Include Filters](../../../cli/latest/reference/s3.md#use-of-exclude-and-include-filters "../../../cli/latest/reference/s3.md#use-of-exclude-and-include-filters") in the AWS CLI Command Reference.
- **Document metadata
  and access control configuration**—Add
  document metadata and access control files that contain information
  such as the source URI, document author, or custom document
  attributes/fields, and your users and which documents they can access.
  Each metadata file contains metadata about a single document.
- **Field mappings**—Choose to map your S3
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [S3 template
schema](ds-schemas.md#ds-s3-schema "ds-schemas.md#ds-s3-schema").

### Learn more

To learn more about integrating Amazon Kendra with your S3
data source, see:

- [Search for answers accurately using Amazon Kendra S3 Connector
  with VPC support](https://aws.amazon.com/blogs/machine-learning/search-for-answers-accurately-using-amazon-kendra-s3-connector-with-vpc-support/ "https://aws.amazon.com/blogs/machine-learning/search-for-answers-accurately-using-amazon-kendra-s3-connector-with-vpc-support/")
