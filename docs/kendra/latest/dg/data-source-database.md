# Amazon RDS/Aurora

You can index documents that are stored in a database using a database data source. After
you provided connection information for the database, Amazon Kendra connects and
indexes documents.

Amazon Kendra supports the following databases:

- Amazon Aurora MySQL
- Amazon Aurora PostgreSQL
- Amazon RDS for MySQL
- Amazon RDS for PostgreSQL

###### Note

Serverless Aurora databases are not supported.

###### Important

This Amazon RDS/Aurora connector is scheduled for deprecation by the end of 2023.

Amazon Kendra now supports new database data source connectors. For an improved
experience, we recommend you choose from the following new connectors for your use
case:

- [Aurora (MySQL)](data-source-aurora-mysql.md "data-source-aurora-mysql.md")
- [Aurora (PostgreSQL)](data-source-aurora-postgresql.md "data-source-aurora-postgresql.md")
- [Amazon RDS (MySQL)](data-source-rds-mysql.md "data-source-rds-mysql.md")
- [Amazon RDS (Microsoft SQL Server)](data-source-rds-ms-sql-server.md "data-source-rds-ms-sql-server.md")
- [Amazon RDS (Oracle)](data-source-rds-oracle.md "data-source-rds-oracle.md")
- [Amazon RDS (PostgreSQL)](data-source-rds-postgresql.md "data-source-rds-postgresql.md")
- [IBM DB2](data-source-ibm-db2.md "data-source-ibm-db2.md")
- [Microsoft SQL
  Server](data-source-ms-sql-server.md "data-source-ms-sql-server.md")
- [MySQL](data-source-mysql.md "data-source-mysql.md")
- [Oracle
  Database](data-source-oracle-database.md "data-source-oracle-database.md")
- [PostgreSQL](data-source-postgresql.md "data-source-postgresql.md")
  You can connect Amazon Kendra to your database data source using the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/") and the [DatabaseConfiguration](../APIReference/API_DatabaseConfiguration.md "../APIReference/API_DatabaseConfiguration.md") API.

For troubleshooting your Amazon Kendra database data source connector, see [Troubleshooting data sources](troubleshooting-data-sources.md "troubleshooting-data-sources.md").

###### Topics

- [Supported features](#supported-features-database "#supported-features-database")
- [Prerequisites](#prerequisites-database "#prerequisites-database")
- [Connection instructions](#data-source-procedure-database "#data-source-procedure-database")

## Supported features

Amazon Kendra database data source connector supports the following
features:

- Field mappings
- User context filtering
- Virtual private cloud (VPC)

## Prerequisites

Before you can use Amazon Kendra to index your database data source,
make these changes in your database and AWS accounts.

**In your database, make sure you
have:**

- Noted your basic authentication credentials of user name and password for your
  database.
- Copied the host name, port number, host address, the name of the database, and
  the name of the data table that contains the document data. For PostgreSQL, the
  data table must be a public table or public schema.

###### Note

The host and port tell Amazon Kendra where to find the database
server on the internet. The database name and table name tell Amazon Kendra where to find the document data on the database
server.

- Copied the names of the columns in the data table that contain the document
  data. You must include the document ID, document body, columns to detect if a
  document has changed (for example, last updated column), and optional data table
  columns that map to custom index fields. You can also map any of the [Amazon Kendra reserved field names](hiw-document-attributes.md#index-reserved-fields "hiw-document-attributes.md#index-reserved-fields") to a table
  column.
- Copied the database engine type information such as whether you use Amazon RDS for MySQL or another type.
- Checked each document is unique in database and across other
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

- Stored your database authentication credentials in an
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
connect your database data source to Amazon Kendra. If you are using the
API, you must provide the ARN of an existing IAM role and Secrets Manager secret, and an index ID.

## Connection instructions

To connect Amazon Kendra to your database data source, you must provide
the necessary details of your database data source so that Amazon Kendra can access
your data. If you have not yet configured database for Amazon Kendra,
see [Prerequisites](#prerequisites-database "#prerequisites-database").

Console
**To connect Amazon Kendra to a
database**

1. Sign in to the AWS Management Console and open the [Amazon Kendra console](https://console.aws.amazon.com/kendra/ "https://console.aws.amazon.com/kendra/").
2. From the left navigation pane, choose **Indexes** and then choose the index you want to use from the list of indexes.

###### Note

You can choose to configure or edit your **User access control** settings under **Index settings**. 3. On the **Getting started** page, choose **Add data source**. 4. On the **Add data source** page, choose **database connector**, and then choose **Add connector**.
If using version 2 (if applicable), choose **database connector** with the "V2.0" tag. 5. On the **Specify data source details** page, enter the following information:

    1. In **Name and description**, for **Data source name**—Enter a name for your data source. You can include hyphens but not spaces.
    2. (Optional) **Description**—Enter an optional description for your data source.
    3. In **Default language**—Choose a language to filter your documents for the index. Unless you specify otherwise,
     the language defaults to English. Language specified in the document metadata overrides the selected language.
    4. In **Tags**, for **Add new tag**—Include optional tags to search and filter your resources or track your AWS costs.
    5. Choose **Next**.

6. On the **Define access and security** page,
   enter the following information:
   1. **Endpoint**—A DNS host name,
      an IPv4 address, or an IPv6 address.
   2. **Port**—A port number.
   3. **Database**—Database
      name.
   4. **Table name**—Table
      name.
   5. For **Type of authentication**,
      choose between **Existing** and
      **New** to store your
      database authentication credentials. If you
      choose to create a new secret an AWS
      Secrets Manager secret window opens.
      1. Enter following information in the
         **Create an AWS
         Secrets Manager secret
         window**:
         1. **Secret name**—A
            name for your secret. The prefix
            ‘AmazonKendra-database-’ is
            automatically added to your secret name.
         2. For **User name** and
            **Password**—Enter the
            authentication credential values from your
            database account.
         3. Choose **Save
            authentication**.

   6. **Virtual Private Cloud (VPC)**—You can choose to use a VPC. If
      so, you must add **Subnets** and **VPC security groups**.

   ###### Note

   You must use a private subnet. If your RDS
   instance is in a public subnet in your VPC, you can
   create a private subnet that has outbound access to
   a NAT gateway in the public subnet. The subnets
   provided in the VPC configuration must be in either
   US West (Oregon), US East (N. Virginia), EU
   (Ireland). 7. **IAM role**—Choose an existing IAM
   role or create a new IAM role to access your repository credentials and index content.

   ###### Note

   IAM roles used for indexes cannot be used for data sources. If you are unsure
   if an existing role is used for an index or FAQ, choose **Create a new role** to avoid
   errors. 8. Choose **Next**.

7. On the **Configure sync settings** page,
   enter the following information:
   1. Select between **Aurora MySQL**,
      **MySQL**, **Aurora
      PostgreSQL**, and
      **PostgreSQL** based on your use
      case.
   2. **Enclose SQL identifiers with double
      quotes**—Select to enclose SQL
      identifiers in double quotes. For example,
      “columnName”.
   3. **ACL column** and **Change
      detecting columns**—Configure the
      columns that Amazon Kendra uses for change
      detection (for example, last updated column) and your
      access control list.
   4. In **Sync run schedule**, for
      **Frequency**—Choose how
      often Amazon Kendra will sync with your data
      source.
   5. Choose **Next**.

8. On the **Set field mappings** page, enter the
   following information:
   1. **Amazon Kendra default field
      mappings**—Select from the Amazon Kendra generated default data source fields you
      want to map to your index. You must add the
      **Database column** values for
      `document_id` and
      `document_body`
   2. **Custom field mappings**—To add
      custom data source fields to create an index field name
      to map to and the field data type.
   3. Choose **Next**.

9. On the **Review and create** page, check that
   the information you have entered is correct and then select
   **Add data source**. You can also choose to edit your information from this page.
   Your data source will appear on the **Data sources** page after the data source has been
   added successfully.

API
**To connect Amazon Kendra to a
database**

You must specify the following the [DatabaseConfiguration](../APIReference/API_DatabaseConfiguration.md "../APIReference/API_DatabaseConfiguration.md") API:

- **ColumnConfiguration**—Information about where
  the index should get the document information from the database.
  For more details, see [ColumnConfiguration](../APIReference/API_ColumnConfiguration.md "../APIReference/API_ColumnConfiguration.md"). You must specify the
  `DocumentDataColumnName` (document body or main
  text) and `DocumentIdColumnName`, and
  `ChangeDetectingColumn` (for example, last
  updated column) fields. The column mapped to the
  `DocumentIdColumnName` field must be an integer
  column. The following example shows a simple column
  configuration for a database data source:

```
"ColumnConfiguration": {
    "ChangeDetectingColumns": [
        "LastUpdateDate",
        "LastUpdateTime"
    ],
    "DocumentDataColumnName": "TextColumn",
    "DocumentIdColumnName": "IdentifierColumn",
    "DocoumentTitleColumnName": "TitleColumn",
    "FieldMappings": [
        {
            "DataSourceFieldName": "AbstractColumn",
            "IndexFieldName": "Abstract"
        }
    ]
}
```

- **ConnectionConfiguration**—Configuration
  information that's required to connect to a database. For more
  details, see [ConnectionConfiguration](../APIReference/API_ConnectionConfiguration.md "../APIReference/API_ConnectionConfiguration.md").
- **DatabaseEngineType**—The
  type of database engine that runs the database. The
  `DatabaseHost` field for
  `ConnectionConfiguration` must be the Amazon Relational Database Service (Amazon RDS) instance endpoint for
  the database. Don't use the cluster endpoint.
- **Secret Amazon Resource Name
  (ARN)**—Provide the Amazon Resource
  Name (ARN) of an Secrets Manager secret that contains the
  authentication credentials for your database account.
  The secret is stored in a JSON structure with the following keys:

```
{
    "username": `"user name"`,
    "password": `"password"`
}
```

The following example shows a database configuration,
including the secret ARN.

```

"DatabaseConfiguration": {
"ConnectionConfiguration": {
"DatabaseHost": "host.subdomain.domain.tld",
        "DatabaseName": "DocumentDatabase",
        "DatabasePort": 3306,
        "SecretArn": "arn:aws:secretmanager:region:account ID:secret/secret name",
        "TableName": "DocumentTable"
    }
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
  APIs for the database connector and Amazon Kendra.
  For more information, see [IAM roles for database
  data sources](iam-roles.md#iam-roles-ds "iam-roles.md#iam-roles-ds").

You can also add the following optional features:

- **Virtual Private Cloud
  (VPC)**—Specify `VpcConfiguration` as
  part of the data source configuration. See [Configuring
  Amazon Kendra to use a VPC](vpc-configuration.md "vpc-configuration.md").

###### Note

You must only use a private subnet. If your RDS instance
is in a public subnet in your VPC, you can create a private
subnet that has outbound access to a NAT gateway in the
public subnet. The subnets provided in the VPC configuration
must be in either US West (Oregon), US East (N. Virginia),
EU (Ireland).

- **Field mappings**—Choose to map your database
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
