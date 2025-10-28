# Neptune streams dataplane API

**Stream access actions:**

- [GetPropertygraphStream (action)](#GetPropertygraphStream "#GetPropertygraphStream")
  **Stream data structures:**

- [PropertygraphRecord (structure)](#PropertygraphRecord "#PropertygraphRecord")
- [PropertygraphData (structure)](#PropertygraphData "#PropertygraphData")

## GetPropertygraphStream (action)

        The AWS CLI name for this API is: `get-propertygraph-stream`.

Gets a stream for a property graph.

With the Neptune Streams feature, you can generate a complete sequence
of change-log entries that record every change made to your graph data as it happens.
`GetPropertygraphStream` lets you collect these change-log entries
for a property graph.

The Neptune streams feature needs to be enabled on your Neptune DBcluster.
To enable streams, set the [neptune_streams](parameters.md#parameters-db-cluster-parameters-neptune_streams "parameters.md#parameters-db-cluster-parameters-neptune_streams")
DB cluster parameter to `1`.

See [Capturing
graph changes in real time using Neptune streams](streams.md "streams.md").

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:GetStreamRecords](iam-dp-actions.md#getstreamrecords "iam-dp-actions.md#getstreamrecords")
IAM action in that cluster.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
enables one of the following IAM actions, depending on the query:

Note that you can restrict property-graph queries using the following
IAM context keys:

- [neptune-db:QueryLanguage:Gremlin](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")
- [neptune-db:QueryLanguage:OpenCypher](iam-data-condition-keys.md#iam-neptune-condition-keys "iam-data-condition-keys.md#iam-neptune-condition-keys")

See [Condition
keys available in Neptune IAM data-access policy statements](iam-data-condition-keys.md "iam-data-condition-keys.md")).

**Request**

- **commitNum**  (in the CLI: `--commit-num`) –  a Long, of type: `long` (a signed 64-bit integer).

The commit number of the starting record to read from the change-log stream.
This parameter is required when `iteratorType` is`AT_SEQUENCE_NUMBER`
or `AFTER_SEQUENCE_NUMBER`, and ignored when `iteratorType`
is `TRIM_HORIZON` or `LATEST`.

- **encoding**  (in the CLI: `--encoding`) –  an Encoding, of type: `string` (a UTF-8 encoded string).

If set to TRUE, Neptune compresses the response using gzip encoding.

- **iteratorType**  (in the CLI: `--iterator-type`) –  an IteratorType, of type: `string` (a UTF-8 encoded string).

Can be one of:

    + `AT_SEQUENCE_NUMBER`   –   Indicates
     that reading should start from the event sequence number specified jointly by
     the `commitNum` and `opNum` parameters.
    + `AFTER_SEQUENCE_NUMBER`   –   Indicates
     that reading should start right after the event sequence number specified jointly
     by the `commitNum` and `opNum` parameters.
    + `TRIM_HORIZON`   –   Indicates that reading
     should start at the last untrimmed record in the system, which is the oldest unexpired
     (not yet deleted) record in the change-log stream.
    + `LATEST`   –   Indicates that reading
     should start at the most recent record in the system, which is the latest unexpired
     (not yet deleted) record in the change-log stream.

- **limit**  (in the CLI: `--limit`) –  a GetPropertygraphStreamInputLimitLong, of type: `long` (a signed 64-bit integer), not less than 1 or more than 100000 ?st?s.

Specifies the maximum number of records to return. There is also a size
limit of 10 MB on the response that can't be modified and that takes precedence
over the number of records specified in the `limit` parameter. The
response does include a threshold-breaching record if the 10 MB limit was reached.

The range for `limit` is 1 to 100,000, with a default of 10.

- **opNum**  (in the CLI: `--op-num`) –  a Long, of type: `long` (a signed 64-bit integer).

The operation sequence number within the specified commit to start reading
from in the change-log stream data. The default is `1`.

**Response**

- **format**   – _Required:_ a String, of type: `string` (a UTF-8 encoded string).

Serialization format for the change records being returned. Currently,
the only supported value is `PG_JSON`.

- **lastEventId**   – _Required:_ It is a map array of key-value pairs where:

    Each key is a a String, of type: `string` (a UTF-8 encoded string).

    Each value is a a String, of type: `string` (a UTF-8 encoded string).

Sequence identifier of the last change in the stream response.

An event ID is composed of two fields: a `commitNum`, which
identifies a transaction that changed the graph, and an `opNum`,
which identifies a specific operation within that transaction:

```
"eventId": {
          "commitNum": 12,
          "opNum": 1
        }
```

- **lastTrxTimestampInMillis**   – _Required:_ a Long, of type: `long` (a signed 64-bit integer).

The time at which the commit for the transaction was requested, in milliseconds
from the Unix epoch.

- **records**   – _Required:_ An array of [PropertygraphRecord](#PropertygraphRecord "#PropertygraphRecord") objects.

An array of serialized change-log stream records included in the response.

- **totalRecords**   – _Required:_ an Integer, of type: `integer` (a signed 32-bit integer).

The total number of records in the response.

###### Errors

- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [ExpiredStreamException](data-api-dp-errors.md#ExpiredStreamException "data-api-dp-errors.md#ExpiredStreamException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [MemoryLimitExceededException](data-api-dp-errors.md#MemoryLimitExceededException "data-api-dp-errors.md#MemoryLimitExceededException")
- [StreamRecordsNotFoundException](data-api-dp-errors.md#StreamRecordsNotFoundException "data-api-dp-errors.md#StreamRecordsNotFoundException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ThrottlingException](data-api-dp-errors.md#ThrottlingException "data-api-dp-errors.md#ThrottlingException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")

## _Stream data structures:_

## PropertygraphRecord (structure)

Structure of a property graph record.

###### Fields

- **commitTimestampInMillis** – This is _Required:_ a Long, of type: `long` (a signed 64-bit integer).

The time at which the commit for the transaction was requested, in milliseconds
from the Unix epoch.

- **data** – This is _Required:_ A [PropertygraphData](#PropertygraphData "#PropertygraphData") object.

The serialized Gremlin or openCypher change record.

- **eventId** – This is _Required:_ It is a map array of key-value pairs where:

    Each key is a a String, of type: `string` (a UTF-8 encoded string).

    Each value is a a String, of type: `string` (a UTF-8 encoded string).

The sequence identifier of the stream change record.

- **isLastOp** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Only present if this operation is the last one in its transaction. If present,
it is set to true. It is useful for ensuring that an entire transaction is consumed.

- **op** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The operation that created the change.

## PropertygraphData (structure)

A Gremlin or openCypher change record.

###### Fields

- **from** – This is a String, of type: `string` (a UTF-8 encoded string).

If this is an edge (type = `e`), the ID of the corresponding
`from` vertex or source node.

- **id** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The ID of the Gremlin or openCypher element.

- **key** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The property name. For element labels, this is `label`.

- **to** – This is a String, of type: `string` (a UTF-8 encoded string).

If this is an edge (type = `e`), the ID of the corresponding
`to` vertex or target node.

- **type** – This is _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The type of this Gremlin or openCypher element. Must be one of:

    + **`v1`**   -  
     Vertex label for Gremlin, or node label for openCypher.
    + **`vp`**   -  
     Vertex properties for Gremlin, or node properties for openCypher.
    + **`e`**   -  
     Edge and edge label for Gremlin, or relationship and relationship type for openCypher.
    + **`ep`**   -  
     Edge properties for Gremlin, or relationship properties for openCypher.

- **value** – This is _Required:_ a Document, of type: `document` (a protocol-agnostic open content represented by a JSON-like data model).

This is a JSON object that contains a value field for the value itself, and
a datatype field for the JSON data type of that value:

```
"value": {
          "value": "(the new value"),
          "dataType": "(the JSON datatypenew value")
        }
```
