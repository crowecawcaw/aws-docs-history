# Use `DescribeVolumeAttribute` with a CLI

The following code examples show how to use `DescribeVolumeAttribute`.

CLI

**AWS CLI**

**To describe a volume attribute**

This example command describes the `autoEnableIo` attribute of the volume with the ID `vol-049df61146c4d7901`.

Command:

```
`aws ec2 describe-volume-attribute --volume-id `vol-049df61146c4d7901` --attribute `autoEnableIO``

```

Output:

```
{
    "AutoEnableIO": {
        "Value": false
    },
    "VolumeId": "vol-049df61146c4d7901"
}
```

- For API details, see
  [DescribeVolumeAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volume-attribute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volume-attribute.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the specified attribute of the specified volume.**

```
Get-EC2VolumeAttribute -VolumeId vol-12345678 -Attribute AutoEnableIO

```

**Output:**

```
AutoEnableIO    ProductCodes    VolumeId
------------    ------------    --------
False           {}              vol-12345678
```

- For API details, see
  [DescribeVolumeAttribute](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the specified attribute of the specified volume.**

```
Get-EC2VolumeAttribute -VolumeId vol-12345678 -Attribute AutoEnableIO

```

**Output:**

```
AutoEnableIO    ProductCodes    VolumeId
------------    ------------    --------
False           {}              vol-12345678
```

- For API details, see
  [DescribeVolumeAttribute](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
