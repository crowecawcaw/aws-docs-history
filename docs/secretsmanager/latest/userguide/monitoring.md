# Monitor AWS Secrets Manager secrets

AWS provides monitoring tools to watch Secrets Manager secrets, report when something
is wrong, and take automatic actions when appropriate. You can use the logs if you need to
investigate any unexpected usage or change, and then you can roll back unwanted changes.
You can also set automated checks for inappropriate usage of secrets and any attempts to
delete secrets.

###### Topics

- [Log with AWS CloudTrail](monitoring-cloudtrail.md "monitoring-cloudtrail.md")
- [Monitor with CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Match Secrets Manager events with EventBridge](monitoring-eventbridge.md "monitoring-eventbridge.md")
- [Monitor secrets scheduled for
  deletion](monitoring_cloudwatch_deleted-secrets.md "monitoring_cloudwatch_deleted-secrets.md")
- [Monitor secrets for compliance](configuring-awsconfig-rules.md "configuring-awsconfig-rules.md")
- [Monitor Secrets Manager costs](monitor-secretsmanager-costs.md "monitor-secretsmanager-costs.md")
- [Detect threats with GuardDuty](monitoring-guardduty.md "monitoring-guardduty.md")
