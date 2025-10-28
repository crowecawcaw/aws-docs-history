# Subscribe to EC2 Windows launch agent notifications

Amazon SNS can notify you when new versions of the EC2 launch agents are released. Use
the following procedure to subscribe to these notifications.

###### Subscribe to EC2Config notifications

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. In the navigation bar, change the Region to
   **US East (N. Virginia)**, if necessary. You must select
   this Region because the SNS notifications that you are subscribing to were
   created in this Region.
3. In the navigation pane, choose **Subscriptions**.
4. Choose **Create subscription**.
5. In the **Create subscription** dialog box, do the
   following:
   1. For **Topic ARN**, use the following Amazon
      Resource Name (ARN) that matches the agent you want to receive
      notifications for:
      - **EC2Launch v2**:

      ```
      `arn:aws:sns:us-east-1:309726204594:amazon-ec2launch-v2`
      ```

      - **EC2Launch or EC2Config**:

      ```
      `arn:aws:sns:us-east-1:801119661308:ec2-windows-ec2config`
      ```

   2. For **Protocol**, choose `Email`.
   3. For **Endpoint**, enter the email address where you
      want to receive the notifications.
   4. Choose **Create subscription**.

6. You'll receive a email asking you to confirm your subscription.
   Open the email and follow the directions to complete your subscription.
   Whenever a new version of the launch agent is released, we send notifications
   to subscribers. If you no longer want to receive these notifications, use the
   following procedure to unsubscribe.

###### Unsubscribe from launch agent notifications

1. Open the Amazon SNS console.
2. In the navigation pane, choose **Subscriptions**.
3. Select the subscription and then choose **Actions**,
   **Delete subscriptions**. When prompted for confirmation,
   choose **Delete**.
