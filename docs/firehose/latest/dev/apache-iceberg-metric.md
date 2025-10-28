# Monitor metrics

For data delivery to Apache Iceberg Tables, Firehose emits the following CloudWatch metrics at
a stream level.

| Metric                                 | Description                                                                                                                                                                 |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `DeliveryToIceberg.Bytes`              | The number of bytes delivered to Apache Iceberg Tables over the specified time period. Units: Bytes                                                                         |
| `DeliveryToIceberg.IncomingRowCount`   | Number of records that Firehose attempts to deliver to Apache Iceberg Tables. Units: Count                                                                                  |
| `DeliveryToIceberg.SuccessfulRowCount` | Number of successful rows delivered to Apache Iceberg Tables. Units: Count                                                                                                  |
| `DeliveryToIceberg.FailedRowCount`     | Number of failed rows delivered to S3 backup bucket. Units: Count                                                                                                           |
| `DeliveryToIceberg.DataFreshness`      | The age (from getting into Firehose to now) of the earliest record in Firehose. Any record earlier than this age has been delivered to Apache Iceberg Tables.Units: Seconds |
| `DeliveryToIceberg.Success`            | Sum of successful commits to Apache Iceberg Tables.                                                                                                                         |
| `JQProcessing.Duration`                | The amount of time it took to run the JQ expression.Units: Milliseconds                                                                                                     |
