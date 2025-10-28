# Write data to Amazon Kinesis Data Streams

A _producer_ is an application that writes data to
Amazon Kinesis Data Streams. You can build producers for Kinesis Data Streams using the AWS SDK for Java and the Kinesis Producer
Library (KPL).

If you are new to Kinesis Data Streams, start by becoming familiar with the concepts and terminology
presented in [What is Amazon Kinesis Data Streams?](introduction.md "introduction.md") and [Use the AWS CLI to perform Amazon Kinesis Data Streams operations](getting-started.md "getting-started.md").

###### Important

Kinesis Data Streams supports changes to the data record retention period of your data stream.
For more information, see [Change the data retention period](kinesis-extended-retention.md "kinesis-extended-retention.md").

To put data into the stream, you must specify the name of the stream, a partition key,
and the data blob to be added to the stream. The partition key is used to determine
which shard in the stream the data record is added to.

All the data in the shard is sent to the same worker that is processing the shard.
Which partition key you use depends on your application logic. The number of partition
keys should typically be much greater than the number of shards. This is because the
partition key is used to determine how to map a data record to a particular shard. If
you have enough partition keys, the data can be evenly distributed across the shards in
a stream.

###### Topics

- [Develop producers using the Amazon Kinesis Producer Library (KPL)](developing-producers-with-kpl.md "developing-producers-with-kpl.md")
- [Develop producers using the Amazon Kinesis Data Streams API
  with the AWS SDK for Java](developing-producers-with-sdk.md "developing-producers-with-sdk.md")
- [Write to Amazon Kinesis Data Streams using Kinesis Agent](writing-with-agents.md "writing-with-agents.md")
- [Write to Kinesis Data Streams using other AWS services](using-other-services.md "using-other-services.md")
- [Write to Kinesis Data Streams using third-party
  integrations](using-other-services-third-party.md "using-other-services-third-party.md")
- [Troubleshoot Amazon Kinesis Data Streams producers](troubleshooting-producers.md "troubleshooting-producers.md")
- [Optimize Kinesis Data Streams producers](advanced-producers.md "advanced-producers.md")
