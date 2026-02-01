# Rules for AWS IoT

Rules give your devices the ability to interact with AWS services. Rules are analyzed
and actions are performed based on the MQTT topic stream. You can use rules to support the
following tasks:

- Augment or filter data received from a device.
- Write data received from a device to an Amazon DynamoDB database.
- Save a file to Amazon S3.
- Send a push notification to all users who are using Amazon SNS.
- Publish data to an Amazon SQS queue.
- Invoke a Lambda function to extract data.
- Process messages from a large number of devices using Amazon Kinesis.
- Send data to Amazon OpenSearch Service.
- Capture a CloudWatch metric.
- Change a CloudWatch alarm.
- Send the data from an MQTT message to Amazon SageMaker AI to make predictions based on a
  machine learning (ML) model.
- Send a message to a Salesforce IoT Input Stream.
- Start process of a Step Functions state machine.
- Send message data to an AWS IoT Events input.
- Send message data to an asset property in AWS IoT SiteWise.
- Send message data to a web application or service.
  Your rules can use MQTT messages that pass through the publish/subscribe protocol
  supported by the [Device communication protocols](protocols.md "protocols.md"). You can also use the [Basic Ingest](iot-basic-ingest.md "iot-basic-ingest.md") feature to securely send device data to
  the AWS services listed previously, without incurring [messaging costs](https://aws.amazon.com/iot-core/pricing/ "https://aws.amazon.com/iot-core/pricing/"). The [Basic Ingest](iot-basic-ingest.md "iot-basic-ingest.md") feature optimizes data flow by removing
  the publish/subscribe message broker from the ingestion path. This makes it cost effective
  while still keeping the security and data processing features of AWS IoT.

Before AWS IoT can perform these actions, you must grant it permission to access your AWS
resources on your behalf. When the actions are performed, you incur the standard charges for
the AWS services that you use.

###### Contents

- [Granting an AWS IoT rule the access it requires](iot-create-role.md "iot-create-role.md")
- [Passing role permissions](pass-role.md "pass-role.md")
- [Creating an AWS IoT rule](iot-create-rule.md "iot-create-rule.md")
- [Managing an AWS IoT rule](iot-managae-rule.md "iot-managae-rule.md")
- [AWS IoT rule actions](iot-rule-actions.md "iot-rule-actions.md")
- [Troubleshooting a rule](#iot-troubleshoot-rule "#iot-troubleshoot-rule")
- [Accessing cross-account
  resources using AWS IoT rules](accessing-cross-account-resources-using-rules.md "accessing-cross-account-resources-using-rules.md")
- [Error handling (error action)](rule-error-handling.md "rule-error-handling.md")
- [Reducing messaging costs with Basic Ingest](iot-basic-ingest.md "iot-basic-ingest.md")
- [AWS IoT SQL reference](iot-sql-reference.md "iot-sql-reference.md")

## Troubleshooting a rule

If you have an issue with your rules, we recommend that you activate CloudWatch Logs. You can
analyze your logs to determine whether the issue is authorization or whether, for
example, a WHERE clause condition didn't match. For more information, see [Setting
Up CloudWatch Logs](cloud-watch-logs.md "cloud-watch-logs.md").
