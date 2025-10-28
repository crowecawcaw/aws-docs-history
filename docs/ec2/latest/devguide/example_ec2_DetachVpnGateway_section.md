# Use `DetachVpnGateway` with a CLI

The following code examples show how to use `DetachVpnGateway`.

CLI

**AWS CLI**

**To detach a virtual private gateway from your VPC**

This example detaches the specified virtual private gateway from the specified VPC. If the command succeeds, no output is returned.

Command:

```
`aws ec2 detach-vpn-gateway --vpn-gateway-id `vgw-9a4cacf3` --vpc-id `vpc-a01106c2``

```

- For API details, see
  [DetachVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-vpn-gateway.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/detach-vpn-gateway.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example detaches the specified virtual private gateway from the specified VPC.**

```
Dismount-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678

```

- For API details, see
  [DetachVpnGateway](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example detaches the specified virtual private gateway from the specified VPC.**

```
Dismount-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678

```

- For API details, see
  [DetachVpnGateway](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
