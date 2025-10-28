# Use Amazon SNS as an alert

receiver

You can use an existing Amazon SNS topic as an alert receiver for Amazon Managed Service for Prometheus, or you can
create a new one. We recommend that you use a topic of the
**Standard** type, so that you can forward alerts from the
topic to email, SMS, or HTTP.

To create a new Amazon SNS topic to use as your alert manager receiver, follow the
steps in [Step 1: Create a
topic](../../../sns/latest/dg/sns-getting-started.md#step-create-queue "../../../sns/latest/dg/sns-getting-started.md#step-create-queue"). Be sure to choose **Standard** for the topic
type.

If you want to receive emails every time a message is sent to that Amazon SNS topic,
follow the steps in [Step 2: Create a
subscription to the topic](../../../sns/latest/dg/sns-getting-started.md#step-send-message "../../../sns/latest/dg/sns-getting-started.md#step-send-message").

Whether you use a new or existing Amazon SNS topic, you will need the Amazon Resource
Name (ARN) of your Amazon SNS topic to complete the following tasks.

###### Topics

- [Giving Amazon Managed Service for Prometheus
  permission to send alert messages to your Amazon SNS topic](AMP-alertmanager-receiver-AMPpermission.md "AMP-alertmanager-receiver-AMPpermission.md")
- [Configure alert manager to
  send messages to your Amazon SNS topic](AMP-alertmanager-receiver-config.md "AMP-alertmanager-receiver-config.md")
- [Configure alert manager to send
  messages to Amazon SNS as JSON](AMP-alertmanager-receiver-JSON.md "AMP-alertmanager-receiver-JSON.md")
- [Configure Amazon SNS to send
  messages for alerts to other destinations](AMP-alertmanager-SNS-otherdestinations.md "AMP-alertmanager-SNS-otherdestinations.md")
- [Understanding
  Amazon SNS message validation rules](AMP-alertmanager-receiver-validation-truncation.md "AMP-alertmanager-receiver-validation-truncation.md")
