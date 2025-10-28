# AOSOPS03-BP01 Establish alarms for OpenSearch Service domain

Set up alerts to receive timely notifications about potential issues
that may impact performance or availability.

**Level of risk exposed if this best practice
is not established:** High

**Desired outcome**: Receive timely,
relevant, and actionable alerts for rapid identification and
mitigation of potential issues, especially when KPI outcomes are at
risk.

**Benefits of establishing this best
practice:**

- **Prompt notification:**
  Configure OpenSearch Service domains with recommended Amazon CloudWatch alarms to receive notifications when critical
  conditions occur, such as a cluster health status remaining in a
  critical state for more than one minute.
- **Enable corrective action:** By
  implementing automatic actions, such as sending email
  notifications, you can take corrective action to address issues
  before they impact your OpenSearch Service domain's performance
  or availability.
- **Improve domain reliability:**
  Regular monitoring and notification through CloudWatch alarms
  helps your OpenSearch Service domain to remain reliable,
  available, and performing optimally, meeting the requirements of
  your users and applications.

## Implementation guidance

It's highly recommended to implement the
[Recommended
Amazon CloudWatch alarms for your Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/cloudwatch-alarms.md "../../../opensearch-service/latest/developerguide/cloudwatch-alarms.md")
domains.

Use alarms to initiate automated actions when specific conditions
are met, such as when a metric exceeds a predetermined threshold
over a set duration. For example, if your cluster health status
remains in a critical state (indicated by a red status) for more
than one minute, you can configure your monitoring tool to send an
email notification, which prepares you to take swift corrective
action.

To set up essential Amazon CloudWatch alarms for your OpenSearch Service domain, follow a multi-step process that
involves two key components:

- **Understanding alarms:**
  Familiarize yourself with the recommended alarms and their
  critical thresholds to stay aware of the most significant
  metrics to monitor.
  [Recommended
  CloudWatch alarms for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/cloudwatch-alarms.md "../../../opensearch-service/latest/developerguide/cloudwatch-alarms.md") details
  the recommended alarms and their thresholds.
- **Creating alarms:** Follow the
  instructions in
  [Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md") and
  [How
  do I use CloudWatch alarms to monitor my OpenSearch Service
  cluster](https://repost.aws/knowledge-center/opensearch-cloudwatch-alarms "https://repost.aws/knowledge-center/opensearch-cloudwatch-alarms") to create alarms that meet your specific needs.

## Resources

- [Recommended
  CloudWatch alarms for Amazon OpenSearch Service](../../../opensearch-service/latest/developerguide/cloudwatch-alarms.md "../../../opensearch-service/latest/developerguide/cloudwatch-alarms.md")
- [Amazon CloudWatch alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md")
- [How
  do I use CloudWatch alarms to monitor my OpenSearch Service
  cluster](https://repost.aws/knowledge-center/opensearch-cloudwatch-alarms "https://repost.aws/knowledge-center/opensearch-cloudwatch-alarms")
