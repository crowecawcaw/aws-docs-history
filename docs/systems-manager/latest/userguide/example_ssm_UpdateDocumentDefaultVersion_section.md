# Use `UpdateDocumentDefaultVersion` with a CLI

The following code examples show how to use `UpdateDocumentDefaultVersion`.

CLI

**AWS CLI**

**To update the default version of a document**

The following `update-document-default-version` example updates the default version of a Systems Manager document.

```
`aws ssm update-document-default-version \
 --name `"Example"` \
 --document-version `"2"``

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

For more information, see [Writing SSM Document Content](create-ssm-doc.md#writing-ssm-doc-content "create-ssm-doc.md#writing-ssm-doc-content") in the _AWS Systems Manager User Guide_.

- For API details, see
  [UpdateDocumentDefaultVersion](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document-default-version.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document-default-version.html")
  in _AWS CLI Command Reference_.

PowerShell

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

- For API details, see
  [UpdateDocumentDefaultVersion](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

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

- For API details, see
  [UpdateDocumentDefaultVersion](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
