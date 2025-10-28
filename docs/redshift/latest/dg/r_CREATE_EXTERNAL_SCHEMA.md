Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# CREATE EXTERNAL SCHEMA

Creates a new external schema in the current database. You can use this external schema
to connect to Amazon RDS for PostgreSQL or Amazon Aurora PostgreSQL-Compatible Edition databases. You can also create
an external schema that references a database in an external data catalog such as AWS Glue,
Athena, or a database in an Apache Hive metastore, such as Amazon EMR.

The owner of this schema is the issuer of the CREATE EXTERNAL SCHEMA command. To
transfer ownership of an external schema, use [ALTER SCHEMA](r_ALTER_SCHEMA.md "r_ALTER_SCHEMA.md") to change the owner. To grant access to the schema to
other users or user groups, use the [GRANT](r_GRANT.md "r_GRANT.md")
command.

You can't use the GRANT or REVOKE commands for permissions on an external table.
Instead, grant or revoke the permissions on the external schema.

###### Note

If you currently have Redshift Spectrum external tables in the Amazon Athena data catalog, you can
migrate your Athena data catalog to an AWS Glue Data Catalog. To use the AWS Glue Data Catalog with
Redshift Spectrum, you might need to change your AWS Identity and Access Management (IAM) policies. For more information, see
[Upgrading to the AWS Glue Data
Catalog](../../../athena/latest/ug/glue-athena.md#glue-upgrade "../../../athena/latest/ug/glue-athena.md#glue-upgrade") in the _Athena User Guide_.

To view details for external schemas, query the [SVV_EXTERNAL_SCHEMAS](r_SVV_EXTERNAL_SCHEMAS.md "r_SVV_EXTERNAL_SCHEMAS.md") system view.

## Syntax

The following syntax describes the CREATE EXTERNAL SCHEMA command used to reference
data using an external data catalog. For more information, see [Amazon Redshift Spectrum](c-using-spectrum.md "c-using-spectrum.md").

```
CREATE EXTERNAL SCHEMA [IF NOT EXISTS] *local\_schema\_name*
FROM [ [ DATA CATALOG ] | HIVE METASTORE | POSTGRES | MYSQL | KINESIS | MSK | REDSHIFT | KAFKA ]
[ DATABASE '*database\_name*' ]
[ SCHEMA '*schema\_name*' ]
[ REGION '*aws-region*' ]
[ IAM_ROLE [ default | 'SESSION' | 'arn:aws:iam::<AWS account-id>:role/<role-name>' ] ]
[ AUTHENTICATION [ none | iam | mtls] ]
[ AUTHENTICATION_ARN 'acm-certificate-arn' | SECRET_ARN 'ssm-secret- arn' ]
[ URI ['hive_metastore_uri' [ PORT port_number ] | 'hostname' [ PORT port_number ] | 'Kafka bootstrap URL'] ]
[ CLUSTER_ARN 'arn:aws:kafka:<region>:<AWS account-id>:cluster/msk/<cluster uuid>' ]
[ CATALOG_ROLE [ 'SESSION' | *'catalog-role-arn-string'* ] ]
[ CREATE EXTERNAL DATABASE IF NOT EXISTS ]
[ CATALOG_ID '*Amazon Web Services account ID containing Glue or Lake Formation database*' ]
```

The following syntax describes the CREATE EXTERNAL SCHEMA command used to reference
data using a federated query to RDS POSTGRES or Aurora PostgreSQL. You can also create an
external schema that references streaming sources, such as Kinesis Data Streams. For more information,
see [Querying data with federated queries in Amazon Redshift](federated-overview.md "federated-overview.md").

```
CREATE EXTERNAL SCHEMA [IF NOT EXISTS] *local\_schema\_name*
FROM POSTGRES
DATABASE '*federated\_database\_name*' [SCHEMA '*schema\_name*']
URI '*hostname*' [ PORT *port\_number* ]
IAM_ROLE [ default | 'arn:aws:iam::<AWS account-id>:role/<role-name>' ]
SECRET_ARN '*ssm-secret-arn*'

```

The following syntax describes the CREATE EXTERNAL SCHEMA command used to reference
data using a federated query to RDS MySQL or Aurora MySQL. For more information, see [Querying data with federated queries in Amazon Redshift](federated-overview.md "federated-overview.md").

```
CREATE EXTERNAL SCHEMA [IF NOT EXISTS] *local\_schema\_name*
FROM MYSQL
DATABASE '*federated\_database\_name*'
URI '*hostname*' [ PORT *port\_number* ]
IAM_ROLE [ default | 'arn:aws:iam::<AWS account-id>:role/<role-name>' ]
SECRET_ARN '*ssm-secret-arn*'

```

The following syntax describes the CREATE EXTERNAL SCHEMA command used to reference
data in a Kinesis stream. For more information, see [Streaming ingestion to a materialized view](materialized-view-streaming-ingestion.md "materialized-view-streaming-ingestion.md").

```
CREATE EXTERNAL SCHEMA [IF NOT EXISTS] *schema\_name*
FROM KINESIS
IAM_ROLE [ default | 'arn:aws:iam::<AWS account-id>:role/<role-name>' ]

```

The following syntax describes the CREATE EXTERNAL SCHEMA command used to reference
the Amazon Managed Streaming for Apache Kafka or Confluent Cloud cluster and its topics to ingest from. To connect, you
provide the broker URI. For more information, see [Streaming ingestion to a materialized view](materialized-view-streaming-ingestion.md "materialized-view-streaming-ingestion.md").

```
CREATE EXTERNAL SCHEMA [IF NOT EXISTS] *schema\_name*
FROM KAFKA
[ IAM_ROLE [ default | 'arn:aws:iam::<AWS account-id>:role/<role-name>' ] ]
URI '*Kafka bootstrap URI*'
AUTHENTICATION [ none | iam | mtls ]
[ AUTHENTICATION_ARN 'acm-certificate-arn' | SECRET_ARN 'ssm-secret- arn' ];

```

The following syntax describes the CREATE EXTERNAL SCHEMA command used to reference
data using a cross-database query.

```
CREATE EXTERNAL SCHEMA *local\_schema\_name*
FROM  REDSHIFT
DATABASE '*redshift\_database\_name*' SCHEMA '*redshift\_schema\_name*'
```

## Parameters

IF NOT EXISTS

A clause that indicates that if the specified schema already exists, the
command should make no changes and return a message that the schema exists,
rather than terminating with an error. This clause is useful when scripting, so
the script doesn't fail if CREATE EXTERNAL SCHEMA tries to create a schema
that already exists.

local_schema_name

The name of the new external schema. For more information about valid names,
see [Names and identifiers](r_names.md "r_names.md").

FROM [ DATA CATALOG ] | HIVE METASTORE | POSTGRES | MYSQL | KINESIS | MSK |
REDSHIFT

A keyword that indicates where the external database is located.

DATA CATALOG indicates that the external database is defined in the Athena
data catalog or the AWS Glue Data Catalog.

If the external database is defined in an external Data Catalog in a different
AWS Region, the REGION parameter is required. DATA CATALOG is the
default.

HIVE METASTORE indicates that the external database is defined in an Apache
Hive metastore. If HIVE METASTORE, is specified, URI is required.

POSTGRES indicates that the external database is defined in RDS PostgreSQL
or Aurora PostgreSQL.

MYSQL indicates that the external database is defined in RDS MySQL or
Aurora MySQL.

KINESIS indicates that the data source is a stream from Kinesis Data Streams.

MSK indicates that the data source is an Amazon MSK provisioned or serverless
cluster.

KAFKA indicates that the data source is a Kafka cluster. You can use this
keyword for both Amazon MSK and Confluent Cloud.

FROM REDSHIFT

A keyword that indicates that the database is located in Amazon Redshift.

DATABASE '_redshift_database_name_' SCHEMA
'_redshift_schema_name_'

The name of the Amazon Redshift database.

The _redshift_schema_name_ indicates the schema in
Amazon Redshift. The default _redshift_schema_name_ is
`public`.

DATABASE '_federated_database_name_'

A keyword that indicates the name of the external database in a supported
PostgreSQL or MySQL database engine.

[SCHEMA '*schema\_name*']

The _schema_name_ indicates the schema in a supported
PostgreSQL database engine. The default _schema_name_ is
`public`.

You can't specify a SCHEMA when you set up a federated query to a
supported MySQL database engine.

REGION '_aws-region_'

If the external database is defined in an Athena data catalog or the
AWS Glue Data Catalog, the AWS Region in which the database is located. This parameter
is required if the database is defined in an external Data Catalog.

URI [ 'hive_metastore_uri' [ PORT port\_number ] | 'hostname' [ PORT port\_number
] | 'Kafka bootstrap URI' ]

The hostname URI and port_number of a supported PostgreSQL or MySQL database
engine. The _hostname_ is the head node of the replica set.
The endpoint must be reachable (routable) from the Amazon Redshift cluster.
The default
PostgreSQL port_number is 5432. The default MySQL port_number is 3306.

###### Note

The supported PostgreSQL or MySQL database engine must be in the same VPC
as your Amazon Redshift cluster with a security group linking Amazon Redshift and RDS
url-rsPostgreSQL or Aurora PostgreSQL. Additionally, you can use enhanced VPC
routing to configure a cross-VPC use case. For more information, see [Redshift-managed VPC
endpoints](../mgmt/managing-cluster-cross-vpc.md "../mgmt/managing-cluster-cross-vpc.md").

**Specifying a hive metastore URI**

If the database is in a Hive metastore, specify the URI and optionally the
port number for the metastore. The default port number is 9083.

A URI doesn't contain a protocol specification ("http://"). An example valid
URI: `uri '172.10.10.10'`.

**Specifying a broker URI for streaming
ingestion**

Including the bootstrap-broker URI provides the ability to connect to an
Amazon MSK or Confluent Cloud cluster and receive streamed data. For more
information and to see an example, see [Getting started with streaming ingestion from Amazon Managed Streaming for Apache Kafka](materialized-view-streaming-ingestion-getting-started-MSK.md "materialized-view-streaming-ingestion-getting-started-MSK.md").

IAM_ROLE [ default | 'SESSION' |
'arn:aws:iam::`<AWS account-id>`:role/`<role-name>`'
]

Use the default keyword to have Amazon Redshift use the IAM role that is set as
default and associated with the cluster when the CREATE EXTERNAL SCHEMA command
runs.

Use `'SESSION'` if you connect to your Amazon Redshift cluster using a
federated identity and access the tables from the external schema created using
this command. For more information, see [Using a federated
identity to manage Amazon Redshift access to local resources and Amazon Redshift Spectrum external
tables](../mgmt/authorization-fas-spectrum.md "../mgmt/authorization-fas-spectrum.md"), which explains how to configure federated identity. Note
that this configuration, using `'SESSION'` in place of the ARN, can
be used only if the schema is created using `DATA CATALOG`.

Use the Amazon Resource Name (ARN) for an IAM role that your cluster uses
for authentication and authorization. As a minimum, the IAM role must have
permission to perform a LIST operation on the Amazon S3 bucket to be accessed and a
GET operation on the Amazon S3 objects the bucket contains.

The following shows the syntax for the IAM_ROLE parameter string for a
single ARN.

```
IAM_ROLE 'arn:aws:iam::`<aws-account-id>`:role/`<role-name>`'
```

You can chain roles so that your cluster can assume another IAM role,
possibly belonging to another account. You can chain up to 10 roles. For an
example of chaining roles, see [Chaining IAM roles in Amazon Redshift Spectrum](c-spectrum-iam-policies.md#c-spectrum-chaining-roles "c-spectrum-iam-policies.md#c-spectrum-chaining-roles").

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

SECRET_ARN '_ssm-secret-arn_'

The Amazon Resource Name (ARN) of a supported PostgreSQL or MySQL database
engine secret created using AWS Secrets Manager. For information about how to create and
retrieve an ARN for a secret, see [Manage secrets with AWS Secrets Manager](../../../secretsmanager/latest/userguide/manage_create-basic-secret.md "../../../secretsmanager/latest/userguide/manage_create-basic-secret.md") in the
_AWS Secrets Manager User Guide_, and [Retrieving the Amazon Resource Name (ARN) of the secret in Amazon Redshift](../mgmt/redshift-secrets-manager-integration-retrieving-secret.md "../mgmt/redshift-secrets-manager-integration-retrieving-secret.md")..

CATALOG_ROLE [ 'SESSION' | *catalog-role-arn-string*]

Use `'SESSION'` to connect to your Amazon Redshift cluster using a federated
identity for authentication and authorization to the data catalog. For more
information about completing the steps for federated identity, see [Using a federated
identity to manage Amazon Redshift access to local resources and Amazon Redshift Spectrum external
tables](../mgmt/authorization-fas-spectrum.md "../mgmt/authorization-fas-spectrum.md"). Note that the `'SESSION'` role can be used only
if the schema is created in DATA CATALOG.

Use the Amazon Resource Name ARN for an IAM role that your cluster uses
for authentication and authorization for the data catalog.

If CATALOG_ROLE isn't specified, Amazon Redshift uses the specified IAM_ROLE. The
catalog role must have permission to access the Data Catalog in AWS Glue or Athena. For
more information, see [IAM policies for Amazon Redshift Spectrum](c-spectrum-iam-policies.md "c-spectrum-iam-policies.md").

The following shows the syntax for the CATALOG_ROLE parameter string for a
single ARN.

```
CATALOG_ROLE 'arn:aws:iam::`<aws-account-id>`:role/`<catalog-role>`'
```

You can chain roles so that your cluster can assume another IAM role,
possibly belonging to another account. You can chain up to 10 roles. For more
information, see [Chaining IAM roles in Amazon Redshift Spectrum](c-spectrum-iam-policies.md#c-spectrum-chaining-roles "c-spectrum-iam-policies.md#c-spectrum-chaining-roles").

###### Note

The list of chained roles must not include spaces.

The following shows the syntax for chaining three roles.

```
CATALOG_ROLE 'arn:aws:iam::`<aws-account-id>`:role/`<catalog-role-1-name>`,arn:aws:iam::`<aws-account-id>`:role/`<catalog-role-2-name>`,arn:aws:iam::`<aws-account-id>`:role/`<catalog-role-3-name>`'
```

CREATE EXTERNAL DATABASE IF NOT EXISTS

A clause that creates an external database with the name specified by the
DATABASE argument, if the specified external database doesn't exist. If
the specified external database exists, the command makes no changes. In this
case, the command returns a message that the external database exists, rather
than terminating with an error.

###### Note

You can't use CREATE EXTERNAL DATABASE IF NOT EXISTS with HIVE
METASTORE.

To use CREATE EXTERNAL DATABASE IF NOT EXISTS with a Data Catalog enabled for
AWS Lake Formation, you need `CREATE_DATABASE` permission on the Data Catalog.

CATALOG_ID '_Amazon Web Services account ID containing Glue or Lake
Formation database_'

The account id where the data catalog database is stored.

`CATALOG_ID` can be specified only if you plan to connect to your
Amazon Redshift cluster or to Amazon Redshift Serverless using a federated identity for
authentication and authorization to the data catalog by setting either of the
following:

- `CATALOG_ROLE` to `'SESSION'`
- `IAM_ROLE` to `'SESSION'` and
  `'CATALOG_ROLE'` set to its default

For more information about completing the steps for federated identity, see
[Using a federated
identity to manage Amazon Redshift access to local resources and Amazon Redshift Spectrum external
tables](../mgmt/authorization-fas-spectrum.md "../mgmt/authorization-fas-spectrum.md").

AUTHENTICATION

The authentication type defined for streaming ingestion. Streaming ingestion
with authentication types works with Amazon Managed Streaming for Apache Kafka. The `AUTHENTICATION`
types are the following:

- **none** – Specifies that there is
  no authentication required. This corresponds to Unauthenticated access on
  MSK or plaintext with TLS on Apache Kafka.
- **iam** – Specifies IAM
  authentication. When you choose this, make sure that the IAM role has
  permissions for IAM authentication. For more information about defining
  the external schema, see [Getting started with streaming ingestion
  from Apache Kafka sources](materialized-view-streaming-ingestion-getting-started-MSK.md "materialized-view-streaming-ingestion-getting-started-MSK.md").
- **mtls** – Specifies that mutual
  transport layer security provides secure communication by facilitating
  authentication between a client and server. In this case, the client is
  Redshift and the server is Amazon MSK. For more information about configuring
  streaming ingestion with mTLS, see [Authentication with mTLS for Redshift
  streaming ingestion from Apache Kafka sources](materialized-view-streaming-ingestion-mtls.md "materialized-view-streaming-ingestion-mtls.md").

AUTHENTICATION_ARN

The ARN of the AWS Certificate Manager certificate used by Amazon Redshift for mtls authentication
with Amazon MSK. The ARN is available in the ACM console when you choose the
issued certificate.

CLUSTER_ARN

For streaming ingestion, the CLUSTER_ARN is the cluster identifier for the
Amazon Managed Streaming for Apache Kafka cluster you're streaming from. When using CLUSTER_ARN, it requires an
IAM role policy that includes the `kafka:GetBootstrapBrokers`
permission. This option is provided for backward compatibility. Currently, we
recommend using the bootstrap-broker URI option to connect to Amazon Managed Streaming for Apache Kafka
clusters. For more information, see [Streaming
ingestion](materialized-view-streaming-ingestion.md "materialized-view-streaming-ingestion.md").

## Usage notes

For limits when using the Athena data catalog, see [Athena Limits](../../../general/latest/gr/aws_service_limits.md#amazon-athena-limits "../../../general/latest/gr/aws_service_limits.md#amazon-athena-limits") in the
AWS General Reference.

For limits when using the AWS Glue Data Catalog, see [AWS Glue Limits](../../../general/latest/gr/aws_service_limits.md#limits_glue "../../../general/latest/gr/aws_service_limits.md#limits_glue") in the
AWS General Reference.

These limits don’t apply to a Hive metastore.

There is a maximum of 9,900 schemas per database. For more information, see [Quotas
and limits](../mgmt/amazon-redshift-limits.md "../mgmt/amazon-redshift-limits.md") in the _Amazon Redshift Management Guide_.

To unregister the schema, use the [DROP SCHEMA](r_DROP_SCHEMA.md "r_DROP_SCHEMA.md") command.

To view details for external schemas, query the following system views:

- [SVV_EXTERNAL_SCHEMAS](r_SVV_EXTERNAL_SCHEMAS.md "r_SVV_EXTERNAL_SCHEMAS.md")
- [SVV_EXTERNAL_TABLES](r_SVV_EXTERNAL_TABLES.md "r_SVV_EXTERNAL_TABLES.md")
- [SVV_EXTERNAL_COLUMNS](r_SVV_EXTERNAL_COLUMNS.md "r_SVV_EXTERNAL_COLUMNS.md")

## Examples

The following example creates an external schema using a database in a data catalog
named `sampledb` in the US West (Oregon) Region. Use this example with an Athena or
AWS Glue data catalog.

```
create external schema spectrum_schema
from data catalog
database 'sampledb'
region 'us-west-2'
iam_role 'arn:aws:iam::123456789012:role/MySpectrumRole';
```

The following example creates an external schema and creates a new external database
named `spectrum_db`.

```
create external schema spectrum_schema
from data catalog
database 'spectrum_db'
iam_role 'arn:aws:iam::123456789012:role/MySpectrumRole'
create external database if not exists;
```

The following example creates an external schema using a Hive metastore database
named `hive_db`.

```
create external schema hive_schema
from hive metastore
database 'hive_db'
uri '172.10.10.10' port 99
iam_role 'arn:aws:iam::123456789012:role/MySpectrumRole';
```

The following example chains roles to use the role `myS3Role` for
accessing Amazon S3 and uses `myAthenaRole` for data catalog access. For more
information, see [Chaining IAM roles in Amazon Redshift Spectrum](c-spectrum-iam-policies.md#c-spectrum-chaining-roles "c-spectrum-iam-policies.md#c-spectrum-chaining-roles").

```
create external schema spectrum_schema
from data catalog
database 'spectrum_db'
iam_role 'arn:aws:iam::123456789012:role/myRedshiftRole,arn:aws:iam::123456789012:role/myS3Role'
catalog_role 'arn:aws:iam::123456789012:role/myAthenaRole'
create external database if not exists;
```

The following example creates an external schema that references an Aurora PostgreSQL
database.

```
CREATE EXTERNAL SCHEMA [IF NOT EXISTS] myRedshiftSchema
FROM POSTGRES
DATABASE 'my_aurora_db' SCHEMA 'my_aurora_schema'
URI 'endpoint to aurora hostname' PORT 5432
IAM_ROLE 'arn:aws:iam::123456789012:role/MyAuroraRole'
SECRET_ARN 'arn:aws:secretsmanager:us-east-2:123456789012:secret:development/MyTestDatabase-AbCdEf'

```

The following example creates an external schema to refer to the sales_db imported on
the consumer cluster.

```
CREATE EXTERNAL SCHEMA sales_schema FROM REDSHIFT DATABASE 'sales_db' SCHEMA 'public';
```

The following example creates an external schema that references an Aurora MySQL
database.

```
CREATE EXTERNAL SCHEMA [IF NOT EXISTS] myRedshiftSchema
FROM MYSQL
DATABASE 'my_aurora_db'
URI 'endpoint to aurora hostname'
IAM_ROLE 'arn:aws:iam::123456789012:role/MyAuroraRole'
SECRET_ARN 'arn:aws:secretsmanager:us-east-2:123456789012:secret:development/MyTestDatabase-AbCdEf'

```
