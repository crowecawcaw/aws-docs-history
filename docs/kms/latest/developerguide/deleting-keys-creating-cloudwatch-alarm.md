# Create an alarm that detects use of a

KMS key pending deletion

You can combine the features of AWS CloudTrail, Amazon CloudWatch Logs, and Amazon Simple Notification Service (Amazon SNS) to create an
Amazon CloudWatch alarm that notifies you when someone in your account tries to use a KMS key that is
pending deletion. If you receive this notification, you might want to cancel deletion of the
KMS key and reconsider your decision to delete it.

The following procedures create an alarm that notifies you whenever the
"``Key ARN` is pending deletion`" error message is
 written to your CloudTrail log files. This error message indicates that a person or application tried
 to use the KMS key in a [cryptographic
 operation](kms-cryptography.md#cryptographic-operations "kms-cryptography.md#cryptographic-operations"). Because the notification is linked to the error message, it is not triggered
 when you use API operations that are permitted on KMS keys that are pending deletion, such as
 `ListKeys`, `CancelKeyDeletion`, and `PutKeyPolicy`. To see a
list of the AWS KMS API operations that return this error message, see [Key states of AWS KMS keys](key-state.md "key-state.md").

The notification email that you receive does not list the KMS key or the cryptographic
operation. You can find that information in [your CloudTrail
log](logging-using-cloudtrail.md "logging-using-cloudtrail.md"). Instead, the email reports that the alarm state changed from **OK** to **Alarm**. For more information about CloudWatch
alarms and state changes, see [Using Amazon CloudWatch
alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") in the _Amazon CloudWatch User Guide_.

###### Warning

This Amazon CloudWatch alarm cannot detect use of the public key of an asymmetric KMS key outside
of AWS KMS. For details about the special risks of deleting asymmetric KMS keys used for
public key cryptography, including creating ciphertexts that cannot be decrypted, see [Deleting asymmetric KMS keys](deleting-keys.md#deleting-asymmetric-cmks "deleting-keys.md#deleting-asymmetric-cmks").

In this procedure, you create a CloudWatch log group metric filter that finds instances of the
pending deletion exception. Then, you create a CloudWatch alarm based on the log group metric. For
information about log group metric filters, see [Creating metrics from log events using
filters](../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md "../../../AmazonCloudWatch/latest/logs/MonitoringLogData.md") in the Amazon CloudWatch Logs User Guide.

1. Create a CloudWatch metric filter that parses CloudTrail logs.

Follow the instructions in [Create a metric filter for a log group](../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md "../../../AmazonCloudWatch/latest/logs/CreateMetricFilterProcedure.md") using the following required values.
For other fields, accept the default values and provide names as requested.

| Field          | Value                                                                             |
| -------------- | --------------------------------------------------------------------------------- |
| Filter pattern | `{ $.eventSource = kms<br>• && $.errorMessage = "<br>• is pending<br>deletion."}` |
| Metric value   | 1                                                                                 |

2. Create a CloudWatch alarm based on the metric filter that you created in Step 1.

Follow the instructions in [Create a CloudWatch alarm
based on a log group-metric filter](../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md "../../../AmazonCloudWatch/latest/monitoring/Alarm-On-Logs.md") using the following required values.
For other fields, accept the default values and provide names as requested.

| Field                  | Value                                                               |
| ---------------------- | ------------------------------------------------------------------- |
| Metric filter          | The name of the metric filter that you created in Step 1.           |
| Threshold type         | Static                                                              |
| Conditions             | **Whenever**<br>`metric-name` is \*_Greater/Equal_<br>• than<br>`1` |
| Data points to alarm   | `1` out of `1`                                                      |
| Missing data treatment | **Treat missing data as good (not breaching<br>threshold)**         |

After you complete this procedure, you will receive a notification each time your new CloudWatch
alarm enters the `ALARM` state. If you receive a notification for this alarm, it
might mean that a KMS key that is scheduled for deletion is still needed to encrypt or decrypt
data. In that case, [cancel deletion of the
KMS key](deleting-keys-scheduling-key-deletion.md "deleting-keys-scheduling-key-deletion.md") and reconsider your decision to delete it.
