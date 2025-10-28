# Enable anomaly detection on a log

group

Use the following steps to use the CloudWatch console to create a log anomaly detector that
scans a log group for anomalies.

You can also create anomaly detectors programmatically. For more information, see
[CreateLogAnomalyDetector](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogAnomalyDetector.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogAnomalyDetector.md").

###### To create a log anomaly detector

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. Choose **Logs**, **Log Anomalies**.
3. Choose **Create anomaly detector**.
4. Select the log group to create this anomaly detector for.
5. Enter a name for the detector in **Anomaly detector
   name**.
6. (Optional) Change the **Evaluation frequency** from the
   default of 5 minutes. Set this value according to the frequency that the log
   group receives new logs. For example, if the log group receives new log events
   in batches every 10 minutes, then setting the evaluation frequency to 15 minutes
   might be appropriate.
7. (Optional) To configure the anomaly detector to look for anomalies only in log
   events that contain certain words or strings, choose **Filter
   patterns**.

Then, enter a pattern in **Anomaly detection filter
pattern**. For more information about pattern syntax, [Filter pattern syntax for metric filters,
subscription filters, filter log events, and Live Tail](FilterAndPatternSyntax.md "FilterAndPatternSyntax.md").

(Optional) To test your filter pattern, enter some log messages into
**Log event messages** and then choose **Test
Pattern**. 8. (Optional) To change the anomaly visibility period from the default or to
associate an AWS KMS key with this anomaly detector, choose **Advanced
configuration**.

    1. To change the anomaly visibility period from the default, enter a new
     value in **Maximum anomaly visibility period
     (days)**.
    2. To associate an AWS KMS key with this anomaly detector, enter the ARN in
     **KMS key ARN**. If you assign a key, the anomaly
     information found by this detector is encrypted at rest with the key.
     Users must have permissions for this key and for the anomaly detector to
     retrieve information about the anomalies that it finds.


    You must also ensure that the CloudWatch Logs service principal has permission
     to use the key. For more information, see [Encrypt an anomaly detector and its results
     with AWS KMS](LogsAnomalyDetection-KMS.md "LogsAnomalyDetection-KMS.md").

9. Choose **Enable Anomaly Detection**.

The anomaly detector is created and starts training its model, based on the
log events the log group is ingesting. After about 15 minutes, anomaly detection
is active and begins to find and surface anomalies.
