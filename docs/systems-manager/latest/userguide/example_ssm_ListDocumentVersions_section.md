

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `ListDocumentVersions` with a CLI
<a name="example_ssm_ListDocumentVersions_section"></a>

The following code examples show how to use `ListDocumentVersions`.

------
#### [ CLI ]

**AWS CLI**  
**To list document versions**  
The following `list-document-versions` example lists all versions for a Systems Manager document.  

```
aws ssm list-document-versions \
    --name {{"Example"}}
```
Output:  

```
{
    "DocumentVersions": [
        {
            "Name": "Example",
            "DocumentVersion": "1",
            "CreatedDate": 1583257938.266,
            "IsDefaultVersion": true,
            "DocumentFormat": "YAML",
            "Status": "Active"
        }
    ]
}
```
For more information, see [Sending Commands that Use the Document Version Parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/run-command-version.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [ListDocumentVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-document-versions.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example lists all the versions for a document.**  

```
Get-SSMDocumentVersionList -Name "AWS-UpdateSSMAgent"
```
**Output:**  

```
CreatedDate       : 6/1/2021 5:19:10 PM
DocumentFormat    : JSON
DocumentVersion   : 1
IsDefaultVersion  : True
Name              : AWS-UpdateSSMAgent
Status            : Active
```
+  For API details, see [ListDocumentVersions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example lists all the versions for a document.**  

```
Get-SSMDocumentVersionList -Name "AWS-UpdateSSMAgent"
```
**Output:**  

```
CreatedDate       : 6/1/2021 5:19:10 PM
DocumentFormat    : JSON
DocumentVersion   : 1
IsDefaultVersion  : True
Name              : AWS-UpdateSSMAgent
Status            : Active
```
+  For API details, see [ListDocumentVersions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.