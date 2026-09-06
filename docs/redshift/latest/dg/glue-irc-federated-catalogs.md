Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026.
We will start enforcing it in phases. For more information on the details of Python end of life
and migration options, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") that was published on June 30, 2025.

# Querying AWS Glue IRC federated catalogs with Amazon Redshift

With AWS Glue Iceberg REST Catalog (IRC), you can federate external data catalogs, such as
Databricks Unity Catalog, into the AWS Glue Data Catalog. After the catalog is federated, Amazon Redshift can query these external
tables directly without requiring data movement. This chapter describes how to access
Databricks Unity Catalog tables using federation from Amazon Redshift.

## Architecture overview

The architecture involves three components that may reside in different accounts and Regions:

- **Source data (Amazon S3 bucket)** – The Amazon S3 bucket
  managed by the external data platform (for example, Databricks). This is where the actual
  Iceberg table data files reside. To read Delta tables, make sure Iceberg metadata is available
  for these tables using UniForm.
- **AWS Glue IRC federated catalog** – The Data Catalog entry
  that federates the external catalog (for example, Databricks Unity Catalog) and exposes its
  metadata through the Iceberg REST protocol.
- **Amazon Redshift compute** – The provisioned cluster or
  serverless workgroup that executes queries against the federated tables.

You can access federated catalogs from Amazon Redshift in the following ways:

- **Automount** – Amazon Redshift automatically mounts the
  `awsdatacatalog` database, which provides access to all databases registered in the
  Data Catalog for the same account and Region. No schema creation is required. Queries use three-part
  notation: `"awsdatacatalog"."`database_name`"."`table_name`"`.
- **External schema** – You explicitly create an
  external schema using `CREATE EXTERNAL SCHEMA` that points to a resource link
  database in the Data Catalog, specifying a static IAM role or `SESSION` for federated
  identity authorization.

###### Important

External schema works only when all resources (catalog, compute, and Amazon S3 bucket) are in the same Region.

## Setting up and querying a federated catalog in the same account

### Setting up catalog federation

Follow the instructions in
[Federate to Databricks Unity Catalog](../../../lake-formation/latest/dg/catalog-federation-databricks.md "../../../lake-formation/latest/dg/catalog-federation-databricks.md")
in the _AWS Lake Formation Developer Guide_.

### Creating a resource link in the Data Catalog

Log in as the data lake admin. Create a database resource link in the Data Catalog pointing to
the federated database.

### Granting permissions for accessing tables in Amazon Redshift

As the data lake admin, grant the following permissions to the IAM principal or IAM role
used for creating the external schema:

- DESCRIBE access on the database resource link
- DESCRIBE access on the federated database
- SELECT and DESCRIBE on the federated table(s)

### Querying the federated table from Amazon Redshift

Connect to your Amazon Redshift cluster or workgroup as an admin user and access the table using one
of the following options.

Option 1: Create an external schema using an IAM role

Create an IAM role with permission to AWS Glue and AWS Lake Formation APIs and attach
the role to the cluster.

```
CREATE EXTERNAL SCHEMA `external_schema_name`
FROM DATA CATALOG DATABASE '`resource_link_database`'
IAM_ROLE 'arn:aws:iam::`account_id`:role/`spectrum_role`';
```

You can grant permissions on this external schema to Amazon Redshift local users and groups.
Local Amazon Redshift identities can access the data by querying the schema using permissions
granted to the IAM role attached to the external schema.

```
SELECT * FROM "`database`"."`external_schema_name`"."`table_name`" LIMIT 10;
```

Option 2: Create an external schema using IAM SESSION for a federated principal

```
CREATE EXTERNAL SCHEMA `external_schema_name`
FROM DATA CATALOG DATABASE '`resource_link_database`'
IAM_ROLE 'SESSION' CATALOG_ID '`account_id`';
```

Log in as a federated user or with an IAM identity and run the following command
to query the table:

```
SELECT * FROM "`database`"."`external_schema_name`"."`table_name`" LIMIT 10;
```

Option 3: Use automount to query a federated table

The admin user should grant usage on the automounted database to federated
principals. The principal can then access the federated table by running the following
command:

```
SELECT * FROM "awsdatacatalog"."`resource_link_database`"."`table_name`" LIMIT 10;
```

## Setting up and querying a federated catalog across accounts

You can share the federated catalog across accounts using AWS Lake Formation and access the shared
table from a different account using Amazon Redshift.

### Grantor account (where the federated catalog resides)

#### Setting up catalog federation

Follow the instructions in
[Federate to Databricks Unity Catalog](../../../lake-formation/latest/dg/catalog-federation-databricks.md "../../../lake-formation/latest/dg/catalog-federation-databricks.md")
in the _AWS Lake Formation Developer Guide_.

#### Setting the cross-account version

Set the cross-account version to V4 in AWS Lake Formation settings. If catalog-level permissions
already exist, make sure AWS RAM has permission to share resources by adding the following Data Catalog
resource policy:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "glue:ShareResource"
      ],
      "Principal": {
        "Service": [
          "ram.amazonaws.com"
        ]
      },
      "Resource": [
        "arn:aws:glue:`region`:`grantor_account_id`:catalog",
        "arn:aws:glue:`region`:`grantor_account_id`:database/*",
        "arn:aws:glue:`region`:`grantor_account_id`:table/*"
      ]
    }
  ]
}
```

#### Sharing federated resources cross-account

This action automatically creates a AWS RAM share invite to share the resource with the
recipient account.

Option 1: Share to the account for the data lake admin to manage delegation

As the data lake admin, grant the following permissions to the recipient
account:

- DESCRIBE access on the federated database with grantable permission
- SELECT and DESCRIBE on the federated table(s) with grantable permission

Option 2: Share directly to IAM principals cross-account

As the data lake admin, grant the following permissions to the IAM principal in
the recipient account:

- DESCRIBE access on the federated database
- SELECT and DESCRIBE on the federated table(s)

Optionally, you can grant the above permissions to the account without grantable
for the recipient account data lake admin to view the shared resources.

### Recipient account (where Amazon Redshift resides)

#### Accepting the AWS RAM share

Log in as the data lake admin. If auto-accept is set for member accounts, the AWS RAM
share is automatically accepted. Otherwise, accept the AWS RAM share invite. Once accepted, the
shared resources become visible in the AWS RAM console under "Shared with me."

#### Creating a database resource link

Create a database resource link in the local Data Catalog that points to the shared federated
database. This resource link serves as the local reference that Amazon Redshift uses to access the
shared data.

#### Granting permissions for accessing tables in Amazon Redshift

Option 1: Shared on account level

As the data lake admin, grant the following AWS Lake Formation permissions to the IAM
principal or IAM role used for creating the external schema:

- DESCRIBE on the resource link database
- DESCRIBE on the shared federated database
- SELECT and DESCRIBE on the shared federated table

Option 2: Shared directly to IAM principals cross-account

As the data lake admin, grant the following AWS Lake Formation permissions to the IAM
principal or IAM role used for creating the external schema:

- DESCRIBE on the resource link database

#### Querying the federated table from Amazon Redshift

Connect to your Amazon Redshift cluster or workgroup as an admin user and access the table using one
of the following options.

Option 1: Create an external schema using an IAM role

Create an IAM role with permission to AWS Glue and AWS Lake Formation APIs and attach
the role to the cluster.

```
CREATE EXTERNAL SCHEMA `external_schema_name`
FROM DATA CATALOG DATABASE '`resource_link_database`'
IAM_ROLE 'arn:aws:iam::`account_id`:role/`spectrum_role`';
```

You can grant permissions on this external schema to Amazon Redshift local users and groups.
Local Amazon Redshift identities can access the data by querying the schema using permissions
granted to the IAM role attached to the external schema.

```
SELECT * FROM "`database`"."`external_schema_name`"."`table_name`" LIMIT 10;
```

Option 2: Create an external schema using IAM SESSION for a federated principal

```
CREATE EXTERNAL SCHEMA `external_schema_name`
FROM DATA CATALOG DATABASE '`resource_link_database`'
IAM_ROLE 'SESSION' CATALOG_ID '`account_id`';
```

Log in as a federated user or with an IAM identity and run the following command
to query the table:

```
SELECT * FROM "`database`"."`external_schema_name`"."`table_name`" LIMIT 10;
```

Option 3: Use automount to query a federated table

The admin user should grant usage on the automounted database to federated
principals. The principal can then access the federated table by running the following
command:

```
SELECT * FROM "awsdatacatalog"."`resource_link_database`"."`table_name`" LIMIT 10;
```

## Best practices and limitations

- **Prefer automount for cross-Region deployments.**
  Automount handles cross-Region resolution transparently and requires no schema management
  overhead.
- **Use same-Region deployment when external schemas are required.**
  If your workflow requires external schemas (for example, to control schema-level permissions
  or naming), make sure the AWS Glue federated catalog, Amazon Redshift compute, and source Amazon S3 bucket are
  all in the same Region.
