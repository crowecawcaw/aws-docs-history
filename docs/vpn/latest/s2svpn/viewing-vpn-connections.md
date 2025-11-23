# View AWS Site-to-Site VPN connections

## View VPN connections using the console

You can view your VPN connections and their details using the AWS Management Console. This provides a visual interface to monitor connection status, tunnel health, and configuration details.

###### To view VPN connections using the console

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN Connections**.
3. Select your VPN connection to view detailed information including:
   - Connection state and status
   - Tunnel details and health status
   - Route information
   - Configuration parameters

The console displays real-time status information and allows you to monitor tunnel connectivity, view routing tables, and access configuration details for troubleshooting.

## View VPN connections using the CLI

Use the AWS CLI to query and retrieve detailed information about your VPN connections programmatically. This method enables automation, scripting, and integration with monitoring tools.

To query all VPN connections in your current AWS account and region, execute the
`describe-vpn-connections` command without parameters. However, if you
want to view the details about a particular VPN connection you'll need to know the VPN
connection Id.

To retrieve detailed information for a specific VPN connection, specify the connection
ID as a parameter. The following example shows a request to view details about a
specific VPN connection.

```
aws ec2 describe-vpn-connections --vpn-connection-ids vpn-1234567890abcdef0
```

The response includes comprehensive information about the VPN connection, including
tunnel options, routing details, and current status.

- `State` - The current state of the VPN connection
- `TunnelOptions` - Configuration and status for each tunnel
- `OutsideIpAddress` - The public IP addresses of the VPN tunnels
- `Routes` - Routing information for the connection

Example response excerpt showing key connection details:

```

{
    "VpnConnections": [
        {
            "VpnConnectionId": "vpn-1234567890abcdef0",
            "State": "available",
            "CustomerGatewayId": "cgw-1234567890abcdef0",
            "Type": "ipsec.1",
            "Options": {
                "StaticRoutesOnly": false,
                "TunnelOptions": [
                    {
                        "OutsideIpAddress": "203.0.113.12",
                        "TunnelInsideCidr": "169.254.10.0/30",
                        "PreSharedKey": "example_key_1234567890abcdef0",
                        "Phase1LifetimeSeconds": 28800,
                        "Phase2LifetimeSeconds": 3600
                    },
                    {
                        "OutsideIpAddress": "203.0.113.34",
                        "TunnelInsideCidr": "169.254.11.0/30",
                        "PreSharedKey": "example_key_0987654321fedcba0",
                        "Phase1LifetimeSeconds": 28800,
                        "Phase2LifetimeSeconds": 3600
                    }
                ]
            }
        }
    ]
}
```

## View VPN connections using the API

Make direct API calls to the Amazon EC2 service to retrieve VPN connection information. This approach provides maximum flexibility for custom applications and programmatic integrations.

The `DescribeVpnConnections` API action queries and returns detailed information about one or more VPN connections. You can apply filters by connection ID, state, or other attributes to narrow your results.

The following shows an example request to provide details about a single VPN
connection.

```

POST / HTTP/1.1
Host: ec2.us-east-1.amazonaws.com
Content-Type: application/x-www-form-urlencoded
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20230101/us-east-1/ec2/aws4_request, SignedHeaders=host;x-amz-date, Signature=example_signature

Action=DescribeVpnConnections
&VpnConnectionId.1=vpn-1234567890abcdef0
&Version=2016-11-15

```

The response returns details about that VPN connection.

```

<?xml version="1.0" encoding="UTF-8"?>
<DescribeVpnConnectionsResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>12345678-1234-1234-1234-123456789012</requestId>
    <vpnConnectionSet>
        <item>
            <vpnConnectionId>vpn-1234567890abcdef0</vpnConnectionId>
            <state>available</state>
            <customerGatewayId>cgw-1234567890abcdef0</customerGatewayId>
            <type>ipsec.1</type>
            <options>
                <staticRoutesOnly>false</staticRoutesOnly>
                <tunnelOptionSet>
                    <item>
                        <outsideIpAddress>203.0.113.12</outsideIpAddress>
                        <tunnelInsideCidr>169.254.10.0/30</tunnelInsideCidr>
                        <preSharedKey>example_key_1234567890abcdef0</preSharedKey>
                    </item>
                    <item>
                        <outsideIpAddress>203.0.113.34</outsideIpAddress>
                        <tunnelInsideCidr>169.254.11.0/30</tunnelInsideCidr>
                        <preSharedKey>example_key_0987654321fedcba0</preSharedKey>
                    </item>
                </tunnelOptionSet>
            </options>
        </item>
    </vpnConnectionSet>
</DescribeVpnConnectionsResponse>

```
