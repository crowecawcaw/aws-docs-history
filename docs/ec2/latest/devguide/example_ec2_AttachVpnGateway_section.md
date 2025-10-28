# Use `AttachVpnGateway` with a CLI

The following code examples show how to use `AttachVpnGateway`.

CLI

**AWS CLI**

**To attach a virtual private gateway to your VPC**

The following `attach-vpn-gateway` example attaches the specified virtual private gateway to the specified VPC.

```
`aws ec2 attach-vpn-gateway \
 --vpn-gateway-id `vgw-9a4cacf3` \
 --vpc-id `vpc-a01106c2``

```

Output:

```
{
    "VpcAttachment": {
        "State": "attaching",
        "VpcId": "vpc-a01106c2"
    }
}
```

- For API details, see
  [AttachVpnGateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-vpn-gateway.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/attach-vpn-gateway.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example attaches the specified virtual private gateway to the specified VPC.**

```
Add-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678

```

**Output:**

```
State        VpcId
-----        -----
attaching    vpc-12345678
```

- For API details, see
  [AttachVpnGateway](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example attaches the specified virtual private gateway to the specified VPC.**

```
Add-EC2VpnGateway -VpnGatewayId vgw-1a2b3c4d -VpcId vpc-12345678

```

**Output:**

```
State        VpcId
-----        -----
attaching    vpc-12345678
```

- For API details, see
  [AttachVpnGateway](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
