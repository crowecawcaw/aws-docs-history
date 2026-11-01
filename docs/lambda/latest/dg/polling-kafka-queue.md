

# Polling Kafka topics in Queue mode
<a name="polling-kafka-queue"></a>

Queue mode is a consumption mode that uses share groups, which became available in Apache Kafka 4.0 (the Kafka Queue Poller requires version 4.2 or later). With Queue mode, you can process Kafka topic messages in an unordered, high-throughput way using share groups. Unlike traditional Kafka consumer groups that assign partitions exclusively to consumers, share groups let multiple consumers read from the same partitions concurrently. This is similar to how Amazon SQS processes messages from a queue.

When you create an event source mapping for a self-managed Apache Kafka cluster, you can choose between two consumption modes:
+ **Stream** (default). Uses Kafka consumer groups with per-partition ordering. Lambda assigns each partition to one consumer.
+ **Queue**. Uses share groups, which became available in Apache Kafka 4.0, for unordered, high-throughput processing (the Kafka Queue Poller requires version 4.2 or later). With share groups, multiple consumers can read from the same partitions concurrently, similar to how Amazon SQS processes messages from a queue.

If you don't specify a consumption mode, the event source mapping uses Stream. This page covers the Queue consumption mode. For general information about using Lambda with self-managed Apache Kafka, see [Using Lambda with self-managed Apache Kafka](with-kafka.md).

In Queue mode, Lambda uses the Kafka Share Consumer to poll messages from the topic. Each event poller processes messages across all partitions without partition-level ordering. This increases concurrency for each poller.

## Minimum requirements
<a name="kafka-queue-requirements"></a>

To use the Queue consumption mode, your Kafka cluster must meet the following requirements:
+ Apache Kafka version 4.2 or later with share groups enabled. Kafka enables `share.version` by default, and you can manage it through `kafka-features.sh`.
+ Self-managed Apache Kafka (SMK) clusters only. Amazon Managed Streaming for Apache Kafka (Amazon MSK) does not currently support Queue mode. AWS adds MSK support once MSK offers Kafka 4.2 or later with share groups enabled.

## Stream and Queue comparison
<a name="kafka-queue-comparison"></a>


| Feature | Stream (default) | Queue | 
| --- | --- | --- | 
| Ordering | Per-partition ordering guaranteed | No ordering guarantee | 
| Consumer model | Consumer group (exclusive partition assignment) | Share group (concurrent partition access) | 
| Throughput per event poller | Up to 5 MB/s | Up to 5 MB/s | 
| Concurrent invocations per event poller | Up to 5 | Up to 10 | 
| Scaling modes | On-demand and provisioned | On-demand and provisioned | 
| EPU sharing | Can share EPUs with other Kafka Streams event source mappings | Isolated. Queue event source mappings share only with other Queue event source mappings | 
| Use case | Ordered event processing | High-throughput unordered workloads | 

## Create queue mapping
<a name="kafka-queue-create"></a>

To create a Queue mode event source mapping, set the `ConsumptionMode` field of `SelfManagedKafkaEventSourceConfig` to `Queue`. In the following examples, replace `my-function`, the broker endpoints, and `my-queue-topic` with your own values.

### AWS CLI
<a name="kafka-queue-create-cli"></a>

The following AWS CLI command creates a Queue mode event source mapping. Replace {{my-function}} with your function name, the broker endpoints with your brokers, and {{my-queue-topic}} with your topic.

```
PROMPT> aws lambda create-event-source-mapping \
  --function-name {{my-function}} \
  --self-managed-event-source '{"Endpoints":{"KAFKA_BOOTSTRAP_SERVERS":["{{broker1.us-west-2.example.com:9092}}","{{broker2.us-west-2.example.com:9092}}"]}}' \
  --topics {{my-queue-topic}} \
  --batch-size 100 \
  --self-managed-kafka-event-source-config '{"ConsumptionMode": "Queue"}' \
  --provisioned-poller-config '{"MinimumPollers": 1, "MaximumPollers": 10}'
```

### AWS CloudFormation
<a name="kafka-queue-create-cfn"></a>

The following AWS CloudFormation template creates a Queue mode event source mapping. Replace the broker endpoints and {{my-queue-topic}} with your own values.

```
MyKafkaQueueESM:
  Type: AWS::Lambda::EventSourceMapping
  Properties:
    FunctionName: !Ref MyFunction
    SelfManagedEventSource:
      Endpoints:
        KafkaBootstrapServers:
          - {{broker1.us-west-2.example.com:9092}}
          - {{broker2.us-west-2.example.com:9092}}
    Topics:
      - {{my-queue-topic}}
    BatchSize: 100
    SelfManagedKafkaEventSourceConfig:
      ConsumptionMode: Queue
    ProvisionedPollerConfig:
      MinimumPollers: 1
      MaximumPollers: 10
```

## Configuration parameters
<a name="kafka-queue-parameters"></a>

The following table lists the parameters that are applicable to Queue mode event source mappings.


| Parameter | Description | Range / Default | 
| --- | --- | --- | 
| BatchSize | Maximum number of records per batch sent to the function | 1–10,000. Default: 100 | 
| Enabled | Whether the event source mapping is active | true or false. Default: true | 
| FilterCriteria | Event filtering patterns to process only matching records | Up to 5 filter patterns | 
| MaximumRetryAttempts | Maximum retries for failed records | -1–10,000. Default: 0 (in Queue mode, the Kafka broker performs retries when no on-failure destination is configured) | 
| BisectBatchOnFunctionError | Split batch in half on function error | true or false. Default: false | 
| ProvisionedPollerConfig.MinimumPollers | Minimum event pollers (provisioned mode) | 1–200. Default: 1 | 
| ProvisionedPollerConfig.MaximumPollers | Maximum event pollers (provisioned mode) | 1–2,000. Default: 200 | 
| ProvisionedPollerConfig.PollerGroupName | Group name for EPU sharing (provisioned mode, Queue event source mappings only) | String. Up to 100 event source mappings per group | 
| SelfManagedKafkaEventSourceConfig.ConsumptionMode | Consumption mode for the event source | Must be Queue for Queue mode | 
| SchemaRegistryConfig | Schema registry for event validation | See [Using schema registries with Kafka event sources in Lambda](services-consume-kafka-events.md) | 

**Important**  
The `MaximumBatchingWindowInSeconds` parameter is **not supported** for Queue mode event source mappings. The Kafka Share Consumer uses explicit acknowledgement. All records in a batch must be explicitly acknowledged before the consumer can fetch new ones. This is incompatible with a time-based batching window. If you specify `MaximumBatchingWindowInSeconds` when creating a Queue mode event source mapping, the API returns a validation error.

## Supported event source mapping features
<a name="kafka-queue-supported-features"></a>

The following table lists the Lambda event source mapping features that are available with Queue mode.


| Feature | Supported | Notes | 
| --- | --- | --- | 
| Provisioned mode | Yes | Configure MinimumPollers and MaximumPollers | 
| On-demand mode | Yes | Default scaling mode. Lambda scales pollers automatically up to 5 MB/s or 50 concurrent invocations, whichever is reached first. No additional configuration required. | 
| Event filtering | Yes | Up to 5 filter patterns per event source mapping | 
| Schema registry | Yes | Avro and Protobuf with Glue Schema Registry or Confluent Schema Registry. Schema registry filtering is available in provisioned mode only. | 
| Low-latency processing | Yes | Available in provisioned mode | 
| Retry configurations | Yes | MaximumRetryAttempts, BisectBatchOnFunctionError | 
| On-failure destination (Kafka topic) | Yes | Send failed records to a Kafka topic | 
| On-failure destination (SNS/SQS) | Yes | Send failed records to SNS or SQS | 
| Event source mapping logging | Yes | CloudWatch Logs for event source mapping diagnostics | 
| Event source mapping grouping (PollerGroupName) | Yes | Queue mode event source mappings can share EPUs with other Queue mode event source mappings only (provisioned mode) | 
| Batching window | No | Not supported due to Share Consumer blocking-mode behavior | 
| Starting position | No | StartingPosition and StartingPositionTimestamp are not supported. Queue mode always reads from the share group's committed position. | 

## Scaling modes
<a name="kafka-queue-scaling"></a>

Queue mode event source mappings support both on-demand (default) and provisioned scaling modes.

### On-demand mode (default)
<a name="kafka-queue-ondemand"></a>

In on-demand mode, Lambda automatically manages event pollers for your Queue mode event source mapping.

On-demand mode scales up to 5 event pollers per event source mapping. It reaches its ceiling at either 5 MB/s aggregate throughput or 50 concurrent invocations (5 pollers times 10). This happens whichever limit is hit first. To scale beyond these limits, use provisioned mode. On-demand mode requires no additional configuration beyond the standard event source mapping parameters.

The following table lists the on-demand mode limits.


| Limit | Value | 
| --- | --- | 
| Throughput per event poller | Up to 1 MB/s | 
| Concurrent invocations per event poller | Up to 10 | 
| Maximum event pollers | 5 | 
| Maximum aggregate throughput | Up to 5 MB/s (5 pollers times 1 MB/s) | 
| Maximum aggregate concurrency | Up to 50 concurrent invocations (5 pollers times 10) | 

**Example – Queue mode event source mapping in on-demand mode (AWS CLI)**

The following AWS CLI command creates a Queue mode event source mapping in on-demand mode. Replace {{my-function}}, the broker endpoints, {{my-queue-topic}}, the subnet IDs, and the security group ID with your own values.

```
PROMPT> aws lambda create-event-source-mapping \
  --function-name {{my-function}} \
  --self-managed-event-source '{"Endpoints":{"KAFKA_BOOTSTRAP_SERVERS":["{{broker1.us-west-2.example.com:9092}}","{{broker2.us-west-2.example.com:9092}}"]}}' \
  --topics {{my-queue-topic}} \
  --batch-size 100 \
  --self-managed-kafka-event-source-config '{"ConsumptionMode": "Queue"}' \
  --source-access-configurations '[{"Type":"VPC_SUBNET","URI":"{{subnet-0123456789abcdef0}}"},{"Type":"VPC_SUBNET","URI":"{{subnet-0123456789abcdef1}}"},{"Type":"VPC_SECURITY_GROUP","URI":"{{sg-0123456789abcdef0}}"}]'
```

### Provisioned mode
<a name="kafka-queue-provisioned"></a>

For workloads with strict performance requirements or spiky traffic patterns, use provisioned mode. Provisioned mode gives you direct control over the minimum and maximum number of event pollers dedicated to your Queue mode event source mapping.

Each Queue mode event poller in provisioned mode supports up to 5 MB/s of throughput and up to 10 concurrent Lambda invocations.

The following table lists the provisioned mode limits.


| Limit | Value | 
| --- | --- | 
| Throughput per event poller | Up to 5 MB/s | 
| Concurrent invocations per event poller | Up to 10 | 
| Minimum event pollers (MinimumPollers) | 1–200. Default: 1 | 
| Maximum event pollers (MaximumPollers) | 1–2,000. Default: 200 | 
| Event source mappings per poller group | Up to 100 | 
| Aggregate maximum pollers per poller group | 2,000 | 
| Throughput per EPU (aggregate) | Up to 5 MB/s per poller; aggregate depends on poller packing density | 

Provisioned mode is charged based on Event Poller Unit (EPU) usage. For pricing details, see [AWS Lambda Pricing](https://aws.amazon.com/lambda/pricing/).

**Example – Queue mode event source mapping with provisioned mode (AWS CLI)**

The following AWS CLI command creates a Queue mode event source mapping in provisioned mode.

```
PROMPT> aws lambda create-event-source-mapping \
  --function-name {{my-function}} \
  --self-managed-event-source '{"Endpoints":{"KAFKA_BOOTSTRAP_SERVERS":["{{broker1.us-west-2.example.com:9092}}","{{broker2.us-west-2.example.com:9092}}"]}}' \
  --topics {{my-queue-topic}} \
  --batch-size 100 \
  --self-managed-kafka-event-source-config '{"ConsumptionMode": "Queue"}' \
  --provisioned-poller-config '{"MinimumPollers": 5, "MaximumPollers": 100}' \
  --source-access-configurations '[{"Type":"VPC_SUBNET","URI":"{{subnet-0123456789abcdef0}}"},{"Type":"VPC_SUBNET","URI":"{{subnet-0123456789abcdef1}}"},{"Type":"VPC_SECURITY_GROUP","URI":"{{sg-0123456789abcdef0}}"}]'
```

Replace the following placeholders with your own values:
+ {{subnet-0123456789abcdef0}} and {{subnet-0123456789abcdef1}}: your subnet IDs.
+ {{sg-0123456789abcdef0}}: your security group ID.
+ `MinimumPollers` and `MaximumPollers`: set according to your throughput needs.

**Note**  
To switch from provisioned mode back to on-demand mode, pass an empty `ProvisionedPollerConfig`:  

```
PROMPT> aws lambda update-event-source-mapping \
  --uuid a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
  --provisioned-poller-config '{}'
```

### Scaling mode selection
<a name="kafka-queue-scaling-choice"></a>


| Consideration | On-demand | Provisioned | 
| --- | --- | --- | 
| Setup | No additional configuration | Configure MinimumPollers and MaximumPollers | 
| Cost | No additional EPU charges | EPU charges based on usage per hour | 
| Best for | Low-concurrency workloads | Strict latency requirements, spiky traffic | 
| Event source mapping grouping (PollerGroupName) | Not supported | Supported. Share EPUs across Queue event source mappings | 
| Low-latency processing | Not available | Available | 
| Schema registry filtering (Avro/Protobuf) | Not available | Available | 

## EPU sharing isolation
<a name="kafka-queue-epu-sharing"></a>

In provisioned mode, you can group multiple event source mappings within the same VPC to share Event Poller Unit (EPU) capacity by assigning them the same `PollerGroupName`. Event source mapping grouping lets low-throughput event source mappings pack onto shared EPUs instead of each requiring dedicated capacity, reducing provisioned-mode cost. For details, see [Cost Optimization for Provisioned mode](kafka-scaling-modes.md#kafka-cost-optimization).

**Queue mode event source mappings share EPUs only with other Queue mode event source mappings.** A `PollerGroupName` used by a Queue mode event source mapping cannot be shared with a Kafka Streams event source mapping, and vice versa. If you configure a `PollerGroupName` already in use by the other consumption mode, `CreateEventSourceMapping` returns a validation error. To use event source mapping grouping with Queue mode, create a `PollerGroupName` dedicated to your Queue event source mappings.

## Example event
<a name="kafka-queue-example-event"></a>

When Lambda invokes your function with a Queue mode event source, the event payload is identical to a standard Kafka event. Each record includes the topic, partition, offset, timestamp, and base64-encoded key and value:

```
{
  "eventSource": "SelfManagedKafka",
  "bootstrapServers": "broker1.example.com:9092,broker2.example.com:9092",
  "records": {
    "my-queue-topic-0": [
      {
        "topic": "my-queue-topic",
        "partition": 0,
        "offset": 15,
        "timestamp": 1545084650987,
        "timestampType": "CREATE_TIME",
        "key": "abcDEFghiJKLmnoPQRstuVWXyz1234==",
        "value": "SGVsbG8sIHRoaXMgaXMgYSB0ZXN0Lg==",
        "headers": [
          {
            "headerKey": [104, 101, 97, 100, 101, 114, 86, 97, 108, 117, 101]
          }
        ]
      }
    ],
    "my-queue-topic-3": [
      {
        "topic": "my-queue-topic",
        "partition": 3,
        "offset": 42,
        "timestamp": 1545084651000,
        "timestampType": "CREATE_TIME",
        "key": "YW5vdGhlcktleQ==",
        "value": "VGhpcyBpcyBhbm90aGVyIG1lc3NhZ2U=",
        "headers": []
      }
    ]
  }
}
```

**Idempotency required**  
Lambda event source mappings process each event at least once, so duplicate processing of records can occur. Because Queue mode does not guarantee ordering, duplicate or out-of-order processing can produce incorrect results, such as double-counting or inconsistent state, if your function code is not idempotent. Make your function code idempotent.

## Limitations
<a name="kafka-queue-limitations"></a>
+ **Self-managed Kafka clusters only.** Amazon MSK is not supported at launch.
+ **Apache Kafka 4.2 or later required.** The cluster must support the Share Consumer protocol with share groups enabled.
+ **Batching window not supported.** The `MaximumBatchingWindowInSeconds` parameter cannot be used with Kafka Queue event source mappings.
+ **Starting position not supported.** `StartingPosition` and `StartingPositionTimestamp` cannot be used with Queue mode event source mappings. The share group consumes from its committed offset position.
+ **EPU isolation.** Queue mode event source mappings cannot share EPUs with Kafka Streams event source mappings. Use separate `PollerGroupName` values.