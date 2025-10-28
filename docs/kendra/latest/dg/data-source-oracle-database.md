# Oracle Database

###### Note

Oracle Database connector remains fully supported for existing customers through May 31, 2026. While this connector is no longer available for new users, current users can continue to use it without interruption. We are continuously evolving our connector portfolio to offer more scalable and customizable solutions. For future integrations, we recommend exploring the Amazon Kendra Custom Connector Framework[1], designed to support a broader range of enterprise use cases with enhanced flexibility.

Oracle Database is a database management system. If you are a Oracle Database user,
you can use Amazon Kendra to index your Oracle Database data source. The Amazon Kendra Oracle Database data source connector supports Oracle Database 18c, 19c,
and 21c.

You can connect Amazon Kendra to your Oracle Database data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") and the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API.

For troubleshooting your Amazon Kendra Oracle Database data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-oracle-database "#supported-features-oracle-database")
- [Prerequisites](#prerequisites-oracle-database "#prerequisites-oracle-database")
- [Connection instructions](#data-source-procedure-oracle-database "#data-source-procedure-oracle-database")
- [Notes](#oracle-database-notes "#oracle-database-notes")

## Supported features

- Field mappings
- User context filtering
- Inclusion/exclusion filters
- Full and incremental content syncs
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your Oracle Database data source,
make these changes in your Oracle Database and AWS accounts.

**In Oracle Database, make sure you have:**

- Noted your database user name and password.

###### Important

As a best practice, provide Amazon Kendra with read-only database
credentials.

- Copied your database host url, port, and instance.
- Checked each document is unique in Oracle Database and across other
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

- Stored your Oracle Database authentication credentials in an
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
connect your Oracle Database data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your Oracle Database data source you must provide
details of your Oracle Database credentials so that Amazon Kendra can access
your data. If you have not yet configured Oracle Database for Amazon Kendra see
[Prerequisites](#prerequisites-oracle-database "#prerequisites-oracle-database").

Console
**To connect Amazon Kendra to
Oracle Database**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **Oracle Database connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **Oracle Database connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page,
   enter the following information:
   1. In **Source**, enter the following
      information:
   2. **Host**— Enter the database
      host name.
   3. **Port**— Enter the database
      port.
   4. **Instance**— Enter the database
      instance.
   5. **Enable SSL certificate
      location**—Choose to enter the Amazon S3 path to your SSL certificate file.
   6. In **Authentication**—enter
      the following information:
      1. **AWS Secrets Manager secret**—Choose an existing secret or create a new
         Secrets Manager secret to store your Oracle Database authentication
         credentials. If you choose to create a new secret an AWS Secrets Manager
         secret window opens.
         1. Enter following information in the
            **Create an AWS
            Secrets Manager secret
            window**:
            1. **Secret name**—A
               name for your secret. The prefix
               ‘AmazonKendra-Oracle Database-’ is
               automatically added to your secret name.
            2. For **Database user name**,
               and **Password**—Enter the
               authentication credential values you copied from
               your database.

         2. Choose **Save**.

   7. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
      so, you must add **Subnets** and **VPC security groups**.
   8. **IAM role**—Choose an existing IAM
      role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 9. Choose **Next**.

7. On the **Configure sync settings** page,
   enter the following information:
   1. In **Sync scope**, choose from the
      following options :
      - **SQL query**—Enter
        SQL query statements like SELECT and JOIN
        operations. SQL queries must be less than 32KB.
        Amazon Kendra will crawl all database content
        that matches your query.
      - **Primary key
        column**—Provide the primary key
        for the database table. This identifies a table
        within your database.
      - **Title
        column**—Provide the name of the
        document title column within your database
        table.
      - **Body
        column**—Provide the name of the
        document body column within your database
        table.

   2. In **Additional configuration –
      _optional_**, choose
      from the following options to sync specific content
      instead of syncing all files:
      - **Change-detecting
        columns**—Enter the names of the
        columns that Amazon Kendra will use to detect
        content changes. Amazon Kendra will re-index
        content when there is a change in any of these
        columns.
      - **User IDs
        column**—Enter the name of the
        column which contains User IDs to be allowed
        access to content.
      - **Groups
        column**—Enter the name of the
        column that contains groups to be allowed access
        to content.
      - **Source URLs
        column**—Enter the name of the
        column which contains Source URLs to be
        indexed.
      - **Time stamps
        column**—Enter the name of the
        column which contains time stamps. Amazon Kendra uses time stamp information to detect
        changes in your content and sync only changed
        content.
      - **Time zones
        column**—Enter the name of the
        column which contains time zones for the content
        to be crawled.
      - **Time stamps
        format**—Enter the name of the
        column which contains time stamp formats to use to
        detect content changes and re-sync your
        content.

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
      **Frequency**—How often
      Amazon Kendra will sync with your data
      source.
   5. Choose **Next**.

8. On the **Set field mappings** page, enter the
   following information:
   1. Select from the generated default data source
      fields—**Document IDs**,
      **Document titles**, and
      **Source URLs**—you want to
      map to Amazon Kendra index.
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
Oracle Database**

You must specify the following using the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") API:

- **Data
  source**—Specify the data source type as
  `JDBC` when you use the [TemplateConfiguration](API_TemplateConfiguration.md "API_TemplateConfiguration.md") JSON
  schema. Also specify the data source as
  `TEMPLATE` when you call
  the [CreateDataSource](API_CreateDataSource.md "API_CreateDataSource.md") API.
- **Database type**—You must
  specify the database type as `oracle`.
- **SQL query**—Specify
  SQL query statements like SELECT and JOIN
  operations. SQL queries must be less than 32KB.
  Amazon Kendra will crawl all database content
  that matches your query.
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
  (ARN) of an Secrets Manager secret that contains the
  authentication credentials you created in your
  Oracle Database account.
  The secret is stored in a JSON
  structure with the following keys:

```
{
    "user name": `"database user name"`,
    "password": `"password"`
}
```

###### Note

We recommend that you regularly refresh or rotate your credentials
and secret. Provide only the necessary access level for your own security.
We do **not** recommend that you re-use
credentials and secrets across data sources, and connector versions 1.0 and
2.0 (where applicable).

- **IAM role**—Specify `RoleArn`
  when you call `CreateDataSource` to provide an IAM role with permissions to access
  your Secrets Manager secret and to call the required public
  APIs for the Oracle Database connector and Amazon Kendra.
  For more information, see [IAM roles for Oracle Database
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify
  `VpcConfiguration` when you call `CreateDataSource`.
  For more information, see [Configuring Amazon Kendra to use an Amazon VPC](vpc-configuration.md "vpc-configuration.md").
- **Inclusion and exclusion
  filters**—You can specify whether to include
  specific content using user IDs, groups, source URLs, time
  stamps, and time zones.
- **User context filtering and access control**—Amazon Kendra
  crawls the access control list (ACL) for your documents,
  if you have an ACL for your documents. The ACL
  information is used to filter search results based on the user or their
  group access to documents. For more information, see [User context
  filtering](user-context-filter.md#datasource-context-filter "user-context-filter.md#datasource-context-filter").
- **Field mappings**—Choose to map your Oracle Database
  data source fields to your
  Amazon Kendra index fields. For more information, see
  [Mapping data
  source fields](field-mapping.md "field-mapping.md").

###### Note

The document body field or the document body equivalent for your documents is required
in order for Amazon Kendra to search your documents. You must map your document body
field name in your data source to the index field name `_document_body`. All other
fields are optional.

For a list of other important JSON keys to configure, see [Oracle Database template schema](ds-schemas.md#ds-oracle-database-schema "ds-schemas.md#ds-oracle-database-schema").

## Notes

- Deleted database rows will not be tracked in when Amazon Kendra checks
  for updated content.
- The size of field names and values in a row of your database can't exceed
  400KB.
- If you have a large amount of data in your database data source, and do not
  want Amazon Kendra to index all your database content after the first sync,
  you can choose to sync only new, modified, or deleted documents.
- As a best practice, provide Amazon Kendra with read-only database
  credentials.
- As a best practice, avoid adding tables with sensitive data or personal
  identifiable information (PII).
