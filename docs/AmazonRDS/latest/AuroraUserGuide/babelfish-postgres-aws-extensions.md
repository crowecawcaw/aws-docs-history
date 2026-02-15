# Using Aurora PostgreSQL extensions with Babelfish

Aurora PostgreSQL provides extensions for working with other AWS services. These are optional extensions that
support various use cases, such as using Amazon S3 with your DB cluster for importing or exporting data.

- To import data from an Amazon S3 bucket to your Babelfish DB cluster, you set up the
  `aws_s3` Aurora PostgreSQL extension. This extension also lets you export data from
  your Aurora PostgreSQL DB cluster to an Amazon S3 bucket.
- AWS Lambda is a compute service that lets
  you run code without provisioning or managing servers. You can use Lambda functions to do things like
  process event notifications from your DB instance. To learn more about Lambda, see
  [What is AWS
  Lambda?](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") in the _AWS Lambda Developer Guide._ To invoke Lambda
  functions from your Babelfish DB cluster, you set up the
  `aws_lambda` Aurora PostgreSQL extension.
  To set up these extensions for your Babelfish cluster, you first need to grant permission
  to the internal Babelfish user to load the extensions. After granting permission, you can then load Aurora PostgreSQL extensions.

## Enabling Aurora PostgreSQL extensions in your Babelfish DB cluster

Before you can load the `aws_s3` or the `aws_lambda` extensions, you
grant the needed privileges to your Babelfish DB cluster.

The procedure following uses the `psql` PostgreSQL command line tool to
connect to the DB cluster. For more information, see [Using psql to connect to the DB
cluster](babelfish-connect-PostgreSQL.md#babelfish-connect-psql "babelfish-connect-PostgreSQL.md#babelfish-connect-psql"). You
can also use pgAdmin. For details, see [Using pgAdmin to connect to the DB
cluster](babelfish-connect-PostgreSQL.md#babelfish-connect-pgadmin "babelfish-connect-PostgreSQL.md#babelfish-connect-pgadmin").

This procedure loads both `aws_s3` and `aws_lambda`, one
after the other. You don't need to load both if you want to use only one of
these extensions. The `aws_commons` extension is required by each, and
it's loaded by default as shown in the output.

###### To set up your Babelfish DB cluster with privileges for the Aurora PostgreSQL

extensions

1. Connect to your Babelfish DB cluster. Use the name for the "master" user (-U) that you
   specified when you created the Babelfish DB cluster. The default
   (`postgres`) is shown in the examples.

For Linux, macOS, or Unix:

```
`psql -h `your-Babelfish.cluster.444455556666-us-east-1.rds.amazonaws.com` \
-U postgres \
-d babelfish_db \
-p 5432`
```

For Windows:

```
`psql -h `your-Babelfish.cluster.444455556666-us-east-1.rds.amazonaws.com` ^
-U postgres ^
-d babelfish_db ^
-p 5432`
```

The command responds with a prompt to enter the password for the user name (-U).

```
`Password:`
```

Enter the password for the user name (-U) for the DB cluster. When you successfully connect,
you see output similar to the following.

```
`psql (13.4)
SSL connection (protocol: TLSv1.3, cipher: TLS_AES_256_GCM_SHA384, bits: 256, compression: off)
Type "help" for help.`

`postgres=>`
```

2. Grant privileges to the internal Babelfish user to create and load extensions.

```
`babelfish_db=>` `GRANT rds_superuser TO master_dbo;`
`GRANT ROLE`
```

3. Create and load the `aws_s3` extension. The `aws_commons` extension is
   required, and it's installed automatically when the `aws_s3` is
   installed.

```
`babelfish_db=>` `create extension aws_s3 cascade;`
`NOTICE: installing required extension "aws_commons"
CREATE EXTENSION`
```

4. Create and load the `aws_lambda` extension.

```
`babelfish_db=>` `create extension aws_lambda cascade;`
`CREATE EXTENSION`
`babelfish_db=>`
```

## Using Babelfish with Amazon S3

If you don't already have an Amazon S3 bucket to use with your Babelfish DB cluster,
you can create one. For any Amazon S3 bucket that you want to use, you provide
access.

Before trying to import or export data using an Amazon S3 bucket, complete the
following one-time steps.

###### To set up access for your Babelfish DB instance to your Amazon S3 bucket

1. Create an Amazon S3 bucket for your Babelfish instance, if needed. To do so, follow the
   instructions in [Create a
   bucket](../../../AmazonS3/latest/userguide/CreatingABucket.md#creating-bucket "../../../AmazonS3/latest/userguide/CreatingABucket.md#creating-bucket") in the _Amazon Simple Storage Service User Guideguide-s3-user;_.
2. Upload files to your Amazon S3
   bucket. To do so, follow the steps in [Add an object to a
   bucket](../../../AmazonS3/latest/userguide/PuttingAnObjectInABucket.md#uploading-an-object-bucket "../../../AmazonS3/latest/userguide/PuttingAnObjectInABucket.md#uploading-an-object-bucket") in the _Amazon Simple Storage Service User Guideguide-s3-user;._
3. Set up permissions as needed:
   - To import data from Amazon S3, the Babelfish DB cluster needs permission to access the
     bucket. We recommend using an AWS Identity and Access Management (IAM) role and attaching
     an IAM policy to that role for your cluster. To do so, follow the
     steps in [Using an IAM role to access an
     Amazon S3 bucket](USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.ARNRole "USER_PostgreSQL.S3Import.md#USER_PostgreSQL.S3Import.ARNRole").
   - To export data from your Babelfish DB cluster, your cluster must be granted
     access to the Amazon S3 bucket. As with importing, we recommend using an
     IAM role and policy. To do so, follow the steps in [Setting up access to an Amazon S3
     bucket](postgresql-s3-export-access-bucket.md "postgresql-s3-export-access-bucket.md").

You can now use Amazon S3 with the `aws_s3` extension with your Babelfish
DB cluster.

###### To import data from Amazon S3 to Babelfish and to export Babelfish data to Amazon S3

1. Use the `aws_s3` extension with your Babelfish DB cluster.

When you do, make sure to reference the tables as they exist in the
context of PostgreSQL. That is, if you want to import into a
Babelfish table named `[database].[schema].[tableA]`,
refer to that table as `database_schema_tableA` in the
`aws_s3` function:

    * For an example of using an `aws_s3` function to import data,
     see [Importing data from Amazon S3 to your Aurora PostgreSQL DB cluster](USER_PostgreSQL.S3Import.md "USER_PostgreSQL.S3Import.md").
    * For examples of using `aws_s3` functions to export data, see
     [Exporting query data using the
     aws\_s3.query\_export\_to\_s3 function](postgresql-s3-export-examples.md "postgresql-s3-export-examples.md").

2. Make sure to reference Babelfish tables using PostgreSQL naming when using the
   `aws_s3` extension and Amazon S3, as shown in the following table.

| Babelfish table               | Aurora PostgreSQL table       |
| ----------------------------- | ----------------------------- |
| ``database`.`schema`.`table`` | ``database`_`schema`_`table`` |

To learn more about using Amazon S3 with Aurora PostgreSQL, see [Importing data from Amazon S3 into an Aurora PostgreSQL DB cluster](USER_PostgreSQL.md "USER_PostgreSQL.md") and
[Exporting data from an Aurora PostgreSQL DB cluster to Amazon S3](postgresql-s3-export.md "postgresql-s3-export.md").

## Using Babelfish with AWS Lambda

After the `aws_lambda` extension is loaded in your Babelfish DB cluster but
before you can invoke Lambda functions, you give Lambda access to your DB cluster by
following this procedure.

###### To set up access for your Babelfish DB cluster to work with Lambda

This procedure uses the AWS CLI to create the IAM policy and role, and associate these with the Babelfish DB cluster.

1. Create an IAM policy that allows access to Lambda from your Babelfish DB cluster.

```
aws iam create-policy  --policy-name `rds-lambda-policy` --policy-document '{
	"Version": "2012-10-17",
    "Statement": [
        {
        "Sid": "AllowAccessToExampleFunction",
        "Effect": "Allow",
        "Action": "lambda:InvokeFunction",
        "Resource": "arn:aws:lambda:``aws-region`:444455556666:function:my-function`"
        }
    ]
}'
```

2. Create an IAM role that the policy can assume at runtime.

```
aws iam create-role  --role-name `rds-lambda-role` --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "rds.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}'
```

3. Attach the policy to the role.

```
aws iam attach-role-policy \
    --policy-arn arn:aws:iam::`444455556666`:policy/`rds-lambda-policy` \
    --role-name `rds-lambda-role` --region `aws-region`

```

4. Attach the role to your Babelfish DB cluster

```
aws rds add-role-to-db-cluster \
       --db-cluster-identifier `my-cluster-name` \
       --feature-name Lambda \
       --role-arn  arn:aws:iam::`444455556666:role/rds-lambda-role`   \
       --region `aws-region`
```

After you complete these tasks, you can invoke your Lambda functions. For more information and examples of setting up AWS Lambda for Aurora PostgreSQL
DB cluster with AWS Lambda, see [Step 2: Configure IAM for your Aurora PostgreSQL DB cluster and AWS Lambda](PostgreSQL-Lambda.md#PostgreSQL-Lambda-access "PostgreSQL-Lambda.md#PostgreSQL-Lambda-access").

###### To invoke a Lambda function from your Babelfish DB cluster

AWS Lambda supports functions written in Java, Node.js, Python, Ruby, and other languages. If the function returns text when invoked,
you can invoke it from your Babelfish DB cluster. The following example is a placeholder python function that returns a greeting.

```
lambda_function.py
import json
def lambda_handler(event, context):
    #TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
```

Currently, Babelfish doesn't support JSON. If your function returns JSON, you use a wrapper to handle the JSON. For example, say that the `lambda_function.py` shown
preceding is stored in Lambda as `my-function`.

1. Connect to your Babelfish DB cluster using the `psql` client (or the pgAdmin client). For more information, see
   [Using psql to connect to the DB
   cluster](babelfish-connect-PostgreSQL.md#babelfish-connect-psql "babelfish-connect-PostgreSQL.md#babelfish-connect-psql").
2. Create the wrapper. This example uses PostgreSQL's procedural language for SQL, `PL/pgSQL`. To learn more,
   see [PL/pgSQL–SQL Procedural Language](https://www.postgresql.org/docs/13/plpgsql.html "https://www.postgresql.org/docs/13/plpgsql.html").

```
create or replace function master_dbo.lambda_wrapper()
returns text
language plpgsql
as
$$
declare
   r_status_code integer;
   r_payload text;
begin
   SELECT payload INTO r_payload
     FROM aws_lambda.invoke(  aws_commons.create_lambda_function_arn('my-function', 'us-east-1')
                            ,'{"body": "Hello from Postgres!"}'::json );
   return r_payload ;
end;
$$;
```

The function can now be run from the Babelfish TDS port (1433) or from the PostgreSQL
port (5433).

    1. To invoke (call) this function from your PostgreSQL port:



    ```
    SELECT * from aws_lambda.invoke(aws_commons.create_lambda_function_arn('my-function', 'us-east-1'), '{"body": "Hello from Postgres!"}'::json );


    ```

    The output is similar to the following:



    ```
    `status_code | payload | executed_version | log_result
    -------------+-------------------------------------------------------+------------------+------------
     200 | {"statusCode": 200, "body": "\"Hello from Lambda!\""} | $LATEST |
    (1 row)`
    ```
    2. To invoke (call) this function from the TDS port, connect to the port using the SQL Server `sqlcmd` command line client. For details,
     see [Using a SQL Server client to connect
     to your DB cluster](babelfish-connect-sqlserver.md "babelfish-connect-sqlserver.md").
     When connected, run the following:



    ```
    `1>` `select lambda_wrapper();`
    `2>` `go`

    ```

    The command returns output similar to the following:



    ```
    `{"statusCode": 200, "body": "\"Hello from Lambda!\""}`
    ```

To learn more about using Lambda with Aurora PostgreSQL,
see [Invoking an AWS Lambda function from an
Aurora PostgreSQL DB cluster](PostgreSQL-Lambda.md "PostgreSQL-Lambda.md"). For more information about working with Lambda functions, see
[Getting started with Lambda](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md")
in the _AWS Lambda Developer Guide._

## Using pg_stat_statements in Babelfish

Babelfish for Aurora PostgreSQL supports `pg_stat_statements` extension from 3.3.0. To learn more, see [pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html "https://www.postgresql.org/docs/current/pgstatstatements.html").

For details about the version of this extension supported by Aurora PostgreSQL, see [Extension versions](../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md "../AuroraPostgreSQLReleaseNotes/AuroraPostgreSQL.md").

### Creating pg_stat_statements extension

To turn on `pg_stat_statements`, you must turn on the Query identifier calculation. This is done automatically if `compute_query_id`
is set to `on` or `auto` in the parameter group. The default value of `compute_query_id` parameter is `auto`.
You also need to create this extension to turn on this feature. Use the following command to install the extension from T-SQL endpoint:

```

`1>`EXEC sp_execute_postgresql 'CREATE EXTENSION pg_stat_statements WITH SCHEMA sys';

```

You can access the query statistics using the following query:

```

`postgres=>`select * from pg_stat_statements;

```

###### Note

During installation, if you don't provide the schema name for the extension then by default it will create it in public schema.
To access it, you must use square brackets with schema qualifier as shown below:

```
`postgres=>`select * from [public].pg_stat_statements;
```

You can also create the extension from PSQL endpoint.

### Authorizing the extension

By default, you can see the statistics for queries performed within your T-SQL database without the need of any authorization.

To access query statistics created by others, you need to have `pg_read_all_stats` PostgreSQL role. Follow the steps mentioned below to construct GRANT pg_read_all_stats command.

1. In T-SQL, use the following query that returns the internal PG role name.

```
SELECT rolname FROM pg_roles WHERE oid = USER_ID();
```

2. Connect to Babelfish for Aurora PostgreSQL database with rds_superuser privilege and use the following command:

```
GRANT pg_read_all_stats TO <rolname_from_above_query>
```

###### Example

From T-SQL endpoint:

```
`1>`SELECT rolname FROM pg_roles WHERE oid = USER_ID();
`2>`go
```

```
`rolname
-------
master_dbo
(1 rows affected)`
```

From PSQL endpoint:

```
babelfish_db=# grant pg_read_all_stats to master_dbo;
```

```
`GRANT ROLE`
```

You can access the query statistics using the pg_stat_statements view:

```
`1>`create table t1(cola int);
`2>`go
`1>`insert into t1 values (1),(2),(3);
`2>`go
```

```
`(3 rows affected)`
```

```
`1>`select userid, dbid, queryid, query from pg_stat_statements;
`2>`go

```

```
`userid dbid queryid query
------ ---- ------- -----
37503 34582 6487973085327558478 select * from t1
37503 34582 6284378402749466286 SET QUOTED_IDENTIFIER OFF
37503 34582 2864302298511657420 insert into t1 values ($1),($2),($3)
10 34582 NULL <insufficient privilege>
37503 34582 5615368793313871642 SET TEXTSIZE 4096
37503 34582 639400815330803392 create table t1(cola int)
(6 rows affected)`

```

### Resetting query statistics

You can use `pg_stat_statements_reset()` to reset the statistics gathered so far by pg_stat_statements. To learn more, see
[pg_stat_statements](https://www.postgresql.org/docs/current/pgstatstatements.html " https://www.postgresql.org/docs/current/pgstatstatements.html"). It is currently supported through
PSQL endpoint only. Connect to Babelfish for Aurora PostgreSQL with `rds_superuser` privilege, use the following command:

```

SELECT pg_stat_statements_reset();
```

### Limitations

- Currently, `pg_stat_statements()` is not supported through T-SQL endpoint. `pg_stat_statements` view is the recommended way to gather the statistics.
- Some of the queries might be re-written by the T-SQL parser implemented by Aurora PostgreSQL engine, `pg_stat_statements` view will show the re-written query and
  not the original query.

Example

```
select next value for [dbo].[newCounter];
```

The above query is re-written as the following in the pg_stat_statements view.

```
select nextval($1);
```

- Based on the execution flow of the statements, some of the queries might not be tracked by pg_stat_statements and will not be visible in the view. This includes the following
  statements: `use dbname`, `goto`, `print`, `raise error`, `set`, `throw`, `declare cursor`.
- For CREATE LOGIN and ALTER LOGIN statements, query and queryid will not be shown. It will show insufficient privileges.
- `pg_stat_statements` view always contains the below two entries, as these are executed internally by `sqlcmd` client.
  - SET QUOTED_IDENTIFIER OFF
  - SET TEXTSIZE 4096

## Using pgvector in Babelfish

pgvector, an open-source extension, lets you search for similar data directly within your Postgres database.
Babelfish now supports this extension starting with versions 15.6 and 16.2.
For more information, [pgvector Open source Documentation](https://github.com/pgvector/pgvector "https://github.com/pgvector/pgvector").

### Prerequisites

To enable pgvector functionality, install the extension in sys schema using one of the following methods:

- Run the following command in sqlcmd client:

```
exec sys.sp_execute_postgresql 'CREATE EXTENSION vector WITH SCHEMA sys';
```

- Connect to `babelfish_db` and run the following command in psql client:

```
CREATE EXTENSION vector WITH SCHEMA sys;
```

###### Note

After installing the pgvector extension, the vector data type will only be available in new database connections you establish. Existing connections won't recognize the new data type.

### Supported Functionality

Babelfish extends the T-SQL functionality to support the following:

- Storing

Babelfish now supports vector datatype compatible syntax, enhancing its T-SQL compatibility. To learn more about storing data with pgvector,
see [Storing](https://github.com/pgvector/pgvector?tab=readme-ov-file#storing "https://github.com/pgvector/pgvector?tab=readme-ov-file#storing").

- Querying

Babelfish expands T-SQL expression support to include vector similarity operators. However, for all other queries, standard T-SQL syntax is still required.

###### Note

T-SQL doesn't support Array type, and the database drivers do not have any interface to handle them. As a workaround, Babelfish uses text strings (varchar/nvarchar) to store vector data.
For example, when you request a vector value [1,2,3], Babelfish will return a string '[1,2,3]' as the response. You can parse and split this string at application level as per your needs.

To learn more about querying data with pgvector,
see [Querying](https://github.com/pgvector/pgvector?tab=readme-ov-file#querying "https://github.com/pgvector/pgvector?tab=readme-ov-file#querying").

- Indexing

T-SQL `Create Index` now supports `USING INDEX_METHOD` syntax. You can now define similarity search operator to be used on a specific column when creating an index.

The grammar is also extended to support Vector similarity operations on the required column (Check column_name_list_with_order_for_vector grammar).

```
CREATE [UNIQUE] [clustered] [COLUMNSTORE] INDEX <index_name> ON <table_name> [USING vector_index_method] (<column_name_list_with_order_for_vector>)
Where column_name_list_with_order_for_vector is:
    <column_name> [ASC | DESC] [VECTOR_COSINE_OPS | VECTOR_IP_OPS | VECTOR_L2_OPS] (COMMA simple_column_name [ASC | DESC] [VECTOR_COSINE_OPS | VECTOR_IP_OPS | VECTOR_L2_OPS])
```

To learn more about indexing data with pgvector,
see [Indexing](https://github.com/pgvector/pgvector?tab=readme-ov-file#indexing "https://github.com/pgvector/pgvector?tab=readme-ov-file#indexing").

- Performance

      + Use `SET BABELFISH_STATISTICS PROFILE ON` to debug Query Plans from T-SQL endpoint.
      + Increase `max_parallel_workers_get_gather` using the `set_config` function supported in T-SQL.
      + Use `IVFFlat` for approximate searches. For more information, see [IVFFlat](https://github.com/pgvector/pgvector?tab=readme-ov-file#ivfflat "https://github.com/pgvector/pgvector?tab=readme-ov-file#ivfflat").

  To improve performance with pgvector,
  see [Performance](https://github.com/pgvector/pgvector?tab=readme-ov-file#performance "https://github.com/pgvector/pgvector?tab=readme-ov-file#performance").

### Limitations

- Babelfish doesn't support Full Text Search for Hybrid Search.
  For more information, see [Hybrid Search](https://github.com/pgvector/pgvector?tab=readme-ov-file#hybrid-search "https://github.com/pgvector/pgvector?tab=readme-ov-file#hybrid-search").
- Babelfish doesn't currently support re-indexing functionality. However, you can still use PostgreSQL endpoint to re-index.
  For more information, see [Vacuuming](https://github.com/pgvector/pgvector?tab=readme-ov-file#vacuuming "https://github.com/pgvector/pgvector?tab=readme-ov-file#vacuuming").

## Using Amazon Aurora machine learning with Babelfish

You can extend the capabilities of your Babelfish for Aurora PostgreSQL DB cluster by integrating it with Amazon Aurora machine learning. This seamless integration grants
you access to a range of powerful services like Amazon Comprehend or Amazon SageMaker AI or Amazon Bedrock, each tailored to address distinct machine learning needs.

As a Babelfish user, you can use existing knowledge of T-SQL syntax and semantics when working with Aurora machine learning. Follow the instructions provided in the AWS documentation for Aurora PostgreSQL.
For more information, see [Using Amazon Aurora machine learning with Aurora PostgreSQL](postgresql-ml.md "postgresql-ml.md").

### Prerequisites

- Before trying to set up your Babelfish for Aurora PostgreSQL DB cluster to use Aurora machine learning, you must understand the related requirements and prerequisites.
  For more information, see [Requirements for using Aurora machine learning with Aurora PostgreSQL](postgresql-ml.md#postgresql-ml-prereqs "postgresql-ml.md#postgresql-ml-prereqs").
- Make sure you install the `aws_ml` extension either using Postgres endpoint or the `sp_execute_postgresql` store procedure.

```
exec sys.sp_execute_postgresql 'Create Extension aws_ml'
```

###### Note

Currently Babelfish doesn't support cascade operations with `sp_execute_postgresql` in Babelfish. Since `aws_ml` relies on `aws_commons`,
you'll need to install it separately using Postgres endpoint.

```
create extension aws_common;
```

### Handling T-SQL syntax and semantics with `aws_ml` functions

The following examples explains how T-SQL syntax and semantics are applied to the Amazon ML services:

###### Example: aws_bedrock.invoke_model – A simple query using Amazon Bedrock functions

```
aws_bedrock.invoke_model(
   model_id      varchar,
   content_type  text,
   accept_type   text,
   model_input   text)
Returns Varchar(MAX)
```

The following example shows how to invoke a Anthropic Claude 2 model for Bedrock using invoke_model.

```

SELECT aws_bedrock.invoke_model (
    'anthropic.claude-v2', -- model_id
    'application/json', -- content_type
    'application/json', -- accept_type
    '{"prompt": "\n\nHuman:
    You are a helpful assistant that answers questions directly
    and only using the information provided in the context below.
    \nDescribe the answerin detail.\n\nContext: %s \n\nQuestion:
    %s \n\nAssistant:","max_tokens_to_sample":4096,"temperature"
    :0.5,"top_k":250,"top_p":0.5,"stop_sequences":[]}' -- model_input
);

```

###### Example: aws_comprehend.detect_sentiment – A simple query using Amazon Comprehend functions

```

aws_comprehend.detect_sentiment(
   input_text varchar,
   language_code varchar,
   max_rows_per_batch int)
Returns table (sentiment varchar, confidence real)

```

The following example shows how to invoke the Amazon Comprehend service.

```

select sentiment from aws_comprehend.detect_sentiment('This is great', 'en');

```

###### Example: aws_sagemaker.invoke_endpoint – A simple query using Amazon SageMaker functions

```
aws_sagemaker.invoke_endpoint(
  endpoint_name varchar,
  max_rows_per_batch int,
  VARIADIC model_input "any") -- Babelfish inherits PG's variadic parameter type
Rerurns Varchar(MAX)
```

Since model_input is marked as VARIADIC and of type “any”, users can pass a list of any length and any datatype to the function which will act as the input the input to the model.
The following example shows how to invoke the Amazon SageMaker service.

```

SELECT CAST (aws_sagemaker.invoke_endpoint(
    'sagemaker_model_endpoint_name',
    NULL,
    arg1, arg2 -- model inputs are separate arguments )
AS INT) -- cast the output to INT

```

For more detailed information on using Aurora machine learning with Aurora PostgreSQL, see [Using Amazon Aurora machine learning with Aurora PostgreSQL](postgresql-ml.md "postgresql-ml.md").

### Limitations

- While Babelfish doesn't allow creating arrays, it can still handle data that represents arrays. When you use functions like
  `aws_bedrock.invoke_model_get_embeddings` that return arrays, the results is delivered as a string containing the array elements.
