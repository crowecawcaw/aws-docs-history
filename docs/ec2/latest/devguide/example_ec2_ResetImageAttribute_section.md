# Use `ResetImageAttribute` with a CLI

The following code examples show how to use `ResetImageAttribute`.

CLI

**AWS CLI**

**To reset the launchPermission attribute**

This example resets the `launchPermission` attribute for the specified AMI to its default value. By default, AMIs are private. If the command succeeds, no output is returned.

Command:

```
`aws ec2 reset-image-attribute --image-id `ami-5731123e` --attribute `launchPermission``

```

- For API details, see
  [ResetImageAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-image-attribute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/reset-image-attribute.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example resets the 'launchPermission' attribute to its default value. By default, AMIs are private.**

```
Reset-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission

```

- For API details, see
  [ResetImageAttribute](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example resets the 'launchPermission' attribute to its default value. By default, AMIs are private.**

```
Reset-EC2ImageAttribute -ImageId ami-12345678 -Attribute launchPermission

```

- For API details, see
  [ResetImageAttribute](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
