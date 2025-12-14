# Setup proactive response and alert triaging workflows

Proactive response and alert triaging workflow is an optional feature to enable within your organization for
monitoring enabled security services. Select the toggle next to the feature to enable.

If you experience any onboarding issues, then please
[create an AWS Support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case") for additional assistance. Make sure to include details including the AWS account ID and
any errors you may have seen during the setup process.

**Proactive response and alert triaging:** AWS Security Incident Response monitors and investigates
alerts generated from Amazon GuardDuty and Security Hub CSPM integrations. To use this feature, [Amazon GuardDuty must be enabled](../../../guardduty/latest/ug/guardduty_settingup.md "../../../guardduty/latest/ug/guardduty_settingup.md").
AWS Security Incident Response triages low-priority alerts with service automation
so your team can focus on the most critical issues. For additional information on how AWS Security Incident Response works with
Amazon GuardDuty and AWS Security Hub CSPM, please review the [Detect and Analyze](detect-and-analyze.md "detect-and-analyze.md") section of the user guide.

This feature enables AWS Security Incident Response to monitor and investigate findings across all covered accounts
and active supported AWS Regions in your organization. To facilitate this functionality, AWS Security Incident Response automatically creates a
service-linked role in all covered member accounts within your AWS Organizations.
However, for the management account, you must manually create the service-linked role to enable monitoring.

_The service cannot create the service-linked role in the management account. You must create this role manually
in the management account by [working with AWS CloudFormation stack sets](working-with-stacksets.md "working-with-stacksets.md")._

**Containment:** In the event of a security incident, AWS Security Incident Response can execute containment actions
to quickly mitigate the impact, such as isolating compromised hosts or rotating credentials. Security Incident Response does not enable
containment capabilities by default. To execute these containment actions, you must first grant the necessary permissions to the service.
This can be done by deploying an [AWS CloudFormation
StackSet](working-with-stacksets.md "working-with-stacksets.md"), which creates the required roles.
