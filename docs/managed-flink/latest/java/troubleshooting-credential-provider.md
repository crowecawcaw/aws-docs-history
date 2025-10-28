Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Credential provider issue with EFO

connector 1.15.2

There is a [known issue](https://issues.apache.org/jira/browse/FLINK-29205 "https://issues.apache.org/jira/browse/FLINK-29205") with Kinesis Data Streams EFO connector versions up to 1.15.2 where the
`FlinkKinesisConsumer` is not respecting `Credential Provider` configuration. Valid configurations are being disregarded due to the issue, which results in the `AUTO` credential provider being used. This can cause a problem using cross-account access to Kinesis using EFO connector.

To resolve this error please use EFO connector version 1.15.3 or higher.
