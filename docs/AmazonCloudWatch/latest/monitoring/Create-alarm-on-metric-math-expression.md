# Create a CloudWatch alarm based on a
 metric math expression

Metric alarms are designed to evaluate time series that you define from either a single
 metric, or a metric math expression that combines or transforms one or more metrics into a
 time series that deliver insights more closely aligned to your unique needs. To create an
 alarm based on a metric math expression, choose one or more CloudWatch metrics to use in the
 expression. Then, specify the expression, threshold, and evaluation periods.

You can't create an alarm based on the **SEARCH** expression. Only
 alarms based on Metrics Insights SQL queries can operate on multiple time series.

###### To create an alarm that's based on a metric math expression

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Alarms**, and then choose
 **All alarms**.
3. Choose **Create alarm**.
4. Choose **Select Metric**, and then perform one of the following
 actions:


	* Select a namespace from the **AWS namespaces** dropdown or
	 **Custom namespaces** dropdown. After you select a namespace, you
	 continue choosing options until a list of metrics appears, where you select the
	 checkbox next to the correct metric.
	* Use the search box to find a metric, account ID, dimension, or resource ID.
	 After you enter the metric, dimension, or resource ID, you continue choosing options
	 until a list of metrics appears, where you select the check box next to the correct
	 metric.
5. (Optional) If you want to add another metric to a metric math expression, you can
 use the search box to find a specific metric. You can add as many as 10 metrics to a
 metric math expression.
6. Select the **Graphed metrics** tab. For each of the metrics that
 you previously added, perform the following actions:


	1. Under the **Statistic** column, select the dropdown menu. In
	 the dropdown menu, choose one of the predefined statistics or percentiles. Use the
	 search box in the dropdown menu to specify a custom
	 percentile.
	2. Under the **Period** column, select the dropdown menu. In the
	 dropdown menu, choose one of the predefined evaluation periods.
	
	
	While you're creating your alarm, you can specify whether the Y-axis legend
	 appears on the left or right side of your graph.###### Note

When CloudWatch evaluates alarms, periods are aggregated into single data points.
7. Choose the **Add math** dropdown, and then select **Start
 with an empty expression** from the list of predefined metric math
 expressions.


After you choose **Start with an empty expression**, a math
 expression box appears where you apply or edit math expressions.
8. In the math expression box, enter your math expression, and then choose
 **Apply**.


After you choose **Apply**, an **ID** column
 appears next to the **Label** column.


To use a metric or the result of another metric math expression as part of your
 current math expression's formula, you use the value that's shown under the
 **ID** column.
 To change the value of **ID**, you select the pen-and-paper icon next
 to the current value. The new value must begin with a lowercase letter and can include
 numbers, letters, and the underscore symbol. Changing the value of
 **ID** to a more significant name can make your alarm graph easier to
 understand.


For information about the functions that are available for metric math, see [Metric math syntax and functions](using-metric-math.md#metric-math-syntax "using-metric-math.md#metric-math-syntax").
9. (Optional) Add more math expressions, using both metrics and the results of other
 math expressions in the formulas of the new math expressions.
10. When you have the expression to use for the alarm, clear the check boxes to the left
 of every other expression and every metric on the page. Only the check box next to the
 expression to use for the alarm should be selected. The expression that you choose for
 the alarm must produce a single time series and show only one line on the graph. Then
 choose **Select metric**.


The **Specify metric and conditions** page appears, showing a graph
 and other information about the math expression that you have selected.
11. For **Whenever `expression` is**, specify
 whether the expression must be greater than, less than, or equal to the threshold. Under
 **than...**, specify the threshold value.
12. Choose **Additional configuration**. For **Datapoints to
 alarm**, specify how many evaluation periods (data points) must be in the
 `ALARM` state to trigger the alarm. If the two values here match, you
 create an alarm that goes to `ALARM` state if that many consecutive periods
 are breaching.


To create an M out of N alarm, specify a lower number for the first value than you
 specify for the second value. For more information, see [Evaluating an alarm](AlarmThatSendsEmail.md#alarm-evaluation "AlarmThatSendsEmail.md#alarm-evaluation").
13. For **Missing data treatment**, choose how to have the alarm behave
 when some data points are missing. For more information, see [Configuring how CloudWatch alarms treat missing
 data](AlarmThatSendsEmail.md#alarms-and-missing-data "AlarmThatSendsEmail.md#alarms-and-missing-data").
14. Choose **Next**.
15. Under **Notification**, select an SNS topic to notify when the
 alarm is in `ALARM` state, `OK` state, or
 `INSUFFICIENT_DATA` state.


To have the alarm send multiple notifications for the same alarm state or for
 different alarm states, choose **Add notification**.


To have the alarm not send notifications, choose **Remove**.
16. To have the alarm perform Auto Scaling, Amazon EC2, Lambda, or Systems Manager actions, choose the
 appropriate button and choose the alarm state and action to perform. If you choose a
 Lambda function as an alarm action, you specify the function name or ARN, and you can
 optionally choose a specific version of the function.


Alarms can perform Systems Manager actions only when they go into ALARM state. For more
 information about Systems Manager actions, see see  [Configuring CloudWatch to create OpsItems from alarms](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html "https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-create-OpsItems-from-CloudWatch-Alarms.html") and [Incident creation](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html "https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-creation.html").


###### Note

To create an alarm that performs an SSM Incident Manager action, you must have
 certain permissions. For more information, see [Identity-based policy examples for AWS Systems Manager Incident
 Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_id-based-policy-examples.html "https://docs.aws.amazon.com/incident-manager/latest/userguide/security_iam_id-based-policy-examples.html").
17. When finished, choose **Next**.
18. Enter a name and description for the alarm. Then choose
 **Next**.


The name must contain only UTF-8 characters, and can't contain ASCII control
 characters. The description can include markdown formatting, which is displayed only in
 the alarm **Details** tab in the CloudWatch console. The markdown can be
 useful to add links to runbooks or other internal resources.
19. Under **Preview and create**, confirm that the information and
 conditions are what you want, then choose **Create alarm**.
You can also add alarms to a dashboard. For more information, see [Adding an alarm to a CloudWatch dashboard](add_alarm_dashboard.md "add_alarm_dashboard.md").
