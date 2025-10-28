# Use `DeleteNetworkInterface` with a CLI

The following code examples show how to use `DeleteNetworkInterface`.

CLI

**AWS CLI**

**To delete a network interface**

This example deletes the specified network interface. If the command succeeds, no output is returned.

Command:

```
`aws ec2 delete-network-interface --network-interface-id `eni-e5aa89a3``

```

- For API details, see
  [DeleteNetworkInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-interface.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-network-interface.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example deletes the specified network interface. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2NetworkInterface -NetworkInterfaceId eni-12345678

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2NetworkInterface (DeleteNetworkInterface)" on Target "eni-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

- For API details, see
  [DeleteNetworkInterface](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example deletes the specified network interface. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2NetworkInterface -NetworkInterfaceId eni-12345678

```

**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2NetworkInterface (DeleteNetworkInterface)" on Target "eni-12345678".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```

- For API details, see
  [DeleteNetworkInterface](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
