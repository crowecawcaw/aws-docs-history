# Amazon SQS batch actions

Amazon SQS provides batch actions to help you reduce costs and manipulate up to 10 messages
with a single action. These batch actions include:

- `SendMessageBatch`
- `DeleteMessageBatch`
- `ChangeMessageVisibilityBatch`
  Using batch actions, you can perform multiple operations in a single API call, which helps
  optimize performance and reduce costs. You can take advantage of batch functionality using
  the query API or any AWS SDK that supports Amazon SQS batch actions.

###### Important Details

- **Message Size Limit:** The total size of all
  messages sent in a single `SendMessageBatch` call cannot exceed 1,048,576 bytes
  (1 MiB)
- **Permissions:** You cannot set permissions
  explicitly for `SendMessageBatch`, `DeleteMessageBatch`, or
  `ChangeMessageVisibilityBatch`. Instead, setting permissions for
  `SendMessage`, `DeleteMessage`, or
  `ChangeMessageVisibility` sets permissions for the corresponding
  batch versions of the actions.
- **Console Support:** The Amazon SQS console does not
  support batch actions. You must use the query API or an AWS SDK to
  perform batch operations.

## Batching message actions

To further optimize costs and efficiency, consider the following best practices for
batching message actions:

- **Batch API Actions:** Use the [Amazon SQS batch API actions](sqs-batch-api-actions.md "sqs-batch-api-actions.md") actions to
  send, receive, and delete messages, and to change the message visibility timeout
  for multiple messages with a single action. This reduces the number of API calls
  and associated costs.
- **Client-Side Buffering and Long Polling:**
  Combine client-side buffering with request batching by using long polling
  together with the [buffered asynchronous client](sqs-client-side-buffering-request-batching.md "sqs-client-side-buffering-request-batching.md") included with the AWS SDK for Java. This
  approach helps to minimize the number of requests and optimizes the handling of
  large volumes of messages.

###### Note

The Amazon SQS Buffered Asynchronous Client doesn't currently support FIFO queues.
