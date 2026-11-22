

# Get started with queues using the AWS CLI

This walkthrough uses the AWS CLI to create a queue on an On-demand stream and work through the receive-and-acknowledge cycle. You create a stream and add a few records, create a queue, receive records, extend the visibility timeout of a record, acknowledge the records you finish, and then delete the queue and the stream.

Before you begin, install and configure the AWS CLI. For instructions, see [Tutorial: Install and configure the AWS CLI for Kinesis Data Streams](kinesis-tutorial-cli-installation.md). You also need permission for the queue actions, including `kinesis:AssociateStreamsWithQueue` on the stream. For more information, see [IAM permissions for queues](queues-iam.md). Queue operations use their own interface VPC endpoint service, separate from the stream endpoint. For more information, see [Use interface VPC endpoints for Kinesis Data Streams](vpc.md#using-interface-vpc-endpoints). The example resource names, Amazon Resource Names (ARNs), and receipt handles in this walkthrough are illustrative. Replace them with the values from your own output.

## Step 1: Create a stream and add records
<a name="queues-gs-create-stream"></a>

A queue works only on an On-demand stream. Create an On-demand stream and add a few records to it. For the full procedure, see [Tutorial: Perform basic Kinesis Data Streams operations using the AWS CLI](fundamental-stream.md).

Create the stream:

```bash
aws kinesis create-stream \
    --stream-name my-stream \
    --stream-mode-details StreamMode=ON_DEMAND
```

Add a few records. To pass the record data as plain text and have the AWS CLI return binary values as base64, use `--cli-binary-format raw-in-base64-out` (or set `cli_binary_format = raw-in-base64-out` in your AWS CLI configuration file):

```bash
aws kinesis put-record \
    --stream-name my-stream \
    --partition-key user-1 \
    --data "hello world" \
    --cli-binary-format raw-in-base64-out
```

## Step 2: Create a queue
<a name="queues-gs-create-queue"></a>

Create a queue with one `StreamConfigurationList` entry that associates the queue with your stream. The list must contain exactly one entry. Set the starting position in that entry, and set the queue default visibility timeout in `QueueAttributes`. The default starting position is `LATEST`.

```bash
aws kinesis create-queue \
    --queue-name my-queue \
    --stream-configuration-list '[
        {
            "StreamARN": "arn:aws:kinesis:us-west-2:111122223333:stream/my-stream",
            "StartingPosition": { "Type": "TRIM_HORIZON" }
        }
    ]' \
    --queue-attributes '{ "VisibilityTimeoutSeconds": 30 }'
```

The response contains the queue description, including the generated queue ARN and the queue status. The queue starts in the `CREATING` state:

```json
{
    "QueueDescription": {
        "QueueName": "my-queue",
        "QueueARN": "arn:aws:kinesis:us-west-2:111122223333:queue/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "QueueStatus": "CREATING",
        "QueueCreationTimestamp": "2026-01-15T10:30:00Z",
        "StreamConfigurationList": [
            {
                "StreamARN": "arn:aws:kinesis:us-west-2:111122223333:stream/my-stream",
                "StartingPosition": { "Type": "TRIM_HORIZON" }
            }
        ],
        "QueueAttributes": {
            "VisibilityTimeoutSeconds": 30,
            "DeadLetterConfiguration": {
                "TargetType": "BUILT_IN",
                "MaxReceiveCount": 6
            }
        }
    }
}
```

The queue ARN resource id is generated when you create the queue. It is not derived from the queue name. Use this queue ARN in the commands that follow.

**Note**  
If you omit `VisibilityTimeoutSeconds`, the queue uses the service default visibility timeout of 30 seconds. Dead-letter handling is enabled by default, so `DeadLetterConfiguration` appears in the queue description with a `MaxReceiveCount` of 6 even when you do not specify it.

## Step 3: Wait for the queue to become active
<a name="queues-gs-wait-active"></a>

Creating a queue is asynchronous. Call `describe-queue` with the queue ARN and wait until `QueueStatus` is `ACTIVE` before you receive records:

```bash
aws kinesis describe-queue \
    --queue-arn arn:aws:kinesis:us-west-2:111122223333:queue/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

```json
{
    "QueueDescription": {
        "QueueName": "my-queue",
        "QueueARN": "arn:aws:kinesis:us-west-2:111122223333:queue/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "QueueStatus": "ACTIVE",
        "QueueCreationTimestamp": "2026-01-15T10:30:00Z",
        "StreamConfigurationList": [
            {
                "StreamARN": "arn:aws:kinesis:us-west-2:111122223333:stream/my-stream",
                "StartingPosition": {
                    "Type": "TRIM_HORIZON",
                    "Timestamp": "2026-01-15T10:29:36Z"
                }
            }
        ],
        "QueueAttributes": {
            "VisibilityTimeoutSeconds": 30,
            "DeadLetterConfiguration": {
                "TargetType": "BUILT_IN",
                "MaxReceiveCount": 6
            }
        }
    }
}
```

## Step 4: List the queues on a stream
<a name="queues-gs-list-queues"></a>

To find the queues on a stream, call `list-queues` with a `StreamFilter` entry for that stream:

```bash
aws kinesis list-queues \
    --stream-filter '[
        { "StreamARN": "arn:aws:kinesis:us-west-2:111122223333:stream/my-stream" }
    ]'
```

```json
{
    "QueueSummaries": [
        {
            "QueueName": "my-queue",
            "QueueARN": "arn:aws:kinesis:us-west-2:111122223333:queue/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "QueueStatus": "ACTIVE",
            "QueueCreationTimestamp": "2026-01-15T10:30:00Z",
            "Streams": [
                {
                    "StreamARN": "arn:aws:kinesis:us-west-2:111122223333:stream/my-stream",
                    "StreamCreationTimestamp": "2026-01-15T10:29:36Z"
                }
            ]
        }
    ]
}
```

## Step 5: Receive records
<a name="queues-gs-receive"></a>

Receive records with `receive-queue-records`. Set `--limit` to the number of records to return (1 to 10). Set `--wait-time-seconds` to how long the call waits for records to arrive, from 1 to 20 seconds. If you omit it, the call waits 9 seconds:

```bash
aws kinesis receive-queue-records \
    --queue-arn arn:aws:kinesis:us-west-2:111122223333:queue/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --limit 10 \
    --wait-time-seconds 20
```

Each returned record carries a receipt handle and delivery metadata in addition to the data and partition key. The record data is base64 encoded:

```json
{
    "QueueRecords": [
        {
            "ReceiptHandle": "AQEBxyzReceiptHandleEXAMPLE1111==",
            "RecordId": "2c455db5cc0161eb3dbac00da1ce9337",
            "PartitionKey": "user-1",
            "Data": "aGVsbG8gd29ybGQ=",
            "ApproximateArrivalTimestamp": "2026-01-15T10:29:40.123456+00:00",
            "FirstReceiveTimestamp": "2026-01-15T10:31:05.654321+00:00",
            "ReceiveCount": 1
        }
    ]
}
```

Use the `ReceiptHandle` value to acknowledge a record, change its visibility timeout, or restore it. A new receipt handle is issued each time you receive a record. The `RecordId` value identifies the record and stays the same across its deliveries.

While a record is in flight, it is not visible to any queue consumer instance until the record is acknowledged or its visibility timeout expires. If the timeout expires without an acknowledgment, the record becomes visible again and the queue can deliver it to any consumer instance.

## Step 6: Extend the visibility timeout of a record
<a name="queues-gs-extend-visibility"></a>

If you need more time to process a record, extend its visibility timeout with `update-queue-records-visibility`. Each entry carries a `ReceiptHandle` and a `VisibilityTimeoutSeconds` value. There is no caller-supplied id:

```bash
aws kinesis update-queue-records-visibility \
    --queue-arn arn:aws:kinesis:us-west-2:111122223333:queue/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --entries '[
        {
            "ReceiptHandle": "AQEBxyzReceiptHandleEXAMPLE1111==",
            "VisibilityTimeoutSeconds": 60
        }
    ]'
```

Results are returned in the `Successful` and `Failed` lists, correlated by `ReceiptHandle`:

```json
{
    "Successful": [
        { "ReceiptHandle": "AQEBxyzReceiptHandleEXAMPLE1111==" }
    ],
    "Failed": []
}
```

To make a record visible immediately, set its `VisibilityTimeoutSeconds` to 0.

## Step 7: Change the queue default visibility timeout
<a name="queues-gs-update-queue"></a>

To change the default visibility timeout for every record the queue delivers, call `update-queue` with the new value in `QueueAttributes`:

```bash
aws kinesis update-queue \
    --queue-arn arn:aws:kinesis:us-west-2:111122223333:queue/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --queue-attributes '{ "VisibilityTimeoutSeconds": 60 }'
```

`UpdateQueue` changes the queue attributes: the default visibility timeout and the dead-letter configuration. The stream association, the queue name, and the starting position cannot be updated.

Updating a queue is asynchronous. The queue status moves to `UPDATING` and returns to `ACTIVE` when the change is applied.

## Step 8: Acknowledge records
<a name="queues-gs-acknowledge"></a>

A queue consumer acknowledges the records it successfully processes, up to 10 per call. Call `acknowledge-queue-records` with one entry per record. Each entry carries a `ReceiptHandle` and nothing else. There is no caller-supplied id:

```bash
aws kinesis acknowledge-queue-records \
    --queue-arn arn:aws:kinesis:us-west-2:111122223333:queue/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --entries '[
        { "ReceiptHandle": "AQEBxyzReceiptHandleEXAMPLE1111==" }
    ]'
```

Results are returned in the `Successful` and `Failed` lists, correlated by `ReceiptHandle`:

```json
{
    "Successful": [
        { "ReceiptHandle": "AQEBxyzReceiptHandleEXAMPLE1111==" }
    ],
    "Failed": []
}
```

Because an individual record can fail to be acknowledged even when the call returns HTTP 200, check the `Failed` list on every response and retry the entries it contains.

Acknowledging a record affects only the queue. The underlying stream record stays for its retention period and remains readable by stream consumers and by any other queue on the same stream.

## Step 9: Clean up
<a name="queues-gs-cleanup"></a>

To avoid ongoing charges, delete the resources you created when you no longer need them. For pricing details, see [Amazon Kinesis Data Streams pricing](https://aws.amazon.com/kinesis/data-streams/pricing/).

Delete the queue:

```bash
aws kinesis delete-queue \
    --queue-arn arn:aws:kinesis:us-west-2:111122223333:queue/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

Deleting a queue is asynchronous and does not delete the stream or its records. You must delete every queue on a stream before you can delete the stream or switch it from On-demand to provisioned capacity mode. `DeleteStream` fails with `ResourceInUseException` while a queue is attached, and `EnforceConsumerDeletion` has no effect on queues.

After the queue is deleted, delete the stream:

```bash
aws kinesis delete-stream \
    --stream-name my-stream
```