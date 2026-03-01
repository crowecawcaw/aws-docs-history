# Create an alarm on Performance Insights counter metrics from an AWS database

CloudWatch includes a **DB_PERF_INSIGHTS** metric math function which you can
use to bring Performance Insights counter metrics into CloudWatch from Amazon Relational Database Service and Amazon DocumentDB (with MongoDB compatibility).
**DB_PERF_INSIGHTS** also brings in the `DBLoad` metric at
sub-minute intervals. You can set CloudWatch alarms on these metrics.

For more information about Amazon RDS Performance Insights, see [Monitoring DB load with
Performance Insights on Amazon RDS](../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md "../../../AmazonRDS/latest/UserGuide/USER_PerfInsights.md").

For more information about Amazon DocumentDB Performance Insights, see [Monitoring with
Performance Insights](../../../documentdb/latest/developerguide/performance-insights.md "../../../documentdb/latest/developerguide/performance-insights.md").

Outlier detection is not supported for alarms based on the
**DB_PERF_INSIGHTS** function.

###### Note

High-resolution metrics with sub-minute granularity retrieved by
**DB_PERF_INSIGHTS** are only applicable to the
**DBLoad** metric, or for operating system metrics if you have enabled
Enhanced Monitoring at a higher resolution. For more information about Amazon RDS enhanced
monitoring, see [Monitoring OS metrics with
Enhanced Monitoring.](../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md "../../../AmazonRDS/latest/UserGuide/USER_Monitoring.md").

You can create a high-resolution alarm using the **DB_PERF_INSIGHTS**
function. The maximum evaluation range for a high-resolution alarm is three hours. You can
use the CloudWatch console to graph metrics retrieved with the
**DB_PERF_INSIGHTS** function for any time range.

###### To create an alarm that's based on Performance Insights metrics

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, and then choose
   **All alarms**.
3. Choose **Create alarm**.
4. Choose **Select Metric**.
5. Choose the **Add math** dropdown, and then select **All
   functions**, **DB_PERF_INSIGHTS** from the list.

After you choose **DB_PERF_INSIGHTS**, a math expression box
appears where you apply or edit math expressions. 6. In the math expression box, enter your **DB_PERF_INSIGHTS** math
expression, and then choose **Apply**.

For example, `DB_PERF_INSIGHTS(‘RDS’, ‘db-ABCDEFGHIJKLMNOPQRSTUVWXY1’,
 ‘os.cpuUtilization.user.avg’)`

###### Important

When you use the **DB_PERF_INSIGHTS** math expression, you must
specify the Unique Database Resource ID of the database. This is different than the
database identifier. To find the database resource ID in the Amazon RDS console, choose the
DB instance to see its details. Then choose the **Configuration**
tab. The **Resource ID** is displayed in the
**Configuration** section.

For information about the **DB_PERF_INSIGHTS** function and other
functions that are available for metric math, see [Metric math syntax and functions](using-metric-math.md#metric-math-syntax "using-metric-math.md#metric-math-syntax"). 7. Choose **Select metric**.

The **Specify metric and conditions** page appears, showing a graph
and other information about the math expression that you have selected. 8. For **Whenever `expression` is**, specify
whether the expression must be greater than, less than, or equal to the threshold. Under
**than...**, specify the threshold value. 9. Choose **Additional configuration**. For **Datapoints to
alarm**, specify how many evaluation periods (data points) must be in the
`ALARM` state to trigger the alarm. If the two values here match, you
create an alarm that goes to `ALARM` state if that many consecutive periods
are breaching.

To create an M out of N alarm, specify a lower number for the first value than you
specify for the second value. For more information, see [Alarm evaluation](alarm-evaluation.md "alarm-evaluation.md"). 10. For **Missing data treatment**, choose how to have the alarm behave
when some data points are missing. For more information, see [Configuring how CloudWatch alarms treat missing data](alarms-and-missing-data.md "alarms-and-missing-data.md"). 11. Choose **Next**. 12. Under **Notification**, select an SNS topic to notify when the
alarm is in `ALARM` state, `OK` state, or
`INSUFFICIENT_DATA` state.

To have the alarm send multiple notifications for the same alarm state or for
different alarm states, choose **Add notification**.

To have the alarm not send notifications, choose **Remove**. 13. To have the alarm perform Auto Scaling, EC2, Lambda, or Systems Manager actions, choose the
appropriate button and choose the alarm state and action to perform. If you choose a
Lambda function as an alarm action, you specify the function name or ARN, and you can
optionally choose a specific version of the function.

Alarms can perform Systems Manager actions only when they go into ALARM state. For more
information about Systems Manager actions, see see [Configuring CloudWatch to create OpsItems from alarms](../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md "../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md") and [Incident creation](../../../incident-manager/latest/userguide/incident-creation.md "../../../incident-manager/latest/userguide/incident-creation.md").

###### Note

To create an alarm that performs an SSM Incident Manager action, you must have
certain permissions. For more information, see [Identity-based policy examples for AWS Systems Manager Incident
Manager](../../../incident-manager/latest/userguide/security_iam_id-based-policy-examples.md "../../../incident-manager/latest/userguide/security_iam_id-based-policy-examples.md"). 14. When finished, choose **Next**. 15. Enter a name and description for the alarm. Then choose
**Next**.

The name must contain only UTF-8 characters, and can't contain ASCII control
characters. The description can include markdown formatting, which is displayed only in
the alarm **Details** tab in the CloudWatch console. The markdown can be
useful to add links to runbooks or other internal resources. 16. Under **Preview and create**, confirm that the information and
conditions are what you want, then choose **Create alarm**.
