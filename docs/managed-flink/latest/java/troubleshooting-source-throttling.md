Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Upstream or source throttling from a Kinesis data

stream

**Symptom**: The application is encountering
`LimitExceededExceptions` from their upstream source Kinesis data stream.

**Potential Cause**: The default setting for the Apache Flink
library Kinesis connector is set to read from the Kinesis data stream source with a very
aggressive default setting for the maximum number of records fetched per
`GetRecords` call. Apache Flink is configured by default to fetch 10,000
records per `GetRecords` call (this call is made by default every 200 ms),
although the limit per shard is only 1,000 records.

This default behavior can lead to throttling when attempting to consume from the Kinesis data
stream, which will affect the applications performance and stability.

You can confirm this by checking the CloudWatch `ReadProvisionedThroughputExceeded`
metric and seeing prolonged or sustained periods where this metric is greater than
zero.

You can also see this in CloudWatch logs for your Amazon Managed Service for Apache Flink application by observing continued
`LimitExceededException` errors.

**Resolution**: You can do one of two things to resolve this
scenario:

- Lower the default limit for the number of records fetched per `GetRecords`
  call
- Enable Adaptive Reads in your Amazon Managed Service for Apache Flink application. For more information on the Adaptive
  Reads feature, see [SHARD_USE_ADAPTIVE_READS](https://nightlies.apache.org/flink/flink-docs-release-1.10/api/java/org/apache/flink/streaming/connectors/kinesis/config/ConsumerConfigConstants.html#SHARD_USE_ADAPTIVE_READS "https://nightlies.apache.org/flink/flink-docs-release-1.10/api/java/org/apache/flink/streaming/connectors/kinesis/config/ConsumerConfigConstants.html#SHARD_USE_ADAPTIVE_READS")
