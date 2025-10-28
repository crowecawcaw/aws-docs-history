# Use `DescribeVpcAttribute` with a CLI

The following code examples show how to use `DescribeVpcAttribute`.

CLI

**AWS CLI**

**To describe the enableDnsSupport attribute**

This example describes the `enableDnsSupport` attribute. This attribute indicates whether DNS resolution is enabled for the VPC. If this attribute is `true`, the Amazon DNS server resolves DNS hostnames for your instances to their corresponding IP addresses; otherwise, it does not.

Command:

```
`aws ec2 describe-vpc-attribute --vpc-id `vpc-a01106c2` --attribute `enableDnsSupport``

```

Output:

```
{
    "VpcId": "vpc-a01106c2",
    "EnableDnsSupport": {
        "Value": true
    }
}
```

**To describe the enableDnsHostnames attribute**

This example describes the `enableDnsHostnames` attribute. This attribute indicates whether the instances launched in the VPC get DNS hostnames. If this attribute is `true`, instances in the VPC get DNS hostnames; otherwise, they do not.

Command:

```
`aws ec2 describe-vpc-attribute --vpc-id `vpc-a01106c2` --attribute `enableDnsHostnames``

```

Output:

```
{
    "VpcId": "vpc-a01106c2",
    "EnableDnsHostnames": {
        "Value": true
    }
}
```

- For API details, see
  [DescribeVpcAttribute](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-attribute.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-attribute.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the 'enableDnsSupport' attribute.**

```
Get-EC2VpcAttribute -VpcId vpc-12345678 -Attribute enableDnsSupport

```

**Output:**

```
EnableDnsSupport
----------------
True
```

**Example 2: This example describes the 'enableDnsHostnames' attribute.**

```
Get-EC2VpcAttribute -VpcId vpc-12345678 -Attribute enableDnsHostnames

```

**Output:**

```
EnableDnsHostnames
------------------
True
```

- For API details, see
  [DescribeVpcAttribute](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the 'enableDnsSupport' attribute.**

```
Get-EC2VpcAttribute -VpcId vpc-12345678 -Attribute enableDnsSupport

```

**Output:**

```
EnableDnsSupport
----------------
True
```

**Example 2: This example describes the 'enableDnsHostnames' attribute.**

```
Get-EC2VpcAttribute -VpcId vpc-12345678 -Attribute enableDnsHostnames

```

**Output:**

```
EnableDnsHostnames
------------------
True
```

- For API details, see
  [DescribeVpcAttribute](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
