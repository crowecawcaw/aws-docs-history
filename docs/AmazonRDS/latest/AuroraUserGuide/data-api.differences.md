# Comparing Amazon RDS Data API behaviors for Aurora Serverless v2 and provisioned clusters with Aurora Serverless v1 clusters

The most recent enhancements to the Amazon RDS Data APIs make Data APIs available for clusters that use recent versions of PostgreSQL or MySQL engines. These clusters can be configured to use Aurora Serverless v2 or provisioned instance classes
such as `db.r6g` or `db.r6i`.

The following sections describe Amazon RDS Data API differences between
Aurora Serverless v2 and provisioned DB clusters, and Aurora Serverless v1 DB clusters.
Aurora Serverless v1 DB clusters use the `serverless` engine mode.
Provisioned DB clusters use the `provisioned` engine mode.
An Aurora Serverless v2 DB cluster also uses the `provisioned`
engine mode, and contains one or more Aurora Serverless v2 DB instances with the `db.serverless`
instance class.

## Maximum number of requests per second

**Aurora Serverless v1**

Data APIs can make up to 1,000 requests per second.

**Aurora Serverless v2**

Data APIs can make an unlimited number of requests per second.

## Enabling or disabling the Amazon RDS Data API on an existing database

###### Aurora Serverless v1

- **With the Amazon RDS API**– Use the `ModifyCluster` operation and specify `True` or `False`, as applicable, for the `EnableHttpEndpoint` parameter.
- **With the AWS CLI**– Use the `modify-db-cluster` operation with the `--enable-http-endpoint` or `--no-enable-http-endpoint` option, as applicable.

###### Aurora Serverless v2

- **With the Amazon RDS API**– Use the `EnableHttpEndpoint` and `DisableHttpEndpoint` operations.
- **With the AWS CLI**:Use the `enable-http-endpoint` and `disable-http-endpoint` operations.

## CloudTrail events

**Aurora Serverless v1**

Events from Data API calls are management events. These events are automatically included in a trail by default. For more information, see [Excluding Data API events from an AWS CloudTrail trail (Aurora Serverless v1 only)](logging-using-cloudtrail-data-api.md#logging-using-cloudtrail-data-api.excluding-cloudtrail-events "logging-using-cloudtrail-data-api.md#logging-using-cloudtrail-data-api.excluding-cloudtrail-events").

**Aurora Serverless v2**

Events from Data API calls are data events. These events are automatically excluded in a trail by default. For more information, see [Including Data API events in an AWS CloudTrail trail](logging-using-cloudtrail-data-api.md#logging-using-cloudtrail-data-api.including-cloudtrail-events "logging-using-cloudtrail-data-api.md#logging-using-cloudtrail-data-api.including-cloudtrail-events").

## Multistatement support

###### Aurora Serverless v1

- For Aurora MySQL, multistatements aren't supported.
- For Aurora PostgreSQL, multistatements return only the first query
  response.

**Aurora Serverless v2**

Multistatements aren't supported. Attempting to execute multiple statements in a single API call returns `“An error occurred (ValidationException) when calling the ExecuteStatement operation: Multistatements aren't supported.”`. To execute multiple statements, make separate `ExecuteStatement` API calls or use the `BatchExecuteStatement` for batch processing.

The following example shows the resulting error message from an API call that attempts to execute a multistatement.

```
 aws rds-data execute-statement \
    --resource-arn "arn:aws:rds:region:account:cluster:cluster-name" \
    --secret-arn "arn:aws:secretsmanager:region:account:secret:secret-name" \
    --database "your_database" \
    --sql "SELECT * FROM your_table; Select * FROM next_table;

                                "An error occurred (ValidationException) when calling the ExecuteStatement operation: Multistatements aren't supported.
```

The following example executes multiple statements with separate `ExecuteStatement` API calls.

```
aws rds-data execute-statement \
    --resource-arn "arn:aws:rds:region:account:cluster:cluster-name" \
    --secret-arn "arn:aws:secretsmanager:region:account:secret:secret-name" \
    --database "your_database" \
    --sql "SELECT * FROM your_table;"

aws rds-data execute-statement \
    --resource-arn "arn:aws:rds:region:account:cluster:cluster-name" \
    --secret-arn "arn:aws:secretsmanager:region:account:secret:secret-name" \
    --database "your_database" \
    --sql "SELECT * FROM next_table;"
```

## Concurrent requests for the same transaction ID

**Aurora Serverless v1**

Subsequent requests wait until the current request finishes. Your application needs to handle timeout errors if the waiting period is too long.

**Aurora Serverless v2**

When the Data API receives multiple requests with the same transaction ID, it immediately returns this error:

`DatabaseErrorException: Transaction is still running a query`

This error occurs in two situations:

- Your application makes asynchronous requests (like JavaScript promises) using the same transaction ID.
- A previous request with that transaction ID is still processing.

The following example shows all requests executed in parallel with `promise.all()`.

```
const api_calls = [];
for (let i = 0; i < 10; i++) {
api_calls.push(
    client.send(
    new ExecuteStatementCommand({
        ...params,
        sql: `insert into table_name values (i);`,
        transactionId
    })
    )
);
}
await Promise.all(api_calls);
```

To resolve this error, wait for the current request to finish before sending another request with the same transaction ID or remove the transaction ID to allow parallel requests.

The following example shows an API call that uses sequential execution with the same transaction ID.

```
 for (let i = 0; i < 10; i++) {
    await client.send(
    new ExecuteStatementCommand({
        ...params,
        sql: `insert into table_name values (i);`,
        transactionId
    })
    ).promise()
);
}
```

## BatchExecuteStatement behavior

For more information about `BatchExecuteStatement`, see [BatchExecuteStatement](../../../rdsdataservice/latest/APIReference/API_BatchExecuteStatement.md "../../../rdsdataservice/latest/APIReference/API_BatchExecuteStatement.md").

**Aurora Serverless v1**

The generated fields object in the update result includes inserted values.

###### Aurora Serverless v2

- For Aurora MySQL, the generated fields object in the update result includes inserted values.
- For Aurora PostgreSQL, the generated fields object is empty.

## ExecuteSQL behavior

For more information about `ExecuteSQL`, see [ExecuteSQL](../../../rdsdataservice/latest/APIReference/API_ExecuteSql.md "../../../rdsdataservice/latest/APIReference/API_ExecuteSql.md").

**Aurora Serverless v1**

The `ExecuteSQL` operation is deprecated.

**Aurora Serverless v2**

The `ExecuteSQL` operation isn't supported.

## ExecuteStatement behavior

For more information about `ExecuteStatement`, see [ExecuteStatement](../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md "../../../rdsdataservice/latest/APIReference/API_ExecuteStatement.md").

**Aurora Serverless v1**

The `ExecuteStatement` parameter supports the retrieval of multidimentional array columns and all advanced data types.

**Aurora Serverless v2**

The `ExecuteStatement` parameter doesn't support multidimensional array columns. It also doesn't support certain PostgreSQL data types, including geometric and monetary types. When a Data API encounters an unsupported data type, it returns this error– `UnsupportedResultException: The result contains the unsupported data type data_type`.

To work around this issue, cast the unsupported data type to `TEXT`. The following example casts an unsupported data type to `TEXT`.

```
SELECT custom_type::TEXT FROM my_table;--
ORSELECT CAST(custom_type AS TEXT) FROM my_table;
```

For a list of supported data types for each Aurora database engine, see [Data API operations reference](data-api.md#data-api-operations "data-api.md#data-api-operations").

## Schema parameter behavior

**Aurora Serverless v1**

The `Schema` paramater isn't supported. When you include the `Schema` parameter in an API call, the Data API ignores the parameter.

**Aurora Serverless v2**

The `Schema` parameter is deprecated. When you include the `Schema` parameter in an API call, the Data API returns this error– `ValidationException: The schema parameter isn't supported`. The following example shows a Data API call that returns the `ValidationException` error.

```
aws rds-data execute-statement \
--resource-arn "arn:aws:rds:region:account:cluster:cluster-name" \
--secret-arn "arn:aws:secretsmanager:region:account:secret:secret-name" \
--database "your_database" \
--schema "your_schema" \
--sql "SELECT * FROM your_table LIMIT 10"

```

To solve this issue, remove the `Schema` parameter from your API call.

The following example shows a Data API call with the `Schema` parameter removed.

```
aws rds-data execute-statement \
--resource-arn "arn:aws:rds:region:account:cluster:cluster-name" \
--secret-arn "arn:aws:secretsmanager:region:account:secret:secret-name" \
--database "your_database" \
--sql "SELECT * FROM your_table LIMIT 10"
```
