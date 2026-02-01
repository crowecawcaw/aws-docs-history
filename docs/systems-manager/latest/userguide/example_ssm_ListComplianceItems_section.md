• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `ListComplianceItems` with a CLI

The following code examples show how to use `ListComplianceItems`.

CLI

**AWS CLI**

**To list compliance items for a specific instance**

This example lists all compliance items for the specified instance.

Command:

```
`aws ssm list-compliance-items --resource-ids `"i-1234567890abcdef0"` --resource-types `"ManagedInstance"``

```

Output:

```
{
  "ComplianceItems": [
      {
          "ComplianceType": "Association",
          "ResourceType": "ManagedInstance",
          "ResourceId": "i-1234567890abcdef0",
          "Id": "8dfe3659-4309-493a-8755-0123456789ab",
          "Title": "",
          "Status": "COMPLIANT",
          "Severity": "UNSPECIFIED",
          "ExecutionSummary": {
              "ExecutionTime": 1550408470.0
          },
          "Details": {
              "DocumentName": "AWS-GatherSoftwareInventory",
              "DocumentVersion": "1"
          }
      },
      {
          "ComplianceType": "Association",
          "ResourceType": "ManagedInstance",
          "ResourceId": "i-1234567890abcdef0",
          "Id": "e4c2ed6d-516f-41aa-aa2a-0123456789ab",
          "Title": "",
          "Status": "COMPLIANT",
          "Severity": "UNSPECIFIED",
          "ExecutionSummary": {
              "ExecutionTime": 1550508475.0
          },
          "Details": {
              "DocumentName": "AWS-UpdateSSMAgent",
              "DocumentVersion": "1"
          }
      },
              ...
  ],
  "NextToken": "--token string truncated--"
}
```

**To list compliance items for a specific instance and association ID**

This example lists all compliance items for the specified instance and association ID.

Command:

```
`aws ssm list-compliance-items --resource-ids `"i-1234567890abcdef0"` --resource-types `"ManagedInstance"` --filters `"Key=ComplianceType,Values=Association,Type=EQUAL"` `"Key=Id,Values=e4c2ed6d-516f-41aa-aa2a-0123456789ab,Type=EQUAL"``

```

**To list compliance items for a instance after a specific date and time**

This example lists all compliance items for an instance after the specified date and time.

Command:

```
`aws ssm list-compliance-items --resource-ids `"i-1234567890abcdef0"` --resource-types `"ManagedInstance"` --filters `"Key=ExecutionTime,Values=2019-02-18T16:00:00Z,Type=GREATER_THAN"``

```

- For API details, see
  [ListComplianceItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-compliance-items.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-compliance-items.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists compliance items list for the given resource id and type, filtering compliance-type being 'Association'**

```
Get-SSMComplianceItemList -ResourceId i-1a2caf345f67d0dc2 -ResourceType ManagedInstance -Filter @{Key="ComplianceType";Values="Association"}

```

**Output:**

```
ComplianceType   : Association
Details          : {[DocumentName, AWS-GatherSoftwareInventory], [DocumentVersion, 1]}
ExecutionSummary : Amazon.SimpleSystemsManagement.Model.ComplianceExecutionSummary
Id               : 123a45a1-c234-1234-1245-67891236db4e
ResourceId       : i-1a2caf345f67d0dc2
ResourceType     : ManagedInstance
Severity         : UNSPECIFIED
Status           : COMPLIANT
Title            :
```

- For API details, see
  [ListComplianceItems](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists compliance items list for the given resource id and type, filtering compliance-type being 'Association'**

```
Get-SSMComplianceItemList -ResourceId i-1a2caf345f67d0dc2 -ResourceType ManagedInstance -Filter @{Key="ComplianceType";Values="Association"}

```

**Output:**

```
ComplianceType   : Association
Details          : {[DocumentName, AWS-GatherSoftwareInventory], [DocumentVersion, 1]}
ExecutionSummary : Amazon.SimpleSystemsManagement.Model.ComplianceExecutionSummary
Id               : 123a45a1-c234-1234-1245-67891236db4e
ResourceId       : i-1a2caf345f67d0dc2
ResourceType     : ManagedInstance
Severity         : UNSPECIFIED
Status           : COMPLIANT
Title            :
```

- For API details, see
  [ListComplianceItems](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
