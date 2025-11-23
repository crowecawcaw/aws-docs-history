# Create an AWS Site-to-Site VPN Concentrator

connection using the CLI or API

## Create a Site-to-Site VPN Concentrator

connection using the CLI

After creating a Site-to-Site VPN Concentrator, you need to establish individual VPN
connections from your remote sites to the Site-to-Site VPN Concentrator. Each remote site requires
its own VPN connection that references the Site-to-Site VPN Concentrator ID. This allows multiple
remote sites to share the same Site-to-Site VPN Concentrator infrastructure while maintaining
separate, secure tunnels for each site.

To establish a VPN connection using a Site-to-Site VPN Concentrator, specify the Site-to-Site VPN
Concentrator instead of the transit gateway when creating the VPN connection. The
following example creates a VPN connection using a Site-to-Site VPN Concentrator:

```
aws ec2 create-vpn-connection \
--type ipsec.1 \
--customer-gateway-id cgw-123456789 \
--vpn-concentrator-id vcn-0123456789abcdef0
```

A successful response returns the following:

```
{
    "VpnConnection": {
        "VpnConnectionId": "vpn-0abcdef1234567890",
        "State": "pending",
        "CustomerGatewayId": "cgw-123456789",
        "Type": "ipsec.1",
        "VpnConcentratorId": "vcn-0123456789abcdef0",
        "Category": "VPN",
        "Routes": [],
        "Options": {
            "StaticRoutesOnly": false
        }
    }
}
```

## Create a Site-to-Site VPN Concentrator connection

using the API

You can create a VPN connection that uses a Site-to-Site VPN Concentrator using the
Amazon EC2 API. This section provides example request and response messages for creating
a VPN connection with a Site-to-Site VPN Concentrator.

Before creating a VPN connection with a Site-to-Site VPN Concentrator using the API, ensure
you have:

- A Site-to-Site VPN Concentrator created and available
- A customer gateway configured for your remote site
- Network configuration allowing IPsec traffic between your site and AWS

The following example shows how to create a VPN connection using a Site-to-Site VPN
Concentrator with the `CreateVpnConnection` API action:

```
POST / HTTP/1.1
Host: ec2.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded

Action=CreateVpnConnection
&Type=ipsec.1
&VpnConcentratorId=vcn-0123456789abcdef0
&CustomerGatewayId=cgw-12345678901234567
&Options.StaticRoutesOnly=false
&Version=2016-11-15
```

This example creates a VPN connection between the specified Site-to-Site VPN
Concentrator and customer gateway. The Site-to-Site VPN Concentrator acts as the AWS side
endpoint, allowing multiple remote sites to connect through a centralized
hub.

A successful API response returns the VPN connection details with Site-to-Site VPN
Concentrator information:

```
<?xml version="1.0" encoding="UTF-8"?>
<CreateVpnConnectionResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>8b73d60f-458f-5gc5-a442-7f9fEXAMPLE</requestId>
    <vpnConnection>
        <vpnConnectionId>vpn-9z8y7x6w5v4u32109</vpnConnectionId>
        <state>pending</state>
        <customerGatewayId>cgw-12345678901234567</customerGatewayId>
        <type>ipsec.1</type>
        <vpnConcentratorId>vcn-0123456789abcdef0</vpnConcentratorId>
        <category>VPN</category>
        <options>
            <staticRoutesOnly>false</staticRoutesOnly>
        </options>
    </vpnConnection>
</CreateVpnConnectionResponse>
```

The response includes the VPN connection ID and references the Site-to-Site VPN
Concentrator ID instead of a transit gateway ID. This connection allows your remote
site to communicate with other sites connected to the same Site-to-Site VPN Concentrator,
enabling hub-and-spoke network topologies.
