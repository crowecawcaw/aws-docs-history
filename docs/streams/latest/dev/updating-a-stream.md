# Update a stream

You can update the details of a stream using the Kinesis Data Streams console, the Kinesis Data Streams API, or the
AWS CLI.

###### Note

You can enable server-side encryption for existing streams, or for streams that
you have recently created.

## Use the console

###### To update a data stream using the console

1. Open the Amazon Kinesis console at [https://console.aws.amazon.com/kinesis/](https://console.aws.amazon.com/kinesis/ "https://console.aws.amazon.com/kinesis/").
2. In the navigation bar, expand the Region selector and choose a
   Region.
3. Choose the name of your stream in the list. The **Stream
   Details** page displays a summary of your stream configuration
   and monitoring information.
4. To switch between on-demand and provisioned capacity modes for a data
   stream, choose **Edit capacity mode** in the
   **Configuration** tab. For more information, see [Choose the right mode to stream in](how-do-i-size-a-stream.md "how-do-i-size-a-stream.md").

###### Important

For each data stream in your AWS account, you can switch between the
on-demand and provisioned modes twice within 24 hours. 5. For a data stream in on-demand mode with [On-demand Advantage mode](how-do-i-size-a-stream.md#ondemand-advantage-mode "how-do-i-size-a-stream.md#ondemand-advantage-mode") enabled, you can configure warm throughput to increase or decrease the stream's ingest capacity.

###### To increase ingest capacity

In the **Configuration** tab, choose **Edit warm throughput** and enter a target throughput value (in MB/s) that is higher than the stream's current capacity. The stream immediately provisions capacity to at least the specified warm throughput, ensuring it can handle the expected traffic without throttling. For example, if you forecast an upcoming event to peak around 200 MB/s, set the warm throughput to 200 MB/s ahead of time at no additional cost.

###### To decrease ingest capacity

If the stream has scaled significantly beyond its warm throughput value, reconfigure the warm throughput to that value or lower to trigger a scale-down. The stream scales to the requested number or the capacity needed to support peak data ingest usage observed within the last hour, whichever is higher. This ensures the stream always retains enough capacity to handle recent traffic patterns.

Using warm throughput does not incur any additional cost. For more information, see [On-demand Advantage mode features and use cases](how-do-i-size-a-stream.md#ondemand-advantage-mode "how-do-i-size-a-stream.md#ondemand-advantage-mode"). 6. For a data stream with the provisioned mode, to edit the number of shards,
choose **Edit provisioned shards** in the
**Configuration** tab, and then enter a new shard
count. 7. To enable server-side encryption of data records, choose
**Edit** in the **Server-side
encryption** section. Choose a KMS key to use as the master key
for encryption, or use the default master key,
**aws/kinesis**, managed by Kinesis. If you enable
encryption for a stream and use your own AWS KMS master key, ensure that your
producer and consumer applications have access to the AWS KMS master key that
you used. To assign permissions to an application to access a user-generated
AWS KMS key, see [Permissions to use user-generated KMS keys](permissions-user-key-KMS.md "permissions-user-key-KMS.md"). 8. To edit the data retention period, choose **Edit** in the
**Data retention period** section, and then enter a new
data retention period. 9. If you have enabled custom metrics on your account, choose
**Edit** in the **Shard level
metrics** section, and then specify metrics for your stream.
For more information, see [Monitor the Amazon Kinesis Data Streams service with Amazon CloudWatch](monitoring-with-cloudwatch.md "monitoring-with-cloudwatch.md").

## Use the API

To update stream details using the API, see the following methods:

- [AddTagsToStream](../../../kinesis/latest/APIReference/API_AddTagsToStream.md "../../../kinesis/latest/APIReference/API_AddTagsToStream.md")
- [DecreaseStreamRetentionPeriod](../../../kinesis/latest/APIReference/API_DecreaseStreamRetentionPeriod.md "../../../kinesis/latest/APIReference/API_DecreaseStreamRetentionPeriod.md")
- [DisableEnhancedMonitoring](../../../kinesis/latest/APIReference/API_DisableEnhancedMonitoring.md "../../../kinesis/latest/APIReference/API_DisableEnhancedMonitoring.md")
- [EnableEnhancedMonitoring](../../../kinesis/latest/APIReference/API_EnableEnhancedMonitoring.md "../../../kinesis/latest/APIReference/API_EnableEnhancedMonitoring.md")
- [IncreaseStreamRetentionPeriod](../../../kinesis/latest/APIReference/API_IncreaseStreamRetentionPeriod.md "../../../kinesis/latest/APIReference/API_IncreaseStreamRetentionPeriod.md")
- [RemoveTagsFromStream](../../../kinesis/latest/APIReference/API_RemoveTagsFromStream.md "../../../kinesis/latest/APIReference/API_RemoveTagsFromStream.md")
- [StartStreamEncryption](../../../kinesis/latest/APIReference/API_StartStreamEncryption.md "../../../kinesis/latest/APIReference/API_StartStreamEncryption.md")
- [StopStreamEncryption](../../../kinesis/latest/APIReference/API_StopStreamEncryption.md "../../../kinesis/latest/APIReference/API_StopStreamEncryption.md")
- [UpdateShardCount](../../../kinesis/latest/APIReference/API_UpdateShardCount.md "../../../kinesis/latest/APIReference/API_UpdateShardCount.md")
- [UpdateStreamMode](../../../kinesis/latest/APIReference/API_UpdateStreamMode.md "../../../kinesis/latest/APIReference/API_UpdateStreamMode.md")
- [UpdateStreamWarmThroughput](../../../kinesis/latest/APIReference/API_UpdateStreamWarmThroughput.md "../../../kinesis/latest/APIReference/API_UpdateStreamWarmThroughput.md") — When On-demand Advantage is enabled for an account, use this API to configure warm throughput for an on-demand stream. When you switch a stream from Provisioned to On-demand mode using the [UpdateStreamMode](../../../kinesis/latest/APIReference/API_UpdateStreamMode.md "../../../kinesis/latest/APIReference/API_UpdateStreamMode.md") API, you can also set warm throughput.

## Use the AWS CLI

For information about updating a stream using the AWS CLI, see the [Kinesis CLI reference](../../../cli/latest/reference/kinesis/index.md "../../../cli/latest/reference/kinesis/index.md").

To configure warm throughput using the AWS CLI, use the `update-stream-warm-throughput` command. For example:

```
aws kinesis update-stream-warm-throughput \
    --stream-arn arn:aws:kinesis:us-east-1:123456789012:stream/my-stream \
    --warm-throughput-mi-bps=200
```

To lower capacity, reconfigure `warm-throughput-mi-bps` to the same or a lower value:

```
aws kinesis update-stream-warm-throughput \
    --stream-arn arn:aws:kinesis:us-east-1:123456789012:stream/my-stream \
    --warm-throughput-mi-bps=50
```

The stream scales to the requested warm throughput or the capacity needed to support recent peak data ingest usage, whichever is higher.
