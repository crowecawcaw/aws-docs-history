# Processing messages

in a timely manner in Amazon SQS

Setting the visibility timeout depends on how long it takes your application to
process and delete a message. For example, if your application requires 10 seconds to
process a message and you set the visibility timeout to 15 minutes, you must wait for a
relatively long time to attempt to process the message again if the previous processing
attempt fails. Alternatively, if your application requires 10 seconds to process a
message but you set the visibility timeout to only 2 seconds, a duplicate message is
received by another consumer while the original consumer is still working on the
message.

To make sure that there is sufficient time to process messages, use one of the
following strategies:

- If you know (or can reasonably estimate) how long it takes to process a
  message, extend the message's _visibility timeout_ to the
  maximum time it takes to process and delete the message. For more information,
  see [Configuring the Visibility
  Timeout](sqs-visibility-timeout.md#configuring-visibility-timeout "sqs-visibility-timeout.md#configuring-visibility-timeout").
- If you don't know how long it takes to process a message, create a _heartbeat_ for your consumer
  process: Specify the initial visibility timeout (for example, 2 minutes) and then—as long as your consumer still works on the message—keep
  extending the visibility timeout by 2 minutes every minute.

###### Important

The maximum visibility timeout is 12 hours from the time that Amazon SQS receives the `ReceiveMessage` request.
Extending the visibility timeout does not reset the 12 hour maximum.

Additionally, you may be unable to set the timeout on an individual message to the full 12 hours (e.g. 43,200 seconds) since the `ReceiveMessage`
request initiates the timer. For example, if you receive a message and immediately set the 12 hour maximum by sending a `ChangeMessageVisibility` call with `VisibilityTimeout` equal to 43,200 seconds, it will likely fail.
However, using a value of 43,195 seconds will work unless there is a significant delay between requesting the message via `ReceiveMessage` and updating the visibility timeout. If your consumer needs longer than 12 hours, consider using Step Functions.
