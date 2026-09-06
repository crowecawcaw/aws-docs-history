

# Suppression rule metrics
<a name="findings_suppression-rule-metrics"></a>

With Amazon GuardDuty, you can monitor how often each suppression rule matches and archives findings. GuardDuty publishes these metrics to Amazon CloudWatch under the AWS/GuardDuty namespace. 

**GuardDuty counts matched findings and suppressed findings differently**  
GuardDuty emits FindingsMatchedByFilter when a finding matches a suppression rule or a NOOP filter (a filter with no action). This metric increments regardless of the filter's action. GuardDuty emits FindingsSuppressedByFilter only when the rule's action is Archive and the rule is the highest-priority archiving rule for that finding. 

GuardDuty publishes suppression rule metrics based on your account configuration:
+ For standalone accounts (not part of an organization), GuardDuty publishes metrics to that account.
+ For accounts that are part of an organization, GuardDuty publishes metrics to the delegated GuardDuty administrator account. For more information about how administrator and member accounts work in GuardDuty, see [Multiple accounts in Amazon GuardDuty](guardduty_accounts.md).

## Metric details
<a name="suppression-rule-metric-details"></a>

The following table describes the Amazon CloudWatch metrics that GuardDuty publishes for suppression rules. 


| Metric | Unit | Description | 
| --- | --- | --- | 
| FindingsMatchedByFilter | Count | The number of findings that matched the criteria of a suppression rule or NOOP filter. A finding can match multiple suppression rules or NOOP filters, and GuardDuty counts it once per match. Every match generates 1 data point. | 
| FindingsSuppressedByFilter | Count | The number of findings archived by a suppression rule. When multiple rules match the same finding, GuardDuty counts only the rule with the lowest Rank value. Every suppression generates 1 data point. | 

## View suppression rule metrics in Amazon CloudWatch
<a name="suppression-rule-metric-view"></a>

You can find suppression rule metrics in the Amazon CloudWatch console under the **AWS/GuardDuty** namespace, grouped by the **FilterName** dimension. The value of the `FilterName` dimension is the name of the suppression rule or filter. For instructions on locating and graphing metrics in Amazon CloudWatch, see [Viewing available metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html) in the *Amazon CloudWatch User Guide*.