

# Handling request errors in Amazon SQS
<a name="handling-request-errors"></a>

To handle request errors, use one of the following strategies:
+ If you use an AWS SDK, you already have automatic *retry and backoff* logic at your disposal. For more information, see [Error Retries and Exponential Backoff in AWS](https://docs.aws.amazon.com/general/latest/gr/api-retries.html) in the *Amazon Web Services General Reference*.
+ If you don't use the AWS SDK features for retry and backoff, allow a pause (for example, 200 ms) before retrying the [ReceiveMessage](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/APIReference/API_ReceiveMessage.html) action after receiving no messages, a timeout, or an error message from Amazon SQS. For subsequent use of `ReceiveMessage` that gives the same results, allow a longer pause (for example, 400 ms). 