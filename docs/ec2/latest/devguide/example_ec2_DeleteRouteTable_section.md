

# Use `DeleteRouteTable` with a CLI
<a name="example_ec2_DeleteRouteTable_section"></a>

The following code examples show how to use `DeleteRouteTable`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Create a basic virtual private network](example_vpc_GettingStartedCLI_section.md) 
+  [Getting started with graph databases](example_ec2_GettingStarted_064_section.md) 
+  [Virtual private network with private servers](example_vpc_GettingStartedPrivate_section.md) 
+  [Working with network peering connections](example_ec2_GettingStarted_015_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To delete a route table**  
This example deletes the specified route table. If the command succeeds, no output is returned.  
Command:  

```
aws ec2 delete-route-table --route-table-id {{rtb-22574640}}
```
+  For API details, see [DeleteRouteTable](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-route-table.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example deletes the specified route table. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**  

```
Remove-EC2RouteTable -RouteTableId rtb-1a2b3c4d
```
**Output:**  

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2RouteTable (DeleteRouteTable)" on Target "rtb-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteRouteTable](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example deletes the specified route table. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**  

```
Remove-EC2RouteTable -RouteTableId rtb-1a2b3c4d
```
**Output:**  

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2RouteTable (DeleteRouteTable)" on Target "rtb-1a2b3c4d".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteRouteTable](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.