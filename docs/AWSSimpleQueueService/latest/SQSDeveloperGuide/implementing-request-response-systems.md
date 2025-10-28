# Implementing request-response

systems in Amazon SQS

When implementing a request-response or remote procedure call (RPC) system, keep the
following best practices in mind:

- **Create reply queues on start-up** –
  Instead of creating reply queues per message, create them on start-up, per
  producer. Use a correlation ID message attribute to map replies to requests
  efficiently.
- **Avoid sharing reply queues among producers**
  – Ensure that each producer has its own reply queue. Sharing reply queues
  can result in a producer receiving response messages intended for another
  producer.
  For more information about implementing the request-response pattern using the
  Temporary Queue Client, see [Request-response messaging pattern
  (virtual queues)](sqs-temporary-queues.md#request-reply-messaging-pattern "sqs-temporary-queues.md#request-reply-messaging-pattern").
