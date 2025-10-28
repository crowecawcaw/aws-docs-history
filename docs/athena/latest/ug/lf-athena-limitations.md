# Considerations and limitations for querying data

registered with Lake Formation

Consider the following when using Athena to query data registered in Lake Formation. For
additional information, see [Known issues for AWS Lake Formation](../../../lake-formation/latest/dg/limitations.md "../../../lake-formation/latest/dg/limitations.md") in
the _AWS Lake Formation Developer Guide_.

###### Considerations and Limitations

- [Column metadata visible to users without data permissions to column in
  some circumstances](#lf-athena-limitations-column-metadata "#lf-athena-limitations-column-metadata")
- [Working with Lake Formation permissions to views](#lf-athena-limitations-permissions-to-views "#lf-athena-limitations-permissions-to-views")
- [Iceberg DDL
  support](#lf-athena-limitations-iceberg-ddl-operations "#lf-athena-limitations-iceberg-ddl-operations")
- [Lake Formation
  fine-grained access control and Athena workgroups](#lf-athena-limitations-fine-grained-access-control "#lf-athena-limitations-fine-grained-access-control")
- [Athena query results location in Amazon S3 not registered with
  Lake Formation](#lf-athena-limitations-query-results-location "#lf-athena-limitations-query-results-location")
- [Use Athena workgroups to limit access to query history](#lf-athena-limitations-use-workgroups-to-limit-access-to-query-history "#lf-athena-limitations-use-workgroups-to-limit-access-to-query-history")
- [CSE-KMS Amazon S3 registered with Lake Formation cannot be queried in
  Athena](#lf-athena-limitations-cse-kms "#lf-athena-limitations-cse-kms")
- [Partitioned data locations registered with Lake Formation must be in table
  subdirectories](#lf-athena-limitations-partioned-data-locations "#lf-athena-limitations-partioned-data-locations")
- [Create table as select (CTAS) queries require Amazon S3 write
  permissions](#lf-athena-limitations-ctas-queries "#lf-athena-limitations-ctas-queries")
- [The DESCRIBE permission is
  required on the default database](#lf-athena-limitations-describe-default "#lf-athena-limitations-describe-default")

## Column metadata visible to

unauthorized users in some circumstances with Avro and custom SerDe

Lake Formation column-level authorization prevents users from accessing data in columns for
which the user does not have Lake Formation permissions. However, in certain situations, users
are able to access metadata describing all columns in the table, including the
columns for which they do not have permissions to the data.

This occurs when column metadata is stored in table properties for tables using
either the Apache Avro storage format or using a custom Serializer/Deserializer
(SerDe) in which table schema is defined in table properties along with the SerDe
definition. When using Athena with Lake Formation, we recommend that you review the contents of
table properties that you register with Lake Formation and, where possible, limit the
information stored in table properties to prevent any sensitive metadata from being
visible to users.

## Understand Lake Formation and

views

For data registered with Lake Formation, an Athena user can create a `VIEW` only
if they have Lake Formation permissions to the tables, columns, and source Amazon S3 data locations
on which the `VIEW` is based. After a `VIEW` is created in
Athena, Lake Formation permissions can be applied to the `VIEW`. Column-level
permissions are not available for a `VIEW`. Users who have Lake Formation
permissions to a `VIEW` but do not have permissions to the table and
columns on which the view was based are not able to use the `VIEW` to
query data. However, users with this mix of permissions are able to use statements
like `DESCRIBE VIEW`, `SHOW CREATE VIEW`, and `SHOW
 COLUMNS` to see `VIEW` metadata. For this reason, be sure to
align Lake Formation permissions for each `VIEW` with underlying table permissions.
Cell filters defined on a table do not apply to a `VIEW` for that table.
Resource link names must have the same name as the resource in the originating
account. There are additional limitations when working with views in a cross-account
setup. For more information about setting up permissions for shared views across
accounts, see [Configure cross-account Data
Catalog access](lf-athena-limitations-cross-account.md "lf-athena-limitations-cross-account.md").

## Iceberg DDL

support

Athena does not currently support DDL operations on Iceberg tables whose location
is registered with Lake Formation. Attempting to run a DDL query on one of these Iceberg
tables can return an Amazon S3 access denied error or fail with a query timeout. DDL
operations on Iceberg tables require the user to have direct Amazon S3 access to the
Iceberg table location.

## Lake Formation

fine-grained access control and Athena workgroups

Users in the same Athena workgroup can see the data that Lake Formation fine-grained access
control has configured to be accessible to the workgroup. For more information about
using fine-grained access control in Lake Formation, see [Manage fine-grained access control using AWS Lake Formation](https://aws.amazon.com/blogs/big-data/manage-fine-grained-access-control-using-aws-lake-formation/ "https://aws.amazon.com/blogs/big-data/manage-fine-grained-access-control-using-aws-lake-formation/") in the _AWS Big Data Blog_.

## Athena query results

location in Amazon S3 not registered with Lake Formation

The query results locations in Amazon S3 for Athena cannot be registered with Lake Formation. Lake Formation permissions don't limit access to these locations. Unless you limit access, Athena users can access query result files and metadata when they don't have Lake Formation permissions for the data. To avoid this, we recommend that you use workgroups to specify the location for query results and align workgroup membership with Lake Formation permissions. You can then use IAM permissions policies to limit access to query results locations. For more information about query results, see [Work with query results and recent queries](querying.md "querying.md").

## Use Athena workgroups to limit access to query history

Athena query history exposes a list of saved queries and complete query strings. Unless you use workgroups to separate access to query histories, Athena users who are not authorized to query data in Lake Formation are able to view query strings run on that data, including column names, selection criteria, and so on. We recommend that you use workgroups to separate query histories, and align Athena workgroup membership with Lake Formation permissions to limit access. For more information, see [Use workgroups to control query
access and costs](workgroups-manage-queries-control-costs.md "workgroups-manage-queries-control-costs.md").

## Query CSE_KMS encrypted tables

registered with Lake Formation

Open Table Format (OTF) tables such as Apache Iceberg that have the following
characteristics cannot be queried with Athena:

- The tables are based on Amazon S3 data locations that are registered with
  Lake Formation.
- The objects in Amazon S3 are encrypted using client-side encryption
  (CSE).
- The encryption uses AWS KMS customer-managed keys
  (`CSE_KMS`).

To query non-OTF tables that are encrypted with a `CSE_KMS` key), add
the following block to the policy of the AWS KMS key that you use for CSE encryption.
`<KMS_KEY_ARN>` is the ARN of the AWS KMS key that
encrypts the data. `<IAM-ROLE-ARN>` is the ARN of the
IAM role that registers the Amazon S3 location in Lake Formation.

```
{
    "Sid": "Allow use of the key",
    "Effect": "Allow",
    "Principal": {
        "AWS": "*"
    },
    "Action": "kms:Decrypt",
    "Resource": "`<KMS-KEY-ARN>`",
    "Condition": {
        "ArnLike": {
            "aws:PrincipalArn": "`<IAM-ROLE-ARN>`"
        }
    }
}
```

## Partitioned data

locations registered with Lake Formation must be in table subdirectories

Partitioned tables registered with Lake Formation must have partitioned data in directories
that are subdirectories of the table in Amazon S3. For example, a table with the location
`s3://amzn-s3-demo-bucket/mytable` and partitions
`s3://amzn-s3-demo-bucket/mytable/dt=2019-07-11`,
`s3://amzn-s3-demo-bucket/mytable/dt=2019-07-12`, and so on can be
registered with Lake Formation and queried using Athena. On the other hand, a table with the
location `s3://amzn-s3-demo-bucket/mytable` and partitions located in
`s3://amzn-s3-demo-bucket/dt=2019-07-11`,
`s3://amzn-s3-demo-bucket/dt=2019-07-12`, and so on, cannot be
registered with Lake Formation. Because such partitions are not subdirectories of
`s3://amzn-s3-demo-bucket/mytable`, they also cannot be read from
Athena.

## Create table as select (CTAS)

queries require Amazon S3 write permissions

Create Table As Statements (CTAS) require write access to the Amazon S3 location of tables. To run CTAS queries on data registered with Lake Formation, Athena users must have IAM permissions to write to the table Amazon S3 locations in addition to the appropriate Lake Formation permissions to read the data locations. For more information, see [Create a table from query results (CTAS)](ctas.md "ctas.md").

## The DESCRIBE permission is

required on the default database

The Lake Formation `DESCRIBE` permission is required on the `default`
database so that Lake Formation can view it. The following example AWS CLI command grants the
`DESCRIBE` permission on the `default` database to the
user `datalake_user1` in AWS account `111122223333`.

```
aws lakeformation grant-permissions --principal DataLakePrincipalIdentifier=arn:aws:iam::111122223333:user/datalake_user1 --permissions "DESCRIBE" --resource '{ "Database": {"Name":"default"}}
```

For more information, see [DESCRIBE](../../../lake-formation/latest/dg/lf-permissions-reference.md#perm-describe "../../../lake-formation/latest/dg/lf-permissions-reference.md#perm-describe") in the _AWS Lake Formation Developer Guide_.
