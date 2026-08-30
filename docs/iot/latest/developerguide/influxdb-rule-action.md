# InfluxDB

Choose this action when you want to query device telemetry for operational trends
or monitor time-series data in real time. You can use client-side or server-side
batching to combine multiple points in one write request. AWS IoT Core converts each
message to InfluxDB line protocol and writes it to the specified database and table.
For more information about the format, see [InfluxDB line protocol](https://docs.influxdata.com/influxdb3/enterprise/reference/line-protocol/ "https://docs.influxdata.com/influxdb3/enterprise/reference/line-protocol/") in the InfluxData documentation. For information
about managed clusters, see [Amazon Timestream for
InfluxDB](../../../timestream/latest/developerguide/influxdb3.md "../../../timestream/latest/developerguide/influxdb3.md").

###### In this topic:

- [Prerequisites](#influxdb-rule-action-prerequisites "#influxdb-rule-action-prerequisites")
- [InfluxDB action destination](#influxdb-action-destination "#influxdb-action-destination")
- [InfluxDB terminology mapping](#influxdb-terminology-mapping "#influxdb-terminology-mapping")
- [Parameters](#influxdb-rule-action-parameters "#influxdb-rule-action-parameters")
- [Batching](#influxdb-rule-action-batching "#influxdb-rule-action-batching")
- [Per-element templates for array payloads](#influxdb-per-element-templates "#influxdb-per-element-templates")
- [InfluxDB record content](#influxdb-record-content "#influxdb-record-content")
- [Error actions](#influxdb-error-actions "#influxdb-error-actions")
- [Examples](#influxdb-rule-action-examples "#influxdb-rule-action-examples")

## Prerequisites

This rule action has the following prerequisites:

- **An InfluxDB action destination**
  – Create an InfluxDB action destination that specifies the
  endpoint, version, and credentials for your InfluxDB instance.
  AWS IoT Core validates endpoint ownership before sending traffic. See
  [InfluxDB action destination](#influxdb-action-destination "#influxdb-action-destination").
- **An IAM role** that AWS IoT can assume
  to write to your InfluxDB databases and perform the
  `GetSecretValue` operation on the secret that stores your
  InfluxDB credentials. For more information, see [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md").
- **InfluxDB credentials stored in
  AWS Secrets Manager** – For InfluxDB V3, Amazon Timestream for
  InfluxDB automatically provisions a Secrets Manager secret when you create
  the InfluxDB cluster. The secret contains the cluster credentials. For
  InfluxDB V2, generate an All Access or custom API token from your
  InfluxDB instance. Store the token value as a plaintext secret in
  AWS Secrets Manager. For more information about token creation, see [Create a token](https://docs.influxdata.com/influxdb/v2/admin/tokens/create-token/ "https://docs.influxdata.com/influxdb/v2/admin/tokens/create-token/") in the InfluxData documentation. At runtime,
  the rule action calls `secretsmanager:GetSecretValue` to
  retrieve these credentials before authenticating to your InfluxDB
  endpoint.
- **Timestamp in message payload**
  – Each object in the message payload must contain a key named
  `timestamp` (case-sensitive) with an integer Unix epoch
  value. The timestamp unit can also be set in the IoT rule definition.
  AWS IoT Core does not generate timestamps for the InfluxDB action, except
  when InfluxDB is used as an Error action.

###### Note

An alias such as `ts` or `time` cannot be
used instead of `timestamp`.

- **HTTPS connectivity** – Your
  InfluxDB instance must be reachable from AWS IoT Core over HTTPS. Supported
  outbound ports are: 443, 8443, 8086 (default port for InfluxDB V2), and
  8181 (default port for InfluxDB V3).
- **JSON-format payload** – The
  InfluxDB action processes JSON payloads only. If your devices publish
  binary or Protobuf data, use the [decode()](binary-payloads.md#binary-payloads-protobuf "binary-payloads.md#binary-payloads-protobuf")
  function in your rule SQL to convert to JSON before the action
  runs.

## InfluxDB action destination

Before you can use the InfluxDB rule action, you must create an InfluxDB
action destination. The destination defines the connection parameters for your
InfluxDB instance. AWS IoT Core then validates endpoint ownership.

### Creating a destination

Use the `CreateTopicRuleDestination` API to create an InfluxDB
destination:

```
{
  "destinationConfiguration": {
    "influxDBConfiguration": {
      "endpoint": "https://my-instance.timestream-influxdb.us-west-2.amazonaws.com:8086",
      "influxDBVersion": "V2",
      "secretId": "arn:aws:secretsmanager:us-west-2:111122223333:secret:my-influxdb-credentials-AbCdEf"
    }
  }
}
```

### Destination parameters

| Parameter         | Type   | Required | Description                                                                                                                                     |
| ----------------- | ------ | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `endpoint`        | String | Yes      | The HTTPS endpoint URL of your InfluxDB instance. HTTP is<br>not supported. Supported ports: 443, 8086, 8181,<br>8443.                          |
| `influxDBVersion` | String | Yes      | The InfluxDB version. Valid values: `V2`,<br>`V3`.                                                                                              |
| `secretId`        | String | Yes      | The name or ARN of the AWS Secrets Manager secret that contains<br>your InfluxDB token.                                                         |
| `secretType`      | String | No       | The type of secret value. Valid values:<br>`SecretString`,<br>`SecretBinary`.                                                                   |
| `secretKey`       | String | No       | The key within the secret JSON that contains the<br>authentication token. Required only when the secret is a<br>JSON object with multiple keys. |

### Endpoint ownership validation

When you create an InfluxDB action destination, AWS IoT Core validates
endpoint ownership by authenticating against the InfluxDB API using the
credentials you provided:

- **InfluxDB V2**: AWS IoT Core calls the
  `/api/v2/me` endpoint.
- **InfluxDB V3**: AWS IoT Core calls the
  list databases endpoint
  (`GET /api/v3/configure/database`).

A successful response (2xx) sets the destination status to
`ENABLED`. On failure, AWS IoT Core sets the status to
`ERROR`. To retry validation, call
`UpdateTopicRuleDestination` with the status set to
`IN_PROGRESS`.

## InfluxDB terminology mapping

The following terms differ between InfluxDB V2 and V3.

| AWS IoT Core parameter | InfluxDB V2 term | InfluxDB V3 term |
| ---------------------- | ---------------- | ---------------- |
| `databaseName`         | Bucket           | Database         |
| `tableName`            | Measurement      | Table            |

###### Note

If you are migrating from Amazon Timestream rule action, the
`dimensions` parameter maps to tags in the InfluxDB action,
and the query result attributes map to fields.

## Parameters

When you create an AWS IoT rule with the InfluxDB action, you must specify the
following information:

`destinationArn`

The ARN of the InfluxDB action destination. See [InfluxDB action destination](#influxdb-action-destination "#influxdb-action-destination").
Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

`roleArn`

The ARN of the IAM role that grants AWS IoT permission to access
the Secrets Manager secret. See [Prerequisites](#influxdb-rule-action-prerequisites "#influxdb-rule-action-prerequisites").
Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No

`databaseName`

The name of the InfluxDB database (called a
_bucket_ in InfluxDB v2, or a
_database_ in InfluxDB v3) to write records
to. Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No. To route data to different databases, create
separate rule actions for each database.

`tableName`

The name of the table (called a
_measurement_ in InfluxDB v2, or a
_table_ in InfluxDB v3) to write records to.
Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): Yes.

`organization`

The InfluxDB organization name. Required for InfluxDB v2. If you
include this parameter for InfluxDB v3, it is ignored.
Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No.

`tags`

Metadata for each point, specified as a map. Each map key is a tag
name, and each map value is the corresponding tag value. Tags are
indexed for query performance.

- In InfluxDB V3, each tag name must be unique within a table
  and cannot duplicate a field name.
- Tag values support message-scope and per-element
  substitution templates.

`timestampUnit`

The precision of the timestamp value in the payload. Valid values:
`s` (seconds) | `ms` (milliseconds) |
`us` (microseconds) | `ns` (nanoseconds).
Default: `ms`. Supports [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md"): No.

`batchConfig`

(Optional) Server-side batching configuration. For more
information, see [Batching](#influxdb-rule-action-batching "#influxdb-rule-action-batching").

- `maxBatchSize` – Maximum number of points
  in each batch. Valid range: 1–500.
- `maxBatchOpenMs` – Maximum time in
  milliseconds to hold a batch open. Valid range:
  5–1,000.
- `maxBatchSizeBytes` – Maximum total size
  in bytes before flushing. Valid range:
  100–131,072.
- `batchAcrossTopics` – Boolean. When
  `true`, the batch includes points from
  messages on different topics. Default:
  `false`.

## Batching

The InfluxDB action supports two batching modes.

### Client-side batching

Your IoT device batches time-series data as a JSON array and publishes it
as a single MQTT message. With client-side batching, each array element
becomes one line-protocol point in a single write request. You do not need
additional configuration.

### Server-side batching

Use server-side batching to group individual messages before writing them
to InfluxDB. Configure server-side batching using the
`batchConfig` parameter. The batch is flushed when any
configured limit (`maxBatchSize`,
`maxBatchOpenMs`, or `maxBatchSizeBytes`) is
reached first.

###### Note

Both server-side batching and client-side batching (JSON array
payloads) can be configured at the same time.

The InfluxDB action is metered based on the outbound payload size in 5 KiB
increments. Line-protocol conversion failures are also metered.

## Per-element templates for array payloads

When your IoT devices send batched time-series data as a JSON array, you can
use the **“per-element substitution
templates”** to resolve values from each individual array
element. This routes each data point to a different table or applies
element-specific tags. For more information, see [Per-element
templates](per-element-templates.md "per-element-templates.md").

### Syntax of two [substitution templates](iot-substitution-templates.md "iot-substitution-templates.md")

- `${expression}` – Resolves at message scope,
  against the incoming device message. Evaluated once for each
  message; the same value applies to every point in the array.
- `@{expression}` – Resolves at element scope,
  against an individual element of the payload produced by the rule's
  SQL SELECT statement. Re-evaluated for each array element, so each
  point can get a different value. For more information, see [`@{expression}` reference](per-element-expression.md "per-element-expression.md").

Use `@{...}` in `tableName` and tag values to
resolve the expression against each array element individually.

### Example

Given the following device payload (JSON array):

```
[
  {"measurement_type": "temperature", "room": "kitchen", "timestamp": 1700000000000, "value": 23.5},
  {"measurement_type": "humidity", "room": "bedroom", "timestamp": 1700000001000, "value": 60.1}
]
```

And the following action configuration:

```
{
  "influxDB": {
    "destinationArn": "arn:aws:iot:us-west-2:111122223333:ruledestination/influxdb/abc123",
    "roleArn": "arn:aws:iam::111122223333:role/iot-influxdb-role",
    "databaseName": "sensor_data",
    "tableName": "@{measurement_type}",
    "tags": {
      "room": "@{room}"
    },
    "timestampUnit": "ms"
  }
}
```

The resulting line-protocol output contains two points:

```
temperature,room=kitchen value=23.5 1700000000000
humidity,room=bedroom value=60.1 1700000001000
```

###### Note

A field referenced by `@{...}` is removed from the
line-protocol field set, so it does not also appear as a field. In this
example, `measurement_type` becomes the table name and
`room` becomes a tag, so neither appears in the field set
— `value` is the only field.

### Restrictions

- `@{...}` is supported only in the InfluxDB action
  configuration (`tableName` and tag values).
- You cannot use `@{...}` in rule SQL (SELECT/WHERE
  clauses), error action definitions, or any other rule
  action.
- Only field references are supported inside
  `@{...}`. Functions are not supported.
- Each value supports at most one `@{...}` marker.
  Multiple markers in a single value produce an API exception.
- You cannot mix `${...}` and `@{...}` in the
  same value. Mixing produces an API exception.
- A single JSON object is treated as a one-element array.

## InfluxDB record content

For each record in the post-SQL query result, the resulting InfluxDB
line-protocol point contains these components:

| Component | Source                                                                     |
| --------- | -------------------------------------------------------------------------- |
| Table     | The `tableName` parameter value                                            |
| Tags      | The key-value pairs from the `tags`<br>parameter                           |
| Fields    | Remaining payload attributes not used as tags, table name, or<br>timestamp |
| Timestamp | The `timestamp` key extracted from the<br>payload                          |

### Data type conversion

AWS IoT Core converts JSON values to InfluxDB line protocol types as
follows:

| JSON type                             | Line protocol type                          | Example                                           |
| ------------------------------------- | ------------------------------------------- | ------------------------------------------------- |
| Integer (−2⁶³ to<br>2⁶³−1)            | Signed integer (`i` suffix)                 | `42` → `42i`                                      |
| Integer (2⁶³ to<br>2⁶⁴−1)             | Unsigned integer (`u` suffix)               | `9223372036854775808` →<br>`9223372036854775808u` |
| Integer outside<br>(−2⁶³ to<br>2⁶⁴−1) | Rejected (error action triggered)           | —                                                 |
| Float / decimal                       | IEEE-754 64-bit float                       | `23.5` → `23.5`                                   |
| Boolean                               | `t` or `f`                                  | `true` → `t`                                      |
| String                                | Quoted string                               | `"active"` →<br>`"active"`                        |
| Null                                  | Omitted (not written)                       | —                                                 |
| Object or array                       | Compacted JSON string (whitespace stripped) | `{"a":1}` →<br>`"{\"a\":1}"`                      |

### Naming restrictions

- Field keys and tag keys cannot be empty or start with an
  underscore (`_`).
- In InfluxDB V3, table name and tag key must start with a letter or
  digit.
- Commas, equals signs, and spaces in field keys, tag keys, and tag
  values are escaped automatically.
- Measurements: commas and spaces are escaped automatically.
- Tags are sorted alphabetically by key before serialization to
  improve ingestion performance.
- Empty tag values are omitted from the output.

### Reserved keys

The following payload keys are stripped from the field set during
line-protocol conversion:

- `timestamp` – Used as the point
  timestamp.
- Keys referenced by `tableName` (via
  `${...}` or `@{...}`) – Used as the
  table name.
- Keys referenced by tag value (via `${...}` or
  `@{...}`) – Used as tag values.

## Error actions

If the InfluxDB action fails, the configured error action is
triggered.

### Using InfluxDB as an error action

You can configure the InfluxDB action as an error action for any rule. The
entire payload is written to a single `tableName` as one record.
Message-scope substitution templates (`${...}`) are supported in
the error action's `tableName` and `tags`.

### Error action output

When the error action is triggered, the output payload contains:
`ruleName`, `topic`,
`cloudwatchTraceId`, `clientId`,
`sourceIp`, `base64OriginalPayload`
(Base64-encoded original message), and a `failures` array where
each entry has `failedAction`, `failedResource`, and
`errorMessage`.

With server-side batching, the payload uses
`payloadsWithMetadata`, with one entry for each distinct
inbound MQTT message. Each failure's `affectedIds` values refer
to the `id` values of those message entries; they are not point
indices. A client-side JSON array is one inbound message even though it
produces multiple InfluxDB points. For the complete payload format, see
[Error Actions for Batching](http_batching.md#batching_errors "http_batching.md#batching_errors").

| Failure scenario                    | Description                                                                                                                                                                        |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Destination DISABLED or ERROR       | The InfluxDB action destination is not enabled. Verify<br>endpoint ownership validation succeeded.                                                                                 |
| Invalid destination ARN             | The specified destination does not exist.                                                                                                                                          |
| Invalid role ARN                    | The IAM role does not exist or lacks<br>permissions.                                                                                                                               |
| Secret retrieval failure            | The secret or configured `secretKey` does not<br>exist, or the rule action role cannot retrieve or decrypt<br>the secret.                                                          |
| Missing timestamp                   | The payload does not contain a `timestamp`<br>key. Each object in the payload must include a<br>`timestamp` field with an integer Unix epoch<br>value.                             |
| Invalid timestamp value             | The timestamp value is not an integer (for example, a<br>string, float, or ISO-8601 date). The value must be an<br>integer Unix epoch in the unit specified by<br>`timestampUnit`. |
| Invalid payload (no fields)         | The payload contains no valid fields for line protocol<br>after removing reserved keys.                                                                                            |
| Invalid field key                   | A field key is empty or starts with<br>`_`.                                                                                                                                        |
| Client batch contains invalid point | One or more elements in a JSON array failed line-protocol<br>validation.                                                                                                           |
| Tags + fields exceed column limit   | Combined tag and field keys exceed the maximum column<br>count (250).                                                                                                              |
| Connection failure                  | AWS IoT Core could not connect to the InfluxDB<br>endpoint.                                                                                                                        |
| Authentication failure              | The InfluxDB token is invalid or expired. Update the<br>secret in AWS Secrets Manager.                                                                                             |
| Resource not found                  | The specified database, table, or organization does not<br>exist in InfluxDB.                                                                                                      |
| Field type conflict                 | One or more fields conflict with the existing schema. The<br>entire batch write fails.                                                                                             |
| InfluxDB server error               | An internal error occurred in InfluxDB.                                                                                                                                            |
| InfluxDB service unavailable        | InfluxDB is temporarily unavailable. The Rules Engine<br>retries with exponential backoff.                                                                                         |

###### Important

A field type conflict on any point in a batch causes the entire batch
write to fail. InfluxDB does not partially commit points — either
all points succeed or the entire write is rejected.

Retryable errors (503) are retried with exponential backoff. For an HTTP
401 response, AWS IoT Core reloads the token from AWS Secrets Manager and retries the
request once. Non-retryable errors (404, 422) trigger the error action
immediately. For retry limits, see [AWS IoT Core service
quotas](../../../general/latest/gr/iot-core.md#limits_iot "../../../general/latest/gr/iot-core.md#limits_iot").

## Examples

### InfluxDB rule action

```
{
  "topicRulePayload": {
    "sql": "SELECT * FROM 'devices/+/telemetry'",
    "ruleDisabled": false,
    "awsIotSqlVersion": "2016-03-23",
    "actions": [
      {
        "influxDB": {
          "destinationArn": "arn:aws:iot:us-west-2:111122223333:ruledestination/influxdb/a1b2c3d4",
          "roleArn": "arn:aws:iam::111122223333:role/iot-influxdb-role",
          "organization": "my-org",
          "databaseName": "sensor_data",
          "tableName": "device_metrics",
          "tags": {
            "device_id": "${clientid()}",
            "location": "building-a"
          },
          "timestampUnit": "ms"
        }
      }
    ]
  }
}
```

**Sample payload:**

```
{
  "timestamp": 1700000000000,
  "temperature": 23.5,
  "humidity": 60.1,
  "pressure": 1013.25,
  "battery_level": 87
}
```

**Resulting line protocol:**

```
device_metrics,device_id=myDevice123,location=building-a temperature=23.5,humidity=60.1,pressure=1013.25,battery_level=87i 1700000000000
```

Field order in the output may vary — fields are not sorted
alphabetically.

### Client-batched array payload with per-element templates

```
{
  "influxDB": {
    "destinationArn": "arn:aws:iot:us-west-2:111122223333:ruledestination/influxdb/a1b2c3d4",
    "roleArn": "arn:aws:iam::111122223333:role/iot-influxdb-role",
    "organization": "my-org",
    "databaseName": "sensor_data",
    "tableName": "@{measurement_type}",
    "tags": {
      "sensor_id": "@{sensor_id}",
      "location": "${topic(2)}"
    },
    "timestampUnit": "ns"
  }
}
```

**Sample payload (published to
`devices/floor3/telemetry`):**

```
[
  {"measurement_type": "temperature", "sensor_id": "sensor-42", "timestamp": 1700000000000000000, "value": 23.5},
  {"measurement_type": "humidity", "sensor_id": "sensor-42", "timestamp": 1700000001000000000, "value": 60.1},
  {"measurement_type": "pressure", "sensor_id": "sensor-43", "timestamp": 1700000002000000000, "value": 1013.25}
]
```

**Resulting line protocol:**

```
temperature,location=floor3,sensor_id=sensor-42 value=23.5 1700000000000000000
humidity,location=floor3,sensor_id=sensor-42 value=60.1 1700000001000000000
pressure,location=floor3,sensor_id=sensor-43 value=1013.25 1700000002000000000
```

### Server-side batching with InfluxDB

To add server-side batching to any InfluxDB action, include
`batchConfig` in the action configuration:

```
"batchConfig": {
  "maxBatchSize": 50,
  "maxBatchOpenMs": 1000,
  "maxBatchSizeBytes": 65536,
  "batchAcrossTopics": false
}
```

### IAM policy for the rule action role

**Trust policy:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {"Service": "iot.amazonaws.com"},
      "Action": "sts:AssumeRole"
    }
  ]
}
```

**Permission policy:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "arn:aws:secretsmanager:us-west-2:111122223333:secret:my-influxdb-secret-a1b2c3"
    }
  ]
}
```

### Combined client-side and server-side batching (point reordering)

When you enable both client-side batching (JSON array payloads) and
server-side batching (`batchConfig`), be aware that the
server-side batch may reorder points from a client-side batched payload. The
Rules Engine accumulates points from multiple incoming messages into a
single server-side batch. Because messages arrive asynchronously from
different devices or topics, points that were ordered within the original
client payload may be interleaved with points from other messages in the
final write.

Action configuration:

```
{
  "influxDB": {
    "destinationArn": "arn:aws:iot:us-west-2:111122223333:ruledestination/influxdb/abc123",
    "roleArn": "arn:aws:iam::111122223333:role/iot-influxdb-role",
    "databaseName": "sensor_data",
    "tableName": "@{measurement_type}",
    "tags": {
      "device_id": "${topic(2)}",
      "floor": "@{floor}"
    },
    "timestampUnit": "ms",
    "batchConfig": {
      "maxBatchSize": 100,
      "maxBatchOpenMs": 500,
      "maxBatchSizeBytes": 65536,
      "batchAcrossTopics": true
    }
  }
}
```

Device A publishes to `devices/deviceA/telemetry` at time
T:

```
[
  {"measurement_type": "temperature", "floor": "1", "timestamp": 1700000000000, "value": 22.1},
  {"measurement_type": "temperature", "floor": "2", "timestamp": 1700000000100, "value": 23.4},
  {"measurement_type": "humidity", "floor": "1", "timestamp": 1700000000200, "value": 55.0}
]
```

Device B publishes to `devices/deviceB/telemetry` at time
T+10ms:

```
[
  {"measurement_type": "temperature", "floor": "3", "timestamp": 1700000000050, "value": 21.8},
  {"measurement_type": "humidity", "floor": "3", "timestamp": 1700000000150, "value": 62.3}
]
```

Both messages arrive within the 500ms batch window
(`maxBatchOpenMs`), so the Rules Engine combines all five
points into a single server-side batch.

Resulting line protocol (server-side batch write):

```
temperature,device_id=deviceB,floor=3 value=21.8 1700000000050
temperature,device_id=deviceA,floor=1 value=22.1 1700000000000
temperature,device_id=deviceA,floor=2 value=23.4 1700000000100
humidity,device_id=deviceB,floor=3 value=62.3 1700000000150
humidity,device_id=deviceA,floor=1 value=55.0 1700000000200
```

Notice that the points are no longer in the order they appeared within
each client payload. The three points from Device A (timestamps
1700000000000, 1700000000100, 1700000000200) are interleaved with the two
points from Device B (timestamps 1700000000050, 1700000000150). The
server-side batch does not guarantee the original ordering within each
message.
InfluxDB uses the timestamp field to place each point on the timeline, so
reordering does not affect query correctness. However, if your application
relies on write-order semantics (for example, handling field type conflicts
or last-write-wins deduplication within the same millisecond), be aware that
the effective write order may differ from the publish order.
