# Setting-up long polling in

Amazon SQS

When the wait time for the `ReceiveMessage` API action is greater than 0, _long polling_
is in effect. The maximum long polling wait time is 20 seconds. Long polling helps reduce the cost of using Amazon SQS by eliminating the number of empty responses
(when there are no messages available for a `ReceiveMessage` request) and false
empty responses (when messages are available but aren't included in a response). For more information, see [Amazon SQS short and long polling](sqs-short-and-long-polling.md "sqs-short-and-long-polling.md").

For optimal message processing, use the following strategies:

- In most cases, you can set the `ReceiveMessage` wait time to 20
  seconds. If 20 seconds is too long for your application, set a shorter
  `ReceiveMessage` wait time (1 second minimum). If you don't use
  an AWS SDK to access Amazon SQS, or if you configure an AWS SDK to have a shorter
  wait time, you might have to modify your Amazon SQS client to either allow longer
  requests or use a shorter wait time for long polling.
- If you implement long polling for multiple queues, use one thread for each
  queue instead of a single thread for all queues. Using a single thread for each
  queue allows your application to process the messages in each of the queues as
  they become available, while using a single thread for polling multiple queues
  might cause your application to become unable to process messages available in
  other queues while the application waits (up to 20 seconds) for the queue which
  doesn't have any available messages.

###### Important

To avoid HTTP errors, make sure that the HTTP response timeout for
`ReceiveMessage` requests is longer than the
`WaitTimeSeconds` parameter. For more information, see [ReceiveMessage](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md").
