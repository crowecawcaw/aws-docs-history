# Monitor AWS IoT using CloudWatch Logs

When [AWS IoT logging is enabled](configure-logging.md "configure-logging.md"), AWS IoT sends
progress events about each message as it passes from your devices through the message broker
and rules engine. In the [CloudWatch console](https://console.aws.amazon.com/cloudwatch "https://console.aws.amazon.com/cloudwatch"),
CloudWatch logs appear in a log group named **AWSIotLogs**.

For more information about CloudWatch Logs, see [CloudWatch Logs](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatchLogs.md"). For information about supported AWS IoT CloudWatch Logs, see [CloudWatch Logs AWS IoT log entries](cwl-format.md "cwl-format.md").

## Viewing AWS IoT logs in the CloudWatch console

###### Note

The `AWSIotLogsV2` log group is not visible in the CloudWatch console
until:

- You've enabled logging in AWS IoT. For more info on how to enable logging in AWS IoT,
  see [Configure AWS IoT logging](configure-logging.md "configure-logging.md")
- Some log entries have been written by AWS IoT operations.

###### To view your AWS IoT logs in the CloudWatch console

1. Browse to [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"). In the navigation pane, choose **Log
   groups**.
2. In the **Filter** text box, enter
   `AWSIotLogsV2` , and then press Enter.
3. Double-click the `AWSIotLogsV2` log group.
4. Choose **Search All**. A complete list of the AWS IoT logs generated
   for your account is displayed.
5. Choose the expand icon to look at an individual stream.

You can also enter a query in the **Filter events** text box. Here are
some interesting queries to try:

- `{ $.logLevel = "INFO" }`

Find all logs that have a log level of `INFO`.

- `{ $.status = "Success" }`

Find all logs that have a status of `Success`.

- `{ $.status = "Success" && $.eventType = "GetThingShadow"
}`

Find all logs that have a status of `Success` and an event type of
`GetThingShadow`.

For more information about creating filter expressions, see [CloudWatch Logs Queries](../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md "../../../AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.md").
