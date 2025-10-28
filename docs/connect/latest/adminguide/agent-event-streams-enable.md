# Enable agent event streams to report agent

activity in Amazon Connect

Agent event streams are not enabled by default. Before you can enable agent event
streams in Amazon Connect, create a data stream in Amazon Kinesis Data Streams. Then, choose the Kinesis stream as the
stream to use for agent event streams. Though you can use the same stream for both agent
event streams and contact records, managing and getting data from the stream is much
easier when you use a separate stream for each. For more information, see the
[Amazon Kinesis Data Streams Developer Guide](../../../streams/latest/dev.md "../../../streams/latest/dev.md").

When data is sent to Kinesis, the partition key used is the agent ARN. All events for a
single agent are sent to the same shard, and any resharding events in the stream are
ignored.

###### Note

If you enable server-side encryption for the Kinesis stream you select for agent
event streams, Amazon Connect cannot publish to the stream. This is because it does not have
permission to Kinesis `kms:GenerateDataKey`. To work around this, first
enable encryption for scheduled reports or recordings of conversations. Next, create
a AWS KMS key using KMS for encryption. Finally, choose the same KMS key for
your Kinesis data stream that you use for encryption of scheduled reports or recordings
of conversations so that Amazon Connect has appropriate permissions to encrypt data sent to
Kinesis. For more information about creating a KMS key, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md "../../../kms/latest/developerguide/create-keys.md").

###### To enable agent event streams

1. Open the Amazon Connect console at
   [https://console.aws.amazon.com/connect/](https://console.aws.amazon.com/connect/ "https://console.aws.amazon.com/connect/").
2. On the console, choose the name in the **Instance Alias**
   column of the instance for which to enable agent event streams.
3. Choose **Data streaming**, then select **Enable data
   streaming**.
4. Under **Agent Events**, select the Kinesis stream to use, and
   then choose **Save**.
