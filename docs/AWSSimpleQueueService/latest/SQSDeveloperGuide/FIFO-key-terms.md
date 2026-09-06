

# Amazon SQS FIFO queue key terms
<a name="FIFO-key-terms"></a>

The following key terms can help you better understand the functionality of FIFO queues. For more information, see the *[Amazon Simple Queue Service API Reference](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/)*.

**Clients**  
The Amazon SQS Buffered Asynchronous Client doesn't currently support FIFO queues.

**Message deduplication ID**  
A token used in Amazon SQS FIFO queues to uniquely identify messages and prevent duplication. If multiple messages with the same deduplication ID are sent within a 5 minute deduplication interval, they are treated as duplicates, and only one copy is delivered. If you don't specify a deduplication ID and content-based deduplication is enabled, Amazon SQS generates a deduplication ID by hashing the message body. This mechanism ensures exactly-once delivery by eliminating duplicate messages within the specified time frame.  
Amazon SQS continues tracking the deduplication ID even after the message has been received and deleted.

**Message group ID**  
In FIFO (First-In-First-Out) queues, `MessageGroupId` is an attribute that organizes messages into distinct groups. Messages within the same message group are always processed one at a time, in strict order, ensuring that no two messages from the same group are processed simultaneously. In standard queues, using `MessageGroupId` enables [fair queues](sqs-fair-queues.md). If strict ordering is required, use a FIFO queue.

**Receive request attempt ID**  
The receive request attempt ID is a unique token used to deduplicate [`ReceiveMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) calls in Amazon SQS.

**Sequence number**  
The large, non-consecutive number that Amazon SQS assigns to each message.

**Services**  
If your application uses multiple AWS services, or a mix of AWS and external services, it is important to understand which service functionality doesn't support FIFO queues.  
Some AWS or external services that send notifications to Amazon SQS might not be compatible with FIFO queues, despite allowing you to set a FIFO queue as a target.  
The following features of AWS services aren't currently compatible with FIFO queues:  
+ [Amazon S3 Event Notifications](https://docs.aws.amazon.com/AmazonS3/latest/userguide/NotificationHowTo.html)
+ [Auto Scaling Lifecycle Hooks](https://docs.aws.amazon.com/autoscaling/ec2/userguide/lifecycle-hooks.html)
+ [AWS IoT Rule Actions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html)
+ [AWS Lambda Dead-Letter Queues](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-dlq)
For information about compatibility of other services with FIFO queues, see your service documentation.