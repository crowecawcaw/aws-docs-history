# Tutorial: Send an email when events happen using Amazon EventBridge

You can send email notifications when [Amazon Simple Storage Service
(Amazon S3)](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") objects are created using Amazon EventBridge and [Amazon SNS](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md"). In this tutorial, you will create an SNS
topic and subscription. Then, you will create a [rule](eb-rules.md "eb-rules.md") in the
EventBridge console that sends [events](eb-events.md "eb-events.md") to that topic when Amazon S3
`Object Created` events are received.

###### Steps:

- [Prerequisites](#eb-s3-object-created-tutorial-prerequisite "#eb-s3-object-created-tutorial-prerequisite")
- [Step 1: Create an Amazon SNS topic](#eb-s3-object-created-tutorial-create-topic "#eb-s3-object-created-tutorial-create-topic")
- [Step 2: Create an Amazon SNS subscription](#eb-s3-object-created-tutorial-create-sns "#eb-s3-object-created-tutorial-create-sns")
- [Step 3: Create a rule](#eb-s3-object-created-tutorial-create-rule "#eb-s3-object-created-tutorial-create-rule")
- [Step 4: Test the rule](#eb-s3-object-created-tutorial-test-rule "#eb-s3-object-created-tutorial-test-rule")
- [Step 5: Clean up your resources](#cleanup "#cleanup")

## Prerequisites

To recieve Amazon S3 events in EventBridge, you must enable EventBridge in the Amazon S3 console. This
tutorial assumes EventBridge is enabled. For more information, see [Enabling Amazon EventBridge in
the S3 console](../../../AmazonS3/latest/userguide/enable-event-notifications-eventbridge.md "../../../AmazonS3/latest/userguide/enable-event-notifications-eventbridge.md").

## Step 1: Create an Amazon SNS topic

Create a topic to receive the events from EventBridge.

###### To create a topic

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Topics**.
3. Choose **Create topic**.
4. For **Type**, choose
   **Standard**.
5. Enter `eventbridge-test` as the name of the topic.
6. Choose **Create topic**.

## Step 2: Create an Amazon SNS subscription

Create a subscription to get email notifications from Amazon S3 when events are received by
the topic.

###### To create a subscription

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation pane, choose **Subscriptions**.
3. Choose **Create subscription**.
4. For **Topic ARN**, choose the topic you created in step 1.
   For this tutorial, choose **eventbridge-test**.
5. For **Protocol**, choose **Email**.
6. For **Endpoint**, enter your email address.
7. Choose **Create subscription**.
8. Confirm the subscription by choosing **Confirm subscription** in the email you receive from
   AWS notifications.

## Step 3: Create a rule

Create a rule to send events to your topic when an Amazon S3 object is created.

###### To create a rule

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. In the navigation pane, choose **Rules**.
3. Choose **Create rule**.
4. Enter a name and description for the rule. For example, name the rule `s3-test`
5. For **Event bus**, select **default**.
6. For **Rule type**, choose **Rule with an event
   pattern**.
7. Choose **Next**.
8. For **Event source**, choose
   **AWS events or EventBridge partner events**.
9. For **Creation method**, choose
   **Use pattern form**.
10. For **Event pattern**, do the following:
    1. For **Event source**, select **AWS services** from the drop-down list.
    2. For **AWS service**, select **Simple Storage Service (S3)** from the drop-down list.
    3. For **Event type**, choose **Amazon S3
       Event Notification** from the drop-down list.
    4. Choose **Specific events(s)** and choose **Object Created** from the drop-down list.
    5. Choose **Any bucket**

11. Choose **Next**.
12. For **Target types**, choose **AWS service**.
13. For **Select a target**, choose **SNS
    topic** from the drop-down list.
14. For **Topic**, select the Amazon SNS topic that you created
    in the **Step 1: Create an SNS topic** section. In this example, select `eventbridge-test`.
15. Choose **Next**.
16. Choose **Next**.
17. Review the details of the rule and choose **Create rule**.

## Step 4: Test the rule

To test your rule, create an Amazon S3 object by uploading a file to an EventBridge-enabled
bucket. Then, wait a few minutes and verify if you receive an email from AWS
notifications.

## Step 5: Clean up your resources

You can now delete the resources that you created for this tutorial, unless you want to retain them. By deleting AWS resources that you are no longer using, you prevent unnecessary charges to your AWS account.

###### To delete the SNS topic

1. Open the [Topics page](https://console.aws.amazon.com/sns/v3/home#/topics "https://console.aws.amazon.com/sns/v3/home#/topics") of the SNS console.
2. Select the topic that you created.
3. Choose **Delete**.
4. Enter `delete me`.
5. Choose **Delete**.

###### To delete the SNS subscription

1. Open the [Subscriptions page](https://console.aws.amazon.com/sns/v3/home#/subscriptions "https://console.aws.amazon.com/sns/v3/home#/subscriptions") of the SNS console.
2. Select the subscription that you created.
3. Choose **Delete**.
4. Choose **Delete**.

###### To delete the EventBridge rule(s)

1. Open the [Rules page](https://console.aws.amazon.com/events/home#/rules "https://console.aws.amazon.com/events/home#/rules") of the EventBridge console.
2. Select the rule(s) that you created.
3. Choose **Delete**.
4. Choose **Delete**.
