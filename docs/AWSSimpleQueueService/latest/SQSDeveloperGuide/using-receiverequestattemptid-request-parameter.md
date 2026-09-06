

# Using the Amazon SQS receive request attempt ID
<a name="using-receiverequestattemptid-request-parameter"></a>

The receive request attempt ID is a unique token used to deduplicate [`ReceiveMessage`](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) calls in Amazon SQS. During a network outage or connectivity issue between your application and Amazon SQS, it is best practice to:
+ Provide a receive request attempt ID when making a `ReceiveMessage` call.
+ Retry using the same receive request attempt ID if the operation fails.