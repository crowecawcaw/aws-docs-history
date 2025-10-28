# Changing the monitoring configuration for an AMS account

You can change your baseline monitoring configuration for Amazon EC2 resources. For the alerts that can be configured, see
[Alerts from baseline monitoring in AMS](monitoring-default-metrics.md "monitoring-default-metrics.md").
You can change the alarm definition, alarm destination, or opt-out of the alarm notification for the
baseline monitors so that the alerts meet your application’s operational requirements.
You can request any or all of the previously mentioned changes by
submitting a Management | Other | Other | Update CT (ct-0xdawir96cy7k) with the following details.

- Instance IDs [optional, if not mentioned, all instances in the account are in-scope]
- CloudWatch metric name, for example, CPU utilization / swap free / IOwait
- Target - email ID / phone number for SMS / SNS topic
  To learn more about the type of changes you can request in the baseline monitoring configuration,

see the [Amazon CloudWatch Documentation](../../../cloudwatch.md "../../../cloudwatch.md").
