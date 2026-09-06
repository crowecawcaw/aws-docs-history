

# Use `RemoveRoleFromInstanceProfile` with a CLI
<a name="iam_example_iam_RemoveRoleFromInstanceProfile_section"></a>

The following code examples show how to use `RemoveRoleFromInstanceProfile`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Getting started with managed streaming](iam_example_ec2_GettingStarted_057_section.md) 
+  [Run CPU stress tests on virtual machine instances using fault injection](iam_example_iam_GettingStarted_069_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To remove a role from an instance profile**  
The following `remove-role-from-instance-profile` command removes the role named `Test-Role` from the instance profile named `ExampleInstanceProfile`.  

```
aws iam remove-role-from-instance-profile \
    --instance-profile-name {{ExampleInstanceProfile}} \
    --role-name {{Test-Role}}
```
For more information, see [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) in the *AWS IAM User Guide*.  
+  For API details, see [RemoveRoleFromInstanceProfile](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/remove-role-from-instance-profile.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes the role named `MyNewRole` from the EC2 instance profile named `MyNewRole`. An instance profile that is created in the IAM console always has the same name as the role, as in this example. If you create them in the API or CLI, then they can have different names.**  

```
Remove-IAMRoleFromInstanceProfile -InstanceProfileName MyNewRole -RoleName MyNewRole -Force
```
+  For API details, see [RemoveRoleFromInstanceProfile](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes the role named `MyNewRole` from the EC2 instance profile named `MyNewRole`. An instance profile that is created in the IAM console always has the same name as the role, as in this example. If you create them in the API or CLI, then they can have different names.**  

```
Remove-IAMRoleFromInstanceProfile -InstanceProfileName MyNewRole -RoleName MyNewRole -Force
```
+  For API details, see [RemoveRoleFromInstanceProfile](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.