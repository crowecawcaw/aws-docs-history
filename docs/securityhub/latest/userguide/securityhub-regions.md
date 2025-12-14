# Regional limits for Security Hub CSPM

Some AWS Security Hub CSPM features are available in only certain AWS Regions. The following
sections specify these Regional limits. For a complete list of all the Regions where Security Hub CSPM
is currently available, see [AWS Security Hub endpoints and quotas](../../../general/latest/gr/sechub.md "../../../general/latest/gr/sechub.md") in the
_AWS General Reference_.

## Cross-Region

aggregation restrictions

In AWS GovCloud (US) Regions, [cross-Region
aggregation](finding-aggregation.md "finding-aggregation.md") is available for findings, finding updates, and insights across
AWS GovCloud (US) Regions only. Specifically, you can aggregate findings, finding updates,
and insights only between the AWS GovCloud (US-East) and AWS GovCloud (US-West)
Regions.

In the China Regions, cross-Region aggregation is available for findings, finding
updates, and insights across the China Regions only. Specifically, you can aggregate
findings, finding updates, and insights only between the China (Beijing) and
China (Ningxia) Regions.

You can't use a Region that's disabled by default as your aggregation Region. For a
list of Regions that are disabled by default, see [Enable
or disable AWS Regions in your account](../../../accounts/latest/reference/manage-acct-regions.md#rande-manage-enable "../../../accounts/latest/reference/manage-acct-regions.md#rande-manage-enable") in the _AWS Account Management Reference Guide_.

## Availability of integrations

by Region

Some integrations aren't available in all AWS Regions. On the Security Hub CSPM console, an
integration doesn't appear on the **Integrations** page if it isn't
available in the Region that you're currently signed in to.

### Integrations

supported in the China (Beijing) and China (Ningxia) Regions

In the China (Beijing) and China (Ningxia) Regions, Security Hub CSPM supports
only the following [integrations with
AWS services](securityhub-internal-providers.md "securityhub-internal-providers.md"):

- AWS Firewall Manager
- Amazon GuardDuty
- AWS Identity and Access Management Access Analyzer
- Amazon Inspector
- AWS IoT Device Defender
- AWS Systems Manager Explorer
- AWS Systems Manager OpsCenter
- AWS Systems Manager Patch Manager

In the China (Beijing) and China (Ningxia) Regions, Security Hub CSPM supports
only the following [third-party
integrations](securityhub-partner-providers.md "securityhub-partner-providers.md"):

- Cloud Custodian
- FireEye Helix
- Helecloud
- IBM QRadar
- PagerDuty
- Palo Alto Networks Cortex XSOAR
- Palo Alto Networks VM-Series
- Prowler
- RSA Archer
- Splunk Enterprise
- Splunk Phantom
- ThreatModeler

### Integrations

supported in the AWS GovCloud (US-East) and AWS GovCloud (US-West)
Regions

In the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions, Security Hub CSPM supports
only the following [integrations with
AWS services](securityhub-internal-providers.md "securityhub-internal-providers.md"):

- AWS Config
- Amazon Detective
- AWS Firewall Manager
- Amazon GuardDuty
- AWS Health
- IAM Access Analyzer
- Amazon Inspector
- AWS IoT Device Defender

In the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions, Security Hub CSPM supports
only the following [third-party
integrations](securityhub-partner-providers.md "securityhub-partner-providers.md"):

- Atlassian Jira Service Management
- Atlassian Jira Service Management Cloud
- Atlassian OpsGenie
- Caveonix Cloud
- Cloud Custodian
- Cloud Storage Security Antivirus for Amazon S3
- CrowdStrike Falcon
- FireEye Helix
- Forcepoint CASB
- Forcepoint DLP
- Forcepoint NGFW
- Fugue
- Kion
- MicroFocus ArcSight
- NETSCOUT Cyber Investigator
- PagerDuty
- Palo Alto Networks – Prisma Cloud Compute
- Palo Alto Networks – Prisma Cloud Enterprise
- Palo Alto Networks – VM-Series (available only in
  AWS GovCloud (US-West))
- Prowler
- Rackspace Technology – Cloud Native Security
- Rapid7 InsightConnect
- RSA Archer
- ServiceNow ITSM
- Slack
- ThreatModeler
- Vectra AI Cognito Detect

## Availability of standards by

Region

The [AWS Control Tower
service-managed standard](service-managed-standard-aws-control-tower.md "service-managed-standard-aws-control-tower.md") is available only in AWS Regions that AWS Control Tower
supports. For a list of Regions that AWS Control Tower currently
supports, see [How AWS Regions Work With
AWS Control Tower](../../../controltower/latest/userguide/region-how.md "../../../controltower/latest/userguide/region-how.md") in the _AWS Control Tower User Guide_.

The [AWS Resource Tagging standard](standards-tagging.md "standards-tagging.md") isn't
available in the Asia Pacific (Taipei) Region.

Other security standards are available in all the Regions where Security Hub CSPM is currently available.

## Availability of controls by

Region

Some Security Hub CSPM controls aren't available in all AWS Regions. For a list of controls that aren't available in each Region,
see [Regional limits on Security Hub CSPM controls](regions-controls.md "regions-controls.md").

On the Security Hub CSPM console, a control doesn't appear in the list of controls if it isn't
available in the Region that you're currently signed in to. The exception is an
aggregation Region. If you set an aggregation Region and sign in to that Region, the
console shows controls that are available in the aggregation Region or one or more
linked Regions.
