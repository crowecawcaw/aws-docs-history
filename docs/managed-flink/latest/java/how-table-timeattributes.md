Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Table API time attributes

Each record in a data stream has several timestamps that define when events related to the record occurred:

- **Event Time**: A user-defined timestamp that defines when the
  event that created the record occurred.
- **Ingestion Time**: The time when your application retrieved the
  record from the data stream.
- **Processing Time**: The time when your application processed the
  record.
  When the Apache Flink Table API creates windows based on record times, you define
  which of these timestamps it uses by using the `setStreamTimeCharacteristic`
  method.

For more information about using timestamps with the Table API, see [Time Attributes](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/concepts/time_attributes/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/table/concepts/time_attributes/") and [Timely Stream Processing](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/concepts/time/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/concepts/time/") in the Apache Flink
Documentation.
