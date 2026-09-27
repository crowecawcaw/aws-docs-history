

# Amazon Data Firehose stream target
<a name="eb-custom-bus-target-firehose"></a>

To deliver to an Amazon Data Firehose stream, set `TargetArn` to the stream ARN and add an empty `FirehoseParameters` block, `"FirehoseParameters": {}`, so that EventBridge knows the target type you intend.

## Parameters
<a name="eb-custom-bus-target-firehose-parameters"></a>

This target has no parameters; the payload is the whole request.

## Delivery role
<a name="eb-custom-bus-target-firehose-role"></a>

The role needs `firehose:PutRecordBatch` on the stream.

## Batching and payload
<a name="eb-custom-bus-target-firehose-batching"></a>

EventBridge calls `PutRecordBatch`, so one target call carries up to 500 events, one record each. Firehose does not add a delimiter between records; if your destination expects one record per line, end each event with a newline in the `Transformer`. See [Batching deliveries to a target](eb-custom-bus-batching.md).