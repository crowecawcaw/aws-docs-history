

# Substitution templates
<a name="iot-substitution-templates"></a>

You can use a substitution template to augment the JSON data returned when a rule is triggered and AWS IoT performs an action. The syntax for a substitution template is `${`*expression*`}`, where *expression* can be any expression supported by AWS IoT in SELECT clauses, WHERE clauses, and [AWS IoT rule actions](iot-rule-actions.md). This expression can be plugged into an action field on a rule, allowing you to dynamically configure an action. In effect, this feature substitutes a piece of information in an action. This includes functions, operators, and information present in the original message payload.

**Important**  
Because an expression in a substitution template is evaluated separately from the "SELECT ..." statement, you can't reference an alias created using the AS clause. You can only reference information present in the original payload, [functions](iot-sql-functions.md), and [operators](iot-sql-operators.md).

For more information about supported expressions, see [AWS IoT SQL reference](iot-sql-reference.md).

The following rule actions support substitution templates. Each action supports different fields that can be substituted.
+ [Apache Kafka](apache-kafka-rule-action.md)
+ [CloudWatch alarms](cloudwatch-alarms-rule-action.md)
+ [CloudWatch Logs](cloudwatch-logs-rule-action.md)
+ [CloudWatch metrics](cloudwatch-metrics-rule-action.md)
+ [DynamoDB](dynamodb-rule-action.md)
+ [DynamoDBv2](dynamodb-v2-rule-action.md)
+ [Elasticsearch](elasticsearch-rule-action.md)
+ [HTTP](https-rule-action.md)
+ [InfluxDB](influxdb-rule-action.md)
+ [AWS IoT SiteWise](iotsitewise-rule-action.md)
+ [Kinesis Data Streams](kinesis-rule-action.md)
+ [Firehose](kinesis-firehose-rule-action.md)
+ [Lambda](lambda-rule-action.md)
+ [Location](location-rule-action.md)
+ [OpenSearch](opensearch-rule-action.md)
+ [Republish](republish-rule-action.md)
+ [S3](s3-rule-action.md)
+ [SNS](sns-rule-action.md)
+ [SQS](sqs-rule-action.md)
+ [Step Functions](stepfunctions-rule-action.md)
+ [Timestream](timestream-rule-action.md)

Substitution templates appear in the action parameters within a rule: 

```
{
    "sql": "SELECT *, timestamp() AS timestamp FROM 'my/iot/topic'",
    "ruleDisabled": false,
    "actions": [{
        "republish": {
            "topic": "${topic()}/republish",
            "roleArn": "arn:aws:iam::123456789012:role/my-iot-role"
        }
    }]
}
```

If this rule is triggered by the following JSON published to `my/iot/topic`:

```
{
    "deviceid": "iot123",
    "temp": 54.98,
    "humidity": 32.43,
    "coords": {
        "latitude": 47.615694,
        "longitude": -122.3359976
    }
}
```

Then this rule publishes the following JSON to `my/iot/topic/republish`, which AWS IoT substitutes from `${topic()}/republish`:

```
{
    "deviceid": "iot123",
    "temp": 54.98,
    "humidity": 32.43,
    "coords": {
        "latitude": 47.615694,
        "longitude": -122.3359976
    },
    "timestamp": 1579637878451
}
```

## Per-element substitution for array payloads in AWS IoT rules
<a name="iot-array-payload-shorthand"></a>

With AWS IoT, you can use the standard substitution template `${`*expression*`}`. This template resolves one time per message, against the message payload as the device published it, before the rule's SQL statement transforms it. If your message payload is a JSON array, use the per-element sequence `@{`*field*`}` instead. This sequence resolves one time for each element of the payload that the rule's SQL statement produces. The rule action writes one InfluxDB line-protocol point per element. It uses the value from the matching element.

**Note**  
The two sequences read different payloads, so they can resolve to different values for the same field name. If the rule's SQL statement renames or reshapes fields, inside `@{`*field*`}` you must reference the field name as it appears in the SQL output. If an element doesn't contain the field, the sequence resolves to an empty value. It doesn't fall back to a message-level value, and AWS IoT drops an empty tag value from the line protocol that it writes.

**Important**  
The `@{`*field*`}` sequence works only in the AWS IoT InfluxDB rule action configuration. It doesn't work in these places:  
The rule SQL statement (the SELECT, WHERE, or SET clauses)
Any other rule action
A function. The sequence can't contain one, such as `@{upper(room)}`. You also can't pass the sequence to a substitution template function, because a single configuration value can't contain both `@{...}` and `${...}`.
The rule's error action, even when that error action is an InfluxDB action. The error action runs one time for the message, so it never resolves per element.
If you use it in any of these places, the `CreateTopicRule` and `ReplaceTopicRule` operations fail with an error.

The per-element sequence `@{`*field*`}` has the following requirements:
+ Must reference a single field, such as `@{room}` or `@{meta.sensor_id}`
+ Must not include functions, arithmetic, comparisons, or literals
+ Must appear at most one time in a configuration value
+ Must not appear in the same configuration value as a `${...}` substitution template
+ Must appear in a configuration value, not a key (for example, an InfluxDB tag value but not a tag key)

**Map array elements to InfluxDB points**  
In this example, an InfluxDB rule action sets the measurement name (`tableName`) to `@{measurement_type}` and a `location` tag to `@{room}`:

```
{
  "topicRulePayload": {
    "sql": "SELECT * FROM 'iot/topic'",
    "ruleDisabled": false,
    "awsIotSqlVersion": "2016-03-23",
    "actions": [
      {
        "influxDB": {
          "destinationArn": "{{arn:aws:iot:us-east-1:123456789012:ruledestination/influxdb/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}",
          "roleArn": "arn:aws:iam::123456789012:role/aws_iot_influxdb",
          "databaseName": "device_metrics",
          "tableName": "@{measurement_type}",
          "organization": "my_organization",
          "tags": {
            "location": "@{room}"
          },
          "timestampUnit": "ms"
        }
      }
    ]
  }
}
```

The following array payload triggers the rule:

```
[
    { "measurement_type": "temperature", "room": "kitchen", "value": 5,  "timestamp": 1700000000000 },
    { "measurement_type": "humidity",    "room": "bedroom", "value": 15, "timestamp": 1700000001000 }
]
```

The action writes one InfluxDB line-protocol point for each element of the array. Each element resolves `@{measurement_type}` to its own measurement name and `@{room}` to its own `location` tag:

```
temperature,location=kitchen value=5i 1700000000000
humidity,location=bedroom value=15i 1700000001000
```

**Note**  
AWS IoT excludes any field that a `@{`*field*`}` sequence references from the field set. AWS IoT uses that field's value as the measurement name or tag value. In this example, `measurement_type` supplies the measurement and `room` supplies the `location` tag. AWS IoT excludes both, so each point keeps only `value` as a field.

The preceding example uses `SELECT *`, so the payload that the action receives matches the payload that the device published. If the SQL statement renames a field, use the name that appears in the SQL output. For example, if the statement includes `room AS location_name`, use `@{location_name}` instead of `@{room}`.

**Resolve against a payload that the SQL statement produces**  
The payload that the action receives isn't always the payload that the device published. In this example, the device publishes an object that contains an array of readings:

```
{
    "device_id": "sensor-1",
    "readings": [
        { "measurement_type": "temperature", "room": "kitchen", "value": 5,  "timestamp": 1700000000000 },
        { "measurement_type": "humidity",    "room": "bedroom", "value": 15, "timestamp": 1700000001000 }
    ]
}
```

The rule uses `SELECT VALUE` to return the `readings` array as the top-level payload. For more information, see [Output an `Array` as a top-level object](iot-rule-sql-version.md#return-array-rule).

```
SELECT VALUE readings FROM 'iot/topic'
```

The action receives the following array, even though the device published an object. It writes the same two points as the preceding example, because each element still contains `measurement_type`, `room`, and `value`.

```
[
    { "measurement_type": "temperature", "room": "kitchen", "value": 5,  "timestamp": 1700000000000 },
    { "measurement_type": "humidity",    "room": "bedroom", "value": 15, "timestamp": 1700000001000 }
]
```

**Note**  
The `device_id` field is in the payload that the device published, but not in the array that the SQL statement produces. For that reason, `@{device_id}` doesn't resolve in this rule. Reference only fields that appear in the elements of the produced array.