# Use `DescribeVpcClassicLink` with a CLI

The following code examples show how to use `DescribeVpcClassicLink`.

CLI

**AWS CLI**

**To describe the ClassicLink status of your VPCs**

This example lists the ClassicLink status of vpc-88888888.

Command:

```
`aws ec2 describe-vpc-classic-link --vpc-id `vpc-88888888``

```

Output:

```
{
  "Vpcs": [
    {
      "ClassicLinkEnabled": true,
      "VpcId": "vpc-88888888",
      "Tags": [
        {
          "Value": "classiclinkvpc",
          "Key": "Name"
        }
      ]
    }
  ]
}
```

This example lists only VPCs that are enabled for Classiclink (the filter value of `is-classic-link-enabled` is set to `true`).

Command:

```
`aws ec2 describe-vpc-classic-link --filter `"Name=is-classic-link-enabled,Values=true"``

```

- For API details, see
  [DescribeVpcClassicLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-classic-link.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-classic-link.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: Above example returns all the VPCs with their ClassicLinkEnabled state for the region**

```
Get-EC2VpcClassicLink -Region eu-west-1

```

**Output:**

```
ClassicLinkEnabled Tags   VpcId
------------------ ----   -----
False              {Name} vpc-0fc1ff23f45b678eb
False              {}     vpc-01e23c4a5d6db78e9
False              {Name} vpc-0123456b078b9d01f
False              {}     vpc-12cf3b4f
False              {Name} vpc-0b12d3456a7e8901d
```

- For API details, see
  [DescribeVpcClassicLink](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: Above example returns all the VPCs with their ClassicLinkEnabled state for the region**

```
Get-EC2VpcClassicLink -Region eu-west-1

```

**Output:**

```
ClassicLinkEnabled Tags   VpcId
------------------ ----   -----
False              {Name} vpc-0fc1ff23f45b678eb
False              {}     vpc-01e23c4a5d6db78e9
False              {Name} vpc-0123456b078b9d01f
False              {}     vpc-12cf3b4f
False              {Name} vpc-0b12d3456a7e8901d
```

- For API details, see
  [DescribeVpcClassicLink](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
