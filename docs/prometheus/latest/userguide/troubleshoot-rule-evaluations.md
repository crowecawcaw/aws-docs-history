# Troubleshoot rule evaluations

This guide provides step-by-step troubleshooting procedures for common issues with
rule evaluations in Amazon Managed Service for Prometheus (AMP). Follow these procedures to diagnose and resolve
problems with your alerting and recording rules.

###### Topics

- [Validate alert firing
  status](#troubleshoot-rule-validate-firing-status "#troubleshoot-rule-validate-firing-status")
- [Resolve missing
  alert notifications](#troubleshoot-rule-missing-alert-notifications "#troubleshoot-rule-missing-alert-notifications")
- [Check rule health
  status](#troubleshoot-rule-check-health-status "#troubleshoot-rule-check-health-status")
- [Use offset in queries to handle
  ingestion delays](#troubleshoot-rule-offset-queries "#troubleshoot-rule-offset-queries")
- [Common issues and
  solutions](#troubleshoot-rule-common-issues "#troubleshoot-rule-common-issues")
- [Best practices for rule
  evaluations](#troubleshoot-rule-best-practices "#troubleshoot-rule-best-practices")

## Validate alert firing

status

When troubleshooting rule evaluation issues, first verify if your alert has fired
by querying the synthetic time series `ALERTS`. The `ALERTS`
time series include the following labels:

- alertname – The name of the
  alert.
- alertstate – Either
  **pending** or **firing**.
  - pending – The alert is
    waiting for the duration specified in the `for`
    clause.
  - firing – The alert has met
    the conditions for the specified duration. Additional labels are
    defined in your alerting rule.

###### Note

While an alert is **firing** or **pending**,
the sample value is **1**. When your alert is idle, no samples
are produced.

## Resolve missing

alert notifications

If alerts are firing but notifications are not arriving, verify the following
Alertmanager settings:

1. Verify your Alertmanager configuration
   – Check that routes receivers, and settings are correctly configured.
   Review route block settings, including wait times, time intervals, and
   required labels, which can affect alert firing. Compare alerting rules with
   their corresponding routes and receivers to confirm proper matching. For
   routes with `time_interval`, verify that timestamps fall within
   the specified intervals.
2. Check alert receiver permissions –
   When using an Amazon SNS topic, verify AMP has the required permissions to
   publish notifications. For more information, see [Giving Amazon Managed Service for Prometheus
   permission to send alert messages to your Amazon SNS topic](AMP-alertmanager-receiver-AMPpermission.md "AMP-alertmanager-receiver-AMPpermission.md").
3. Validate receiver payload compatibility
   – Confirm your alert receiver accepts Alertmanager's payload format.
   For Amazon SNS requirements, see [Understanding
   Amazon SNS message validation rules](AMP-alertmanager-receiver-validation-truncation.md "AMP-alertmanager-receiver-validation-truncation.md").
4. Review Alertmanager logs – AMP
   provides vended logs from Alertmanager to help debug notification issues.
   For more information, see [Monitor Amazon Managed Service for Prometheus events with CloudWatch Logs](CW-logs.md "CW-logs.md").

For more information about Alertmanager, see [Managing and forwarding alerts in Amazon Managed Service for Prometheus with alert
manager](AMP-alert-manager.md "AMP-alert-manager.md").

## Check rule health

status

Malformed rules can cause evaluation failures. Use the following methods to
identify why a rule failed to evaluate:

###### Example

**Use the ListRules API**

The [ListRules](AMP-APIReference-ListRules.md "AMP-APIReference-ListRules.md") API provides information about
rule health. Check the `health` and `lastError` fields to
diagnose issues.

**Example response:**

```
{
  "status": "success",
  "data": {
    "groups": [
      {
        "name": "my_rule_group",
        "file": "my_namespace",
        "rules": [
          {
            "state": "firing",
            "name": "broken_alerting_rule",
            "query": "...",
            "duration": 0,
            "keepFiringFor": 0,
            "labels": {},
            "annotations": {},
            "alerts": [],
            "health": "err",
            "lastError": "vector contains metrics with the same labelset after applying alert labels",
            "type": "alerting",
            "lastEvaluation": "1970-01-01T00:00:00.00000000Z",
            "evaluationTime": 0.08
          }
        ]
      }
    ]
  }
}

```

###### Example

**Use vended logs**

The ListRules API only displays the most recent information. For a more
detailed history, enable [vended logs](CW-logs.md "CW-logs.md") in your
workspace to access:

- Timestamps of evaluation failures
- Detailed error messages
- Historical evaluation data
  **Example vended log message:**

```
{
  "workspaceId": "ws-a2c55905-e0b4-4065-a310-d83ce597a391",
  "message": {
    "log": "Evaluating rule failed, name=broken_alerting_rule, group=my_rule_group, namespace=my_namespace, err=vector contains metrics with the same labelset after applying alert labels",
    "level": "ERROR",
    "name": "broken_alerting_rule",
    "group": "my_rule_group",
    "namespace": "my_namespace"
  },
  "component": "ruler"
}

```

For more examples of logs from Ruler or Alertmanager, see [Troubleshooting Ruler](Troubleshooting-rule-fail-error.md "Troubleshooting-rule-fail-error.md") and [Managing and forwarding alerts in Amazon Managed Service for Prometheus with alert
manager](AMP-alert-manager.md "AMP-alert-manager.md").

## Use offset in queries to handle

ingestion delays

By default, expressions are evaluated with no offset (instant query), using values
at the evaluation time. If metrics ingestion is delayed, recording rules might not
represent the same values as when you manually evaluate the expression after all
metrics are ingested.

###### Tip

Using the offset modifier can reduce issues caused by ingestion delays. For
more information, see [Offset modifier](https://prometheus.io/docs/prometheus/latest/querying/basics/#offset-modifier "https://prometheus.io/docs/prometheus/latest/querying/basics/#offset-modifier") in the _Prometheus
documentation_.

If your rule evaluates at 12:00, but the latest sample for the metric is
from 11:45 due to ingestion delay, the rule will find no samples at the
12:00 timestamp. To mitigate this, add an offset, such as:
`my_metric_name offset 15m` .

When metrics originate from different sources, such as two servers, they
might be ingested at different times. To mitigate this, form an expression,
such as: `metric_from_server_A / metric_from_server_B`

If the rule evaluates between the ingestion times of server A and server
B, you'll get unexpected results. Using an offset can help align the
evaluation times.

## Common issues and

solutions

**Gaps in recording rule data**

If you notice gaps in your recording rule data compared to manual evaluation (when
you directly execute the recording rule's original PromQL expression through the
query API or UI), this might be due to one of the following:

1. Long evaluation times – A rule group
   cannot have multiple simultaneous evaluations. If evaluation time exceeds
   the configured interval, subsequent evaluations may be missed. Multiple
   consecutive missed evaluations exceeding the configured interval can cause
   the recording rule to become stale. For more information, see [Staleness](https://prometheus.io/docs/prometheus/latest/querying/basics/#staleness "https://prometheus.io/docs/prometheus/latest/querying/basics/#staleness") in the _Prometheus documentation_.
   You can monitor evaluation duration using the CloudWatch metric
   `RuleGroupLastEvaluationDuration` to identify rule groups
   that are taking too long to evaluate.
2. Monitoring missed evaluations – AMP
   provides the `RuleGroupIterationsMissed` CloudWatch metric to track
   when evaluations are skipped. The ListRules API displays the evaluation time
   and last evaluation time for each rule/group, which can help identify
   patterns of missed evaluations. For more information, see [ListRules](AMP-APIReference-ListRules.md "AMP-APIReference-ListRules.md").

**Recommendation: Split rules into separate
groups**

To reduce evaluation durations, split rules into separate rule groups. Rules
within a group execute sequentially, while rule groups can execute in parallel. Keep
related rules that depend on each other in the same group. Generally, smaller rule
groups ensure more consistent evaluations and fewer gaps.

## Best practices for rule

evaluations

1. Optimize rule group size – Keep rule
   groups small to ensure consistent evaluations. Group related rules together,
   but avoid large rule groups.
2. Set appropriate evaluation intervals
   – Balance between timely alerts and system load. Review the stability
   patterns of your monitored metrics to understand their normal fluctuation
   ranges.
3. Use offset modifiers for delayed metrics
   – Add offsets to compensate for ingestion delays. Adjust offset
   duration based on observed ingestion patterns.
4. Monitor evaluation performance –
   Track the `RuleGroupIterationsMissed` metric. Review evaluation
   times in the ListRules API.
5. Validate rule expressions – Ensure
   expressions match exactly between rule definitions and manual queries. Test
   expressions with different time ranges to understand behavior.
6. Review rule health regularly – Check
   for errors in rule evaluations. Monitor vended logs for recurring
   issues.

By following these troubleshooting steps and best practices, you can identify and
resolve common issues with rule evaluations in Amazon Managed Service for Prometheus.
