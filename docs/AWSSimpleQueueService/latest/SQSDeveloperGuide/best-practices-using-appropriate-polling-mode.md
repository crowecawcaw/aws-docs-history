# Using the appropriate

polling mode in Amazon SQS

- Long polling lets you consume messages from your Amazon SQS queue as soon as they
  become available.
  - To reduce the cost of using Amazon SQS and to decrease the number of empty
    receives to an empty queue (responses to the `ReceiveMessage`
    action which return no messages), enable long polling. For more
    information, see [Amazon SQS Long
    Polling](sqs-short-and-long-polling.md "sqs-short-and-long-polling.md").
  - To increase efficiency when polling for multiple threads with multiple
    receives, decrease the number of threads.
  - Long polling is preferable over short polling in most cases.

- Short polling returns responses immediately, even if the polled Amazon SQS queue is
  empty.
  - To satisfy the requirements of an application that expects immediate
    responses to the `ReceiveMessage` request, use short
    polling.
  - Short polling is billed the same as long polling.
