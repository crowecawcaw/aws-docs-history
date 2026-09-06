

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `ModifyDocumentPermission` with a CLI
<a name="example_ssm_ModifyDocumentPermission_section"></a>

The following code examples show how to use `ModifyDocumentPermission`.

------
#### [ CLI ]

**AWS CLI**  
**To modify document permissions**  
The following `modify-document-permission` example shares a Systems Manager document publicly.  

```
aws ssm modify-document-permission \
    --name {{"Example"}} \
    --permission-type {{"Share"}} \
    --account-ids-to-add {{"All"}}
```
This command produces no output.  
For more information, see [Share a Systems Manager Document](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-how-to-share.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [ModifyDocumentPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/modify-document-permission.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example adds "share" permissions to all accounts for a document. There is no output if the command succeeds.**  

```
Edit-SSMDocumentPermission -Name "RunShellScript" -PermissionType "Share" -AccountIdsToAdd all
```
**Example 2: This example adds "share" permissions to a specific account for a document. There is no output if the command succeeds.**  

```
Edit-SSMDocumentPermission -Name "RunShellScriptNew" -PermissionType "Share" -AccountIdsToAdd "123456789012"
```
+  For API details, see [ModifyDocumentPermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example adds "share" permissions to all accounts for a document. There is no output if the command succeeds.**  

```
Edit-SSMDocumentPermission -Name "RunShellScript" -PermissionType "Share" -AccountIdsToAdd all
```
**Example 2: This example adds "share" permissions to a specific account for a document. There is no output if the command succeeds.**  

```
Edit-SSMDocumentPermission -Name "RunShellScriptNew" -PermissionType "Share" -AccountIdsToAdd "123456789012"
```
+  For API details, see [ModifyDocumentPermission](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.