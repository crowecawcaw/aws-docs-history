# Neptune Query APIs

**Gremlin query actions:**

- [ExecuteGremlinQuery (action)](#ExecuteGremlinQuery "#ExecuteGremlinQuery")
- [ExecuteGremlinExplainQuery (action)](#ExecuteGremlinExplainQuery "#ExecuteGremlinExplainQuery")
- [ExecuteGremlinProfileQuery (action)](#ExecuteGremlinProfileQuery "#ExecuteGremlinProfileQuery")
- [ListGremlinQueries (action)](#ListGremlinQueries "#ListGremlinQueries")
- [GetGremlinQueryStatus (action)](#GetGremlinQueryStatus "#GetGremlinQueryStatus")
- [CancelGremlinQuery (action)](#CancelGremlinQuery "#CancelGremlinQuery")
  **openCypher query actions:**

- [ExecuteOpenCypherQuery (action)](#ExecuteOpenCypherQuery "#ExecuteOpenCypherQuery")
- [ExecuteOpenCypherExplainQuery (action)](#ExecuteOpenCypherExplainQuery "#ExecuteOpenCypherExplainQuery")
- [ListOpenCypherQueries (action)](#ListOpenCypherQueries "#ListOpenCypherQueries")
- [GetOpenCypherQueryStatus (action)](#GetOpenCypherQueryStatus "#GetOpenCypherQueryStatus")
- [CancelOpenCypherQuery (action)](#CancelOpenCypherQuery "#CancelOpenCypherQuery")
  **Query structures:**

- [QueryEvalStats (structure)](#QueryEvalStats "#QueryEvalStats")
- [GremlinQueryStatus (structure)](#GremlinQueryStatus "#GremlinQueryStatus")
- [GremlinQueryStatusAttributes (structure)](#GremlinQueryStatusAttributes "#GremlinQueryStatusAttributes")

## ExecuteGremlinQuery (action)

        The AWS CLI name for this API is: `execute-gremlin-query`.

This commands executes a Gremlin query. Amazon Neptune is compatible
with Apache TinkerPop3 and Gremlin, so you can use the Gremlin traversal language
to query the graph, as described under [The
Graph](https://tinkerpop.apache.org/docs/current/reference/#graph "https://tinkerpop.apache.org/docs/current/reference/#graph") in the Apache TinkerPop3 documentation. More details can also
be found in [Accessing
a Neptune graph with Gremlin](access-graph-gremlin.md "access-graph-gremlin.md").

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
enables one of the following IAM actions in that cluster, depending on the query:

- [neptune-db:ReadDataViaQuery](iam-dp-actions.md#readdataviaquery "iam-dp-actions.md#readdataviaquery")
- [neptune-db:WriteDataViaQuery](iam-dp-actions.md#writedataviaquery "iam-dp-actions.md#writedataviaquery")
- [neptune-db:DeleteDataViaQuery](iam-dp-actions.md#deletedataviaquery "iam-dp-actions.md#deletedataviaquery")

Note that the [neptune-db:QueryLanguage:Gremlin](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")
IAM condition key can be used in the policy document to restrict the use of Gremlin
queries (see [Condition
keys available in Neptune IAM data-access policy statements](iam-data-condition-keys.md "iam-data-condition-keys.md")).

**Request**

- **gremlinQuery**  (in the CLI: `--gremlin-query`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

Using this API, you can run Gremlin queries in string format much as you
can using the HTTP endpoint. The interface is compatible with whatever Gremlin
version your DB cluster is using (see the [Tinkerpop
client section](access-graph-gremlin-client.md#best-practices-gremlin-java-latest "access-graph-gremlin-client.md#best-practices-gremlin-java-latest") to determine which Gremlin releases your engine version
supports).

- **serializer**  (in the CLI: `--serializer`) –  a String, of type: `string` (a UTF-8 encoded string).

If non-null, the query results are returned in a serialized response message
in the format specified by this parameter. See the [GraphSON](https://tinkerpop.apache.org/docs/current/reference/#_graphson "https://tinkerpop.apache.org/docs/current/reference/#_graphson")
section in the TinkerPop documentation for a list of the formats that are currently
supported.

**Response**

- **meta**   – a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

Metadata about the Gremlin query.

- **requestId**   – a String, of type: `string` (a UTF-8 encoded string).

The unique identifier of the Gremlin query.

- **result**   – a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

The Gremlin query output from the server.

- **status**   – A [GremlinQueryStatusAttributes](#GremlinQueryStatusAttributes "#GremlinQueryStatusAttributes") object.

The status of the Gremlin query.

###### Errors

- [QueryTooLargeException](data-api-dp-errors.md#QueryTooLargeException "data-api-dp-errors.md#QueryTooLargeException")
- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [QueryLimitExceededException](data-api-dp-errors.md#QueryLimitExceededException "data-api-dp-errors.md#QueryLimitExceededException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [QueryLimitException](data-api-dp-errors.md#QueryLimitException "data-api-dp-errors.md#QueryLimitException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [CancelledByUserException](data-api-dp-errors.md#CancelledByUserException "data-api-dp-errors.md#CancelledByUserException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException "data-api-dp-errors.md#FailureByQueryException")
- [MemoryLimitExceededException](data-api-dp-errors.md#MemoryLimitExceededException "data-api-dp-errors.md#MemoryLimitExceededException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [MalformedQueryException](data-api-dp-errors.md#MalformedQueryException "data-api-dp-errors.md#MalformedQueryException")
- [ParsingException](data-api-dp-errors.md#ParsingException "data-api-dp-errors.md#ParsingException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException "data-api-dp-errors.md#TimeLimitExceededException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")
- [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException "data-api-dp-errors.md#ConcurrentModificationException")

## ExecuteGremlinExplainQuery (action)

        The AWS CLI name for this API is: `execute-gremlin-explain-query`.

Executes a Gremlin Explain query.

Amazon Neptune has added a Gremlin feature named `explain`
that provides is a self-service tool for understanding the execution approach
being taken by the Neptune engine for the query. You invoke it by adding an `explain`
parameter to an HTTP call that submits a Gremlin query.

The explain feature provides information about the logical structure
of query execution plans. You can use this information to identify potential
evaluation and execution bottlenecks and to tune your query, as explained in
[Tuning
Gremlin queries](gremlin-traversal-tuning.md "gremlin-traversal-tuning.md"). You can also use query hints to improve query execution
plans.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows one of the following IAM actions in that cluster, depending on the query:

- [neptune-db:ReadDataViaQuery](iam-dp-actions.md#readdataviaquery "iam-dp-actions.md#readdataviaquery")
- [neptune-db:WriteDataViaQuery](iam-dp-actions.md#writedataviaquery "iam-dp-actions.md#writedataviaquery")
- [neptune-db:DeleteDataViaQuery](iam-dp-actions.md#deletedataviaquery "iam-dp-actions.md#deletedataviaquery")

Note that the [neptune-db:QueryLanguage:Gremlin](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")
IAM condition key can be used in the policy document to restrict the use of Gremlin
queries (see [Condition
keys available in Neptune IAM data-access policy statements](iam-data-condition-keys.md "iam-data-condition-keys.md")).

**Request**

- **gremlinQuery**  (in the CLI: `--gremlin-query`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The Gremlin explain query string.

**Response**

- **output**   – a ReportAsText, of type: `blob` (a block of uninterpreted binary data).

A text blob containing the Gremlin explain result, as described in [Tuning
Gremlin queries](gremlin-traversal-tuning.md "gremlin-traversal-tuning.md").

###### Errors

- [QueryTooLargeException](data-api-dp-errors.md#QueryTooLargeException "data-api-dp-errors.md#QueryTooLargeException")
- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [QueryLimitExceededException](data-api-dp-errors.md#QueryLimitExceededException "data-api-dp-errors.md#QueryLimitExceededException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [QueryLimitException](data-api-dp-errors.md#QueryLimitException "data-api-dp-errors.md#QueryLimitException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [CancelledByUserException](data-api-dp-errors.md#CancelledByUserException "data-api-dp-errors.md#CancelledByUserException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException "data-api-dp-errors.md#FailureByQueryException")
- [MemoryLimitExceededException](data-api-dp-errors.md#MemoryLimitExceededException "data-api-dp-errors.md#MemoryLimitExceededException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [MalformedQueryException](data-api-dp-errors.md#MalformedQueryException "data-api-dp-errors.md#MalformedQueryException")
- [ParsingException](data-api-dp-errors.md#ParsingException "data-api-dp-errors.md#ParsingException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException "data-api-dp-errors.md#TimeLimitExceededException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")
- [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException "data-api-dp-errors.md#ConcurrentModificationException")

## ExecuteGremlinProfileQuery (action)

        The AWS CLI name for this API is: `execute-gremlin-profile-query`.

Executes a Gremlin Profile query, which runs a specified traversal, collects
various metrics about the run, and produces a profile report as output. See [Gremlin
profile API in Neptune](gremlin-profile-api.md "gremlin-profile-api.md") for details.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:ReadDataViaQuery](iam-dp-actions.md#readdataviaquery "iam-dp-actions.md#readdataviaquery")
IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:Gremlin](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")
IAM condition key can be used in the policy document to restrict the use of Gremlin
queries (see [Condition
keys available in Neptune IAM data-access policy statements](iam-data-condition-keys.md "iam-data-condition-keys.md")).

**Request**

- **chop**  (in the CLI: `--chop`) –  an Integer, of type: `integer` (a signed 32-bit integer).

If non-zero, causes the results string to be truncated at that number of
characters. If set to zero, the string contains all the results.

- **gremlinQuery**  (in the CLI: `--gremlin-query`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The Gremlin query string to profile.

- **indexOps**  (in the CLI: `--index-ops`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

If this flag is set to `TRUE`, the results include a detailed
report of all index operations that took place during query execution and serialization.

- **results**  (in the CLI: `--results`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

If this flag is set to `TRUE`, the query results are gathered
and displayed as part of the profile report. If `FALSE`, only the
result count is displayed.

- **serializer**  (in the CLI: `--serializer`) –  a String, of type: `string` (a UTF-8 encoded string).

If non-null, the gathered results are returned in a serialized response
message in the format specified by this parameter. See [Gremlin profile
API in Neptune](gremlin-profile-api.md "gremlin-profile-api.md") for more information.

**Response**

- **output**   – a ReportAsText, of type: `blob` (a block of uninterpreted binary data).

A text blob containing the Gremlin Profile result. See [Gremlin profile
API in Neptune](gremlin-profile-api.md "gremlin-profile-api.md") for details.

###### Errors

- [QueryTooLargeException](data-api-dp-errors.md#QueryTooLargeException "data-api-dp-errors.md#QueryTooLargeException")
- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [QueryLimitExceededException](data-api-dp-errors.md#QueryLimitExceededException "data-api-dp-errors.md#QueryLimitExceededException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [QueryLimitException](data-api-dp-errors.md#QueryLimitException "data-api-dp-errors.md#QueryLimitException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [CancelledByUserException](data-api-dp-errors.md#CancelledByUserException "data-api-dp-errors.md#CancelledByUserException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException "data-api-dp-errors.md#FailureByQueryException")
- [MemoryLimitExceededException](data-api-dp-errors.md#MemoryLimitExceededException "data-api-dp-errors.md#MemoryLimitExceededException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [MalformedQueryException](data-api-dp-errors.md#MalformedQueryException "data-api-dp-errors.md#MalformedQueryException")
- [ParsingException](data-api-dp-errors.md#ParsingException "data-api-dp-errors.md#ParsingException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException "data-api-dp-errors.md#TimeLimitExceededException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")
- [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException "data-api-dp-errors.md#ConcurrentModificationException")

## ListGremlinQueries (action)

        The AWS CLI name for this API is: `list-gremlin-queries`.

Lists active Gremlin queries. See [Gremlin
query status API](gremlin-api-status.md "gremlin-api-status.md") for details about the output.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:GetQueryStatus](iam-dp-actions.md#getquerystatus "iam-dp-actions.md#getquerystatus")
IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:Gremlin](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")
IAM condition key can be used in the policy document to restrict the use of Gremlin
queries (see [Condition
keys available in Neptune IAM data-access policy statements](iam-data-condition-keys.md "iam-data-condition-keys.md")).

**Request**

- **includeWaiting**  (in the CLI: `--include-waiting`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

If set to `TRUE`, the list returned includes waiting queries.
The default is `FALSE`;

**Response**

- **acceptedQueryCount**   – an Integer, of type: `integer` (a signed 32-bit integer).

The number of queries that have been accepted but not yet completed, including
queries in the queue.

- **queries**   – An array of [GremlinQueryStatus](#GremlinQueryStatus "#GremlinQueryStatus") objects.

A list of the current queries.

- **runningQueryCount**   – an Integer, of type: `integer` (a signed 32-bit integer).

The number of Gremlin queries currently running.

###### Errors

- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException "data-api-dp-errors.md#AccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException "data-api-dp-errors.md#FailureByQueryException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ParsingException](data-api-dp-errors.md#ParsingException "data-api-dp-errors.md#ParsingException")
- [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException "data-api-dp-errors.md#ReadOnlyViolationException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException "data-api-dp-errors.md#TimeLimitExceededException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")
- [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException "data-api-dp-errors.md#ConcurrentModificationException")

## GetGremlinQueryStatus (action)

        The AWS CLI name for this API is: `get-gremlin-query-status`.

Gets the status of a specified Gremlin query.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:GetQueryStatus](iam-dp-actions.md#getquerystatus "iam-dp-actions.md#getquerystatus")
IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:Gremlin](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")
IAM condition key can be used in the policy document to restrict the use of Gremlin
queries (see [Condition
keys available in Neptune IAM data-access policy statements](iam-data-condition-keys.md "iam-data-condition-keys.md")).

**Request**

- **queryId**  (in the CLI: `--query-id`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The unique identifier that identifies the Gremlin query.

**Response**

- **queryEvalStats**   – A [QueryEvalStats](#QueryEvalStats "#QueryEvalStats") object.

The evaluation status of the Gremlin query.

- **queryId**   – a String, of type: `string` (a UTF-8 encoded string).

The ID of the query for which status is being returned.

- **queryString**   – a String, of type: `string` (a UTF-8 encoded string).

The Gremlin query string.

###### Errors

- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException "data-api-dp-errors.md#AccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException "data-api-dp-errors.md#FailureByQueryException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ParsingException](data-api-dp-errors.md#ParsingException "data-api-dp-errors.md#ParsingException")
- [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException "data-api-dp-errors.md#ReadOnlyViolationException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException "data-api-dp-errors.md#TimeLimitExceededException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")
- [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException "data-api-dp-errors.md#ConcurrentModificationException")

## CancelGremlinQuery (action)

        The AWS CLI name for this API is: `cancel-gremlin-query`.

Cancels a Gremlin query. See [Gremlin
query cancellation](gremlin-api-status-cancel.md "gremlin-api-status-cancel.md") for more information.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:CancelQuery](iam-dp-actions.md#cancelquery "iam-dp-actions.md#cancelquery")
IAM action in that cluster.

**Request**

- **queryId**  (in the CLI: `--query-id`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The unique identifier that identifies the query to be canceled.

**Response**

- **status**   – a String, of type: `string` (a UTF-8 encoded string).

The status of the cancelation

###### Errors

- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException "data-api-dp-errors.md#FailureByQueryException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ParsingException](data-api-dp-errors.md#ParsingException "data-api-dp-errors.md#ParsingException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException "data-api-dp-errors.md#TimeLimitExceededException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")
- [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException "data-api-dp-errors.md#ConcurrentModificationException")

## _openCypher query actions:_

## ExecuteOpenCypherQuery (action)

        The AWS CLI name for this API is: `execute-open-cypher-query`.

Executes an openCypher query. See [Accessing
the Neptune Graph with openCypher](access-graph-opencypher.md "access-graph-opencypher.md") for more information.

Neptune supports building graph applications using openCypher, which
is currently one of the most popular query languages among developers working
with graph databases. Developers, business analysts, and data scientists like
openCypher's declarative, SQL-inspired syntax because it provides a familiar
structure in which to querying property graphs.

The openCypher language was originally developed by Neo4j, then open-sourced
in 2015 and contributed to the [openCypher
project](https://opencypher.org/ "https://opencypher.org/") under an Apache 2 open-source license.

Note that when invoking this operation in a Neptune cluster that has IAM
authentication enabled, the IAM user or role making the request must have a policy
attached that allows one of the following IAM actions in that cluster, depending
on the query:

- [neptune-db:ReadDataViaQuery](iam-dp-actions.md#readdataviaquery "iam-dp-actions.md#readdataviaquery")
- [neptune-db:WriteDataViaQuery](iam-dp-actions.md#writedataviaquery "iam-dp-actions.md#writedataviaquery")
- [neptune-db:DeleteDataViaQuery](iam-dp-actions.md#deletedataviaquery "iam-dp-actions.md#deletedataviaquery")

Note also that the [neptune-db:QueryLanguage:OpenCypher](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")
IAM condition key can be used in the policy document to restrict the use of openCypher
queries (see [Condition
keys available in Neptune IAM data-access policy statements](iam-data-condition-keys.md "iam-data-condition-keys.md")).

**Request**

- **openCypherQuery**  (in the CLI: `--open-cypher-query`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The openCypher query string to be executed.

- **parameters**  (in the CLI: `--parameters`) –  a String, of type: `string` (a UTF-8 encoded string).

The openCypher query parameters for query execution. See [Examples
of openCypher parameterized queries](opencypher-parameterized-queries.md "opencypher-parameterized-queries.md") for more information.

**Response**

- **results**   – _Required:_ a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

The openCypherquery results.

###### Errors

- [QueryTooLargeException](data-api-dp-errors.md#QueryTooLargeException "data-api-dp-errors.md#QueryTooLargeException")
- [InvalidNumericDataException](data-api-dp-errors.md#InvalidNumericDataException "data-api-dp-errors.md#InvalidNumericDataException")
- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [QueryLimitExceededException](data-api-dp-errors.md#QueryLimitExceededException "data-api-dp-errors.md#QueryLimitExceededException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [QueryLimitException](data-api-dp-errors.md#QueryLimitException "data-api-dp-errors.md#QueryLimitException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [CancelledByUserException](data-api-dp-errors.md#CancelledByUserException "data-api-dp-errors.md#CancelledByUserException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException "data-api-dp-errors.md#FailureByQueryException")
- [MemoryLimitExceededException](data-api-dp-errors.md#MemoryLimitExceededException "data-api-dp-errors.md#MemoryLimitExceededException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [MalformedQueryException](data-api-dp-errors.md#MalformedQueryException "data-api-dp-errors.md#MalformedQueryException")
- [ParsingException](data-api-dp-errors.md#ParsingException "data-api-dp-errors.md#ParsingException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException "data-api-dp-errors.md#TimeLimitExceededException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")
- [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException "data-api-dp-errors.md#ConcurrentModificationException")

## ExecuteOpenCypherExplainQuery (action)

        The AWS CLI name for this API is: `execute-open-cypher-explain-query`.

Executes an openCypher `explain` request. See [The
openCypher explain feature](access-graph-opencypher-explain.md "access-graph-opencypher-explain.md") for more information.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:ReadDataViaQuery](iam-dp-actions.md#readdataviaquery "iam-dp-actions.md#readdataviaquery")
IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:OpenCypher](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")
IAM condition key can be used in the policy document to restrict the use of openCypher
queries (see [Condition
keys available in Neptune IAM data-access policy statements](iam-data-condition-keys.md "iam-data-condition-keys.md")).

**Request**

- **explainMode**  (in the CLI: `--explain-mode`) –  _Required:_ an OpenCypherExplainMode, of type: `string` (a UTF-8 encoded string).

The openCypher `explain` mode. Can be one of: `static`,
`dynamic`, or `details`.

- **openCypherQuery**  (in the CLI: `--open-cypher-query`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The openCypher query string.

- **parameters**  (in the CLI: `--parameters`) –  a String, of type: `string` (a UTF-8 encoded string).

The openCypher query parameters.

**Response**

- **results**   – _Required:_ a Blob, of type: `blob` (a block of uninterpreted binary data).

A text blob containing the openCypher `explain` results.

###### Errors

- [QueryTooLargeException](data-api-dp-errors.md#QueryTooLargeException "data-api-dp-errors.md#QueryTooLargeException")
- [InvalidNumericDataException](data-api-dp-errors.md#InvalidNumericDataException "data-api-dp-errors.md#InvalidNumericDataException")
- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [QueryLimitExceededException](data-api-dp-errors.md#QueryLimitExceededException "data-api-dp-errors.md#QueryLimitExceededException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [QueryLimitException](data-api-dp-errors.md#QueryLimitException "data-api-dp-errors.md#QueryLimitException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [CancelledByUserException](data-api-dp-errors.md#CancelledByUserException "data-api-dp-errors.md#CancelledByUserException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException "data-api-dp-errors.md#FailureByQueryException")
- [MemoryLimitExceededException](data-api-dp-errors.md#MemoryLimitExceededException "data-api-dp-errors.md#MemoryLimitExceededException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [MalformedQueryException](data-api-dp-errors.md#MalformedQueryException "data-api-dp-errors.md#MalformedQueryException")
- [ParsingException](data-api-dp-errors.md#ParsingException "data-api-dp-errors.md#ParsingException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException "data-api-dp-errors.md#TimeLimitExceededException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")
- [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException "data-api-dp-errors.md#ConcurrentModificationException")

## ListOpenCypherQueries (action)

        The AWS CLI name for this API is: `list-open-cypher-queries`.

Lists active openCypher queries. See [Neptune
openCypher status endpoint](access-graph-opencypher-status.md "access-graph-opencypher-status.md") for more information.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:GetQueryStatus](iam-dp-actions.md#getquerystatus "iam-dp-actions.md#getquerystatus")
IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:OpenCypher](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")
IAM condition key can be used in the policy document to restrict the use of openCypher
queries (see [Condition
keys available in Neptune IAM data-access policy statements](iam-data-condition-keys.md "iam-data-condition-keys.md")).

**Request**

- **includeWaiting**  (in the CLI: `--include-waiting`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

When set to `TRUE` and other parameters are not present, causes
status information to be returned for waiting queries as well as for running queries.

**Response**

- **acceptedQueryCount**   – an Integer, of type: `integer` (a signed 32-bit integer).

The number of queries that have been accepted but not yet completed, including
queries in the queue.

- **queries**   – An array of [GremlinQueryStatus](#GremlinQueryStatus "#GremlinQueryStatus") objects.

A list of current openCypher queries.

- **runningQueryCount**   – an Integer, of type: `integer` (a signed 32-bit integer).

The number of currently running openCypher queries.

###### Errors

- [InvalidNumericDataException](data-api-dp-errors.md#InvalidNumericDataException "data-api-dp-errors.md#InvalidNumericDataException")
- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException "data-api-dp-errors.md#AccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException "data-api-dp-errors.md#FailureByQueryException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ParsingException](data-api-dp-errors.md#ParsingException "data-api-dp-errors.md#ParsingException")
- [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException "data-api-dp-errors.md#ReadOnlyViolationException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException "data-api-dp-errors.md#TimeLimitExceededException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")
- [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException "data-api-dp-errors.md#ConcurrentModificationException")

## GetOpenCypherQueryStatus (action)

        The AWS CLI name for this API is: `get-open-cypher-query-status`.

Retrieves the status of a specified openCypher query.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:GetQueryStatus](iam-dp-actions.md#getquerystatus "iam-dp-actions.md#getquerystatus")
IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:OpenCypher](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")
IAM condition key can be used in the policy document to restrict the use of openCypher
queries (see [Condition
keys available in Neptune IAM data-access policy statements](iam-data-condition-keys.md "iam-data-condition-keys.md")).

**Request**

- **queryId**  (in the CLI: `--query-id`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The unique ID of the openCypher query for which to retrieve the query status.

**Response**

- **queryEvalStats**   – A [QueryEvalStats](#QueryEvalStats "#QueryEvalStats") object.

The openCypher query evaluation status.

- **queryId**   – a String, of type: `string` (a UTF-8 encoded string).

The unique ID of the query for which status is being returned.

- **queryString**   – a String, of type: `string` (a UTF-8 encoded string).

The openCypher query string.

###### Errors

- [InvalidNumericDataException](data-api-dp-errors.md#InvalidNumericDataException "data-api-dp-errors.md#InvalidNumericDataException")
- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException "data-api-dp-errors.md#AccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException "data-api-dp-errors.md#FailureByQueryException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ParsingException](data-api-dp-errors.md#ParsingException "data-api-dp-errors.md#ParsingException")
- [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException "data-api-dp-errors.md#ReadOnlyViolationException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException "data-api-dp-errors.md#TimeLimitExceededException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")
- [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException "data-api-dp-errors.md#ConcurrentModificationException")

## CancelOpenCypherQuery (action)

        The AWS CLI name for this API is: `cancel-open-cypher-query`.

Cancels a specified openCypher query. See [Neptune
openCypher status endpoint](access-graph-opencypher-status.md "access-graph-opencypher-status.md") for more information.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:CancelQuery](iam-dp-actions.md#cancelquery "iam-dp-actions.md#cancelquery")
IAM action in that cluster.

**Request**

- **queryId**  (in the CLI: `--query-id`) –  _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The unique ID of the openCypher query to cancel.

- **silent**  (in the CLI: `--silent`) –  a Boolean, of type: `boolean` (a Boolean (true or false) value).

If set to `TRUE`, causes the cancelation of the openCypher
query to happen silently.

**Response**

- **payload**   – a Boolean, of type: `boolean` (a Boolean (true or false) value).

The cancelation payload for the openCypher query.

- **status**   – a String, of type: `string` (a UTF-8 encoded string).

The cancellation status of the openCypher query.

###### Errors

- [InvalidNumericDataException](data-api-dp-errors.md#InvalidNumericDataException "data-api-dp-errors.md#InvalidNumericDataException")
- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [FailureByQueryException](data-api-dp-errors.md#FailureByQueryException "data-api-dp-errors.md#FailureByQueryException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ParsingException](data-api-dp-errors.md#ParsingException "data-api-dp-errors.md#ParsingException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [TimeLimitExceededException](data-api-dp-errors.md#TimeLimitExceededException "data-api-dp-errors.md#TimeLimitExceededException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")
- [ConcurrentModificationException](data-api-dp-errors.md#ConcurrentModificationException "data-api-dp-errors.md#ConcurrentModificationException")

## _Query structures:_

## QueryEvalStats (structure)

Structure to capture query statistics such as how many queries are running,
accepted or waiting and their details.

###### Fields

- **cancelled** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Set to `TRUE` if the query was cancelled, or FALSE otherwise.

- **elapsed** – This is an Integer, of type: `integer` (a signed 32-bit integer).

The number of milliseconds the query has been running so far.

- **subqueries** – This is a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

The number of subqueries in this query.

- **waited** – This is an Integer, of type: `integer` (a signed 32-bit integer).

Indicates how long the query waited, in milliseconds.

## GremlinQueryStatus (structure)

Captures the status of a Gremlin query (see the [Gremlin query
status API](gremlin-api-status.md "gremlin-api-status.md") page).

###### Fields

- **queryEvalStats** – This is A [QueryEvalStats](#QueryEvalStats "#QueryEvalStats") object.

The query statistics of the Gremlin query.

- **queryId** – This is a String, of type: `string` (a UTF-8 encoded string).

The ID of the Gremlin query.

- **queryString** – This is a String, of type: `string` (a UTF-8 encoded string).

The query string of the Gremlin query.

## GremlinQueryStatusAttributes (structure)

Contains status components of a Gremlin query.

###### Fields

- **attributes** – This is a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

Attributes of the Gremlin query status.

- **code** – This is an Integer, of type: `integer` (a signed 32-bit integer).

The HTTP response code returned fro the Gremlin query request..

- **message** – This is a String, of type: `string` (a UTF-8 encoded string).

The status message.
