# PromQL alarms

A PromQL alarm monitors metrics using a Prometheus Query Language (PromQL) instant query.
The query selects metrics ingested through the CloudWatch OTLP endpoint, and all matching time series
returned by the query are considered to be breaching. The alarm evaluates the query at a regular
interval and tracks each breaching time series independently as a
_contributor_.

For information about ingesting metrics using OpenTelemetry, see [OpenTelemetry](CloudWatch-OpenTelemetry-Sections.md "CloudWatch-OpenTelemetry-Sections.md").

## How PromQL alarms work

A PromQL alarm evaluates a PromQL instant query on a recurring schedule defined by the
`EvaluationInterval`. The query returns only the time series that satisfy the
condition. Each returned time series is a _contributor_, identified by its
unique set of attributes.

The alarm uses duration-based state transitions:

- When a contributor is returned by the query, it is considered
  _breaching_. If the contributor continues breaching for the duration
  specified by `PendingPeriod`, the contributor transitions to `ALARM`
  state.
- When a contributor stops being returned by the query, it is considered
  _recovering_. If the contributor remains absent for the duration
  specified by `RecoveryPeriod`, the contributor transitions back to `OK`
  state.

The alarm is in `ALARM` state when at least one contributor has been breaching
for longer than the pending period. The alarm returns to `OK` state when all
contributors have recovered.

## PromQL alarm configuration

A PromQL alarm is configured with the following parameters:

- **PendingPeriod** is the duration in seconds that a contributor must continuously breach before the
  contributor transitions to `ALARM` state. This is equivalent to the Prometheus alert rule's
  `for` duration.
- **RecoveryPeriod** is the duration in seconds that a contributor must stop breaching before the contributor
  transitions back to `OK` state. This is equivalent to the Prometheus alert rule's
  `keep_firing_for` duration.
- **EvaluationInterval** is how frequently, in seconds, the alarm evaluates the PromQL query.

To create a PromQL alarm, see [Create an alarm using a PromQL query](Create_PromQL_Alarm.md "Create_PromQL_Alarm.md").
