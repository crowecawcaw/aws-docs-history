# Use `DeleteTags` with a CLI

The following code examples show how to use `DeleteTags`.

CLI

**AWS CLI**

**Example 1: To delete a tag from a resource**

The following `delete-tags` example deletes the tag `Stack=Test` from the specified image. When you specify both a value and a key name, the tag is deleted only if the tag's value matches the specified value.

```
`aws ec2 delete-tags \
 --resources `ami-1234567890abcdef0` \
 --tags `Key=Stack,Value=Test``

```

It's optional to specify the value for a tag. The following `delete-tags` example deletes the tag with the key name `purpose` from the specified instance, regardless of the tag value for the tag.

```
`aws ec2 delete-tags \
 --resources `i-1234567890abcdef0` \
 --tags `Key=purpose``

```

If you specify the empty string as the tag value, the tag is deleted only if the tag's value is the empty string. The following `delete-tags` example specifies the empty string as the tag value for the tag to delete.

```
`aws ec2 delete-tags \
 --resources `i-1234567890abcdef0` \
 --tags `Key=Name,Value=``

```

**Example 2: To delete a tag from multiple resources**

The following `delete-tags` example deletes the tag`Purpose=Test` from both an instance and an AMI. As shown in the previous example, you can omit the tag value from the command.

```
`aws ec2 delete-tags \
 --resources `i-1234567890abcdef0` `ami-1234567890abcdef0` \
 --tags `Key=Purpose``

```

- For API details, see
  [DeleteTags](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-tags.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-tags.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the specified tag from the specified resource, regardless of the tag value. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-EC2Tag -Resource i-12345678 -Tag @{ Key="myTag" } -Force

```

**Example 2: This example deletes the specified tag from the specified resource, but only if the tag value matches. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-EC2Tag -Resource i-12345678 -Tag @{ Key="myTag";Value="myTagValue" } -Force

```

**Example 3: This example deletes the specified tag from the specified resource, regardless of the tag value.**

```
$tag = New-Object Amazon.EC2.Model.Tag
$tag.Key = "myTag"

Remove-EC2Tag -Resource i-12345678 -Tag $tag -Force

```

**Example 4: This example deletes the specified tag from the specified resource, but only if the tag value matches.**

```
$tag = New-Object Amazon.EC2.Model.Tag
$tag.Key = "myTag"
$tag.Value = "myTagValue"

Remove-EC2Tag -Resource i-12345678 -Tag $tag -Force

```

- For API details, see
  [DeleteTags](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the specified tag from the specified resource, regardless of the tag value. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-EC2Tag -Resource i-12345678 -Tag @{ Key="myTag" } -Force

```

**Example 2: This example deletes the specified tag from the specified resource, but only if the tag value matches. The syntax used by this example requires PowerShell version 3 or later.**

```
Remove-EC2Tag -Resource i-12345678 -Tag @{ Key="myTag";Value="myTagValue" } -Force

```

**Example 3: This example deletes the specified tag from the specified resource, regardless of the tag value.**

```
$tag = New-Object Amazon.EC2.Model.Tag
$tag.Key = "myTag"

Remove-EC2Tag -Resource i-12345678 -Tag $tag -Force

```

**Example 4: This example deletes the specified tag from the specified resource, but only if the tag value matches.**

```
$tag = New-Object Amazon.EC2.Model.Tag
$tag.Key = "myTag"
$tag.Value = "myTagValue"

Remove-EC2Tag -Resource i-12345678 -Tag $tag -Force

```

- For API details, see
  [DeleteTags](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
