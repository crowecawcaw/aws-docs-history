# Create an AWS Site-to-Site VPN Cloud WAN connection using

the CLI or API

You can create an Site-to-Site VPN connections between your on-premises and AWS Cloud WAN following the
procedure below. For more information, see
[Site-to-site VPN attachments in AWS Cloud WAN](../../../network-manager/latest/cloudwan/cloudwan-s2s-vpn-attachment.md "../../../network-manager/latest/cloudwan/cloudwan-s2s-vpn-attachment.md") in the _AWS Cloud WAN User Guide_.

## Create a VPN connection to Cloud WAN using the

CLI

Use the [create-vpn-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpn-connection.html") command to create a VPN connection that will later be attached to a Cloud WAN global network. This creates an unattached VPN connection that can subsequently be associated with Cloud WAN through the Network Manager console or API.

**Prerequisites**

Before creating a Cloud WAN VPN connection, ensure you have the following:

- `customer-gateway-id` - An existing customer gateway
  resource (`cgw-xxxxxxxxx`) that represents your on-premises VPN
  device.
- **Cloud WAN Global Network** - A Cloud WAN global
  network must be created and configured with appropriate network segments.
- **BGP Configuration** - Cloud WAN VPN connections
  require BGP routing; static routing is not supported. You must set `StaticRoutesOnly=false` in the options parameter

This command creates a VPN connection without specifying a target gateway. The connection will be in an unattached state and can later be associated with your Cloud WAN global network through the Network Manager console or API. The `StaticRoutesOnly=false` option enables BGP routing, which is mandatory for Cloud WAN VPN attachments as static routing is not supported.

The following example creates an unattached VPN connection for Cloud WAN:

```
aws ec2 create-vpn-connection \
            --type ipsec.1 \
            --customer-gateway-id cgw-0123456789abcdef0 \
            --options StaticRoutesOnly=false
```

The response returns the following:

```
{
            "VpnConnection": {
            "VpnConnectionId": "vpn-0abcdef1234567890",
            "State": "pending",
            "CustomerGatewayId": "cgw-0123456789abcdef0",
            "Type": "ipsec.1",
            "Category": "VPN",
            "Routes": [],
            "Options": {
            "StaticRoutesOnly": false
            }
            }
            }
```

After creating the VPN connection, you can attach it to your Cloud WAN global network using the Network Manager console or the `create-site-to-site-vpn-attachment` API call.

## Create a VPN Cloud WAN connection using the

API

You can use the EC2 API to create a VPN connection for Cloud WAN integration. This involves making a `CreateVpnConnection` API call that creates an unattached VPN connection, which can then be associated with your Cloud WAN global network.

The API request creates a VPN connection without specifying a target gateway, leaving it in an unattached state that's ready for Cloud WAN integration. The connection uses BGP routing, which is required for Cloud WAN VPN attachments.

The following example shows the HTTP request to create a Cloud WAN VPN connection:

```
POST / HTTP/1.1
            Host: ec2.us-east-1.amazonaws.com
            Content-Type: application/x-www-form-urlencoded
            Authorization: AWS4-HMAC-SHA256 Credential=...

            Action=CreateVpnConnection
            &Type=ipsec.1
            &CustomerGatewayId=cgw-0123456789abcdef0
            &Options.StaticRoutesOnly=false
            &Version=2016-11-15
```

The API returns a successful response containing the VPN connection details. The
connection will be in a `pending` state initially while AWS provisions the
VPN tunnels, at which time the status changes to `available`.

```
<?xml version="1.0" encoding="UTF-8"?>
            <CreateVpnConnectionResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
            <requestId>12345678-1234-1234-1234-123456789012</requestId>
            <vpnConnection>
            <vpnConnectionId>vpn-0abcdef1234567890</vpnConnectionId>
            <state>pending</state>
            <customerGatewayId>cgw-0123456789abcdef0</customerGatewayId>
            <type>ipsec.1</type>
            <category>VPN</category>
            <options>
            <staticRoutesOnly>false</staticRoutesOnly>
            </options>
            <vgwTelemetry/>
            <routes/>
            </vpnConnection>
            </CreateVpnConnectionResponse>
```

**Response Details**

The API response provides the following key information:

- **vpnConnectionId** - The unique identifier for your VPN connection (e.g., `vpn-0abcdef1234567890`) that you'll use to attach it to Cloud WAN
- **state** - Initially "pending" while AWS provisions the VPN tunnels, then transitions to "available" when ready for attachment
- **category** - Shows "VPN" indicating this is an unattached VPN connection suitable for Cloud WAN integration
- **staticRoutesOnly** - Set to "false" to enable BGP routing, which is required for Cloud WAN VPN attachments

Once the VPN connection reaches the "available" state, you can attach it to your Cloud WAN global network using the Network Manager `CreateSiteToSiteVpnAttachment` API or through the AWS console.
