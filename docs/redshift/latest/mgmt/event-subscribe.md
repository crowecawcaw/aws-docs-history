Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating an event notification subscription

You can create an Amazon Simple Notification Service (Amazon SNS) event notification subscription to send
notifications when an event occurs for a given Amazon Redshift cluster, snapshot, security
group, or parameter group. These notifications are sent to an SNS topic, which in turn
transmits messages to any SNS consumers subscribed to the topic.

The SNS messages to the consumers can be in any notification form supported by Amazon SNS
for an AWS Region, such as an email, a text message, or a call to an HTTP endpoint.
For example, all regions support email notifications, but SMS notifications can only be
created in the US East (N. Virginia) Region. For more information, see [Amazon Redshift provisioned cluster event
notifications](working-with-event-notifications.md "working-with-event-notifications.md").

###### To create an event subscription

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Events**.
3. Choose the **Event subscription** tab, then choose
   **Create event subscriptions**.
4. Enter the properties of your event subscription, such as name, source type,
   category, and severity. You can also enable Amazon SNS topics to get notified of
   events.
5. Choose **Create event subscriptions** to create your
   subscription.
