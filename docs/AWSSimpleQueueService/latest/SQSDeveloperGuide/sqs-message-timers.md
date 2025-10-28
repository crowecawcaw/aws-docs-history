# Amazon SQS message timers

Message timers allow you to set an initial invisibility period for a message when it's
added to a queue. For example, if you send a message with a 45-second timer, it remains
hidden from consumers for the first 45 seconds. The default (minimum) delay for a message is 0 seconds. The maximum is 15 minutes. For
information about sending messages with timers using the console, see [Sending a message using a standard queue](creating-sqs-standard-queues.md#sqs-send-messages "creating-sqs-standard-queues.md#sqs-send-messages").

###### Note

FIFO queues don't support timers on individual messages.

To set a delay period on an entire queue, rather than on individual messages, use [delay queues](sqs-delay-queues.md "sqs-delay-queues.md"). A message timer setting for an
individual message overrides any `DelaySeconds` value on an Amazon SQS delay queue.

**Extended scheduling options**

While Amazon SQS delay queues and message timers allow scheduling of message delivery up to 15
minutes in the future, you may require more flexible scheduling capabilities. In such cases,
consider using [EventBridge Scheduler](../../../scheduler/latest/UserGuide/what-is-scheduler.md "../../../scheduler/latest/UserGuide/what-is-scheduler.md"), which enables you
to schedule billions of one-time or recurring API actions without time limitations. EventBridge Scheduler is the recommended solution for advanced message scheduling use cases.
