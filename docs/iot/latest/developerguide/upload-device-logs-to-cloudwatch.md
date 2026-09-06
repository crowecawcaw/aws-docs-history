

# Upload device-side logs to Amazon CloudWatch
<a name="upload-device-logs-to-cloudwatch"></a>

You can upload historical, device-side logs into Amazon CloudWatch to monitor and analyze a device's activity in the field. Device-side logs can include system, application, and device logs files. This process uses a CloudWatch Logs rules action parameter to publish device-side logs into a customer-defined [log group](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html). 

## How it works
<a name="upload-process-overview"></a>

The process begins when an AWS IoT device sends MQTT messages containing formatted log files to an AWS IoT topic. An AWS IoT rule monitors the message topic and sends the log files to a CloudWatch Logs group that you define. You can then review and analyze the information.

**Topics**
+ [MQTT topics](#upload-mqtt-topics-overview)
+ [Rule action](#upload-rule-action-overview)

### MQTT topics
<a name="upload-mqtt-topics-overview"></a>

Choose an MQTT topic name space that you will use to publish the logs. We recommend using this format for the common topic space, `$aws/rules/things/thing_name/logs`, and this format for error topics, `$aws/rules/things/thing_name/logs/errors`. The naming structure for logs and error topics is recommended, but not required. For more information, see [Designing MQTT Topics for AWS IoT Core](https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/designing-mqtt-topics-aws-iot-core.html). 

By using the recommended common topic space, you utilize AWS IoT Basic Ingest reserved topics. AWS IoT Basic Ingest securely sends device data to the AWS services that are supported by AWS IoT rule actions. It removes the publish/subscribe message broker from the ingestion path, making it more cost effective. For more information, see [Reducing messaging costs with Basic Ingest](https://docs.aws.amazon.com/iot/latest/developerguide/iot-basic-ingest.html). 

If you use batchMode to upload log files, your messages must follow a specific format that includes a UNIX timestamp and message. For more information, see the [MQTT message format requirements for batchMode](https://docs.aws.amazon.com/iot/latest/developerguide/cloudwatch-logs-rule-action.html#cloudwatch-logs-rule-action-message-format) topic within [CloudWatch Logs rule action](https://docs.aws.amazon.com/iot/latest/developerguide/cloudwatch-logs-rule-action.html). 

### Rule action
<a name="upload-rule-action-overview"></a>

When AWS IoT receives the MQTT messages from the client devices, an AWS IoT rule monitors the customer-defined topic and publishes the contents into a CloudWatch log group that you define. This process uses a CloudWatch Logs rule action to monitor MQTT for batches of log files. For more information, see the [CloudWatch Logs](https://docs.aws.amazon.com/iot/latest/developerguide/cloudwatch-logs-rule-action.html) AWS IoT rule action.

#### Batch mode
<a name="upload-batch-mode-overview"></a>

 `batchMode` is a Boolean parameter within the AWS IoT CloudWatch Logs rule action. This parameter is optional and is off (`false`) by default. To upload device-side log files in batches, you must turn this parameter on (`true`) when you create the AWS IoT rule. For more information, see [CloudWatch Logs](https://docs.aws.amazon.com/iot/latest/developerguide/cloudwatch-logs-rule-action.html) in the [AWS IoT rule actions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html) section.