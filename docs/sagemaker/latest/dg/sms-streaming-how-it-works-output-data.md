# Receive output data from a streaming

labeling job

Your Amazon S3 output bucket is periodically updated with new output data
from your streaming labeling job. Optionally, you can specify an Amazon SNS output
topic. Each time a worker submits a labeled object, a notification with the
output data is sent to that topic. You can subscribe an endpoint to your SNS
output topic to receive notifications or trigger events when you receive output
data from a labeling task. Use an Amazon SNS output topic if you want to do real time
chaining to another streaming job and receive an Amazon SNS notifications each time a
data object is submitted by a worker.

To learn more, see [Subscribe an Endpoint to
Your Amazon SNS Output Topic](sms-create-sns-input-topic.md#sms-streaming-subscribe-output-topic "sms-create-sns-input-topic.md#sms-streaming-subscribe-output-topic").
