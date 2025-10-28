# Kafka connector for Amazon EventBridge

The Kafka sink connector for EventBridge allows you convert records from one or more Kafka topics into events,
and send those events to the event bus of your choice.

The connector includes the following capabilities:

- Customizable mapping of Kafka records to event types.

You can customize the mapping of Kafka topic names to the event type, including
using JsonPath expressions. This enables you to configure the connector to consume
from multiple Kafka topics and filter the events sent to the specified event
bus.

- Offload large event payloads to Amazon S3.

Kafka topics can contain records exceeding the size limit of [PutEvents](eb-putevents.md "eb-putevents.md").
You can configure the connector to offload events to Amazon S3 prior to calling PutEvents.

- Support for dead-letter topics.
- Schema registry support for Avro and Protocol Buffers (Protobuf)
  The [Kafka Connector for Amazon EventBridge](https://github.com/awslabs/eventbridge-kafka-connector/blob/main/README.md "https://github.com/awslabs/eventbridge-kafka-connector/blob/main/README.md") is available on GitHub.
  For detailed instruction on installing and configuring the connector using Amazon MSK Connect, see [Set up EventBridge Kafka sink connector for Amazon MSK Connect](../../../msk/latest/developerguide/mkc-eventbridge-kafka-connector.md "../../../msk/latest/developerguide/mkc-eventbridge-kafka-connector.md") in the _Amazon Managed Streaming for Apache Kafka Developer Guide_.
