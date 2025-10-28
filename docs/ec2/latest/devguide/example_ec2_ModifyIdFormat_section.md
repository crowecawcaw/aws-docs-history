# Use `ModifyIdFormat` with a CLI

The following code examples show how to use `ModifyIdFormat`.

CLI

**AWS CLI**

**To enable the longer ID format for a resource**

The following `modify-id-format` example enables the longer ID format for the `instance` resource type.

```
`aws ec2 modify-id-format \
 --resource `instance` \
 --use-long-ids`

```

**To disable the longer ID format for a resource**

The following `modify-id-format` example disables the longer ID format for the `instance` resource type.

```
`aws ec2 modify-id-format \
 --resource `instance` \
 --no-use-long-ids`

```

The following `modify-id-format` example enables the longer ID format for all supported resource types that are within their opt-in period.

```
`aws ec2 modify-id-format \
 --resource `all-current` \
 --use-long-ids`

```

- For API details, see
  [ModifyIdFormat](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-id-format.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-id-format.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example enables the longer ID format for the specified resource type.**

```
Edit-EC2IdFormat -Resource instance -UseLongId $true

```

**Example 2: This example disables the longer ID format for the specified resource type.**

```
Edit-EC2IdFormat -Resource instance -UseLongId $false

```

- For API details, see
  [ModifyIdFormat](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example enables the longer ID format for the specified resource type.**

```
Edit-EC2IdFormat -Resource instance -UseLongId $true

```

**Example 2: This example disables the longer ID format for the specified resource type.**

```
Edit-EC2IdFormat -Resource instance -UseLongId $false

```

- For API details, see
  [ModifyIdFormat](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
