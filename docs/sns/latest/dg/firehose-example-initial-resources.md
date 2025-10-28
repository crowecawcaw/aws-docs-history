# Setting-up initial AWS

resources for Amazon SNS message archiving and analytics

This topic describes how to create the resources needed for the [message archiving and analytics example use
case](firehose-example-use-case.md "firehose-example-use-case.md"):

- An Amazon Simple Storage Service (Amazon S3) bucket
- Two Amazon Simple Queue Service (Amazon SQS) queues
- An Amazon SNS topic
- Two Amazon SQS subscriptions to the Amazon SNS topic

###### To create the initial resources

1.  Create the Amazon S3 bucket:
    1. Open the [Amazon S3 console](https://console.aws.amazon.com/s3/home "https://console.aws.amazon.com/s3/home").
    2. Choose **Create bucket**.
    3. For **Bucket name**, enter a globally unique name. Keep the other
       fields as the defaults.
    4. Choose **Create bucket**.For more information about Amazon S3 buckets, see [Creating a bucket](../../../AmazonS3/latest/userguide/CreatingABucket.md "../../../AmazonS3/latest/userguide/CreatingABucket.md") in the
       _Amazon Simple Storage Service User Guide_ and [Working
       with Amazon S3 Buckets](../../../AmazonS3/latest/userguide/UsingBucket.md "../../../AmazonS3/latest/userguide/UsingBucket.md") in the _Amazon Simple Storage Service User Guide_.

2.  Create the two Amazon SQS queues:
    1. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/home "https://console.aws.amazon.com/sqs/home").
    2. Choose **Create queue**.
    3. For **Type**, choose **Standard**.
    4. For **Name**, enter
       `ticketPaymentQueue`.
    5. Under **Access policy**, for **Choose method**,
       choose **Advanced**.
    6. In the JSON policy box, paste the following policy:

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Principal": {
     "Service": "sns.amazonaws.com"
     },
     "Action": "sqs:SendMessage",
     "Resource": "*",
     "Condition": {
     "ArnEquals": {
     "aws:SourceArn": "arn:aws:sns:us-east-1:123456789012:ticketTopic"
     }
     }
     }
     ]
    }`

    ```

    In this access policy, replace the AWS account number
    (`123456789012`) with your own, and change the AWS Region
    (`us-east-1`) accordingly. 7. Choose **Create queue**. 8. Repeat these steps to create a second SQS queue named
    `ticketFraudQueue`.For more information on creating SQS queues, see [Creating an Amazon SQS queue
    (console)](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-create-queue.md") in the _Amazon Simple Queue Service Developer Guide_.

3.  Create the SNS topic:
    1. Open the [Topics page](https://console.aws.amazon.com/sns/home#/topics "https://console.aws.amazon.com/sns/home#/topics") of
       the Amazon SNS console.
    2. Choose **Create topic**.
    3. Under **Details**, for **Type**, choose
       **Standard**.
    4. For **Name**, enter `ticketTopic`.
    5. Choose **Create topic**.For more information on creating SNS topics, see [Creating an Amazon SNS topic](sns-create-topic.md "sns-create-topic.md").

4.  Subscribe both SQS queues to the SNS topic:

        1. In the [Amazon SNS console](https://console.aws.amazon.com/sns/home#/topics "https://console.aws.amazon.com/sns/home#/topics"), on
         the **ticketTopic** topic's details page, choose **Create
         subscription**.
        2. Under **Details**, for **Protocol**, choose
         **Amazon SQS**.
        3. For **Endpoint**, choose the Amazon Resource Name (ARN) of the
         **ticketPaymentQueue** queue.
        4. Choose **Create subscription**.
        5. Repeat these steps to create a second subscription using the ARN of the
         **ticketFraudQueue** queue.


        For more information on subscribing to SNS topics, see [Creating a subscription to an Amazon SNS
         topic](sns-create-subscribe-endpoint-to-topic.md "sns-create-subscribe-endpoint-to-topic.md"). You can also subscribe SQS
         queues to SNS topics from the Amazon SQS console. For more information, see [Subscribing an Amazon SQS
         queue to an Amazon SNS topic (console)](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-subscribe-queue-sns-topic.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-configure-subscribe-queue-sns-topic.md") in the
         *Amazon Simple Queue Service Developer Guide*.

    You've created the initial resources for this example use case. To continue, see [Setting-up a Amazon Data Firehose delivery stream for
    Amazon SNS message archiving](firehose-example-create-delivery-stream.md "firehose-example-create-delivery-stream.md").
