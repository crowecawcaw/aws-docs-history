

# Connection parameters
<a name="sagemaker-sql-extension-connection-properties"></a>

The following tables detail the supported Python properties for AWS Glue connections per data store.

## Amazon Redshift connection parameters
<a name="sagemaker-sql-extension-connection-properties-redshift"></a>

The following Python connection parameters are supported by AWS Glue connections to Amazon Redshift.


| Key | Type | Description | Constraints | Required | 
| --- | --- | --- | --- | --- | 
| auto\_create | Type: boolean | Indicates whether the user should be created if they do not exist. Defaults to false. | true, false | No | 
| aws\_secret\_arn | Type: string | The ARN of the secret used to retrieve the additional parameters for the connection. | Valid ARN | No | 
| cluster\_identifier | Type: string - maxLength: 63 | The cluster identifier of the Amazon Redshift cluster. | ^(?\!.\*—)[a-z][a-z0-9-]{0,61}[a-z0-9]$ | No | 
| database | Type: string - maxLength: 127 | The name of the database to connect to. |  | No | 
| database\_metadata\_current\_db\_only | Type: boolean | Indicates if the application supports multi-database datashare catalogs. Defaults to true to indicate that the application does not support multi-database datashare catalogs for backwards compatibility. | true, false | No | 
| db\_groups | Type: string | A comma-separated list of existing database group names that the db\_user joins for the current session. |  | No | 
| db\_user | Type: string | The user ID to use with Amazon Redshift. |  | No | 
| host | Type: string - maxLength: 256 | The hostname of the Amazon Redshift cluster. |  | No | 
| iam | Type: boolean | Flag to enable or disable IAM based authentication for a connection. Defaults to false. | true, false | No | 
| iam\_disable\_cache | Type: boolean | This option specifies whether the IAM credentials are cached. Defaults to true. This improves performance when requests to the API gateway are throttled. | true, false | No | 
| max\_prepared\_statements | Type: integer | The maximum number of prepared statements that can be open at once. |  | No | 
| numeric\_to\_float | Decimal to float | Specifies if NUMERIC datatype values will be converted from decimal. By default NUMERIC values are received as decimal.Decimal Python objects. Enabling this option is not recommended for use cases which prefer the most precision as results may be rounded. Please reference the Python documentation on [`decimal.Decimal`](https://docs.python.org/3/library/decimal.html#decimal-objects) to understand the tradeoffs between decimal.Decimal and float before enabling this option. Defaults to false. | true, false | No | 
| port | Type: integer | The port number of the Amazon Redshift cluster. | Range 1150-65535 | No | 
| profile | Type: string - maxLength: 256 | The name of the profile containing the credentials and setting used by the AWS CLI. |  | No | 
| region | Type: string | The AWS Region where the cluster is located. | Valid AWS Region | No | 
| serverless\_acct\_id | Type: string - maxLength: 256 | The AWS account ID that is associated with the Amazon Redshift serverless resource. |  | No | 
| serverless\_work\_group | Type: string - maxLength: 256 | The name of the work group for the Amazon Redshift serverless endpoint. |  | No | 
| ssl | Type: boolean | true if SSL is enabled. | true, false | No | 
| ssl\_mode | Type: enum[verify-ca, verify-full, null]) | The security of the connection to Amazon Redshift. verify-ca (SSL must be used and the server certificate must be verified.) and verify-full (SSL must be used. The server certificate must be verified and the server hostname must match the hostname attribute on the certificate.) are supported. For more information, see [Configuring security options for connections](https://docs.aws.amazon.com/redshift/latest/mgmt/connecting-ssl-support.html) in Amazon Redshift documentation. Defaults to verify-ca. | verify-ca, verify-full | No | 
| timeout | Type: integer | The number of seconds before the connection to the server times out. | 0 | No | 

## Athena connection parameters
<a name="sagemaker-sql-extension-connection-properties-athena"></a>

The following Python connection parameters are supported by AWS Glue connections to Athena.


| Key | Type | Description | Constraints | Required | 
| --- | --- | --- | --- | --- | 
| aws\_access\_key\_id | Type: string - maxLength: 256 | Specifies an AWS access key associated with an IAM account. We recommend storing this information in the aws\_secret. | Length 16-128 | No | 
| aws\_secret\_access\_key | Type: string - maxLength: 256 | Secret part of an AWS access key. We recommend storing this information in the aws\_secret. |  | No | 
| aws\_secret\_arn | Type: string | The ARN of the secret used to retrieve the additional parameters for the connection. | Valid ARN | No | 
| catalog\_name | Type: string - maxLength: 256 | The catalog that contains the databases and the tables that are accessed with the driver. For information about catalogs, see [DataCatalog](https://docs.aws.amazon.com/athena/latest/APIReference/API_DataCatalog.html). |  | No | 
| duration\_seconds | Type: number | The duration, in seconds, of the role session. This setting can have a value from 1 hour to 12 hours. By default the duration is set to 3600 seconds (1 hour).  | Range from 900 seconds (15 minutes) up to the maximum session duration setting for the role | No | 
| encryption\_option | Type: enum[SSE\_S3, SSE\_KMS, CSE\_KMS, null]) | Encryption at rest for Amazon S3. See the Encryption at rest section in [Athena guide](https://docs.aws.amazon.com/athena/latest/ug/encryption.html). | SSE\_S3, SSE\_KMS, CSE\_KMS | No | 
| kms\_key | Type: string - maxLength: 256 | AWS KMS key if using CSE\_KMS in encrytion\_option. |  | No | 
| poll\_interval | Type: number | Interval in seconds to poll the status of query results in Athena. |  | No | 
| profile\_name | Type: string - maxLength: 256 | The name of the AWS configuration profile whose credentials should be used to authenticate the request to Athena. |  | No | 
| region\_name | Type: string | The AWS Region where queries are run. | Valid AWS Region | No | 
| result\_reuse\_enable | Type: boolean | Enable the reuse of previous query result. | true, false | No | 
| result\_reuse\_minutes | Type: integer | Specifies, in minutes, the maximum age of a previous query result that Athena should consider for reuse. The default is 60. | >= 1 | No | 
| role\_arn | Type: string | Role to be used for running queries. | Valid ARN | No | 
| schema\_name | Type: string - maxLength: 256 | Name of the default schema to use for the database. |  | No | 
| s3\_staging\_dir | Type: string - maxLength: 1024 | The location in Amazon S3 where the query results are stored. |  | Either s3\_staging\_dir or work\_group is required | 
| work\_group | Type: string | The workgroup in which queries will run. For information about workgroups, see [WorkGroup](https://docs.aws.amazon.com/athena/latest/APIReference/API_WorkGroup.html). | ^[a-zA-Z0-9.\_-]{1,128}$ | Either s3\_staging\_dir or work\_group is required | 

## Snowflake connection parameters
<a name="sagemaker-sql-extension-connection-properties-snowflake"></a>

The following Python connection parameters are supported by AWS Glue connections to Snowflake.

Snowflake connection parameters


| Key | Type | Description | Constraints | Required | 
| --- | --- | --- | --- | --- | 
| account | Type: string - maxLength: 256 | The Snowflake account identifier. The account identifier does not include the snowflakecomputing.com suffix. |  | Yes | 
| arrow\_number\_to\_decimal | Type: boolean | False by default, which means that NUMBER column values are returned as double-precision floating point numbers (float64). Set this to True to return DECIMAL column values as decimal numbers (decimal.Decimal) when calling the fetch\_pandas\_all() and fetch\_pandas\_batches() methods. | true, false | No | 
| autocommit | Type: boolean | Defaults to false, which honors the Snowflake parameter AUTOCOMMIT. Set to true or false to enable or disable the autocommit mode in the session, respectively. | true, false | No | 
| aws\_secret\_arn | Type: string | The ARN of the secret used to retrieve the additional parameters for the connection. | Valid ARN | No | 
| client\_prefetch\_threads | Type: integer | The number of threads used to download the result sets (4 by default). Increasing the value improves the fetch performance but requires more memory. |  | No | 
| database | Type: string - maxLength: 256 | The name of the default database to use. |  | No | 
| login\_timeout | Type: integer | The timeout in seconds for the login request. Defaults to 60 seconds. The login request gives up after the timeout length if the HTTP response is not success. |  | No | 
| network\_timeout | Type: integer | The timeout in seconds for all other operations. Defaults to none (infinite). A general request gives up after the timeout length if the HTTP response is not success. |  | No | 
| paramstyle | Type: string - maxLength: 256 | Placeholder syntaxes used for parameter substitution when executing SQL queries from Python code. Defaults to pyformat for client side binding. Specify qmark or numeric to change the bind variable formats for server side binding. |  | No | 
| role | Type: string - maxLength: 256 | The name of the default role to use. |  | No | 
| schema | Type: string - maxLength: 256 | The name of the default schema to use for the database. |  | No | 
| timezone | Type: string - maxLength: 128 | None by default, which honors the Snowflake parameter TIMEZONE. Set to a valid time zone (such as America/Los\_Angeles) to set the session time zone. | Timezone in a format similar to America/Los\_Angeles | No | 
| validate\_default\_parameters | Type: boolean | Set to true to raise an exception if the specified database, schema, or warehouse doesn’t exist. Defaults to false. |  | No | 
| warehouse | Type: string - maxLength: 256 | The name of the default warehouse to use. |  | No | 