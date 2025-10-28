# Use `AddRoleToInstanceProfile` with a CLI

The following code examples show how to use `AddRoleToInstanceProfile`.

CLI

**AWS CLI**

**To add a role to an instance profile**

The following `add-role-to-instance-profile` command adds the role named `S3Access` to the instance profile named `Webserver`.

```
`aws iam add-role-to-instance-profile \
 --role-name `S3Access` \
 --instance-profile-name `Webserver``

```

This command produces no output.

To create an instance profile, use the `create-instance-profile` command.

For more information, see [Using an IAM role to grant permissions to applications running on Amazon EC2 instances](id_roles_use_switch-role-ec2.md "id_roles_use_switch-role-ec2.md") in the _AWS IAM User Guide_.

- For API details, see
  [AddRoleToInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-role-to-instance-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/add-role-to-instance-profile.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This command adds the role named `S3Access` to an existing instance profile named `webserver`.
To create the instance profile, use the `New-IAMInstanceProfile` command. After you create the instance profile and associate it with a role using this command, you can attach it to an EC2 instance. To do that, use the `New-EC2Instance` cmdlet with either the `InstanceProfile_Arn` or the `InstanceProfile-Name` parameter to launch the new instance.**

```
Add-IAMRoleToInstanceProfile -RoleName "S3Access" -InstanceProfileName "webserver"

```

- For API details, see
  [AddRoleToInstanceProfile](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This command adds the role named `S3Access` to an existing instance profile named `webserver`.
To create the instance profile, use the `New-IAMInstanceProfile` command. After you create the instance profile and associate it with a role using this command, you can attach it to an EC2 instance. To do that, use the `New-EC2Instance` cmdlet with either the `InstanceProfile_Arn` or the `InstanceProfile-Name` parameter to launch the new instance.**

```
Add-IAMRoleToInstanceProfile -RoleName "S3Access" -InstanceProfileName "webserver"

```

- For API details, see
  [AddRoleToInstanceProfile](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
