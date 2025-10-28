# Subscribing a Firehose delivery stream to an Amazon SNS

topic

To deliver Amazon SNS notifications to [delivery streams](sns-firehose-as-subscriber.md "sns-firehose-as-subscriber.md"), first make sure that you've addressed all the [prerequisites](prereqs-kinesis-data-firehose.md "prereqs-kinesis-data-firehose.md"). For a list of supported
endpoints, see [endpoints
and quotas](../../../general/latest/gr/fh.md "../../../general/latest/gr/fh.md") in the _Amazon Web Services General Reference_.

###### To subscribe a Firehose delivery stream to a topic

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. In the navigation pane, choose **Subscriptions**.
3. On the **Subscriptions** page, choose **Create
   subscription**.
4. On the **Create subscription** page, in the
   **Details** section, do the following:
   1. For **Topic ARN**, choose the Amazon Resource Name (ARN) of a
      standard topic.
   2. For **Protocol**, choose **Firehose**.
   3. For **Endpoint**, choose the ARN of a Firehose delivery stream that
      can receive notifications from Amazon SNS.
   4. For **Subscription role ARN**, specify the ARN of the AWS Identity and Access Management
      (IAM) role that you created for writing to Firehose delivery streams. For more
      information, see [Prerequisites for subscribing Firehose delivery
      streams to Amazon SNS topics](prereqs-kinesis-data-firehose.md "prereqs-kinesis-data-firehose.md").
   5. (Optional) To remove any Amazon SNS metadata from published messages, choose
      **Enable raw message delivery**. For more information, see [Amazon SNS raw message delivery](sns-large-payload-raw-message-delivery.md "sns-large-payload-raw-message-delivery.md").

5. (Optional) To configure a filter policy, expand the **Subscription filter
   policy** section. For more information, see [Amazon SNS subscription filter
   policies](sns-subscription-filter-policies.md "sns-subscription-filter-policies.md").
6. (Optional) To configure a dead-letter queue for the subscription, expand the
   **Redrive policy (dead-letter queue)** section. For more information, see
   [Amazon SNS dead-letter queues](sns-dead-letter-queues.md "sns-dead-letter-queues.md").
7. Choose **Create subscription**.
   The console creates the subscription and opens the subscription's
   **Details** page.
