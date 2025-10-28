Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Precautions and known issues with application

upgrades

## Kafka Commit on checkpointing fails repeatedly after a

broker restart

There is a known open source Apache Flink issue with the Apache Kafka connector in
Flink version 1.15 caused by a critical open source Kafka Client bug in Kafka Client
2.8.1. For more information, see [Kafka Commit on checkpointing fails repeatedly after a broker restart](https://issues.apache.org/jira/browse/FLINK-28060 "https://issues.apache.org/jira/browse/FLINK-28060")
and [KafkaConsumer is unable to recover connection to group coordinator after commitOffsetAsync exception](https://issues.apache.org/jira/browse/KAFKA-13840 "https://issues.apache.org/jira/browse/KAFKA-13840").

To avoid this issue, we recommend that you use Apache Flink 1.18 or later in
Amazon Managed Service for Apache Flink.

## Known limitations of state compatibility

- If you are using the Table API, Apache Flink doesn't guarantee state
  compatibility between Flink versions. For more information, see [Stateful Upgrades and Evolution](https://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/concepts/overview/#stateful-upgrades-and-evolution "https://nightlies.apache.org/flink/flink-docs-master/docs/dev/table/concepts/overview/#stateful-upgrades-and-evolution") in the Apache Flink
  documentation.
- Flink 1.6 states are not compatible with Flink 1.18. The API rejects your
  request if you try to upgrade from 1.6 to 1.18 and later with state. You can
  upgrade to 1.8, 1.11, 1.13 and 1.15 and take a snapshot, and then upgrade to
  1.18 and later. For more information, see [Upgrading Applications and Flink Versions](https://nightlies.apache.org/flink/flink-docs-master/docs/ops/upgrading/ "https://nightlies.apache.org/flink/flink-docs-master/docs/ops/upgrading/") in the Apache Flink
  documentation.

## Known issues with the Flink Kinesis Connector

- If you are using Flink 1.11 or earlier and using the
  `amazon-kinesis-connector-flink` connector for
  Enhanced-fan-out (EFO) support, you must take extra steps for a stateful
  upgrade to Flink 1.13 or later. This is because of the change in the package
  name of the connector. For more information, see [amazon-kinesis-connector-flink](https://github.com/awslabs/amazon-kinesis-connector-flink "https://github.com/awslabs/amazon-kinesis-connector-flink").

The `amazon-kinesis-connector-flink` connector for Flink
1.11 and earlier uses the packaging
`software.amazon.kinesis`, whereas the Kinesis connector for
Flink 1.13 and later uses
`org.apache.flink.streaming.connectors.kinesis`. Use this
tool to support your migration: [amazon-kinesis-connector-flink-state-migrator](https://github.com/awslabs/amazon-kinesis-connector-flink-state-migrator "https://github.com/awslabs/amazon-kinesis-connector-flink-state-migrator").

- If you are using Flink 1.13 or earlier with `FlinkKinesisProducer`
  and upgrading to Flink 1.15 or later, for a stateful upgrade you must continue
  to use `FlinkKinesisProducer` in Flink 1.15 or later, instead of the
  newer `KinesisStreamsSink`. However, if you already have a custom
  `uid` set on your sink, you should be able to switch to
  `KinesisStreamsSink` because `FlinkKinesisProducer`
  doesn't keep state. Flink will treat it as the same operator because a custom
  `uid` is set.

## Flink applications written in Scala

- As of Flink 1.15, Apache Flink doesn't include Scala in the runtime. You must include the version of Scala you want to use and other Scala
  dependencies in your code JAR/zip when upgrading to Flink 1.15 or later. For more information, see [Amazon Managed Service for Apache Flink for Apache Flink 1.15.2 release](flink-1-15-2.md "flink-1-15-2.md").
- If your application uses Scala and you are upgrading it from Flink 1.11 or
  earlier (Scala 2.11) to Flink 1.13 (Scala 2.12), make sure that your code uses
  Scala 2.12. Otherwise, your Flink 1.13 application may fail to find Scala 2.11
  classes in the Flink 1.13 runtime.

## Things to consider when downgrading Flink application

- Downgrading Flink applications is possible, but limited to cases when the
  application was previously running with the older Flink version. For a stateful upgrade
  Managed Service for Apache Flink will require using a snapshot taken with matching
  or earlier version for the downgrade
- If you are updating your runtime from Flink 1.13 or later to Flink 1.11 or
  earlier, and if your app uses the HashMap state backend, your application will
  continuously fail.
