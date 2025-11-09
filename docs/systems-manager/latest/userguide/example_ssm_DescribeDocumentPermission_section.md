AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Use `DescribeDocumentPermission` with a CLI

The following code examples show how to use `DescribeDocumentPermission`.

CLI

**AWS CLI**

**To describe document permissions**

The following `describe-document-permission` example displays permission details about a Systems Manager document that is shared publicly.

```
`aws ssm describe-document-permission \
 --name `"Example"` \
 --permission-type `"Share"``

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

For more information, see [Share a Systems Manager Document](ssm-how-to-share.md "ssm-how-to-share.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribeDocumentPermission](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document-permission.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-document-permission.html")
  in _AWS CLI Command Reference_.

PowerShell

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

- For API details, see
  [DescribeDocumentPermission](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

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

- For API details, see
  [DescribeDocumentPermission](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
