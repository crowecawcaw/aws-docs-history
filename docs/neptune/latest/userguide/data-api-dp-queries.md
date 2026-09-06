

# Neptune Query APIs
<a name="data-api-dp-queries"></a>

**Gremlin query actions:**
+ [ExecuteGremlinQuery (action)](#ExecuteGremlinQuery)
+ [ExecuteGremlinExplainQuery (action)](#ExecuteGremlinExplainQuery)
+ [ExecuteGremlinProfileQuery (action)](#ExecuteGremlinProfileQuery)
+ [ListGremlinQueries (action)](#ListGremlinQueries)
+ [GetGremlinQueryStatus (action)](#GetGremlinQueryStatus)
+ [CancelGremlinQuery (action)](#CancelGremlinQuery)

**openCypher query actions:**
+ [ExecuteOpenCypherQuery (action)](#ExecuteOpenCypherQuery)
+ [ExecuteOpenCypherExplainQuery (action)](#ExecuteOpenCypherExplainQuery)
+ [ListOpenCypherQueries (action)](#ListOpenCypherQueries)
+ [GetOpenCypherQueryStatus (action)](#GetOpenCypherQueryStatus)
+ [CancelOpenCypherQuery (action)](#CancelOpenCypherQuery)

**Query structures:**
+ [QueryEvalStats (structure)](#QueryEvalStats)
+ [GremlinQueryStatus (structure)](#GremlinQueryStatus)
+ [GremlinQueryStatusAttributes (structure)](#GremlinQueryStatusAttributes)

## ExecuteGremlinQuery (action)
<a name="ExecuteGremlinQuery"></a>

         The AWS CLI name for this API is: `execute-gremlin-query`.

This commands executes a Gremlin query. Amazon Neptune is compatible with Apache TinkerPop3 and Gremlin, so you can use the Gremlin traversal language to query the graph, as described under [The Graph](https://tinkerpop.apache.org/docs/current/reference/#graph) in the Apache TinkerPop3 documentation. More details can also be found in [Accessing a Neptune graph with Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin.html).

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that enables one of the following IAM actions in that cluster, depending on the query:
+ [neptune-db:ReadDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery)
+ [neptune-db:WriteDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#writedataviaquery)
+ [neptune-db:DeleteDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletedataviaquery)

Note that the [neptune-db:QueryLanguage:Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

**Request**
+ **gremlinQuery**  (in the CLI: `--gremlin-query`) –  *Required:* a String, of type: `string` (a UTF-8 encoded string).

  Using this API, you can run Gremlin queries in string format much as you can using the HTTP endpoint. The interface is compatible with whatever Gremlin version your DB cluster is using (see the [Tinkerpop client section](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-gremlin-client.html#best-practices-gremlin-java-latest) to determine which Gremlin releases your engine version supports).
+ **serializer**  (in the CLI: `--serializer`) –  a String, of type: `string` (a UTF-8 encoded string).

  If non-null, the query results are returned in a serialized response message in the format specified by this parameter. See the [GraphSON](https://tinkerpop.apache.org/docs/current/reference/#_graphson) section in the TinkerPop documentation for a list of the formats that are currently supported.

**Response**
+ **meta**   – a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

  Metadata about the Gremlin query.
+ **requestId**   – a String, of type: `string` (a UTF-8 encoded string).

  The unique identifier of the Gremlin query.
+ **result**   – a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

  The Gremlin query output from the server.
+ **status**   – A [GremlinQueryStatusAttributes](#GremlinQueryStatusAttributes) object.

  The status of the Gremlin query.

**Errors**
+ [QueryTooLargeException](data-api-dp-errors.md#QueryTooLargeException)
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [QueryLimitExceededException](data-api-dp-errors.md#QueryLimitExceededException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [QueryLimitException](data-api-dp-errors.md#QueryLimitException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [CancelledByUserException](data-api-dp-errors.md#CancelledByUserException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException)
+ [MemoryLimitExceededException](data-api-dp-errors.md#MemoryLimitExceededException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [MalformedQueryException](data-api-dp-errors.md#MalformedQueryException)
+ [ParsingException](data-api-dp-errors.md#ParsingException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)
+ [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException)

## ExecuteGremlinExplainQuery (action)
<a name="ExecuteGremlinExplainQuery"></a>

         The AWS CLI name for this API is: `execute-gremlin-explain-query`.

Executes a Gremlin Explain query.

Amazon Neptune has added a Gremlin feature named `explain` that provides is a self-service tool for understanding the execution approach being taken by the Neptune engine for the query. You invoke it by adding an `explain` parameter to an HTTP call that submits a Gremlin query.

The explain feature provides information about the logical structure of query execution plans. You can use this information to identify potential evaluation and execution bottlenecks and to tune your query, as explained in [Tuning Gremlin queries](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-traversal-tuning.html). You can also use query hints to improve query execution plans.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows one of the following IAM actions in that cluster, depending on the query:
+ [neptune-db:ReadDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery)
+ [neptune-db:WriteDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#writedataviaquery)
+ [neptune-db:DeleteDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletedataviaquery)

Note that the [neptune-db:QueryLanguage:Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

**Request**
+ **gremlinQuery**  (in the CLI: `--gremlin-query`) –  *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The Gremlin explain query string.

**Response**
+ **output**   – a ReportAsText, of type: `blob` (a block of uninterpreted binary data).

  A text blob containing the Gremlin explain result, as described in [Tuning Gremlin queries](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-traversal-tuning.html).

**Errors**
+ [QueryTooLargeException](data-api-dp-errors.md#QueryTooLargeException)
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [QueryLimitExceededException](data-api-dp-errors.md#QueryLimitExceededException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [QueryLimitException](data-api-dp-errors.md#QueryLimitException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [CancelledByUserException](data-api-dp-errors.md#CancelledByUserException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException)
+ [MemoryLimitExceededException](data-api-dp-errors.md#MemoryLimitExceededException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [MalformedQueryException](data-api-dp-errors.md#MalformedQueryException)
+ [ParsingException](data-api-dp-errors.md#ParsingException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)
+ [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException)

## ExecuteGremlinProfileQuery (action)
<a name="ExecuteGremlinProfileQuery"></a>

         The AWS CLI name for this API is: `execute-gremlin-profile-query`.

Executes a Gremlin Profile query, which runs a specified traversal, collects various metrics about the run, and produces a profile report as output. See [Gremlin profile API in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html) for details.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:ReadDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery) IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

**Request**
+ **chop**  (in the CLI: `--chop`) –  an Integer, of type: `integer` (a signed 32-bit integer).

  If non-zero, causes the results string to be truncated at that number of characters. If set to zero, the string contains all the results.
+ **gremlinQuery**  (in the CLI: `--gremlin-query`) –  *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The Gremlin query string to profile.
+ **indexOps**  (in the CLI: `--index-ops`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

  If this flag is set to `TRUE`, the results include a detailed report of all index operations that took place during query execution and serialization.
+ **results**  (in the CLI: `--results`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

  If this flag is set to `TRUE`, the query results are gathered and displayed as part of the profile report. If `FALSE`, only the result count is displayed.
+ **serializer**  (in the CLI: `--serializer`) –  a String, of type: `string` (a UTF-8 encoded string).

  If non-null, the gathered results are returned in a serialized response message in the format specified by this parameter. See [Gremlin profile API in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html) for more information.

**Response**
+ **output**   – a ReportAsText, of type: `blob` (a block of uninterpreted binary data).

  A text blob containing the Gremlin Profile result. See [Gremlin profile API in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html) for details.

**Errors**
+ [QueryTooLargeException](data-api-dp-errors.md#QueryTooLargeException)
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [QueryLimitExceededException](data-api-dp-errors.md#QueryLimitExceededException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [QueryLimitException](data-api-dp-errors.md#QueryLimitException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [CancelledByUserException](data-api-dp-errors.md#CancelledByUserException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException)
+ [MemoryLimitExceededException](data-api-dp-errors.md#MemoryLimitExceededException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [MalformedQueryException](data-api-dp-errors.md#MalformedQueryException)
+ [ParsingException](data-api-dp-errors.md#ParsingException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)
+ [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException)

## ListGremlinQueries (action)
<a name="ListGremlinQueries"></a>

         The AWS CLI name for this API is: `list-gremlin-queries`.

Lists active Gremlin queries. See [Gremlin query status API](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-status.html) for details about the output.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetQueryStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getquerystatus) IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

**Request**
+ **includeWaiting**  (in the CLI: `--include-waiting`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

  If set to `TRUE`, the list returned includes waiting queries. The default is `FALSE`;

**Response**
+ **acceptedQueryCount**   – an Integer, of type: `integer` (a signed 32-bit integer).

  The number of queries that have been accepted but not yet completed, including queries in the queue.
+ **queries**   – An array of [GremlinQueryStatus](#GremlinQueryStatus) objects.

  A list of the current queries.
+ **runningQueryCount**   – an Integer, of type: `integer` (a signed 32-bit integer).

  The number of Gremlin queries currently running.

**Errors**
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [ParsingException](data-api-dp-errors.md#ParsingException)
+ [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)
+ [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException)

## GetGremlinQueryStatus (action)
<a name="GetGremlinQueryStatus"></a>

         The AWS CLI name for this API is: `get-gremlin-query-status`.

Gets the status of a specified Gremlin query.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetQueryStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getquerystatus) IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

**Request**
+ **queryId**  (in the CLI: `--query-id`) –  *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The unique identifier that identifies the Gremlin query.

**Response**
+ **queryEvalStats**   – A [QueryEvalStats](#QueryEvalStats) object.

  The evaluation status of the Gremlin query.
+ **queryId**   – a String, of type: `string` (a UTF-8 encoded string).

  The ID of the query for which status is being returned.
+ **queryString**   – a String, of type: `string` (a UTF-8 encoded string).

  The Gremlin query string.

**Errors**
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [ParsingException](data-api-dp-errors.md#ParsingException)
+ [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)
+ [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException)

## CancelGremlinQuery (action)
<a name="CancelGremlinQuery"></a>

         The AWS CLI name for this API is: `cancel-gremlin-query`.

Cancels a Gremlin query. See [Gremlin query cancellation](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-status-cancel.html) for more information.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:CancelQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelquery) IAM action in that cluster.

**Request**
+ **queryId**  (in the CLI: `--query-id`) –  *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The unique identifier that identifies the query to be canceled.

**Response**
+ **status**   – a String, of type: `string` (a UTF-8 encoded string).

  The status of the cancelation

**Errors**
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [ParsingException](data-api-dp-errors.md#ParsingException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)
+ [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException)

## *openCypher query actions:*
<a name="data-api-dp-queries-opencypher-query-actions-spacer"></a>

## ExecuteOpenCypherQuery (action)
<a name="ExecuteOpenCypherQuery"></a>

         The AWS CLI name for this API is: `execute-open-cypher-query`.

Executes an openCypher query. See [Accessing the Neptune Graph with openCypher](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher.html) for more information.

Neptune supports building graph applications using openCypher, which is currently one of the most popular query languages among developers working with graph databases. Developers, business analysts, and data scientists like openCypher's declarative, SQL-inspired syntax because it provides a familiar structure in which to querying property graphs.

The openCypher language was originally developed by Neo4j, then open-sourced in 2015 and contributed to the [openCypher project](https://opencypher.org/) under an Apache 2 open-source license.

Note that when invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows one of the following IAM actions in that cluster, depending on the query:
+ [neptune-db:ReadDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery)
+ [neptune-db:WriteDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#writedataviaquery)
+ [neptune-db:DeleteDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletedataviaquery)

Note also that the [neptune-db:QueryLanguage:OpenCypher](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of openCypher queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

**Request**
+ **openCypherQuery**  (in the CLI: `--open-cypher-query`) –  *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The openCypher query string to be executed.
+ **parameters**  (in the CLI: `--parameters`) –  a String, of type: `string` (a UTF-8 encoded string).

  The openCypher query parameters for query execution. See [Examples of openCypher parameterized queries](https://docs.aws.amazon.com/neptune/latest/userguide/opencypher-parameterized-queries.html) for more information.

**Response**
+ **results**   – *Required:* a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

  The openCypherquery results.

**Errors**
+ [QueryTooLargeException](data-api-dp-errors.md#QueryTooLargeException)
+ [InvalidNumericDataException](data-api-dp-errors.md#InvalidNumericDataException)
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [QueryLimitExceededException](data-api-dp-errors.md#QueryLimitExceededException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [QueryLimitException](data-api-dp-errors.md#QueryLimitException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [CancelledByUserException](data-api-dp-errors.md#CancelledByUserException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException)
+ [MemoryLimitExceededException](data-api-dp-errors.md#MemoryLimitExceededException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [MalformedQueryException](data-api-dp-errors.md#MalformedQueryException)
+ [ParsingException](data-api-dp-errors.md#ParsingException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)
+ [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException)

## ExecuteOpenCypherExplainQuery (action)
<a name="ExecuteOpenCypherExplainQuery"></a>

         The AWS CLI name for this API is: `execute-open-cypher-explain-query`.

Executes an openCypher `explain` request. See [The openCypher explain feature](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-explain.html) for more information.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:ReadDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery) IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:OpenCypher](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of openCypher queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

**Request**
+ **explainMode**  (in the CLI: `--explain-mode`) –  *Required:* an OpenCypherExplainMode, of type: `string` (a UTF-8 encoded string).

  The openCypher `explain` mode. Can be one of: `static`, `dynamic`, or `details`.
+ **openCypherQuery**  (in the CLI: `--open-cypher-query`) –  *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The openCypher query string.
+ **parameters**  (in the CLI: `--parameters`) –  a String, of type: `string` (a UTF-8 encoded string).

  The openCypher query parameters.

**Response**
+ **results**   – *Required:* a Blob, of type: `blob` (a block of uninterpreted binary data).

  A text blob containing the openCypher `explain` results.

**Errors**
+ [QueryTooLargeException](data-api-dp-errors.md#QueryTooLargeException)
+ [InvalidNumericDataException](data-api-dp-errors.md#InvalidNumericDataException)
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [QueryLimitExceededException](data-api-dp-errors.md#QueryLimitExceededException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [QueryLimitException](data-api-dp-errors.md#QueryLimitException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [CancelledByUserException](data-api-dp-errors.md#CancelledByUserException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException)
+ [MemoryLimitExceededException](data-api-dp-errors.md#MemoryLimitExceededException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [MalformedQueryException](data-api-dp-errors.md#MalformedQueryException)
+ [ParsingException](data-api-dp-errors.md#ParsingException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)
+ [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException)

## ListOpenCypherQueries (action)
<a name="ListOpenCypherQueries"></a>

         The AWS CLI name for this API is: `list-open-cypher-queries`.

Lists active openCypher queries. See [Neptune openCypher status endpoint](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-status.html) for more information.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetQueryStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getquerystatus) IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:OpenCypher](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of openCypher queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

**Request**
+ **includeWaiting**  (in the CLI: `--include-waiting`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

   When set to `TRUE` and other parameters are not present, causes status information to be returned for waiting queries as well as for running queries.

**Response**
+ **acceptedQueryCount**   – an Integer, of type: `integer` (a signed 32-bit integer).

  The number of queries that have been accepted but not yet completed, including queries in the queue.
+ **queries**   – An array of [GremlinQueryStatus](#GremlinQueryStatus) objects.

  A list of current openCypher queries.
+ **runningQueryCount**   – an Integer, of type: `integer` (a signed 32-bit integer).

  The number of currently running openCypher queries.

**Errors**
+ [InvalidNumericDataException](data-api-dp-errors.md#InvalidNumericDataException)
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [ParsingException](data-api-dp-errors.md#ParsingException)
+ [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)
+ [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException)

## GetOpenCypherQueryStatus (action)
<a name="GetOpenCypherQueryStatus"></a>

         The AWS CLI name for this API is: `get-open-cypher-query-status`.

Retrieves the status of a specified openCypher query.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetQueryStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getquerystatus) IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:OpenCypher](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of openCypher queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html)).

**Request**
+ **queryId**  (in the CLI: `--query-id`) –  *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The unique ID of the openCypher query for which to retrieve the query status.

**Response**
+ **queryEvalStats**   – A [QueryEvalStats](#QueryEvalStats) object.

  The openCypher query evaluation status.
+ **queryId**   – a String, of type: `string` (a UTF-8 encoded string).

  The unique ID of the query for which status is being returned.
+ **queryString**   – a String, of type: `string` (a UTF-8 encoded string).

  The openCypher query string.

**Errors**
+ [InvalidNumericDataException](data-api-dp-errors.md#InvalidNumericDataException)
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [ParsingException](data-api-dp-errors.md#ParsingException)
+ [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)
+ [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException)

## CancelOpenCypherQuery (action)
<a name="CancelOpenCypherQuery"></a>

         The AWS CLI name for this API is: `cancel-open-cypher-query`.

Cancels a specified openCypher query. See [Neptune openCypher status endpoint](https://docs.aws.amazon.com/neptune/latest/userguide/access-graph-opencypher-status.html) for more information.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:CancelQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#cancelquery) IAM action in that cluster.

**Request**
+ **queryId**  (in the CLI: `--query-id`) –  *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The unique ID of the openCypher query to cancel.
+ **silent**  (in the CLI: `--silent`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

  If set to `TRUE`, causes the cancelation of the openCypher query to happen silently.

**Response**
+ **payload**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

  The cancelation payload for the openCypher query.
+ **status**   – a String, of type: `string` (a UTF-8 encoded string).

  The cancellation status of the openCypher query.

**Errors**
+ [InvalidNumericDataException](data-api-dp-errors.md#InvalidNumericDataException)
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [ParsingException](data-api-dp-errors.md#ParsingException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)
+ [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException)

## *Query structures:*
<a name="data-api-dp-queries-query-structures-spacer"></a>

## QueryEvalStats (structure)
<a name="QueryEvalStats"></a>

Structure to capture query statistics such as how many queries are running, accepted or waiting and their details.

**Fields**
+ **cancelled** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

  Set to `TRUE` if the query was cancelled, or FALSE otherwise.
+ **elapsed** – This is an Integer, of type: `integer` (a signed 32-bit integer).

  The number of milliseconds the query has been running so far.
+ **subqueries** – This is a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

  The number of subqueries in this query.
+ **waited** – This is an Integer, of type: `integer` (a signed 32-bit integer).

  Indicates how long the query waited, in milliseconds.

## GremlinQueryStatus (structure)
<a name="GremlinQueryStatus"></a>

Captures the status of a Gremlin query (see the [Gremlin query status API](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-api-status.html) page).

**Fields**
+ **queryEvalStats** – This is A [QueryEvalStats](#QueryEvalStats) object.

  The query statistics of the Gremlin query.
+ **queryId** – This is a String, of type: `string` (a UTF-8 encoded string).

  The ID of the Gremlin query.
+ **queryString** – This is a String, of type: `string` (a UTF-8 encoded string).

  The query string of the Gremlin query.

## GremlinQueryStatusAttributes (structure)
<a name="GremlinQueryStatusAttributes"></a>

Contains status components of a Gremlin query.

**Fields**
+ **attributes** – This is a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

  Attributes of the Gremlin query status.
+ **code** – This is an Integer, of type: `integer` (a signed 32-bit integer).

  The HTTP response code returned fro the Gremlin query request..
+ **message** – This is a String, of type: `string` (a UTF-8 encoded string).

  The status message.