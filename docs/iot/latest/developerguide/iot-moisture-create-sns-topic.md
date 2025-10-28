# Step 3: Create an Amazon SNS topic and

subscription

Create an Amazon SNS topic and subscription.

1. From the [AWS SNS
   console](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home"), in the navigation pane, choose
   **Topics**, and then choose **Create
   topic**.
2. Choose type as **Standard** and enter a name for the
   topic (for example, `MoistureSensorTopic`).
3. Enter a display name for the topic (for example, `Moisture
Sensor Topic`). This is the name displayed for your topic in
   the Amazon SNS console.
4. Choose **Create topic**.
5. In the Amazon SNS topic detail page, choose **Create
   subscription**.
6. For **Protocol**, choose
   **Email**.
7. For **Endpoint**, enter your email address.
8. Choose **Create subscription**.
9. Open your email client and look for a message with the subject
   `MoistureSensorTopic`. Open the email and click the
   **Confirm subscription** link.

###### Important

You won't receive any email alerts from this Amazon SNS topic until you
confirm the subscription.
You should receive an email message with the text you typed.
