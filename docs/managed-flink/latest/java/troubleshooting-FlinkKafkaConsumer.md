Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# FlinkKafkaConsumer issue with stop with savepoint

When using the legacy FlinkKafkaConsumer there is a possibility your application may get stuck in UPDATING, STOPPING or SCALING,
if you have system snapshots enabled. There is no published fix available for this [issue](https://issues.apache.org/jira/browse/FLINK-28758 "https://issues.apache.org/jira/browse/FLINK-28758"), therefore we recommend you upgrade
to the new [KafkaSource](https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/kafka/#kafka-source "https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/kafka/#kafka-source") to mitigate this issue.

If you are using the `FlinkKafkaConsumer` with snapshots enabled, there is a possibility when the Flink job processes a stop with savepoint API
request, the `FlinkKafkaConsumer` can fail with a runtime error reporting a `ClosedException`. Under these conditions the Flink application becomes stuck, manifesting as Failed Checkpoints.
