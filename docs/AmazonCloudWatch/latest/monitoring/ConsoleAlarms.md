# Create a CloudWatch alarm based on a static threshold

You choose a CloudWatch metric for the alarm to watch, and the threshold for that metric. The
alarm goes to `ALARM` state when the metric breaches the threshold for a specified
number of evaluation periods.

If you are creating an alarm in an account set up as a monitoring account in CloudWatch
cross-account observability, you can set up the alarm to watch a metric in a source account
linked to this monitoring account. For more information, see [CloudWatch cross-account observability](CloudWatch-Unified-Cross-Account.md "CloudWatch-Unified-Cross-Account.md").

###### To create an alarm based on a single metric

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, **All
   alarms**.
3. Choose **Create alarm**.
4. Choose **Select Metric**.
5. Do one of the following:
   - Choose the service namespace that contains the metric that you want. Continue
     choosing options as they appear to narrow the choices. When a list of metrics appears,
     select the check box next to the metric that you want.
   - In the search box, enter the name of a metric, account ID, account label,
     dimension, or resource ID. Then, choose one of the results and continue until a list
     of metrics appears. Select the check box next to the metric that you want.

6. Choose the **Graphed metrics** tab.
   1. Under **Statistic** , choose one of the statistics or predefined
      percentiles, or specify a custom percentile (for example,
      `p95.45`).
   2. Under **Period**, choose the evaluation period for the alarm.
      When evaluating the alarm, each period is aggregated into one data point.

   You can also choose whether the y-axis legend appears on the left or right while
   you're creating the alarm. This preference is used only while you're creating the
   alarm. 3. Choose **Select metric**.

   The **Specify metric and conditions** page appears, showing a
   graph and other information about the metric and statistic that you selected.

7. Under **Conditions**, specify the following:
   1. For **Whenever `metric` is**, specify
      whether the metric must be greater than, less than, or equal to the threshold. Under
      **than...**, specify the threshold value.
   2. Choose **Additional configuration**. For **Datapoints to
      alarm**, specify how many evaluation periods (data points) must be in the
      `ALARM` state to trigger the alarm. If the two values here match, you
      create an alarm that goes to `ALARM` state if that many consecutive periods
      are breaching.

   To create an M out of N alarm, specify a lower number for the first value than you
   specify for the second value. For more information, see [Alarm evaluation](alarm-evaluation.md "alarm-evaluation.md"). 3. For **Missing data treatment**, choose how to have the alarm
   behave when some data points are missing. For more information, see [Configuring how CloudWatch alarms treat missing data](alarms-and-missing-data.md "alarms-and-missing-data.md"). 4. If the alarm uses a percentile as the monitored statistic, a **Percentiles
   with low samples** box appears. Use it to choose whether to evaluate or
   ignore cases with low sample rates. If you choose **ignore (maintain alarm
   state)**, the current alarm state is always maintained when the sample size
   is too low. For more information, see [Percentile-based alarms and low data samples](percentiles-with-low-samples.md "percentiles-with-low-samples.md").

8. Choose **Next**.
9. Under **Notification**, select an SNS topic to notify when the alarm
   is in `ALARM` state, `OK` state, or `INSUFFICIENT_DATA`
   state.

To have the alarm send multiple notifications for the same alarm state or for
different alarm states, choose **Add notification**.

In CloudWatch cross-account observability, you can choose to have notifications sent to
multiple AWS accounts. For example, to both the monitoring account and the source
account.

To have the alarm not send notifications, choose **Remove**. 10. To have the alarm perform Auto Scaling, EC2, Lambda, investigation, or Systems Manager actions,
choose the appropriate button and choose the alarm state and action to perform. Alarms can
perform Systems Manager actions and investigation actions only when they go into ALARM state. For
more information about Systems Manager actions, see [Configuring CloudWatch to create OpsItems from alarms](../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md "../../../systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.md") and [Incident creation](../../../incident-manager/latest/userguide/incident-creation.md "../../../incident-manager/latest/userguide/incident-creation.md").

To have the alarm start an investigation, choose **Add investigation
action** and then select your investigation group. For more information about
, see [CloudWatch investigations](Investigations.md "Investigations.md").

###### Note

To create an alarm that performs an SSM Incident Manager action, you must have
certain permissions. For more information, see [Identity-based policy examples for AWS Systems Manager Incident
Manager](../../../incident-manager/latest/userguide/security_iam_id-based-policy-examples.md "../../../incident-manager/latest/userguide/security_iam_id-based-policy-examples.md"). 11. When finished, choose **Next**. 12. Enter a name and description for the alarm. The name must contain only UTF-8
characters, and can't contain ASCII control characters. The description can include
markdown formatting, which is displayed only in the alarm **Details** tab
in the CloudWatch console. The markdown can be useful to add links to runbooks or other internal
resources. Then choose **Next**. 13. Under **Preview and create**, confirm that the information and
conditions are what you want, then choose **Create alarm**.
You can also add alarms to a dashboard. For more information, see [Adding an alarm to a CloudWatch dashboard](add_alarm_dashboard.md "add_alarm_dashboard.md").
