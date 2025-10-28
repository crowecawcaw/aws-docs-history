# Use `AddTagsToResource` with a CLI

The following code examples show how to use `AddTagsToResource`.

CLI

**AWS CLI**

**Example 1: To add tags to a maintenance window**

The following `add-tags-to-resource` example adds a tag to the specified maintenance window.

```
`aws ssm add-tags-to-resource \
 --resource-type `"MaintenanceWindow"` \
 --resource-id `"mw-03eb9db428EXAMPLE"` \
 --tags `"Key=Stack,Value=Production"``

```

This command produces no output.

**Example 2: To add tags to a parameter**

The following `add-tags-to-resource` example adds two tags to to the specified parameter.

```
`aws ssm add-tags-to-resource \
 --resource-type `"Parameter"` \
 --resource-id `"My-Parameter"` \
 --tags '`[{"Key":"Region","Value":"East"},{"Key":"Environment", "Value":"Production"}]`'`

```

This command produces no output.

**Example 3: To add tags to an SSM document**

The following `add-tags-to-resource` example adds a tag to to the specified document.

```
`aws ssm add-tags-to-resource \
 --resource-type `"Document"` \
 --resource-id `"My-Document"` \
 --tags `"Key=Quarter,Value=Q322"``

```

This command produces no output.

For more information, see [Tagging Systems Manager resources](tagging-resources.md "tagging-resources.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [AddTagsToResource](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/add-tags-to-resource.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/add-tags-to-resource.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example updates a maintenance window with new tags. There is no output if the command succeeds. The syntax used by this example requires PowerShell version 3 or later.**

```
$option1 = @{Key="Stack";Value=@("Production")}
Add-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow" -Tag $option1

```

**Example 2: With PowerShell version 2, you must use New-Object to create each tag. There is no output if the command succeeds.**

```
$tag1 = New-Object Amazon.SimpleSystemsManagement.Model.Tag
$tag1.Key = "Stack"
$tag1.Value = "Production"

Add-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow" -Tag $tag1

```

- For API details, see
  [AddTagsToResource](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example updates a maintenance window with new tags. There is no output if the command succeeds. The syntax used by this example requires PowerShell version 3 or later.**

```
$option1 = @{Key="Stack";Value=@("Production")}
Add-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow" -Tag $option1

```

**Example 2: With PowerShell version 2, you must use New-Object to create each tag. There is no output if the command succeeds.**

```
$tag1 = New-Object Amazon.SimpleSystemsManagement.Model.Tag
$tag1.Key = "Stack"
$tag1.Value = "Production"

Add-SSMResourceTag -ResourceId "mw-03eb9db42890fb82d" -ResourceType "MaintenanceWindow" -Tag $tag1

```

- For API details, see
  [AddTagsToResource](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
