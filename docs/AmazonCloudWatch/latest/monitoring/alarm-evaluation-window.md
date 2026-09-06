

# Alarm evaluation window
<a name="alarm-evaluation-window"></a>

When CloudWatch evaluates a metric alarm, it retrieves metric data for a time range called the *evaluation window*. The length of the window is `Period` multiplied by `Evaluation Periods`. Where the boundaries of that window fall is controlled by the `EvaluationWindow` parameter on the [PutMetricAlarm](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_PutMetricAlarm.html) API. `EvaluationWindow` accepts one of two configurations:
+ `SlidingWindow` – the default. The window advances each time the alarm is evaluated, forming a rolling time window.
+ `WallClockWindow` – the window is aligned to clock boundaries that match the period (such as the top of the hour, midnight, or the start of the calendar week) and, optionally, to a specific time zone.

If you don't specify `EvaluationWindow` when you create or update a metric alarm, the alarm uses a sliding window. You can switch an existing alarm to a wall clock window at any time by updating the alarm.

Both configurations are supported on all types of metric alarms except alarms that are based on a PromQL query.

## Choosing between a sliding window and a wall clock window
<a name="choosing-evaluation-window"></a>

A sliding window continuously incorporates the most recent data, so it detects breaches as soon as data points cross your threshold. Choose a sliding window for real-time monitoring where calendar alignment doesn't matter, such as performance, latency, or resource-exhaustion workloads.

A wall clock window evaluates complete, calendar-aligned periods such as each hour, day, or week. Choose a wall clock window when monitoring is tied to a business or calendar period. It also avoids false alarms that can occur when events span rolling window boundaries. For example, a daily backup alarm with a sliding window can enter `ALARM` if consecutive backups are more than 24 hours apart, even though each calendar day had a backup. A wall clock window evaluates each day independently and avoids this.

The trade-off is detection timing. A wall clock window reflects a data point only after the period that contains it ends. If you need to detect a problem while it is still in progress, use a sliding window.

## Sliding window
<a name="sliding-window"></a>

With a sliding window, the evaluation window moves forward each time the alarm is evaluated, forming a rolling time window. For example, an alarm with a 1-hour period and 1 evaluation period might evaluate the time range 13:07–14:07 on one evaluation and 13:08–14:08 on the next.

Because the window always incorporates the most recent data points, a sliding window is the better choice for alarms that trigger Auto Scaling actions.

A sliding window has no additional configuration options. To configure one explicitly through the API, set `EvaluationWindow` to `{"SlidingWindow":{}}`. Omitting `EvaluationWindow` has the same effect.

## Wall clock window
<a name="wall-clock-window"></a>

Evaluation periods align to fixed time boundaries (for example, each hour or day) in your selected time zone. Best for scheduled workloads like daily reports, batch jobs, or backups.

Boundaries align to the start of the matching calendar period in the selected time zone: the top of the hour for a 1-hour period, midnight for a 1-day period, and Monday at 00:00 (the start of the ISO 8601 week) for a 1-week period. These alignment points are fixed and can't be changed.

### When to use a wall clock window
<a name="wall-clock-when-to-use"></a>

Choose a wall clock window when you want alarm evaluations to align with time-of-day or calendar boundaries. Common scenarios include:
+ Daily batch jobs that should complete by midnight in a specific time zone.
+ Weekly compliance or business reports that summarize a calendar week.

**Note**  
We don't recommend using a wall clock window for alarms that trigger Auto Scaling actions. The alarm reflects new data only after the current period ends, so it can't track load closely enough for responsive scaling. Use a sliding window instead.

### Supported periods
<a name="wall-clock-supported-periods"></a>

You can use a wall clock window with metric alarms that have one of the following periods:
+ 1 minute (60 seconds)
+ 5 minutes (300 seconds)
+ 1 hour (3600 seconds)
+ 1 day (86400 seconds)
+ 1 week (604800 seconds)

Wall clock windows are not supported for high-resolution alarms (periods of 10, 20, or 30 seconds).

If you specify a period that wall clock windows don't support, `PutMetricAlarm` returns a validation error that lists the supported periods.

For metric math and Metrics Insights alarms, every metric in the `Metrics` array must use one of the supported wall clock periods.

**Note**  
A Metrics Insights alarm can evaluate a time range of no more than 3 hours (**Period** multiplied by **Evaluation Periods**). When a Metrics Insights alarm uses a wall clock window, CloudWatch automatically reserves one additional period to align the window to wall clock boundaries. As a result, the effective limit becomes **Period** multiplied by (**Evaluation Periods** \+ 1), which must still be 3 hours or less. This means a Metrics Insights alarm that uses a wall clock window can span one fewer evaluation period than the same alarm with a sliding window. For example, with a 1-hour period, a sliding window supports up to 3 evaluation periods, but a wall clock window supports up to 2. If you exceed this limit, `PutMetricAlarm` returns a validation error.

### Time zones and daylight saving time
<a name="wall-clock-timezone"></a>

You can optionally specify a time zone for the wall clock window. If you don't specify a time zone, CloudWatch uses `UTC`. The time zone determines where wall clock boundaries fall: for example, an alarm with a 1-day period in `America/New_York` evaluates each calendar day from local midnight to local midnight in New York, while the same alarm in `UTC` evaluates from 00:00 UTC to 00:00 UTC. Time zones with non-whole-hour offsets such as `Asia/Kolkata` (`+05:30`) shift the boundaries even for hourly and sub-hourly periods.

You can specify the time zone in any of the following forms:
+ An IANA time zone identifier, such as `America/New_York`, `Europe/London`, or `Asia/Kolkata`.
+ A fixed UTC offset, such as `+05:30`, `-08:00`, or `Z` (equivalent to UTC).
+ An offset-prefixed identifier, such as `UTC+05:30` or `GMT-08:00`.

The time zone you specify must resolve to a UTC offset that is a multiple of 5 minutes. For example, `+01:00`, `+05:30`, and `+01:05` are accepted, but `+01:03` is rejected. CloudWatch rejects time zones that don't meet this requirement with a validation error at alarm creation.

When you specify an IANA time zone, CloudWatch automatically handles daylight saving time transitions. The evaluation window remains aligned to the local wall clock in the specified time zone, even on the days when clocks change. Fixed UTC offsets and offset-prefixed identifiers don't observe daylight saving time.

### How often the alarm is evaluated
<a name="wall-clock-evaluation-frequency"></a>

An alarm with a wall clock window is evaluated at the same frequency as an alarm with a sliding window. Choosing a wall clock window changes only the *boundaries* of the window that CloudWatch uses to retrieve metric data, not how often the alarm runs.

For example, an alarm with a 1-hour period and a wall clock window evaluates every minute. Each evaluation looks at the data for the most recently completed clock hour. As a new clock hour begins, the window advances to the new hour boundary.

To create a metric alarm that uses a wall clock window, see [Create a metric alarm that uses a wall clock evaluation window](Create_WallClock_Alarm.md).