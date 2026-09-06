

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `ListDocuments` with a CLI
<a name="example_ssm_ListDocuments_section"></a>

The following code examples show how to use `ListDocuments`.

------
#### [ CLI ]

**AWS CLI**  
**Example 1: To list documents**  
The following `list-documents` example lists documents owned by the requesting account tagged with the custom tag.  

```
aws ssm list-documents \
    --filters {{Key=Owner,Values=Self}} {{Key=tag:DocUse,Values=Testing}}
```
Output:  

```
{
    "DocumentIdentifiers": [
        {
            "Name": "Example",
            "Owner": "29884EXAMPLE",
            "PlatformTypes": [
                "Windows",
                "Linux"
            ],
            "DocumentVersion": "1",
            "DocumentType": "Automation",
            "SchemaVersion": "0.3",
            "DocumentFormat": "YAML",
            "Tags": [
                {
                    "Key": "DocUse",
                    "Value": "Testing"
                }
            ]
        }
    ]
}
```
For more information, see [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html) in the *AWS Systems Manager User Guide*.  
**Example 2: To list shared documents**  
The following `list-documents` example lists shared documents, including private shared documents not owned by AWS.  

```
aws ssm list-documents \
    --filters {{Key=Name,Values=sharedDocNamePrefix}}  {{Key=Owner,Values=Private}}
```
Output:  

```
{
    "DocumentIdentifiers": [
        {
            "Name": "Example",
            "Owner": "12345EXAMPLE",
            "PlatformTypes": [
                "Windows",
                "Linux"
            ],
            "DocumentVersion": "1",
            "DocumentType": "Command",
            "SchemaVersion": "0.3",
            "DocumentFormat": "YAML",
            "Tags": []
        }
    ]
}
```
For more information, see [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [ListDocuments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-documents.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: Lists all the configuration documents in your account.**  

```
Get-SSMDocumentList
```
**Output:**  

```
DocumentType    : Command
DocumentVersion : 1
Name            : AWS-ApplyPatchBaseline
Owner           : Amazon
PlatformTypes   : {Windows}
SchemaVersion   : 1.2

DocumentType    : Command
DocumentVersion : 1
Name            : AWS-ConfigureAWSPackage
Owner           : Amazon
PlatformTypes   : {Windows, Linux}
SchemaVersion   : 2.0

DocumentType    : Command
DocumentVersion : 1
Name            : AWS-ConfigureCloudWatch
Owner           : Amazon
PlatformTypes   : {Windows}
SchemaVersion   : 1.2
...
```
**Example 2: This example retrieves all automation documents with name matchingi 'Platform'**  

```
Get-SSMDocumentList -DocumentFilterList @{Key="DocumentType";Value="Automation"} | Where-Object Name -Match "Platform"
```
**Output:**  

```
DocumentFormat  : JSON
DocumentType    : Automation
DocumentVersion : 7
Name            : KT-Get-Platform
Owner           : 987654123456
PlatformTypes   : {Windows, Linux}
SchemaVersion   : 0.3
Tags            : {}
TargetType      :
VersionName     :
```
+  For API details, see [ListDocuments](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: Lists all the configuration documents in your account.**  

```
Get-SSMDocumentList
```
**Output:**  

```
DocumentType    : Command
DocumentVersion : 1
Name            : AWS-ApplyPatchBaseline
Owner           : Amazon
PlatformTypes   : {Windows}
SchemaVersion   : 1.2

DocumentType    : Command
DocumentVersion : 1
Name            : AWS-ConfigureAWSPackage
Owner           : Amazon
PlatformTypes   : {Windows, Linux}
SchemaVersion   : 2.0

DocumentType    : Command
DocumentVersion : 1
Name            : AWS-ConfigureCloudWatch
Owner           : Amazon
PlatformTypes   : {Windows}
SchemaVersion   : 1.2
...
```
**Example 2: This example retrieves all automation documents with name matchingi 'Platform'**  

```
Get-SSMDocumentList -DocumentFilterList @{Key="DocumentType";Value="Automation"} | Where-Object Name -Match "Platform"
```
**Output:**  

```
DocumentFormat  : JSON
DocumentType    : Automation
DocumentVersion : 7
Name            : KT-Get-Platform
Owner           : 987654123456
PlatformTypes   : {Windows, Linux}
SchemaVersion   : 0.3
Tags            : {}
TargetType      :
VersionName     :
```
+  For API details, see [ListDocuments](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.