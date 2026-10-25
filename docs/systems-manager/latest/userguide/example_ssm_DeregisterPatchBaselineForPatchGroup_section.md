

# Use `DeregisterPatchBaselineForPatchGroup` with a CLI
<a name="example_ssm_DeregisterPatchBaselineForPatchGroup_section"></a>

The following code examples show how to use `DeregisterPatchBaselineForPatchGroup`.

------
#### [ CLI ]

**AWS CLI**  
**To deregister a patch group from a patch baseline**  
The following `deregister-patch-baseline-for-patch-group` example deregisters the specified patch group from the specified patch baseline.  

```
aws ssm deregister-patch-baseline-for-patch-group \
    --patch-group {{"Production"}} \
    --baseline-id {{"pb-0ca44a362fEXAMPLE"}}
```
Output:  

```
{
  "PatchGroup":"Production",
  "BaselineId":"pb-0ca44a362fEXAMPLE"
}
```
For more information, see [Add a Patch Group to a Patch Baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-patchbaseline.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DeregisterPatchBaselineForPatchGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/deregister-patch-baseline-for-patch-group.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deregisters a patch group from a patch baseline.**  

```
Unregister-SSMPatchBaselineForPatchGroup -BaselineId "pb-045f10b4f382baeda" -PatchGroup "Production"
```
**Output:**  

```
BaselineId           PatchGroup
----------           ----------
pb-045f10b4f382baeda Production
```
+  For API details, see [DeregisterPatchBaselineForPatchGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deregisters a patch group from a patch baseline.**  

```
Unregister-SSMPatchBaselineForPatchGroup -BaselineId "pb-045f10b4f382baeda" -PatchGroup "Production"
```
**Output:**  

```
BaselineId           PatchGroup
----------           ----------
pb-045f10b4f382baeda Production
```
+  For API details, see [DeregisterPatchBaselineForPatchGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.