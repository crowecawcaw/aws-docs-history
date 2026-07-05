# Onboarding prerequisites

The only required prerequisite is enabling [AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md") with **All Features** enabled. Consolidated billing alone is not sufficient.

###### Note

The AWS Identity and Access Management (IAM) principal used to sign in to the delegated administrator account during enablement
must have `AdministratorAccess` permissions. Without these permissions, the
enablement process fails.

## Detection services

While not required, we strongly recommend enabling Amazon GuardDuty and AWS Security Hub CSPM across all accounts and active AWS Regions. These detection services provide the signal that AWS Security Incident Response monitors on your behalf. Without them, there are no findings to ingest and no data to triage proactively. It then becomes your responsibility to detect issues and raise them through a case. Additionally, the ability to investigate and assist is significantly reduced without detection tool data, since these tools are critical to understanding what's happening in your accounts.

We also strongly recommend enabling AWS CloudTrail logging across all accounts. During investigations, the Security Incident Response Engineering team relies on CloudTrail data to analyze activity, trace actions, and identify anomalous patterns in your accounts. Without CloudTrail logs available, the ability to conduct thorough investigations is limited.

You don't need to enable GuardDuty or Security Hub CSPM before activating AWS Security Incident Response. You can enable these detection services at any time after onboarding, and AWS Security Incident Response begins ingesting findings as soon as they're available.

###### Note

AWS Security Incident Response only triages threat detection findings. Security posture or compliance findings (such as misconfiguration alerts or benchmark violations) aren't triaged because they represent a state about your environment rather than an active threat requiring investigation.

### GuardDuty and AWS Security Incident Response

We recommend enabling GuardDuty in all accounts and all AWS Regions, including Regions where you have no active workloads. Attackers commonly target unused Regions and dormant accounts to spin up expensive resources or gain lateral access without being detected. A common misconception is that you only need to monitor the Regions and production accounts you actively use. However, this is a key vector that attackers exploit.

GuardDuty doesn't incur charges in Regions with no activity, so enabling it everywhere carries no cost penalty for quiet Regions. If unauthorized activity occurs in an unused Region, GuardDuty gives immediate visibility to act on your behalf.

To enable GuardDuty across your organization, see [Setting up GuardDuty](../../../guardduty/latest/ug/guardduty_settingup.md "../../../guardduty/latest/ug/guardduty_settingup.md").

### Third-party integration

You don't need to enable Security Hub CSPM standards or controls for AWS Security Incident Response. Security Hub CSPM is used only as a conduit to ingest findings from third-party endpoint detection and response (EDR) vendors. The controls and standards are optional from the AWS Security Incident Response perspective, though you can keep them enabled if they provide value for your own compliance and posture management needs.

When third-party findings are ingested through Security Hub CSPM, AWS Security Incident Response auto-triages them for proactive case creation. To set up a third-party EDR integration, follow the steps in the [Security Hub CSPM integrations documentation](../../../securityhub/latest/userguide/securityhub-partner-providers.md "../../../securityhub/latest/userguide/securityhub-partner-providers.md").

For supported third-party tools, see [Detect and analyze](detect-and-analyze.md "detect-and-analyze.md"). If your third-party tool integrates with Security Hub CSPM but isn't listed, AWS Security Incident Response can still ingest those findings on a best-effort basis while support is evaluated. To discuss support for additional tools, open an AWS Support case or contact your TAM.

## Findings created before onboarding

###### Important

AWS Security Incident Response can only ingest findings generated after you complete onboarding. Findings that were created before activation are not retroactively ingested. If you have existing findings you want investigated, raise them through a case after onboarding is complete.
