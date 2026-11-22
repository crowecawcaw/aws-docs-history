

# How queues work

A queue delivers records from a stream to a queue consumer, tracks the delivery state of each record, and redelivers any record that is not acknowledged in time. A queue consumer works in a repeating cycle: it receives a batch of visible records, processes them, and acknowledges the ones it successfully processes. A receive call waits up to `WaitTimeSeconds` for records to arrive before it returns, 9 seconds by default and up to 20, so a consumer instance that finds the queue empty does not need to back off and retry on its own. Acknowledging a record tells the queue that the record is processed, so the queue does not deliver it again. A queue can deliver a record only while the stream still retains it, so a record that is never acknowledged expires when the stream's retention period ends for that record.

## Delivery and ordering
<a name="queues-delivery-and-ordering"></a>

Queues deliver records at least once. In rare cases the queue can deliver a record again even after you acknowledge it. Design your queue consumer to be idempotent, so that processing the same record more than once is safe.

A queue consumer does not necessarily receive records in the order that producers wrote them to the stream.

## Visibility timeout
<a name="queues-visibility-timeout"></a>

When a queue consumer instance receives a record, the record becomes in flight: it is not visible to any consumer instance until the instance acknowledges the record or the record's visibility timeout expires. If the timeout expires without an acknowledgment, the record becomes visible again, and the queue can redeliver it to any consumer instance.

A queue has a default visibility timeout, set by the `VisibilityTimeoutSeconds` queue attribute. To override the default for a single receive, set `VisibilityTimeoutSeconds` on the receive call. To change the timeout of records that are already in flight, call `UpdateQueueRecordsVisibility`. Set the timeout to 0 to make a record visible immediately. The visibility timeout can range from 0 to 43,200 seconds (12 hours).

If you omit `VisibilityTimeoutSeconds` when you create a queue, the queue uses a default visibility timeout of 30 seconds.

Set the visibility timeout longer than the time your queue consumer needs to process a record. If the timeout is shorter, the queue redelivers records that are still being processed, which duplicates work and increases `ReceiveCount` on records that have not failed. If the timeout is much longer, records held by a consumer instance that stops without acknowledging them stay in flight until the timeout expires. If processing time varies, set a timeout that covers the common case and call `UpdateQueueRecordsVisibility` to extend individual records that need longer.

## Starting position
<a name="queues-starting-position"></a>

When you create a queue, you choose a starting position, which sets the approximate position in the stream where delivery begins. A queue supports the following starting positions:

`LATEST`  
Delivers records that arrive after you create the queue. This is the default.

`TRIM_HORIZON`  
Delivers records starting with the oldest record the stream still retains.

`AT_TIMESTAMP`  
Delivers records that arrive at or after a time stamp that you provide. If the time stamp is earlier than the oldest record the stream still retains, delivery begins with that oldest record, the same as `TRIM_HORIZON`.

You choose the starting position when you create the queue, and you cannot change it afterward. To deliver from a different position, create a new queue.

**Note**  
Set `Timestamp` only with `AT_TIMESTAMP`. `CreateQueue` rejects a `Timestamp` with `TRIM_HORIZON` or `LATEST`. `DescribeQueue` returns a resolved `Timestamp` inside `StartingPosition` for every starting position type, including `TRIM_HORIZON` and `LATEST`.

## Record lifecycle
<a name="queues-record-lifecycle"></a>

A record moves through four states in a queue:
+ **Visible**: The record is ready to be received. A record is visible before its first receive, and again whenever its visibility timeout expires without an acknowledgment.
+ **In flight**: A consumer instance has received the record. The record is not visible to any consumer instance until the instance acknowledges the record or its visibility timeout expires.
+ **Acknowledged**: A consumer instance has acknowledged the record. The queue does not deliver it again.
+ **Dead-letter**: The queue has stopped delivering the record on the normal receive path, because the queue consumer received it `MaxReceiveCount` times without acknowledging it. You work with the record through a separate set of operations, and restoring the record puts it back to the normal receive path.

If you turn off dead-letter handling by setting `TargetType` to `NONE`, an unacknowledged record keeps being redelivered until it is acknowledged or its retention period ends. For more information about the retention period, see [Change the data retention period](kinesis-extended-retention.md). For more information about dead-letter records, see [Handle dead-letter records in a queue](queues-dead-letter-records.md).

## What a record contains
<a name="queues-record-metadata"></a>

A record that a queue delivers is the same record a stream consumer reads. The queue delivers the record's own fields unchanged, and adds the record identifier and the delivery metadata that the queue tracks.

The following fields come from the record as it is stored in the stream, and carry the same values that a stream consumer sees:

`Data`  
The data blob that the producer wrote. Kinesis Data Streams does not inspect, interpret, or change the data in the blob in any way.

`PartitionKey`  
The partition key that the producer supplied.

`ApproximateArrivalTimestamp`  
The approximate time at which the record was written to the stream.

`RecordId` identifies the record itself. It stays the same across every delivery of that record, and it is the same in every queue on the stream that delivers the record.

The remaining fields are delivery metadata that a queue tracks for each record it delivers:

`ReceiptHandle`  
Identifies a single delivery of the record, and is the value you pass to acknowledge the record, change its visibility timeout, or restore it. It is valid only while the record is in flight, and the queue issues a new `ReceiptHandle` each time it delivers the record.

`FirstReceiveTimestamp`  
The time at which the queue first delivered the record.

`ReceiveCount`  
The number of times the queue has delivered the record. When this count reaches `MaxReceiveCount` without an acknowledgment, the queue moves the record to the dead-letter state.

Acknowledging a record affects only its delivery state in the queue, not the record itself. The record remains in the stream for its retention period, where stream consumers can still read it and other queues can still deliver it.