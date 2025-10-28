# Use `DescribeVpnConnections` with a CLI

The following code examples show how to use `DescribeVpnConnections`.

CLI

**AWS CLI**

**Example 1: To describe your VPN connections**

The following `describe-vpn-connections` example describes all of your Site-to-Site VPN connections.

```
`aws ec2 describe-vpn-connections`

```

Output:

```
{
    "VpnConnections": [
        {
            "CustomerGatewayConfiguration": "...configuration information...",
            "CustomerGatewayId": "cgw-01234567abcde1234",
            "Category": "VPN",
            "State": "available",
            "Type": "ipsec.1",
            "VpnConnectionId": "vpn-1122334455aabbccd",
            "TransitGatewayId": "tgw-00112233445566aab",
            "Options": {
                "EnableAcceleration": false,
                "StaticRoutesOnly": true,
                "LocalIpv4NetworkCidr": "0.0.0.0/0",
                "RemoteIpv4NetworkCidr": "0.0.0.0/0",
                "TunnelInsideIpVersion": "ipv4"
            },
            "Routes": [],
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "CanadaVPN"
                }
            ],
            "VgwTelemetry": [
                {
                    "AcceptedRouteCount": 0,
                    "LastStatusChange": "2020-07-29T10:35:11.000Z",
                    "OutsideIpAddress": "203.0.113.3",
                    "Status": "DOWN",
                    "StatusMessage": ""
                },
                {
                    "AcceptedRouteCount": 0,
                    "LastStatusChange": "2020-09-02T09:09:33.000Z",
                    "OutsideIpAddress": "203.0.113.5",
                    "Status": "UP",
                    "StatusMessage": ""
                }
            ]
        }
    ]
}
```

For more information, see [How AWS Site-to-Site VPN works](../../../vpn/latest/s2svpn/how_it_works.md "../../../vpn/latest/s2svpn/how_it_works.md") in the _AWS Site-to-Site VPN User Guide_.

**Example 2: To describe your available VPN connections**

The following `describe-vpn-connections` example describes your Site-to-Site VPN connections with a state of `available`.

```
`aws ec2 describe-vpn-connections \
 --filters `"Name=state,Values=available"``

```

For more information, see [How AWS Site-to-Site VPN works](../../../vpn/latest/s2svpn/how_it_works.md "../../../vpn/latest/s2svpn/how_it_works.md") in the _AWS Site-to-Site VPN User Guide_.

- For API details, see
  [DescribeVpnConnections](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpn-connections.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpn-connections.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example describes the specified VPN connection.**

```
Get-EC2VpnConnection -VpnConnectionId vpn-12345678

```

**Output:**

```
CustomerGatewayConfiguration : [XML document]
CustomerGatewayId            : cgw-1a2b3c4d
Options                      : Amazon.EC2.Model.VpnConnectionOptions
Routes                       : {Amazon.EC2.Model.VpnStaticRoute}
State                        : available
Tags                         : {}
Type                         : ipsec.1
VgwTelemetry                 : {Amazon.EC2.Model.VgwTelemetry, Amazon.EC2.Model.VgwTelemetry}
VpnConnectionId              : vpn-12345678
VpnGatewayId                 : vgw-1a2b3c4d
```

**Example 2: This example describes any VPN connection whose state is either pending or available.**

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "pending", "available" )

Get-EC2VpnConnection -Filter $filter

```

**Example 3: This example describes all your VPN connections.**

```
Get-EC2VpnConnection

```

- For API details, see
  [DescribeVpnConnections](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example describes the specified VPN connection.**

```
Get-EC2VpnConnection -VpnConnectionId vpn-12345678

```

**Output:**

```
CustomerGatewayConfiguration : [XML document]
CustomerGatewayId            : cgw-1a2b3c4d
Options                      : Amazon.EC2.Model.VpnConnectionOptions
Routes                       : {Amazon.EC2.Model.VpnStaticRoute}
State                        : available
Tags                         : {}
Type                         : ipsec.1
VgwTelemetry                 : {Amazon.EC2.Model.VgwTelemetry, Amazon.EC2.Model.VgwTelemetry}
VpnConnectionId              : vpn-12345678
VpnGatewayId                 : vgw-1a2b3c4d
```

**Example 2: This example describes any VPN connection whose state is either pending or available.**

```
$filter = New-Object Amazon.EC2.Model.Filter
$filter.Name = "state"
$filter.Values = @( "pending", "available" )

Get-EC2VpnConnection -Filter $filter

```

**Example 3: This example describes all your VPN connections.**

```
Get-EC2VpnConnection

```

- For API details, see
  [DescribeVpnConnections](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Create Amazon EC2 resources using an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
