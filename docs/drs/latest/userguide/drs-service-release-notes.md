# AWS Elastic Disaster Recovery Service Release Notes

## April 2025

- AWS Elastic Disaster Recovery is now authorized for Department of Defense Cloud Computing
  Security Requirements Guide Impact Levels 4 and 5 (DoD CC SRG IL4 and IL5)
  in the AWS GovCloud (US-East and US-West) Regions.

## February 2025

- Added support for RHEL 9.5.
- Added ability to add tags to Amazon EBS snapshots.
-

## October 2024

- Added support for Oracle 9.0-9.4.
- You can use AWS Elastic Disaster Recovery with workloads that require
  FedRAMP High categorization level in the AWS GovCloud (US-East and US-West) Regions. Learn more in [Federal Risk and Authorization Management Program](https://aws.amazon.com/compliance/fedramp/ "https://aws.amazon.com/compliance/fedramp/").

## September 2024

- AWS Elastic Disaster Recovery now supports recovery to AWS Local Zones.

## July 2024

- AWS Elastic Disaster Recovery now supports [Flexible Instance Types](flexible-instance-types.md "flexible-instance-types.md").
- [AWS managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  Created managed policy revisions to support FlexibleInstances feature for DRS. The following managed policies were updated:
  - AWSElasticDisasterRecoveryConsoleFullAccess_v2
  - AWSElasticDisasterRecoveryReadOnlyAccess

## May 2024

- AWS Elastic Disaster Recovery now supports protecting Source Servers with up to 60 volumes.

## April 2024

- AWS Elastic Disaster Recovery now supports AWS Outposts. For more information see:
  [Working with AWS DRS and Outposts.](outposts.md "outposts.md")
- [Source Networks](source-networks.md "source-networks.md") –
  Added support for replicating Security Groups with references to other Security Groups.

## January 2024

- [AWS managed policy update](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  Updated AWSElasticDisasterRecoveryServiceRolePolicy and AWSElasticDisasterRecoveryCrossAccountReplicationPolicy policies to support replicating marketplace licenses to launched instances.
- [Source Networks](source-networks.md "source-networks.md") –
  Added support for replicating Security Groups with Prefix Lists.

## November 2023

- AWS Elastic Disaster Recovery is now generally available in the AWS GovCloud (US) Regions.
  This launch gives customers in both the public and commercial sectors, as well as their partners,
  access to AWS DRS capabilities in the AWS GovCloud (US) Regions.
- Introduced disaster recovery drill validation automation for AWS Elastic Disaster Recovery, this allows you to automate
  validations when launching EC2 instances for recovery and drills.
- [AWS managed policy update](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  updated AWSElasticDisasterRecoveryReadOnlyAccess to support describing additional post-launch actions.
- [New AWS managed policy](security-iam-awsmanpol.md "security-iam-awsmanpol.md") – Added
  new policy: AWSElasticDisasterRecoveryConsoleFullAccess_v2.
- [AWS managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  Created new revisions to support DRS in AWS GovCloud and added Statement ID (SID) to managed policy
  statements. The following managed policies were updated:
  - AWSElasticDisasterRecoveryAgentPolicy
  - AWSElasticDisasterRecoveryAgentInstallationPolicy
  - AWSElasticDisasterRecoveryEc2InstancePolicy
  - AWSElasticDisasterRecoveryConsoleFullAccess
  - AWSElasticDisasterRecoveryLaunchActionsPolicy
  - AWSElasticDisasterRecoveryNetworkReplicationPolicy
  - AWSElasticDisasterRecoveryRecoveryInstancePolicy
  - AWSElasticDisasterRecoveryServiceRolePolicy
  - AWSElasticDisasterRecoveryConversionServerPolicy
  - AWSElasticDisasterRecoveryFailbackPolicy
  - AWSElasticDisasterRecoveryFailbackInstallationPolicy
  - AWSElasticDisasterRecoveryStagingAccountPolicy_v2
  - AWSElasticDisasterRecoveryStagingAccountPolicy
  - AWSElasticDisasterRecoveryReplicationServerPolicy

- [New revision of AWSElasticDisasterRecoveryCrossAccountReplicationPolicy](security-iam-awsmanpol-AWSElasticDisasterRecoveryCrossAccountReplicationPolicy.md "security-iam-awsmanpol-AWSElasticDisasterRecoveryCrossAccountReplicationPolicy.md") policy to support DRS in GovCloud

## October 2023

- Introduced a new feature: Recover into existing instance, allowing you to set an existing EC2 instance as the target of a drill, recovery or failback launch, instead of launching a new instance.
- [AWS managed policy update](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  Updated policies AWSElasticDisasterRecoveryConsoleFullAccess and AWSElasticDisasterRecoveryLaunchActionsPolicy to support launching into existing instance.

## September 2023

- Introduced a new feature: [Post-launch actions framework](post-launch-action-settings-overview.md "post-launch-action-settings-overview.md") for automating any action needed to be performed on recovery instances after launch.
- Service launch in Israel (Tel Aviv) Region.
- [AWS managed policy update](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  added policies [AWSElasticDisasterRecoveryRecoveryInstancePolicy](https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2Fservice-role%2FAWSElasticDisasterRecoveryRecoveryInstancePolicy "https://us-east-1.console.aws.amazon.com/iamv2/home?region=us-east-1#/policies/details/arn%3Aaws%3Aiam%3A%3Aaws%3Apolicy%2Fservice-role%2FAWSElasticDisasterRecoveryRecoveryInstancePolicy") and AWSElasticDisasterRecoveryLaunchActionsPolicy to support post-launch actions.

## August 2023

- Added support for Amazon Linux 2023.
- [Source Networks](source-networks.md "source-networks.md") –
  Added support for replicating Route Tables.

## July 2023

- Service launch in the following regions: Europe (Zurich), Europe (Spain),
  Asia Pacific (Hyderabad), Australia (Melbourne), and Middle East (UAE) regions.
- Introduced a new feature: In-AWS Right Sizing,
  allowing you to easily replicate your EC2 instance and EBS volume types between AWS regions.

## June 2023

- Introduced a new feature: [Trusted accounts](trusted-accounts.md "trusted-accounts.md"), allowing to quickly create roles
  for multiple accounts and providing visibility into existing permissions.
- [AWS managed policy update](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  updated AWSElasticDisasterRecoveryAgentInstallationPolicy to support network replication and recovery.

## May 2023

- Introduced a new feature: [Network replication configurations](source-networks.md "source-networks.md"), allowing you to
  easily replicate your existing source network configurations, saving time and resources
  and preventing security risks.
- [New AWS managed policy](security-iam-awsmanpol.md "security-iam-awsmanpol.md") – Added
  new policies: AWSElasticDisasterRecoveryCrossAccountReplicationPolicy policy and
  AWSElasticDisasterRecoveryNetworkReplicationPolicy policy.
- [AWS managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  Updated the AWSElasticDisasterRecoveryRecoveryInstancePolicy policy, the
  AWSElasticDisasterRecoveryEc2InstancePolicy policy, the
  AWSElasticDisasterRecoveryAgentPolicy policy, the
  AWSElasticDisasterRecoveryServiceRolePolicy policy, and the
  AWSElasticDisasterRecoveryConsoleFullAccess policy.

## April 2023

- Introducing a new feature: Launch settings management, allowing to configure default launch settings
  that apply to newly add source servers and the ability to update multiple servers’ settings.
- [AWS managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  AWSElasticDisasterRecoveryAgentPolicy and
  AWSElasticDisasterRecoveryConsoleFullAccess.

## March 2023

- Introduced a new feature: automated replication of new disks
  Introduced a new feature: support for Oracle ASM Filter Driver

## February 2023

- Introduced a new feature: MAP 2.0 Auto Tagging

## December 2022

- [New AWS managed policy](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  Added the AWSElasticDisasterRecoveryStagingAccountPolicy_v2 policy.

## November 2022

- Added support for cross-Region failback and cross-Availability-Zone recovery.
  Learn more about [cross-Region
  failback](failback-failover-region-region.md "failback-failover-region-region.md") and [cross-Availability-Zone recovery](failback-failover-cross-availability-zone-failback.md "failback-failover-cross-availability-zone-failback.md").
- [AWS managed policy update](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  updated AWSElasticDisasterRecoveryAgentInstallationPolicy for Replication Agent
  reinstallation on recovery instance.

## October 2022

- [AWS managed policy update](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  AWSElasticDisasterRecoveryRecoveryInstancePolicy.

## September 2022

- Service launch in Asia Pacific (Jakarta) Region.

## June 2022

- Service launch in the following regions: US West (N. California), Africa (Cape
  Town), Asia Pacific (Hong Kong), Asia Pacific (Mumbai), Asia Pacific (Osaka),
  Asia Pacific (Seoul), Canada (Central), Europe (Milan), Europe (Paris), Europe
  (Stockholm), Middle East (Bahrain), and South America (São Paulo).
- [AWS managed policy update](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  Updated several policies: AWSElasticDisasterRecoveryAgentInstallationPolicy, AWSElasticDisasterRecoveryFailbackInstallationPolicy, AWSElasticDisasterRecoveryServiceRolePolicy, and AWSElasticDisasterRecoveryReplicationServerPolicy.

## May 2022

- [AWS managed policy update](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  Updates the AWSElasticDisasterRecoveryConsoleFullAccess policy and the AWSElasticDisasterRecoveryReadOnlyAccess policy.

## April 2022

- [AWS managed policy update](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  Updates the AWSElasticDisasterRecoveryAgentPolicy policy.

## March 2022

- Added support for no rescan for all Windows operating systems and certain Linux operating
  systems.
  [Learn more about the no-rescan feature.](Agent-Related-FAQ.md#agent-no-rescan "Agent-Related-FAQ.md#agent-no-rescan")

## February 2022

- [New AWS managed policy](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  Added the AWSElasticDisasterRecoveryStagingAccountPolicy.

## January 2022

- Added support for failback automation.

## November 2021

- [New AWS managed policy](security-iam-awsmanpol.md "security-iam-awsmanpol.md") –
  Added several policies:
  - AWSElasticDisasterRecoveryStagingAccountPolicy

  - AWSElasticDisasterRecoveryAgentPolicy

  - AWSElasticDisasterRecoveryConversionServerPolicy

  - AWSElasticDisasterRecoveryFailbackPolicy

  - AWSElasticDisasterRecoveryFailbackInstallationPolicy

  - AWSElasticDisasterRecoveryConsoleFullAccess

  - AWSElasticDisasterRecoveryReplicationServerPolicy

  - AWSElasticDisasterRecoveryRecoveryInstancePolicy

  - AWSElasticDisasterRecoveryServiceRolePolicy
