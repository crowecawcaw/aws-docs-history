

# `AWS-UpdateLinuxAmi`
<a name="automation-aws-updatelinuxami"></a>

**Description**

Update an Amazon Machine Image (AMI) with Linux distribution packages and Amazon software.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWS-UpdateLinuxAmi)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux

**Parameters**
+ AutomationAssumeRole

  Type: String

  Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user that starts this runbook.

  Allowed Pattern: `^$|^arn:aws[a-z0-9-]*:iam::(\d{12}|\{\{global:ACCOUNT_ID\}\}):role/[\w/.@+=,-]{1,1017}$` 
  + Must be a valid IAM role ARN or an empty string. System variable `{{global:ACCOUNT_ID}}` can be used in place of the AWS Account ID in the arn. 
+ ExcludePackages

  Type: String

  Default: none

  Description: (Optional) Names of packages to hold back from updates, under all conditions. By default ("none"), no package is excluded.

  Allowed Pattern: `^(none|[a-zA-Z0-9\s,._+:=<>()\[\]/*-]+)$` 
  + Must be "none" OR a comma-separated list of items consisting of letters, numbers, spaces, and the following characters: `, . _ + : = < > ( ) [ ] / * -` 
+ IamInstanceProfileName

  Type: String

  Default: ManagedInstanceProfile

  Description: (Required) The instance profile that enables Systems Manager to manage the instance.

  Allowed Pattern: `^[\w+=,.@-]{1,128}$` 
  + Must be between 1 and 128 characters and contain only letters, numbers, and these characters: `+ = , . @ - _` 
+ IncludePackages

  Type: String

  Default: all

  Description: (Optional) Only update these named packages. By default ("all"), all available updates are applied.

  Allowed Pattern: `^(all|[a-zA-Z0-9\s,._+:=<>()\[\]/*-]+)$` 
  + Must be "all" OR a comma-separated list of items consisting of letters, numbers, spaces, and the following characters: `, . _ + : = < > ( ) [ ] / * -` 
+ InstanceType

  Type: String

  Default: t2.micro

  Description: (Optional) Type of instance to launch as the workspace host. Instance types vary by Region.

  Allowed Pattern: `^[a-z0-9]+(-[a-z0-9]+)*\.[a-z0-9]+$` 
  + Must be in the format prefix.suffix where both parts contain lowercase letters and numbers, and the prefix may include hyphens
+ MetadataOptions

  Type: StringMap

  Default: {"HttpEndpoint": "enabled", "HttpTokens": "optional"}

  Description: (Optional) The metadata options for the instance. For more information, see [InstanceMetadataOptionsRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_InstanceMetadataOptionsRequest.html).

  Allowed Pattern: `^\{[^<>\$;|&\\]*\}$` 
  + Must be wrapped in curly braces { } and cannot contain these characters: `< > $ ; | & \` 
+ PostUpdateScript

  Type: String

  Default: none

  Description: (Optional) URL of a script to run after package updates are applied. Default ("none") is to not run a script.

  Allowed Pattern: `^(none|https?://[\w\-._~:/?#\[\]@!$&'()*+,;=%]+)$` 
  + Must be "none" OR a valid HTTP/HTTPS URL
+ PreUpdateScript

  Type: String

  Default: none

  Description: (Optional) URL of a script to run before updates are applied. Default ("none") is to not run a script.

  Allowed Pattern: `^(none|https?://[\w\-._~:/?#\[\]@!$&'()*+,;=%]+)$` 
  + Must be "none" OR a valid HTTP/HTTPS URL
+ SecurityGroupIds

  Type: String

  Description: (Required) A comma separated list of the IDs of the security groups you want to apply to the AMI.

  Allowed Pattern: `^sg-[a-z0-9]{8,17}$` 
  + Must start with "sg-" followed by 8-17 lowercase letters or numbers
+ SourceAmiId

  Type: String

  Description: (Required) The source Amazon Machine Image ID.

  Allowed Pattern: `^ami-[a-z0-9]{8,17}$` 
  + Must start with "ami-" followed by 8-17 lowercase letters or numbers
+ SubnetId

  Type: String

  Description: (Optional) The ID of the subnet you want to launch the instance into. If you have deleted your default VPC, this parameter is required.

  Allowed Pattern: `^$|^subnet-[a-z0-9]{8,17}$` 
  + Must be empty OR start with "subnet-" followed by 8-17 lowercase letters or numbers
+ TargetAmiName

  Type: String

  Default: UpdateLinuxAmi\_from\_{{SourceAmiId}}\_on\_{{global:DATE\_TIME}}

  Description: (Optional) The name of the new AMI that will be created. Default is a system-generated string including the source AMI id, and the creation time and date.

  Allowed Pattern: `^[a-zA-Z0-9()\[\]\{\} ./'@_:-]{3,128}$` 
  + Must be between 3 and 128 characters and contain only letters, numbers, spaces, and these characters: `( ) [ ] { } . / ' @ _ : -` 