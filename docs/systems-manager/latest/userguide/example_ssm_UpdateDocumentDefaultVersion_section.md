

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `UpdateDocumentDefaultVersion` with a CLI
<a name="example_ssm_UpdateDocumentDefaultVersion_section"></a>

The following code examples show how to use `UpdateDocumentDefaultVersion`.

------
#### [ CLI ]

**AWS CLI**  
**To update the default version of a document**  
The following `update-document-default-version` example updates the default version of a Systems Manager document.  

```
aws ssm update-document-default-version \
    --name {{"Example"}} \
    --document-version {{"2"}}
```
Output:  

```
{
    "Description": {
        "Name": "Example",
        "DefaultVersion": "2"
    }
}
```
For more information, see [Writing SSM Document Content](https://docs.aws.amazon.com/systems-manager/latest/userguide/create-ssm-doc.html#writing-ssm-doc-content) in the *AWS Systems Manager User Guide*.  
+  For API details, see [UpdateDocumentDefaultVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document-default-version.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This updates the default version of a document. You can obtain the available document versions with the "Get-SSMDocumentVersionList" cmdlet.**  

```
Update-SSMDocumentDefaultVersion -Name "RunShellScript" -DocumentVersion "2"
```
**Output:**  

```
DefaultVersion Name
-------------- ----
2              RunShellScript
```
+  For API details, see [UpdateDocumentDefaultVersion](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This updates the default version of a document. You can obtain the available document versions with the "Get-SSMDocumentVersionList" cmdlet.**  

```
Update-SSMDocumentDefaultVersion -Name "RunShellScript" -DocumentVersion "2"
```
**Output:**  

```
DefaultVersion Name
-------------- ----
2              RunShellScript
```
+  For API details, see [UpdateDocumentDefaultVersion](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.