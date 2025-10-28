# Scanning Amazon EC2 instances with Amazon Inspector

Amazon Inspector Amazon EC2 scanning extracts metadata from your EC2 instance before comparing the metadata against rules collected from security advisories.
Amazon Inspector scans instances for package vulnerabilities and network reachability issues to produce [findings](findings-types.md "findings-types.md").
Amazon Inspector performs network reachability scans once every 12 hours and package vulnerability scans on a variable cadence that depends on the scan method associated with the EC2 instance.

Package vulnerability scans can be performed using an [agent-based](scanning-ec2.md#agent-based "scanning-ec2.md#agent-based") or [agentless](scanning-ec2.md#agentless "scanning-ec2.md#agentless") scan method.
Both of these scan methods determine how and when Amazon Inspector collects the software inventory from an EC2 instance for package vulnerability scans.
Agent-based scanning collects software inventory using the SSM agent, and agentless scanning collects software inventory using on Amazon EBS snapshots.

Amazon Inspector uses the scan methods that you activate for your account.
When you activate Amazon Inspector for the first time, your account is automatically enrolled in hybrid scanning, which uses both scan methods.
However, you can [change this setting](scanning-ec2.md#scan-mode "scanning-ec2.md#scan-mode") at any time.
For information about how to activate a scan type, see [Activating a scan type](activate-scans.md "activate-scans.md").
This section provides information about Amazon EC2 scanning.

###### Note

Amazon EC2 scanning does not scan filesystem directories related to virtual environment even if they are provisioned through deep inspection.
For example, the path `/var/lib/docker/` is not scanned because it's commonly used for container run times.

## Agent-based scanning

Agent-based scans are performed continuously using the SSM agent on all eligible
instances. For agent-based scans, Amazon Inspector uses SSM associations, and plugins installed
through these associations, to collect software inventory from your instances. In
addition to package vulnerability scans for operating system packages, Amazon Inspector
agent-based scanning can also detect package vulnerabilities for application
programming language packages in Linux-based instances through [Amazon Inspector deep inspection for Linux-based Amazon EC2 instances](deep-inspection.md "deep-inspection.md").

The following process explains how Amazon Inspector uses SSM to collect inventory and perform
agent-based scans:

1. Amazon Inspector creates SSM associations in your account to collect inventory from
   your instances. For some Instance types (Windows, and Linux), these
   associations install plugins on individual instances to collect inventory.
2. Using SSM, Amazon Inspector extracts package inventory from an instance.
3. Amazon Inspector evaluates the extracted inventory and generates findings for any
   detected vulnerabilities.

###### Note

For agent-based scanning, the Amazon EC2 instance must be managed by SSM in same AWS account.

### Eligible instances

Amazon Inspector will use the agent-based method to scan an instance if it meets the
following conditions:

- The instance has a supported OS. For a list of supported OS see the
  **Agent-based scan support** column of [Supported operating systems: Amazon EC2 scanning](supported.md#supported-os-ec2 "supported.md#supported-os-ec2").
- The instance is not excluded from scans by Amazon Inspector EC2 exclusion
  tags.
- The instance is SSM managed. For instructions on verifying and
  configuring the agent, see [Configuring the SSM Agent](#configure-ssm "#configure-ssm").

### Agent-based scan behaviors

When using the agent-based scan method, Amazon Inspector initiates new vulnerability
scans of EC2 instances in the following situations:

- When you launch a new EC2 instance.
- When you install new software on an existing EC2 instance (Linux and
  Mac).
- When Amazon Inspector adds a new common vulnerabilities and exposures (CVE) item
  to its database, and that CVE is relevant to your EC2 instance (Linux and
  Mac).

Amazon Inspector updates the **Last scanned** field for an EC2 instance when
an initial scan is completed. After this, the **Last scanned**
field is updated when Amazon Inspector evaluates SSM inventory (every 30 minutes by
default), or when an instance is re-scanned because a new CVE impacting that
instance was added to the Amazon Inspector database.

You can check when an EC2 instance was last scanned for vulnerabilities from
the Instances tab on the **Account management** page or by
using the [ListCoverage](../../v2/APIReference/API_ListCoverage.md "../../v2/APIReference/API_ListCoverage.md") command.

### Configuring the SSM Agent

In order for Amazon Inspector to detect software vulnerabilities for an Amazon EC2 instance
using the agent-based scan method, the instance must be a [managed
instance](../../../systems-manager/latest/userguide/managed_instances.md "../../../systems-manager/latest/userguide/managed_instances.md") in Amazon EC2 Systems Manager (SSM). An SSM managed instance has the
SSM Agent installed and running, and SSM has permission to manage the
instance. If you are already using SSM to manage your instances, no other
steps are needed for agent-based scans.

The SSM Agent is installed by default on EC2 instances created from some Amazon
Machine Images (AMIs). For more information, see [About SSM
Agent](../../../systems-manager/latest/userguide/prereqs-ssm-agent.md "../../../systems-manager/latest/userguide/prereqs-ssm-agent.md") in the _AWS Systems Manager User
Guide_. However, even if it's installed, you may need to activate the
SSM Agent manually, and grant SSM permission to manage your instance.

The following procedure describes how to configure an Amazon EC2 instance as a
managed instance using an IAM instance profile. The procedure also provides
links to more detailed information in the _AWS Systems Manager User
Guide_.

[AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md") is the recommended
policy to use when you attach an instance profile. This policy has all the
permissions needed for Amazon Inspector EC2 scanning.

###### Note

You can also automate SSM management of all your EC2 instances, without
the use of IAM instance profiles using SSM Default Host Management
Configuration. For more information, see [Default Host Management Configuration](../../../systems-manager/latest/userguide/managed-instances-default-host-management.md "../../../systems-manager/latest/userguide/managed-instances-default-host-management.md").

###### To configure SSM for an Amazon EC2 instance

1. If it's not already installed by your operating system vendor, install
   the SSM Agent. For more information, see [Working with
   SSM Agent](../../../systems-manager/latest/userguide/ssm-agent.md "../../../systems-manager/latest/userguide/ssm-agent.md").
2. Use the AWS CLI to verify that the SSM Agent is running. For more
   information, see [Checking SSM Agent status and starting the agent](../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md "../../../systems-manager/latest/userguide/ssm-agent-status-and-restart.md").
3. Grant permission for SSM to manage your instance. You can grant
   permission by creating an IAM instance profile and attaching it to
   your instance. We recommend using the [AmazonSSMManagedInstanceCore](../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md "../../../aws-managed-policy/latest/reference/AmazonSSMManagedInstanceCore.md") policy,
   because this policy has the permissions for SSM Distributor, SSM
   Inventory and SSM State manager, that Amazon Inspector needs for scans. For
   instructions on creating an instance profile with these permissions and
   attaching it an instance, see [Configure instance permissions for Systems Manager
   Systems Manager](../../../systems-manager/latest/userguide/setup-instance-permissions.md#instance-profile-add-permissions "../../../systems-manager/latest/userguide/setup-instance-permissions.md#instance-profile-add-permissions").
4. (Optional) Activate automatic updates for the SSM Agent. For more
   information, see [Automating updates to SSM Agent](../../../systems-manager/latest/userguide/ssm-agent-automatic-updates.md "../../../systems-manager/latest/userguide/ssm-agent-automatic-updates.md").
5. (Optional) Configure Systems Manager to use an Amazon Virtual Private Cloud (Amazon VPC) endpoint. For
   more information, see [Create
   Amazon VPC endpoints](../../../systems-manager/latest/userguide/setup-create-vpc.md "../../../systems-manager/latest/userguide/setup-create-vpc.md").

###### Important

Amazon Inspector requires a Systems Manager State Manager association in your account to
collect software application inventory. Amazon Inspector automatically creates an
association called `InspectorInventoryCollection-do-not-delete`
if one doesn't already exist.

Amazon Inspector also requires a resource data sync and automatically creates one
called `InspectorResourceDataSync-do-not-delete` if one doesn't
already exist. For more information, see [Configuring resource data sync for Inventory](../../../systems-manager/latest/userguide/sysman-inventory-datasync.md "../../../systems-manager/latest/userguide/sysman-inventory-datasync.md") in the _AWS Systems Manager User Guide_. Each account can have a
set number of resource data syncs per Region. For more information, see
Maximum number of resource data syncs (per AWS account per Region) in
[SSM endpoints and quotas](../../../general/latest/gr/ssm.md#limits_ssm "../../../general/latest/gr/ssm.md#limits_ssm").

#### SSM resources created for scanning

Amazon Inspector requires a number of SSM resources in your account to run Amazon EC2 scans.
The following resources are created when you first activate Amazon Inspector EC2 scanning:

###### Note

If any of these SSM resources are deleted while Amazon Inspector Amazon EC2 scanning is activated for your account, Amazon Inspector will attempt to recreate them at the next scan interval.

`InspectorInventoryCollection-do-not-delete`

This is a Systems Manager State Manager (SSM) association that Amazon Inspector
uses to collect software application inventory from your Amazon EC2
instances. If your account already has an SSM association for
collecting inventory from `InstanceIds*`, Amazon Inspector will
use that instead of creating its own.

`InspectorResourceDataSync-do-not-delete`

This is a resource data sync that Amazon Inspector uses to send collected
inventory data from your Amazon EC2 instances to an Amazon S3 bucket owned
by Amazon Inspector. For more information, see [Configuring resource data sync for Inventory](../../../systems-manager/latest/userguide/sysman-inventory-datasync.md "../../../systems-manager/latest/userguide/sysman-inventory-datasync.md") in the
_AWS Systems Manager User
Guide_.

`InspectorDistributor-do-not-delete`

This is an SSM association Amazon Inspector uses for scanning Windows
instances. This association installs the Amazon Inspector SSM plugin on
your Windows instances. If the plugin file is inadvertently
deleted this association will reinstall it at the next
association interval.

`InvokeInspectorSsmPlugin-do-not-delete`

This is an SSM association Amazon Inspector uses for scanning Windows
instances. This association allows Amazon Inspector to initiate scans using
the plugin, you can also use it to set custom intervals for
scans of Windows instances. For more information, see [Setting custom schedules for Windows
instance scans](windows-scanning.md#windows-scan-schedule "windows-scanning.md#windows-scan-schedule").

`InspectorLinuxDistributor-do-not-delete`

This is an SSM association that Amazon Inspector uses for Amazon EC2 Linux deep inspection.
This association installs the Amazon Inspector SSM plugin on your Linux instances.

`InvokeInspectorLinuxSsmPlugin-do-not-delete`

This is an SSM association Amazon Inspector uses for Amazon EC2 Linux deep
inspection. This association allows Amazon Inspector to initiate scans
using the plugin.

###### Note

When you deactivate Amazon Inspector Amazon EC2 scanning or deep inspection, the SSM resource `InvokeInspectorLinuxSsmPlugin-do-not-delete` is no longer invoked.

## Agentless scanning

Amazon Inspector uses the agentless scanning method on eligible instances when your account is in hybrid scanning mode.
Hybrid scanning mode includes agent-based and agentless scans and is automatically enabled when you activate Amazon EC2 scanning.

For agentless scans, Amazon Inspector uses EBS snapshots to collect a software inventory from your instances.
Agentless scanning scans instances for operating system and application programming language package vulnerabilities..

###### Note

When scanning Linux instances for application programming language package
vulnerabilities, the agentless method scans all available paths, whereas
agent-based scanning only scans the default paths and additional paths you
specify as part of [Amazon Inspector deep inspection for Linux-based Amazon EC2 instances](deep-inspection.md "deep-inspection.md"). This may result in the same instance
having different findings depending on whether it is scanned using the
agent-based method or agentless method.

The following process explains how Amazon Inspector uses EBS snapshots to collect inventory
and perform agentless scans:

1. Amazon Inspector creates an EBS snapshot of all volumes attached to the instance.
   While Amazon Inspector is using it, the snapshot is stored in your account and tagged
   with `InspectorScan` as a tag key, and a unique scan ID as the
   tag value.
2. Amazon Inspector retrieves data from the snapshots using [EBS direct
   APIs](../../../AWSEC2/latest/UserGuide/ebs-accessing-snapshot.md "../../../AWSEC2/latest/UserGuide/ebs-accessing-snapshot.md") and evaluates them for vulnerabilities. Findings are
   generated for any detected vulnerabilities.
3. Amazon Inspector deletes the EBS snapshots it created in your account.

### Eligible instances

Amazon Inspector will use the agentless method to scan an instance if it meets the following conditions:

- The instance has a supported OS.
  For more information, see the >Agent-based scan support column of [Supported operating systems: Amazon EC2 scanning](supported.md#supported-os-ec2 "supported.md#supported-os-ec2").
- The instance has a status of `Unmanaged EC2 instance`, `Stale inventory`, or `No inventory`.
- The instance is backed by Amazon EBS and has one of the following file system formats:
  - `ext3`
  - `ext4`
  - `xfs`

- The instance isn't excluded from scans through Amazon EC2 exclusion tags.
- The number of volumes attached to the instance is less than 8 and have a combined size that's less than or equal to 1200 GB.

### Agentless scan behaviors

When your account is configured for **Hybrid scanning**,
Amazon Inspector performs agentless scans on eligible instances every 24 hours. Amazon Inspector
detects and scans newly eligible instances every hour, which includes new
instances without SSM agents, or pre-existing instances with statuses that have
changed to `SSM_UNMANAGED`.

Amazon Inspector updates the **Last scanned** field for an Amazon EC2
instance whenever it scans extracted snapshots from an instance after an
agentless scan.

You can check when an EC2 instance was last scanned for vulnerabilities from
the Instances tab on the Account management page or by using the [ListCoverage](../../v2/APIReference/API_ListCoverage.md "../../v2/APIReference/API_ListCoverage.md") command.

## Managing scan mode

Your EC2 scan mode determines which scan methods Amazon Inspector will use when performing
EC2 scans in your account. You can view the scan mode for your account from the EC2
scanning settings page under **General settings**. Standalone
accounts or Amazon Inspector delegated administrators can change the scan mode. When you set
the scan mode as the Amazon Inspector delegated administrator that scan mode is set for all
member accounts in your organization. Amazon Inspector has the following scan modes:

**Agent-based scanning** – In this scan mode, Amazon Inspector will
exclusively use the agent-based scan method when scanning for package
vulnerabilities. This scan mode only scans SSM managed instances in your account,
but has the benefit of providing continuous scans in response to new CVE’s or
changes to the instances. Agent-based scanning also provides Amazon Inspector deep Inspection
for eligible instances. This is the default scan mode for newly activated
accounts.

**Hybrid scanning** – In this scan mode, Amazon Inspector uses a
combination of both agent-based and agentless methods to scan for package
vulnerabilities. For eligible EC2 instances that have the SSM agent installed and
configured, Amazon Inspector uses the agent-based method. For eligible instances that aren't
SSM managed, Amazon Inspector will use the agentless method for eligible EBS-backed
instances.

###### To change the scan mode

1. Sign in using your credentials, and then open the Amazon Inspector console at [https://console.aws.amazon.com/inspector/v2/home](https://console.aws.amazon.com/inspector/v2/home "https://console.aws.amazon.com/inspector/v2/home").
2. Using the AWS Region selector in the upper-right corner of the page,
   select the Region where you want to change your EC2 scan mode.
3. From the side navigation panel, under **General
   settings**, select **EC2 scanning
   settings**.
4. Under **Scan Mode**, select
   **Edit**.
5. Choose a scan mode and then select **Save
   changes**.

## Excluding instances from Amazon Inspector scans

You can exclude Linux and Windows instances from Amazon Inspector scans by tagging these instances with the `InspectorEc2Exclusion` key.
Including a tag value is optional.
For information about adding tags, see [Tag your Amazon EC2 resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md").

When you tag an instance for exclusion from Amazon Inspector scans, Amazon Inspector marks the instance as excluded and won't create findings for it.
However, the Amazon Inspector SSM plugin will continue to be invoked.
To prevent the plugin from being invoked, you must [allow access to tags in instance metadata](../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS "../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS").

###### Note

You're not charged for excluded instances.

Additionally, you can exclude an encrypted EBS volume from agentless scans by tagging the AWS KMS key used to encrypt that volume with the `InspectorEc2Exclusion` tag.
For more information, see [Tagging keys](../../../kms/latest/developerguide/tagging-keys.md "../../../kms/latest/developerguide/tagging-keys.md").

## Supported operating systems

Amazon Inspector scans supported Mac, Windows, and Linux EC2 instance for vulnerabilities in
operating system packages. For Linux instances, Amazon Inspector can produce findings for
application programming language packages using [Amazon Inspector deep inspection for Linux-based Amazon EC2 instances](deep-inspection.md "deep-inspection.md"). For Mac and Windows instances only operating
system packages are scanned.

For information about supported operating systems, including which operating
system can be scanned without an SSM agent, see [Amazon EC2
instances status values](supported.md#supported-os-ec2 "supported.md#supported-os-ec2").
