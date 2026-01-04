# Step 2: Subscribe the HTTP/HTTPS endpoint to the

Amazon SNS topic

To send messages to an HTTP or HTTPS endpoint through a topic, you must subscribe the
endpoint to the Amazon SNS topic. You specify the endpoint using its URL. To subscribe to a topic,
you can use the Amazon SNS console, the [sns-subscribe](../../../cli/latest/reference/sns/subscribe.md "../../../cli/latest/reference/sns/subscribe.md") command, or the [Subscribe](../api/API_Subscribe.md "../api/API_Subscribe.md") API action. Before you start, make sure you have the URL for the endpoint
that you want to subscribe and that your endpoint is prepared to receive the confirmation and
notification messages as described in Step 1.

###### To subscribe an HTTP or HTTPS endpoint to a topic using the Amazon SNS console

1. Sign in to the [Amazon SNS console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. On the navigation panel, choose **Subscriptions**.
3. Choose the **Create subscription**.
4. In the **Protocol** drop-down list, select **HTTP**
   or **HTTPS**.
5. In the **Endpoint** box, paste in the URL for the endpoint that you
   want the topic to send messages to and then choose **Create
   subscription**.
6. The confirmation message is displayed. Choose **Close**.

Your new subscription's **Subscription ID** displays
PendingConfirmation. When you confirm the subscription, **Subscription
ID** will display the subscription ID.
