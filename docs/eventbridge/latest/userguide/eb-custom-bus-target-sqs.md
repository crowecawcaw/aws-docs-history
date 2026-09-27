

# Amazon SQS queue target
<a name="eb-custom-bus-target-sqs"></a>

To deliver to an Amazon SQS queue, set `TargetArn` to the queue ARN, for example `arn:aws:sqs:us-east-1:111122223333:large-orders`, and add `SqsParameters`. For a FIFO queue, set `MessageGroupId`; the usual value is the event's group, `{% $events.SystemMetadata.EventGroupId %}`.

## Parameters
<a name="eb-custom-bus-target-sqs-parameters"></a>


| Parameter | What it sets | 
| --- | --- | 
| MessageGroupId | The queue message group. Required for a FIFO queue | 
| MessageDeduplicationId | The queue deduplication identifier for a FIFO queue without content-based deduplication. Derive it from the event; a constant makes the queue discard every message after the first | 
| DelaySeconds | Delivery delay for the message | 
| MessageAttributes | Message attributes to attach | 
| MessageSystemAttributes | System attributes, such as the AWS X-Ray trace header | 

## Delivery role
<a name="eb-custom-bus-target-sqs-role"></a>

The role needs `sqs:SendMessage` on the queue. If the queue is encrypted with a customer managed key, the role also needs `kms:GenerateDataKey` and `kms:Decrypt` on that key.

## Batching and payload
<a name="eb-custom-bus-target-sqs-batching"></a>

EventBridge calls `SendMessageBatch`, so one target call carries up to 10 events, and one queue message carries one event. `Transformer` decides the body of each message. See [Batching deliveries to a target](eb-custom-bus-batching.md).