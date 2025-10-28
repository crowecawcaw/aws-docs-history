# `AWSSupport-CopyEC2Instance`

**Description**

The `AWSSupport-CopyEC2Instance` runbook provides an automated solution
for the procedure outlined in the Knowledge Center article [How do I move my EC2
instance to another subnet, Availability Zone, or VPC?](https://aws.amazon.com/premiumsupport/knowledge-center/move-ec2-instance/ "https://aws.amazon.com/premiumsupport/knowledge-center/move-ec2-instance/") The automation
branches depending on the values you specify for the `Region` and
`SubnetId` parameters.

If you specify a value for the `SubnetId` parameter but not a value for
the `Region` parameter, the automation creates an Amazon Machine Image (AMI) of
the target instance and launches a new instance from the AMI in the subnet you
specified.

If you specify a value for the `SubnetId` parameter and the
`Region` parameter, the automation creates an AMI of the target
instance, copies the AMI to the AWS Region you specified, and launches a new
instance from the AMI in the subnet you specified.

If you specify a value for the `Region` parameter but not a value for
the `SubnetId` parameter, the automation creates an AMI of the target
instance, copies the AMI to the Region you specified, and launches a new instance
from the AMI in the default subnet of your virtual private cloud (VPC) in the
destination Region.

If no value is specified for either the `Region` or
`SubnetId` parameters, the automation creates an AMI of the target
instance, and launches a new instance from the AMI in the default subnet of your
VPC.

To copy an AMI to a different Region, you must provide a value for the
`AutomationAssumeRole` parameter. If the automation times out during
the `waitForAvailableDestinationAmi` step, the AMI might still be
copying. If this is the case, you can wait for the copy to complete and launch the
instance manually.

Before running this automation, note the following:

- AMIs are based on Amazon Elastic Block Store (Amazon EBS) snapshots. For large file systems
  without a previous snapshot, AMI creation can take several hours. To
  decrease the AMI creation time, create an Amazon EBS snapshot before you create
  the AMI.
- Creating an AMI doesn't create a snapshot for instance store volumes on
  the instance. For information about backing up instance store volumes to
  Amazon EBS, see [How do
  I back up an instance store volume on my Amazon EC2 instance to
  Amazon EBS?](https://aws.amazon.com/premiumsupport/knowledge-center/back-up-instance-store-ebs/ "https://aws.amazon.com/premiumsupport/knowledge-center/back-up-instance-store-ebs/")
- The new Amazon EC2 instance has a different private IPv4 or public IPv6 IP
  address. You must update all references to the old IP addresses (for
  example, in DNS entries) with the new IP addresses that are assigned to the
  new instance. If you're using an Elastic IP address on your source instance,
  be sure to attach it to the new instance.
- Domain security identifier (SID) conflict issues can occur when the copy
  launches and tries to contact the domain. Before you capture the AMI, use
  Sysprep or remove the domain-joined instance from the domain to prevent
  conflict issues. For more information, see [How can I use Sysprep to create and install custom reusable Windows
  AMIs?](https://aws.amazon.com/premiumsupport/knowledge-center/sysprep-create-install-ec2-windows-amis/ "https://aws.amazon.com/premiumsupport/knowledge-center/sysprep-create-install-ec2-windows-amis/")

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CopyEC2Instance "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-CopyEC2Instance")

###### Important

We do not recommend using this runbook to copy Microsoft Active Directory
Domain Controller instances.

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- InstanceId

Type: String

Description: (Required) The ID of the instance that you want to
copy.

- KeyPair

Type: String

Description: (Optional) The key pair you want to associate with the new
copied instance. If you're copying the instance to a different Region, make
sure the key pair exists in the specified Region.

- Region

Type: String

Description: (Optional) The Region you want to copy the instance to. If
you specify a value for this parameter, but do not specify values for the
`SubnetId` and `SecurityGroupIds` parameters, the
automation attempts to launch the instance in the default VPC with the
default security group. If EC2-Classic is enabled in the destination Region,
the launch will fail.

- SubnetId

Type: String

Description: (Optional) The ID of the subnet you want to copy the instance
to. If EC2-Classic is enabled in the destination Region, you must provide a
value for this parameter.

- InstanceType

Type: String

Description: (Optional) The instance type the copied instance should be
launched as. If you do not specify a value for this parameter, the source
instance type is used. If the source instance type is not supported in the
Region the instance is being copied to, the automation fails.

- SecurityGroupIds

Type: String

Description: (Optional) A comma-separated list of security group IDs you
want to associate with the copied instance. If you do not specify a value
for this parameter, and the instance is not being copied to a different
Region, the security groups associated with the source instance are used. If
you're copying the instance to a different Region, the default security
group for the default VPC in the destination Region is used.

- KeepImageSourceRegion

Type: Boolean

Valid values: true | false

Default: true

Description: (Optional) If you specify `true` for this
parameter, the automation does not delete the AMI of the source instance.
If you specify `false` for this parameter, the automation
deregisters the AMI and deletes the associated snapshots.

- KeepImageDestinationRegion

Type: Boolean

Valid values: true | false

Default: true

Description: (Optional) If you specify `true` for this
parameter, the automation does not delete the AMI that is copied to the
Region you specified. If you specify `false` for this parameter,
the automation deregisters the AMI and deletes the associated
snapshots.

- NoRebootInstanceBeforeTakingImage

Type: Boolean

Valid values: true | false

Default: false

Description: (Optional) If you specify `true` for this
parameter, the source instance will not be restarted before creating the
AMI. When this option is used, file system integrity on the created image
can't be guaranteed.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ec2:CreateImage`
- `ec2:DeleteSnapshot`
- `ec2:DeregisterImage`
- `ec2:DescribeInstances`
- `ec2:DescribeImages`
- `ec2:RunInstances`
  If you're copying the instance to a different Region, you will also need the
  following permissions.

- `ec2:CopyImage`

**Document Steps**

- describeOriginalInstanceDetails - Gathers details from the instance to be
  copied.
- assertRootVolumeIsEbs - Checks if the root volume device type is
  `ebs`, and if not, ends the automation.
- evalInputParameters - Evaluates the values provided for the input
  parameters.
- createLocalAmi - Creates an AMI of the source instance.
- tagLocalAmi - Tags the AMI created in the previous step.
- branchAssertRegionIsSame - Branches based on whether the instance is being
  copied within the same Region or to a different Region.
- branchAssertSameRegionWithKeyPair - Branches based on whether a value was
  provided for the `KeyPair` parameter for an instance that's being
  copied within the same Region.
- sameRegionLaunchInstanceWithKeyPair - Launches an Amazon EC2 instance from the
  AMI of the source instance in the same subnet or the subnet you specify
  using the key pair that you specified.
- sameRegionLaunchInstanceWithoutKeyPair - Launches an Amazon EC2 instance from
  the AMI of the source instance in the same subnet or the subnet you
  specify without a key pair.
- copyAmiToRegion - Copies the AMI to the destination Region.
- waitForAvailableDestinationAmi - Waits for the copied AMI state to
  become `available`.
- destinationRegionLaunchInstance - Launches an Amazon EC2 Instance using the
  copied AMI.
- branchAssertDestinationAmiToDelete - Branches based on the value you
  provided for the `KeepImageDestinationRegion` parameter.
- deregisterDestinationAmiAndDeleteSnapshots - Deregisters the copied AMI
  and deletes associated snapshots.
- branchAssertSourceAmiTodelete - Branches based on the value you provided
  for the `KeepImageSourceRegion` parameter.
- deregisterSourceAmiAndDeleteSnapshots - Deregisters the AMI created from
  the source instance and deletes associated snapshots.
- sleep - Sleeps the automation for 2 seconds. This is a terminal
  step.

**Outputs**

sameRegionLaunchInstanceWithKeyPair.InstanceIds

sameRegionLaunchInstanceWithoutKeyPair.InstanceIds

destinationRegionLaunchInstance.DestinationInstanceId
