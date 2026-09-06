

# Create a metric alarm that uses a wall clock evaluation window
<a name="Create_WallClock_Alarm"></a>

You can create a metric alarm that aligns its evaluation window to wall clock boundaries instead of a sliding window. For information about how wall clock windows work and when to use them, see [Wall clock window](alarm-evaluation-window.md#wall-clock-window).

## Creating a wall clock alarm using the AWS Management Console
<a name="wall-clock-alarm-create-console"></a>

This example shows how to create an alarm that uses a 1-hour wall clock window.

**To create a wall clock alarm**

1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/).

1. In the navigation pane, choose **Alarms**, **All alarms**.

1. Choose **Create alarm**.

1. Choose **Select metric**, choose the metric you want to monitor, and then choose **Select metric**.

1. Under **Metric**, for **Period**, choose a period that supports wall clock windows: **1 minute**, **5 minutes**, **1 hour**, **1 day**, or **1 week**.

1. Under **Conditions**, configure the threshold and comparison operator for your alarm.

1. For **Evaluation window**, choose **Wall clock window**.
**Note**  
If you don't see the **Evaluation window** option, the metric type or period you selected does not support wall clock windows. Wall clock windows are not available for high-resolution alarms, composite alarms, or PromQL alarms, and are only available for periods of 1 minute, 5 minutes, 1 hour, 1 day, or 1 week.

1. Optionally, choose a time zone for **Time zone**. The alarm aligns its evaluation window to clock boundaries in this time zone. If you don't choose a time zone, CloudWatch uses `UTC`. For details about how time zones affect wall clock boundaries, see [Time zones and daylight saving time](alarm-evaluation-window.md#wall-clock-timezone).

1. Configure notifications and actions as needed, then choose **Next**.

1. Add a name and description for your alarm, then choose **Next**.

1. Review the alarm configuration and choose **Create alarm**.

## Creating a wall clock alarm (AWS CLI)
<a name="wall-clock-alarm-create-cli"></a>

Use the [PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html) API action to create or update a metric alarm with an `EvaluationWindow`. Set `WallClockWindow` to align the alarm to wall clock boundaries, or set `SlidingWindow` to use the default sliding behavior. If you omit the `EvaluationWindow` parameter, the alarm uses a sliding window.

**Example Create an alarm that uses a 1-hour wall clock window**  
This alarm evaluates the most recently completed clock hour in `UTC`. To align to a different time zone, set `Timezone` on the `WallClockWindow`.  

```
aws cloudwatch put-metric-alarm \
  --alarm-name HourlyCpuAlarm \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 3600 \
  --evaluation-periods 1 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --evaluation-window '{"WallClockWindow":{}}'
```

**Example Create a daily alarm aligned to a specific time zone**  
This alarm evaluates each calendar day in the `America/New_York` time zone. Daylight saving time transitions are handled automatically.  

```
aws cloudwatch put-metric-alarm \
  --alarm-name DailyBackupCheck \
  --metric-name SuccessfulBackups \
  --namespace MyApplication \
  --statistic Sum \
  --period 86400 \
  --evaluation-periods 1 \
  --threshold 1 \
  --comparison-operator LessThanThreshold \
  --evaluation-window '{"WallClockWindow":{"Timezone":"America/New_York"}}'
```

**Example Create a weekly alarm in UTC**  
This alarm evaluates each calendar week (Monday 00:00 UTC through the following Monday 00:00 UTC).  

```
aws cloudwatch put-metric-alarm \
  --alarm-name WeeklyComplianceCheck \
  --metric-name ComplianceFailures \
  --namespace MyApplication \
  --statistic Sum \
  --period 604800 \
  --evaluation-periods 1 \
  --threshold 0 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-window '{"WallClockWindow":{}}'
```

**Example Switch an existing alarm back to a sliding window**  
Set `EvaluationWindow` to `SlidingWindow` to make the change explicit. You can also omit the parameter, which has the same effect.  

```
aws cloudwatch put-metric-alarm \
  --alarm-name HourlyCpuAlarm \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 3600 \
  --evaluation-periods 1 \
  --threshold 80 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --evaluation-window '{"SlidingWindow":{}}'
```

## View the evaluation window for an existing alarm
<a name="wall-clock-alarm-view"></a>

Use the [DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) API action to retrieve the evaluation window configuration of an alarm. The `EvaluationWindow` field is included in the response when the alarm uses a wall clock window. If the field is absent, the alarm uses a sliding window.

```
aws cloudwatch describe-alarms \
  --alarm-names HourlyCpuAlarm
```

You can also view the evaluation window in the AWS Management Console on the alarm details page.