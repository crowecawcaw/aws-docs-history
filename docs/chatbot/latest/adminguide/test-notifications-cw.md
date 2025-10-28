AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Test notifications from AWS services to chat channels using CloudWatch

To verify that an Amazon Simple Notification Service (Amazon SNS) topic sends notifications to your chat channels, you can test your setup by sending a notification. Any SNS topic can send
notifications to your chat channels, but the topic must be assigned to a service supported by
Amazon Q Developer in chat applications. For more information about supported services, see [Supported services for Amazon Q Developer in chat applications](chatbot-services.md "chatbot-services.md").

###### Note

CloudWatch alarms and events are separately configured and have different characteristics for
use with Amazon Q Developer in chat applications.

The following procedure uses a CloudWatch alarm because most AWS services supported by Amazon Q Developer in chat applications
send their event and alarm data to CloudWatch.

You configure CloudWatch alarms using performance metrics from the services that are active in
your account. When you associate CloudWatch alarms with an Amazon SNS topic that is mapped to Amazon Q Developer in chat applications, the
Amazon SNS topic sends the CloudWatch alarm notifications to the chat channels. For more information, see
[Monitoring AWS services using Amazon Q Developer in chat applications](related-services.md "related-services.md") and the [Troubleshooting](chatbot-troubleshooting.md "chatbot-troubleshooting.md") topic.

###### To test notifications to configured

chat clients

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **Create
   alarm**.
3. Select the correct AWS **Region** at the top right of
   the AWS console, that contains the Amazon SNS topic you need. (**Tip:** to make sure you have the right Region for your SNS topics for testing
   alarms, you can check the Amazon Q Developer in chat applications configuration to see the regions for all configured SNS
   topics in each channel or webhook.)
4. Choose **Select metric**, and choose the **SNS**
   service namespace. (All CloudWatch alarms use service _metrics_ to generate
   their notifications, and you need to select one for this example.)
   1. Choose **Topic metrics**.
   2. Choose the check box for the SNS topic next to its **Topic Name**
      and **Metric Name**. Any SNS topics that you configured with
      Amazon Q Developer in chat applications appear in this list.

   _Important_: if you don't see your desired Amazon SNS topic in the
   SNS Topic list, make sure to select the correct AWS Region in the AWS console when
   you begin configuring the new CloudWatch alarm. 3. Choose **Select metric**.The **Specify metric and conditions** page shows a graph and other
   information about the metric and statistic.

5. For **Conditions** (the circumstances under which the CloudWatch alarm
   fires and an action takes place), choose the following options:
   1. For **Threshold type**, choose
      **Static**.
   2. For **Whenever _metric_ is**, choose
      **Lower/Equal <=threshold**.
   3. For **than...**, specify a threshold value of
      `1`. This setting ensures you will trigger the test
      notification within one minute.
   4. Under **Additional configuration**, do the following:
      1. For **Datapoints to alarm**, select **1 out of 1**.
      2. For **Missing data treatment**, select **Treat missing data as bad**.

   5. Choose **Next**.

6. Choose **Configure actions**. Here, you set the
   _action_ to create SNS notifications when the metric threshold is
   exceeded.

For **Notification**, choose the following options.

    1. For **Whenever this alarm state is...**, choose **In
     Alarm**.
    2. For **Select an SNS topic**, choose **Select an existing
     SNS topic**.
    3. For **Send a notification to...**, choose your SNS topic that has
     a subscription to Amazon Q Developer in chat applications. If the SNS topic is subscribed in Amazon Q Developer in chat applications, the endpoint
     value for Amazon Q Developer in chat applications appears in the **Email (endpoints)** field.


    ###### Note

    If the endpoint value doesn't appear in the **Email
     (endpoints)** field, make sure that the SNS topic is set up correctly in
     the Microsoft Teams channel, Slack channel or Amazon Chime webhook. For more information, see
     [Setting up Amazon Q Developer in chat applications with Microsoft Teams](teams-setup.md "teams-setup.md"),
     [Setting up Amazon Q Developer in chat applications with
     Slack](slack-setup.md "slack-setup.md"), or [Setting up Amazon Q Developer in chat applications with Amazon Chime](chime-setup.md "chime-setup.md").
    4. Choose **Next**.

7. Enter a name and description for the alarm. The name must contain only ASCII
   characters. Then, choose **Next**.
8. For **Preview and create**, confirm that the information and
   conditions are correct, then choose **Create alarm**.
   When the alarm triggers for the first time, you should receive the first test notification
   in your chat room, confirming that Amazon Q Developer in chat applications is working correctly and receiving alarm
   notifications from Amazon CloudWatch.
