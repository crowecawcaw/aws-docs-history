

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `ListTagsForResource` with a CLI
<a name="example_ssm_ListTagsForResource_section"></a>

The following code examples show how to use `ListTagsForResource`.

------
#### [ CLI ]

**AWS CLI**  
**To list the tags applied to a patch baseline**  
The following `list-tags-for-resource` example lists the tags for a patch baseline.  

```
aws ssm list-tags-for-resource \
    --resource-type {{"PatchBaseline"}} \
    --resource-id {{"pb-0123456789abcdef0"}}
```
Output:  

```
{
    "TagList": [
        {
            "Key": "Environment",
            "Value": "Production"
        },
        {
            "Key": "Region",
            "Value": "EMEA"
        }
    ]
}
```
For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference*.  
+  For API details, see [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-tags-for-resource.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example lists the tags for a maintenance window.**  

```
Get-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow"
```
**Output:**  

```
Key   Value
---   -----
Stack Production
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example lists the tags for a maintenance window.**  

```
Get-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow"
```
**Output:**  

```
Key   Value
---   -----
Stack Production
```
+  For API details, see [ListTagsForResource](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.