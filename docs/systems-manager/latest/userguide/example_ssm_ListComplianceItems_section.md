

# Use `ListComplianceItems` with a CLI
<a name="example_ssm_ListComplianceItems_section"></a>

The following code examples show how to use `ListComplianceItems`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To list compliance items for a specific instance**  
The following `list-compliance-items` example lists all compliance items for the specified instance.  

```
aws ssm list-compliance-items \
    --resource-ids {{"i-1234567890abcdef0"}} \
    --resource-types {{"ManagedInstance"}}
```
Output:  

```
{
    "ComplianceItems": [
        {
            "ComplianceType": "Association",
            "ResourceType": "ManagedInstance",
            "ResourceId": "i-1234567890abcdef0",
            "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
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
            "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
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
    }
    ],
    "NextToken": "--token string truncated--"
}
```
For more information, see [Learn details about Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-about.html) in the *AWS Systems Manager User Guide*.  
**Example 2: To list compliance items for a specific instance and association ID**  
The following `list-compliance-items` example lists all compliance items for the specified instance and association ID.  

```
aws ssm list-compliance-items \
    --resource-ids {{"i-1234567890abcdef0"}} \
    --resource-types {{"ManagedInstance"}} \
    --filters {{"Key=ComplianceType,Values=Association,Type=EQUAL"}} {{"Key=Id,Values=a1b2c3d4-5678-90ab-cdef-EXAMPLE22222,Type=EQUAL"}}
```
Output:  

```
{
    "ComplianceItems": [
        {
            "ComplianceType": "Association",
            "ResourceType": "ManagedInstance",
            "ResourceId": "i-1234567890abcdef0",
            "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
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
        }
    ]
}
```
For more information, see [Learn details about Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-about.html) in the *AWS Systems Manager User Guide*.  
**Example 3: To list compliance items for an instance after a specific date and time**  
The following `list-compliance-items` example lists all compliance items for an instance after the specified date and time.  

```
aws ssm list-compliance-items \
    --resource-ids {{"i-1234567890abcdef0"}} \
    --resource-types {{"ManagedInstance"}} \
    --filters {{"Key=ExecutionTime,Values=2019-02-18T16:00:00Z,Type=GREATER_THAN"}}
```
Output:  

```
{
    "ComplianceItems": [
        {
            "ComplianceType": "Association",
            "ResourceType": "ManagedInstance",
            "ResourceId": "i-1234567890abcdef0",
            "Id": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
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
        }
    ]
}
```
For more information, see [Learn details about Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/compliance-about.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [ListComplianceItems](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-compliance-items.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

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
+  For API details, see [ListComplianceItems](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

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
+  For API details, see [ListComplianceItems](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.