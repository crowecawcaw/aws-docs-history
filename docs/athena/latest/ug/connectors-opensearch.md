# Amazon Athena OpenSearch connector

OpenSearch Service

The Amazon Athena OpenSearch connector enables Amazon Athena to communicate with your OpenSearch
instances so that you can use SQL to query your OpenSearch data.

This connector can be registered with Glue Data Catalog as a federated catalog.
It supports data access controls defined in Lake Formation at the catalog, database, table, column, row, and tag levels. This connector uses Glue Connections to centralize configuration properties in Glue.

###### Note

Due to a known issue, the OpenSearch connector cannot be used with a VPC.

If you have Lake Formation enabled in your account, the IAM role for your Athena federated Lambda connector that you deployed in the AWS Serverless Application Repository must have read access in Lake Formation to the AWS Glue Data Catalog.

## Prerequisites

- Deploy the connector to your AWS account using the Athena console or the AWS Serverless Application Repository. For more information, see [Create a data source connection](connect-to-a-data-source.md "connect-to-a-data-source.md") or [Use the AWS Serverless Application Repository to deploy a data
  source connector](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md").

## Terms

The following terms relate to the OpenSearch connector.

- Domain – A name that this connector
  associates with the endpoint of your OpenSearch instance. The domain is also
  used as the database name. For OpenSearch instances defined within the
  Amazon OpenSearch Service, the domain is auto-discoverable. For other instances, you must
  provide a mapping between the domain name and endpoint.
- Index – A database table defined in your
  OpenSearch instance.
- Mapping – If an index is a database
  table, then the mapping is its schema (that is, the definitions of its fields
  and attributes).

This connector supports both metadata retrieval from the OpenSearch instance
and from the AWS Glue Data Catalog. If the connector finds a AWS Glue database and table that
match your OpenSearch domain and index names, the connector attempts to use
them for schema definition. We recommend that you create your AWS Glue table so
that it is a superset of all fields in your OpenSearch index.

- Document – A record within a database
  table.
- Data stream – Time based data that is
  composed of multiple backing indices. For more information, see [Data streams](https://opensearch.org/docs/latest/dashboards/im-dashboards/datastream/ "https://opensearch.org/docs/latest/dashboards/im-dashboards/datastream/") in the OpenSearch documentation and [Getting started with data streams](../../../opensearch-service/latest/developerguide/data-streams.md#data-streams-example "../../../opensearch-service/latest/developerguide/data-streams.md#data-streams-example") in the
  _Amazon OpenSearch Service Developer Guide_.

###### Note

Because data stream indices are internally created and managed by open
search, the connector chooses the schema mapping from the first available
index. For this reason, we strongly recommend setting up an AWS Glue table as a
supplemental metadata source. For more information, see [Setting up databases and tables in AWS Glue](#connectors-opensearch-setting-up-databases-and-tables-in-aws-glue "#connectors-opensearch-setting-up-databases-and-tables-in-aws-glue").

## Parameters

Use the parameters in this section to configure the OpenSearch connector.

###### Note

Athena data source connectors created on December 3, 2024 and later use AWS Glue connections.

The parameter names and definitions listed below are for Athena data source connectors created prior to December 3, 2024. These can differ from their corresponding [AWS Glue connection properties](../../../glue/latest/dg/connection-properties.md "../../../glue/latest/dg/connection-properties.md"). Starting December 3, 2024, use the parameters below only when you [manually deploy](connect-data-source-serverless-app-repo.md "connect-data-source-serverless-app-repo.md") an earlier version of an Athena data source connector.

We recommend that you configure a OpenSearch connector by using a Glue
connections object. To do this, set the `glue_connection`
environment variable of the OpenSearch connector Lambda to the name of the Glue
connection to use.

**Glue connections properties**

Use the following command to get the schema for a Glue connection object. This schema contains all the parameters that you can use to control your connection.

```
aws glue describe-connection-type --connection-type OPENSEARCH
```

**Lambda environment properties**

- glue_connection – Specifies the name of the Glue connection associated with the federated connector.

###### Note

- All connectors that use Glue connections must use AWS Secrets Manager to store credentials.
- The OpenSearch connector created using Glue connections does not support the use of a multiplexing handler.
- The OpenSearch connector created using Glue connections only supports `ConnectionSchemaVersion` 2.

- spill_bucket – Specifies the Amazon S3 bucket
  for data that exceeds Lambda function limits.
- spill_prefix – (Optional) Defaults to a
  subfolder in the specified `spill_bucket` called
  `athena-federation-spill`. We recommend that you
  configure an Amazon S3 [storage
  lifecycle](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") on this location to delete spills older than a
  predetermined number of days or hours.
- spill_put_request_headers – (Optional) A
  JSON encoded map of request headers and values for the Amazon S3
  `putObject` request that is used for spilling (for example,
  `{"x-amz-server-side-encryption" : "AES256"}`). For other
  possible headers, see [PutObject](../../../AmazonS3/latest/API/API_PutObject.md "../../../AmazonS3/latest/API/API_PutObject.md") in the
  _Amazon Simple Storage Service API Reference_.
- kms_key_id – (Optional) By default, any
  data that is spilled to Amazon S3 is encrypted using the AES-GCM authenticated
  encryption mode and a randomly generated key. To have your Lambda function use
  stronger encryption keys generated by KMS like
  `a7e63k4b-8loc-40db-a2a1-4d0en2cd8331`, you can specify a KMS key
  ID.
- disable_spill_encryption – (Optional)
  When set to `True`, disables spill encryption. Defaults to
  `False` so that data that is spilled to S3 is encrypted using
  AES-GCM – either using a randomly generated key or KMS to generate keys.
  Disabling spill encryption can improve performance, especially if your spill
  location uses [server-side
  encryption](../../../AmazonS3/latest/userguide/serv-side-encryption.md "../../../AmazonS3/latest/userguide/serv-side-encryption.md").
- disable_glue – (Optional) If present and set to true, the connector does not attempt to retrieve supplemental metadata from AWS Glue.
- query_timeout_cluster – The timeout
  period, in seconds, for cluster health queries used in the generation of
  parallel scans.
- query_timeout_search – The timeout
  period, in seconds, for search queries used in the retrieval of documents from
  an index.
- auto_discover_endpoint – Boolean. The
  default is `true`. When you use the Amazon OpenSearch Service and set this parameter
  to true, the connector can auto-discover your domains and endpoints by calling
  the appropriate describe or list API operations on the OpenSearch Service. For any other type
  of OpenSearch instance (for example, self-hosted), you must specify the
  associated domain endpoints in the `domain_mapping` variable. If
  `auto_discover_endpoint=true`, the connector uses AWS
  credentials to authenticate to the OpenSearch Service. Otherwise, the connector retrieves
  user name and password credentials from AWS Secrets Manager through the
  `domain_mapping` variable.
- domain_mapping – Used only when
  `auto_discover_endpoint` is set to false and defines the mapping
  between domain names and their associated endpoints. The
  `domain_mapping` variable can accommodate multiple OpenSearch
  endpoints in the following format:

```
domain1=endpoint1,domain2=endpoint2,domain3=endpoint3,...
```

For the purpose of authenticating to an OpenSearch endpoint, the connector
supports substitution strings injected using the format
`${SecretName}` with user name and password retrieved from
AWS Secrets Manager. The secret should be stored in the following JSON format:

```
{ "username": "your_username", "password": "your_password" }
```

The connector will automatically parse this JSON structure to retrieve the credentials.

###### Important

As a security best practice, don't use hardcoded credentials in your
environment variables or connection strings. For information about moving
your hardcoded secrets to AWS Secrets Manager, see [Move hardcoded
secrets to AWS Secrets Manager](../../../secretsmanager/latest/userguide/hardcoded.md "../../../secretsmanager/latest/userguide/hardcoded.md") in the
_AWS Secrets Manager User Guide_.

The following example uses the `opensearch-creds` secret.

```
movies=https://${opensearch-creds}:search-movies-ne...qu.us-east-1.es.amazonaws.com
```

At runtime, `${opensearch-creds}` is rendered as the user name and
password, as in the following example.

```
movies=https://myusername@mypassword:search-movies-ne...qu.us-east-1.es.amazonaws.com
```

In the `domain_mapping` parameter, each domain-endpoint pair can
use a different secret. The secret itself must be specified in the format
`user_name`@`password`.
Although the password may contain embedded `@` signs, the first
`@` serves as a separator from
`user_name`.

It is also important to note that the comma (,) and equal sign (=) are used by
this connector as separators for the domain-endpoint pairs. For this reason, you
should not use them anywhere inside the stored secret.

## Setting up databases and tables in AWS Glue

The connector obtains metadata information by using AWS Glue or OpenSearch. You can set
up an AWS Glue table as a supplemental metadata definition source. To enable this feature,
define a AWS Glue database and table that match the domain and index of the source that you
are supplementing. The connector can also take advantage of metadata definitions stored
in the OpenSearch instance by retrieving the mapping for the specified index.

### Defining metadata for arrays in OpenSearch

OpenSearch does not have a dedicated array data type. Any field can contain zero
or more values so long as they are of the same data type. If you want to use
OpenSearch as your metadata definition source, you must define a
`_meta` property for all indices used with Athena for the fields that
to be considered a list or array. If you fail to complete this step, queries return
only the first element in the list field. When you specify the `_meta`
property, field names should be fully qualified for nested JSON structures (for
example, `address.street`, where `street` is a nested field
inside an `address` structure).

The following example defines `actor` and `genre` lists in
the `movies` table.

```
PUT movies/_mapping
{
  "_meta": {
    "actor": "list",
    "genre": "list"
  }
}
```

### Data types

The OpenSearch connector can extract metadata definitions from either AWS Glue or
the OpenSearch instance. The connector uses the mapping in the following table to
convert the definitions to Apache Arrow data types, including the points noted in
the section that follows.

| OpenSearch                                                                                                                                                                                                                     | Apache Arrow | AWS Glue          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------ | ----------------- |
| text, keyword, binary                                                                                                                                                                                                          | VARCHAR      | string            |
| long                                                                                                                                                                                                                           | BIGINT       | bigint            |
| scaled_float                                                                                                                                                                                                                   | BIGINT       | SCALED_FLOAT(...) |
| integer                                                                                                                                                                                                                        | INT          | int               |
| short                                                                                                                                                                                                                          | SMALLINT     | smallint          |
| byte                                                                                                                                                                                                                           | TINYINT      | tinyint           |
| double                                                                                                                                                                                                                         | FLOAT8       | double            |
| float, half_float                                                                                                                                                                                                              | FLOAT4       | float             |
| boolean                                                                                                                                                                                                                        | BIT          | boolean           |
| date, date_nanos                                                                                                                                                                                                               | DATEMILLI    | timestamp         |
| JSON structure                                                                                                                                                                                                                 | STRUCT       | STRUCT            |
| \_meta (for information, see the section [Defining metadata for arrays in OpenSearch](#connectors-opensearch-defining-metadata-for-arrays-in-opensearch "#connectors-opensearch-defining-metadata-for-arrays-in-opensearch").) | LIST         | ARRAY             |

#### Notes on data types

- Currently, the connector supports only the OpenSearch and AWS Glue
  data-types listed in the preceding table.
- A `scaled_float` is a floating-point number scaled by a
  fixed double scaling factor and represented as a `BIGINT` in
  Apache Arrow. For example, 0.756 with a scaling factor of 100 is rounded
  to 76.
- To define a `scaled_float` in AWS Glue, you must select the
  `array` column type and declare the field using the
  format SCALED_FLOAT(`scaling_factor`).

The following examples are valid:

```
SCALED_FLOAT(10.51)
SCALED_FLOAT(100)
SCALED_FLOAT(100.0)
```

The following examples are not valid:

```
SCALED_FLOAT(10.)
SCALED_FLOAT(.5)
```

- When converting from `date_nanos` to
  `DATEMILLI`, nanoseconds are rounded to the nearest
  millisecond. Valid values for `date` and
  `date_nanos` include, but are not limited to, the
  following formats:

```
"2020-05-18T10:15:30.123456789"
"2020-05-15T06:50:01.123Z"
"2020-05-15T06:49:30.123-05:00"
1589525370001 (epoch milliseconds)
```

- An OpenSearch `binary` is a string representation of a
  binary value encoded using `Base64` and is converted to a
  `VARCHAR`.

## Running SQL queries

The following are examples of DDL queries that you can use with this connector. In the
examples, `function_name` corresponds to the name of your Lambda
function, `domain` is the name of the domain that you want to
query, and `index` is the name of your index.

```
SHOW DATABASES in `lambda:`function_name``
```

```
SHOW TABLES in `lambda:`function_name``.`domain`
```

```
DESCRIBE `lambda:`function_name``.`domain`.`index`
```

## Performance

The Athena OpenSearch connector supports shard-based parallel scans. The connector
uses cluster health information retrieved from the OpenSearch instance to generate
multiple requests for a document search query. The requests are split for each shard and
run concurrently.

The connector also pushes down predicates as part of its document search queries. The
following example query and predicate shows how the connector uses predicate push
down.

**Query**

```
SELECT * FROM "lambda:elasticsearch".movies.movies
WHERE year >= 1955 AND year <= 1962 OR year = 1996
```

**Predicate**

```
(_exists_:year) AND year:([1955 TO 1962] OR 1996)
```

## Passthrough

queries

The OpenSearch connector supports [passthrough queries](federated-query-passthrough.md "federated-query-passthrough.md") and uses the
Query DSL language. For more information about querying with Query DSL, see [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html "https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html") in the Elasticsearch documentation or [Query DSL](https://opensearch.org/docs/latest/query-dsl/ "https://opensearch.org/docs/latest/query-dsl/") in the
OpenSearch documentation.

To use passthrough queries with the OpenSearch connector, use the following
syntax:

```
SELECT * FROM TABLE(
        system.query(
            schema => '`schema_name`',
            index => '`index_name`',
            query => "{`query_string`}"
        ))
```

The following OpenSearch example passthrough query filters for employees with active
employment status in the `employee` index of the `default`
schema.

```
SELECT * FROM TABLE(
        system.query(
            schema => 'default',
            index => 'employee',
            query => "{ ''bool'':{''filter'':{''term'':{''status'': ''active''}}}}"
        ))
```

## Additional resources

- For an article on using the Amazon Athena OpenSearch connector to query data in
  Amazon OpenSearch Service and Amazon S3 in a single query, see [Query data in Amazon OpenSearch Service using SQL from Amazon Athena](https://aws.amazon.com/blogs/big-data/query-data-in-amazon-opensearch-service-using-sql-from-amazon-athena/ "https://aws.amazon.com/blogs/big-data/query-data-in-amazon-opensearch-service-using-sql-from-amazon-athena/") in the
  _AWS Big Data Blog_.
- For additional information about this connector, visit [the corresponding site](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-elasticsearch "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-elasticsearch") on GitHub.com.
