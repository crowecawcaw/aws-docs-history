# Create alarms on log anomaly

detectors

You can create an alarm for a log anomaly detector in a log group. You can specify for
the alarm to go into `ALARM` state when a specified number of anomalies are
found in the log group during a specified period of time. You can also use filters so
that only anomalies of specified priorities are counted by the alarm.

###### To create an alarm for a log anomaly detector

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Logs**, **Log
   Anomalies**.

The table of log anomaly detectors appears. 3. Choose the radio button for the anomaly detector that you want to set the
alarm for, and choose **Create alarm**.

The CloudWatch alarm creation wizard appears. The
**LogAnomalyDetector** field displays the name of the
anomaly detector that you chose. The **Metric name** field
displays **AnomalyCount**. 4. (Optional) To filter this alarm for anomaly priority, do one of the
following:

    * To have the alarm count only high-priority anomalies, enter
     `HIGH` for
     **LogAnomalyPriority**.
    * To have the alarm count only high- and medium-priority anomalies,
     enter `MEDIUM` for
     **LogAnomalyPriority**.For more information about priority levels, see [Severity and priority of

anomalies and patterns](LogsAnomalyDetection.md#LogsAnomalyDetection-Severity-Priority "LogsAnomalyDetection.md#LogsAnomalyDetection-Severity-Priority"). 5. Choose to use a static or metric anomaly detection threshold for the alarm.
This selection determines how the alarm threshold is set. A
**Static** threshold means that the alarm threshold is a
static, constant number that you choose. An **Anomaly
detection** threshold means that CloudWatch determines a range of usual
values, and the alarm triggers if the actual count crosses the threshold of this
band. You don't have to choose **Anomaly detection** for a log
anomaly detection alarm. For more information about metric anomaly detection,
see [Using CloudWatch anomaly detection](../monitoring/CloudWatch_Anomaly_Detection.md "../monitoring/CloudWatch_Anomaly_Detection.md"). 6. For **Whenever `your-metric-name` is . .
.**, choose **Greater**,
**Greater/Equal**, **Lower/Equal**, or
**Lower**. Then for **than . . .**,
specify a number for your threshold value. The alarm goes into
`ALARM` state if the anomaly detector finds more than this number
of alarms during a time specified by **Period**. 7. Choose **Additional configuration**. For **Datapoints
to alarm**, specify how many evaluation periods (data points) must
be in the `ALARM` state to trigger the alarm. If the two values here
match, you create an alarm that goes to `ALARM` state if that many
consecutive periods are breaching.

To create an M out of N alarm, specify a number for the first value that is
lower than the number for the second value. For more information, see [Evaluating an alarm](../monitoring/AlarmThatSendsEmail.md#alarm-evaluation "../monitoring/AlarmThatSendsEmail.md#alarm-evaluation"). 8. For **Missing data treatment**, choose how the alarm behaves
when some data points are missing. For more information, see [Configuring how CloudWatch alarms treat missing data](../monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data "../monitoring/AlarmThatSendsEmail.md#alarms-and-missing-data"). 9. Choose **Next**. 10. For **Notification**, choose **Add
notification**, and then specify an Amazon SNS topic to notify when your
alarm transitions to the `ALARM`, `OK`, or
`INSUFFICIENT_DATA` state.

    1. (Optional) To send multiple notifications for the same alarm state or
     for different alarm states, choose **Add
     notification**.


    ###### Note

    We recommend that you set the alarm to take actions when it goes
     into **Insufficient data** state in addition to
     when it goes into **Alarm** state. This is because
     many issues with the Lambda function that connects to the data source
     can cause the alarm to transition to **Insufficient
     data**.
    2. (Optional) To not send Amazon SNS notifications, choose **Remove**.

11. (Optional) If you want your alarm to perform actions for Amazon EC2 Auto Scaling, Amazon EC2,
    tickets, or AWS Systems Manager, choose the appropriate button, and specify the alarm
    state and action.

###### Note

Your alarm can perform Systems Manager actions only when it's in the
`ALARM` state. For information about Systems Manager actions, see
[Configuring CloudWatch to create OpsItems](../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md "../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md") and [Incident
creation](../../../incident-manager/latest/userguide/incident-creation.md "../../../incident-manager/latest/userguide/incident-creation.md"). 12. Choose **Next**. 13. Under **Name and description**, enter a name and description
for your alarm, and choose **Next**. The name must contain only
UTF-8 characters, and can't contain ASCII control characters. The description
can include markdown formatting, which is displayed only in the alarm
**Details** tab in the CloudWatch console. The markdown can be
useful to add links to runbooks or other internal resources.

###### Tip

The alarm name must contain only UTF-8 characters. It can't contain ASCII
control characters. 14. Under **Preview and create**, confirm that your alarm's
information and conditions are correct, and choose **Create
alarm**.
