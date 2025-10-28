# Managing Amazon GuardDuty findings

GuardDuty offers several important features to help you sort, store, and manage your findings.
These features will help you tailor findings to your specific environment, reduce noise from
low value findings, and help you focus on threats to your unique AWS environment. Review
the topics on this page to understand how you can use these features to increase the value
of security findings in your environment.

**Topics:**

[Summary dashboard in Amazon GuardDuty](guardduty-summary.md "guardduty-summary.md")

Learn about the components of the summary dashboard available in the GuardDuty
console.

[Filtering findings in GuardDuty](guardduty_filter-findings.md "guardduty_filter-findings.md")

Learn how to filter GuardDuty findings based on the criteria you specify.

[Suppression rules in GuardDuty](findings_suppression-rule.md "findings_suppression-rule.md")

Learn how to automatically filter the findings GuardDuty alerts you to through
suppression rules. Suppression rules automatically archive findings based on
filters.

[Customizing threat detection with entity lists and
IP address lists](guardduty_upload-lists.md "guardduty_upload-lists.md")

Customize the GuardDuty monitoring scope using IP Lists and Threat Lists based on
publicly-routable IP addresses. Trusted IP lists prevent non-DNS findings from
being generated from IP's you consider trusted, while Threat Intel Lists will
cause GuardDuty to alert you of activity from user-defined IPs.

[Exporting generated findings to
Amazon S3](guardduty_exportfindings.md "guardduty_exportfindings.md")

Export the generated findings to an Amazon S3 bucket so that you can maintain
records past the 90-day findings retention period in GuardDuty. Use this historical
data to track potential suspicious activities in your account and evaluate
whether the recommended remediation steps were successful.

[Processing GuardDuty findings with
Amazon EventBridge](guardduty_findings_eventbridge.md "guardduty_findings_eventbridge.md")

Set up automatic notifications for GuardDuty findings through Amazon EventBridge events. You
can also automate other tasks through EventBridge to help you respond to findings.

[Understanding CloudWatch Logs and reasons for
skipping resources during Malware Protection for EC2 scan](malware-protection-auditing-scan-logs.md "malware-protection-auditing-scan-logs.md")

Learn how you can audit the CloudWatch Logs for GuardDuty Malware Protection for EC2 and what are the reasons
because of which your impacted Amazon EC2 instance or Amazon EBS volumes may have been
skipped during the scanning process.

[Reporting false positives in Malware Protection for EC2](malware-protection-false-positives.md "malware-protection-false-positives.md")

Learn how you can report potential false positive threat detections in
Malware Protection for S3.

[Reporting S3 object scan
result as false positive in Malware Protection for S3](report-malware-protection-s3-false-positives.md "report-malware-protection-s3-false-positives.md")

Learn how you can report potential false positive threat detections in
Malware Protection for S3.
