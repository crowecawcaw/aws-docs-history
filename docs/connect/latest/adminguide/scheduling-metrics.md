# Schedule Adherence metrics in Amazon Connect

This section describes the metrics used when calculating Historical Schedule
Adherence.

The following Scheduling metrics are available on the Real-time and Historical
metrics reports. Use these metrics to track when agents are following the schedule
that you have created. For instructions about how add these metrics to your report,
see [How to create a historical
metrics report](create-historical-metrics-report.md#historical-reports-howto-create "create-historical-metrics-report.md#historical-reports-howto-create").

These metrics are available in AWS Regions only where [Forecasting, capacity planning, and
scheduling](regions.md#optimization_region "regions.md#optimization_region") is
available.

## Adherence

This metric measures the percentage of time that an agent correctly follows their schedule.

**Metric type**: String

- Min value: 0.00%
- Max value: 100.00%

**Metric category**: Agent activity-driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AGENT_SCHEDULE_ADHERENCE`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Adherence

**Notes**:

- Any time you change the schedule, Schedule Adherence is re-calculated up
  to 30 days in the past from the current date (not the date of the schedule),
  if schedules are changed.

## Adherent time

This metric measures the total time an agent adhered to their schedule.

**Metric type**: String

**Metric category**: Agent activity-driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AGENT_ADHERENT_TIME`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Adherent time

## Non-adherent time

This metric measures the total time an agent did not adhere to their schedule.

**Metric type**: String (_hh:mm:ss_)

**Metric category**: Agent activity-driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AGENT_NON_ADHERENT_TIME`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Non-Adherent time

## Scheduled time

This metric measures the total time an agent was scheduled (either for productive or non-productive
time) and _Adherence_ for those shifts was set to
`Yes`.

**Metric type**: String

**Metric category**: Agent activity-driven metric

**How to access using the Amazon Connect API**:

- [GetMetricDataV2](../APIReference/API_GetMetricDataV2.md "../APIReference/API_GetMetricDataV2.md") API metric identifier:
  `AGENT_SCHEDULED_TIME`

**How to access using the Amazon Connect admin website**:

- Historical metrics reports: Scheduled time

## Using thresholds

This status indicates an agent is operating within configured adherence
thresholds rather than exact scheduled times.

## Threshold duration

The amount of time an agent has been operating within their configured
threshold window.
