Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# SHOW DATABASES

Displays databases from a Data Catalog or an Amazon Redshift data warehouse. SHOW DATABASES lists all
accessible databases, such as, within the data warehouse, AWS Glue Data Catalog databases
(awsdatacatalog), data sharing databases, and Lake Formation databases.

## Required permissions

All databases are visible to users except:

- For databases created from a datashare with permissions to be visible, the current user must be granted USAGE permission on the database.

## Syntax

To show databases from an Amazon Redshift data warehouse:

```
SHOW DATABASES
[ LIKE '<expression>' ]
[ LIMIT *row\_limit* ]
```

To show databases from a Data Catalog:

```
SHOW DATABASES FROM DATA CATALOG
[ ACCOUNT  '<id1>', '<id2>', ... ]
[ LIKE '<expression>' ]
[ IAM_ROLE default | 'SESSION' | 'arn:aws:iam::<account-id>:role/<role-name>' ]
[ LIMIT *row\_limit* ]
```

## Parameters

ACCOUNT '<id1>', '<id2>', ...

The AWS Glue Data Catalog accounts from which to list databases. Omitting this
parameter indicates that Amazon Redshift should show the databases from the account
that owns the cluster.

LIKE '<expression>'

Filters the list of databases to those that match the expression that you
specify. This parameter supports patterns that use the wildcard characters %
(percent) and \_ (underscore).

IAM_ROLE default | 'SESSION' |
'arn:aws:iam::<account-id>:role/<role-name>'

If you specify an IAM role that is associated with the cluster when running
the SHOW DATABASES command, Amazon Redshift will use the role’s credentials when you
run queries on the database.

Specifying the `default` keyword means to use the IAM role
that's set as the default and associated with the cluster.

Use `'SESSION'` if you connect to your Amazon Redshift cluster using a
federated identity and access the tables from the external database created
using the [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md") command. For an example of using
a federated identity, see [Using a federated
identity to manage Amazon Redshift access to local resources and Amazon Redshift Spectrum external
tables](../mgmt/authorization-fas-spectrum.md "../mgmt/authorization-fas-spectrum.md"), which explains how to configure federated identity.

Use the Amazon Resource Name (ARN) for an IAM role that your cluster uses
for authentication and authorization. As a minimum, the IAM role must have
permission to perform a LIST operation on the Amazon S3 bucket to be accessed and a
GET operation on the Amazon S3 objects the bucket contains. To learn more about
databases created from the AWS Glue Data Catalog for datashares and using IAM_ROLE, see
[Working with Lake Formation-managed datashares as a consumer](lake-formation-getting-started-consumer.md "lake-formation-getting-started-consumer.md").

The following shows the syntax for the IAM_ROLE parameter string for a
single ARN.

```
IAM_ROLE 'arn:aws:iam::`<aws-account-id>`:role/`<role-name>`'

```

You can chain roles so that your cluster can assume another IAM role,
possibly belonging to another account. You can chain up to 10 roles. For more
information, see [Chaining IAM roles in Amazon Redshift Spectrum](c-spectrum-iam-policies.md#c-spectrum-chaining-roles "c-spectrum-iam-policies.md#c-spectrum-chaining-roles").

To this IAM role, attach an IAM permissions policy similar to the
following.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AccessSecret",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetResourcePolicy",
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret",
 "secretsmanager:ListSecretVersionIds"
 ],
 "Resource": "arn:aws:secretsmanager:`us-west-2`:`123456789012`:secret:my-rds-secret-VNenFy"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetRandomPassword",
 "secretsmanager:ListSecrets"
 ],
 "Resource": "*"
 }
 ]
}`

```

For the steps to create an IAM role to use with federated query, see [Creating a secret and an IAM role to use
federated queries](federated-create-secret-iam-role.md "federated-create-secret-iam-role.md").

###### Note

Don't include spaces in the list of chained roles.

The following shows the syntax for chaining three roles.

```
IAM_ROLE 'arn:aws:iam::`<aws-account-id>`:role/`<role-1-name>`,arn:aws:iam::`<aws-account-id>`:role/`<role-2-name>`,arn:aws:iam::`<aws-account-id>`:role/`<role-3-name>`'

```

LIMIT _row_limit_

Clause to LIMIT the number of rows returned. Where
_row_limit_ is the maximum number of rows to return. The
_row_limit_ can be 0–10,000.

## Examples

The following example displays all of the Data Catalog databases from the account ID 123456789012.

```
`SHOW DATABASES FROM DATA CATALOG ACCOUNT '123456789012'`
`catalog_id | database_name | database_arn | type | target_database | location | parameters
--------------+---------------+--------------------------------------------------------+--------------+--------------------------------------------------------------------------------------------------+----------+------------
 123456789012 | database1 | arn:aws:glue:us-east-1:123456789012:database/database1 | Data Catalog | | |
 123456789012 | database2 | arn:aws:glue:us-east-1:123456789012:database/database2 | Data Catalog | arn:aws:redshift:us-east-1:123456789012:datashare:035c45ea-61ce-86f0-8b75-19ac6102c3b7/database2 | |`

```

The following are examples that demonstrate how to display all of the Data Catalog
databases from the account ID 123456789012 while using an IAM role's
credentials.

```
SHOW DATABASES FROM DATA CATALOG ACCOUNT '123456789012' IAM_ROLE default;

```

```
SHOW DATABASES FROM DATA CATALOG ACCOUNT '123456789012' IAM_ROLE <iam-role-arn>;

```

The following example displays all of the databases in the connected Amazon Redshift data
warehouse.

```
`SHOW DATABASES`
`database_name | database_owner | database_type | database_acl | parameters | database_isolation_level
---------------+----------------+----------------------+--------------+------------+--------------------
awsdatacatalog | 1 | auto mounted catalog | NULL | UNKNOWN | UNKNOWN
dev | 1 | local | NULL | NULL | Snapshot Isolation`
```
