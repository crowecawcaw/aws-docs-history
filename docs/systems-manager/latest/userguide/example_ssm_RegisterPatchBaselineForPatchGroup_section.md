

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `RegisterPatchBaselineForPatchGroup` with a CLI
<a name="example_ssm_RegisterPatchBaselineForPatchGroup_section"></a>

The following code examples show how to use `RegisterPatchBaselineForPatchGroup`.

------
#### [ CLI ]

**AWS CLI**  
**To register a patch baseline for a patch group**  
The following `register-patch-baseline-for-patch-group` example registers a patch baseline for a patch group.  

```
aws ssm register-patch-baseline-for-patch-group \
    --baseline-id {{"pb-045f10b4f382baeda"}} \
    --patch-group {{"Production"}}
```
Output:  

```
{
    "BaselineId": "pb-045f10b4f382baeda",
    "PatchGroup": "Production"
}
```
For more information, see Create a Patch Group <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-tagging.html>\_\_ and [Add a Patch Group to a Patch Baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-patchbaseline.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [RegisterPatchBaselineForPatchGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/register-patch-baseline-for-patch-group.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example registers a patch baseline for a patch group.**  

```
Register-SSMPatchBaselineForPatchGroup -BaselineId "pb-03da896ca3b68b639" -PatchGroup "Production"
```
**Output:**  

```
BaselineId           PatchGroup
----------           ----------
pb-03da896ca3b68b639 Production
```
+  For API details, see [RegisterPatchBaselineForPatchGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example registers a patch baseline for a patch group.**  

```
Register-SSMPatchBaselineForPatchGroup -BaselineId "pb-03da896ca3b68b639" -PatchGroup "Production"
```
**Output:**  

```
BaselineId           PatchGroup
----------           ----------
pb-03da896ca3b68b639 Production
```
+  For API details, see [RegisterPatchBaselineForPatchGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.