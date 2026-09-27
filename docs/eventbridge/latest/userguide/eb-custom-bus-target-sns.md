

# Amazon SNS topic target
<a name="eb-custom-bus-target-sns"></a>

To deliver to an Amazon SNS topic, set `TargetArn` to the topic ARN and add `SnsParameters`. For a FIFO topic, set `MessageGroupId`, usually `{% $events.SystemMetadata.EventGroupId %}`.

## Parameters
<a name="eb-custom-bus-target-sns-parameters"></a>


| Parameter | What it sets | 
| --- | --- | 
| MessageGroupId | The topic message group. Required for a FIFO topic | 
| MessageDeduplicationId | The deduplication identifier for a FIFO topic without content-based deduplication. Derive it from the event | 
| Subject | The message subject, for email subscriptions | 
| MessageStructure | Set to json to send a different message per protocol | 
| MessageAttributes | Message attributes to attach | 

## Delivery role
<a name="eb-custom-bus-target-sns-role"></a>

The role needs `sns:Publish` on the topic. If the topic is encrypted with a customer managed key, the role also needs `kms:GenerateDataKey` and `kms:Decrypt` on that key.

## Batching and payload
<a name="eb-custom-bus-target-sns-batching"></a>

EventBridge calls `PublishBatch`, so one target call carries up to 10 events, and each topic message carries one event. See [Batching deliveries to a target](eb-custom-bus-batching.md).