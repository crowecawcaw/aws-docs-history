

# Alarm warm-up periods
<a name="alarm-warm-up"></a>

A warm-up period delays alarm evaluation after you create or update an alarm. This reduces noise from missing data while a new resource or service starts to publish data. During warm-up, the alarm stays in `INSUFFICIENT_DATA` and does not perform alarm actions.

Use a warm-up period when you deploy alarms with a new application or service that takes time to emit metrics. Without a warm-up period, the alarm can transition and run actions on missing data during startup, and cause false notifications.

Warm-up periods work with metric alarms and log alarms.

## Warm-up period configuration
<a name="warm-up-configuration"></a>

Set the `WarmUpConfiguration` parameter when you create or update an alarm. This parameter includes the following settings:
+ `WarmUpPeriodDurationInMinutes` (required) – The warm-up duration, in minutes. Specify a value from 1 to 2,880 minutes (2 days).
+ `OnlyStartEvaluatingAfterWarmUpPeriodEnds` (optional, default is `false`) – Controls when evaluation begins. When set to `false` (default), the alarm ends warm-up early. Evaluation begins as soon as enough data fills its evaluation window. When set to `true`, the alarm waits the full warm-up duration before it evaluates, even if data arrives sooner. Use this setting when startup fluctuations, such as a CPU spike, could cause premature alarm transitions.

When `OnlyStartEvaluatingAfterWarmUpPeriodEnds` is `false`, the alarm ends warm-up as soon as it can fill its evaluation window. The evaluation window spans `Period` multiplied by `Evaluation Periods` and is full when a datapoint exists for the most recent period.

For example, an alarm with a 5-minute period and 3 evaluation periods has a 15-minute evaluation window. Suppose that you create this alarm at 10:00 and the resource starts to publish at 10:04. The alarm stays in `INSUFFICIENT_DATA` until a full 15-minute window is available. This happens at about 10:19, and then the alarm begins to evaluate. The `Datapoints to Alarm` setting does not affect when warm-up ends.

## Change or end a warm-up period
<a name="warm-up-change"></a>

You can change the warm-up configuration while the alarm is still in its warm-up period. You can also end warm-up early when you update the configuration. Warm-up applies only once at alarm creation and does not restart.

After the warm-up period ends, you can update the warm-up configuration. However, the update does not start a new warm-up period. The alarm continues to evaluate normally.

## View warm-up status
<a name="warm-up-view-status"></a>

During warm-up, the alarm state remains `INSUFFICIENT_DATA` and the evaluation state is `IN_WARM_UP`. View the alarm configuration and state with the [DescribeAlarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_DescribeAlarms.html) API. For more information about evaluation states, see [Alarm evaluation state](alarm-evaluation.md#alarm-evaluation-state).

For instructions on creating an alarm with a warm-up period, see [Create an alarm that uses a warm-up period](Create_WarmUp_Alarm.md).