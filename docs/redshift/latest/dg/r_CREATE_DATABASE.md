Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE DATABASE

Creates a new database.

To create a database, you must be a superuser or have the CREATEDB privilege.
To create a
database associated with a zero-ETL integration, you must be a superuser or have both CREATEDB and
CREATEUSER privileges.

You can't run CREATE DATABASE within a transaction block (BEGIN ... END). For more
information about transactions, see [Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md").

## Syntax

```
CREATE DATABASE *database\_name*
[ { [
      FROM INTEGRATION '<integration_id>'[ DATABASE '<source_database>' ]
      [ SET ]
      [ ACCEPTINVCHARS [=] { TRUE | FALSE }]
      [ QUERY_ALL_STATES [=] { TRUE | FALSE }]
      [ REFRESH_INTERVAL <interval> ]
      [ TRUNCATECOLUMNS [=] { TRUE | FALSE } ]
      [ HISTORY_MODE [=] {TRUE | FALSE} ]
    ]
    [ WITH ]
    [ OWNER [=] *db\_owner* ]
    [ CONNECTION LIMIT { *limit* | UNLIMITED } ]
    [ COLLATE { CASE_SENSITIVE | CS | CASE_INSENSITIVE | CI } ]
    [ ISOLATION LEVEL { SNAPSHOT | SERIALIZABLE } ]
  }
  | { FROM { { ARN '<arn>' } { WITH DATA CATALOG SCHEMA '<schema>' | WITH NO DATA CATALOG SCHEMA } } }
  | { IAM_ROLE  {default | 'SESSION' | 'arn:aws:iam::<account-id>:role/<role-name>' } }
  | { [ WITH PERMISSIONS ] FROM DATASHARE *datashare\_name* OF [ ACCOUNT *account\_id* ] NAMESPACE *namespace\_guid* }
]
```

## Parameters

_database_name_

Name of the new database. For more information about valid names, see [Names and identifiers](r_names.md "r_names.md").

FROM INTEGRATION '<integration_id>' [ DATABASE '<source\_database>'
]

Specifies whether to create the database using a zero-ETL integration identifier. You
can retrieve the `integration_id` from SVV_INTEGRATION system view.
For Aurora PostgreSQL zero-ETL integrations, you also need to specify
`source_database` name, which can also be retrieved from
SVV_INTEGRATION.

For an example, see [Create databases to receive results of
zero-ETL integrations](#r_CREATE_DATABASE-integration "#r_CREATE_DATABASE-integration"). For more information about
creating databases with zero-ETL integrations, see [Creating
destination databases in Amazon Redshift](../mgmt/zero-etl-using.md "../mgmt/zero-etl-using.md") in the
_Amazon Redshift Management Guide_.

SET

Optional keyword.

ACCEPTINVCHARS [=] { TRUE | FALSE }

The ACCEPTINVCHARS clause sets whether zero-ETL integration tables continue with
ingestion when invalid characters are detected for the VARCHAR data type. When
invalid characters are encountered, the invalid character is replaced with a
default `?` character.

QUERY_ALL_STATES [=] { TRUE | FALSE }

The QUERY_ALL_STATES clause sets whether zero-ETL integration tables can be queried in
all states (`Synced`, `Failed`,
`ResyncRequired`, and `ResyncInitiated`). By default,
a zero-ETL integration table can only be queried in `Synced` state.

REFRESH_INTERVAL <interval>

The REFRESH_INTERVAL clause sets the approximate time interval, in seconds,
to refresh data from the zero-ETL source to the target database. The value can
be set 0–432,000 seconds (5 days) for zero-ETL integrations whose source type is
Aurora MySQL, Aurora PostgreSQL, or RDS for MySQL. For Amazon DynamoDB zero-ETL integrations, the value
can be set 900–432,000 seconds (15 minutes –5 days). The default
`interval` is zero (0) seconds for zero-ETL integrations whose source type
is Aurora MySQL, Aurora PostgreSQL, or RDS for MySQL.
For Amazon DynamoDB
zero-ETL integrations, the default `interval` is 900 seconds (15
minutes).

TRUNCATECOLUMNS [=] { TRUE | FALSE }

The TRUNCATECOLUMNS clause sets whether zero-ETL integration tables continue with
ingestion when the values for the VARCHAR column or SUPER column attributes are
beyond the limit. When `TRUE`, the values are truncated to fit into
the column and the values of overflowing JSON attributes are truncated to fit
into the SUPER column.

HISTORY_MODE [=] {TRUE | FALSE}

A clause that specifies whether Amazon Redshift will set history mode for all new
tables in the specified database. This option is only applicable for databases
created for zero-ETL integration.

The HISTORY_MODE clause can be set to `TRUE` or
`FALSE`. The default is `FALSE`. For information about
HISTORY_MODE, see [History mode](../mgmt/zero-etl-history-mode.md "../mgmt/zero-etl-history-mode.md")
in the _Amazon Redshift Management Guide_.

WITH

Optional keyword.

OWNER [=] db_owner

Specifies username of database owner.

CONNECTION LIMIT { _limit_ | UNLIMITED }

The maximum number of database connections users are permitted to have open
concurrently. The limit isn't enforced for superusers. Use the UNLIMITED
keyword to permit the maximum number of concurrent connections.

A limit on the number of connections for each user might also apply. For more
information, see [CREATE USER](r_CREATE_USER.md "r_CREATE_USER.md").
The default is UNLIMITED. To view current connections, query the [STV_SESSIONS](r_STV_SESSIONS.md "r_STV_SESSIONS.md") system
view.

###### Note

If both user and database connection limits apply, an unused connection
slot must be available that is within both limits when a user attempts to
connect.

COLLATE { CASE_SENSITIVE | CS | CASE_INSENSITIVE | CI }

A clause that specifies whether string search or comparison is
case sensitive or case insensitive. The default is case sensitive.

COLLATE is not supported when you create a database from a datashare.

CASE_SENSITIVE and CS are interchangeable and yield the same results.
Similarly, CASE_INSENSITIVE and CI are interchangeable and yield the same results.

ISOLATION LEVEL { SNAPSHOT | SERIALIZABLE }

A clause that specifies the isolation level used when queries run against a
database. For
more information on isolation levels, see [Isolation levels in Amazon Redshift](c_serial_isolation.md "c_serial_isolation.md").

- SNAPSHOT isolation – Provides an isolation level with
  protection against update and delete conflicts. This is the default for a
  database created in a provisioned cluster or serverless namespace.
- SERIALIZABLE isolation – Provides full serializability for
  concurrent transactions.

FROM ARN '<ARN>'

The AWS Glue database ARN to use to create the database.

{ WITH DATA CATALOG SCHEMA '<schema>' | WITH NO DATA CATALOG SCHEMA
}

###### Note

This parameter is only applicable if your CREATE DATABASE command also
uses the FROM ARN parameter.

Specifies whether to create the database using a schema to help access
objects in the AWS Glue Data Catalog.

IAM_ROLE { default | 'SESSION' |
'arn:aws:iam::`<AWS account-id>`:role/`<role-name>`'
}

###### Note

This parameter is only applicable if your CREATE DATABASE command also
uses the FROM ARN parameter.

If you specify an IAM role that is associated with the cluster when running
the CREATE DATABASE command, Amazon Redshift will use the role’s credentials when you
run queries on the database.

Specifying the `default` keyword means to use the IAM role
that's set as the default and associated with the cluster.

Use `'SESSION'` if you connect to your Amazon Redshift cluster using a
federated identity and access the tables from the external schema created using
this command. For an example of using a federated identity, see [Using a federated
identity to manage Amazon Redshift access to local resources and Amazon Redshift Spectrum external
tables](../mgmt/authorization-fas-spectrum.md "../mgmt/authorization-fas-spectrum.md"), which explains how to configure federated identity.

Use the Amazon Resource Name (ARN) for an IAM role that your cluster uses
for authentication and authorization. As a minimum, the IAM role must have
permission to perform a LIST operation on the Amazon S3 bucket to be accessed and a
GET operation on the Amazon S3 objects the bucket contains. To learn more about
using IAM_ROLE when creating a database using AWS Glue Data Catalog for datashares, see
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

## Syntax for using CREATE DATABASE

with a datashare

The following syntax describes the CREATE DATABASE command used to create databases
from a datashare for sharing data within the same AWS account.

```
CREATE DATABASE *database\_name*
[ [ WITH PERMISSIONS ] FROM DATASHARE *datashare\_name* OF [ ACCOUNT *account\_id* ] NAMESPACE *namespace\_guid*
```

The following syntax describes the CREATE DATABASE command used to create databases
from a datashare for sharing data across AWS accounts.

```
CREATE DATABASE *database\_name*
[ [ WITH PERMISSIONS ] FROM DATASHARE *datashare\_name* OF ACCOUNT *account\_id* NAMESPACE *namespace\_guid*
```

### Parameters for using CREATE

DATABASE with a datashare

FROM DATASHARE

A keyword that indicates where the datashare is located.

_datashare_name_

The name of the datashare that the consumer database is created
on.

WITH PERMISSIONS

Specifies that the database created from the datashare requires
object-level permissions to access individual database objects. Without this
clause, users or roles granted the USAGE permission on the database will
automatically have access to all database objects in the database.

NAMESPACE _namespace_guid_

A value that specifies the producer namespace that the datashare belongs
to.

ACCOUNT _account_id_

A value that specifies the producer account that the datashare belongs
to.

## Usage notes for CREATE DATABASE for data

sharing

As a database superuser, when you use CREATE DATABASE to create databases from
datashares within the AWS account, specify the NAMESPACE option. The ACCOUNT option is
optional. When you use CREATE DATABASE to create databases from datashares across AWS
accounts, specify both the ACCOUNT and NAMESPACE from the producer.

You can create only one consumer database for one datashare on a consumer cluster.
You can't create multiple consumer databases referring to the same
datashare.

## CREATE DATABASE from AWS Glue Data Catalog

To create a database using an AWS Glue database ARN, specify the ARN in your CREATE
DATABASE command.

```
CREATE DATABASE sampledb FROM ARN <glue-database-arn> WITH NO DATA CATALOG SCHEMA;
```

Optionally, you can also supply a value into the IAM_ROLE parameter. For more
information about the parameter and accepted values, see [Parameters](r_CREATE_DATABASE.md#r_CREATE_DATABASE-parameters "r_CREATE_DATABASE.md#r_CREATE_DATABASE-parameters").

The following are examples that demonstrate how to create a database from an ARN
using an IAM role.

```
CREATE DATABASE sampledb FROM ARN <glue-database-arn> WITH NO DATA CATALOG SCHEMA IAM_ROLE <iam-role-arn>
```

```
CREATE DATABASE sampledb FROM ARN <glue-database-arn> WITH NO DATA CATALOG SCHEMA IAM_ROLE default;
```

You can also create a database using a DATA CATALOG SCHEMA.

```
CREATE DATABASE sampledb FROM ARN <glue-database-arn> WITH DATA CATALOG SCHEMA <sample_schema> IAM_ROLE default;
```

## Create databases to receive results of

zero-ETL integrations

To create a database using a zero-ETL integration identity, specify the
`integration_id` in your CREATE DATABASE command.

```
CREATE DATABASE `destination_db_name` FROM INTEGRATION '`integration_id`';
```

For example, first, retrieve the integration ids from SVV_INTEGRATION;

```
SELECT integration_id FROM SVV_INTEGRATION;
```

Then use one of the integration ids retrieved to create the database that receives
zero-ETL integrations.

```
CREATE DATABASE sampledb FROM INTEGRATION 'a1b2c3d4-5678-90ab-cdef-EXAMPLE11111';
```

When the zero-ETL integrations source database is needed, then, for example, specify.

```
CREATE DATABASE sampledb FROM INTEGRATION 'a1b2c3d4-5678-90ab-cdef-EXAMPLE11111' DATABASE sourcedb;
```

You can also set a refresh interval for the database. For example, to set the refresh
interval to 7,200 seconds for data from a zero-ETL integration source:

```
CREATE DATABASE myacct_mysql FROM INTEGRATION 'a1b2c3d4-5678-90ab-cdef-EXAMPLE11111' SET REFRESH_INTERVAL 7200;
```

Query the SVV_INTEGRATION catalog view for information about a zero-ETL integration, such as,
integration_id, target_database, source, refresh_interval, and more.

```
SELECT * FROM svv_integration;
```

The following example creates a database from an integration with history mode
on.

```
CREATE DATABASE sample_integration_db FROM INTEGRATION 'a1b2c3d4-5678-90ab-cdef-EXAMPLE11111' SET HISTORY_MODE = true;
```

## CREATE DATABASE

limits

Amazon Redshift enforces these limits for databases:

- Maximum of 60 user-defined databases per cluster.
- Maximum of 127 bytes for a database name.
- A database name can't be a reserved word.

## Database collation

Collation is a set of rules that defines how database engine compares and sorts the
character type data in SQL. Case-insensitive collation is the most commonly used
collation. Amazon Redshift uses case-insensitive collation to facilitate migration from other
data warehouse systems. With the native support of case-insensitive collation, Amazon Redshift
continues to use important tuning or optimization methods, such as distribution keys,
sort keys, or range restricted scan.

The COLLATE clause specifies the default collation for all CHAR and VARCHAR columns
in the database. If CASE_INSENSITIVE is specified, all CHAR or VARCHAR columns use
case-insensitive collation. For information about collation, see [Collation sequences](c_collation_sequences.md "c_collation_sequences.md").

Data inserted or ingested in case-insensitive columns will keep its original case.
But all comparison-based string operations including sorting and grouping are
case-insensitive. Pattern matching operations such as LIKE predicates, similar to, and
regular expression functions are also case-insensitive.

The following SQL operations support applicable collation semantics:

- Comparison operators: =, <>, <, <=, >, >=.
- LIKE operator
- ORDER BY clauses
- GROUP BY clauses
- Aggregate functions that use string comparison, such as MIN and MAX and
  LISTAGG
- Window functions, such as PARTITION BY clauses and ORDER BY clauses
- Scalar functions greatest() and least(), STRPOS(), REGEXP_COUNT(),
  REGEXP_REPLACE(), REGEXP_INSTR(), REGEXP_SUBSTR()
- Distinct clause
- UNION, INTERSECT and EXCEPT
- IN LIST

For external queries, including Amazon Redshift Spectrum and Aurora PostgreSQL federated queries,
collation of VARCHAR or CHAR column is the same as the current database-level
collation.

The following example queries a Amazon Redshift Spectrum table:

```
SELECT ci_varchar FROM spectrum.test_collation
WHERE ci_varchar = 'AMAZON';

ci_varchar
----------
amazon
Amazon
AMAZON
AmaZon
(4 rows)
```

For information on how to create tables using database collation, see [CREATE TABLE](r_CREATE_TABLE_NEW.md "r_CREATE_TABLE_NEW.md").

For information on the COLLATE function, see [COLLATE function](r_COLLATE.md "r_COLLATE.md").

### Database collation

limitations

The following are limitations when working with database collation in
Amazon Redshift:

- All system tables or views, including PG catalog tables and Amazon Redshift system
  tables are case-sensitive.
- When consumer database and producer database have different database-level
  collations, Amazon Redshift doesn't support cross-database and cross-cluster
  queries.
- Amazon Redshift doesn't support case-insensitive collation in leader node-only
  query.

The following example shows an unsupported case-insensitive query and the
error that Amazon Redshift sends:

```
SELECT collate(usename, 'case_insensitive') FROM pg_user;
ERROR:  Case insensitive collation is not supported in leader node only query.
```

- Amazon Redshift doesn't support interaction between case-sensitive and
  case-insensitive columns, such as comparison, function, join, or set
  operations.

The following examples show errors when case-sensitive and case-insensitive
columns interact:

```
CREATE TABLE test
  (ci_col varchar(10) COLLATE case_insensitive,
   cs_col varchar(10) COLLATE case_sensitive,
   cint int,
   cbigint bigint);
```

```
SELECT ci_col = cs_col FROM test;
ERROR:  Query with different collations is not supported yet.
```

```
SELECT concat(ci_col, cs_col) FROM test;
ERROR:  Query with different collations is not supported yet.
```

```
SELECT ci_col FROM test UNION SELECT cs_col FROM test;
ERROR:  Query with different collations is not supported yet.
```

```
SELECT * FROM test a, test b WHERE a.ci_col = b.cs_col;
ERROR:  Query with different collations is not supported yet.
```

```
Select Coalesce(ci_col, cs_col) from test;
ERROR:  Query with different collations is not supported yet.
```

```
Select case when cint > 0 then ci_col else cs_col end from test;
ERROR:  Query with different collations is not supported yet.
```

To make these queries work, use the COLLATE function to convert collation of one
column to match the other. For more information, see [COLLATE function](r_COLLATE.md "r_COLLATE.md").

## Examples

###### Creating a database

The following example creates a database named TICKIT and gives ownership to the
user DWUSER.

```
create database tickit
with owner dwuser;
```

To view details about databases, query the PG_DATABASE_INFO catalog table.

```
select datname, datdba, datconnlimit
from pg_database_info
where datdba > 1;

 datname     | datdba | datconnlimit
-------------+--------+-------------
 admin       |    100 | UNLIMITED
 reports     |    100 | 100
 tickit      |    100 | 100
```

The following example creates a database named `sampledb` with
SNAPSHOT isolation level.

```
CREATE DATABASE sampledb ISOLATION LEVEL SNAPSHOT;
```

The following example creates the database sales_db from the datashare
salesshare.

```
CREATE DATABASE sales_db FROM DATASHARE salesshare OF NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
```

### Database collation

examples

###### Creating a case-insensitive database

The following example creates the `sampledb` database, creates the
`T1` table, and inserts data into the `T1` table.

```
create database sampledb collate case_insensitive;
```

Connect to the new database that you just created using your SQL client. When
using Amazon Redshift query editor v2, choose the `sampledb` in the
**Editor**. When using RSQL, use a command like the
following.

```
\connect sampledb;
```

```
CREATE TABLE T1 (
  col1 Varchar(20) distkey sortkey
);
```

```
INSERT INTO T1 VALUES ('bob'), ('john'), ('Mary'), ('JOHN'), ('Bob');
```

Then the query finds results with `John`.

```
SELECT * FROM T1 WHERE col1 = 'John';

 col1
 ------
 john
 JOHN
(2 row)
```

###### Ordering in a case-insensitive order

The following example shows the case-insensitive ordering with table T1. The
ordering of _Bob_ and _bob_ or
_John_ and _john_ is nondeterministic
because they are equal in case-insensitive column.

```
SELECT * FROM T1 ORDER BY 1;

 col1
 ------
 bob
 Bob
 JOHN
 john
 Mary
(5 rows)
```

Similarly, the following example shows case-insensitive ordering with the GROUP BY
clause. _Bob_ and _bob_ are equal and belong to
the same group. It is nondeterministic which one shows up in the result.

```
SELECT col1, count(*) FROM T1 GROUP BY 1;

 col1 | count
 -----+------
 Mary |  1
 bob  |  2
 JOHN |  2
(3 rows)
```

###### Querying with a window function on case-insensitive columns

The following example queries a window function on a case-insensitive
column.

```
SELECT col1, rank() over (ORDER BY col1) FROM T1;

 col1 | rank
 -----+------
 bob  |   1
 Bob  |   1
 john |   3
 JOHN |   3
 Mary |   5
(5 rows)
```

###### Querying with the DISTINCT keyword

The following example queries the `T1` table with the DISTINCT
keyword.

```
SELECT DISTINCT col1 FROM T1;

 col1
 ------
 bob
 Mary
 john
(3 rows)
```

###### Querying with the UNION clause

The following example shows the results from the UNION of the tables
`T1` and `T2`.

```
CREATE TABLE T2 AS SELECT * FROM T1;
```

```
SELECT col1 FROM T1 UNION SELECT col1 FROM T2;

 col1
 ------
 john
 bob
 Mary
(3 rows)
```
