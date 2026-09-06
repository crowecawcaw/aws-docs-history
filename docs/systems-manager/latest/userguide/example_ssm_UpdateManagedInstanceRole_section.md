

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `UpdateManagedInstanceRole` with a CLI
<a name="example_ssm_UpdateManagedInstanceRole_section"></a>

The following code examples show how to use `UpdateManagedInstanceRole`.

------
#### [ CLI ]

**AWS CLI**  
**To update the IAM role of a managed instance**  
The following `update-managed-instance-role` example updates the IAM instance profile of a managed instance.  

```
aws ssm update-managed-instance-role \
    --instance-id {{"mi-08ab247cdfEXAMPLE"}} \
    --iam-role {{"ExampleRole"}}
```
This command produces no output.  
For more information, see [Step 4: Create an IAM Instance Profile for Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [UpdateManagedInstanceRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-managed-instance-role.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example updates the role of a managed instance. There is no output if the command succeeds.**  

```
Update-SSMManagedInstanceRole -InstanceId "mi-08ab247cdf1046573" -IamRole "AutomationRole"
```
+  For API details, see [UpdateManagedInstanceRole](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example updates the role of a managed instance. There is no output if the command succeeds.**  

```
Update-SSMManagedInstanceRole -InstanceId "mi-08ab247cdf1046573" -IamRole "AutomationRole"
```
+  For API details, see [UpdateManagedInstanceRole](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.