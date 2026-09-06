

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Use `DescribeDocumentPermission` with a CLI
<a name="example_ssm_DescribeDocumentPermission_section"></a>

The following code examples show how to use `DescribeDocumentPermission`.

------
#### [ CLI ]

**AWS CLI**  
**To describe document permissions**  
The following `describe-document-permission` example displays permission details about a Systems Manager document that is shared publicly.  

```
aws ssm describe-document-permission \
    --name {{"Example"}} \
    --permission-type {{"Share"}}
```
Output:  

```
{
    "AccountIds": [
        "all"
    ],
    "AccountSharingInfoList": [
        {
            "AccountId": "all",
            "SharedDocumentVersion": "$DEFAULT"
        }
    ]
}
```
For more information, see [Share a Systems Manager Document](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-how-to-share.html) in the *AWS Systems Manager User Guide*.  
+  For API details, see [DescribeDocumentPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document-permission.html) in *AWS CLI Command Reference*. 

------
#### [ PowerShell ]

**Tools for PowerShell V4**  
**Example 1: This example lists all the versions for a document.**  

```
Get-SSMDocumentVersionList -Name "RunShellScript"
```
**Output:**  

```
CreatedDate          DocumentVersion IsDefaultVersion Name
-----------          --------------- ---------------- ----
2/24/2017 5:25:13 AM 1               True             RunShellScript
```
+  For API details, see [DescribeDocumentPermission](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*. 

**Tools for PowerShell V5**  
**Example 1: This example lists all the versions for a document.**  

```
Get-SSMDocumentVersionList -Name "RunShellScript"
```
**Output:**  

```
CreatedDate          DocumentVersion IsDefaultVersion Name
-----------          --------------- ---------------- ----
2/24/2017 5:25:13 AM 1               True             RunShellScript
```
+  For API details, see [DescribeDocumentPermission](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.