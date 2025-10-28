# Use `DisableVpcClassicLinkDnsSupport` with a CLI

The following code examples show how to use `DisableVpcClassicLinkDnsSupport`.

CLI

**AWS CLI**

**To disable ClassicLink DNS support for a VPC**

This example disables ClassicLink DNS support for `vpc-88888888`.

Command:

```
`aws ec2 disable-vpc-classic-link-dns-support --vpc-id `vpc-88888888``

```

Output:

```
{
  "Return": true
}
```

- For API details, see
  [DisableVpcClassicLinkDnsSupport](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-vpc-classic-link-dns-support.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-vpc-classic-link-dns-support.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example disables ClassicLink DNS support for the vpc-0b12d3456a7e8910d**

```
Disable-EC2VpcClassicLinkDnsSupport -VpcId vpc-0b12d3456a7e8910d

```

- For API details, see
  [DisableVpcClassicLinkDnsSupport](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example disables ClassicLink DNS support for the vpc-0b12d3456a7e8910d**

```
Disable-EC2VpcClassicLinkDnsSupport -VpcId vpc-0b12d3456a7e8910d

```

- For API details, see
  [DisableVpcClassicLinkDnsSupport](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
