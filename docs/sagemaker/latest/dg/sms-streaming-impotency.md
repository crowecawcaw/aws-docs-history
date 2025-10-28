# Duplicate message handling

For data objects sent in real time, Ground Truth guarantees idempotency by
ensuring each unique object is only sent for labeling once, even if the input
message referring to that object is received multiple times (duplicate
messages). To do this, each data object sent to a streaming labeling job is
assigned a _deduplication ID_, which is
identified with a _deduplication key_. If you
send your requests to label data objects directly through your Amazon SNS input topic
using Amazon SNS messages, you can optionally choose a custom deduplication key and
deduplication IDs for your objects. For more information, see [Specify a deduplication key and ID in an Amazon SNS
message](sms-streaming-impotency-create.md "sms-streaming-impotency-create.md").

If you do not provide your own deduplication key, or if you use the Amazon S3
configuration to send data objects to your labeling job, Ground Truth uses one of the
following for the deduplication ID:

- For messages sent directly to your Amazon SNS input topic, Ground Truth uses the SNS
  message ID.
- For messages that come from an Amazon S3 configuration, Ground Truth creates a
  deduplication ID by combining the Amazon S3 URI of the object with the [sequencer token](../../../AmazonS3/latest/dev/notification-content-structure.md "../../../AmazonS3/latest/dev/notification-content-structure.md") in the message.

###### Note

Do not use the `$` character in your label attribute name.
