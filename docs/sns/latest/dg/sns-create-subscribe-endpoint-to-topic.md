# Creating a subscription to an Amazon SNS

topic

To receive messages published to [a topic](sns-create-topic.md "sns-create-topic.md"), you must
_subscribe_ an [endpoint](#sns-endpoints "#sns-endpoints") to the
topic. When you subscribe an endpoint to a topic, the endpoint begins to receive messages
published to the associated topic.

###### Note

HTTP(S) endpoints, email addresses, and AWS resources in other AWS accounts
require confirmation of the subscription before they can receive messages.

## To subscribe an endpoint to an Amazon SNS

topic

Subscribing an endpoint to an Amazon SNS topic enables message delivery to the specified
endpoint, ensuring the right systems or users receive notifications when a message is
published to the topic. This step is essential for linking the topic to
consumers—whether they are applications, email recipients, or other services—allowing
for seamless communication across systems.

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the left navigation pane, choose **Subscriptions**.
3. On the **Subscriptions** page, choose **Create
   subscription**.
4. On the **Create subscription** page, in the
   **Details** section, do the following:
   1. For **Topic ARN**, choose the Amazon Resource Name
      (ARN) of a topic. This value is the AWS ARN that was
      generated when you created the Amazon SNS topic, for example
      `arn:aws:sns:us-east-2:123456789012:your_topic`.
   2. For **Protocol**, choose an endpoint type. The available endpoint types are:
      - [HTTP/HTTPS](sns-http-https-endpoint-as-subscriber.md "sns-http-https-endpoint-as-subscriber.md")
      - [Email/Email-JSON](sns-email-notifications.md "sns-email-notifications.md")
      -
      - [Amazon SQS](sns-sqs-as-subscriber.md "sns-sqs-as-subscriber.md")

      ###### Note

      To subscribe to an [SNS
      FIFO topic](sns-fifo-topics.md "sns-fifo-topics.md"), choose this option.
      - [AWS Lambda](sns-lambda-as-subscriber.md "sns-lambda-as-subscriber.md")
      - [Platform application
        endpoint](sns-mobile-application-as-subscriber.md "sns-mobile-application-as-subscriber.md")
      - [SMS](sns-mobile-phone-number-as-subscriber.md "sns-mobile-phone-number-as-subscriber.md")

   3. For **Endpoint**, enter the endpoint value, such as
      an email address or the ARN of an Amazon SQS queue.
   4. Firehose endpoints only: For **Subscription role ARN**,
      specify the ARN of the IAM role that you created for writing to Firehose
      delivery streams. For more information, see [Prerequisites for subscribing Firehose delivery
      streams to Amazon SNS topics](prereqs-kinesis-data-firehose.md "prereqs-kinesis-data-firehose.md").
   5. (Optional) For Firehose, Amazon SQS, HTTP/S endpoints, you can also enable raw
      message delivery. For more information, see [Amazon SNS raw message delivery](sns-large-payload-raw-message-delivery.md "sns-large-payload-raw-message-delivery.md").
   6. (Optional) To configure a filter policy, expand the
      **Subscription filter policy** section. For more
      information, see [Amazon SNS subscription filter
      policies](sns-subscription-filter-policies.md "sns-subscription-filter-policies.md").
   7. (Optional) To enable payload-based filtering, configure `Filter
Policy Scope` to `MessageBody`. For more
      information, see [Amazon SNS subscription filter policy
      scope](sns-message-filtering-scope.md "sns-message-filtering-scope.md").
   8. (Optional) To configure a dead-letter queue for the subscription,
      expand the **Redrive policy (dead-letter queue)**
      section. For more information, see [Amazon SNS dead-letter queues](sns-dead-letter-queues.md "sns-dead-letter-queues.md").
   9. Choose **Create subscription**.

   The console creates the subscription and opens the subscription's
   **Details** page.
