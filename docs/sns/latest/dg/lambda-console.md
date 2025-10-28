# Subscribing a Lambda function to an Amazon SNS topic

This topic explains how to subscribe a Lambda function to an Amazon SNS topic, enabling the
function to be triggered by published messages.

1.  Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2.  On the navigation panel, choose **Topics**.
3.  On the **Topics** page, choose a topic.
4.  In the **Subscriptions** section, choose **Create
    subscription**.
5.  On the **Create subscription** page, in the
    **Details** section, do the following:

        1. Verify the chosen **Topic ARN**.
        2. For **Protocol** choose AWS Lambda.
        3. For **Endpoint** enter the ARN of a function.
        4. Choose **Create subscription**.

    When a message is published to an SNS topic that has a Lambda function subscribed to it,
    the Lambda function is invoked with the payload of the published message. For information about
    how to use AWS Lambda with Amazon SNS, including a tutorial, see [Using AWS Lambda with Amazon SNS](../../../lambda/latest/dg/with-sns.md "../../../lambda/latest/dg/with-sns.md").
