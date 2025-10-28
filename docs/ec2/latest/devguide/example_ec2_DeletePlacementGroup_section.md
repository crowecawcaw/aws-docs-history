# Use `DeletePlacementGroup` with a CLI

The following code examples show how to use `DeletePlacementGroup`.

CLI

**AWS CLI**

**To delete a placement group**

This example command deletes the specified placement group.

Command:

```
`aws ec2 delete-placement-group --group-name `my-cluster``

```

- For API details, see
  [DeletePlacementGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-placement-group.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-placement-group.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the specified placement group. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2PlacementGroup -GroupName my-placement-group

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2PlacementGroup (DeletePlacementGroup)" on Target "my-placement-group".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

- For API details, see
  [DeletePlacementGroup](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the specified placement group. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2PlacementGroup -GroupName my-placement-group

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2PlacementGroup (DeletePlacementGroup)" on Target "my-placement-group".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

- For API details, see
  [DeletePlacementGroup](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
