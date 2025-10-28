# Tutorial: Sending Amazon SNS alerts for available software

updates

In this tutorial, you configure an Amazon EventBridge event rule that captures notifications for
available service software updates in Amazon OpenSearch Service and sends you an email notification
through Amazon Simple Notification Service (Amazon SNS).

## Prerequisites

This tutorial assumes that you have an existing OpenSearch Service domain. If you haven't
created a domain, follow the steps in [Creating and managing Amazon OpenSearch Service domains](createupdatedomains.md "createupdatedomains.md") to
create one.

## Step 1: Create and subscribe to an Amazon SNS

topic

Configure an Amazon SNS topic to serve as an event target for your new event
rule.

**To create an Amazon SNS target**

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. Choose **Topics** and **Create
   topic**.
3. For the job type, choose **Standard**, and name the job
   **software-update**.
4. Choose **Create topic**.
5. After the topic is created, choose **Create
   subscription**.
6. For **Protocol**, choose **Email**. For
   **Endpoint**, enter an email address that you currently
   have access to and choose **Create subscription**.
7. Check your email account and wait to receive a subscription confirmation
   email message. When you receive it, choose **Confirm
   subscription**.

## Step 2: Register an event rule

Next, register an event rule that captures only service software update
events.

**To create an event rule**

1. Open the EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/ "https://console.aws.amazon.com/events/").
2. Choose **Create rule**.
3. Name the rule **softwareupdate-rule**.
4. Choose **Next**.
5. For the event pattern, select **AWS services**,
   **Amazon OpenSearch Service (managed cluster)**, and **Amazon
   OpenSearch Service Software Update Notification**. This pattern
   matches any service software update event from OpenSearch Service. For more information
   about event patterns, see [Amazon EventBridge event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in the _Amazon EventBridge
   User Guide_.
6. Optionally, you can filter to only specific severities. For the severities
   of each event, see [Service software update events](monitoring-events.md#monitoring-events-sso "monitoring-events.md#monitoring-events-sso").
7. Choose **Next**.
8. For the target, choose **SNS topic** and select
   **software-update**.
9. Choose **Next**.
10. Skip the tags and choose **Next**.
11. Review the rule configuration and choose **Create
    rule**.

The next time you receive a notification from OpenSearch Service about an available service
software update, if everything is configured properly, Amazon SNS should send you an
email alert about the update.
