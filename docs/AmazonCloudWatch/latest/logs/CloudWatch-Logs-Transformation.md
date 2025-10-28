# Transform logs during ingestion

With logs transformation and enrichment, you can normalize all your logs in a consistent
and context-rich format at the time of ingestion into CloudWatch Logs. You can add structure to your
logs by using pre-configured templates for common AWS services such as AWS WAF and
Amazon Route 53, or build custom transformers with native parsers such as [Grok](CloudWatch-Logs-Transformation-Processors.md#CloudWatch-Logs-Transformation-Grok "CloudWatch-Logs-Transformation-Processors.md#CloudWatch-Logs-Transformation-Grok"). You can also rename existing
attributes and add additional metadata to your logs such as account ID, and Region.

Log transformation helps simplify and shorten your log queries across your applications,
and helps simplify creating alerts on your logs. This feature provides transformation for
common log types with out-of-the-box transformation templates for major AWS log sources
like VPC Flow logs, Route 53, and Amazon RDS for PostgreSQL. You can use pre-configured
transformation templates or create custom transformers to suit your needs.

Log transformation helps you manage logs emitted from various sources that vary widely in
format and attribute names.

After you create a transformer, ingested log events are converted and stored in a standard
format. You can leverage these transformed logs to accelerate your analytics experience with
the following features:

- [Field indexes](CloudWatchLogs-Field-Indexing.md "CloudWatchLogs-Field-Indexing.md")
- [CloudWatch Logs Insights discovered fields](CWL_AnalyzeLogData-discoverable-fields.md "CWL_AnalyzeLogData-discoverable-fields.md")
- Flexibility in alarming using [metric filters](MonitoringLogData.md "MonitoringLogData.md")
- Forwarding via [subscription filters](Subscriptions.md "Subscriptions.md")
- Creating metric data from log events with [Contributor Insights](../monitoring/ContributorInsights.md "../monitoring/ContributorInsights.md"), where you can choose to have the Contributor Insights rule
  evaluate log events either before or after they are transformed.
  Transformations happen only during log ingestion. You can't transform log events that have
  already been ingested. Transformations are not reversible. Both original and transformed
  logs are stored in CloudWatch Logs with the same retention policy. Log transformation and enrichment
  capability is included in the existing Standard log class ingestion price. Log storage costs
  will be based on log size after transformation, which might exceed the original log
  volume.

###### Important

After log events have been transformed, you must use CloudWatch Logs Insights queries to view
the transformed versions of the logs. The [GetLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.md") and [FilterLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.md") actions return only the original versions of the log events,
before they were transformed.

In addition to transforming into different formats, you can also enrich your logs with
additional context, such as account ID, Region, and keyword. These are extracted from the
log group name and from static keywords.

Log transformation helps you with logs emitted from various sources that vary widely in
format and attribute names.

Log transformation and enrichment is supported only for log groups in the Standard log
class.

You can create transformers for individual log groups, and you can also create
account-level transformers that apply to all or many log groups in your account. If a log
group has a log group-level transformer, that transformer overrides any account-level
transformer that would otherwise apply to that log group.

###### Topics

- [Create and manage log
  transformers](CloudWatch-Logs-Transformation-Create.md "CloudWatch-Logs-Transformation-Create.md")
- [Processors that you can
  use](CloudWatch-Logs-Transformation-Processors.md "CloudWatch-Logs-Transformation-Processors.md")
- [Transformation metrics and errors](Transformation-Errors-Metrics.md "Transformation-Errors-Metrics.md")
