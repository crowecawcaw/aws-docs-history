# Troubleshooting device fleet

disconnects

###### Help us improve this topic

[Let us know what would help make it better](../../../forms/aws-doc-feedback.md "../../../forms/aws-doc-feedback.md")

AWS IoT device fleet disconnects can happen for multiple reasons. This article explains
how to diagnose a disconnect reason and how to handle disconnects caused by regular
maintenance of AWS IoT service or a throttling limit.

**To diagnose the disconnect reason**

You can check the [AWSIotLogsV2](cloud-watch-logs.md "cloud-watch-logs.md") log group in
[CloudWatch](cwl-format.md "cwl-format.md")
to identify the disconnect reason in the `disconnectReason` field of the log
entry.

You can also use AWS IoT's [lifecycle events](life-cycle-events.md "life-cycle-events.md") feature
to identify the disconnect reason. If you’ve subscribed to [lifecycle's
disconnect event](life-cycle-events.md#connect-disconnect "life-cycle-events.md#connect-disconnect")
(`$aws/events/presence/disconnected/`clientId``),
 you’ll get a notification from AWS IoT when the disconnect happens. You can identify the
 disconnect reason in the `disconnectReason` field of the notification.

For more information, see [CloudWatch AWS IoT log entries](cwl-format.md "cwl-format.md") and
[Lifecycle events](life-cycle-events.md "life-cycle-events.md").

**To troubleshoot disconnects due to AWS IoT service
maintenance**

Disconnects caused by AWS IoT's service maintenance are logged as
`SERVER_INITIATED_DISCONNECT` in AWS IoT's lifecycle event and CloudWatch. To handle
these disconnects, adjust your client-side setup to make sure your devices can be
automatically reconnected to the AWS IoT platform.

**To troubleshoot disconnects due to a throttling
limit**

Disconnects caused by a throttling limit are logged as `THROTTLED` in AWS IoT's
lifecycle event and CloudWatch. To handle these disconnects, you can request [message
broker limit increases](../../../general/latest/gr/iot-core.md#message-broker-limits "../../../general/latest/gr/iot-core.md#message-broker-limits") as the device count grows.

For more information, see [AWS IoT Core Message
Broker](../../../general/latest/gr/iot-core.md#message-broker-limits "../../../general/latest/gr/iot-core.md#message-broker-limits").
