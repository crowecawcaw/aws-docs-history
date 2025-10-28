# Avoid large message

backlogs with the same message group ID in Amazon SQS

FIFO queues support a maximum of 120,000 in-flight messages (messages received by a consumer but not yet deleted). If this limit is reached, Amazon SQS does not return an error, but processing may be impacted. You can request an increase beyond this limit by contacting [AWS Support](../../../awssupport/latest/user/create-service-quota-increase.md "../../../awssupport/latest/user/create-service-quota-increase.md").

FIFO queues scan the first 120,000 messages to determine available message groups.
If a large backlog builds up in a single message group, messages from other groups
sent later will remain blocked until the backlog is processed.

###### Note

A message backlog can occur when a consumer repeatedly fails to process a
message. This could be due to message content issues or consumer-side failures.
To prevent message processing delays, configure a [dead-letter queue](sqs-dead-letter-queues.md "sqs-dead-letter-queues.md") to move
unprocessed messages after multiple failed attempts. This ensures that other
messages in the same message group can be processed, preventing system
bottlenecks.
