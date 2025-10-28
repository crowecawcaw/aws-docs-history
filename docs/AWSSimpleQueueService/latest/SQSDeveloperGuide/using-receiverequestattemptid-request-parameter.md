# Using the Amazon SQS

receive request attempt ID

The receive request attempt ID is a unique token used to deduplicate [`ReceiveMessage`](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md") calls in Amazon SQS. During a network outage or
connectivity issue between your application and Amazon SQS, it is best practice to:

- Provide a receive request attempt ID when making a `ReceiveMessage`
  call.
- Retry using the same receive request attempt ID if the operation fails.
