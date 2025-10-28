# Monitoring threats with Amazon GuardDuty RDS Protection for Amazon Aurora

Amazon GuardDuty is a threat detection service that helps protect your accounts, containers, workloads, and
the data within your AWS environment. Using machine learning (ML) models, and anomaly and threat
detection capabilities, GuardDuty continuously monitors different log sources and runtime activity
to identify and prioritize potential security risks and malicious activities in your environment.

GuardDuty RDS Protection analyzes and profiles login events for potential access threats to your Amazon Aurora
databases. When you turn on RDS Protection, GuardDuty consumes RDS login events from your Aurora
databases. RDS Protection monitors these events and profiles them for potential insider threats or
external actors.

For more information about enabling GuardDuty RDS Protection, see [GuardDuty RDS Protection](../../../guardduty/latest/ug/rds-protection.md "../../../guardduty/latest/ug/rds-protection.md") in the _Amazon GuardDuty User Guide_.

When RDS Protection detects a potential threat, such as an unusual pattern in
successful or failed login attempts, GuardDuty generates a new finding with details about the
potentially compromised database. You can view the finding details in the finding summary section in the Amazon GuardDuty console. The finding details vary based on the finding type.
The primary details, resource type and resource role, determine the kind of information available for any finding.
For more information about the commonly available details for findings and the finding types, see [Finding details](../../../guardduty/latest/ug/guardduty_findings-summary.md "../../../guardduty/latest/ug/guardduty_findings-summary.md") and
[GuardDuty RDS Protection finding types](../../../guardduty/latest/ug/findings-rds-protection.md "../../../guardduty/latest/ug/findings-rds-protection.md")
respectively in the _Amazon GuardDuty User Guide_.

You can turn the RDS Protection feature on or off for any AWS account in any AWS Region where
this feature is available. When RDS Protection isn't enabled, GuardDuty doesn't detect potentially
compromised Aurora databases or provide details of the compromise.

An existing GuardDuty account can
enable RDS Protection with a 30-day trial period. For a new GuardDuty account, RDS Protection is
already enabled and included in the 30-day free trial period. For more information, see
[Estimating
GuardDuty cost](../../../guardduty/latest/ug/monitoring_costs.md "../../../guardduty/latest/ug/monitoring_costs.md") in the _Amazon GuardDuty User Guide_.

For information about the AWS Regions where GuardDuty doesn't yet support RDS Protection, see [Region-specific feature availability](../../../guardduty/latest/ug/guardduty_regions.md#gd-regional-feature-availability "../../../guardduty/latest/ug/guardduty_regions.md#gd-regional-feature-availability")
in the _Amazon GuardDuty User Guide_.

For information about the Aurora database versions that GuardDuty RDS Protection supports, see [Supported Amazon Aurora, Amazon RDS, and Aurora Limitless databases](../../../guardduty/latest/ug/rds-protection.md#rds-pro-supported-db "../../../guardduty/latest/ug/rds-protection.md#rds-pro-supported-db") in the _Amazon GuardDuty User Guide_.
