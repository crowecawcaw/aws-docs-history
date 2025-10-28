# Neptune dataplane statistics and graph summary APIs

**Property graph statistics actions:**

- [GetPropertygraphStatistics (action)](#GetPropertygraphStatistics "#GetPropertygraphStatistics")
- [ManagePropertygraphStatistics (action)](#ManagePropertygraphStatistics "#ManagePropertygraphStatistics")
- [DeletePropertygraphStatistics (action)](#DeletePropertygraphStatistics "#DeletePropertygraphStatistics")
- [GetPropertygraphSummary (action)](#GetPropertygraphSummary "#GetPropertygraphSummary")
  **Statistics structures:**

- [Statistics (structure)](#Statistics "#Statistics")
- [StatisticsSummary (structure)](#StatisticsSummary "#StatisticsSummary")
- [DeleteStatisticsValueMap (structure)](#DeleteStatisticsValueMap "#DeleteStatisticsValueMap")
- [RefreshStatisticsIdMap (structure)](#RefreshStatisticsIdMap "#RefreshStatisticsIdMap")
- [NodeStructure (structure)](#NodeStructure "#NodeStructure")
- [EdgeStructure (structure)](#EdgeStructure "#EdgeStructure")
- [SubjectStructure (structure)](#SubjectStructure "#SubjectStructure")
- [PropertygraphSummaryValueMap (structure)](#PropertygraphSummaryValueMap "#PropertygraphSummaryValueMap")
- [PropertygraphSummary (structure)](#PropertygraphSummary "#PropertygraphSummary")

## GetPropertygraphStatistics (action)

        The AWS CLI name for this API is: `get-propertygraph-statistics`.

Gets property graph statistics (Gremlin and openCypher).

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:GetStatisticsStatus](iam-dp-actions.md#getstatisticsstatus "iam-dp-actions.md#getstatisticsstatus")
IAM action in that cluster.

###### Request

- _No Request parameters._

**Response**

- **payload**   – _Required:_ A [Statistics](#Statistics "#Statistics") object.

Statistics for property-graph data.

- **status**   – _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP return code of the request. If the request succeeded, the code
is 200. See [Common
error codes for DFE statistics request](neptune-dfe-statistics.md#neptune-dfe-statistics-errors "neptune-dfe-statistics.md#neptune-dfe-statistics-errors") for a list of common errors.

###### Errors

- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [StatisticsNotAvailableException](data-api-dp-errors.md#StatisticsNotAvailableException "data-api-dp-errors.md#StatisticsNotAvailableException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException "data-api-dp-errors.md#AccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException "data-api-dp-errors.md#ReadOnlyViolationException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")

## ManagePropertygraphStatistics (action)

        The AWS CLI name for this API is: `manage-propertygraph-statistics`.

Manages the generation and use of property graph statistics.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:ManageStatistics](iam-dp-actions.md#managestatistics "iam-dp-actions.md#managestatistics")
IAM action in that cluster.

**Request**

- **mode**  (in the CLI: `--mode`) –  a StatisticsAutoGenerationMode, of type: `string` (a UTF-8 encoded string).

The statistics generation mode. One of: `DISABLE_AUTOCOMPUTE`,
`ENABLE_AUTOCOMPUTE`, or `REFRESH`, the last of which
manually triggers DFE statistics generation.

**Response**

- **payload**   – A [RefreshStatisticsIdMap](#RefreshStatisticsIdMap "#RefreshStatisticsIdMap") object.

This is only returned for refresh mode.

- **status**   – _Required:_ a String, of type: `string` (a UTF-8 encoded string).

The HTTP return code of the request. If the request succeeded, the code
is 200.

###### Errors

- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [StatisticsNotAvailableException](data-api-dp-errors.md#StatisticsNotAvailableException "data-api-dp-errors.md#StatisticsNotAvailableException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException "data-api-dp-errors.md#AccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException "data-api-dp-errors.md#ReadOnlyViolationException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")

## DeletePropertygraphStatistics (action)

        The AWS CLI name for this API is: `delete-propertygraph-statistics`.

Deletes statistics for Gremlin and openCypher (property graph) data.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:DeleteStatistics](iam-dp-actions.md#deletestatistics "iam-dp-actions.md#deletestatistics")
IAM action in that cluster.

###### Request

- _No Request parameters._

**Response**

- **payload**   – A [DeleteStatisticsValueMap](#DeleteStatisticsValueMap "#DeleteStatisticsValueMap") object.

The deletion payload.

- **status**   – a String, of type: `string` (a UTF-8 encoded string).

The cancel status.

- **statusCode**   – an Integer, of type: `integer` (a signed 32-bit integer).

The HTTP response code: 200 if the delete was successful, or 204 if there
were no statistics to delete.

###### Errors

- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [StatisticsNotAvailableException](data-api-dp-errors.md#StatisticsNotAvailableException "data-api-dp-errors.md#StatisticsNotAvailableException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException "data-api-dp-errors.md#AccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException "data-api-dp-errors.md#ReadOnlyViolationException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")

## GetPropertygraphSummary (action)

        The AWS CLI name for this API is: `get-propertygraph-summary`.

Gets a graph summary for a property graph.

When invoking this operation in a Neptune cluster that has IAM authentication
enabled, the IAM user or role making the request must have a policy attached that
allows the [neptune-db:GetGraphSummary](iam-dp-actions.md#getgraphsummary "iam-dp-actions.md#getgraphsummary")
IAM action in that cluster.

**Request**

- **mode**  (in the CLI: `--mode`) –  a GraphSummaryType, of type: `string` (a UTF-8 encoded string).

Mode can take one of two values: `BASIC` (the default), and
`DETAILED`.

**Response**

- **payload**   – A [PropertygraphSummaryValueMap](#PropertygraphSummaryValueMap "#PropertygraphSummaryValueMap") object.

Payload containing the property graph summary response.

- **statusCode**   – an Integer, of type: `integer` (a signed 32-bit integer).

The HTTP return code of the request. If the request succeeded, the code
is 200.

###### Errors

- [BadRequestException](data-api-dp-errors.md#BadRequestException "data-api-dp-errors.md#BadRequestException")
- [InvalidParameterException](data-api-dp-errors.md#InvalidParameterException "data-api-dp-errors.md#InvalidParameterException")
- [StatisticsNotAvailableException](data-api-dp-errors.md#StatisticsNotAvailableException "data-api-dp-errors.md#StatisticsNotAvailableException")
- [ClientTimeoutException](data-api-dp-errors.md#ClientTimeoutException "data-api-dp-errors.md#ClientTimeoutException")
- [AccessDeniedException](data-api-dp-errors.md#AccessDeniedException "data-api-dp-errors.md#AccessDeniedException")
- [IllegalArgumentException](data-api-dp-errors.md#IllegalArgumentException "data-api-dp-errors.md#IllegalArgumentException")
- [TooManyRequestsException](data-api-dp-errors.md#TooManyRequestsException "data-api-dp-errors.md#TooManyRequestsException")
- [UnsupportedOperationException](data-api-dp-errors.md#UnsupportedOperationException "data-api-dp-errors.md#UnsupportedOperationException")
- [PreconditionsFailedException](data-api-dp-errors.md#PreconditionsFailedException "data-api-dp-errors.md#PreconditionsFailedException")
- [ReadOnlyViolationException](data-api-dp-errors.md#ReadOnlyViolationException "data-api-dp-errors.md#ReadOnlyViolationException")
- [ConstraintViolationException](data-api-dp-errors.md#ConstraintViolationException "data-api-dp-errors.md#ConstraintViolationException")
- [InvalidArgumentException](data-api-dp-errors.md#InvalidArgumentException "data-api-dp-errors.md#InvalidArgumentException")
- [MissingParameterException](data-api-dp-errors.md#MissingParameterException "data-api-dp-errors.md#MissingParameterException")

## _Statistics structures:_

## Statistics (structure)

Contains statistics information. The DFE engine uses information about
the data in your Neptune graph to make effective trade-offs when planning query
execution. This information takes the form of statistics that include so-called
characteristic sets and predicate statistics that can guide query planning.
See [Managing
statistics for the Neptune DFE to use](neptune-dfe-statistics.md "neptune-dfe-statistics.md").

###### Fields

- **active** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not DFE statistics generation is enabled at all.

- **autoCompute** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

Indicates whether or not automatic statistics generation is enabled.

- **date** – This is a SyntheticTimestamp_date_time, of type: `string` (a UTF-8 encoded string).

The UTC time at which DFE statistics have most recently been generated.

- **note** – This is a String, of type: `string` (a UTF-8 encoded string).

A note about problems in the case where statistics are invalid.

- **signatureInfo** – This is A [StatisticsSummary](#StatisticsSummary "#StatisticsSummary") object.

A StatisticsSummary structure that contains:

    + `signatureCount` - The total number of signatures across
     all characteristic sets.
    + `instanceCount` - The total number of characteristic-set
     instances.
    + `predicateCount` - The total number of unique predicates.

- **statisticsId** – This is a String, of type: `string` (a UTF-8 encoded string).

Reports the ID of the current statistics generation run. A value of -1 indicates
that no statistics have been generated.

## StatisticsSummary (structure)

Information about the characteristic sets generated in the statistics.

###### Fields

- **instanceCount** – This is an Integer, of type: `integer` (a signed 32-bit integer).

The total number of characteristic-set instances.

- **predicateCount** – This is an Integer, of type: `integer` (a signed 32-bit integer).

The total number of unique predicates.

- **signatureCount** – This is an Integer, of type: `integer` (a signed 32-bit integer).

The total number of signatures across all characteristic sets.

## DeleteStatisticsValueMap (structure)

The payload for DeleteStatistics.

###### Fields

- **active** – This is a Boolean, of type: `boolean` (a Boolean (true or false) value).

The current status of the statistics.

- **statisticsId** – This is a String, of type: `string` (a UTF-8 encoded string).

The ID of the statistics generation run that is currently occurring.

## RefreshStatisticsIdMap (structure)

Statistics for `REFRESH` mode.

###### Fields

- **statisticsId** – This is a String, of type: `string` (a UTF-8 encoded string).

The ID of the statistics generation run that is currently occurring.

## NodeStructure (structure)

A node structure.

###### Fields

- **count** – This is a Long, of type: `long` (a signed 64-bit integer).

Number of nodes that have this specific structure.

- **distinctOutgoingEdgeLabels** – This is a String, of type: `string` (a UTF-8 encoded string).

A list of distinct outgoing edge labels present in this specific structure.

- **nodeProperties** – This is a String, of type: `string` (a UTF-8 encoded string).

A list of the node properties present in this specific structure.

## EdgeStructure (structure)

An edge structure.

###### Fields

- **count** – This is a Long, of type: `long` (a signed 64-bit integer).

The number of edges that have this specific structure.

- **edgeProperties** – This is a String, of type: `string` (a UTF-8 encoded string).

A list of edge properties present in this specific structure.

## SubjectStructure (structure)

A subject structure.

###### Fields

- **count** – This is a Long, of type: `long` (a signed 64-bit integer).

Number of occurrences of this specific structure.

- **predicates** – This is a String, of type: `string` (a UTF-8 encoded string).

A list of predicates present in this specific structure.

## PropertygraphSummaryValueMap (structure)

Payload for the property graph summary response.

###### Fields

- **graphSummary** – This is A [PropertygraphSummary](#PropertygraphSummary "#PropertygraphSummary") object.

The graph summary.

- **lastStatisticsComputationTime** – This is a SyntheticTimestamp_date_time, of type: `string` (a UTF-8 encoded string).

The timestamp, in ISO 8601 format, of the time at which Neptune last computed
statistics.

- **version** – This is a String, of type: `string` (a UTF-8 encoded string).

The version of this graph summary response.

## PropertygraphSummary (structure)

The graph summary API returns a read-only list of node and edge labels and
property keys, along with counts of nodes, edges, and properties. See [Graph
summary response for a property graph (PG)](neptune-graph-summary.md#neptune-graph-summary-pg-response "neptune-graph-summary.md#neptune-graph-summary-pg-response").

###### Fields

- **edgeLabels** – This is a String, of type: `string` (a UTF-8 encoded string).

A list of the distinct edge labels in the graph.

- **edgeProperties** – This is LongValuedMap objects It is a map array of key-value pairs where:

    Each key is a a String, of type: `string` (a UTF-8 encoded string).

    Each value is a a Long, of type: `long` (a signed 64-bit integer).

A list of the distinct edge properties in the graph, along with the count
of edges where each property is used.

- **edgeStructures** – This is An array of [EdgeStructure](#EdgeStructure "#EdgeStructure") objects.

This field is only present when the requested mode is `DETAILED`.
It contains a list of edge structures.

- **nodeLabels** – This is a String, of type: `string` (a UTF-8 encoded string).

A list of the distinct node labels in the graph.

- **nodeProperties** – This is LongValuedMap objects It is a map array of key-value pairs where:

    Each key is a a String, of type: `string` (a UTF-8 encoded string).

    Each value is a a Long, of type: `long` (a signed 64-bit integer).

The number of distinct node properties in the graph.

- **nodeStructures** – This is An array of [NodeStructure](#NodeStructure "#NodeStructure") objects.

This field is only present when the requested mode is `DETAILED`.
It contains a list of node structures.

- **numEdgeLabels** – This is a Long, of type: `long` (a signed 64-bit integer).

The number of distinct edge labels in the graph.

- **numEdgeProperties** – This is a Long, of type: `long` (a signed 64-bit integer).

The number of distinct edge properties in the graph.

- **numEdges** – This is a Long, of type: `long` (a signed 64-bit integer).

The number of edges in the graph.

- **numNodeLabels** – This is a Long, of type: `long` (a signed 64-bit integer).

The number of distinct node labels in the graph.

- **numNodeProperties** – This is a Long, of type: `long` (a signed 64-bit integer).

A list of the distinct node properties in the graph, along with the count
of nodes where each property is used.

- **numNodes** – This is a Long, of type: `long` (a signed 64-bit integer).

The number of nodes in the graph.

- **totalEdgePropertyValues** – This is a Long, of type: `long` (a signed 64-bit integer).

The total number of usages of all edge properties.

- **totalNodePropertyValues** – This is a Long, of type: `long` (a signed 64-bit integer).

The total number of usages of all node properties.
