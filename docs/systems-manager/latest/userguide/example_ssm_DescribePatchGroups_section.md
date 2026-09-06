

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DescribePatchGroups` with a CLI
<a name="example_ssm_DescribePatchGroups_section"></a>

The following code examples show how to use `DescribePatchGroups`.

------
#### [ CLI ]

**AWS CLI**  
**To display patch group registrations**  
The following `describe-patch-groups` example lists the patch group registrations.  

```
aws ssm describe-patch-groups
```
Output:  

```
{
    "Mappings": [
        {
            "PatchGroup": "Production",
            "BaselineIdentity": {
                "BaselineId": "pb-0123456789abcdef0",
                "BaselineName": "ProdPatching",
                "OperatingSystem": "WINDOWS",
                "BaselineDescription": "Patches for Production",
                "DefaultBaseline": false
            }
        },
        {
            "PatchGroup": "Development",
            "BaselineIdentity": {
                "BaselineId": "pb-0713accee01234567",
                "BaselineName": "DevPatching",
                "OperatingSystem": "WINDOWS",
                "BaselineDescription": "Patches for Development",
                "DefaultBaseline": true
            }
        },
        ...
    ]
}
```
For more information, see Create a Patch Group <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-tagging.html>\_\_ and [Add a Patch Group to a Patch Baseline](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-patchbaseline.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DescribePatchGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-groups.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example lists the patch group registrations.**  

```
Get-SSMPatchGroup
```
**Output:**  

```
BaselineIdentity                                           PatchGroup
----------------                                           ----------
Amazon.SimpleSystemsManagement.Model.PatchBaselineIdentity Production
```
+  For API details, see [DescribePatchGroups](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example lists the patch group registrations.**  

```
Get-SSMPatchGroup
```
**Output:**  

```
BaselineIdentity                                           PatchGroup
----------------                                           ----------
Amazon.SimpleSystemsManagement.Model.PatchBaselineIdentity Production
```
+  For API details, see [DescribePatchGroups](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.