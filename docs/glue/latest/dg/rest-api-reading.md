# Reading from a REST API

After you register a REST API ConnectionType and create an AWS Glue connection, you can read data
from the REST API in your AWS Glue ETL jobs. With this connection, you can process external REST API data
alongside other sources in the same job. You need the connection name and entity name to read data.

The following example shows how to read from a REST API data source using Python:

```

rest_read = glueContext.create_dynamic_frame.from_options(
    connection_type="rest",
    connection_options={
        "connectionName": "`connection-name`",
        "ENTITY_NAME": "`entity-name`",
        "CONNECTION_TYPE": "`REST-connection-type`"
    }
)
```

## Filtering data

You can push down filter predicates to the source REST API to reduce the amount of data transferred.
The REST API connector supports two filter modes:

- **QUERY\_PARAMS** – Each filter becomes a separate URL query parameter.
  For example: `?created[gte]=1704067200&created[lte]=1717200000`
- **FILTER\_STRING** – All filters combine into a single query parameter.
  For example: `?search=status eq "ACTIVE" and lastUpdated gt "2024-01-01"`

To apply a filter predicate in your AWS Glue ETL job, use the `FILTER_PREDICATE` connection option:

```

rest_read = glueContext.create_dynamic_frame.from_options(
    connection_type="rest",
    connection_options={
        "connectionName": "`connection-name`",
        "ENTITY_NAME": "`entity-name`",
        "CONNECTION_TYPE": "`REST-connection-type`",
        "FILTER_PREDICATE": "status = \"ACTIVE\" AND lastUpdated >= \"2024-01-01T00:00:00.000Z\""
    }
)
```

###### FilterConfiguration properties

Configure filtering behavior in your ConnectionType registration using the
`FilterConfiguration` object. The following table describes the available properties:

| Property                    | Type    | Description                                                                       |
| --------------------------- | ------- | --------------------------------------------------------------------------------- |
| `FilterMode`                | String  | Required. `QUERY_PARAMS` or `FILTER_STRING`.                                      |
| `OperatorMappings`          | Map     | Maps logical operators to API-specific syntax.                                    |
| `DateTimeFormat`            | String  | DateTime format pattern or `EPOCH_SECONDS`/`EPOCH_MILLIS`.                        |
| `StripQuotes`               | Boolean | Specifies whether to strip surrounding quotes from input values. Default: `true`. |
| `BetweenConfiguration`      | Object  | Default BETWEEN handling configuration.                                           |
| `FilterStringConfiguration` | Object  | Settings specific to `FILTER_STRING` mode.                                        |

###### FilterStringConfiguration properties

The following table describes the properties for `FILTER_STRING` mode:

| Property            | Type    | Description                                                        |
| ------------------- | ------- | ------------------------------------------------------------------ |
| `FilterStringKey`   | String  | Required. Query parameter key (for example, "search" or "filter"). |
| `QuoteStringValues` | Boolean | Specifies whether to wrap String and DateTime values in quotes.    |
| `QuoteCharacter`    | String  | Quote character. Default: `"`                                      |

###### BetweenConfiguration properties

The following table describes the BETWEEN handling properties:

| Property       | Mode           | Description                                                 |
| -------------- | -------------- | ----------------------------------------------------------- |
| `LowBoundKey`  | QUERY\_PARAMS  | Key template for low bound. Supports `{FIELD}` placeholder. |
| `HighBoundKey` | QUERY\_PARAMS  | Key template for high bound. Omit to drop high bound.       |
| `Template`     | FILTER\_STRING | Template with `{FIELD}`, `{LOW}`, `{HIGH}` placeholders.    |

###### Supported operators

The following operators are supported in filter predicates: `EQUAL_TO`,
`GREATER_THAN`, `LESS_THAN`, `GREATER_THAN_OR_EQUAL_TO`,
`LESS_THAN_OR_EQUAL_TO`, `NOT_EQUAL_TO`, `CONTAINS`,
`BETWEEN`, `AND`, `OR`.

###### Field-level overrides

You can configure per-field filter behavior using `FilterOverrides` in the Schema
definition. The following override properties are available:

- `FieldName` – Override the field name used in filter output.
- `OperatorMappings` – Field-level operator overrides.
- `BetweenConfiguration` – Per-field BETWEEN override.
- `DateTimeFormat` – Per-field DateTime format override.

###### Example: QUERY\_PARAMS mode

The following example shows a `FilterConfiguration` for a REST API that uses query parameters
with bracket notation for operators and epoch timestamps for date values:

```

"FilterConfiguration": {
    "FilterMode": "QUERY_PARAMS",
    "OperatorMappings": {
        "EQUAL_TO": "{FIELD}",
        "GREATER_THAN_OR_EQUAL_TO": "{FIELD}[gte]",
        "LESS_THAN_OR_EQUAL_TO": "{FIELD}[lte]"
    },
    "DateTimeFormat": "EPOCH_SECONDS",
    "BetweenConfiguration": {
        "LowBoundKey": "{FIELD}[gte]",
        "HighBoundKey": "{FIELD}[lte]"
    }
}
```

With this configuration, an input filter of `created >= 2024-01-01 AND created <= 2024-06-01`
produces the URL query string: `?created[gte]=1704067200&created[lte]=1717200000`

###### Example: FILTER\_STRING mode

The following example shows a `FilterConfiguration` for a REST API that uses a single
filter string parameter with space-padded operators:

```

"FilterConfiguration": {
    "FilterMode": "FILTER_STRING",
    "OperatorMappings": {
        "EQUAL_TO": " eq ",
        "GREATER_THAN": " gt ",
        "GREATER_THAN_OR_EQUAL_TO": " ge ",
        "LESS_THAN": " lt ",
        "AND": " and ",
        "OR": " or "
    },
    "DateTimeFormat": "yyyy-MM-dd'T'HH:mm:ss.SSS'Z'",
    "BetweenConfiguration": {
        "Template": "{FIELD} ge {LOW} and {FIELD} le {HIGH}"
    },
    "FilterStringConfiguration": {
        "FilterStringKey": "search",
        "QuoteStringValues": true,
        "QuoteCharacter": "\""
    }
}
```

With this configuration, an input filter of `status = "ACTIVE" AND lastUpdated > 2024-01-01T00:00:00.000Z`
produces the URL query string: `?search=status eq "ACTIVE" and lastUpdated gt "2024-01-01T00:00:00.000Z"`

## Partitioning queries

You can split data reads into parallel partitions across Spark workers to improve throughput.
The REST API connector supports field-based partitioning, which divides data into ranges based on a specified field.

###### Spark job parameters

The following connection options control partitioning behavior:

- `PARTITION_FIELD` – Field to partition on. Must be marked `IsPartitionable: true` in the schema.
- `LOWER_BOUND` – Inclusive lower bound for the partition range.
- `UPPER_BOUND` – Upper bound for the partition range. Intermediate partitions exclude this value. The last partition includes it.
- `NUM_PARTITIONS` – Number of parallel partitions.

###### Field-based partitioning

Field-based partitioning divides data into ranges based on a specified field. The following
example partitions data on the `lastUpdated` field:

```

rest_read = glueContext.create_dynamic_frame.from_options(
    connection_type="rest",
    connection_options={
        "connectionName": "`connection-name`",
        "ENTITY_NAME": "`entity-name`",
        "CONNECTION_TYPE": "`REST-connection-type`",
        "PARTITION_FIELD": "lastUpdated",
        "LOWER_BOUND": "2024-01-01T00:00:00.000Z",
        "UPPER_BOUND": "2024-12-31T00:00:00.000Z",
        "NUM_PARTITIONS": "4"
    }
)
```

With 4 partitions on the `lastUpdated` field, the work is distributed as follows:

- Worker 1: `lastUpdated >= "2024-01-01" AND lastUpdated < "2024-04-01"`
- Worker 2: `lastUpdated >= "2024-04-01" AND lastUpdated < "2024-07-01"`
- Worker 3: `lastUpdated >= "2024-07-01" AND lastUpdated < "2024-10-01"`
- Worker 4: `lastUpdated >= "2024-10-01" AND lastUpdated <= "2024-12-31"`

###### Configuring partition support in RegisterConnectionType

To enable field-based partitioning, mark fields as partitionable in the Schema definition:

```

"Schema": {
    "lastUpdated": {
        "FieldDataType": "TIMESTAMP",
        "IsPartitionable": true
    }
}
```

The following `FieldDataType` values are supported for partitioning:

- `TIMESTAMP` – DateTime partitioning. Splits the range into time windows.
- `INTEGER` – Integer partitioning. Splits the range into numeric windows.

###### Note

The connector combines partition filters with user filters using AND. If your filter contains a LIMIT clause,
the connector skips partitioning. If partition generation fails, the connector falls back to a single partition and the job still
completes.
