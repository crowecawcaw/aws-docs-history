NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Release notes

## September 2025

- Specify your operating system licensing approach (BYOL / LI) and tenancy when importing inventory. Learn more in [Import parameters](import-main.md#import-parameters "import-main.md#import-parameters").

## August 2025

- The post-launch actions _Enable Refactor Spaces_ and _App2Container for Replatforming_ are no longer supported.

## July 2025

- You can now reset launch template values during the inventory import process.
  Learn more in [Editing your configuration](configuration-editing.md "configuration-editing.md").
- Service launch in these regions: _Asia Pacific (Thailand)_ ,
  and _Asia Pacific (Malaysia)_ Regions.

## April 2025

- AWS Application Migration Service is now authorized for Department of
  Defense Cloud Computing Security Requirements Guide Impact Levels 4 and 5 (DoD CC SRG IL4 and IL5) in the
  AWS GovCloud (US-East and US-West) Regions. Learn more in [AWS Application Migration Service authorized for DoD Impact Level 4 and 5](https://aws.amazon.com/about-aws/whats-new/2025/04/aws-application-migration-service-dod-impact-level-4-5/ "https://aws.amazon.com/about-aws/whats-new/2025/04/aws-application-migration-service-dod-impact-level-4-5/")

## February 2025

- Enabled tagging of network interfaces during RunInstances. 

Updated the AWSApplicationMigrationFullAccess policy to support tagging network interface during runInstance.
If you’re managing your own policy, you must include a statement allowing `ec2:CreateTags` on `arn:aws:ec2:*:*:network-interface/*`  
 with a condition of `“ec2:CreateAction”: [“RunInstances”]`.

- Added support for RHEL 9.5.

## January 2025

- Enabled tagging of network interfaces during RunInstances.
- Changed the definition of the **mgn:region**
  import parameter, used in the [**Import** feature](import-main.md "import-main.md").
  Providing a region other than the console region results in an error.

## October 2024

- Added support for Oracle 9.0-9.4.

## September 2024

- Introduced a new predefined post-launch action: TrendMicro. [Learn more about the TrendMicro
  action](predefined-post-launch-actions.md#predefined-trend-micro "predefined-post-launch-actions.md#predefined-trend-micro").

## August 2024

- Added support for updating AWS credentials for agentless replication. [Learn more about updating
  vCenter & AWS credentials for agentless replication](updating-vcenter-or-aws-credentials.md "updating-vcenter-or-aws-credentials.md").

## July 2024

- Introduced a new predefined post-launch action: New Relic. [Learn more about the New Relic
  action](predefined-post-launch-actions.md#predefined-new-relic "predefined-post-launch-actions.md#predefined-new-relic").
- You can use AWS Application Migration Service with workloads that require
  FedRAMP High categorization level in the AWS GovCloud (US-East and US-West) Regions. Learn more in [AWS Application Migration Service achieves FedRAMP High authorization](https://aws.amazon.com/about-aws/whats-new/2024/07/aws-application-migration-fedramp-high-authorization/ "https://aws.amazon.com/about-aws/whats-new/2024/07/aws-application-migration-fedramp-high-authorization/")

## June 2024

- Added support for deploying AWS Replication Agent on a secured network in the Europe (Spain), Europe (Zurich), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Osaka) and Asia Pacific (Melbourne) regions.
  [Learn about installing the agent on a secured network](installing-agent-blocked.md "installing-agent-blocked.md").
- Added support for encrypting post-launch action parameters. Learn about
  [post launch action.](post-launch-settings.md#post-launch-settings-editing "post-launch-settings.md#post-launch-settings-editing")
- [AWS managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md")

* Updated the AWSApplicationMigrationFullAccess policy to support SecureString parameter type
  in SSM Parameters Store for post-migration framework actions.

- Added support for migrating servers with Kernel versions up to 6.8.
- Added support for Ubuntu LTS 24.04.
- Introduced a new predefined post-launch action: Dynatrace. [Learn more about Dynatrace
  action](predefined-post-launch-actions.md#predefined-dynatrace "predefined-post-launch-actions.md#predefined-dynatrace").

## May 2024

- Added support for deploying AWS Replication Agent on a secured network in the Israel (Tel Aviv) region.
  [Learn about installing the agent on a secured network](installing-agent-blocked.md "installing-agent-blocked.md").

## March 2024

- Added support for migration of Linux servers retaining boot mode UEFI.
- Added support for migrating servers running Rocky Linux 9.0 and SUSE Linux Enterprise Server 15 service packs 4 and 5.
- Added support for migrating servers with Kernel versions up to 6.5.

## January 2024

- Added support for agentless replication on VMware vCenter version 8. [Learn about agentless
  replication](installing-vcenter-appliance-mgn.md "installing-vcenter-appliance-mgn.md").

## December 2023

- Added support for the MGN connector to communicate with Windows servers over HTTP and to authenticate with Linux servers using a
  password.
  [Learn more about MGN connector actions.](mgn-connector.md "mgn-connector.md")
- [AWS managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
  – Created a new revision to support MGN in AWS GovCloud and added Statement ID (SID) to a managed policy statement:
  AWSApplicationMigrationServiceEc2InstancePolicy.
- Added support for deploying AWS Replication Agent on a secured network in the Asia Pacific (Jakarta) Region.
  [Learn about installing the agent on a secured network](installing-agent-blocked.md "installing-agent-blocked.md").

## November 2023

- Introduced a new predefined post-launch action:
  App2Container for Replatforming.

## September 2023

- Introduced **MGN connector**, a feature that helps automate the agent installation on source
  servers.
  [Learn more here.](mgn-connector.md "mgn-connector.md")
- Display tags as columns in the source servers, applications and waves table in the console.
- Added support for Amazon Linux 2023.
- Added support for kernel versions up to 6.1.
- Added support for using agentless replication with a proxy server. For more information see
  [agentless replication installation instructions](agentless-mgn.md#installing-vcenter-appliance-mgn "agentless-mgn.md#installing-vcenter-appliance-mgn").

## August 2023

- Introduced 3 new predefined post-launch actions:
  - [Verify tags](predefined-post-launch-actions.md#predefined-verify-tags "predefined-post-launch-actions.md#predefined-verify-tags")
  - [Auto Scaling group setting](predefined-post-launch-actions.md#predefined-autoscaling-group-setting "predefined-post-launch-actions.md#predefined-autoscaling-group-setting")
  - Enable Refactor Spaces

[Learn more about predefined post-launch
actions.](predefined-post-launch-actions.md "predefined-post-launch-actions.md")

- Service launch in the Israel (Tel Aviv) region.

## June 2023

- Service launch in the following regions: Europe (Zurich), Europe (Spain), Asia Pacific (Hyderabad), Asia Pacific (Melbourne).
- Introduced Import and export from local disk. You can now import and export your source servers,
  applications, and waves from and to a CSV file on your local disk.
  [Learn more about the
  import and export feature.](import-export.md "import-export.md")
- Introduced 4 new predefined post-launch actions:
  - [Configure Time Sync](predefined-post-launch-actions.md#predefined-time-sync "predefined-post-launch-actions.md#predefined-time-sync")
  - [Validate disk space](predefined-post-launch-actions.md#predefined-validate-disk-space "predefined-post-launch-actions.md#predefined-validate-disk-space")
  - [Verify HTTP/HTTPS response](predefined-post-launch-actions.md#predefined-verify-http-https-response "predefined-post-launch-actions.md#predefined-verify-http-https-response")
  - [Enable Amazon Inspector](predefined-post-launch-actions.md#predefined-inspector "predefined-post-launch-actions.md#predefined-inspector")

[Learn more about predefined post-launch
actions.](predefined-post-launch-actions.md "predefined-post-launch-actions.md")

- Introduced global view, that allows you to manage migrations across multiple accounts using an integration with AWS
  Organizations.
  This feature provides visibility and the ability to perform actions on source servers,
  apps, and waves in different AWS accounts from a single console.
  [Learn more about global view.](global-view.md "global-view.md")
- Add new actions to the source server data replication process. You can now stop and start, pause and resume data replication,
  from the console. You can also install the AWS Replication Agent without immediately starting the data replication.
  [Learn more about data replication actions.](server-replication-main.md "server-replication-main.md")
- [AWS managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
  – Updated the
  AWSApplicationMigrationServiceRolePolicy policy to support the global view feature.

## May 2023

- Service launch in the following regions: AWS GovCloud (US-East) and AWS GovCloud (US-West).

## April 2023

- [AWS managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
  – Updated the AWSApplicationMigrationFullAccess policy to
  further support automation SSM documents.

## March 2023

- Introduced **Import and export**, a new feature that allows
  you to import and export your source servers, applications, and waves from and to a CSV file.
  [Learn more about the import and export feature.](import-export.md "import-export.md")
- Added support for CentOS 5.5–5.11 and RHEL 5.5–5.11.
- Added support for migration of servers using the Oracle ASM Filter Driver.
- Introduced 8 new predefined post-launch actions:
  - [Conduct EC2 connectivity
    checks](predefined-post-launch-actions.md#predefined-ec2-connectivity-check "predefined-post-launch-actions.md#predefined-ec2-connectivity-check")
  - [Validate volume
    integrity](predefined-post-launch-actions.md#predefined-volume-integrity-validation "predefined-post-launch-actions.md#predefined-volume-integrity-validation")
  - [Verify process status](predefined-post-launch-actions.md#predefined-process-status-validation "predefined-post-launch-actions.md#predefined-process-status-validation")
  - [Convert MS-SQL license
    conversion](predefined-post-launch-actions.md#predefined-windows-ms-sql-conversion "predefined-post-launch-actions.md#predefined-windows-ms-sql-conversion")
  - [Install a CloudWatch
    Agent](predefined-post-launch-actions.md#predefined-cloudwatch-agent-installation "predefined-post-launch-actions.md#predefined-cloudwatch-agent-installation")
  - [Upgrade Windows](predefined-post-launch-actions.md#predefined-windows-upgrade "predefined-post-launch-actions.md#predefined-windows-upgrade")
  - [Create AMI from
    instance](predefined-post-launch-actions.md#predefined-create-ami-from-instance "predefined-post-launch-actions.md#predefined-create-ami-from-instance")
  - [Join Directory Service domain](predefined-post-launch-actions.md#predefined-joined-domain "predefined-post-launch-actions.md#predefined-joined-domain")

[Learn more about predefined post-launch
actions.](predefined-post-launch-actions.md "predefined-post-launch-actions.md")

- Introduced major UI enhancements to the post-launch action feature.
  [Learn more about the new post-launch actions
  layout.](predefined-post-launch-actions.md "predefined-post-launch-actions.md")
- Enhanced the source server page dashboard, adding migration metrics view of the displayed
  servers.
- Service launch in the following regions: Middle East (UAE).
- [AWS managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
  – Updated the AWSApplicationMigrationFullAccess policy,
  the AWSApplicationMigrationSSMAccess policy, and the AWSApplicationMigrationReadOnlyAccess
  policy.

## January 2023

- [AWS managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
  – Updated the
  AWSApplicationMigrationEC2Access policy.

## November 2022

- Introduced support for Application management. [Learn more
  about Applications](applications.md "applications.md").
- Introduced support for Wave management. [Learn more about
  Waves](waves.md "waves.md").
- Added support for additional launch template options. [Learn more](launch-template.md "launch-template.md").
- Added support for post-launch custom actions. [Learn more](post-launch-settings.md#post-launch-settings-custom-actions-add "post-launch-settings.md#post-launch-settings-custom-actions-add").
- Added support for no rescan upon reboot for specific operating systems. [Learn more about the no-rescan feature](Agent-Related-FAQ.md#agent-no-rescan "Agent-Related-FAQ.md#agent-no-rescan").
- The service onboarding process has been simplified. All initial templates: replication
  template, launch template, and post-launch template are initialized with defaults. The
  templates can be modified from the Settings page. [Learn
  more](settings.md "settings.md").
- Added support for SUSE 11 operating system.
- [AWS managed policy updates](security-iam-awsmanpol.md "security-iam-awsmanpol.md") – added
  one new policy and updated two existing policies. For details see [AWS MGN updates for AWS managed policies](security-iam-awsmanpol.md#security-iam-awsmanpol-updates "security-iam-awsmanpol.md#security-iam-awsmanpol-updates") .

## August 2022

- Added support for migration using [AWS Local Zones](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-local-zones "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-local-zones").
- Service launch in the following region: Asia Pacific (Jakarta).
- Added additional instance families to the right-sizing mechanism. [Learn more](right-sizing.md "right-sizing.md").

## July 2022

- Added support for automatically tagging migrated resources with the required MAP program
  tags. [Learn more about automatic tagging](launch-template.md "launch-template.md").

## June 2022

- Added support for updating vCenter credentials for agentless replication. [Learn more about updating vCenter credentials for agentless
  replication](agentless-mgn.md "agentless-mgn.md").
- Support for agent installation using temporary credentials. [Learn more about agent installation using temporary
  credentials](credentials.md#credentials-agent-temporary "credentials.md#credentials-agent-temporary").

## May 2022

- Added support for post-launch settings. Post-launch settings allow you to control and
  automate actions performed after the server has been launched in AWS. [Learn more about post-launch settings](post-launch-settings.md "post-launch-settings.md").
- Added support for Linux SUSE SLES 12 service packs 1 and 2.

## February 2022

- Added support for Microsoft Windows Server 2003, Microsoft Windows Server 2008, Microsoft
  Windows Server 2022, and Microsoft Windows 10.
- Added support for gp3 and io2 EBS volume types for replication servers.
- Added support for UEFI boot for Windows.

## January 2022

- Added support for Kernel 5.15.

## December 2021

- Added support for Kernels 5.8-5.14.

## November 2021

- Service launch in the following regions: Europe (Paris), Europe (Milan), Middle East (Bahrain),
  and Africa (Cape Town).
- Application Migration Service now supports an additional replication method that does not
  require agent installation on each source server. This option is available for source servers
  running on VMware vCenter versions 6.7 and 7.0. [Learn more about
  agentless replication](agentless-mgn.md "agentless-mgn.md").

## October 2021

- Service launch in the following regions: Asia Pacific (Mumbai), Asia Pacific (Seoul), Asia Pacific (Hong Kong), Europe (London).

## July 2021

- Service launch in the following
  regions: US West (N. California), South America (São Paulo), Canada (Central), Asia Pacific (Osaka).

## April 2021

- Service initial launch in: US East (N. Virginia), US East (Ohio), US West (Oregon), Europe (Ireland),
  Europe (Frankfurt), Europe (Stockholm), Asia Pacific (Sydney), Asia Pacific (Singapore).
