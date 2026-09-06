

# Step 3: Verifying Amazon SNS application and pipeline performance
<a name="verify-sample-application-pipelines"></a>

## Step 1: Verifying the execution of the sample checkout pipeline
<a name="verify-execution-checkout-pipeline"></a>

1. Sign in to the [Amazon DynamoDB console](https://console.aws.amazon.com/dynamodb/).

1. On the navigation panel, choose **Tables**.

1. Search for `serverlessrepo-fork-example` and choose `CheckoutTable`.

1. On the table details page, choose **Items** and then choose the created item.

   The stored attributes are displayed.

## Step 2: Verifying the execution of the event storage and backup pipeline
<a name="verify-execution-event-storage-backup-pipeline"></a>

1. Sign in to the [Amazon S3 console](https://console.aws.amazon.com/s3/).

1. On the navigation panel, choose **Buckets**.

1. Search for `serverlessrepo-fork-example` and then choose `CheckoutBucket`.

1. Navigate the directory hierarchy until you find a file with the extension `.gz`.

1. To download the file, choose **Actions**, **Open**.

1. The pipeline is configured with a Lambda function that sanitizes credit card information for compliance reasons.

   To verify that the stored JSON payload doesn't contain any credit card information, decompress the file.

## Step 3: Verifying the execution of the event search and analytics pipeline
<a name="verify-execution-event-search-analytics-pipeline"></a>

1. Sign in to the [OpenSearch Service console](https://console.aws.amazon.com/aos/).

1. On the navigation panel, under **My domains**, choose the domain prefixed with `serverl-analyt`.

1. The pipeline is configured with an Amazon SNS subscription filter policy that sets a numeric matching condition.

   To verify that the event is indexed because it refers to an order whose value is higher than USD $100, on the **serverl-analyt-{{abcdefgh1ijk}}** page, choose **Indices**, **checkout\_events**.

## Step 4: Verifying the execution of the event replay pipeline
<a name="verify-execution-event-replay-pipeline"></a>

1. Sign in to the [Amazon SQS console](https://console.aws.amazon.com/sqs/).

1. In the list of queues, search for `serverlessrepo-fork-example` and choose `ReplayQueue`.

1. Choose **Send and receive messages**.

1. In the **Send and receive messages in fork-example-ecommerce-{{my-app}}...ReplayP-ReplayQueue-{{123ABCD4E5F6}}** dialog box, choose **Poll for messages**. 

1. To verify that the event is enqueued, choose **More Details** next to the message that appears in the queue.