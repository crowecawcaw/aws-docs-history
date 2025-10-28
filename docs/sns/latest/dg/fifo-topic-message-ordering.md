# Amazon SNS message ordering details for FIFO

topics

An Amazon SNS FIFO topic always delivers messages to subscribed Amazon SQS queues in the exact order
in which the messages are published to the topic, and only once. With an Amazon SQS FIFO queue
subscribed, the consumer of the queue receives the messages in the exact order in which the
messages are delivered to the queue, and no duplicates. With an Amazon SQS standard queue subscribed,
however, the consumer of the queue may receive messages out of order, and more than once. This
enables further decoupling of subscribers from publishers, giving subscribers more flexibility
in terms of message consumption and cost optimization, as shown in the following diagram, based
on the [Amazon SNS FIFO topic example use case](fifo-example-use-case.md "fifo-example-use-case.md").

![Example of the message delivery system in an Amazon SNS FIFO (First-In-First-Out) topic, highlighting how messages are consistently delivered in a strict order to Amazon SQS FIFO queues. It contrasts this with the behavior of an Amazon SQS standard queue, where messages may arrive out of order and more than once. The example showcases three different subscriber types—an analytics function, a wholesale application, and a retail application—demonstrating how each receives messages either in strict order or in a best-effort order depending on the type of queue they subscribe to.](images/sns-fifo-ordering-1.png)
Note that there is no implied ordering of the subscribers. The following example shows that
message **m1** is delivered first to the wholesale subscriber and
then to the retail subscriber and then to the analytics subscriber. Message **m2** is delivered first to the retail subscriber and then to the
wholesale subscriber and finally to the analytics subscriber. Though the two messages are
delivered to the subscribers in a different order, message ordering is preserved for each Amazon SQS
FIFO subscriber. Each subscriber is perceived in isolation from any other subscribers.

![Example of how Amazon SNS FIFO topics and various types of subscribers, including Amazon SQS FIFO and standard queues, handle message ordering and delivery. It shows that messages are published to a topic and delivered to different types of queues—ensuring ordered delivery for FIFO queues and best-effort ordering for standard queues. This setup supports scenarios in an e-commerce platform where different components need reliable message delivery in a specific order for accurate processing.](images/sns-fifo-ordering-2.png)
If an Amazon SQS queue subscriber becomes unreachable, it can get out of sync. For example, say
the wholesale application queue owner mistakenly changes the [Amazon SQS queue policy](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-using-identity-based-policies.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-using-identity-based-policies.md") in a way that prevents the Amazon SNS service principal from delivering
messages to the queue. In this case, price update deliveries to the wholesale queue fail, while
the ones to the retail and analytics queues succeed, causing the subscribers to be out of sync.
When the wholesale application queue owner corrects its queue policy, Amazon SNS resumes delivering
messages to the subscribed queue. Any messages published to the topic that target the
incorrectly configured queue are dropped, unless the corresponding subscription has a [dead-letter queue](sns-dead-letter-queues.md "sns-dead-letter-queues.md") configured.

![Example of the behavior of message delivery in an Amazon SNS FIFO setup where messages are published to different subscriber types (wholesale, retail, and analytics) through Amazon SQS queues. It highlights the impact of a queue policy misconfiguration on message delivery synchronization across different subscriber queues. The example shows how message delivery fails for the wholesale subscriber due to a policy error, but continues successfully for retail and analytics subscribers, emphasizing the importance of correct queue configuration to maintain synchronized data delivery. This scenario underlines the capability of FIFO topics to ensure ordered and exactly-once delivery under normal circumstances and the consequences of configuration errors.](images/sns-fifo-ordering-3.png)
You can have multiple applications (or multiple threads within the same application)
publishing messages to an SNS FIFO topic in parallel. When you do this, you effectively delegate
message sequencing to the Amazon SNS service. To determine the established sequence of messages, you
can check the sequence number.

The sequence number is a large, non-consecutive number that Amazon SNS assigns to each message.
The length of the sequence number is 128-bits, and continues to increase for each [Message Group](fifo-message-grouping.md "fifo-message-grouping.md"). The sequence number is passed to the
subscribed Amazon SQS queues as part of the message body. However, if you enable [raw message delivery](sns-large-payload-raw-message-delivery.md "sns-large-payload-raw-message-delivery.md"), the message
that's delivered to the Amazon SQS queue doesn't include the sequence number or any other Amazon SNS
message metadata.

![Example of multiple Lambda functions publish messages to an Amazon SNS FIFO (First In, First Out) topic, which then delivers these messages to an Amazon SQS FIFO queue, preserving the strict order of message processing. This setup is used to ensure that messages are processed in the exact order they are sent across different components of an application, with sequence numbers indicating the order for each message within a group. This type of configuration is crucial for applications where the order of operations and messages must be strictly maintained to ensure consistency.](images/sns-fifo-ordering-4.png)
Amazon SNS FIFO topics define ordering in the context of a message group. For more information,
see [Amazon SNS message grouping for FIFO topics](fifo-message-grouping.md "fifo-message-grouping.md").
