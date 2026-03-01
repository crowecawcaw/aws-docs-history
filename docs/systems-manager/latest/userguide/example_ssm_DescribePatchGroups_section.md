# Use `DescribePatchGroups` with a CLI

The following code examples show how to use `DescribePatchGroups`.

CLI

**AWS CLI**

**To display patch group registrations**

The following `describe-patch-groups` example lists the patch group registrations.

```
`aws ssm describe-patch-groups`

```

Output:

```
{
    "Mappings": [
        {
            "PatchGroup": "Production",
            "BaselineIdentity": {
                "BaselineId": "pb-0123456789abcdef0",
                "BaselineName": "ProdPatching",
                "OperatingSystem": "WINDOWS",
                "BaselineDescription": "Patches for Production",
                "DefaultBaseline": false
            }
        },
        {
            "PatchGroup": "Development",
            "BaselineIdentity": {
                "BaselineId": "pb-0713accee01234567",
                "BaselineName": "DevPatching",
                "OperatingSystem": "WINDOWS",
                "BaselineDescription": "Patches for Development",
                "DefaultBaseline": true
            }
        },
        ...
    ]
}
```

For more information, see Create a Patch Group <https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-patch-group-tagging.html>\_\_ and [Add a Patch Group to a Patch Baseline](sysman-patch-group-patchbaseline.md "sysman-patch-group-patchbaseline.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [DescribePatchGroups](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-groups.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-patch-groups.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists the patch group registrations.**

```
Get-SSMPatchGroup

```

**Output:**

```
BaselineIdentity                                           PatchGroup
----------------                                           ----------
Amazon.SimpleSystemsManagement.Model.PatchBaselineIdentity Production
```

- For API details, see
  [DescribePatchGroups](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists the patch group registrations.**

```
Get-SSMPatchGroup

```

**Output:**

```
BaselineIdentity                                           PatchGroup
----------------                                           ----------
Amazon.SimpleSystemsManagement.Model.PatchBaselineIdentity Production
```

- For API details, see
  [DescribePatchGroups](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
