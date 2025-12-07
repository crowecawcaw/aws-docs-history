# Using the Spark structured

streaming Amazon Kinesis Data Streams connector

Amazon EMR releases 7.1.0 and higher include a spark structured streaming Amazon Kinesis Data Streams
connector in the release image. With this connector, you can use Spark on Amazon EMR to
process data that's stored in Amazon Kinesis Data Streams. The connector supports both consumer types of
`GetRecords` (shared throughput) and `SubscribeToShard`
(enhanced fan-out). This integration is based on the [`spark-sql-kinesis-connector`](https://github.com/awslabs/spark-sql-kinesis-connector "https://github.com/awslabs/spark-sql-kinesis-connector"). For details about how to get started
using the connector, see the [README](https://github.com/awslabs/spark-sql-kinesis-connector/blob/main/README.md "https://github.com/awslabs/spark-sql-kinesis-connector/blob/main/README.md").

The following example demonstrates how to use the connector to launch a Spark
application with Amazon EMR

```
spark-submit `my_kinesis_streaming_script.py`
```
