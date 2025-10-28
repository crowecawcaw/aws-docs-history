# Using Kafka Streams with MSK Express brokers and MSK Serverless

Kafka Streams supports stateless and stateful transformations. Stateful transformations, such as count, aggregate, or join, use operators which store their state in internal Kafka topics. Furthermore, some stateless transformations such as groupBy or repartition store their results in internal Kafka topics. By default, Kafka Streams names these internal topics based on the corresponding operator. If these topics don't exist, Kafka Streams creates internal Kafka topics. For creating the internal topics, Kafka Streams hardcodes the segment.bytes configuration and sets it to 50 MB. [MSK Provisioned with Express brokers](msk-configuration-express-read-write.md#msk-configuration-express-topic-configuration "msk-configuration-express-read-write.md#msk-configuration-express-topic-configuration") and MSK Serverless protects some [topic configurations](serverless-config.md "serverless-config.md"), including segment.size during topic creation. Therefore, a Kafka Streams application with stateful transformations fails to create the internal topics using MSK Express brokers or MSK Serverless.

To run such Kafka Streams applications on MSK Express brokers or MSK Serverless, you must create the internal topics yourself. To do this, first identify and name the Kafka Streams operators, which require topics. Then, create the corresponding internal Kafka topics.

###### Note

- It's a best practice to name the operators manually in Kafka Streams, especially the ones which depend on internal topics. For information about naming operators, see [Naming Operators in a Kafka Streams DSL Application](https://kafka.apache.org/38/documentation/streams/developer-guide/dsl-topology-naming.html "https://kafka.apache.org/38/documentation/streams/developer-guide/dsl-topology-naming.html") in the Kafka Streams documentation.
- The internal topic name for a stateful transformation depends on the `application.id` of the Kafka Streams application and the name of the stateful operator, `application.id-statefuloperator_name`.

###### Topics

- [Creating a Kafka Streams application using MSK Express brokers or MSK Serverless](#create-kafka-streams-app-express-broker-msk-serverless "#create-kafka-streams-app-express-broker-msk-serverless")

## Creating a Kafka Streams application using MSK Express brokers or MSK Serverless

If your Kafka Streams application has its `application.id` set to `msk-streams-processing`, you can create a Kafka Streams application using MSK Express brokers or MSK Serverless. To do this, use the `count()` operator, which requires an internal topic with the name. For example, `msk-streams-processing-count-store`.

To create a Kafka Streams application, do the following:

###### Topics

- [Identify and name the operators](#create-kafka-streams-app-identify-name-operators "#create-kafka-streams-app-identify-name-operators")
- [Create the internal topics](#create-kafka-streams-app-create-internal-topics "#create-kafka-streams-app-create-internal-topics")
- [(Optional) Check the topic name](#create-kafka-streams-app-check-topic-name "#create-kafka-streams-app-check-topic-name")
- [Examples of naming operators](#create-kafka-streams-app-naming-operators-examples "#create-kafka-streams-app-naming-operators-examples")

### Identify and name the operators

1. Identify the stateful processors using the [Stateful transformations](https://kafka.apache.org/39/documentation/streams/developer-guide/dsl-api.html#stateful-transformations "https://kafka.apache.org/39/documentation/streams/developer-guide/dsl-api.html#stateful-transformations") in the Kafka Streams documentation.

Some examples of stateful processors include `count`, `aggregate`, or `join`. 2. Identify the processors that create topics for repartitioning.

The following example contains a `count()` operation, which needs a state.

```
var stream =
    paragraphStream
        .groupByKey()
        .count()
        .toStream();
```

3. To name the topic, add a name for each stateful processor. Based on the processor type, the naming is done by a different naming class. For example, `count()` operation is an aggregation operation. Therefore, it needs the `Materialized` class.

For information about the naming classes for the stateful operations, see [Conclusion](https://kafka.apache.org/38/documentation/streams/developer-guide/dsl-topology-naming.html "https://kafka.apache.org/38/documentation/streams/developer-guide/dsl-topology-naming.html") in the Kafka Streams documentation.

The following example sets the name of `count()` operator to `count-store` using the `Materialized` class.

```
var stream =
    paragraphStream
        .groupByKey()
        .count(Materialized.<String, Long, KeyValueStore<Bytes, byte[]>>as("count-store")  // descriptive name for the store
            .withKeySerde(Serdes.String())
            .withValueSerde(Serdes.Long()))
        .toStream();
```

### Create the internal topics

Kafka Streams prefixes `application.id` to names of internal topics, where `application.id` is user-defined. For example, `application.id-internal_topic_name`. The internal topics are normal Kafka topics, and you can create the topics using the information available in [Create an Apache Kafka topic](msk-serverless-create-topic.md "msk-serverless-create-topic.md") or `AdminClient` of the Kafka API.

Depending on your use case, you can use the Kafka Streams' default cleanup and retention policies, or customize their values. You define these in `cleanup.policy` and `retention.ms`.

The following example creates the topics with the `AdminClient` API and sets the `application.id` to `msk-streams-processing`.

```
try (AdminClient client = AdminClient.create(configs.kafkaProps())) {
    Collection<NewTopic> topics = new HashSet<>();
    topics.add(new NewTopic("msk-streams-processing-count-store", 3, (short) 3));
    client.createTopics(topics);
}
```

After the topics are created on the cluster, your Kafka Streams application can use the `msk-streams-processing-count-store` topic for the `count()` operation.

### (Optional) Check the topic name

You can use the _topography describer_ to describe the topology of your stream and view the names of the internal topics. The following example shows how to run the topology describer.

```
final StreamsBuilder builder = new StreamsBuilder();
Topology topology = builder.build();
System.out.println(topology.describe());
```

The following output shows the topology of the stream for the preceding example.

```
Topology Description:
Topologies:
   Sub-topology: 0
    Source: KSTREAM-SOURCE-0000000000 (topics: [input_topic])
      --> KSTREAM-AGGREGATE-0000000001
    Processor: KSTREAM-AGGREGATE-0000000001 (stores: [count-store])
      --> KTABLE-TOSTREAM-0000000002
      <-- KSTREAM-SOURCE-0000000000
    Processor: KTABLE-TOSTREAM-0000000002 (stores: [])
      --> KSTREAM-SINK-0000000003
      <-- KSTREAM-AGGREGATE-0000000001
    Sink: KSTREAM-SINK-0000000003 (topic: output_topic)
      <-- KTABLE-TOSTREAM-0000000002
```

For information about how to use the topology describer, see [Naming Operators in a Kafka Streams DSL Application](https://kafka.apache.org/38/documentation/streams/developer-guide/dsl-topology-naming.html "https://kafka.apache.org/38/documentation/streams/developer-guide/dsl-topology-naming.html") in the Kafka Streams documentation.

### Examples of naming operators

This section provides some examples of naming operators.

**Example of naming operator for groupByKey()**

```
groupByKey() -> groupByKey(Grouped.as("kafka-stream-groupby"))
```

**Example of naming operator for normal count()**

```
normal count() -> .count(Materialized.<String, Long, KeyValueStore<Bytes, byte[]>>as("kafka-streams-window")  // descriptive name for the store
    .withKeySerde(Serdes.String())
    .withValueSerde(Serdes.Long()))
```

**Example of naming operator for windowed count()**

```
windowed count() -> .count(Materialized.<String, Long, WindowStore<Bytes, byte[]>>as("kafka-streams-window")  // descriptive name for the store
    .withKeySerde(Serdes.String())
    .withValueSerde(Serdes.Long()))
```

**Example of naming operator for windowed suppressed()**

```
windowed suppressed() ->
Suppressed<Windowed> suppressed = Suppressed
        .untilWindowCloses(Suppressed.BufferConfig.unbounded())
        .withName("kafka-suppressed");
    .suppress(suppressed)
```
