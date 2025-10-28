# Use `DetachNetworkInterface` with a CLI

The following code examples show how to use `DetachNetworkInterface`.

CLI

**AWS CLI**

**To detach a network interface from your instance**

This example detaches the specified network interface from the specified instance. If the command succeeds, no output is returned.

Command:

```
`aws ec2 detach-network-interface --attachment-id `eni-attach-66c4350a``

```

- For API details, see
  [DetachNetworkInterface](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-network-interface.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-network-interface.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example removes the specified attachment between a network interface and an instance.**

```
Dismount-EC2NetworkInterface -AttachmentId eni-attach-1a2b3c4d -Force

```

- For API details, see
  [DetachNetworkInterface](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example removes the specified attachment between a network interface and an instance.**

```
Dismount-EC2NetworkInterface -AttachmentId eni-attach-1a2b3c4d -Force

```

- For API details, see
  [DetachNetworkInterface](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
