

# Handle dead-letter records in a queue

When a queue consumer receives a record `MaxReceiveCount` times without acknowledging it, the queue marks the record as a dead-letter record and stops delivering it on the normal receive path. A record that reaches `MaxReceiveCount` without an acknowledgment usually cannot be processed as it stands, and setting it aside stops the queue from redelivering it to your consumer instances.

Set `MaxReceiveCount` high enough that a record is unlikely to be processable by the time it reaches the limit, and low enough that a failing record is set aside before the queue redelivers it many times. A dead-letter record stays on the same queue, and you work with it through a separate set of operations: you receive dead-letter records, and then either acknowledge them or restore them to the normal receive path.

Set an alarm on `VisibleDeadLetterQueueRecords` so that you learn when dead-letter records begin to accumulate. Receive the records to inspect why they failed, and correct the cause in your queue consumer or in a downstream dependency. Then restore the records so that the queue delivers them again, up to `MaxReceiveCount` times. Acknowledge only the records that cannot be processed. For more information about monitoring dead-letter records, see [Monitor a queue](queues-monitoring.md).

## How dead-letter handling works
<a name="queues-dead-letter-config"></a>

Dead-letter handling is built into every queue. By default it is on, and a record becomes a dead-letter record after it is received 6 times without an acknowledgment.

`DeadLetterConfiguration` is a queue attribute. Set `TargetType` to `BUILT_IN` to keep it on, or to `NONE` to turn it off. When you set `TargetType` to `BUILT_IN`, you must also set `MaxReceiveCount`, from 1 to 1,000. A queue that you create without `DeadLetterConfiguration` gets `BUILT_IN` with a `MaxReceiveCount` of 6.

When dead-letter handling is off, an unacknowledged record keeps being redelivered until it is acknowledged or its retention period ends.

A queue has no retention period of its own. A dead-letter record expires when the stream's retention period ends for that record, the same as any other record in the stream. Correct the cause and restore or acknowledge dead-letter records before the stream's retention period ends. For more information about the retention period, see [Change the data retention period](kinesis-extended-retention.md).

## Work with dead-letter records
<a name="queues-dead-letter-operations"></a>

Dead-letter records remain on the same queue as its other records, and you work with them through a separate set of operations that use the same queue ARN. Use the following operations:

`ReceiveDeadLetterQueueRecords`  
Receives a batch of dead-letter records, up to 10 records per call. Each record carries the same fields and delivery metadata as a record on the normal receive path.

`AcknowledgeDeadLetterQueueRecords`  
Acknowledges dead-letter records, up to 10 records per call. The queue does not deliver an acknowledged record again.

`UpdateDeadLetterQueueRecordsVisibility`  
Changes the visibility timeout of dead-letter records that are in flight, up to 10 records per call. Set the timeout to 0 to make a record visible again immediately.

`RestoreDeadLetterQueueRecords`  
Returns dead-letter records to the normal receive path, up to 10 records per call. Restoring a record clears its dead-letter state and resets its receive count.

## Example: receive and handle a dead-letter record
<a name="queues-dead-letter-example"></a>

The following example receives a dead-letter record, and then acknowledges or restores it. Replace the queue ARN and the receipt handle with your own values.

Receive a dead-letter record:

```bash
aws kinesis receive-dead-letter-queue-records \
    --queue-arn arn:aws:kinesis:us-east-1:111122223333:queue/resource-id \
    --limit 10
```

The response includes a receipt handle, a record ID, and the receive count. The following is example output.

```json
{
    "QueueRecords": [
        {
            "ReceiptHandle": "AQID...example...",
            "RecordId": "2c455db5cc0161eb3dbac00da1ce9337",
            "PartitionKey": "user-1234",
            "Data": "eyJldmVudCI6ICJvcmRlciJ9",
            "ApproximateArrivalTimestamp": "2026-01-15T10:00:00.000000+00:00",
            "FirstReceiveTimestamp": "2026-01-15T10:05:00.000000+00:00",
            "ReceiveCount": 7
        }
    ]
}
```

After you inspect the record, acknowledge it if you have handled it, or restore it to deliver it again after you correct the cause.

Acknowledge the dead-letter record:

```bash
aws kinesis acknowledge-dead-letter-queue-records \
    --queue-arn arn:aws:kinesis:us-east-1:111122223333:queue/resource-id \
    --entries '[
        { "ReceiptHandle": "AQID...example..." }
    ]'
```

Or restore the dead-letter record:

```bash
aws kinesis restore-dead-letter-queue-records \
    --queue-arn arn:aws:kinesis:us-east-1:111122223333:queue/resource-id \
    --entries '[
        { "ReceiptHandle": "AQID...example..." }
    ]'
```

The acknowledge and restore operations return `Successful` and `Failed` lists, correlated by `ReceiptHandle`. Check the `Failed` list even when the response returns HTTP 200.