AWS Chatbot is now Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

# Accessing Amazon CloudWatch Logs for Amazon Q Developer in chat applications

###### Note

AWS Chatbot has integrated with Amazon Q Developer. [Learn more](service-rename.md "service-rename.md")

AWS provides event logging with Amazon CloudWatch Logs. With CloudWatch Logs for Amazon Q Developer in chat applications, you can see all the events
handled by Amazon Q Developer in chat applications. You can also see details of any error that may have prevented a notification
from appearing in your Amazon Chime or Slack chat room.

Possible errors that you can see with CloudWatch Logs include lack of permissions, unsupported events,
and events throttled by the chat client. For more information about these errors, see [Troubleshooting Amazon Q Developer in chat applications](chatbot-troubleshooting.md "chatbot-troubleshooting.md").

Amazon Q Developer in chat applications also provides an audit log of commands executed by Amazon Q Developer in chat applications in CloudWatch Logs. With CloudWatch Logs' audit log events for Amazon Q Developer in chat applications, you can see an audit log of executed commands and their chat workspace ID,
channel ID, and channel user ID attributes. The audit log events in CloudWatch Logs are always enabled and can't be disabled.

Amazon Q Developer in chat applications always logs audit events for command execution to CloudWatch Logs. You can choose to enable logging for all events, or only for errors.

###### Note

There is an additional charge for using CloudWatch Logs. For more details, see [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing "https://aws.amazon.com/cloudwatch/pricing").

## Enabling CloudWatch Logs

You can enable CloudWatch Logs during the setup flow of your Amazon Chime, Microsoft Teams, or Slack channel configuration.
For existing channels, you can edit the configuration to enable logging.

###### To enable CloudWatch Logs for a new configuration

1. On the **Configure channel** page, during the setup flow, under **Configuration details**, choose **Send logs to CloudWatch.**
2. Choose either **All events** or **Errors only**.
3. Continue the setup flow, then choose **Configure channel**.

###### To enable CloudWatch Logs for an existing configuration

1. In the Amazon Q Developer in chat applications console, under **Configured clients**, navigate to the chat client you want to edit.
2. From the list of existing configurations, choose the configuration you want to edit, then choose **Edit**.
3. On the **Edit** page, choose **Send logs to CloudWatch.**
4. Choose either **All events** or **Errors only**.
5. Choose **Save**.

## Viewing CloudWatch Logs

Your Amazon Q Developer in chat applications logs will be sent to CloudWatch under a designated CloudWatch Logs group for your configuration. The group name is **/aws/chatbot/`configuration-name`**.
To learn more about log groups and other CloudWatch concepts such as log events and log streams, see [Amazon CloudWatch Logs Concepts](../../../AmazonCloudWatch/latest/logs/CloudWatchLogsConcepts.md "../../../AmazonCloudWatch/latest/logs/CloudWatchLogsConcepts.md")
in the _Amazon CloudWatch Logs User Guide_.

You can view your logs in the Amazon CloudWatch console. Note that you must specify **US East (N. Virginia)** for the Region. For more information, see [View Log Data Sent to CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#ViewingLogData "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md#ViewingLogData") in the _Amazon CloudWatch Logs User Guide_.
