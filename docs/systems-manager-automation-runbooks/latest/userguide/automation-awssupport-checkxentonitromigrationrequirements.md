# `AWSSupport-CheckXenToNitroMigrationRequirements`

**Description**

The `AWSSupport-CheckXenToNitroMigrationRequirements` runbook verifies
that an Amazon Elastic Compute Cloud (Amazon EC2) instance meets the prerequistes to successfully change the
instance type from a Xen type instance to Nitro-based instance type. This automation
checks the following:

- The root device is an Amazon Elastic Block Store (Amazon EBS) volume.
- The `enaSupport` attribute is enabled.
- The ENA module is installed on the instance.
- The NVMe module is installed on the instance. If yes, the module is
  installed and a script verifies that the module is loaded in the
  `initramfs` image.
- Analyzes `/etc/fstab` and looks for block devices being
  mounted using device names.
- Determines whether the operating system (OS) uses predictable network
  interface names by default.
  This runbook supports the following operating systems:

- Red Hat Enterprise Linux
- CentOS
- Amazon Linux 2
- Amazon Linux
- Debian Server
- Ubuntu Server
- SUSE Linux Enterprise Server 15 SP2
- SUSE Linux Enterprise Server 12 SP5
  [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CheckXenToNitroMigrationRequirements "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CheckXenToNitroMigrationRequirements")

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

- InstanceId

Type: String

Default: false

Description: (Required) The ID of the Amazon EC2 instance which you want to
check prerequisites for before migrating to a Nitro-based instance
type.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:DescribeAutomationExecutions`
- `ssm:DescribeAutomationStepExecutions`
- `ssm:DescribeAutomationStepExecutions`
- `ssm:DescribeInstanceInformation`
- `ssm:DescribeInstanceProperties`
- `ssm:StartAutomationExecution`
- `ssm:GetAutomationExecution`
- `ssm:GetDocument`
- `ssm:ListCommands`
- `ssm:ListCommandInvocations`
- `ssm:ListDocuments`
- `ssm:StartAutomationExecution`
- `ssm:SendCommand`
- `iam:ListRoles`
- `ec2:DescribeInstances`
- `ec2:DescribeInstancesTypes`

**Document Steps**

- `aws:executeAwsApi` - Gathers details about the
  instance.
- `aws:executeAwsApi` - Gathers information about the hypervisor
  for the instance.
- `aws:branch` - Branches based on whether the target instance is
  already running a Nitro-based instance type.
- `aws:branch` - Checks whether the instance's OS is supported by
  Nitro-based instances.
- `aws:assertAwsResourceProperty` - Verifies the instance you
  specified is managed by Systems Manager, and that the status is `Online`.
- `aws:branch` - Branches based on whether the root device of the
  instance is an Amazon EBS volume.
- `aws:branch` - Branches based on whether the ENA attribute is
  enabled for the instance.
- `aws:runCommand` - Checks for ENA drivers on the
  instance.
- `aws:runCommand` - Checks for NVMe drivers on the
  instance.
- `aws:runCommand` - Checks the `fstab` file
  for unrecognized formats.
- `aws:runCommand` - Checks for predictable interface name
  configuration on the instance.
- `aws:executeScript` - Generates output based on previous
  steps.

**Outputs**

finalOutput.output - The results of the checks performed by the automation.
