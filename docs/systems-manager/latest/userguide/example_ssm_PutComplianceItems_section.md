• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `PutComplianceItems` with a CLI

The following code examples show how to use `PutComplianceItems`.

CLI

**AWS CLI**

**To register a compliance type and compliance details to a designated instance**

This example registers the compliance type `Custom:AVCheck` to the specified managed instance. There is no output if the command succeeds.

Command:

```
`aws ssm put-compliance-items --resource-id `"i-1234567890abcdef0"` --resource-type `"ManagedInstance"` --compliance-type `"Custom:AVCheck"` --execution-summary `"ExecutionTime=2019-02-18T16:00:00Z"` --items `"Id=Version2.0,Title=ScanHost,Severity=CRITICAL,Status=COMPLIANT"``

```

- For API details, see
  [PutComplianceItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-compliance-items.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/put-compliance-items.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example writes a custom compliance item for the given managed instance**

```
$item = [Amazon.SimpleSystemsManagement.Model.ComplianceItemEntry]::new()
$item.Id = "07Jun2019-3"
$item.Severity="LOW"
$item.Status="COMPLIANT"
$item.Title="Fin-test-1 - custom"
Write-SSMComplianceItem -ResourceId mi-012dcb3ecea45b678 -ComplianceType Custom:VSSCompliant2 -ResourceType ManagedInstance -Item $item -ExecutionSummary_ExecutionTime "07-Jun-2019"

```

- For API details, see
  [PutComplianceItems](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example writes a custom compliance item for the given managed instance**

```
$item = [Amazon.SimpleSystemsManagement.Model.ComplianceItemEntry]::new()
$item.Id = "07Jun2019-3"
$item.Severity="LOW"
$item.Status="COMPLIANT"
$item.Title="Fin-test-1 - custom"
Write-SSMComplianceItem -ResourceId mi-012dcb3ecea45b678 -ComplianceType Custom:VSSCompliant2 -ResourceType ManagedInstance -Item $item -ExecutionSummary_ExecutionTime "07-Jun-2019"

```

- For API details, see
  [PutComplianceItems](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
