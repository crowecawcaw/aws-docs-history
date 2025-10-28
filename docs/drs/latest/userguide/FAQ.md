# Elastic Disaster Recovery FAQ

## What source infrastructure does AWS Elastic Disaster Recovery

support?

With AWS Elastic Disaster Recovery, you can recover your applications on AWS from any source
infrastructure on which you can install the AWS Replication Agent, and on which you can
run the DRS Failback Client. This includes physical infrastructure, virtual machines
on hypervisors by VMware, Microsoft, and others, and cloud infrastructure from other
cloud providers.

## How do I upgrade from CloudEndure Disaster Recovery to

AWS Elastic Disaster Recovery?

You can use the CEDR to DRS Upgrade Assessment Tool and the Server Upgrade Tool
and to move your source servers from CloudEndure Disaster Recovery (CEDR) to
AWS Elastic Disaster Recovery (DRS). [Learn more in the CloudEndure documentation](https://docs.cloudendure.com/#Configuring_and_Running_Disaster_Recovery/Upgrade_CEDR_to_DRS/Upgrade_CEDR_to_DRS.htm#Upgrading_from_CEDR_to_AWS%C2%A0DRS%3FTocPath%3DNavigation%7CConfiguring%2520and%2520Running%2520Disaster%2520Recovery%7CUpgrading%2520from%2520CEDR%2520to%2520AWS%25C2%25A0DRS%7C_____0 "https://docs.cloudendure.com/#Configuring_and_Running_Disaster_Recovery/Upgrade_CEDR_to_DRS/Upgrade_CEDR_to_DRS.htm#Upgrading_from_CEDR_to_AWS%C2%A0DRS%3FTocPath%3DNavigation%7CConfiguring%2520and%2520Running%2520Disaster%2520Recovery%7CUpgrading%2520from%2520CEDR%2520to%2520AWS%25C2%25A0DRS%7C_____0").

AWS Elastic Disaster Recovery (Elastic Disaster Recovery) is the next generation of CloudEndure Disaster Recovery (CEDR)
and is the recommended service to use for Disaster Recovery to AWS. All customers
are encouraged to transition from CEDR to Elastic Disaster Recovery, as soon as this is feasible for
them.

Prior to upgrading, [learn more
about the differences between the two services](https://aws.amazon.com/disaster-recovery/faqs/?nc=sn&loc=4 "https://aws.amazon.com/disaster-recovery/faqs/?nc=sn&loc=4"), and make sure that
[DRS is right for you](https://aws.amazon.com/disaster-recovery/when-to-choose-aws-drs/?cloud-endure-blogs.sort-by=item.additionalFields.createdDate&cloud-endure-blogs.sort-order=desc "https://aws.amazon.com/disaster-recovery/when-to-choose-aws-drs/?cloud-endure-blogs.sort-by=item.additionalFields.createdDate&cloud-endure-blogs.sort-order=desc").

For manual upgrading instructions, refer to [this section](#cedr-to-drs-instructions "#cedr-to-drs-instructions").

## Can AWS Elastic Disaster Recovery protect physical servers?

Because AWS Elastic Disaster Recovery works at the OS layer it can protect not only virtual servers
but physical ones as well.

## What data is stored on and transmitted through

AWS Elastic Disaster Recovery servers?

AWS Elastic Disaster Recovery store only configuration and log data on the AWS Elastic Disaster Recovery Console's
encrypted database. Replicated data is always stored on the customer’s own cloud
VPC. The replicated data is encrypted in transit.

## What is the Recovery Time Objective (RTO) of

AWS Elastic Disaster Recovery?

The Recovery Time Objective (RTO) of Elastic Disaster Recovery is typically
measured in minutes. The RTO is highly dependent on the OS boot time.

## What is the Recovery Point Objective (RPO) of

AWS Elastic Disaster Recovery?

The Recovery Point Objective (RPO) of AWS Elastic Disaster Recovery is typically in the sub-second
range.

## What to consider when replicating Active

Directory

There are two main approaches when it comes to migrating Active Directory or
domain controllers from a disaster:

1. Replicating the entire environment, including the AD server(s) - in this
   approach it is recommended to launch the drill or recovery AD servers first,
   wait until it's up and running and then launch the other drill or recovery
   instances, to make sure the AD servers are ready to authenticate them.
2. Leaving the AD server(s) in the Source environment - in this approach, the
   drill or recovery instances will communicate back to the AD server in the
   source environment and will take the source server's place in the AD
   automatically.

In this case, it is important to conduct any drills using an isolated
subnet in the AWS cloud, so to avoid having the drill or recovery instances
communicate into the source AD server outside of a recovery.

## Does AWS Elastic Disaster Recovery work with LVM and RAID

configurations?

AWS Elastic Disaster Recovery works with any hardware RAID configuration and LVM configuration.

###### Note

Boot partitions that span or mirror, using software over multiple physical
disks, are not supported by AWS Elastic Disaster Recovery and are not recommended for use in EC2. If
your source server's configuration contains mirrored boot partition (e.g. [Windows Mirrored Disks](https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/mirror-system-boot-partition-raid1 "https://learn.microsoft.com/en-us/troubleshoot/windows-server/backup-and-storage/mirror-system-boot-partition-raid1")), we recommend installing the agent to
replicate only one physical disk of the mirrored boot partition using the
`--devices` parameter.

- [Windows EC2 RAID Documentation.](../../../AWSEC2/latest/WindowsGuide/raid-config.md "../../../AWSEC2/latest/WindowsGuide/raid-config.md")
- [Linux EC2 RAID Documentation.](../../../AWSEC2/latest/UserGuide/raid-config.md "../../../AWSEC2/latest/UserGuide/raid-config.md")

## Do Replication Servers have the SSM agent installed on them?

The SSM agent is intentionally not installed on these servers as part of our security architecture to maintain isolation and prevent any potential unauthorized access paths.

## What is there to note regarding SAN/NAS

Support?

If the disks are represented as block devices on the machine, as most SAN are,
Elastic Disaster Recovery will replicate them transparently, just like actual local
disks.

If the disks are mounted over the network, such as an NFS share, as most NAS
implementations are, the AWS Replication Agent would need to be installed on the
actual NFS server in order to replicate the disk.

## Does AWS Elastic Disaster Recovery support Windows

License Migration?

AWS Elastic Disaster Recovery conforms to the [Microsoft Licensing on
AWS](https://aws.amazon.com/windows/resources/licensing/ "https://aws.amazon.com/windows/resources/licensing/") guidelines.

## Can you perform an OS (Operating System) upgrade

with AWS Elastic Disaster Recovery?

No. AWS Elastic Disaster Recovery copies the entire machine as-is. However, you can copy the data
disks exclusively and attach them to a new machine with an upgraded OS.

## What are the private APIs used by AWS DRS to define

actions in the IAM Policy?

AWS Elastic Disaster Recovery (AWS DRS)utilizes the following private API resources as actions in the
IAM Policy. Learn more about actions, resources, and condition keys for Elastic Disaster Recovery.

- BatchCreateVolumeSnapshotGroupForDRS – Grants permission to create volume
  snapshot group.
- BatchDeleteSnapshotRequestForDRS – Grants permission to batch delete
  snapshot request.
- DescribeReplicationServerAssociationsForDRS – Grants permission to
  describe replication server associations.
- DescribeSnapshotRequestsForDRS – Grants permission to describe snapshots
  requests.
- GetAgentCommandForDRS – Grants permission to get agent command.
- GetAgentConfirmedResumeInfoForDRS – Grants permission to get agent
  confirmed resume info.
- GetAgentInstallationAssetsForDRS – Grants permission to get agent
  installation assets.
- GetAgentReplicationInfoForDRS – Grants permission to get agent replication
  info.
- GetAgentRuntimeConfigurationForDRS – Grants permission to get agent
  runtime configuration.
- GetAgentSnapshotCreditsForDRS – Grants permission to get agent snapshots
  credits.
- GetChannelCommandsForDRS – Grants permission to get channel
  commands.
- NotifyAgentAuthenticationForDRS – Grants permission to notify agent
  authentication.
- NotifyAgentConnectedForDRS – Grants permission to notify agent is
  connected.
- NotifyAgentDisconnectedForDRS – Grants permission to notify agent is
  disconnected
- NotifyAgentReplicationProgressForDRS – Grants permission to notify agent
  replication progress.
- RegisterAgentForDRS – Grants permission to register agent.
- SendAgentLogsForDRS – Grants permission to send agent logs.
- SendAgentMetricsForDRS – Grants permission to send agent metrics.
- SendChannelCommandResultForDRS – Grants permission to send channel command
  result.
- SendClientLogsForDRS – Grants permission to send client logs.
- SendClientMetricsForDRS – Grants permission to send client metrics.
- UpdateAgentBacklogForDRS – Grants permission to update agent
  backlog.
- UpdateAgentConversionInfoForDRS – Grants permission to update agent
  conversion info.
- UpdateAgentReplicationInfoForDRS – Grants permission to update agent
  replication info.
- UpdateAgentSourcePropertiesForDRS – Grants permission to update agent
  source properties.
- IssueAgentCertificateForDrs – Grants permission to issue an agent
  certificate.
- CreateConvertedSnapshotForDrs – Grants permission to create converted
  snapshot.

## What post-launch scripts does

AWS Elastic Disaster Recovery support?

DRS can run scripts on a launched drill or recovery instance. This is done by
creating the following folder on the source server and placing the scripts within
that folder.

**Linux**: /boot/post_launch (any files that are
marked as executable)

**Windows**: C:\Program Files (x86)\AWS Replication
Agent\post_launch\ (any .exe, .cmd, or .bat files)

Once you put these scripts in the above folders on the source server, the folder
will be replicated to the drill or recovery instance and be executed once after the
instance boots for the first time.

###### Note

Post-launch scripts on Windows run under the Local System context. Post-launch
scripts on Linux run under the 'root' user.

## Is BitLocker

encryption supported?

DRS does not support OS-based disk encryption features such as BitLocker. These
should be deactivated before using AWS Elastic Disaster Recovery.

## Can I set instance metadata on my launched

instance to support IMDSv2 only?

You can easily set Instance Metadata Service Version 2 (IMDSv2) on your recovery
instances using the EC2 launch template associated with your DRS source server.

Follow the instructions on the [EC2 launch template
page](ec2-launch.md "ec2-launch.md").

When you are redirected to the EC2 console to modify your template, take the
following steps

- Click **Advanced details > Metadata
  version**.
- Select **V2 only (token required)**.

You can then set this launch template as your default version.

## Upgrading from CEDR to AWS DRS - Manual

instructions

###### Important

You can now use the CEDR to DRS Upgrade Assessment Tool and the Server Upgrade
Tool and to move your source servers from CloudEndure Disaster Recovery (CEDR)
to AWS Elastic Disaster Recovery (AWS DRS). [Learn more in the CloudEndure documentation](https://docs.cloudendure.com/#Configuring_and_Running_Disaster_Recovery/Upgrade_CEDR_to_DRS/Upgrade_CEDR_to_DRS.htm#Upgrading_from_CEDR_to_AWS%C2%A0DRS%3FTocPath%3DNavigation%7CConfiguring%2520and%2520Running%2520Disaster%2520Recovery%7CUpgrading%2520from%2520CEDR%2520to%2520AWS%25C2%25A0DRS%7C_____0 "https://docs.cloudendure.com/#Configuring_and_Running_Disaster_Recovery/Upgrade_CEDR_to_DRS/Upgrade_CEDR_to_DRS.htm#Upgrading_from_CEDR_to_AWS%C2%A0DRS%3FTocPath%3DNavigation%7CConfiguring%2520and%2520Running%2520Disaster%2520Recovery%7CUpgrading%2520from%2520CEDR%2520to%2520AWS%25C2%25A0DRS%7C_____0").

AWS Elastic Disaster Recovery (AWS DRS) is the next generation of CloudEndure Disaster Recovery (CEDR)
and is the recommended service to use for Disaster Recovery to AWS. All customers
are encouraged to transition from CEDR to AWS DRS, as soon as this is feasible for
them.

Prior to upgrading, [learn more
about the differences between the two services](https://aws.amazon.com/disaster-recovery/faqs/?nc=sn&loc=4 "https://aws.amazon.com/disaster-recovery/faqs/?nc=sn&loc=4"), and make sure that
[DRS is right for you](https://aws.amazon.com/disaster-recovery/when-to-choose-aws-drs/?cloud-endure-blogs.sort-by=item.additionalFields.createdDate&cloud-endure-blogs.sort-order=desc "https://aws.amazon.com/disaster-recovery/when-to-choose-aws-drs/?cloud-endure-blogs.sort-by=item.additionalFields.createdDate&cloud-endure-blogs.sort-order=desc").

The following are the manual instructions for upgrading:

1. Follow the DRS [getting started procedure to initialize AWS DRS](getting-started-initializing.md "getting-started-initializing.md") in the
   AWS Region you want to replicate to.
2. [Launch a recovery instance (target machine)](https://docs.cloudendure.com/#Configuring_and_Running_Disaster_Recovery/Performing_a_Disaster_Recovery_Failover/Performing_a_Disaster_Recovery_Failover.htm#Performing_a_Failover_with_CloudEndure_..20%3FTocPath%3DNavigation%7CConfiguring%2520and%2520Running%2520Disaster%2520Recovery%7CPerforming%2520a%2520Disaster%2520Recovery%2520Failover%2520and%2520Failback%7CFailover%2520and%2520Failback%2520with%2520CloudEndure%2520-%2520Detailed%2520Instructions%7CPerforming%2520a%2520Failover%2520with%2520CloudEndure%7C_____0 "https://docs.cloudendure.com/#Configuring_and_Running_Disaster_Recovery/Performing_a_Disaster_Recovery_Failover/Performing_a_Disaster_Recovery_Failover.htm#Performing_a_Failover_with_CloudEndure_..20%3FTocPath%3DNavigation%7CConfiguring%2520and%2520Running%2520Disaster%2520Recovery%7CPerforming%2520a%2520Disaster%2520Recovery%2520Failover%2520and%2520Failback%7CFailover%2520and%2520Failback%2520with%2520CloudEndure%2520-%2520Detailed%2520Instructions%7CPerforming%2520a%2520Failover%2520with%2520CloudEndure%7C_____0") using CloudEndure,
   and make sure that it works as expected. Once you have verified that
   everything works as expected, terminate the launched instance using the
   CloudEndure Console by choosing the ["Delete Target Machines" option](https://docs.cloudendure.com/#Getting_Started_with_CloudEndure/Exploring_the_CloudEndure_Console/Machines/Machines.htm#MACHINE_ACTIONS_Menu%3FTocPath%3DNavigation%7CGetting%2520Started%2520with%2520CloudEndure%7CExploring%2520the%2520CloudEndure%2520User%2520Console%7CMachines%2520Page%7C_____3 "https://docs.cloudendure.com/#Getting_Started_with_CloudEndure/Exploring_the_CloudEndure_Console/Machines/Machines.htm#MACHINE_ACTIONS_Menu%3FTocPath%3DNavigation%7CGetting%2520Started%2520with%2520CloudEndure%7CExploring%2520the%2520CloudEndure%2520User%2520Console%7CMachines%2520Page%7C_____3"). If you want to keep the
   instance, [activate EC2 termination protection](../../../AWSEC2/latest/WindowsGuide/terminating-instances.md#Using_ChangingDisableAPITermination "../../../AWSEC2/latest/WindowsGuide/terminating-instances.md#Using_ChangingDisableAPITermination") before removing the source
   machine from the CloudEndure service.

Until the server is ready on DRS, CloudEndure will still be your way to
launch Recovery instances should you need them. That is why you must make
sure that recovery using CloudEndure is working as expected for the server/s
you are about to transition to DRS. 3. [Pause data replication](https://docs.cloudendure.com/#Getting_Started_with_CloudEndure/Exploring_the_CloudEndure_Console/Machines/Machines.htm#MACHINE_ACTIONS_Menu%3FTocPath%3DNavigation%7CGetting%2520Started%2520with%2520CloudEndure%7CExploring%2520the%2520CloudEndure%2520User%2520Console%7CMachines%2520Page%7C_____3 "https://docs.cloudendure.com/#Getting_Started_with_CloudEndure/Exploring_the_CloudEndure_Console/Machines/Machines.htm#MACHINE_ACTIONS_Menu%3FTocPath%3DNavigation%7CGetting%2520Started%2520with%2520CloudEndure%7CExploring%2520the%2520CloudEndure%2520User%2520Console%7CMachines%2520Page%7C_____3")for this server in CloudEndure. 4. [Manually uninstall the CloudEndure agent from your source
servers](https://docs.cloudendure.com/#FAQ/FAQ/Agent_Related.htm#How_do_I_manually_uninstall_the_CloudEndure_Agent_from_a_Source_or_Target_mac...%3FTocPath%3DNavigation%7CFAQ%25C2%25A0and%25C2%25A0Troubleshooting%7CFAQ%7CAgent%2520Related%7C_____14 "https://docs.cloudendure.com/#FAQ/FAQ/Agent_Related.htm#How_do_I_manually_uninstall_the_CloudEndure_Agent_from_a_Source_or_Target_mac...%3FTocPath%3DNavigation%7CFAQ%25C2%25A0and%25C2%25A0Troubleshooting%7CFAQ%7CAgent%2520Related%7C_____14").

###### Important

Do **_not_** do use the **Remove from
console** option available from the CloudEndure user
console. By keeping this server’s records in CloudEndure, you also
maintain it’s Point In Time recovery points, allowing you to launch a
recovery instance using CloudEndure, should you need such a recovery
instance before this server is ready on Elastic Disaster Recovery. 5. [Install the AWS Replication Agent on your source server.](adding-servers.md "adding-servers.md") 6. Configure [Replication settings](replication-settings-template.md "replication-settings-template.md") and [Launch settings](launching-target-servers.md "launching-target-servers.md") for this server in AWS Elastic Disaster Recovery (AWS DRS). 7. Wait for initial sync to be complete until your source server's [data replication status](recovery-dashboard.md#data-replication-stat "recovery-dashboard.md#data-replication-stat") has reached the **Healthy** state in the AWS DRS console. 8. Use DRS to[launch a drill instance](failback-preparing.md#recovery-drill-overview "failback-preparing.md#recovery-drill-overview") for your source server and make sure it
works as desired. 9. Wait for the number of recovery days you want to have [Points In Time](failback-overview.md#point-in-time-faq "failback-overview.md#point-in-time-faq") for to pass. For example, if you have
CloudEndure and AWS DRS configured to retain 10 daily recovery Points In
Time, then wait for 10 full days after the server has achieved the **Healthy** state in AWS DRS before removing it from
CloudEndure.

###### Important

[Remove your source servers from the CloudEndure console](https://docs.cloudendure.com/#Installing_the_CloudEndure_Agents/Uninstalling_the_Agents/Uninstalling_the_Agents.htm#Uninstalling_Agents_from_Source_Machines%3FTocPath%3DNavigation%7CInstalling%2520the%2520CloudEndure%2520Agents%7CUninstalling%2520the%2520Agents%7CUninstalling%2520Agents%2520from%2520Source%2520Machines%7C_____0 "https://docs.cloudendure.com/#Installing_the_CloudEndure_Agents/Uninstalling_the_Agents/Uninstalling_the_Agents.htm#Uninstalling_Agents_from_Source_Machines%3FTocPath%3DNavigation%7CInstalling%2520the%2520CloudEndure%2520Agents%7CUninstalling%2520the%2520Agents%7CUninstalling%2520Agents%2520from%2520Source%2520Machines%7C_____0").

This action will cause all replication resources created for this server in
AWS to be terminated. Until you do this, these resources continue to cost you
money.

If you have a launched a target instance in AWS using CEDR, consider whether
you want to keep it or not.

If you experience a disaster recovery event before the server reaches the **Healthy** state in AWS DRS, navigate to the CloudEndure
console and [launch a Target instance from there](https://docs.cloudendure.com/#Configuring_and_Running_Disaster_Recovery/Performing_a_Disaster_Recovery_Failover/Performing_a_Disaster_Recovery_Failover.htm#Performing_a_Failover_with_CloudEndure_..20%3FTocPath%3DNavigation%7CConfiguring%2520and%2520Running%2520Disaster%2520Recovery%7CPerforming%2520a%2520Disaster%2520Recovery%2520Failover%2520and%2520Failback%7CFailover%2520and%2520Failback%2520with%2520CloudEndure%2520-%2520Detailed%2520Instructions%7CPerforming%2520a%2520Failover%2520with%2520CloudEndure%7C_____0 "https://docs.cloudendure.com/#Configuring_and_Running_Disaster_Recovery/Performing_a_Disaster_Recovery_Failover/Performing_a_Disaster_Recovery_Failover.htm#Performing_a_Failover_with_CloudEndure_..20%3FTocPath%3DNavigation%7CConfiguring%2520and%2520Running%2520Disaster%2520Recovery%7CPerforming%2520a%2520Disaster%2520Recovery%2520Failover%2520and%2520Failback%7CFailover%2520and%2520Failback%2520with%2520CloudEndure%2520-%2520Detailed%2520Instructions%7CPerforming%2520a%2520Failover%2520with%2520CloudEndure%7C_____0"). This will launch the Target
instance from the last PIT the system created before you removed the CloudEndure
agent from the source servers. The CloudEndure console UI will show you the PIT from
when this will launch.

###### Note

During some of the time it takes to transition from CloudEndure to DRS you
will not have the same level of protection: While replication in CloudEndure is
paused and the server has not yet completed the initial scan, you will not be
able to launch instances in DRS, and only be able to launch instances in
CloudEndure with data prior to the pause action. This applies both to launching
from latest snapshot and to launching from point-in-time.

###### Note

Once you install the AWS Replication Agent on the source server, and until you
remove that source server from the CloudEndure user console, you will be paying
for the two services in parallel, and nearly twice for replication resources
such as EBS, snapshots, and more.
