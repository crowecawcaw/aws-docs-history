# Alarm evaluation

## Metric alarm states

A metric alarm has the following possible states:

- `OK` – The metric or expression is within the defined threshold.
- `ALARM` – The metric or expression is outside of the defined threshold.
- `INSUFFICIENT_DATA` – The alarm has just started, the metric is not available, or not enough data is available for the metric to determine the alarm state.

## Alarm evaluation state

In addition to the alarm state, each alarm has an evaluation state that provides information about the alarm evaluation process. The following states may occur:

- `PARTIAL_DATA` – Indicates that not all the available data was able to be retrieved due to quota limitations. For more information, see [How partial data is handled](cloudwatch-metrics-insights-alarms-partial-data.md "cloudwatch-metrics-insights-alarms-partial-data.md").
- `EVALUATION_ERROR` – Indicates configuration errors in alarm setup that require review and correction. Refer to StateReason field of the alarm for more details.
- `EVALUATION_FAILURE` – Indicates temporary CloudWatch issues. We recommend manual monitoring until the issue is resolved

You can view the evaluation state in the alarm details in the console, or by using the `describe-alarms` CLI command or `DescribeAlarms` API.

## Alarm evaluation settings

When you create an alarm, you specify three settings to enable CloudWatch to evaluate when to change the alarm state:

- **Period** is the length of time to use to evaluate the metric or expression to create each individual data point for an alarm. It is expressed in seconds.
- **Evaluation Periods** is the number of the most recent periods, or data points, to evaluate when determining alarm state.
- **Datapoints to Alarm** is the number of data points within the Evaluation Periods that must be breaching to cause the alarm to go to the `ALARM` state. The breaching data points don't have to be consecutive, but they must all be within the last number of data points equal to **Evaluation Period**.

For any period of one minute or longer, an alarm is evaluated every minute and the evaluation is based on the window of time defined by the **Period** and **Evaluation Periods**. For example, if the **Period** is 5 minutes (300 seconds) and **Evaluation Periods** is 1, then at the end of minute 5 the alarm evaluates based on data from minutes 1 to 5. Then at the end of minute 6, the alarm is evaluated based on the data from minutes 2 to 6.

If the alarm period is 10 seconds, 20 seconds, or 30 seconds, the alarm is evaluated every
10 seconds. For more information, see [High-resolution alarms](#high-resolution-alarms "#high-resolution-alarms").

If the number of evaluation periods multiplied by the length of each evaluation period
exceeds one day, the alarm is evaluated once per hour. For more details about how these
multi-day alarms are evaluated, see [Example of evaluating a multi-day alarm](#evaluate-multiday-alarm "#evaluate-multiday-alarm").

In the following figure, the alarm threshold for a metric alarm is set to three units.
Both **Evaluation Period** and **Datapoints to Alarm** are 3. That is, when all existing data points in the most recent three consecutive periods are
above the threshold, the alarm goes to `ALARM` state. In the figure, this happens
in the third through fifth time periods. At period six, the value dips below the threshold, so
one of the periods being evaluated is not breaching, and the alarm state changes back to
`OK`. During the ninth time period, the threshold is breached again, but for only
one period. Consequently, the alarm state remains `OK`.

![Alarm threshold trigger alarm](images/alarm_graph.png)

When you configure **Evaluation Periods** and **Datapoints to Alarm** as different values, you're setting an "M out of N" alarm. **Datapoints to Alarm** is ("M") and **Evaluation Periods** is ("N").The evaluation interval is the number of evaluation periods
multiplied by the period length. For example, if you configure 4 out of 5 data points with a
period of 1 minute, the evaluation interval is 5 minutes. If you configure 3 out of 3 data
points with a period of 10 minutes, the evaluation interval is 30 minutes.

###### Note

If data points are missing soon after you create an alarm, and the metric was being
reported to CloudWatch before you created the alarm, CloudWatch retrieves the most recent data points
from before the alarm was created when evaluating the alarm.

## High-resolution alarms

If you set an alarm on a high-resolution metric, you can specify a high-resolution alarm
with a period of 10 seconds, 20 seconds, or 30 seconds. There is a higher charge for high-resolution alarms. For
more information about high-resolution metrics, see [Publish custom metrics](publishingMetrics.md "publishingMetrics.md").

## Example of evaluating a multi-day alarm

An alarm is a multi-day alarm if the number of evaluation periods multiplied by the
length of each evaluation period exceeds one day. Multi-day alarms are evaluated once per
hour. When multi-day alarms are evaluated, CloudWatch takes into account only the metrics up to
the current hour at the :00 minute when evaluating.

For example, consider an alarm that monitors a job that runs every 3 days at
10:00.

1. At 10:02, the job fails
2. At 10:03, the alarm evaluates and stays in `OK` state, because the
   evaluation considers data only up to 10:00.
3. At 11:03, the alarm considers data up to 11:00 and goes into `ALARM`
   state.
4. At 11:43, you correct the error and the job now runs successfully.
5. At 12:03, the alarm evaluates again, sees the successful job, and returns to
   `OK` state.
