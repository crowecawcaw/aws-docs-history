# Use `RemoveRoleFromInstanceProfile` with a CLI

The following code examples show how to use `RemoveRoleFromInstanceProfile`.

CLI

**AWS CLI**

**To remove a role from an instance profile**

The following `remove-role-from-instance-profile` command removes the role named `Test-Role` from the instance
profile named `ExampleInstanceProfile`.

```
`aws iam remove-role-from-instance-profile \
 --instance-profile-name `ExampleInstanceProfile` \
 --role-name `Test-Role``

```

For more information, see [Using instance profiles](id_roles_use_switch-role-ec2_instance-profiles.md "id_roles_use_switch-role-ec2_instance-profiles.md") in the _AWS IAM User Guide_.

- For API details, see
  [RemoveRoleFromInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/remove-role-from-instance-profile.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/remove-role-from-instance-profile.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the role named `MyNewRole` from the EC2 instance profile named `MyNewRole`. An instance profile that is created in the IAM console always has the same name as the role, as in this example. If you create them in the API or CLI, then they can have different names.**

```
Remove-IAMRoleFromInstanceProfile -InstanceProfileName MyNewRole -RoleName MyNewRole -Force

```

- For API details, see
  [RemoveRoleFromInstanceProfile](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the role named `MyNewRole` from the EC2 instance profile named `MyNewRole`. An instance profile that is created in the IAM console always has the same name as the role, as in this example. If you create them in the API or CLI, then they can have different names.**

```
Remove-IAMRoleFromInstanceProfile -InstanceProfileName MyNewRole -RoleName MyNewRole -Force

```

- For API details, see
  [RemoveRoleFromInstanceProfile](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
