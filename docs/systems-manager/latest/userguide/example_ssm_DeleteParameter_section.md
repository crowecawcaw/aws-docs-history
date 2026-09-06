

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DeleteParameter` with a CLI
<a name="example_ssm_DeleteParameter_section"></a>

The following code examples show how to use `DeleteParameter`.

------
#### [ CLI ]

**AWS CLI**  
**To delete a parameter**  
The following `delete-parameter` example deletes the specified single parameter.  

```
aws ssm delete-parameter \
    --name {{"MyParameter"}}
```
This command produces no output.  
For more information, see [Working with Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-working-with.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DeleteParameter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/delete-parameter.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes a parameter. There is no output if the command succeeds.**  

```
Remove-SSMParameter -Name "helloWorld"
```
+  For API details, see [DeleteParameter](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes a parameter. There is no output if the command succeeds.**  

```
Remove-SSMParameter -Name "helloWorld"
```
+  For API details, see [DeleteParameter](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.