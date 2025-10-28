# Step 3: Verifying Amazon SNS

application and pipeline performance

## Step 1: Verifying the execution

of the sample checkout pipeline

1. Sign in to the [Amazon DynamoDB
   console](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. On the navigation panel, choose **Tables**.
3. Search for `serverlessrepo-fork-example` and choose
   `CheckoutTable`.
4. On the table details page, choose **Items** and then
   choose the created item.

The stored attributes are displayed.

## Step 2: Verifying

the execution of the event storage and backup pipeline

1. Sign in to the [Amazon S3
   console](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. On the navigation panel, choose **Buckets**.
3. Search for `serverlessrepo-fork-example` and then choose
   `CheckoutBucket`.
4. Navigate the directory hierarchy until you find a file with the extension
   `.gz`.
5. To download the file, choose **Actions**,
   **Open**.
6. The pipeline is configured with a Lambda function that sanitizes credit
   card information for compliance reasons.

To verify that the stored JSON payload doesn't contain any credit card
information, decompress the file.

## Step 3: Verifying

the execution of the event search and analytics pipeline

1. Sign in to the [OpenSearch Service
   console](https://console.aws.amazon.com/aos/ "https://console.aws.amazon.com/aos/").
2. On the navigation panel, under **My domains**, choose the
   domain prefixed with `serverl-analyt`.
3. The pipeline is configured with an Amazon SNS subscription filter policy that
   sets a numeric matching condition.

To verify that the event is indexed because it refers to an order whose
value is higher than USD $100, on the
**serverl-analyt-`abcdefgh1ijk`**
page, choose **Indices**,
**checkout_events**.

## Step 4: Verifying the

execution of the event replay pipeline

1. Sign in to the [Amazon SQS
   console](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. In the list of queues, search for `serverlessrepo-fork-example`
   and choose `ReplayQueue`.
3. Choose **Send and receive messages**.
4. In the **Send and receive messages in
   fork-example-ecommerce-`my-app`...ReplayP-ReplayQueue-`123ABCD4E5F6`**
   dialog box, choose **Poll for messages**.
5. To verify that the event is enqueued, choose **More
   Details** next to the message that appears in the queue.
