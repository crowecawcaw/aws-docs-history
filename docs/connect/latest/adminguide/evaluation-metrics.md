

# Evaluation metrics in Connect Customer
<a name="evaluation-metrics"></a>

You can view the following metrics on the [Agent performance evaluations dashboard](agent-performance-evaluation-dashboard.md). With these metrics, you can view aggregated agent performance, and get insights across agent cohorts and over time. 

## Average evaluation score
<a name="average-evaluation-score-hmetric"></a>

This metric provides the average evaluation score for all submitted evaluations. Evaluations for calibrations are excluded from this metric.

The average evaluation score corresponds to the grouping. For example, if the grouping contains evaluation questions, then the average evaluation score is provided for the questions. If the grouping does not contain evaluation form, section or question, then the average evaluation score is at an evaluation form level.

**Metric type**: Percent

**Metric category**: Contact evaluation driven metric

**How to access using the Connect Customer API**: 
+ [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) API metric identifier: `AVG_EVALUATION_SCORE`

**How to access using the Connect Customer admin website**: 
+ Dashboard: [Agent performance evaluations dashboard](agent-performance-evaluation-dashboard.md)

**Calculation logic**:
+ Get sum of of evaluation scores: forms \+ sections \+ questions.
+ Get total number of evaluations where scoring has been completed and recorded.
+ Calculate average score: (sum of scores) / (total evaluations).

**Notes**:
+ Excludes calibration evaluations. 
+ Score granularity depends on grouping level. 
+ Returns percentage value. 
+ Requires at least one filter from: queues, routing profiles, agents, or user hierarchy groups. 
+ Based on contact initiation date. 
+ Data for this metric is available starting from January 10, 2025 0:00:00 GMT.

## Average evaluation score (Submit time)
<a name="average-evaluation-score-by-submit-time-hmetric"></a>

This metric provides the average evaluation score across all submission events by the evaluator, including resubmissions. Each submission event, including every resubmission of the same evaluation, is included in the average. Evaluations for calibrations are excluded from this metric.

The average evaluation score is provided at an evaluation form level.

**Metric type**: Percent

**Metric category**: Contact evaluation driven metric

**How to access using the Connect Customer API**: 
+ [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) API metric identifier: `AVG_EVALUATION_SCORE_BY_SUBMIT_TIME`

**How to access using the Connect Customer admin website**: 
+ Dashboard: [Agent performance evaluations dashboard](agent-performance-evaluation-dashboard.md)

**Calculation logic**:
+ Get sum of of evaluation scores across forms.
+ Get total number of submission events where scoring has been completed and recorded, including resubmissions.
+ Calculate average score: (sum of scores) / (total submission events).

**Notes**:
+ Includes all resubmissions. 
+ Excludes calibration evaluations. 
+ Provided at an evaluation form level. 
+ Returns percentage value. 
+ Requires at least one filter from: queues, routing profiles, agents, or user hierarchy groups. 
+ Based on evaluation submission timestamp. 

## Average weighted evaluation score
<a name="average-weighted-evaluation-score-hmetric"></a>

This metric provides the average weighted evaluation score for all submitted evaluations. Evaluations for calibrations are excluded from this metric.

The weights are per the evaluation form version that was used to perform the evaluation. 

 The average evaluation score corresponds to the grouping. For example, if the grouping contains evaluation questions, then the average evaluation score is provided for the questions. If the grouping does not contain evaluation form, section or question, then the average evaluation score is at an evaluation form level. 

**Metric type**: Percent

**Metric category**: Contact evaluation driven metric

**How to access using the Connect Customer API**: 
+ [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) API metric identifier: `AVG_WEIGHTED_EVALUATION_SCORE`

**How to access using the Connect Customer admin website**: 
+ Dashboard: [Agent performance evaluations dashboard](agent-performance-evaluation-dashboard.md)

**Calculation logic**:
+ Get sum of weighted scores using form version weights.
+ Get total number of evaluations where scoring has been completed and recorded.
+ Calculate weighted average: (sum of weighted scores) / (total evaluations).

**Notes**:
+ Uses evaluation form version-specific weights. 
+ Excludes calibration evaluations. 
+ Score granularity depends on grouping level. 
+ Returns percentage value. 
+ Requires at least one filter from: queues, routing profiles, agents, or user hierarchy groups. 
+ Based on contact initiation date. 
+ Data for this metric is available starting from January 10, 2025 0:00:00 GMT.

## Automatic fails percent
<a name="percent-evaluation-automatic-failures-hmetric"></a>

This metric provides the percentage of performance evaluations with automatic fails. Evaluations for calibrations are excluded from this metric. 

If a question is marked as an automatic fail, then the parent section and the form is also marked as an automatic fail. 

**Metric type**: Percent

**Metric category**: Contact evaluation driven metric

**How to access using the Connect Customer admin website**: 
+ Dashboard: [Agent performance evaluations dashboard](agent-performance-evaluation-dashboard.md)

**Calculation logic**:
+ Get total automatic fails count.
+ Get total evaluations performed.
+ Calculate percentage: (automatic fails / total evaluations) \* 100.

**Notes**:
+ Automatic fail cascades up (question → section → form).
+ Excludes calibration evaluations.
+ Returns percentage value.
+ Requires at least one filter from: queues, routing profiles, agents, or user hierarchy groups.
+ Based on contact initiation date.
+ Data for this metric is available starting from January 10, 2025 0:00:00 GMT.

## Evaluations performed
<a name="evaluations-performed-hmetric"></a>

This metric provides the number of evaluations performed with evaluation status as "Submitted." Evaluations for calibrations are excluded from this metric.

**Metric type**: Integer

**Metric category**: Contact evaluation driven metric

**How to access using the Connect Customer API**: 
+ [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) API metric identifier: `EVALUATIONS_PERFORMED`

**How to access using the Connect Customer admin website**: 
+ Dashboard: [Agent performance evaluations dashboard](agent-performance-evaluation-dashboard.md)

**Calculation logic**:
+ Check evaluationId present?
+ Verify itemType is form.
+ Count submitted evaluations (excluding calibrations).

**Notes**:
+ Counts only submitted evaluations.
+ Excludes calibration evaluations.
+ Returns integer count.
+ Requires at least one filter from: queues, routing profiles, agents, or user hierarchy groups.
+ Based on contact initiation date.
+ Data for this metric is available starting from January 10, 2025 0:00:00 GMT.

## Evaluations performed (Submit time)
<a name="evaluations-performed-by-submit-time-hmetric"></a>

This metric provides the number of evaluations submitted by the evaluator, including resubmissions. Each submission event, including every resubmission of the same evaluation, is also counted here. Evaluations for calibrations are excluded from this metric.

**Metric type**: Integer

**Metric category**: Contact evaluation driven metric

**How to access using the Connect Customer API**: 
+ [GetMetricDataV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_GetMetricDataV2.html) API metric identifier: `EVALUATIONS_PERFORMED_BY_SUBMIT_TIME`

**How to access using the Connect Customer admin website**: 
+ Dashboard: [Agent performance evaluations dashboard](agent-performance-evaluation-dashboard.md)

**Calculation logic**:
+ Check evaluationId present?
+ Verify itemType is form.
+ Count every submission event (excluding calibrations), including resubmissions.

**Notes**:
+ Counts every submission event, including resubmissions.
+ Excludes calibration evaluations.
+ Returns integer count.
+ Requires at least one filter from: queues, routing profiles, agents, or user hierarchy groups.
+ Based on evaluation submission timestamp.