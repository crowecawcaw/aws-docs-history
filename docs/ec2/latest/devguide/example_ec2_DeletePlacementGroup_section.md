

# Use `DeletePlacementGroup` with a CLI
<a name="example_ec2_DeletePlacementGroup_section"></a>

The following code examples show how to use `DeletePlacementGroup`.

------
#### [ CLI ]

**AWS CLI**  
**To delete a placement group**  
This example command deletes the specified placement group.  
Command:  

```
aws ec2 delete-placement-group --group-name {{my-cluster}}
```
+  For API details, see [DeletePlacementGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-placement-group.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes the specified placement group. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**  

```
Remove-EC2PlacementGroup -GroupName my-placement-group
```
**Output:**  

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2PlacementGroup (DeletePlacementGroup)" on Target "my-placement-group".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeletePlacementGroup](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes the specified placement group. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**  

```
Remove-EC2PlacementGroup -GroupName my-placement-group
```
**Output:**  

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2PlacementGroup (DeletePlacementGroup)" on Target "my-placement-group".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeletePlacementGroup](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.