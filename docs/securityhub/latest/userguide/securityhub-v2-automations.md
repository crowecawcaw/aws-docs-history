# Automations in Security Hub

Security Hub includes features that automatically modify and take action on findings based on your specifications.

Security Hub currently supports the following types of automations:

- **Automation rules** – Automatically update and suppress findings, as well as send findings to ticketing tools, in near real time based on defined criteria.
- **Automated response and remediation** – Create custom Amazon EventBridge rules that define automatic actions to take against specific findings and insights.

Automation rules are helpful when you want to automatically update finding fields in the Open Cybersecurity Schema Framework (OCSF).
For example, you can use an automation rule to update the severity level of findings for resources with a specific tag.
Using the automation rule eliminates the need to manually update the severity level of each finding related to the specific tag.
You can configure automation rules to create tickets in tools like Jira Cloud and ServiceNow when findings match specific attributes.
This allows findings to be created into tickets as soon as they are sent to Security Hub or created in Security Hub.

EventBridge rules are helpful when you want to take actions outside of Security Hub CSPM with regards to specific findings or send specific findings to third-party tools for remediation or additional investigation.
The rules can be used to trigger supported actions, such as invoking an AWS Lambda function or notifying an Amazon Simple Notification Service (Amazon SNS) topic about a specific finding.

Automation rules take effect before EventBridge rules are applied.
That is, automation rules are triggered and update a finding before EventBridge receives the finding.
EventBridge rules then apply to the updated finding.
