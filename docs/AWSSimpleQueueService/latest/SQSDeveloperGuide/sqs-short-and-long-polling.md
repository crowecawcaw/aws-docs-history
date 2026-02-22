# Amazon SQS short and long polling

Amazon SQS offers short and long polling options for receiving messages from a queue. Consider
your application's requirements for responsiveness and cost efficiency when choosing between
these two polling options:

- **Short polling** (default) – The [`ReceiveMessage`](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md")
  request queries a subset of servers (based on a weighted random distribution) to
  find available messages and sends an immediate response, even if no messages are
  found.
- **Long polling** – [`ReceiveMessage`](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md")
  queries all servers for messages, sending a response once at least one message is
  available, up to the specified maximum. An empty response is sent only if the
  polling wait time expires. This option can reduce the number of empty responses and
  potentially lower costs.
  The following sections explain the details of short polling and long polling.

## Consuming messages using short polling

When you consume messages from a queue (FIFO or standard) using short polling, Amazon SQS
samples a subset of its servers (based on a weighted random distribution) and returns
messages from only those servers. Thus, a particular [`ReceiveMessage`](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md")
request might not return all of your messages. However, if you have fewer than 1,000
messages in your queue, a subsequent request will return your messages. If you keep
consuming from your queues, Amazon SQS samples all of its servers, and you receive all of
your messages.

The following diagram shows the short-polling behavior of messages returned from a
standard queue after one of your system components makes a receive request. Amazon SQS
samples several of its servers (in gray) and returns messages A, C, D, and B from these
servers. Message E isn't returned for this request, but is returned for a subsequent
request.

![Message sampling using short (standard) polling](images/ArchOverview_Receive.png)

## Consuming messages using long polling

When the wait time for the `ReceiveMessage` API action is greater than 0, _long polling_
is in effect. The maximum long polling wait time is 20 seconds. Long polling helps reduce the cost of using Amazon SQS by reducing the number of empty responses
(when there are no messages available for a `ReceiveMessage` request) and false
empty responses (when messages are available but aren't included in a response). For information about enabling long polling for a new or
existing queue using the Amazon SQS console, see the [Configuring queue parameters using the Amazon SQS
console](sqs-configure-queue-parameters.md "sqs-configure-queue-parameters.md"). For best practices, see [Setting-up long polling in
Amazon SQS](best-practices-setting-up-long-polling.md "best-practices-setting-up-long-polling.md").

Long polling offers the following benefits:

- Reduce empty responses by allowing Amazon SQS to wait until a message is available
  in a queue before sending a response. Unless the connection times out, the
  response to the `ReceiveMessage` request contains at least one of the
  available messages, up to the maximum number of messages specified in the
  `ReceiveMessage` action. In rare cases, you might receive empty
  responses even when a queue still contains messages, especially if you specify a
  low value for the [`ReceiveMessageWaitTimeSeconds`](../APIReference/API_ReceiveMessage.md#SQS-ReceiveMessage-request-WaitTimeSeconds "../APIReference/API_ReceiveMessage.md#SQS-ReceiveMessage-request-WaitTimeSeconds") parameter.
- Reduce false empty responses by querying all—rather than a subset
  of—Amazon SQS servers.
- Return messages as soon as they become available.

For information about how to confirm that a queue is empty, see [Confirming that an Amazon SQS queue is empty](confirm-queue-is-empty.md "confirm-queue-is-empty.md").

## Differences between long and short

polling

Short polling occurs when the [`WaitTimeSeconds`](../APIReference/API_ReceiveMessage.md#SQS-ReceiveMessage-request-WaitTimeSeconds "../APIReference/API_ReceiveMessage.md#SQS-ReceiveMessage-request-WaitTimeSeconds") parameter of a `ReceiveMessage` request
is set to `0` in one of two ways:

- The `ReceiveMessage` call sets `WaitTimeSeconds` to
  `0`.
- The `ReceiveMessage` call doesn’t set `WaitTimeSeconds`,
  but the queue attribute [`ReceiveMessageWaitTimeSeconds`](../APIReference/API_SetQueueAttributes.md "../APIReference/API_SetQueueAttributes.md") is set to
  `0`.
