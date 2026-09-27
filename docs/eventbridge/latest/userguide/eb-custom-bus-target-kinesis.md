

# Kinesis stream target
<a name="eb-custom-bus-target-kinesis"></a>

To deliver to a Kinesis data stream, set `TargetArn` to the stream ARN and add `KinesisParameters` with a `PartitionKey`. To keep an event group on one shard, use `{% $events.SystemMetadata.EventGroupId %}`.

## Parameters
<a name="eb-custom-bus-target-kinesis-parameters"></a>


| Parameter | What it sets | 
| --- | --- | 
| PartitionKey | The partition key for each record. Required | 
| ExplicitHashKey | A hash key that overrides the shard chosen from the partition key | 

## Delivery role
<a name="eb-custom-bus-target-kinesis-role"></a>

The role needs `kinesis:PutRecords` on the stream.

## Batching and payload
<a name="eb-custom-bus-target-kinesis-batching"></a>

EventBridge calls `PutRecords`, so one target call carries up to 500 events, one record each. See [Batching deliveries to a target](eb-custom-bus-batching.md).