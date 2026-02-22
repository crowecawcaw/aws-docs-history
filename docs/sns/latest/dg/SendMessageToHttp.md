# Step 6: Send Amazon SNS messages to the HTTP/HTTPS

endpoint

You can send a message to a topic's subscriptions by publishing to the topic. To publish
to a topic, you can use the Amazon SNS console, the `sns-publish` CLI command, or the `Publish` API.

If you followed [Step 1](SendMessageToHttp.md "SendMessageToHttp.md"), the code that you
deployed at your endpoint should process the notification.

###### To publish to a topic using the Amazon SNS console

1. Using the credentials of the AWS account or IAM user with permission to publish to
   the topic, sign in to the AWS Management Console and open the Amazon SNS console at [https://console.aws.amazon.com/sns/](https://console.aws.amazon.com/sns/home "https://console.aws.amazon.com/sns/home").
2. On the navigation panel, choose **Topics** and then choose a
   topic.
3. Choose the **Publish message** button.
4. In the **Subject** box, enter a subject (for example,
   `Testing publish to my endpoint`).
5. In the **Message** box, enter some text (for example,
   `Hello world!`), and choose **Publish
   message**.

The following message appears: Your message has been successfully published.
