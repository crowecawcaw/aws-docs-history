# Create an AWS Site-to-Site VPN transit gateway connection

using the CLI or API

## Create a VPN connection to Transit Gateway using the CLI

Use the [create-vpn-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection.html") command and specify the transit gateway ID for the
`--transit-gateway-id` option.

The following example demonstrates creating a VPN connection with IPv6 outer tunnel IPs and IPv6 inner tunnel IPs:

```
aws ec2 create-vpn-connection \
--type ipsec.1 \
--transit-gateway-id tgw-12312312312312312 \
--customer-gateway-id cgw-001122334455aabbc \
--options OutsideIPAddressType=Ipv6,TunnelInsideIpVersion=ipv6,TunnelOptions=[{StartupAction=start},{StartupAction=start}]
```

Example response:

```
{
    "VpnConnection": {
        "VpnConnectionId": "vpn-0abcdef1234567890",
        "State": "pending",
        "CustomerGatewayId": "cgw-001122334455aabbc",
        "Type": "ipsec.1",
        "TransitGatewayId": "tgw-12312312312312312",
        "Category": "VPN",
        "Routes": [],
        "Options": {
            "StaticRoutesOnly": false,
            "OutsideIPAddressType": "Ipv6",
            "TunnelInsideIpVersion": "ipv6"
        }
    }
}
```

## Create a VPN connection to Transit Gateway using the API

You can create a VPN connection using the Amazon EC2 API. This section provides example request and response messages for creating a transit gateway VPN connection using the API.

### Prerequisites

Before creating a VPN connection using the API, ensure you have:

- A transit gateway created and available
- A customer gateway configured with your on-premises device details

The following example shows how to create a VPN connection using the
`CreateVpnConnection` API action:

```
POST / HTTP/1.1
Host: ec2.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded

Action=CreateVpnConnection
&Type=ipsec.1
&TransitGatewayId=tgw-12345678901234567
&CustomerGatewayId=cgw-12345678901234567
&Options.StaticRoutesOnly=false
&Version=2016-11-15
```

This example creates a VPN connection with dynamic routing (BGP) between the specified transit gateway and customer gateway.

A successful API response returns the VPN connection details:

```
<?xml version="1.0" encoding="UTF-8"?>
<CreateVpnConnectionResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>7a62c49f-347e-4fc4-9331-6e8eEXAMPLE</requestId>
    <vpnConnection>
        <vpnConnectionId>vpn-1a2b3c4d5e6f78901</vpnConnectionId>
        <state>pending</state>
        <customerGatewayId>cgw-12345678901234567</customerGatewayId>
        <type>ipsec.1</type>
        <transitGatewayId>tgw-12345678901234567</transitGatewayId>
        <category>VPN</category>
        <options>
            <staticRoutesOnly>false</staticRoutesOnly>
        </options>
    </vpnConnection>
</CreateVpnConnectionResponse>
```

The response includes the VPN connection ID, current state, and configuration details. The connection will initially be in a "pending" state while AWS provisions the VPN tunnels.
