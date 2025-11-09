# Configure access to databases and

tables in the AWS Glue Data Catalog

If you use the AWS Glue Data Catalog with Amazon Athena, you can define resource-level policies for the
database and table Data Catalog objects that are used in Athena.

###### Note

This topic discusses database- and table-level security. For information about
configuring column-, row-, and cell-level security, see [Data filtering and cell-level
security in Lake Formation](../../../lake-formation/latest/dg/data-filtering.md "../../../lake-formation/latest/dg/data-filtering.md").

You define resource-level permissions in IAM identity-based policies.

###### Important

This section discusses resource-level permissions in IAM identity-based policies.
These are different from resource-based policies. For more information about the
differences, see [Identity-based policies and resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md") in the
_IAM User Guide_.

See the following topics for these tasks:

| To perform this task                                     | See the following topic                                                                                                                                                                             |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create an IAM policy that defines access to resources    | [Creating IAM<br>policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_.                              |
| Learn about IAM identity-based policies used in AWS Glue | [Identity-based policies (IAM policies)](../../../glue/latest/dg/using-identity-based-policies.md "../../../glue/latest/dg/using-identity-based-policies.md") in the _AWS Glue<br>Developer Guide_. |

**In this section**

- [Limitations](#access-to-glue-resources-limitations "#access-to-glue-resources-limitations")
- [Configure AWS Glue access to your
  catalog and database per AWS Region](#full-access-to-default-db-per-region "#full-access-to-default-db-per-region")
- [About access
  control for table partitions and versions in AWS Glue](#access-to-glue-resources-table-partitions-and-versions "#access-to-glue-resources-table-partitions-and-versions")
- [Examples of database and
  table-level permissions](#examples-fine-grained-table-database-policies "#examples-fine-grained-table-database-policies")

## Limitations

Consider the following limitations when you use database and table-level access
control for the AWS Glue Data Catalog and Athena:

- IAM Identity Center enabled Athena workgroups require Lake Formation be configured to use IAM Identity Center
  identities. For more information, see [Integrating
  IAM Identity Center](../../../lake-formation/latest/dg/identity-center-integration.md "../../../lake-formation/latest/dg/identity-center-integration.md") in the _AWS Lake Formation Developer Guide_.
- You can limit access only to databases and tables. These controls apply at the
  table level. You cannot limit access to individual partitions within a table.
  For more information, see [About access
  control for table partitions and versions in AWS Glue](#access-to-glue-resources-table-partitions-and-versions "#access-to-glue-resources-table-partitions-and-versions").
- The AWS Glue Data Catalog contains the following resources: `CATALOG`,
  `DATABASE`, `TABLE`, and `FUNCTION`.

###### Note

From this list, resources that are common between Athena and the
AWS Glue Data Catalog are `TABLE`, `DATABASE`, and
`CATALOG` for each account. `Function` is specific
to AWS Glue. For delete actions in Athena, you must include permissions to AWS Glue
actions. See [Examples of database and
table-level permissions](#examples-fine-grained-table-database-policies "#examples-fine-grained-table-database-policies").

The hierarchy is as follows: `CATALOG` is an ancestor of all
`DATABASES` in each account, and each `DATABASE` is an
ancestor for all of its `TABLES` and `FUNCTIONS`. For
example, for a table named `table_test` that belongs to a database
`db` in the catalog in your account, its ancestors are
`db` and the catalog in your account. For the `db`
database, its ancestor is the catalog in your account, and its descendants are
tables and functions. For more information about the hierarchical structure of
resources, see [List of ARNs in Data Catalog](../../../glue/latest/dg/glue-specifying-resource-arns.md#data-catalog-resource-arns "../../../glue/latest/dg/glue-specifying-resource-arns.md#data-catalog-resource-arns") in the _AWS Glue Developer
Guide_.

- For any non-delete Athena action on a resource, such as `CREATE
DATABASE`, `CREATE TABLE`, `SHOW DATABASE`,
  `SHOW TABLE`, or `ALTER TABLE`, you need permissions
  to call this action on the resource (table or database) and all ancestors of the
  resource in the Data Catalog. For example, for a table, its ancestors are the
  database to which it belongs, and the catalog for the account. For a database,
  its ancestor is the catalog for the account. See [Examples of database and
  table-level permissions](#examples-fine-grained-table-database-policies "#examples-fine-grained-table-database-policies").
- For a delete action in Athena, such as `DROP DATABASE` or `DROP
TABLE`, you also need permissions to call the delete action on all
  ancestors and descendants of the resource in the Data Catalog. For example, to delete
  a database you need permissions on the database, the catalog, which is its
  ancestor, and all the tables and user defined functions, which are its
  descendents. A table does not have descendants. To run `DROP TABLE`,
  you need permissions to this action on the table, the database to which it
  belongs, and the catalog. See [Examples of database and
  table-level permissions](#examples-fine-grained-table-database-policies "#examples-fine-grained-table-database-policies").

## Configure AWS Glue access to your

catalog and database per AWS Region

For Athena to work with the AWS Glue, a policy that grants access to your database and to
the AWS Glue Data Catalog in your account per AWS Region is required. To create databases, the
`CreateDatabase` permission is also required. In the following example
policy, replace the AWS Region, AWS account ID, and database name with those of your
own.

```
{
   "Sid": "DatabasePermissions",
   "Effect": "Allow",
   "Action": [
      "glue:GetDatabase",
      "glue:GetDatabases",
      "glue:CreateDatabase"
   ],
   "Resource": [
     "arn:aws:glue:`us-east-1`:`123456789012`:catalog",
     "arn:aws:glue:`us-east-1`:`123456789012`:database/`default`"
   ]
}
```

## About access

control for table partitions and versions in AWS Glue

In AWS Glue, tables can have partitions and versions. Table versions and partitions are
not considered to be independent resources in AWS Glue. Access to table versions and
partitions is given by granting access on the table and ancestor resources for the
table.

For the purposes of access control, the following access permissions apply:

- Controls apply at the table level. You can limit access only to databases and
  tables. For example, if you allow access to a partitioned table, this access
  applies to all partitions in the table. You cannot limit access to individual
  partitions within a table.

###### Important

To run actions in AWS Glue on partitions, permissions for partition actions
are required at the catalog, database, and table levels. Having access to
partitions within a table is not sufficient. For example, to run
`GetPartitions` on table `myTable` in the database
`myDB`, you must grant `glue:GetPartitions`
permissions on the catalog, `myDB` database, and
`myTable` resources.

- Access controls do not apply to table versions. As with partitions, access to
  previous versions of a table is granted through access to the table version APIs
  in AWS Glue on the table, and to the table ancestors.

For information about permissions on AWS Glue actions, see [AWS Glue API permissions: Actions and
resources reference](../../../glue/latest/dg/api-permissions-reference.md "../../../glue/latest/dg/api-permissions-reference.md") in the _AWS Glue Developer Guide_.

## Examples of database and

table-level permissions

The following table lists examples of IAM identity-based policies that allow access
to databases and tables in Athena. We recommend that you start with these examples and,
depending on your needs, adjust them to allow or deny specific actions to particular
databases and tables.

These examples include access to databases and catalogs so that Athena and AWS Glue can
work together. For multiple AWS Regions, include similar policies for each of your
databases and catalogs, one line for each Region.

In the examples, replace the `example_db` database and `test`
table with your own database and table names.

| DDL statement     | Example of an IAM access policy granting access to the<br>resource                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ALTER DATABASE    | Allows you to modify the properties for the `example_db`<br>database.<br>``<br>{<br>"Effect": "Allow",<br>"Action": [<br>"glue:GetDatabase",<br>"glue:UpdateDatabase"<br>],<br>"Resource": [<br>"arn:aws:glue:`us-east-1`:`123456789012`:catalog",<br>"arn:aws:glue:`us-east-1`:`123456789012`:database/`example_db`"<br>]<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| CREATE DATABASE   | Allows you to create the database named<br>`example_db`.<br>``<br>{<br>"Effect": "Allow",<br>"Action": [<br>"glue:GetDatabase",<br>"glue:CreateDatabase"<br>],<br>"Resource": [<br>"arn:aws:glue:`us-east-1`:`123456789012`:catalog",<br>"arn:aws:glue:`us-east-1`:`123456789012`:database/`example_db`"<br>]<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| CREATE TABLE      | Allows you to create a table named `test` in the<br>`example_db`<br>database.<br>``<br>{<br>"Sid": "DatabasePermissions",<br>"Effect": "Allow",<br>"Action": [<br>"glue:GetDatabase",<br>"glue:GetDatabases"<br>],<br>"Resource": [<br>"arn:aws:glue:`us-east-1`:`123456789012`:catalog",<br>"arn:aws:glue:`us-east-1`:`123456789012`:database/`example_db`"<br>]<br>},<br>{<br>"Sid": "TablePermissions",<br>"Effect": "Allow",<br>"Action": [<br>"glue:GetTables",<br>"glue:GetTable",<br>"glue:GetPartitions",<br>"glue:CreateTable"<br>],<br>"Resource": [<br>"arn:aws:glue:`us-east-1`:`123456789012`:catalog",<br>"arn:aws:glue:`us-east-1`:`123456789012`:database/`example_db`",<br>"arn:aws:glue:`us-east-1`:`123456789012`:table/`example_db`/`test`"<br>]<br>}<br>`` |
| DROP DATABASE     | Allows you to drop the `example_db` database, including<br>all tables in it.<br>``<br>{<br>"Effect": "Allow",<br>"Action": [<br>"glue:GetDatabase",<br>"glue:DeleteDatabase",<br>"glue:GetTables",<br>"glue:GetTable",<br>"glue:DeleteTable"<br>],<br>"Resource": [<br>"arn:aws:glue:`us-east-1`:`123456789012`:catalog",<br>"arn:aws:glue:`us-east-1`:`123456789012`:database/`example_db`",<br>"arn:aws:glue:`us-east-1`:`123456789012`:table/`example_db`/*",<br>"arn:aws:glue:`us-east-1`:`123456789012`:userDefinedFunction/`example_db`/*"<br>]<br>}<br>``                                                                                                                                                                                                                |
| DROP TABLE        | Allows you to drop a partitioned table named `test` in the<br>`example_db` database. If your table does not have<br>partitions, do not include partition<br>actions.<br>``<br>{<br>"Effect": "Allow",<br>"Action": [<br>"glue:GetDatabase",<br>"glue:GetTable",<br>"glue:DeleteTable",<br>"glue:GetPartitions",<br>"glue:GetPartition",<br>"glue:DeletePartition"<br>],<br>"Resource": [<br>"arn:aws:glue:`us-east-1`:`123456789012`:catalog",<br>"arn:aws:glue:`us-east-1`:`123456789012`:database/`example_db`",<br>"arn:aws:glue:`us-east-1`:`123456789012`:table/`example_db`/`test`"<br>]<br>}<br>``                                                                                                                                                                       |
| MSCK REPAIR TABLE | Allows you to update catalog metadata after you add Hive compatible<br>partitions to the table named `test` in the<br>`example_db`<br>database.<br>``<br>{<br>"Effect": "Allow",<br>"Action": [<br>"glue:GetDatabase",<br>"glue:CreateDatabase",<br>"glue:GetTable",<br>"glue:GetPartitions",<br>"glue:GetPartition",<br>"glue:BatchCreatePartition"<br>],<br>"Resource": [<br>"arn:aws:glue:`us-east-1`:`123456789012`:catalog",<br>"arn:aws:glue:`us-east-1`:`123456789012`:database/`example_db`",<br>"arn:aws:glue:`us-east-1`:`123456789012`:table/`example_db`/`test`"<br>]<br>}<br>``                                                                                                                                                                                    |
| SHOW DATABASES    | Allows you to list all databases in the<br>AWS Glue Data Catalog.<br>``<br>{<br>"Effect": "Allow",<br>"Action": [<br>"glue:GetDatabase",<br>"glue:GetDatabases"<br>],<br>"Resource": [<br>"arn:aws:glue:`us-east-1`:`123456789012`:catalog",<br>"arn:aws:glue:`us-east-1`:`123456789012`:database/*"<br>]<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| SHOW TABLES       | Allows you to list all tables in the `example_db`<br>database.<br>``<br>{<br>"Effect": "Allow",<br>"Action": [<br>"glue:GetDatabase",<br>"glue:GetTables"<br>],<br>"Resource": [<br>"arn:aws:glue:`us-east-1`:`123456789012`:catalog",<br>"arn:aws:glue:`us-east-1`:`123456789012`:database/`example_db`",<br>"arn:aws:glue:`us-east-1`:`123456789012`:table/`example_db`/*"<br>]<br>}<br>``                                                                                                                                                                                                                                                                                                                                                                                    |
