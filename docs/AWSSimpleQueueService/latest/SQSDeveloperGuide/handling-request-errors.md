# Handling request errors in Amazon SQS

To handle request errors, use one of the following strategies:

- If you use an AWS SDK, you already have automatic _retry and
  backoff_ logic at your disposal. For more information, see [Error Retries and Exponential Backoff in
  AWS](../../../general/latest/gr/api-retries.md "../../../general/latest/gr/api-retries.md") in the _Amazon Web Services General Reference_.
- If you don't use the AWS SDK features for retry and backoff, allow a pause
  (for example, 200 ms) before retrying the [ReceiveMessage](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md") action
  after receiving no messages, a timeout, or an error message from Amazon SQS. For
  subsequent use of `ReceiveMessage` that gives the same results, allow
  a longer pause (for example, 400 ms).
