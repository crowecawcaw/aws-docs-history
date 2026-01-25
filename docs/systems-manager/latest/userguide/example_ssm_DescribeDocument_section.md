AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `DescribeDocument` with an AWS SDK or CLI

The following code examples show how to use `DescribeDocument`.

CLI

**AWS CLI**

**To display details of a document**

The following `describe-document` example displays details about a Systems Manager document in your AWS account.

```
`aws ssm describe-document \
 --name `"Example"``

```

Output:

```
{
    "Document": {
        "Hash": "fc2410281f40779e694a8b95975d0f9f316da8a153daa94e3d9921102EXAMPLE",
        "HashType": "Sha256",
        "Name": "Example",
        "Owner": "29884EXAMPLE",
        "CreatedDate": 1583257938.266,
        "Status": "Active",
        "DocumentVersion": "1",
        "Description": "Document Example",
        "Parameters": [
            {
                "Name": "AutomationAssumeRole",
                "Type": "String",
                "Description": "(Required) The ARN of the role that allows Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses your IAM permissions to execute this document.",
                "DefaultValue": ""
            },
            {
                "Name": "InstanceId",
                "Type": "String",
                "Description": "(Required) The ID of the Amazon EC2 instance.",
                "DefaultValue": ""
            }
        ],
        "PlatformTypes": [
            "Windows",
            "Linux"
        ],
        "DocumentType": "Automation",
        "SchemaVersion": "0.3",
        "LatestVersion": "1",
        "DefaultVersion": "1",
        "DocumentFormat": "YAML",
        "Tags": []
    }
}
```

For more information, see [Creating Systems Manager Documents](create-ssm-doc.md "create-ssm-doc.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribeDocument](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns information about a document.**

```
Get-SSMDocumentDescription -Name "RunShellScript"

```

**Output:**

```
CreatedDate     : 2/24/2017 5:25:13 AM
DefaultVersion  : 1
Description     : Run an updated script
DocumentType    : Command
DocumentVersion : 1
Hash            : f775e5df4904c6fa46686c4722fae9de1950dace25cd9608ff8d622046b68d9b
HashType        : Sha256
LatestVersion   : 1
Name            : RunShellScript
Owner           : 123456789012
Parameters      : {commands}
PlatformTypes   : {Linux}
SchemaVersion   : 2.0
Sha1            :
Status          : Active
```

- For API details, see
  [DescribeDocument](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns information about a document.**

```
Get-SSMDocumentDescription -Name "RunShellScript"

```

**Output:**

```
CreatedDate     : 2/24/2017 5:25:13 AM
DefaultVersion  : 1
Description     : Run an updated script
DocumentType    : Command
DocumentVersion : 1
Hash            : f775e5df4904c6fa46686c4722fae9de1950dace25cd9608ff8d622046b68d9b
HashType        : Sha256
LatestVersion   : 1
Name            : RunShellScript
Owner           : 123456789012
Parameters      : {commands}
PlatformTypes   : {Linux}
SchemaVersion   : 2.0
Sha1            :
Status          : Active
```

- For API details, see
  [DescribeDocument](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

SAP ABAP

**SDK for SAP ABAP**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ssm#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ssm#code-examples").

```
    TRY.
        DATA(lo_result) = lo_ssm->describedocument( iv_name = iv_name ).
        DATA(lo_document) = lo_result->get_document( ).
        IF lo_document IS BOUND.
          rv_status = lo_document->get_status( ).
          MESSAGE |Document status: { rv_status }| TYPE 'I'.
        ENDIF.
      CATCH /aws1/cx_ssminvaliddocument.
        MESSAGE 'Invalid document.' TYPE 'I'.
    ENDTRY.


```

- For API details, see
  [DescribeDocument](../../../sdk-for-sap-abap/v1/api/latest/index.md "../../../sdk-for-sap-abap/v1/api/latest/index.md")
  in _AWS SDK for SAP ABAP API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
