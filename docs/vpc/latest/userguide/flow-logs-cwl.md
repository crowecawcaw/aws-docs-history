# Publish flow logs to CloudWatch Logs

Flow logs can publish flow log data directly to Amazon CloudWatch. Amazon CloudWatch is a
comprehensive monitoring and observability service. It collects and tracks metrics,
logs, and event data from various AWS resources, as well as your own applications and
services. CloudWatch provides visibility into resource utilization, application
performance, and operational health, enabling you to detect and respond to system-wide
performance changes and potential issues. With CloudWatch, you can set alarms, visualize
logs and metrics, and automatically react to collect and optimize your cloud resources.
It is an essential tool for ensuring the reliability, availability, and performance of
your cloud-based infrastructure and applications.

When publishing to CloudWatch Logs,
flow log data is published to a log group, and each network interface has a unique
log stream in the log group. Log streams contain flow log records. You can create
multiple flow logs that publish data to the same log group. If the same network
interface is present in one or more flow logs in the same log group, it has one
combined log stream. If you've specified that one flow log should capture rejected
traffic, and the other flow log should capture accepted traffic, then the combined
log stream captures all traffic.

In CloudWatch Logs, the **timestamp** field corresponds to the start time
that's captured in the flow log record. The **ingestionTime** field
indicates the date and time when the flow log record was received by CloudWatch Logs. This
timestamp is later than the end time that's captured in the flow log record.

For more information about CloudWatch Logs, see [Logs sent to CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-CWL "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md#AWS-logs-infrastructure-CWL") in the _Amazon CloudWatch Logs User Guide_.

###### Pricing

Data ingestion and archival charges for vended logs apply when you publish flow
logs to CloudWatch Logs. For more information, open [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/"), select **Logs** and find
**Vended Logs**.

###### Contents

- [IAM role for publishing flow logs to CloudWatch Logs](flow-logs-iam-role.md "flow-logs-iam-role.md")
- [Create a flow log that publishes
  to CloudWatch Logs](flow-logs-cwl-create-flow-log.md "flow-logs-cwl-create-flow-log.md")
- [View flow log records with CloudWatch Logs](view-flow-log-records-cwl.md "view-flow-log-records-cwl.md")
- [Search flow log records](search-flow-log-records-cwl.md "search-flow-log-records-cwl.md")
- [Process flow log records in CloudWatch Logs](process-records-cwl.md "process-records-cwl.md")
