# Use `DisableVpcClassicLink` with a CLI

The following code examples show how to use `DisableVpcClassicLink`.

CLI

**AWS CLI**

**To disable ClassicLink for a VPC**

This example disables ClassicLink for vpc-8888888.

Command:

```
`aws ec2 disable-vpc-classic-link --vpc-id `vpc-88888888``

```

Output:

```
{
  "Return": true
}
```

- For API details, see
  [DisableVpcClassicLink](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-vpc-classic-link.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/disable-vpc-classic-link.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example disables EC2VpcClassicLink for the vpc-01e23c4a5d6db78e9. It returns either True or False**

```
Disable-EC2VpcClassicLink -VpcId vpc-01e23c4a5d6db78e9

```

- For API details, see
  [DisableVpcClassicLink](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example disables EC2VpcClassicLink for the vpc-01e23c4a5d6db78e9. It returns either True or False**

```
Disable-EC2VpcClassicLink -VpcId vpc-01e23c4a5d6db78e9

```

- For API details, see
  [DisableVpcClassicLink](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
