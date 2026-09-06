

# Update a stream
<a name="updating-a-stream"></a>

You can update the details of a stream using the Kinesis Data Streams console, the Kinesis Data Streams API, or the AWS CLI.

**Note**  
You can enable server-side encryption for existing streams, or for streams that you have recently created.

## Use the console
<a name="update-stream-console"></a>

**To update a data stream using the console**

1. Open the Amazon Kinesis console at [https://console.aws.amazon.com/kinesis/](https://console.aws.amazon.com/kinesis/).

1. In the navigation bar, expand the Region selector and choose a Region.

1. Choose the name of your stream in the list. The **Stream Details** page displays a summary of your stream configuration and monitoring information.

1. To switch between on-demand and provisioned capacity modes for a data stream, choose **Edit capacity mode** in the **Configuration** tab. For more information, see [Choose the right mode to stream in](how-do-i-size-a-stream.md).
**Important**  
For each data stream in your AWS account, you can switch between the on-demand and provisioned modes twice within 24 hours.

1. For a data stream in on-demand mode with [On-demand Advantage mode](how-do-i-size-a-stream.md#ondemand-advantage-mode) enabled, you can configure warm throughput to increase or decrease the stream's ingest capacity.

**To increase ingest capacity**  
In the **Configuration** tab, choose **Edit warm throughput** and enter a target throughput value (in MB/s) that is higher than the stream's current capacity. The stream immediately provisions capacity to at least the specified warm throughput, ensuring it can handle the expected traffic without throttling. For example, if you forecast an upcoming event to peak around 200 MB/s, set the warm throughput to 200 MB/s ahead of time at no additional cost.

**To decrease ingest capacity**  
If the stream has scaled significantly beyond its warm throughput value, reconfigure the warm throughput to that value or lower to trigger a scale-down. The stream scales to the requested number or the capacity needed to support peak data ingest usage observed within the last hour, whichever is higher. This ensures the stream always retains enough capacity to handle recent traffic patterns.

   Using warm throughput does not incur any additional cost. For more information, see [On-demand Advantage mode features and use cases](how-do-i-size-a-stream.md#ondemand-advantage-mode).

1. For a data stream with the provisioned mode, to edit the number of shards, choose **Edit provisioned shards** in the **Configuration** tab, and then enter a new shard count.

1. To enable server-side encryption of data records, choose **Edit** in the **Server-side encryption** section. Choose a KMS key to use as the master key for encryption, or use the default master key, **aws/kinesis**, managed by Kinesis. If you enable encryption for a stream and use your own AWS KMS master key, ensure that your producer and consumer applications have access to the AWS KMS master key that you used. To assign permissions to an application to access a user-generated AWS KMS key, see [Permissions to use user-generated KMS keys](permissions-user-key-KMS.md).

1. To edit the data retention period, choose **Edit** in the **Data retention period** section, and then enter a new data retention period.

1. If you have enabled custom metrics on your account, choose **Edit** in the **Shard level metrics** section, and then specify metrics for your stream. For more information, see [Monitor the Amazon Kinesis Data Streams service with Amazon CloudWatch](monitoring-with-cloudwatch.md).

## Use the API
<a name="update-stream-api"></a>

To update stream details using the API, see the following methods:
+ [AddTagsToStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_AddTagsToStream.html)
+ [DecreaseStreamRetentionPeriod](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DecreaseStreamRetentionPeriod.html)
+ [DisableEnhancedMonitoring](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DisableEnhancedMonitoring.html)
+ [EnableEnhancedMonitoring](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_EnableEnhancedMonitoring.html)
+ [IncreaseStreamRetentionPeriod](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_IncreaseStreamRetentionPeriod.html)
+ [RemoveTagsFromStream](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_RemoveTagsFromStream.html)
+ [StartStreamEncryption](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StartStreamEncryption.html)
+ [StopStreamEncryption](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_StopStreamEncryption.html)
+ [UpdateShardCount](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateShardCount.html)
+ [UpdateStreamMode](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateStreamMode.html)
+ [UpdateStreamWarmThroughput](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateStreamWarmThroughput.html) — When On-demand Advantage is enabled for an account, use this API to configure warm throughput for an on-demand stream. When you switch a stream from Provisioned to On-demand mode using the [UpdateStreamMode](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_UpdateStreamMode.html) API, you can also set warm throughput.

## Use the AWS CLI
<a name="update-stream-cli"></a>

For information about updating a stream using the AWS CLI, see the [Kinesis CLI reference](https://docs.aws.amazon.com/cli/latest/reference/kinesis/index.html). 

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