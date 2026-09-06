

# Neptune dataplane statistics and graph summary APIs
<a name="data-api-dp-statistics"></a>

**Property graph statistics actions:**
+ [GetPropertygraphStatistics (action)](#GetPropertygraphStatistics)
+ [ManagePropertygraphStatistics (action)](#ManagePropertygraphStatistics)
+ [DeletePropertygraphStatistics (action)](#DeletePropertygraphStatistics)
+ [GetPropertygraphSummary (action)](#GetPropertygraphSummary)

**Statistics structures:**
+ [Statistics (structure)](#Statistics)
+ [StatisticsSummary (structure)](#StatisticsSummary)
+ [DeleteStatisticsValueMap (structure)](#DeleteStatisticsValueMap)
+ [RefreshStatisticsIdMap (structure)](#RefreshStatisticsIdMap)
+ [NodeStructure (structure)](#NodeStructure)
+ [EdgeStructure (structure)](#EdgeStructure)
+ [SubjectStructure (structure)](#SubjectStructure)
+ [PropertygraphSummaryValueMap (structure)](#PropertygraphSummaryValueMap)
+ [PropertygraphSummary (structure)](#PropertygraphSummary)

## GetPropertygraphStatistics (action)
<a name="GetPropertygraphStatistics"></a>

         The AWS CLI name for this API is: `get-propertygraph-statistics`.

Gets property graph statistics (Gremlin and openCypher).

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetStatisticsStatus](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getstatisticsstatus) IAM action in that cluster.

**Request**
+ *No Request parameters.*

**Response**
+ **payload**   – *Required:* A [Statistics](#Statistics) object.

  Statistics for property-graph data.
+ **status**   – *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP return code of the request. If the request succeeded, the code is 200. See [Common error codes for DFE statistics request](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-statistics.html#neptune-dfe-statistics-errors) for a list of common errors.

**Errors**
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [StatisticsNotAvailableException](data-api-dp-errors.md#StatisticsNotAvailableException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)

## ManagePropertygraphStatistics (action)
<a name="ManagePropertygraphStatistics"></a>

         The AWS CLI name for this API is: `manage-propertygraph-statistics`.

Manages the generation and use of property graph statistics.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:ManageStatistics](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#managestatistics) IAM action in that cluster.

**Request**
+ **mode**  (in the CLI: `--mode`) –  a StatisticsAutoGenerationMode, of type: `string` (a UTF-8 encoded string).

  The statistics generation mode. One of: `DISABLE_AUTOCOMPUTE`, `ENABLE_AUTOCOMPUTE`, or `REFRESH`, the last of which manually triggers DFE statistics generation.

**Response**
+ **payload**   – A [RefreshStatisticsIdMap](#RefreshStatisticsIdMap) object.

  This is only returned for refresh mode.
+ **status**   – *Required:* a String, of type: `string` (a UTF-8 encoded string).

  The HTTP return code of the request. If the request succeeded, the code is 200.

**Errors**
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [StatisticsNotAvailableException](data-api-dp-errors.md#StatisticsNotAvailableException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)

## DeletePropertygraphStatistics (action)
<a name="DeletePropertygraphStatistics"></a>

         The AWS CLI name for this API is: `delete-propertygraph-statistics`.

Deletes statistics for Gremlin and openCypher (property graph) data.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:DeleteStatistics](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#deletestatistics) IAM action in that cluster.

**Request**
+ *No Request parameters.*

**Response**
+ **payload**   – A [DeleteStatisticsValueMap](#DeleteStatisticsValueMap) object.

  The deletion payload.
+ **status**   – a String, of type: `string` (a UTF-8 encoded string).

  The cancel status.
+ **statusCode**   – an Integer, of type: `integer` (a signed 32-bit integer).

  The HTTP response code: 200 if the delete was successful, or 204 if there were no statistics to delete.

**Errors**
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [StatisticsNotAvailableException](data-api-dp-errors.md#StatisticsNotAvailableException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)

## GetPropertygraphSummary (action)
<a name="GetPropertygraphSummary"></a>

         The AWS CLI name for this API is: `get-propertygraph-summary`.

Gets a graph summary for a property graph.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetGraphSummary](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getgraphsummary) IAM action in that cluster.

**Request**
+ **mode**  (in the CLI: `--mode`) –  a GraphSummaryType, of type: `string` (a UTF-8 encoded string).

  Mode can take one of two values: `BASIC` (the default), and `DETAILED`.

**Response**
+ **payload**   – A [PropertygraphSummaryValueMap](#PropertygraphSummaryValueMap) object.

  Payload containing the property graph summary response.
+ **statusCode**   – an Integer, of type: `integer` (a signed 32-bit integer).

  The HTTP return code of the request. If the request succeeded, the code is 200.

**Errors**
+ [BadRequestException](data-api-dp-errors.md#BadRequestException)
+ [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException)
+ [StatisticsNotAvailableException](data-api-dp-errors.md#StatisticsNotAvailableException)
+ [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException)
+ [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException)
+ [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException)
+ [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException)
+ [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException)
+ [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException)
+ [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException)
+ [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException)
+ [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException)
+ [MissingParameterException](data-api-dp-errors.md#MissingParameterException)

## *Statistics structures:*
<a name="data-api-dp-statistics-statistics-structures-spacer"></a>

## Statistics (structure)
<a name="Statistics"></a>

Contains statistics information. The DFE engine uses information about the data in your Neptune graph to make effective trade-offs when planning query execution. This information takes the form of statistics that include so-called characteristic sets and predicate statistics that can guide query planning. See [Managing statistics for the Neptune DFE to use](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-dfe-statistics.html).

**Fields**
+ **active** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

  Indicates whether or not DFE statistics generation is enabled at all.
+ **autoCompute** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

  Indicates whether or not automatic statistics generation is enabled.
+ **date** – This is a SyntheticTimestamp\_date\_time, of type: `string` (a UTF-8 encoded string).

  The UTC time at which DFE statistics have most recently been generated.
+ **note** – This is a String, of type: `string` (a UTF-8 encoded string).

  A note about problems in the case where statistics are invalid.
+ **signatureInfo** – This is A [StatisticsSummary](#StatisticsSummary) object.

  A StatisticsSummary structure that contains:
  + `signatureCount` - The total number of signatures across all characteristic sets.
  + `instanceCount` - The total number of characteristic-set instances.
  + `predicateCount` - The total number of unique predicates.
+ **statisticsId** – This is a String, of type: `string` (a UTF-8 encoded string).

  Reports the ID of the current statistics generation run. A value of -1 indicates that no statistics have been generated.

## StatisticsSummary (structure)
<a name="StatisticsSummary"></a>

Information about the characteristic sets generated in the statistics.

**Fields**
+ **instanceCount** – This is an Integer, of type: `integer` (a signed 32-bit integer).

  The total number of characteristic-set instances.
+ **predicateCount** – This is an Integer, of type: `integer` (a signed 32-bit integer).

  The total number of unique predicates.
+ **signatureCount** – This is an Integer, of type: `integer` (a signed 32-bit integer).

  The total number of signatures across all characteristic sets.

## DeleteStatisticsValueMap (structure)
<a name="DeleteStatisticsValueMap"></a>

The payload for DeleteStatistics.

**Fields**
+ **active** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

  The current status of the statistics.
+ **statisticsId** – This is a String, of type: `string` (a UTF-8 encoded string).

  The ID of the statistics generation run that is currently occurring.

## RefreshStatisticsIdMap (structure)
<a name="RefreshStatisticsIdMap"></a>

Statistics for `REFRESH` mode.

**Fields**
+ **statisticsId** – This is a String, of type: `string` (a UTF-8 encoded string).

  The ID of the statistics generation run that is currently occurring.

## NodeStructure (structure)
<a name="NodeStructure"></a>

A node structure.

**Fields**
+ **count** – This is a Long, of type: `long` (a signed 64-bit integer).

  Number of nodes that have this specific structure.
+ **distinctOutgoingEdgeLabels** – This is a String, of type: `string` (a UTF-8 encoded string).

  A list of distinct outgoing edge labels present in this specific structure.
+ **nodeProperties** – This is a String, of type: `string` (a UTF-8 encoded string).

  A list of the node properties present in this specific structure.

## EdgeStructure (structure)
<a name="EdgeStructure"></a>

An edge structure.

**Fields**
+ **count** – This is a Long, of type: `long` (a signed 64-bit integer).

  The number of edges that have this specific structure.
+ **edgeProperties** – This is a String, of type: `string` (a UTF-8 encoded string).

  A list of edge properties present in this specific structure.

## SubjectStructure (structure)
<a name="SubjectStructure"></a>

A subject structure.

**Fields**
+ **count** – This is a Long, of type: `long` (a signed 64-bit integer).

  Number of occurrences of this specific structure.
+ **predicates** – This is a String, of type: `string` (a UTF-8 encoded string).

  A list of predicates present in this specific structure.

## PropertygraphSummaryValueMap (structure)
<a name="PropertygraphSummaryValueMap"></a>

Payload for the property graph summary response.

**Fields**
+ **graphSummary** – This is A [PropertygraphSummary](#PropertygraphSummary) object.

  The graph summary.
+ **lastStatisticsComputationTime** – This is a SyntheticTimestamp\_date\_time, of type: `string` (a UTF-8 encoded string).

  The timestamp, in ISO 8601 format, of the time at which Neptune last computed statistics.
+ **version** – This is a String, of type: `string` (a UTF-8 encoded string).

  The version of this graph summary response.

## PropertygraphSummary (structure)
<a name="PropertygraphSummary"></a>

The graph summary API returns a read-only list of node and edge labels and property keys, along with counts of nodes, edges, and properties. See [Graph summary response for a property graph (PG)](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-graph-summary.html#neptune-graph-summary-pg-response).

**Fields**
+ **edgeLabels** – This is a String, of type: `string` (a UTF-8 encoded string).

  A list of the distinct edge labels in the graph.
+ **edgeProperties** – This is LongValuedMap objects It is a map array of key-value pairs where:

      Each key is a a String, of type: `string` (a UTF-8 encoded string).

      Each value is a a Long, of type: `long` (a signed 64-bit integer).

  A list of the distinct edge properties in the graph, along with the count of edges where each property is used.
+ **edgeStructures** – This is An array of [EdgeStructure](#EdgeStructure) objects.

  This field is only present when the requested mode is `DETAILED`. It contains a list of edge structures.
+ **nodeLabels** – This is a String, of type: `string` (a UTF-8 encoded string).

  A list of the distinct node labels in the graph.
+ **nodeProperties** – This is LongValuedMap objects It is a map array of key-value pairs where:

      Each key is a a String, of type: `string` (a UTF-8 encoded string).

      Each value is a a Long, of type: `long` (a signed 64-bit integer).

  The number of distinct node properties in the graph.
+ **nodeStructures** – This is An array of [NodeStructure](#NodeStructure) objects.

  This field is only present when the requested mode is `DETAILED`. It contains a list of node structures.
+ **numEdgeLabels** – This is a Long, of type: `long` (a signed 64-bit integer).

  The number of distinct edge labels in the graph.
+ **numEdgeProperties** – This is a Long, of type: `long` (a signed 64-bit integer).

  The number of distinct edge properties in the graph.
+ **numEdges** – This is a Long, of type: `long` (a signed 64-bit integer).

  The number of edges in the graph.
+ **numNodeLabels** – This is a Long, of type: `long` (a signed 64-bit integer).

  The number of distinct node labels in the graph.
+ **numNodeProperties** – This is a Long, of type: `long` (a signed 64-bit integer).

  A list of the distinct node properties in the graph, along with the count of nodes where each property is used.
+ **numNodes** – This is a Long, of type: `long` (a signed 64-bit integer).

  The number of nodes in the graph.
+ **totalEdgePropertyValues** – This is a Long, of type: `long` (a signed 64-bit integer).

  The total number of usages of all edge properties.
+ **totalNodePropertyValues** – This is a Long, of type: `long` (a signed 64-bit integer).

  The total number of usages of all node properties.