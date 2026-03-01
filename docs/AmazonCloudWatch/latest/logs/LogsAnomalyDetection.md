# Log anomaly detection

You can detect anomalies in your log data in two ways: by creating a _log anomaly
detector_ for continuous monitoring, or by using the [anomaly detection](CWL_QuerySyntax-Anomaly.md "CWL_QuerySyntax-Anomaly.md") command in CloudWatch Logs
Insights queries for on-demand analysis.

A log anomaly detector scans the log events ingested into a log group and finds anomalies
in the log data automatically. Anomaly detection uses machine-learning and pattern
recognition to establish baselines of typical log content. For on-demand analysis, you can
use the `anomaly detection` command in CloudWatch Logs Insights queries to identify unusual
patterns in time-series data. For more information about query-based anomaly detection, see
[Using anomaly detection in CloudWatch Logs Insights](LogsAnomalyDetection-Insights.md "LogsAnomalyDetection-Insights.md").

After you create an anomaly detector for a log group, it trains using the past two weeks
of log events in the log group for training. The training period can take up to 15 minutes.
After the training is complete, it begins to analyze incoming logs to identify anomalies,
and the anomalies are displayed in the CloudWatch Logs console for you to examine.

CloudWatch Logs pattern recognition extracts log patterns by identifying static and dynamic content
in your logs. Patterns are useful for analyzing large log sets because a large number of log
events can often be compressed into a few patterns.

For example, see the following sample of three log events.

```
2023-01-01 19:00:01 [INFO] Calling DynamoDB to store for ResourceID: 12342342k124-12345
2023-01-01 19:00:02 [INFO] Calling DynamoDB to store for ResourceID: 324892398123-1234R
2023-01-01 19:00:03 [INFO] Calling DynamoDB to store for ResourceID: 3ff231242342-12345
```

In the previous sample, all three log events follow one pattern:

```
<Date-1> <Time-2> [INFO] Calling DynamoDB to store for resource id <ResourceID-3>
```

Fields within a pattern are called _tokens_. Fields that vary within a
pattern, such as a request ID or timestamp, are referred to as _dynamic
tokens_. Each different value found for a dynamic token is called a
_token value_.

If CloudWatch Logs can infer the type of data that a dynamic token represents, it displays the token
as `<`string`-`number`>`.
The `string` is a description of the type of data that the token
represents. The `number` shows where in the pattern this token
appears, compared to the other dynamic tokens.

CloudWatch Logs assigns the string part of the name based on analyzing the content of the log events
that contain it.

If CloudWatch Logs can't infer the type of data that a dynamic token represents, it displays the
token as <Token-`number`>, and
`number` indicates where in the pattern this token appears,
compared to the other dynamic tokens.

Common examples of dynamic tokens include error codes, IP addresses, timestamps, and
request IDs.

Logs anomaly detection uses these patterns to find anomalies. After the anomaly detector
model training period, logs are evaluated against known trends. The anomaly detector flags
significant fluctuations as anomalies.

This chapter describes how to enable anomaly detection, view anomalies, create alarms for
log anomaly detectors, and metrics that log anomaly detectors publish. It also describes how
to encrypt anomaly detector and its results with AWS Key Management Service.

Creating log anomaly detectors doesn't incur charges.

## Severity and priority of anomalies and patterns

Each anomaly found by a log anomaly detector is assigned a
_priority_. Each pattern found is assigned a
_severity_.

- _Priority_ is automatically computed, and is based on both
  the severity level of the pattern and the amount of deviation from expected
  values. For example, if a certain token value suddenly increases by 500%, that
  anomaly might be designated as `HIGH` priority even if its severity
  is `NONE`.
- _Severity_ is based only on keywords found in the patterns
  such as `FATAL`, `ERROR`, and `WARN`. If none
  of these keywords are found, the severity of a pattern is marked as
  `NONE`.

## Anomaly visibility time

When you create an anomaly detector, you specify the maximum anomaly visibility period
for it. This is the number of days that the anomaly is displayed in the console and is
returned by the [ListAnomalies](../../../AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.md") API operation. After this time period has elapsed for an
anomaly, if it continues to happen, it's automatically accepted as regular behavior and
the anomaly detector model stops flagging it as an anomaly.

If you don't adjust the visibility time when you create an anomaly detector, 21 days
is used as the default.

## Suppressing an anomaly

After an anomaly has been found, you can choose to suppress it temporarily or
permanently. Suppressing an anomaly causes the anomaly detector to stop flagging this
occurrence as an anomaly for the amount of time that you specify. When you suppress an
anomaly, you can choose to suppress only that specific anomaly, or suppress all
anomalies related to the pattern that the anomaly was found in.

You can still view suppressed anomalies in the console. You can also choose to stop
suppressing them.

## Frequently asked questions

**Does AWS use my data to train machine-learning algorithms for
AWS use or for other customers?**

No. The anomaly detection model created by the training is based on the log events in
a log group and is used only within that log group and that AWS account.

**What types of log events work well with anomaly
detection?**

**Log anomaly detection is well-suited for:** Application
logs and other types of logs where most log entries fit typical patterns. Log groups
with events that contain a log level or severity keywords such as
**INFO**, **ERROR**, and
**DEBUG** are especially well-suited to log anomaly
detection.

**Log anomaly detection is not suited for:** Log events
with extremely long JSON structures, such as CloudTrail Logs. Pattern analysis analyzes only
up to the first 1500 characters of a log line, so any characters beyond that limit are
skipped.

Audit or access logs, such as VPC flow logs, will also have less success with anomaly
detection. Anomaly detection is meant to find application issues, so it might not be
well-suited for network or access anomalies.

To help you determine whether an anomaly detector is suited to a certain log group,
use CloudWatch Logs pattern analysis to find the number of patterns in the log events in the
group. If the number of patterns is no more than about 300, anomaly detection might work
well. For more information about pattern analysis, see [Pattern analysis](CWL_AnalyzeLogData_Patterns.md "CWL_AnalyzeLogData_Patterns.md").

**What gets flagged as an anomaly?**

The following occurrences can cause a log event to be flagged as an anomaly:

- A log event with a pattern not seen before in the log group.
- A significant variation to a known pattern.
- A new value for a dynamic token that has a discrete set of usual
  values.
- A large change in the number of occurrences of a value for a dynamic token.

While all the preceding items might be flagged as anomalies, they don't all mean that
the application is performing poorly. For example, a higher-than-usual number of
`200` success values might be flagged as an anomaly. In cases like this,
you might consider suppressing these anomalies that don't indicate problems.

**What happens with sensitive data that is being masked?**

Any parts of log events that are masked as sensitive data are not scanned for
anomalies. For more information about masking sensitive data, see [Help protect sensitive log data with masking](mask-sensitive-log-data.md "mask-sensitive-log-data.md").
