

# Monitor and troubleshoot rule sets

Use Amazon CloudWatch metrics and Mail Manager rule-set logs to monitor rule-set processing and investigate email that did not follow the expected path. Metrics show successful rule-set executions and actions over time. Logs provide per-message details, including the rule, selected recipients, action order, action status, and failure details.

**Topics**
+ [Monitor rule-set processing](#eb-rules-monitoring-processing)
+ [Enable rule-set logging](#eb-rules-monitoring-enable-logging)
+ [CloudWatch metrics for rule sets and SMTP relays](#eb-rules-monitoring-cloudwatch-metrics)
+ [Follow rule execution](#eb-rules-monitoring-follow-execution)
+ [Troubleshoot rule-set processing](#eb-rules-monitoring-troubleshoot)

## Monitor rule-set processing
<a name="eb-rules-monitoring-processing"></a>

CloudWatch metrics and rule-set logs provide different levels of detail.
+ A **metric** is a time-series value in CloudWatch. Use metrics to monitor successful rule-set executions and actions over time.
+ A **dimension** identifies the rule set associated with a metric series.
+ A **vended log** is a per-message record delivered to a destination that you configure. Use logs to identify which rules and actions processed a message.

Metrics do not identify individual rules, actions, or recipients. Use rule-set logs when you need to investigate a specific message or explain why an expected action did not run.

## Enable rule-set logging
<a name="eb-rules-monitoring-enable-logging"></a>

Enable rule-set logging before you need per-message troubleshooting. Mail Manager can deliver these logs to Amazon CloudWatch Logs, Amazon S3, or Amazon Data Firehose.

For delivery-source, destination, permission, and setup instructions, see [Setting up Mail Manager log delivery](eb-logging.md#setting-up-log-delivery). For the rule-set log schema and example CloudWatch Logs Insights queries, see [Rule set logs – `APPLICATION_LOGS`](eb-logging.md#rule-set-logs) and [Example CloudWatch Logs Insights queries](eb-logging.md#rule-set-queries).

## CloudWatch metrics for rule sets and SMTP relays
<a name="eb-rules-monitoring-cloudwatch-metrics"></a>

Mail Manager publishes rule-set and SMTP relay metrics to the `AWS/SES/MailManager` namespace. Each metric uses the `Count` unit. The dimension identifies the rule set or relay associated with the metric.

The following table lists the rule-set and SMTP relay metrics.


| Metric | Dimension | Description | Recommended statistic | 
| --- | --- | --- | --- | 
| ActionSuccessful | RuleSetId | Records 1 when action processing completes without an immediate error. Records 0 when an action reports a handled customer configuration error. For a remote action, 1 can represent successful initiation rather than its final outcome. | Sum | 
| ExecutionSuccessful | RuleSetId | Records 1 when a rule-set execution completes successfully. This metric does not confirm that every action succeeded. | Sum | 
| Delivered | RelayId | Records the number of recipients with a successful final delivery outcome for an SMTP relay action. | Sum | 
| Rejected | RelayId | Records the number of recipients whose final SMTP relay outcome was not successful. This includes bounced recipients and recipients that the destination rejected. | Sum | 

`ActionSuccessful` can record successful initiation before a remote action has its final outcome. For an SMTP relay action, use `Delivered` and `Rejected` to monitor final recipient outcomes.

**Rule-set metric example**  
The following values select successful action activity for one rule set.

```
Namespace: AWS/SES/MailManager
Metric name: ActionSuccessful
Dimension name: RuleSetId
Dimension value: rs-0123456789
Unit: Count
Statistic: Sum
```

**SMTP relay metric example**  
The following values select successfully delivered recipients for one relay.

```
Namespace: AWS/SES/MailManager
Metric name: Delivered
Dimension name: RelayId
Dimension value: rl-0123456789abcdef
Unit: Count
Statistic: Sum
```

The `RuleSetId` dimension value is the identifier returned when you create the rule set. The `RelayId` dimension value is the identifier returned when you create the relay. The metrics do not include rule name, action name, action type, or recipient dimensions. Use rule-set logs to identify these details.

Mail Manager emits `Delivered` and `Rejected` after every selected recipient has a final relay outcome. A delivery-delay notification does not complete the relay action. It waits for a later delivery or failure outcome.

Mail Manager does not emit periodic zero samples. A completed relay action can emit `0` for `Delivered` or `Rejected` when no recipient has that outcome. The SES console rule-set graphs use one-hour periods and display missing periods as `0`. Therefore, a displayed zero can represent either a reported zero or an absent sample.

For information about selecting namespaces and dimensions, see [View available metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/viewing_metrics_with_cloudwatch.html) in the *Amazon CloudWatch User Guide*. For information about `Sum` and other statistics, see [CloudWatch statistics definitions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Statistics-definitions.html).

## Follow rule execution
<a name="eb-rules-monitoring-follow-execution"></a>

Rule-set logs contain the message, rule, selected recipient, and action details for an execution. For the complete field reference, see [Rule set logs – `APPLICATION_LOGS`](eb-logging.md#rule-set-logs). For CloudWatch Logs Insights queries that find one message or failed actions, see [Example CloudWatch Logs Insights queries](eb-logging.md#rule-set-queries).

Query by `message_id`, then read the records in `rule_index` and `action_index` order. Every action record uses the common fields shown in the following example.

```json
{
  "resource_arn": "arn:aws:ses:us-east-1:123456789012:mailmanager-rule-set/rs-0123456789abcdef01234567",
  "event_timestamp": 1763150400000,
  "message_id": "0000llcki1jmushh817gr586f963a5inhkvnh81",
  "rule_set_name": "OrdersRuleSet",
  "rule_name": "ProcessOrders",
  "rule_index": 1,
  "recipients_matched": ["orders@example.com"],
  "action_metadata": {
    "action_name": "ADD_HEADER",
    "action_index": 1,
    "action_status": "SUCCESS"
  }
}
```

**Rule action log examples**  
The `action_metadata` object changes for each action. Each example assumes that the action is first in its rule.

[Add header](eb-rules-actions.md#eb-rules-actions-add-header)  

```json
{
  "action_name": "ADD_HEADER",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

[Replace recipient](eb-rules-actions.md#eb-rules-actions-replace-recipient)  

```json
{
  "action_name": "REPLACE_RECIPIENT",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

[Write to S3](eb-rules-actions.md#eb-rules-actions-write-to-s3)  

```json
{
  "action_name": "WRITE_TO_S3",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

[Archive](eb-rules-actions.md#eb-rules-actions-archive)  

```json
{
  "action_name": "ARCHIVE",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

[Publish to SNS](eb-rules-actions.md#eb-rules-actions-publish-to-sns)  

```json
{
  "action_name": "PUBLISH_TO_SNS",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

[Invoke Lambda function](eb-rules-actions.md#eb-rules-actions-invoke-lambda)  

```json
{
  "action_name": "INVOKE_LAMBDA",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

[Deliver to Q Business](eb-rules-actions.md#eb-rules-actions-deliver-to-q-business)  

```json
{
  "action_name": "DELIVER_TO_AMAZON_Q_BUSINESS",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

[SMTP relay](eb-rules-actions.md#eb-rules-actions-relay)  
An SMTP relay action first records that delivery is in progress.  

```json
{
  "action_name": "RELAY",
  "action_index": 1,
  "action_status": "IN_PROGRESS"
}
```
After every selected recipient has a final outcome, a successful relay records the following object.  

```json
{
  "action_name": "RELAY",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

[Send to internet](eb-rules-actions.md#eb-rules-actions-send)  

```json
{
  "action_name": "SEND",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

[Deliver to WorkMail mailbox](eb-rules-actions.md#eb-rules-actions-deliver-to-mailbox)  

```json
{
  "action_name": "DELIVER_TO_MAILBOX",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

[Drop](eb-rules-actions.md#eb-rules-actions-drop)  

```json
{
  "action_name": "DROP",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

[Bounce](eb-rules-actions.md#eb-rules-actions-bounce)  

```json
{
  "action_name": "BOUNCE",
  "action_index": 1,
  "action_status": "SUCCESS"
}
```

A failed action uses `FAILURE` and can include `action_failure`. For example:

```json
{
  "action_name": "WRITE_TO_S3",
  "action_index": 1,
  "action_status": "FAILURE",
  "action_failure": "Access denied"
}
```

A record with an empty `recipients_matched` value and no `action_metadata` confirms that no recipients remained selected for that rule. The record does not identify which `Conditions` entry failed or which `Unless` entry matched. Compare the message with the rule configuration to identify the cause.

For details about matching, see [How rule condition matching works](eb-rules-conditions.md#eb-rules-conditions-how-matching-works). For action order and behavior, see [How action order works](eb-rules-actions.md#eb-rules-actions-order).

## Troubleshoot rule-set processing
<a name="eb-rules-monitoring-troubleshoot"></a>

### No actions ran
<a name="eb-rules-monitoring-no-actions"></a>

1. Query the rule-set logs by `message_id`.

1. Find the expected rule by `rule_index` or `rule_name`.

1. If `recipients_matched` is empty and `action_metadata` is absent, compare each `Conditions` entry with the message and recipients.

1. Check whether any `Unless` condition matched the recipients that passed the `Conditions` entries.

1. If there is no record for the expected rule, inspect earlier action records for `Drop` or a failed action that uses `ActionFailurePolicy=DROP`.

1. Check whether a Replace recipient action changed the recipient before the expected rule ran.

Every `Conditions` entry must match for a recipient to remain selected. A match on any `Unless` entry skips the current rule's actions for that recipient. For details, see [Rule conditions](eb-rules-conditions.md).

### An action failed
<a name="eb-rules-monitoring-action-failed"></a>

1. Find the record with `action_status` set to `FAILURE`.

1. Read `action_failure` for the reported cause.

1. Use `action_name` and `action_index` to locate the action in the rule.

1. Check that referenced resources still exist and use the expected identifiers.

1. Check the action's execution role and resource permissions.

1. Check the action-specific configuration described in [Rule actions](eb-rules-actions.md).

`ActionFailurePolicy` controls customer configuration errors such as a missing resource or insufficient permission.
+ `CONTINUE` records the failure and continues to the next action with the same selected recipients.
+ `DROP` records the failure and stops further rule-set processing for the selected recipients.

If the action omits `ActionFailurePolicy`, processing uses `CONTINUE`. Service faults and action timeouts use a separate retry or failure path. For details, see [Handling an action failure](eb-rules-actions.md#eb-rules-actions-failure-policy).

### Unexpected recipients were processed
<a name="eb-rules-monitoring-unexpected-recipients"></a>

1. Compare `recipients_matched` with the SMTP envelope recipients.

1. Check whether the rule uses `RECIPIENT`, `TO`, or `CC`.

1. Check every `Unless` condition.

1. Check for an earlier Replace recipient action.

`RECIPIENT` checks each SMTP envelope recipient supplied with the SMTP `RCPT TO` command. `TO` and `CC` check addresses displayed in the message headers. These addresses can differ, including when the message uses a blind carbon copy recipient.

A Replace recipient action changes the SMTP envelope recipient list. Later actions in the current rule use the replacement recipients, and later rules evaluate the updated recipient list. For details, see [Recipient-level and message-level matching](eb-rules-conditions.md#eb-rules-conditions-recipient-message) and [Replace recipient](eb-rules-actions.md#eb-rules-actions-replace-recipient).

### Processing stopped early
<a name="eb-rules-monitoring-stopped-early"></a>

1. Find the last action record for the message.

1. If `action_name` is `DROP`, check `recipients_matched` to identify the recipients whose processing stopped.

1. If the last record has `action_status=FAILURE`, check whether the action uses `ActionFailurePolicy=DROP`.

1. Check whether the action removed every remaining recipient.

1. If neither case applies, check for a service fault or timeout and confirm whether the execution retried.

`Drop` stops later actions and later rules for its selected recipients. Other recipients continue through the rule set. If `Drop` or `ActionFailurePolicy=DROP` removes every remaining recipient, no later action or rule runs. For details, see [Drop](eb-rules-actions.md#eb-rules-actions-drop).

After correcting a condition, action, or resource configuration, update the rule set as described in [Create and manage rule sets](eb-rules-setup.md). For complete working patterns, see [Rule set examples](eb-rules-examples.md).