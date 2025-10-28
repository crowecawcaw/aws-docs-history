# Use `ConfirmProductInstance` with a CLI

The following code examples show how to use `ConfirmProductInstance`.

CLI

**AWS CLI**

**To confirm the product instance**

This example determines whether the specified product code is associated with the specified instance.

Command:

```
`aws ec2 confirm-product-instance --product-code `774F4FF8` --instance-id `i-1234567890abcdef0``

```

Output:

```
{
  "OwnerId": "123456789012"
}
```

- For API details, see
  [ConfirmProductInstance](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/confirm-product-instance.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/confirm-product-instance.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example determines whether the specified product code is associated with the specified instance.**

```
Confirm-EC2ProductInstance -ProductCode 774F4FF8 -InstanceId i-12345678

```

- For API details, see
  [ConfirmProductInstance](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example determines whether the specified product code is associated with the specified instance.**

```
Confirm-EC2ProductInstance -ProductCode 774F4FF8 -InstanceId i-12345678

```

- For API details, see
  [ConfirmProductInstance](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
