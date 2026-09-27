

# Batching deliveries to a target
<a name="eb-custom-bus-batching"></a>

EventBridge groups events into one target call when it can, so a queue receives up to 10 events per `SendMessageBatch` and a function receives an array per `Invoke`. To bound a batch, set `BatchConfiguration` on the subscriber: `MaxBatchSize` from 1 to 500, and `MaxBatchWindowInSeconds` from 0 to 300 to wait for more events before calling. For one event per call, set `MaxBatchSize` to 1.

## How a batch is closed
<a name="eb-custom-bus-batching-rules"></a>

A batch closes when the first of three limits is reached: the count in `MaxBatchSize`, the wait in `MaxBatchWindowInSeconds`, or the target's own payload size limit, for example 256 KB for an Amazon SQS request. Large events therefore arrive in smaller batches than `MaxBatchSize`. You can set the count and the window; the byte limit is the target's and cannot be changed.
+ For a bespoke target, `BatchConfiguration` is optional. Without it, EventBridge batches up to the largest size the target accepts, with a window of 0 seconds.
+ For a universal target, `BatchConfiguration` is required, with both fields set, because EventBridge cannot know how many events the action's request can carry.

## Batching and ordering
<a name="eb-custom-bus-batching-order"></a>

Within a batch, events keep their publish order. A batch from a FIFO subscriber can hold events from several event groups; each group's events are in order relative to one another. A target that processes a batch in parallel, such as a function iterating over the array with concurrency, loses that order.

## Seeing the batch size
<a name="eb-custom-bus-batching-metrics"></a>

The `TargetInvocations` metric counts target calls and `EventDeliveryAttempts` counts events, so their ratio is the average batch size. See [Observability for the Custom Event Bus: metrics, logs, and CloudTrail](eb-custom-bus-observability.md).