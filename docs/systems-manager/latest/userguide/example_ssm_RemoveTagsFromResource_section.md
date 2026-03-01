# Use `RemoveTagsFromResource` with a CLI

The following code examples show how to use `RemoveTagsFromResource`.

CLI

**AWS CLI**

**To remove a tag from a patch baseline**

The following `remove-tags-from-resource` example removes tags from a patch baseline.

```
`aws ssm remove-tags-from-resource \
 --resource-type `"PatchBaseline"` \
 --resource-id `"pb-0123456789abcdef0"` \
 --tag-keys `"Region"``

```

This command produces no output.

For more information, see [Tagging AWS Resources](../../../general/latest/gr/aws_tagging.md "../../../general/latest/gr/aws_tagging.md") in the _AWS General Reference_.

- For API details, see
  [RemoveTagsFromResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/remove-tags-from-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/remove-tags-from-resource.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example removes a tag from a maintenance window. There is no output if the command succeeds.**

```
Remove-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow" -TagKey "Production"

```

- For API details, see
  [RemoveTagsFromResource](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example removes a tag from a maintenance window. There is no output if the command succeeds.**

```
Remove-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow" -TagKey "Production"

```

- For API details, see
  [RemoveTagsFromResource](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
