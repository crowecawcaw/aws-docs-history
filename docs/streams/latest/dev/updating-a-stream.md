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
   **Configuration** tab. For more information, see [Choose the data stream capacity mode](how-do-i-size-a-stream.md "how-do-i-size-a-stream.md").

###### Important

For each data stream in your AWS account, you can switch between the
on-demand and provisioned modes twice within 24 hours. 5. For a data stream with the provisioned mode, to edit the number of shards,
choose **Edit provisioned shards** in the
**Configuration** tab, and then enter a new shard
count. 6. To enable server-side encryption of data records, choose
**Edit** in the **Server-side
encryption** section. Choose a KMS key to use as the master key
for encryption, or use the default master key,
**aws/kinesis**, managed by Kinesis. If you enable
encryption for a stream and use your own AWS KMS master key, ensure that your
producer and consumer applications have access to the AWS KMS master key that
you used. To assign permissions to an application to access a user-generated
AWS KMS key, see [Permissions to use user-generated
KMS keys](permissions-user-key-KMS.md "permissions-user-key-KMS.md"). 7. To edit the data retention period, choose **Edit** in the
**Data retention period** section, and then enter a new
data retention period. 8. If you have enabled custom metrics on your account, choose
**Edit** in the **Shard level
metrics** section, and then specify metrics for your stream.
For more information, see [Monitor the Amazon Kinesis Data Streams service with
Amazon CloudWatch](monitoring-with-cloudwatch.md "monitoring-with-cloudwatch.md").

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

## Use the AWS CLI

For information about updating a stream using the AWS CLI, see the [Kinesis CLI reference](../../../cli/latest/reference/kinesis/index.md "../../../cli/latest/reference/kinesis/index.md").
