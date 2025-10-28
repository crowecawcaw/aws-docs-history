# When to provide a message

deduplication ID in Amazon SQS

A producer should specify a message deduplication ID in the following
scenarios:

- When sending identical message bodies that must be treated as
  unique.
- When sending messages with the same content but different message
  attributes, ensuring each message is processed separately.
- When sending messages with different content (for example, a retry counter
  in the message body) but requiring Amazon SQS to recognize them as
  duplicates.
