AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `ListDocumentVersions` with a CLI

The following code examples show how to use `ListDocumentVersions`.

CLI

**AWS CLI**

**To list document versions**

The following `list-document-versions` example lists all versions for a Systems Manager document.

```
`aws ssm list-document-versions \
 --name `"Example"``

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

For more information, see [Sending Commands that Use the Document Version Parameter](run-command-version.md "run-command-version.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [ListDocumentVersions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-document-versions.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-document-versions.html")
  in _AWS CLI Command Reference_.

PowerShell

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

- For API details, see
  [ListDocumentVersions](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

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

- For API details, see
  [ListDocumentVersions](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
