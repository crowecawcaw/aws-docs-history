# Upload device-side logs to Amazon CloudWatch

You can upload historical, device-side logs into Amazon CloudWatch to monitor and analyze a
device's activity in the field. Device-side logs can include system, application, and device
logs files. This process uses a CloudWatch Logs rules action parameter to publish device-side logs into
a customer-defined [log
group](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md").

## How it works

The process begins when an AWS IoT device sends MQTT messages containing formatted log
files to an AWS IoT topic. An AWS IoT rule monitors the message topic and sends the log files to
a CloudWatch Logs group that you define. You can then review and analyze the information.

###### Topics

- [MQTT topics](#upload-mqtt-topics-overview "#upload-mqtt-topics-overview")
- [Rule action](#upload-rule-action-overview "#upload-rule-action-overview")

### MQTT topics

Choose an MQTT topic name space that you will use to publish the logs. We recommend
using this format for the common topic space,
`$aws/rules/things/*thing\_name*/logs`, and this format
for error topics,
`$aws/rules/things/*thing\_name*/logs/errors`. The naming
structure for logs and error topics is recommended, but not required. For more
information, see [Designing MQTT Topics for AWS IoT Core](../../../whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.md "../../../whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.md").

By using the recommended common topic space, you utilize AWS IoT Basic Ingest reserved
topics. AWS IoT Basic Ingest securely sends device data to the AWS services that are
supported by AWS IoT rule actions. It removes the publish/subscribe message broker from the
ingestion path, making it more cost effective. For more information, see [Reducing
messaging costs with Basic Ingest](iot-basic-ingest.md "iot-basic-ingest.md").

If you use batchMode to upload log files, your messages must follow a specific format
that includes a UNIX timestamp and message. For more information, see the [MQTT message format requirements for batchMode](cloudwatch-logs-rule-action.md#cloudwatch-logs-rule-action-message-format "cloudwatch-logs-rule-action.md#cloudwatch-logs-rule-action-message-format") topic within [CloudWatch Logs rule action](cloudwatch-logs-rule-action.md "cloudwatch-logs-rule-action.md").

### Rule action

When AWS IoT receives the MQTT messages from the client devices, an AWS IoT rule monitors
the customer-defined topic and publishes the contents into a CloudWatch log group that you
define. This process uses a CloudWatch Logs rule action to monitor MQTT for batches of log files.
For more information, see the [CloudWatch Logs](cloudwatch-logs-rule-action.md "cloudwatch-logs-rule-action.md") AWS IoT
rule action.

#### Batch mode

`batchMode` is a Boolean parameter within the AWS IoT CloudWatch Logs rule action.
This parameter is optional and is off (`false`) by default. To upload
device-side log files in batches, you must turn this parameter on (`true`)
when you create the AWS IoT rule. For more information, see [CloudWatch Logs](cloudwatch-logs-rule-action.md "cloudwatch-logs-rule-action.md") in the
[AWS IoT rule actions](iot-rule-actions.md "iot-rule-actions.md") section.
