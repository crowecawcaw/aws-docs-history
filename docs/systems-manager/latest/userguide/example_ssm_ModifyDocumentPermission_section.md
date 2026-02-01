• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `ModifyDocumentPermission` with a CLI

The following code examples show how to use `ModifyDocumentPermission`.

CLI

**AWS CLI**

**To modify document permissions**

The following `modify-document-permission` example shares a Systems Manager document publicly.

```
`aws ssm modify-document-permission \
 --name `"Example"` \
 --permission-type `"Share"` \
 --account-ids-to-add `"All"``

```

This command produces no output.

For more information, see [Share a Systems Manager Document](ssm-how-to-share.md "ssm-how-to-share.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [ModifyDocumentPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/modify-document-permission.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/modify-document-permission.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example adds "share" permissions to all accounts for a document. There is no output if the command succeeds.**

```
Edit-SSMDocumentPermission -Name "RunShellScript" -PermissionType "Share" -AccountIdsToAdd all

```

**Example 2: This example adds "share" permissions to a specific account for a document. There is no output if the command succeeds.**

```
Edit-SSMDocumentPermission -Name "RunShellScriptNew" -PermissionType "Share" -AccountIdsToAdd "123456789012"

```

- For API details, see
  [ModifyDocumentPermission](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example adds "share" permissions to all accounts for a document. There is no output if the command succeeds.**

```
Edit-SSMDocumentPermission -Name "RunShellScript" -PermissionType "Share" -AccountIdsToAdd all

```

**Example 2: This example adds "share" permissions to a specific account for a document. There is no output if the command succeeds.**

```
Edit-SSMDocumentPermission -Name "RunShellScriptNew" -PermissionType "Share" -AccountIdsToAdd "123456789012"

```

- For API details, see
  [ModifyDocumentPermission](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
