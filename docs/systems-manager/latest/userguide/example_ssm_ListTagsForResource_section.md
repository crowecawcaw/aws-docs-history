# Use `ListTagsForResource` with a CLI

The following code examples show how to use `ListTagsForResource`.

CLI

**AWS CLI**

**To list the tags applied to a patch baseline**

The following `list-tags-for-resource` example lists the tags for a patch baseline.

```
`aws ssm list-tags-for-resource \
 --resource-type `"PatchBaseline"` \
 --resource-id `"pb-0123456789abcdef0"``

```

Output:

```
{
    "TagList": [
        {
            "Key": "Environment",
            "Value": "Production"
        },
        {
            "Key": "Region",
            "Value": "EMEA"
        }
    ]
}
```

For more information, see [Tagging AWS Resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General Reference_.

- For API details, see
  [ListTagsForResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-tags-for-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-tags-for-resource.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example lists the tags for a maintenance window.**

```
Get-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow"

```

**Output:**

```
Key   Value
---   -----
Stack Production
```

- For API details, see
  [ListTagsForResource](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example lists the tags for a maintenance window.**

```
Get-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow"

```

**Output:**

```
Key   Value
---   -----
Stack Production
```

- For API details, see
  [ListTagsForResource](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
