End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# EventBridgeTutorial: Send Amazon Simple Notification Service alerts for AWS Proton service status changes

In this tutorial, you use an AWS Proton pre-configured _event rule_ that captures status changes for your AWS Proton service. EventBridge
sends the status changes to an Amazon SNS topic. You subscribe to the topic and Amazon SNS sends you status change emails for your AWS Proton service.

## Prerequisites

You have an existing AWS Proton service with an `Active` status. As part of this tutorial, you can add service instances to this service,
and then delete the instances.

If you need to create an AWS Proton service, see [Getting started with AWS Proton](ag-getting-started.md "ag-getting-started.md"). For more information, see [AWS Proton quotas](ag-limits.md "ag-limits.md") and [Edit a service](ag-svc-update.md "ag-svc-update.md").

## Step 1: Create and subscribe to an Amazon SNS topic

Create an Amazon SNS topic to serve as an _event target_ for the _event rule_ that you create in Step 2.

###### Create an Amazon SNS topic

1. Log in and open the [Amazon SNS console](https://console.aws.amazon.com//sns/v3/ "https://console.aws.amazon.com//sns/v3/").
2. In the navigation pane, choose **Topics**, **Create topic**.
3. In **Create topic** page:
   1. Choose **Type**
      **Standard**.
   2. For **Name**, enter `tutorial-service-status-change` and choose **Create
      topic**.

4. In the **tutorial-service-status-change** detail page, choose **Create subscription**.
5. In the **Create subscription** page:
   1. For **Protocol**, choose **Email**.
   2. For **Endpoint**, enter an email address that you currently have access to and choose **Create
      subscription**.

6. Check your email account and wait to receive a subscription confirmation email message. When you receive it, open it and choose **Confirm
   subscription**.

## Step 2: Register an event rule

Register an _event rule_ that captures status changes for your AWS Proton service. For more information, see [Prerequisites](#event-tutorial-sns-prereq "#event-tutorial-sns-prereq").

###### Create an event rule.

1. Open the [Amazon EventBridge console](https://console.aws.amazon.com//events/ "https://console.aws.amazon.com//events/").
2. In the navigation pane, choose **Events**, **Rules**.
3. In the **Rules** page, in the **Rules** section, choose **Create rule**.
4. In the **Create rule** page:
   1. In the **Name and description** section, for **Name**, enter `tutorial-rule`.
   2. In the **Define pattern** section, choose **Event pattern**.
      1. For **Event matching pattern**, choose **Pre-defined by service**.
      2. For **Service provider**, choose **AWS**.
      3. For **Service name**, choose **AWS Proton**.
      4. For **Event type**, choose **AWS Proton Service Status Change**.

      The **Event pattern** appears in a text editor. 5. Open the [AWS Proton console](https://console.aws.amazon.com//proton/ "https://console.aws.amazon.com//proton/"). 6. In the navigation pane, choose **Services**. 7. In **Services** page, choose the name of your AWS Proton service. 8. In **Service details** page, copy the service Amazon Resource Name (ARN). 9. Navigate back to the _EventBridge console_ and your tutorial rule and choose **Edit** at the text
      editor. 10. In the text editor, for `"resources":`, enter the service ARN that you copied in step viii.

      ```
      {
          "source": ["aws.proton"],
          "detail-type": ["AWS Proton Service Status Change"],
          "resources": ["arn:aws:proton:`region-id`:`123456789012`:service/`your-service`"]
      }
      ```

      11. **Save** the event pattern.

   3. In the **Select targets** section:
      1. For **Target**, choose **SNS topic**.
      2. For **Topic**, choose **tutorial-service-status-change**.

   4. Choose **Create**.

## Step 3: Test your event rule

Verify that your _event rule_ is working by adding an instance to your AWS Proton service.

1. Switch to the [AWS Proton console](https://console.aws.amazon.com//proton/ "https://console.aws.amazon.com//proton/").
2. In the navigation pane, choose **Services**.
3. In **Services** page, choose the name of your service.
4. In **Service details** page, choose **Edit**.
5. In **Configure service** page, choose **Next**.
6. In **Configure custom settings** page, in the **Service instances** section, choose **Add new
   instance**.
7. Complete the form for your **New instance**:
   1. Enter a **Name** for your new instance.
   2. Select the _same compatible environments_ that you chose for your existing instances.
   3. Enter values for the required inputs.
   4. Choose **Next**.

8. Review your inputs and choose **Update**.
9. After the **Service status** is `Active`, check your email to verify you received AWS notifications that give status
   updates.

```
{
    "version": "0",
    "id": "af76c382-2b3c-7a0a-cf01-936dff228276",
    "detail-type": "AWS Proton Service Status Change",
    "source": "aws.proton",
    "account": "123456789012",
    "time": "2021-06-29T20:40:16Z",
    "region": "region-id",
    "resources": ["arn:aws:proton:region-id:123456789012:service/your-service"],
    "detail": {
        "previousStatus": "ACTIVE",
        "status": "UPDATE_IN_PROGRESS",
        "name": "your-service"
    }
}
```

```
{
    "version": "0",
    "id": "87131e29-ad95-bda2-cd30-0ce825dfb0cd",
    "detail-type": "AWS Proton Service Status Change",
    "source": "aws.proton",
    "account": "123456789012",
    "time": "2021-06-29T20:42:27Z",
    "region": "region-id",
    "resources": ["arn:aws:proton:region-id:123456789012:service/your-service"],
    "detail": {
        "previousStatus": "UPDATE_IN_PROGRESS",
        "status": "ACTIVE",
        "name": "your-service"
    }
}
```

## Step 4: Clean up

Delete your Amazon SNS topic and subscription and delete your EventBridge rule.

###### Delete your Amazon SNS topic and subscription.

1. Navigate to the [Amazon SNS console](https://console.aws.amazon.com//sns/v3/ "https://console.aws.amazon.com//sns/v3/").
2. In the navigation panel, choose **Subscriptions**.
3. In the **Subscriptions** page, choose the subscription that you made to the topic named
   `tutorial-service-status-change` and then choose **Delete**.
4. In the navigation panel, choose **Topics**.
5. In the **Topics** page, choose the topic named `tutorial-service-status-change` and then choose
   **Delete**.
6. A modal prompts you to verify the deletion. Follow the instructions and choose **Delete**.

###### Delete your EventBridge rule.

1. Navigate to the [Amazon EventBridge console](https://console.aws.amazon.com//events/ "https://console.aws.amazon.com//events/").
2. In the navigation pane, choose **Events**, **Rules**.
3. In the **Rules** page, choose the rule named `tutorial-rule` and then choose **Delete**.
4. A modal prompts you to verify the deletion. Choose **Delete**.

###### Delete the added service instance.

1. Navigate to the [AWS Proton console](https://console.aws.amazon.com//proton/ "https://console.aws.amazon.com//proton/").
2. In the navigation pane, choose **Services**.
3. In the **Services** page, choose the name of your service.
4. In the **Service** detail page, choose **Edit** and then **Next**.
5. In **Configure custom settings** page, in the **Service instances** section, choose **Delete**
   for the service instance that you created as part of this tutorial and then choose **Next**.
6. Review your inputs and choose **Update**.
7. A modal prompts you to verify the deletion. Follow the instructions and choose **Yes, delete**.
