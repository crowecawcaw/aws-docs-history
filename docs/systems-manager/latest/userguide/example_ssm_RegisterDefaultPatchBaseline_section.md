

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `RegisterDefaultPatchBaseline` with a CLI
<a name="example_ssm_RegisterDefaultPatchBaseline_section"></a>

The following code examples show how to use `RegisterDefaultPatchBaseline`.

------
#### [ CLI ]

**AWS CLI**  
**To set the default patch baseline**  
The following `register-default-patch-baseline` example registers the specified custom patch baseline as the default patch baseline for the operating system type that it supports.  

```
aws ssm register-default-patch-baseline \
    --baseline-id {{"pb-abc123cf9bEXAMPLE"}}
```
Output:  

```
{
    "BaselineId":"pb-abc123cf9bEXAMPLE"
}
```
The following `register-default-patch-baseline` example registers the default patch baseline provided by AWS for CentOS as the default patch baseline.  

```
aws ssm register-default-patch-baseline \
    --baseline-id {{"arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0574b43a65ea646ed"}}
```
Output:  

```
{
    "BaselineId":"pb-abc123cf9bEXAMPLE"
}
```
For more information, see [About Predefined and Custom Patch Baselines](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-baselines.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [RegisterDefaultPatchBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-default-patch-baseline.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example registers a patch baseline as the default patch baseline.**  

```
Register-SSMDefaultPatchBaseline -BaselineId "pb-03da896ca3b68b639"
```
**Output:**  

```
pb-03da896ca3b68b639
```
+  For API details, see [RegisterDefaultPatchBaseline](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example registers a patch baseline as the default patch baseline.**  

```
Register-SSMDefaultPatchBaseline -BaselineId "pb-03da896ca3b68b639"
```
**Output:**  

```
pb-03da896ca3b68b639
```
+  For API details, see [RegisterDefaultPatchBaseline](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.