

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DeleteActivation` with a CLI
<a name="example_ssm_DeleteActivation_section"></a>

The following code examples show how to use `DeleteActivation`.

------
#### [ CLI ]

**AWS CLI**  
**To delete a managed instance activation**  
The following `delete-activation` example deletes a managed instance activation.  

```
aws ssm delete-activation \
    --activation-id {{"aa673477-d926-42c1-8757-1358cEXAMPLE"}}
```
This command produces no output.  
For more information, see [Setting Up AWS Systems Manager for Hybrid Environments](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DeleteActivation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-activation.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes an activation. There is no output if the command succeeds.**  

```
Remove-SSMActivation -ActivationId "08e51e79-1e36-446c-8e63-9458569c1363"
```
+  For API details, see [DeleteActivation](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes an activation. There is no output if the command succeeds.**  

```
Remove-SSMActivation -ActivationId "08e51e79-1e36-446c-8e63-9458569c1363"
```
+  For API details, see [DeleteActivation](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.