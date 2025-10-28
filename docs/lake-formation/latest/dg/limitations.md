# Known issues for AWS Lake Formation

Review these known issues for AWS Lake Formation.

###### Topics

- [Limitation on filtering of table metadata](#issue-table-metadata-avro "#issue-table-metadata-avro")
- [Issue with renaming an excluded column](#issue-rename-column "#issue-rename-column")
- [Issue with deleting columns in CSV tables](#issue-csv-schema "#issue-csv-schema")
- [Table partitions must be added under a common path](#issue-table-partitions "#issue-table-partitions")
- [Issue with creating a database during workflow
  creation](#issue-create-table-permission "#issue-create-table-permission")
- [Issue with deleting and then re-creating a user](#issue-recreate-user "#issue-recreate-user")
- [Data Catalog API operations do not update the value for the IsRegisteredWithLakeFormation parameter](#issue-get-tables-parameter "#issue-get-tables-parameter")
- [Lake Formation operations do not support AWS Glue Schema
  Registry](#not-support-GlueSchemaRegistry.title "#not-support-GlueSchemaRegistry.title")

## Limitation on filtering of table metadata

AWS Lake Formation column-level permissions can be used to restrict access to specific columns in a
table. When a user retrieves metadata about the table using the console or an API like
`glue:GetTable`, the column list in the table object contains only the
fields to which they have access. It is important to understand the limitations of this
metadata filtering.

Although Lake Formation makes available metadata about column permissions to integrated
services, the actual filtering of columns in query responses is the responsibility of
the integrated service. Lake Formation clients that support column-level filtering, including
Amazon Athena, Amazon Redshift Spectrum, and Amazon EMR filter the data based on the column permissions
registered with Lake Formation. Users won't be able to read any data to which they should not have
access. Currently, AWS Glue ETL doesn't support column filtering.

###### Note

EMR clusters are not completely managed by AWS. Therefore, it's the responsibility of
EMR administrators to properly secure the clusters to avoid unauthorized access to
data.

Certain applications or formats might store additional metadata, including column
names and types, in the `Parameters` map as table properties. These
properties are returned unmodified and are accessible by any user with
`SELECT` permission on any column.

For example, the [Avro
SerDe](../../../athena/latest/ug/supported-serdes.md "../../../athena/latest/ug/supported-serdes.md") stores a JSON representation of the table schema in a table property
named `avro.schema.literal`, which is available to all users with access to
the table. We recommend that you avoid storing sensitive information in table properties
and be aware that users can learn the complete schema of Avro format tables. This
limitation is specific to the metadata about a table.

AWS Lake Formation removes any table property beginning with `spark.sql.sources.schema`
when responding to a `glue:GetTable` or similar request if the caller does
not have `SELECT` permissions on all columns in the table. This prevents
users from gaining access to additional metadata about tables created with Apache Spark.
When run on Amazon EMR, Apache Spark applications still can read these tables, but certain
optimizations might not be applied, and case-sensitive column names are not supported.
If the user has access to all columns in the table, Lake Formation returns the table unmodified
with all table properties.

## Issue with renaming an excluded column

If you use column-level permissions to exclude a column and then rename the column, the
column is no longer excluded from queries, such as `SELECT *`.

## Issue with deleting columns in CSV tables

If you create a Data Catalog table with the CSV format and then delete a column from the schema,
queries could return erroneous data, and column-level permissions might not be adhered
to.

Workaround: Create a new table instead.

## Table partitions must be added under a common path

Lake Formation expects all partitions of a table to be under a common path that is set in the table's
location field. When you use the crawler to add partitions to a catalog, this works
seamlessly. But if you add partitions manually, and these partitions are not under the
location set in the parent table, data access does not work.

## Issue with creating a database during workflow

creation

When creating a workflow from a blueprint using the Lake Formation console, you can create
the target database if it doesn't exist. When you do so, the user who is signed
in gets the `CREATE_TABLE` permission on the database that is created.
However, the crawler that the workflow generates assumes the workflow's role as it tries
to create a table. This fails because the role doesn’t have the
`CREATE_TABLE` permission on the database.

Workaround: If you create the database through the console during the workflow setup, before
you run the workflow, you must give the role associated with the workflow the
`CREATE_TABLE` permission on the database that you just created.

## Issue with deleting and then re-creating a user

The following scenario results in erroneous Lake Formation permissions returned by
`lakeformation:ListPermissions`:

1. Create a user and grant Lake Formation permissions.
2. Delete the user.
3. Re-create the user with the same name.

`ListPermissions` returns two entries, one for the old user and one for the new
user. If you try to revoke permissions granted to the old user, the permissions are
revoked from the new user.

## Data Catalog API operations do not update the value for the `IsRegisteredWithLakeFormation` parameter

There is a known limitation that Data Catalog API operations such as `GetTables` and `SearchTables` do not update the value for the `IsRegisteredWithLakeFormation` parameter, and return the default, which is false. It is recommended to use the `GetTable` API to view the correct value for the `IsRegisteredWithLakeFormation` parameter.

## Lake Formation operations do not support AWS Glue Schema

Registry

Lake Formation operations do not support AWS Glue tables that contain a `SchemaReference` in
the `StorageDescriptor` to be utilized in the [Schema
Registery](../../../glue/latest/dg/schema-registry.md "../../../glue/latest/dg/schema-registry.md").
