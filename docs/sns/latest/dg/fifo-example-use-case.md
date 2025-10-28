# Amazon SNS FIFO topic example use case

The following example describes an ecommerce platform built by an auto parts manufacturer
using Amazon SNS FIFO topics and Amazon SQS queues. The platform is composed of four serverless
applications:

- Inventory managers use a price management application to set the price for each item in
  stock. At this company, product prices can change based on currency exchange fluctuation,
  market demand, and shifts in sales strategy. The price management application uses an
  AWS Lambda function that publishes price updates to an Amazon SNS FIFO topic whenever prices
  change.
- A wholesale application provides the backend for a website where auto body shops and car
  manufacturers can buy the company's auto parts in bulk. To get price change notifications,
  the wholesale application subscribes its Amazon SQS FIFO queue to the price management
  application's Amazon SNS FIFO topic.
- A retail application provides the backend for another website where car owners and car
  tuning enthusiasts can purchase individual auto parts for their vehicles. To get price
  change notifications, the retail application also subscribes its Amazon SQS FIFO queue to the
  price management application's Amazon SNS FIFO topic.
- An analytics application that aggregates price updates and stores them into an
  Amazon S3 bucket, enabling Amazon Athena to query the bucket for business intelligence
  (BI) purposes. To get price change notifications, the analytics application subscribes its
  Amazon SQS standard queue to the price management application's Amazon SNS FIFO topic. Unlike the
  other applications, the analytics one doesn't require the price updates to be strictly
  ordered.

![An example of an ecommerce platform created by an auto parts manufacturer using Amazon SNS FIFO topics and Amazon SQS queues, showing how different serverless applications, such as price management, wholesale, retail, and analytics, leverage these services for ordered message delivery and deduplication. This setup ensures that wholesale and retail applications receive price updates in the correct order, while the analytics application aggregates data for business intelligence purposes without requiring strict message ordering.](images/sns-fifo-usecase.png)
For the wholesale and retail applications to receive price updates in the correct order, the
price management application must use a strictly ordered message distribution system. Using
Amazon SNS FIFO topics and Amazon SQS FIFO queues enables the processing of messages in order and with no
duplication. For more information, see [Amazon SNS message ordering details for FIFO
topics](fifo-topic-message-ordering.md "fifo-topic-message-ordering.md"). For code snippets that implement this use case,
see [Amazon SNS code examples for FIFO topics](fifo-topic-code-examples.md "fifo-topic-code-examples.md").
