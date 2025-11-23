# `AWSSupport-MigrateXenToNitroLinux`

**Description**

The `AWSSupport-MigrateXenToNitroLinux` runbook clones, prepares, and migrates
an Amazon Elastic Compute Cloud (Amazon EC2) Linux Xen instance to a [Nitro instance type](../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances "../../../AWSEC2/latest/UserGuide/instance-types.md#ec2-nitro-instances"). This runbook provide two options for
operation types:

- `Clone&Migrate` – This option’s workflow consists of the
  **Preliminary Checks**, **Testing**, and **Clone&Migrate** phases. The workflow is run using
  the `AWSSupport-CloneXenEC2InstanceAndMigrateToNitro` runbook.
- `FullMigration` – This option runs the
  `Clone&Migrate` workflow and then performs the additional step of
  **Replace root Amazon EBS volumes**.

###### Important

Using this runbook incurs costs to your account for the running time of Amazon EC2
instances, creation of Amazon Elastic Block Store (Amazon EBS) volumes, and AMIs. For more details, see
[Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/ "https://aws.amazon.com/ec2/pricing/") and [Amazon EBS Pricing](https://aws.amazon.com/ebs/pricing/ "https://aws.amazon.com/ebs/pricing/").

**Preliminary checks**

The automation performs the following preliminary checks before continuing with the
migration. If any of the checks fail, the automation ends. This phase is only part of the
`Clone&Migrate` workflow.

- Checks if the target instance is already a Nitro instance
  type.
- Checks if the Spot Instances purchasing option was used for the target
  instance.
- Checks if instance store volumes are attached to the target instance.
- Verifies the target instance operating system (OS) is Linux.
- Checks if the target instance is a part of an Amazon EC2 Auto Scaling group. If it is part of an
  Amazon EC2 Auto Scaling group, the automation verifies that the instance is in the `standby`
  state.
- Verifies that the instance is managed by AWS Systems Manager.

**Testing**

The automation creates an Amazon Machine Image (AMI) from the target instance and launches a test
instance from the newly created AMI. This phase is part of only the
`Clone&Migrate` workflow.

If the test instance passes all status checks, the automation pauses and approval from the
designated principals is requested through Amazon Simple Notification Service (Amazon SNS) notification. If approval is
provided, the automation terminates the test instance, stops the target instance, and
continues with the migration, while the newly created AMI is deregistered at the end of
the `Clone&Migrate` workflow.

###### Note

Before providing approval, we recommend verifying that all applications running on the
target instance have been closed gracefully.

**Clone and Migrate**

The automation creates another AMI from the target instance, and launches a new instance
to change to a Nitro instance type. The automation completes the following
prerequisites before continuing with the migration. If any of the checks fail, the
automation ends. This phase is also only part of the `Clone&Migrate`
workflow.

- Turns on the enhanced networking (ENA) attribute.
- Installs the latest version of ENA drivers if they're not already installed, or
  updates the ENA drivers version to the latest version. To ensure maximum network
  performance, updating to the latest ENA driver version is required if the
  Nitro instance type is the 6th generation.
- Verifies that the NVMe module is installed. If the module is installed, the
  automation verifies that the module is loaded in
  `initramfs`.
- Analyzes `/etc/fstab` and replaces entries with block device
  names (`/dev/sd*` or `/dev/xvd*`) with their
  respective UUIDs. Before modifying the configuration, the automation creates a
  backup of the file at the path `/etc/fstab*`.
- Turns off predictable interface naming by adding the `net.ifnames=0`
  option to the `GRUB_CMDLINE_LINUX` line in the
  `/etc/default/grub` file if it exists, or to the kernel in
  `/boot/grub/menu.lst`.
- Removes the `/etc/udev/rules.d/70-persistent-net.rules` file
  if it exists. Before removing the file, the automation creates a backup of the file
  at the path `/etc/udev/rules.d/`.
  After verifying all requirements, the instance type is changed to the Nitro
  instance type that you specify. The automation waits for the newly created instance to pass
  all status checks after starting as a Nitro instance type. The automation
  then waits for approval from the designated principals to create an AMI of the
  successfully launched Nitro instance. If approval is denied, the automation
  ends, leaving the newly created instance running, and the target instance remains
  stopped.

**Replace root Amazon EBS Volume**

If you choose `FullMigration` as the `OperationType`, the
automation migrates the target Amazon EC2 instance to the Nitro instance type that
you specify. Automation requests approval from designated principals to replace the root
Amazon EBS volume of the target Amazon EC2 instance with the cloned Amazon EC2 instance's root volume.
After the migration is successful, the cloned Amazon EC2 instance is terminated. If the
automation fails, the original Amazon EBS root volume is attached to the target Amazon EC2 instance.
If the root Amazon EBS volume attached to the target Amazon EC2 instance has tags with the
`aws:` prefix applied, the `FullMigration` operation isn't
supported.

**Before you begin**

The target instance must have outbound internet access. This is to access repositories for
drivers and dependencies like kernel-devel, gcc,
patch, rpm-build, wget,
dracut, make, linux-headers, and
unzip. Package manager is used if needed.

An Amazon SNS topic is required to send notifications for approvals and updates. For more
information about creating an Amazon SNS topic, see [Creating an Amazon SNS topic](../../../sns/latest/dg/sns-create-topic.md "../../../sns/latest/dg/sns-create-topic.md") in the
_Amazon Simple Notification Service Developer Guide_.

This runbook supports the following operating systems:

- RHEL 7.x - 8.5
- Amazon Linux (2018.03), Amazon Linux 2
- Debian Server
- Ubuntu Server 18.04 LTS, 20.04 LTS, and 20.10 STR
- SUSE Linux Enterprise Server (SUSE12SP5, SUSE15SP2)

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-MigrateXenToNitroLinux "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-MigrateXenToNitroLinux")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- Acknowledgement

Type: String

Description: (Required) Read the complete details of the actions performed by this
automation runbook, and enter `Yes, I understand and
 acknowledge` to proceed with using the runbook.

- ApproverIAM

Type: String

Description: (Required) The ARNs of IAM roles, users, or user names who can
provide approvals to the automation. You can specify a maximum of 10
approvers.

- DeleteResourcesOnFailure

Type: Boolean

Description: (Optional) Determines whether the newly created instance and AMI
for the migration are deleted if the automation fails.

Valid values: True | False

Default: True

- MinimumRequiredApprovals

Type: String

Description: (Optional) The minimum number of approvals required to continue
running the automation when approvals are requested.

Valid values: 1-10

Default: 1

- NitroInstanceType

Type: String

Description: (Required) The Nitro instance type that you want to
change the instance to. Supported instance types include M5, M6, C5, C6, R5, R6, and
T3.

Default: m5.xlarge

- OperationType

Type: String

Description: (Required) The operation that you want to perform. The
`FullMigration` option performs the same tasks as
`Clone&Migrate` and additionally replaces the root volume of your
target instance. The root volume of the target instance is replaced with the root
volume from the newly created instance following the migration process. The
`FullMigration` operation does not support root volumes defined by
Logical Volume Manager (LVM).

Valid values: Clone&Migrate | FullMigration

- SNSTopicArn

Type: String

Description: (Required) The ARN of the Amazon SNS topic for approval notification. The
Amazon SNS topic is used to send required approval notifications during the
automation.

- TargetInstanceId

Type: String

Description: (Required) The ID of the Amazon EC2 instances to migrate.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:DescribeAutomationExecutions`
- `ssm:StartAutomationExecution`
- `ssm:DescribeInstanceInformation`
- `ssm:DescribeAutomationStepExecutions`
- `ssm:SendCommand`
- `ssm:GetAutomationExecution`
- `ssm:ListCommands`
- `ssm:ListCommandInvocations`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceTypeOfferings`
- `ec2:DescribeInstanceTypes`
- `ec2:DescribeImages`
- `ec2:CreateImage`
- `ec2:RunInstances`
- `ec2:DescribeInstanceStatus`
- `ec2:DeregisterImage`
- `ec2:DeleteSnapshot`
- `ec2:TerminateInstances`
- `ec2:StartInstances`
- `ec2:DescribeKeyPairs`
- `ec2:StopInstances`
- `kms:CreateGrant*`
- `kms:ReEncrypt`
- `ec2:ModifyInstanceAttribute`
- `autoscaling:DescribeAutoScalingInstances`
- `iam:passRole`
- `iam:ListRoles`

**Document Steps**

- `startOfPreliminaryChecksBranch` - Branches to the Preliminary
  checks workflow.
- `getTargetInstanceProperties` - Gathers details from the target
  instance.
- `checkIfNitroInstanceTypeIsSupportedInAZ` - Determines if the
  target Amazon EC2 instance type is supported in the same Availability Zone as the
  target instance.
- `getXenInstanceTypeDetails` - Gathers details about the source
  instance type.
- `checkIfInstanceHypervisorIsNitroAlready` - Checks if the target
  instance is already running as a Nitro instance type.
- `checkIfTargetInstanceLifecycleIsSpot` - Checks if the purchasing
  option of the target instance is Spot.
- `checkIfOperatingSystemIsLinux` - Checks if the target instance
  OS is Linux.
- `verifySSMConnectivityForTargetInstance` - Verifies that the
  target instance is managed by Systems Manager.
- `checkIfEphemeralVolumeAreSupported` - Checks if the current
  instance type of the target instance supports instance store volumes.
- `verifyIfTargetInstanceHasEphemeralVolumesAttached` - Checks if
  the target instance has instance store volumes attached.
- `checkIfRootVolumeIsEBS` - Checks if the target instance's root
  volume type is EBS.
- `checkIfTargetInstanceIsInASG` - Checks if the target instance is
  a part of an Amazon EC2 Auto Scaling group.
- `endOfPreliminaryChecksBranch` - End of the Preliminary checks
  branch.
- `startOfTestBranch` - Branches to the Testing workflow.
- `createTestImage` - Creates a test AMI of the target instance.
- `launchTestInstanceInSameSubnet` - Launches a test instance from
  the test AMI using the same configuration as target instance.
- `cleanupTestInstance` - Terminates the test instance.
- `endOfTestBranch` - End of the Testing branch.
- `checkIfTestingBranchSucceeded` - Checks the status of the
  Testing branch.
- `approvalToStopTargetInstance` - Waits for approval from the
  designated principals to stop the target instance.
- `stopTargetEC2Instance` - Stops the target instance.
- `forceStopTargetEC2Instance` - Force stops the target instance
  only if the previous step fails to stop the instance.
- `startOfCloneAndMigrateBranch` - Branches to the
  Clone&Migrate workflow.
- `createBackupImage` - Creates an AMI of the target instance to
  serve as a backup.
- `launchInstanceInSameSubnet` - Launches a new instance from the
  backup AMI using the same configuration as the source instance.
- `waitForClonedInstanceToPassStatusChecks` - Waits for the newly
  created instance to pass all status checks.
- `verifySSMConnectivityForClonedInstance` - Verifies that the
  newly created instance is managed by Systems Manager.
- `checkAndInstallENADrivers` - Checks if ENA drivers are installed
  on the newly created instance, and installs the drivers if needed.
- `checkAndAddNVMEDrivers` - Checks if NVMe drivers are installed
  on the newly created instance, and installs the drivers if needed.
- `checkAndModifyFSTABEntries` - Checks if device names are used in
  `/etc/fstab` and replaces them with UUIDs if needed.
- `stopClonedInstance` - Stops the newly created instance.
- `forceStopClonedInstance` - Force stops the newly created
  instance only if the previous step fails to stop the instance.
- `checkENAAttributeForClonedInstance` - Checks if the enhanced
  networking attribute is turned on for the newly created instance.
- `setNitroInstanceTypeForClonedInstance` - Changes the instance
  type for the newly created instance to the Nitro instance
  type that you specify.
- `startClonedInstance` - Starts the newly created instance whose
  instance type you changed.
- `approvalForCreatingImageAfterDriversInstallation` - If the
  instance successfully starts as a Nitro instance type, the
  automation waits for approval from the required principals. If approval is
  provided, an AMI is created to be used as a Golden AMI.
- `createImageAfterDriversInstallation` - Creates an AMI to be
  used as a Golden AMI.
- `endOfCloneAndMigrateBranch` - End of
  Clone&Migrate branch.
- `cleanupTestImage` - Deregisters the AMI created for testing.
- `failureHandling` - Checks if you chose to terminate resources on
  failure.
- `onFailureTerminateClonedInstance` - Terminates the newly created
  instance if the automation fails.
- `onFailurecleanupTestImage` - Deregisters the AMI created for
  testing.
- `onFailureApprovalToStartTargetInstance` - If the automation
  fails, waits for approval from the designated principals to start the target
  instance.
- `onFailureStartTargetInstance` - If the automation fails, starts
  the target instance.
  **Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:DescribeAutomationExecutions`
- `ssm:DescribeInstanceInformation`
- `ssm:DescribeAutomationStepExecutions`
- `ssm:SendCommand`
- `ssm:GetAutomationExecution`
- `ssm:ListCommands`
- `ssm:ListCommandInvocations`
- `ec2:DescribeInstances`
- `ec2:DescribeInstanceTypeOfferings`
- `ec2:DescribeInstanceTypes`
- `ec2:DescribeImages`
- `ec2:CreateImage`
- `ec2:RunInstances`
- `ec2:DescribeInstanceStatus`
- `ec2:DeregisterImage`
- `ec2:DeleteSnapshot`
- `ec2:TerminateInstances`
- `ec2:StartInstances`
- `ec2:DescribeKeyPairs`
- `ec2:StopInstances`
- `kms:CreateGrant*`
- `kms:ReEncrypt`
- `ec2:ModifyInstanceAttribute`
- `ec2:DetachVolume`
- `ec2:AttachVolume`
- `ec2:DescribeVolumes`
- `autoscaling:DescribeAutoScalingInstances`
- `iam:PassRole`
- `ec2:CreateTags`
- `cloudformation:DescribeStackResources`

**Document Steps**

The `FullMigration` workflow runs the same steps as the
`Clone&Migrate` workflow and additionally performs the following
steps:

- `checkConcurrency` - Verifies that there is only one automation
  of this runbook targeting the Amazon EC2 instance that you specify. If the
  runbook finds another automation in progress targeting the same instance,
  the automation ends.
- `getTargetInstanceProperties` - Gathers details from the target
  instance.
- `checkRootVolumeTags` - Determines if the root volume of the
  target Amazon EC2 instance contains any AWS reserved tags.
- `cloneTargetInstanceAndMigrateToNitro` - Starts a child
  automation using the `AWS-CloneXenInstanceToNitro` runbook.
- `branchOnTheOperationType` - Branches on the value that you
  specify for the `OperationType` parameter.
- `getClonedInstanceId` - Retrieves the ID of the newly launched
  instance from the child automation.
- `checkIfRootVolumeIsBasedOnLVM` - Determines if the root
  partition is managed by LVM.
- `branchOnTheRootVolumeLVMStatus` - If the minimum required
  approvals are received from the principals, the automation proceeds with the
  root volume replacement.
- `manualInstructionsInCaseOfLVM` - If the root volume is managed
  by LVM, the automation sends output containing instructions for how to
  manually replace the root volumes.
- `startOfReplaceRootEBSVolumeBranch` - Starts the Replace Root EBS
  Volume branch workflow.
- `checkIfTargetInstanceIsManagedByCFN` - Determines if the target
  instance is managed by an AWS CloudFormation stack.
- `branchOnCFNStackStatus` - Branches based on the status of the
  CloudFormation stack.
- `approvalForRootVolumesReplacement(WithCFN)` - If the target
  instance was launched by CloudFormation, the automation waits for approval after
  the newly launched instance successfully starts as a Nitro
  instance type. When approvals are provided, the Amazon EBS volumes of the target
  instance are replaced with the root volumes from the newly launched
  instance.
- `approvalForRootVolumesReplacement` - Waits for approval after
  the newly launched instance successfully starts as a Nitro
  instance type. When approvals are provided, the Amazon EBS volumes of the target
  instance are replaced with the root volumes from the newly launched
  instance.
- `assertIfTargetEC2InstanceIsStillStopped` - Verifies that the
  target instance is in a `stopped` state before replacing the root
  volume.
- `stopTargetInstanceForRootVolumeReplacement` - If the target
  instance is running, the automation stops the instance before replacing the
  root volume.
- `forceStopTargetInstanceForRootVolumeReplacement` - Force stops
  the target instance if the previous step fails.
- `stopClonedInstanceForRootVolumeReplacement` - Stops the newly
  created instance before replacing the Amazon EBS volumes.
- `forceStopClonedInstanceForRootVolumeReplacement` - Force stops
  the newly created instance if the previous step fails.
- `getBlockDeviceMappings` - Retrieves the block device mappings
  for both the target and newly created instances.
- `replaceRootEbsVolumes` - Replaces the root volume of the target
  instance with the root volume of the newly created instance.
- `EndOfReplaceRootEBSVolumeBranch` - End of Replace Root EBS
  Volume branch workflow.
- `checkENAAttributeForTargetInstance` - Checks if the enhanced
  networking (ENA) attribute is turned on for the target Amazon EC2
  instance.
- `enableENAAttributeForTargetInstance` - Turns on the ENA
  attribute for the target Amazon EC2 instance if needed.
- `setNitroInstanceTypeForTargetInstance` - Changes the target
  instance to the Nitro instance type that you specify.
- `replicateRootVolumeTags` - Replicates the tags on the root Amazon EBS
  volume from the target Amazon EC2 instance.
- `startTargetInstance` - Starts the target Amazon EC2 instance after
  changing the instance type.
- `onFailureStopTargetEC2Instance` - Stops the target Amazon EC2
  instance if it fails to start as a Nitro instance
  type.
- `onFailureForceStopTargetEC2Instance` - Force stops the target
  Amazon EC2 instance if the previous step fails.
- `OnFailureRevertOriginalInstanceType` - Reverts the target Amazon EC2
  instance to the original instance type if the target instance fails to start
  as a Nitro instance type.
- `onFailureRollbackRootVolumeReplacement` - Reverts all the
  changes made by the `replaceRootEbsVolumes` step if
  needed.
- `onFailureApprovalToStartTargetInstance` - Waits for designated
  principal's approval to start the target Amazon EC2 instance after rolling back
  the previous changes.
- `onFailureStartTargetInstance` - Starts the target Amazon EC2
  instance.
- `terminateClonedEC2Instance` - Terminates the cloned Amazon EC2
  instance after replacing the root Amazon EBS volume.
