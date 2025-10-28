# Amazon SQS FIFO queue and Lambda concurrency

behavior

By using a FIFO (First-In-First-Out) queue with Lambda, you can ensure ordered processing
of messages within each message group. The Lambda function will not run multiple instances
for the same message group simultaneously, thereby maintaining the order. However, it can
scale up to handle multiple message groups in parallel, ensuring efficient processing of
your queue's workload. The following points describe the behavior of Lambda functions when
processing messages from an Amazon SQS FIFO queue with respect to message group IDs:

- **Single instance per message group:** At any point
  in time, only one Lambda instance will be processing messages from a specific message
  group ID. This ensures that messages within the same group are processed in order,
  maintaining the integrity of the FIFO sequence.
- **Concurrent processing of different groups:** Lambda
  can concurrently process messages from different message group IDs using multiple
  instances. This means that while one instance of the Lambda function is handling
  messages from one message group ID, other instances can simultaneously handle
  messages from other message group IDs, leveraging the concurrency capabilities of
  Lambda to process multiple groups in parallel.

## FIFO queue message grouping

FIFO queues ensure that messages are processed in the exact order they are sent. They
use a **message group ID** to group messages that should be
processed sequentially.

Messages within the same message group are processed in order, and only one message
from each group is processed at a time to maintain this order.

## Lambda concurrency with FIFO

queues

After you create your queue, you can send a message to it.

When you set up a Lambda function to process messages from an Amazon SQS FIFO queue, Lambda
respects the ordering guarantees provided by the FIFO queue. The following points
describe the behavior of Lambda functions in terms of concurrency and scaling when
processing messages from an Amazon SQS FIFO queue when using message group IDs.

- **Concurrency within message groups:** Only one
  Lambda instance processes messages for a particular message group ID at a time.
  This ensures that messages within a group are handled sequentially.
- **Scaling and multiple message groups:**While
  Lambda can scale up to process messages concurrently, this scaling occurs across
  different message groups. If you have multiple message groups, Lambda can process
  multiple groups in parallel, with each group being handled by a separate Lambda
  instance.

For more information, see [Scaling and concurrency
in Lambda](../../../lambda/latest/operatorguide/scaling-concurrency.md "../../../lambda/latest/operatorguide/scaling-concurrency.md") in the _AWS Lambda Operator Guide_.

## Use case example

Suppose your FIFO queue receives messages with the same message group ID, and your
Lambda function has a high concurrency limit (up to 1000).

If a message from group ID 'A' is being processed and another message from group ID
'A' arrives, the second message will not trigger a new Lambda instance until the first
message is fully processed.

However, if messages from group IDs 'A' and 'B' arrive, both messages can be processed
concurrently by separate Lambda instances.
