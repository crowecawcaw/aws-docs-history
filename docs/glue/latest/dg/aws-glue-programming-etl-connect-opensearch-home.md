# OpenSearch Service connections

You can use AWS Glue for Spark to read from and write to tables in OpenSearch Service in AWS Glue 4.0 and later versions. You can
define what to read from OpenSearch Service with an OpenSearch query. You connect to OpenSearch Service using HTTP basic authentication
credentials stored in AWS Secrets Manager through a AWS Glue connection. This feature is not compatible with OpenSearch Service serverless.

For more information about Amazon OpenSearch Service, see the [Amazon OpenSearch Service documentation](../../../opensearch-service.md "../../../opensearch-service.md").

## Configuring OpenSearch Service connections

To connect to OpenSearch Service from AWS Glue, you will need to create and store your OpenSearch Service credentials
in a AWS Secrets Manager secret, then associate that secret with a OpenSearch Service AWS Glue connection.

**Prerequisites:**

- Identify the domain endpoint, `aosEndpoint` and port,
  `aosPort` you would
  like to read from, or create the resource by following instructions in the Amazon OpenSearch Service documentation.
  For more information on creating a domain, see [Creating and managing
  Amazon OpenSearch Service domains](../../../opensearch-service/latest/developerguide/createupdatedomains.md "../../../opensearch-service/latest/developerguide/createupdatedomains.md") in the Amazon OpenSearch Service documentation.

An Amazon OpenSearch Service domain endpoint will have the following default form,
https://search-`domainName`-`unstructuredIdContent`.`region`.es.amazonaws.com.
For more information on identifying your domain endpoint, see [Creating and managing
Amazon OpenSearch Service domains](../../../opensearch-service/latest/developerguide/createupdatedomains.md "../../../opensearch-service/latest/developerguide/createupdatedomains.md") in the Amazon OpenSearch Service documentation.

Identify or generate HTTP basic authentication credentials, `aosUser` and
`aosPassword` for your domain.

###### To configure a connection to OpenSearch Service:

1. In AWS Secrets Manager, create a secret using your OpenSearch Service credentials.
   To create a secret in Secrets Manager, follow the tutorial available in [Create an AWS Secrets Manager secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the AWS Secrets Manager documentation.
   After creating the secret, keep the Secret name, `secretName` for the next step.
   - When selecting **Key/value pairs**, create a pair for
     the key `USERNAME` with the value `aosUser`.
   - When selecting **Key/value pairs**, create a pair for
     the key `PASSWORD` with the value `aosPassword`.

2. In the AWS Glue console, create a connection by following the steps in [Adding an AWS Glue connection](console-connections.md "console-connections.md").
   After creating the connection, keep the connection name, `connectionName`, for future use in AWS Glue.
   - When selecting a **Connection type**, select OpenSearch Service.
   - When selecting a Domain endpoint, provide `aosEndpoint`.
   - When selecting a port, provide `aosPort`.
   - When selecting an **AWS Secret**, provide `secretName`.

After creating a AWS Glue OpenSearch Service connection, you will need to perform the following steps before running your AWS Glue job:

- Grant the IAM role associated with your AWS Glue job permission to read `secretName`.
- In your AWS Glue job configuration, provide `connectionName` as an **Additional network connection**.

## Reading from OpenSearch Service indexes

**Prerequisites:**

- A OpenSearch Service index you would like to read from, `aosIndex`.
- A AWS Glue OpenSearch Service connection configured to provide auth and network location information. To acquire this, complete the steps in the previous procedure, _To configure a connection to OpenSearch Service_. You will need the name of the AWS Glue connection,
  `connectionName`.

This example reads an index from Amazon OpenSearch Service. You will need to provide the `pushdown` parameter.

For example:

```
opensearch_read = glueContext.create_dynamic_frame.from_options(
    connection_type="opensearch",
    connection_options={
        "connectionName": "`connectionName`",
        "opensearch.resource": "`aosIndex`",
        "pushdown": "true",
    }
)
```

You can also provide a query string to filter the results returned in your DynamicFrame. You will need to configure `opensearch.query`.

`opensearch.query` can take a URL query parameter string `queryString`
or a query DSL JSON object `queryObject`. For more information about the query DSL,
see [Query DSL](https://opensearch.org/docs/latest/query-dsl/index/ "https://opensearch.org/docs/latest/query-dsl/index/") in the OpenSearch
documentation. To provide a URL query parameter string, prepend `?q=` to your query, as you would
in a fully qualified URL. To provide a query DSL object, string escape the JSON object before providing
it.

For example:

```

            queryObject = "{ "query": { "multi_match": { "query": "Sample", "fields": [ "sample" ] } } }"
            queryString = "?q=`queryString`"

            opensearch_read_query = glueContext.create_dynamic_frame.from_options(
    connection_type="opensearch",
    connection_options={
        "connectionName": "`connectionName`",
        "opensearch.resource": "`aosIndex`",
        "opensearch.query": queryString,
        "pushdown": "true",
    }
)
```

For more information about how to build a query outside of its specific syntax, see [Query string
syntax](https://opensearch.org/docs/latest/query-dsl/full-text/query-string/#query-string-syntax "https://opensearch.org/docs/latest/query-dsl/full-text/query-string/#query-string-syntax") in the OpenSearch documentation.

When reading from OpenSearch collections that contain array type data, you must specify which fields are
array type in your method call using the `opensearch.read.field.as.array.include` parameter.

For example, when reading the following document, you will encounter the `genre` and `actor` array fields:

```
{
    "_index": "movies",
    "_id": "2",
    "_version": 1,
    "_seq_no": 0,
    "_primary_term": 1,
    "found": true,
    "_source": {
        "director": "Frankenheimer, John",
        "genre": [
            "Drama",
            "Mystery",
            "Thriller",
            "Crime"
        ],
        "year": 1962,
        "actor": [
            "Lansbury, Angela",
            "Sinatra, Frank",
            "Leigh, Janet",
            "Harvey, Laurence",
            "Silva, Henry",
            "Frees, Paul",
            "Gregory, James",
            "Bissell, Whit",
            "McGiver, John",
            "Parrish, Leslie",
            "Edwards, James",
            "Flowers, Bess",
            "Dhiegh, Khigh",
            "Payne, Julie",
            "Kleeb, Helen",
            "Gray, Joe",
            "Nalder, Reggie",
            "Stevens, Bert",
            "Masters, Michael",
            "Lowell, Tom"
        ],
        "title": "The Manchurian Candidate"
    }
}
```

In this case, you would include those field names in your method call. For example:

```
"opensearch.read.field.as.array.include": "genre,actor"
```

If your array field is nested inside of your document structure, refer to it using dot notation:
`"genre,actor,foo.bar.baz"`. This would specify an array `baz` included in your source
document through the embedded document `foo` containing the embedded document `bar`.

## Writing to OpenSearch Service tables

This example writes information from an existing DynamicFrame, `dynamicFrame` to
OpenSearch Service. If the index already has information, AWS Glue will append data from your DynamicFrame. You will need to provide the `pushdown` parameter.

**Prerequisites:**

- A OpenSearch Service table you would like to write to. You will need identification information for the table. Let's call this `tableName`.
- A AWS Glue OpenSearch Service connection configured to provide auth and network location information. To acquire this, complete the steps in the previous procedure, _To configure a connection to OpenSearch Service_. You will need the name of the AWS Glue connection,
  `connectionName`.

For example:

```
glueContext.write_dynamic_frame.from_options(
    frame=`dynamicFrame`,
    connection_type="opensearch",
    connection_options={
      "connectionName": "`connectionName`",
      "opensearch.resource": "`aosIndex`",
    },
)
```

## OpenSearch Service connection option reference

- `connectionName` — Required. Used for Read/Write. The name of a AWS Glue OpenSearch Service
  connection configured to provide auth and network location information to your connection method.
- `opensearch.resource` — Required. Used for Read/Write. Valid Values: OpenSearch index names. The name of the index your connection method will interact
  with.
- `opensearch.query` — Used for Read. Valid Values: String escaped JSON or, when this string begins with `?`, the search part of a URL. An OpenSearch query that filters what should be retrieved
  when reading. For more information on using this parameter, consult the previous section [Reading from OpenSearch Service indexes](#aws-glue-programming-etl-connect-opensearch-read "#aws-glue-programming-etl-connect-opensearch-read").
- `pushdown` — Required if. Used for Read. Valid Values: boolean. Instructs Spark to pass read queries down to OpenSearch so the database only returns relevant documents.
- `opensearch.read.field.as.array.include` — Required if reading array type data. Used for Read. Valid Values: comma separated lists of field names. Specifies fields to read as arrays from OpenSearch documents.
  For more information on using this parameter, consult the previous section [Reading from OpenSearch Service indexes](#aws-glue-programming-etl-connect-opensearch-read "#aws-glue-programming-etl-connect-opensearch-read").
