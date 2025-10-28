# `AWS-UpdateLinuxAmi`

**Description**

Update an Amazon Machine Image (AMI) with Linux distribution packages and Amazon
software.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateLinuxAmi "https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateLinuxAmi")

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

- ExcludePackages

Type: String

Default: none

Description: (Optional) Names of packages to hold back from updates, under
all conditions. By default ("none"), no package is excluded.

- IamInstanceProfileName

Type: String

Default: ManagedInstanceProfile

Description: (Required) The instance profile that enables Systems Manager to manage
the instance.

- IncludePackages

Type: String

Default: all

Description: (Optional) Only update these named packages. By default
("all"), all available updates are applied.

- InstanceType

Type: String

Default: t2.micro

Description: (Optional) Type of instance to launch as the workspace host.
Instance types vary by Region.

- MetadataOptions

Type: StringMap

Default: {"HttpEndpoint": "enabled", "HttpTokens": "optional"}

Description: (Optional) The metadata options for the instance. For more information, see [InstanceMetadataOptionsRequest](../../../AWSEC2/latest/APIReference/API_InstanceMetadataOptionsRequest.md "../../../AWSEC2/latest/APIReference/API_InstanceMetadataOptionsRequest.md").

- PostUpdateScript

Type: String

Default: none

Description: (Optional) URL of a script to run after package updates are
applied. Default ("none") is to not run a script.

- PreUpdateScript

Type: String

Default: none

Description: (Optional) URL of a script to run before updates are applied.
Default ("none") is to not run a script.

- SecurityGroupIds

Type: String

Description: (Required) A comma separated list of the IDs of the security
groups you want to apply to the AMI.

- SourceAmiId

Type: String

Description: (Required) The source Amazon Machine Image ID.

- SubnetId

Type: String

Description: (Optional) The ID of the subnet you want to launch the
instance into. If you have deleted your default VPC, this parameter is
required.

- TargetAmiName

Type: String

Default:
UpdateLinuxAmi_from\_{{SourceAmiId}}\_on\_{{global:DATE\_TIME}}

Description: (Optional) The name of the new AMI that will be created.
Default is a system-generated string including the source AMI id, and the
creation time and date.
