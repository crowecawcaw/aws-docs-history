

# Amazon SQS FIFO queues
<a name="sqs-fifo-queues"></a>

FIFO (First-In-First-Out) queues have all the capabilities of the [standard queues](standard-queues.md), but are designed to enhance messaging between applications when the order of operations and events is critical, or where duplicates can't be tolerated.

The most important features of FIFO queues are [*FIFO (First-In-First-Out) delivery*](FIFO-queues-understanding-logic.md) and *[exactly-once processing](FIFO-queues-exactly-once-processing.md)*:
+ The order in which messages are sent and received is strictly preserved and a message is delivered once and remains unavailable until a consumer processes and deletes it.
+ Duplicates aren't introduced into the queue.

Additionally, FIFO queues support *message groups* that allow multiple ordered message groups within a single queue. There is no quota to the number of message groups within a FIFO queue.

Examples of situations where you might use FIFO queues include the following:

1. E-commerce order management system where order is critical

1. Integrating with a third-party systems where events need to be processed in order

1. Processing user-entered inputs in the order entered

1. Communications and networking – Sending and receiving data and information in the same order

1. Computer systems – Making sure that user-entered commands are run in the right order

1. Educational institutes – Preventing a student from enrolling in a course before registering for an account

1. Online ticketing system – Where tickets are distributed on a first come first serve basis

**Note**  
FIFO queues also provide exactly-once processing, but have a limited number of transactions per second (TPS). You can use Amazon SQS **high throughput** mode with your FIFO queue to increase your transaction limit. For details on using high throughput mode, see [High throughput for FIFO queues in Amazon SQS](high-throughput-fifo.md). For information on throughput quotas, see [Amazon SQS message quotas](quotas-messages.md).

Amazon SQS FIFO queues are available in all Regions where Amazon SQS is available.

For more on using FIFO queues with complex ordering, see [Solving Complex Ordering Challenges with Amazon SQS FIFO Queues](https://aws.amazon.com/blogs/compute/solving-complex-ordering-challenges-with-amazon-sqs-fifo-queues/). 

For information about how to create and configure queues using the Amazon SQS console, see [Creating a standard queue using the Amazon SQS console](creating-sqs-standard-queues.md#step-create-standard-queue). For Java examples, see [Amazon SQS Java SDK examples](sqs-java-tutorials.md).

For best practices for working with FIFO queues, see [Amazon SQS best practices](sqs-best-practices.md).