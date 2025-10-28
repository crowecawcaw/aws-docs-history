# Create CloudWatch alarms for Amazon EC2

instances that fail status checks

You can use the [status check metrics](viewing_metrics_with_cloudwatch.md#status-check-metrics "viewing_metrics_with_cloudwatch.md#status-check-metrics")
to create CloudWatch alarms to notify you when an instance has a failed status
check.

Status checks and status check alarms can temporarily enter an
_insufficient data_ state if there are missing metric
data points. Although rare, this can happen when there is an interruption in the
metric reporting systems, even when an instance is healthy. We recommend that
you treat this state as missing data instead of a status check failure or alarm
breach. This is especially important when taking stop, terminate, reboot, or
recover actions on the instance in response.

Console
This example configures an alarm that sends a notification when an
instance fails a status check. You can optionally stop, terminate, or
recover the instance.

###### To create a status check alarm

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance, choose the **Status
   Checks** tab, and choose
   **Actions**, **Create status check
   alarm**.
4. On the **Manage CloudWatch alarms** page,
   under **Add or edit alarm**, choose
   **Create an alarm**.
5. For **Alarm notification**, turn the toggle
   on to configure Amazon Simple Notification Service (Amazon SNS) notifications. Select an
   existing Amazon SNS topic or enter a name to create a new
   topic.

If you add an email address to the list of recipients or
create a new topic, Amazon SNS sends a confirmation email to each new
address. Each recipient must choose the confirmation link in the
email. Only confirmed addresses receive alert
notifications. 6. For **Alarm action**, turn the toggle on to
specify an action to take when the alarm is triggered. Select
the action. 7. For **Alarm thresholds**, specify the metric
and criteria for the alarm.

You can leave the default settings for **Group samples
by** (**Average**) and
**Type of data to sample**
(**Status check failed:either**), or you
can change them to suit your needs.

For **Consecutive period**, set the number of
periods to evaluate and, in **Period**, enter
the evaluation period duration before triggering the alarm and
sending an email. 8. (Optional) For **Sample metric data**, choose
**Add to dashboard**. 9. Choose **Create**.

If you need to change an instance status alarm, you can edit
it.

###### To edit a status check alarm

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select the instance and choose **Actions**,
   **Monitoring**, **Manage CloudWatch
   alarms**.
4. On the **Manage CloudWatch alarms** page,
   under **Add or edit alarm**, choose
   **Edit an alarm**.
5. For **Search for alarm**, choose the
   alarm.
6. When you are finished making changes, choose
   **Update**.

AWS CLI
In the following example, the alarm publishes a notification to an SNS
topic when the instance fails either the instance check or system status check
for at least two consecutive periods. The CloudWatch metric used is
`StatusCheckFailed`.

###### To create a status check alarm

1. Select an existing SNS topic or create a new one. For more
   information, see [Accessing Amazon SNS in the AWS CLI](../../../cli/latest/userguide/cli-services-sns.md "../../../cli/latest/userguide/cli-services-sns.md") in the
   _AWS Command Line Interface User Guide_.
2. Use the following [list-metrics](../../../cli/latest/reference/cloudwatch/list-metrics.md "../../../cli/latest/reference/cloudwatch/list-metrics.md") command to view the available Amazon CloudWatch
   metrics for Amazon EC2.

```
aws cloudwatch list-metrics --namespace AWS/EC2
```

3. Use the following [put-metric-alarm](../../../cli/latest/reference/cloudwatch/put-metric-alarm.md "../../../cli/latest/reference/cloudwatch/put-metric-alarm.md") command to create the
   alarm.

```
aws cloudwatch put-metric-alarm \
    --alarm-name `StatusCheckFailed-Alarm-for-i-1234567890abcdef0` \
    --metric-name StatusCheckFailed \
    --namespace AWS/EC2 \
    --statistic Maximum \
    --dimensions Name=InstanceId,Value=`i-1234567890abcdef0` \
    --unit Count \
    --period 300 \
    --evaluation-periods 2 \
    --threshold 1 \
    --comparison-operator GreaterThanOrEqualToThreshold \
    --alarm-actions arn:aws:sns:`us-west-2`:`111122223333`:`my-sns-topic`
```

The period is the time frame, in seconds, in which Amazon CloudWatch
metrics are collected. This example uses 300, which is 60
seconds multiplied by 5 minutes. The evaluation period is the
number of consecutive periods for which the value of the metric
must be compared to the threshold. This example uses 2. The
alarm actions are the actions to perform when this alarm is
triggered.

PowerShell

###### To create a status check alarm

Use the [Write-CWMetricAlarm](../../../powershell/latest/reference/items/Write-CWMetricAlarm.md "../../../powershell/latest/reference/items/Write-CWMetricAlarm.md")
cmdlet as follows to publish notifications to an SNS topic when
the instance fails status checks for at least two consecutive
periods.

```
Write-CWMetricAlarm `
    -AlarmName "`StatusCheckFailed-Alarm-for-i-1234567890abcdef0`" `
    -MetricName "StatusCheckFailed" `
    -Namespace "AWS/EC2" `
    -Statistic "Maximum" `
    -Dimension @{Name="InstanceId"; Values="`i-1234567890abcdef0`"} `
    -Unit "Count" `
    -Period 300 `
    -EvaluationPeriod 2 `
    -Threshold 1 `
    -ComparisonOperator "GreaterThanOrEqualToThreshold" `
    -AlarmAction "arn:aws:sns:`us-west-2`:`111122223333`:`my-sns-topic`"
```

The period is the time frame, in seconds, in which Amazon CloudWatch
metrics are collected. This example uses 300, which is 60
seconds multiplied by 5 minutes. The evaluation period is the
number of consecutive periods for which the value of the metric
must be compared to the threshold. This example uses 2. The
alarm actions are the actions to perform when this alarm is
triggered.
