

# Amazon Athena Workday Live Data Query connector

With the Amazon Athena connector for Workday Live Data Query, you can run SQL queries on the current data in your Workday tenant, without copying or moving that data. This connector can be registered with AWS Glue Data Catalog as a federated catalog. It supports data access controls defined in Lake Formation at the catalog, database, table, column, and row levels. This connector uses Glue connections to centralize configuration properties in AWS Glue. AWS manages the connector for you, so you don't need to deploy an AWS Lambda function in your account.

For more information about Workday Live Data Query, see [Connecting to Workday Live Data Query](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-workday.html) in the *AWS Glue User Guide*. For information about federating Workday data to the AWS Glue Data Catalog through Workday Data Connect, see [Federate to Workday Data Connect](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation-workday.html) in the *AWS Lake Formation Developer Guide*.

## Prerequisites
<a name="connectors-workday-ldq-prerequisites"></a>

Before you set up the connector, make sure that you have the following.
+ A Workday tenant with Workday Data Cloud, and Live Data Query available for your tenant. Your subscription might require extra enablement.
+ An Integration System User (ISU), and an API client registered for the ISU with the JWT Bearer Grant client grant type. The domain permissions of the ISU determine which Workday tables and columns you can query. For more information, see [Set Up Live Data Query ISU Authentication in Workday](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-live-data-query-/set-up-live-data-query-isu-authentication.html) in the Workday documentation.
+ The following information from your Workday administrator.
  + **Workday Data Service host** – The host name of the Workday service that runs Live Data Query queries.
  + **Token endpoint** – The Workday OAuth 2.0 token endpoint, in the format `https://{{host}}/ccx/oauth2/{{tenant}}/token`.
  + **Integration System User** – The ISU user name.
  + **Client ID** – The client ID of the API client registered for the ISU.
  + **Private key** – The RSA private key, in PEM format, that matches the x509 certificate registered for the API client.
+ An Amazon S3 bucket in the same AWS Region as the connector, to use as a spill location for data that exceeds the memory limits of the connector.
+ The AWS CLI, installed and configured. For more information, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) in the *AWS Command Line Interface User Guide*.
+ An IAM principal that is a Lake Formation data lake administrator or that has the `CREATE_CATALOG` permission on the AWS Glue Data Catalog, and that has permissions to create AWS Glue connections and catalogs, AWS Secrets Manager secrets, and IAM roles.

## Limitations
<a name="connectors-workday-ldq-limitations"></a>
+ Write DDL and DML operations are not supported. The connector is read-only.
+ DDL statements such as `SHOW TABLES` are not supported on the federated catalog. To list tables and columns, query `information_schema` or browse the catalog in the Athena query editor.
+ Passthrough queries are not supported.
+ The Athena console doesn't offer Workday Live Data Query as a data source. Create the connection and the federated catalog with the AWS CLI, or with the AWS Glue and Lake Formation APIs, as described in [Set up the connector](#connectors-workday-ldq-setup).
+ Workday Live Data Query connections that you create in AWS Glue Studio are for AWS Glue ETL jobs. If you want to use the connection with Athena, you can update the connection with the AWS CLI to add support for Athena.
+ The connector supports only ISU authentication. Workday User As Self (UAS) authentication isn't supported.
+ Queries run against live data in your Workday tenant, so they typically take longer than queries on data stored in Amazon S3.
+ Workday applies its own guardrails, such as query run time, concurrent queries per tenant, and memory per query. These guardrails apply to queries that come from Athena. For current limits, see [Get Started with Workday Live Data Query](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-live-data-query-/workday-live-data-query.html) in the Workday documentation.

## Parameters
<a name="connectors-workday-ldq-parameters"></a>

You configure the connector by using a Glue connection of type `WORKDAYLDQ`.

### Glue connection properties
<a name="connectors-workday-ldq-glue-properties"></a>

Use the following command to get the schema for the connection type. This schema contains the properties that you can use to control your connection.

```bash
aws glue describe-connection-type --connection-type WORKDAYLDQ
```

The following table describes the connection properties.



| Property | Required | Description | 
| --- | --- | --- | 
| HOST | Yes | Your Workday Data Service host name. | 
| PORT | Yes | The port number. Use 443. | 
| ROLE\_ARN | Yes | The ARN of the IAM role that AWS Glue and Lake Formation use to retrieve the secret and access the spill location. | 
| ENFORCE\_SSL | No | Whether to enforce SSL. The default is false. Connections to Workday on port 443 use TLS whether or not you set this property. | 
| JDBC\_PARAMS | No | Additional Workday driver parameters, in the format key1=value1;key2=value2. | 

### Athena properties
<a name="connectors-workday-ldq-athena-properties"></a>

Specify the following properties in the `AthenaProperties` object of the Glue connection.



| Property | Required | Description | 
| --- | --- | --- | 
| MANAGED\_CONNECTION | Yes | Set to true so that AWS manages the connector for Athena. You can't create a federated catalog from the connection without this property. | 
| spill\_bucket | Yes | The Amazon S3 bucket for data that exceeds the memory limits of the connector. The bucket must be in the same AWS Region as the connection. | 
| spill\_prefix | No | The prefix in spill\_bucket for spilled data. We recommend that you configure an Amazon S3 [storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) to delete old spills. | 
| spill\_kms\_key\_id | No | The AWS KMS key ID to use to encrypt spilled data. By default, spilled data is encrypted with AES-GCM and a randomly generated key. | 
| disable\_spill\_encryption | No | When set to true, disables spill encryption. The default is false. | 
| default\_scale | No | The default scale for numeric values, which is the number of digits to the right of the decimal point. | 

## Storing credentials
<a name="connectors-workday-ldq-storing-credentials"></a>

The connector uses custom authentication and reads Workday OAuth 2.0 credentials from an AWS Secrets Manager secret. The connector signs a JSON Web Token (JWT) for the ISU with your private key and exchanges it for an access token at the Workday token endpoint.

The secret must contain the following keys.
+ `wd.authn.isu` – The ISU user name. The connector uses this value as the JWT subject.
+ `wd.authn.clientId` – The client ID of the API client registered for the ISU.
+ `wd.authn.accessTokenEndpoint` – The Workday OAuth 2.0 token endpoint URL.
+ `wd.authn.privateKey` – The PEM private key that the connector uses to sign the JWT.

**Note**  
The key names are reserved. Enter them exactly. The private key must keep its line breaks. If you create the secret as JSON, encode each line break as `\n`.

## Set up the connector
<a name="connectors-workday-ldq-setup"></a>

To create a connection for Athena with Workday Live Data Query as a data source, you can use the AWS CLI. The following steps create an AWS Secrets Manager secret, an IAM role, and a Glue connection, register the connection with Lake Formation, and create a federated catalog that you query in Athena. Create all resources in the same AWS Region.

### Create an AWS Secrets Manager secret
<a name="connectors-workday-ldq-setup-secret"></a>

Create a file named `secret.json` that contains your Workday OAuth 2.0 credentials.

```json
{
  "wd.authn.isu": "{{isu}}",
  "wd.authn.clientId": "{{clientId}}",
  "wd.authn.accessTokenEndpoint": "https://{{host}}/ccx/oauth2/{{tenant}}/token",
  "wd.authn.privateKey": "-----BEGIN PRIVATE KEY-----\n{{key}}\n-----END PRIVATE KEY-----"
}
```

Create the secret with the following command.

```bash
aws secretsmanager create-secret --region {{region}} --name {{name}} --secret-string file://secret.json
```

### Create an IAM role for the connector
<a name="connectors-workday-ldq-setup-role"></a>

Create an IAM role for the connector. AWS Glue uses the role to retrieve the secret and validate the connection. Lake Formation uses the role when you register the connection. The connector uses the role at query time to read the secret and write to the spill location.

Create a file named `trust-policy.json` that allows AWS Glue and Lake Formation to assume the role.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "glue.amazonaws.com",
          "lakeformation.amazonaws.com"
        ]
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "{{account}}"
        }
      }
    }
  ]
}
```

Create a file named `permissions-policy.json` that grants the role access to the secret, the Glue connection, Lake Formation, the managed connector, and the spill bucket.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Secret",
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:us-east-1:123456789012:secret:secretName-AbCdEf"
    },
    {
      "Sid": "GlueConnection",
      "Effect": "Allow",
      "Action": [
        "glue:GetConnection",
        "glue:GetConnections"
      ],
      "Resource": "*"
    },
    {
      "Sid": "LakeFormationDataAccess",
      "Effect": "Allow",
      "Action": "lakeformation:GetDataAccess",
      "Resource": "*"
    },
    {
      "Sid": "ManagedConnector",
      "Effect": "Allow",
      "Action": "glue:ManagedConnector",
      "Resource": "*"
    },
    {
      "Sid": "SpillBucket",
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket",
        "s3:GetBucketLocation"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket",
        "arn:aws:s3:::amzn-s3-demo-bucket/*"
      ]
    }
  ]
}
```

Create the role and attach the permissions policy with the following commands.

```bash
aws iam create-role --role-name {{role}} --assume-role-policy-document file://trust-policy.json

aws iam put-role-policy --role-name {{role}} --policy-name WorkdayLDQConnectorAccess --policy-document file://permissions-policy.json
```

**Note**  
The `glue:ManagedConnector` permission and the spill bucket permissions are required. Without them, queries fail at run time.

### Create the Glue connection
<a name="connectors-workday-ldq-setup-connection"></a>

Create the Glue connection of type `WORKDAYLDQ`. In `AthenaProperties`, set `MANAGED_CONNECTION` to `true` and specify a spill bucket. When `ValidateCredentials` is `true`, AWS Glue gets an access token from Workday and runs a test query before it creates the connection.

```bash
aws glue create-connection --region {{region}} --cli-input-json '{"ConnectionInput":{"Name":"{{name}}","ConnectionType":"WORKDAYLDQ","ConnectionProperties":{"HOST":"{{host}}","PORT":"443","ROLE_ARN":"arn:aws:iam::{{account}}:role/{{role}}"},"AthenaProperties":{"MANAGED_CONNECTION":"true","spill_bucket":"{{bucket}}","spill_prefix":"workday-ldq-spill"},"AuthenticationConfiguration":{"AuthenticationType":"CUSTOM","SecretArn":"{{secret-arn}}"},"ValidateCredentials":true,"ValidateForComputeEnvironments":["SPARK","ATHENA"]}}'
```

On success, the command returns `"CreateConnectionStatus":"READY"`.

### Register the connection with Lake Formation
<a name="connectors-workday-ldq-setup-register"></a>

Register the connection with Lake Formation. The connection ARN has the format `arn:aws:glue:{{region}}:{{account}}:connection/{{name}}`.

```bash
aws lakeformation register-resource --region {{region}} --resource-arn arn:aws:glue:{{region}}:{{account}}:connection/{{name}} --role-arn arn:aws:iam::{{account}}:role/{{role}} --with-federation --with-privileged-access
```

### Create the federated catalog
<a name="connectors-workday-ldq-setup-catalog"></a>

Create the federated catalog that points to the connection with the identifier `workday`. The catalog name that you choose is the name that you use in Athena.

```bash
aws glue create-catalog --region {{region}} --cli-input-json '{"Name":"{{catalog}}","CatalogInput":{"FederatedCatalog":{"Identifier":"workday","ConnectionName":"{{name}}"},"CreateDatabaseDefaultPermissions":[],"CreateTableDefaultPermissions":[]}}'
```

Verify the catalog with the following command. The `public` database contains your Workday tables.

```bash
aws glue get-databases --region {{region}} --catalog-id {{account}}:{{catalog}}
```

### Grant Lake Formation permissions
<a name="connectors-workday-ldq-setup-grant"></a>

Grant Lake Formation permissions to each IAM principal that queries Workday from Athena. Grant `DESCRIBE` on the `public` database and `SELECT` and `DESCRIBE` on all tables.

```bash
aws lakeformation grant-permissions --region {{region}} --principal DataLakePrincipalIdentifier={{principal}} --permissions DESCRIBE --resource '{"Database":{"CatalogId":"{{account}}:{{catalog}}","Name":"public"}}'

aws lakeformation grant-permissions --region {{region}} --principal DataLakePrincipalIdentifier={{principal}} --permissions SELECT DESCRIBE --resource '{"Table":{"CatalogId":"{{account}}:{{catalog}}","DatabaseName":"public","TableWildcard":{}}}'
```

To limit access to specific columns, grant `SELECT` on a `TableWithColumns` resource. To limit access to specific rows, create a data filter with a row filter expression and grant `SELECT` on the data filter. For more information, see [Data filtering and cell-level security in Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/data-filtering.html) in the *AWS Lake Formation Developer Guide*.

Each principal that queries Workday from Athena also needs IAM permissions to run Athena queries and to write to the Athena query result location. For example, attach the [AmazonAthenaFullAccess](https://docs.aws.amazon.com/athena/latest/ug/security-iam-awsmanpol.html#amazonathenafullaccess-managed-policy) managed policy to the principal. For more information, see [Identity and access management in Athena](https://docs.aws.amazon.com/athena/latest/ug/security-iam-athena.html) and [Specify a query result location](https://docs.aws.amazon.com/athena/latest/ug/query-results-specify-location.html).

**Note**  
Lake Formation data lake administrators can query the federated catalog without these grants. To confirm that your grants work as you intend, run a test query as a principal that isn't a data lake administrator.

## Running queries
<a name="connectors-workday-ldq-running-queries"></a>

In the Athena query editor, for **Data source**, choose your federated catalog, and then choose the `public` database. You can reference tables with three-part names in the format `"{{catalog}}"."{{database}}"."{{table}}"`. The Athena query result location must be in the same AWS Region as the federated catalog.

The following example query returns the columns and data types of a table.

```sql
SELECT column_name, data_type FROM "{{catalog}}".information_schema.columns WHERE table_schema = 'public' AND table_name = 'procurement_supplier';
```

The following example query returns rows from a table.

```sql
SELECT id, workday_id, display_id FROM "{{catalog}}"."public"."procurement_supplier" LIMIT 10;
```

## Data type support
<a name="connectors-workday-ldq-data-type-support"></a>

The following table shows the corresponding data types for Workday Live Data Query and Athena.



| Workday Live Data Query | Athena | 
| --- | --- | 
| Long (64-bit integer) | bigint | 
| Boolean | boolean | 
| String | varchar | 
| Date | date | 
| Timestamp (millisecond precision) | timestamp(3) | 
| Decimal | decimal(p,s). The precision and scale depend on the Workday field. For example, currency amounts use decimal(26,6). | 
| Multi-instance field | array(varchar) | 

To see the data type of each column, query `information_schema.columns`.

## Performance
<a name="connectors-workday-ldq-performance"></a>

For optimal performance, use filters in queries whenever possible and select only the columns that you need. The connector performs predicate pushdown to decrease the data scanned. `LIMIT` clauses and simple predicates are pushed down to Workday.

### LIMIT clauses
<a name="connectors-workday-ldq-performance-limit-clauses"></a>

A `LIMIT N` statement reduces the data scanned by the query. With `LIMIT N` pushdown, the connector returns only `N` rows to Athena.

### Predicates
<a name="connectors-workday-ldq-performance-predicates"></a>

A predicate is an expression in the `WHERE` clause of a SQL query that evaluates to a Boolean value and filters rows. The following operators support predicate pushdown.
+ **Boolean: **AND, OR
+ **Equality: **EQUAL, LESS\_THAN, LESS\_THAN\_OR\_EQUAL, GREATER\_THAN, GREATER\_THAN\_OR\_EQUAL, IS\_NULL
+ **Other: **IN, BETWEEN

Athena evaluates other expressions, such as `LIKE` patterns, after it reads data from the connector.

### Combined pushdown example
<a name="connectors-workday-ldq-performance-pushdown-example"></a>

For enhanced querying capabilities, combine the pushdown types, as in the following example.

```sql
SELECT id, display_id FROM "{{catalog}}"."public"."procurement_supplier" WHERE (id BETWEEN 1000 AND 2000 OR id IN (3000, 3001)) AND basic_worktag_only = false LIMIT 10;
```

## Additional resources
<a name="connectors-workday-ldq-additional-resources"></a>
+ [Get Started with Workday Live Data Query](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/workday-live-data-query-/workday-live-data-query.html) in the Workday documentation
+ [Data Cloud Catalog](https://doc.workday.com/admin-guide/en-us/workday-data-cloud/data-out/data-cloud-catalog.html) in the Workday documentation
+ [Connecting to Workday Live Data Query](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-workday.html) in the *AWS Glue User Guide*
+ [Use Amazon Athena Federated Query](federated-queries.md)
+ [Lake Formation permissions reference](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-reference.html) in the *AWS Lake Formation Developer Guide*
+ [Federate to Workday Data Connect](https://docs.aws.amazon.com/lake-formation/latest/dg/catalog-federation-workday.html) in the *AWS Lake Formation Developer Guide*