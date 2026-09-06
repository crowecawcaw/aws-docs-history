

# Neptune dataplane engine, fast reset, and general structure APIs
<a name="data-api-dp-environment-APIs"></a>

**Engine operations:**
+ [GetEngineStatus (action)](#GetEngineStatus)
+ [ExecuteFastReset (action)](#ExecuteFastReset)

**Engine operation structures:**
+ [QueryLanguageVersion (structure)](#QueryLanguageVersion)
+ [FastResetToken (structure)](#FastResetToken)

## GetEngineStatus (action)
<a name="GetEngineStatus"></a>

         The AWS CLI name for this API is: `get-engine-status`.

Retrieves the status of the graph database on the host.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetEngineStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getenginestatus) IAM action in that cluster.

**Request**
+ *No Request parameters.*

**Response**
+ **dbEngineVersion**   – a String, of type: `string` (a UTF-8 encoded string).

  Set to the Neptune engine version running on your DB cluster. If this engine version has been manually patched since it was released, the version number is prefixed by `Patch-`.
+ **dfeQueryEngine**   – a String, of type: `string` (a UTF-8 encoded string).

  Set to `enabled` if the DFE engine is fully enabled, or to `viaQueryHint` (the default) if the DFE engine is only used with queries that have the `useDFE` query hint set to `true`.
+ **features**   – It is a map array of key-value pairs where:

      Each key is a a String, of type: `string` (a UTF-8 encoded string).

      Each value is a a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

  Contains status information about the features enabled on your DB cluster.
+ **gremlin**   – A [QueryLanguageVersion](#QueryLanguageVersion) object.

  Contains information about the Gremlin query language available on your cluster. Specifically, it contains a version field that specifies the current TinkerPop version being used by the engine.
+ **labMode**   – It is a map array of key-value pairs where:

      Each key is a a String, of type: `string` (a UTF-8 encoded string).

      Each value is a a String, of type: `string` (a UTF-8 encoded string).

  Contains Lab Mode settings being used by the engine.
+ **opencypher**   – A [QueryLanguageVersion](#QueryLanguageVersion) object.

  Contains information about the openCypher query language available on your cluster. Specifically, it contains a version field that specifies the current operCypher version being used by the engine.
+ **role**   – a String, of type: `string` (a UTF-8 encoded string).

  Set to `reader` if the instance is a read-replica, or to `writer` if the instance is the primary instance.
+ **rollingBackTrxCount**   – an Integer, of type: `integer` (a signed 32-bit integer).

  If there are transactions being rolled back, this field is set to the number of such transactions. If there are none, the field doesn't appear at all.
+ **rollingBackTrxEarliestStartTime**   – a String, of type: `string` (a UTF-8 encoded string).

  Set to the start time of the earliest transaction being rolled back. If no transactions are being rolled back, the field doesn't appear at all.
+ **settings**   – It is a map array of key-value pairs where:

      Each key is a a String, of type: `string` (a UTF-8 encoded string).

      Each value is a a String, of type: `string` (a UTF-8 encoded string).

  Contains information about the current settings on your DB cluster. For example, contains the current cluster query timeout setting (`clusterQueryTimeoutInMs`).
+ **sparql**   – A [QueryLanguageVersion](#QueryLanguageVersion) object.

  Contains information about the SPARQL query language available on your cluster. Specifically, it contains a version field that specifies the current SPARQL version being used by the engine.
+ **startTime**   – a String, of type: `string` (a UTF-8 encoded string).

  Set to the UTC time at which the current server process started.
+ **status**   – a String, of type: `string` (a UTF-8 encoded string).

  Set to `healthy` if the instance is not experiencing problems. If the instance is recovering from a crash or from being rebooted and there are active transactions running from the latest server shutdown, status is set to `recovery`.

**Errors**
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [InternalFailureException](data-api-dp-errors.md#InternalFailureException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)

## ExecuteFastReset (action)
<a name="ExecuteFastReset"></a>

         The AWS CLI name for this API is: `execute-fast-reset`.

The fast reset REST API lets you reset a Neptune graph quicky and easily, removing all of its data.

Neptune fast reset is a two-step process. First you call `ExecuteFastReset` with `action` set to `initiateDatabaseReset`. This returns a UUID token which you then include when calling `ExecuteFastReset` again with `action` set to `performDatabaseReset`. See [Empty an Amazon Neptune DB cluster using the fast reset API](https://docs.aws.amazon.com/neptune/latest/userguide/manage-console-fast-reset.html).

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:ResetDatabase](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#resetdatabase) IAM action in that cluster.

**Request**
+ **action**  (in the CLI: `--action`) –  *Required:* an Action, of type: `string` (a UTF-8 encoded string).

  The fast reset action. One of the following values:
  + **`initiateDatabaseReset`**   –   This action generates a unique token needed to actually perform the fast reset.
  + **`performDatabaseReset`**   –   This action uses the token generated by the `initiateDatabaseReset` action to actually perform the fast reset.

    
+ **token**  (in the CLI: `--token`) –  a String, of type: `string` (a UTF-8 encoded string).

  The fast-reset token to initiate the reset.

**Response**
+ **payload**   – A [FastResetToken](#FastResetToken) object.

  The `payload` is only returned by the `initiateDatabaseReset` action, and contains the unique token to use with the `performDatabaseReset` action to make the reset occur.
+ **status**   – *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The `status` is only returned for the `performDatabaseReset` action, and indicates whether or not the fast reset rquest is accepted.

**Errors**
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [ServerShutdownException](data-api-dp-errors.md#ServerShutdownException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [MethodNotAllowedException](data-api-dp-errors.md#MethodNotAllowedException)
+ [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)

## *Engine operation structures:*
<a name="data-api-dp-environment-APIs-engine-operation-structures-spacer"></a>

## QueryLanguageVersion (structure)
<a name="QueryLanguageVersion"></a>

Structure for expressing the query language version.

**Fields**
+ **version** – This is *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The version of the query language.

## FastResetToken (structure)
<a name="FastResetToken"></a>

A structure containing the fast reset token used to initiate a fast reset.

**Fields**
+ **token** – This is a String, of type: `string` (a UTF-8 encoded string).

  A UUID generated by the database in the `initiateDatabaseReset` action, and then consumed by the `performDatabaseReset` to reset the database.