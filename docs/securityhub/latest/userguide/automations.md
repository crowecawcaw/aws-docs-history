# Automatically modifying and acting on findings in

Security Hub CSPM

AWS Security Hub CSPM has features that automatically modify and take action on findings based on your
specifications.

Security Hub CSPM currently supports two types of automations:

- **Automation rules** – Automatically update
  and suppress findings in near real time based on criteria that you define.
- **Automated response and remediation** –
  Create custom Amazon EventBridge rules that define automatic actions to take against specific
  findings and insights.
  Automation rules are helpful when you want to automatically update finding fields in the AWS Security Finding Format (ASFF). For example,
  you can use an automation rule to update the severity level or workflow status of findings from a specific third-party integrations.
  Using the automation rule eliminates the need to manually update the severity level or workflow status of each finding from this
  third-party product.

EventBridge rules are helpful when you want to take actions outside of Security Hub CSPM with regards to specific findings or send specific findings to third-party tools for remediation or additional
investigation. The rules can be used to trigger supported actions, such as invoking an AWS Lambda function or notifying an Amazon Simple Notification Service (Amazon SNS)
topic about a specific finding.

Automation rules take effect before EventBridge rules are applied. That is, automation rules are triggered and update a finding before
EventBridge receives the finding. EventBridge rules then apply to the updated finding.

When setting up automations for security controls, we recommend filtering based on control ID rather than title or description. Whereas Security Hub CSPM
occasionally updates control titles and descriptions, control IDs stay the same.

###### Topics

- [Understanding automation rules in Security Hub CSPM](automation-rules.md "automation-rules.md")
- [Using EventBridge for automated response and remediation](securityhub-cloudwatch-events.md "securityhub-cloudwatch-events.md")
