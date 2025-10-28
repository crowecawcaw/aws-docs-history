# Tutorial: Create and subscribe to an Amazon SNS topic

For this tutorial, you configure an Amazon SNS topic to serve as an event target for your new event rule.

###### To create an Amazon SNS topic

1. Open the Amazon SNS console at
   [https://console.aws.amazon.com/sns/v3/home](https://console.aws.amazon.com/sns/v3/home "https://console.aws.amazon.com/sns/v3/home").
2. Choose **Topics**, **Create topic**.
3. For **Type**, choose **Standard**.
4. For **Name**, enter `MembershipUpdated` and choose
   **Create topic**.
5. On the **MembershipUpdated** screen, choose **Create
   subscription**.
6. For **Protocol**, choose **Email**.
7. For **Endpoint**, enter an email address that you currently have access
   to and choose **Create subscription**.
8. Check your email account, and wait to receive a subscription confirmation email message.
   When you receive it, choose **Confirm subscription**.
