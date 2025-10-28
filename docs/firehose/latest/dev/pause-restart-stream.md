# Pause and resume data delivery

After you setup a Firehose stream, data available in the stream source is continuously
delivered to the destination. If you encounter situations where your stream destination
is temporarily unavailable (for example, during planned maintenance operations), you may
want to temporarily pause data delivery, and resume when the destination becomes
available again.

###### Important

When you use the approach described below to pause and resume a stream, after you resume the stream, you will see that few records get delivered to the error bucket in Amazon S3 while the rest of the stream continues to get delivered to the destination. This is a known limitation of the approach, and it occurs because a small number of records that could not be previously delivered to the destination after multiple retries are tracked as failed.

## Pause a Firehose stream

To pause stream delivery in Firehose, first remove permissions for Firehose to write to the S3 backup location
for failed deliveries. For example, if you want to pause the Firehose stream with an OpenSearch destination,
you can do this by updating permissions. For more information, see [Grant Firehose Access to a Public OpenSearch Service Destination](controlling-access.md#using-iam-es "controlling-access.md#using-iam-es").

Remove the `"Effect": "Allow"` permission for the action `s3:PutObject`, and explicitly add a statement that applies `Effect": "Deny"` permission on the action
`s3:PutObject` for the S3 bucket used for backing up failed deliveries. Next, turn off the stream destination
(for example, turning off the destination OpenSearch domain), or remove permissions for Firehose to write to the destination.
To update permissions for other destinations, check the section for your destination in
[Controlling Access with Amazon Data Firehose](controlling-access.md "controlling-access.md").
After you complete these two actions, Firehose will stop delivering streams, and you can monitor this using
[CloudWatch metrics for Firehose](cloudwatch-metrics.md "cloudwatch-metrics.md").

###### Important

When you pause stream delivery in Firehose, you need to ensure that the source of the stream
(for example, in Kinesis Data Streams or in Managed Service for Kafka) is configured to retain data until stream delivery
is resumed and the data gets delivered to the destination. If the source is DirectPUT, Firehose will

retain data for 24 hours. Data loss could happen if you do not resume the stream and deliver the data before the expiration of data retention period.

## Resume a Firehose stream

To resume delivery, first revert the change made earlier to the stream destination by turning on the destination and ensuring that
Firehose has permissions to deliver the stream to the destination. Next, revert the changes made earlier to permissions applied

to the S3 bucket for backing up failed deliveries. That is, apply `"Effect": "Allow"` permission for the action `s3:PutObject`,
and remove `"Effect": "Deny"` permission on the action `s3:PutObject` for the S3 bucket used for backing up failed deliveries.
Finally, monitor using [CloudWatch metrics for Firehose](cloudwatch-metrics.md "cloudwatch-metrics.md") to confirm that the stream is being delivered to the destination.
To view and troubleshoot errors, use [Amazon CloudWatch Logs monitoring for Firehose](monitoring-with-cloudwatch-logs.md "monitoring-with-cloudwatch-logs.md").
