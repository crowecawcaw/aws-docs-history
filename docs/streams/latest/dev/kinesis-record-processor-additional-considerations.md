# Handle startup, shutdown,

and throttling

Here are some additional considerations to incorporate into the design of your
Amazon Kinesis Data Streams application.

###### Topics

- [Start up data
  producers and data consumers](#kinesis-record-processor-producer-consumer-coordination "#kinesis-record-processor-producer-consumer-coordination")
- [Shut down an Amazon Kinesis Data Streams
  application](#developing-consumers-with-kcl-shutdown "#developing-consumers-with-kcl-shutdown")
- [Read throttling](#kinesis-record-processor-read-throttling "#kinesis-record-processor-read-throttling")

## Start up data

producers and data consumers

By default, the KCL begins reading records from the tip of the stream, which is
the most recently added record. In this configuration, if a data-producing application adds
records to the stream before any receiving record processors are running, the records are
not read by the record processors after they start up.

To change the behavior of the record processors so that it always reads data from the
beginning of the stream, set the following value in the properties file for your Amazon Kinesis Data Streams application:

```
initialPositionInStream = TRIM_HORIZON
```

By default, Amazon Kinesis Data Streams stores all data for 24 hours. It also supports extended retention of
up to 7 days and the long-term retention of up to 365 days. This time frame is called the
_retention period_. Setting the starting position to the
`TRIM_HORIZON` will start the record processor with the oldest data in the
stream, as defined by the retention period. Even with the `TRIM_HORIZON` setting,
if a record processor were to start after a greater time has passed than the retention
period, then some of the records in the stream will no longer be available. For this reason,
you should always have consumer applications reading from the stream and use the CloudWatch metric
`GetRecords.IteratorAgeMilliseconds` to monitor that applications are keeping
up with incoming data.

In some scenarios, it may be fine for record processors to miss the first few records in
the stream. For example, you might run some initial records through the stream to test that
the stream is working end-to-end as expected. After doing this initial verification, you
would then start your workers and begin to put production data into the stream.

For more information about the `TRIM_HORIZON` setting, see [Use shard
iterators](developing-consumers-with-sdk.md#kinesis-using-sdk-java-get-data-shard-iterators "developing-consumers-with-sdk.md#kinesis-using-sdk-java-get-data-shard-iterators").

## Shut down an Amazon Kinesis Data Streams

application

When your Amazon Kinesis Data Streams application has completed its intended task, you should shut it down by
terminating the EC2 instances on which it is running. You can terminate the instances using
the [AWS Management Console](https://console.aws.amazon.com//ec2/home "https://console.aws.amazon.com//ec2/home") or the [AWS CLI](../../../cli/latest/reference/ec2/index.md "../../../cli/latest/reference/ec2/index.md").

After shutting down your Amazon Kinesis Data Streams application, you should delete the Amazon DynamoDB table that the
KCL used to track the application's state.

## Read throttling

The throughput of a stream is provisioned at the shard level. Each shard has a read
throughput of up to 5 transactions per second for reads, up to a maximum total data read rate of 2 MB per second. If an application (or a group of applications operating on
the same stream) attempts to get data from a shard at a faster rate, Kinesis Data Streams throttles the
corresponding Get operations.

In an Amazon Kinesis Data Streams application, if a record processor is processing data faster than the limit —
such as in the case of a failover — throttling occurs. Because KCL manages the
interactions between the application and Kinesis Data Streams, throttling exceptions occur in the
KCL code rather than in the application code. However, because the KCL
logs these exceptions, you see them in the logs.

If you find that your application is throttled consistently, you should consider
increasing the number of shards for the stream.
