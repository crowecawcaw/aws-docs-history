# Create a transit gateway AWS Site-to-Site VPN attachment

To create a VPN attachment on a transit gateway, you must specify the transit gateway and the customer
gateway. The transit gateway will need to be created before following this procedure. For more
information about creating a transit gateway, see [Transit gateways](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md") in _Amazon VPC Transit Gateways_.

Transit gateway VPN attachments support both IPv4 or IPv6. For more information on using either of these protocols for a transit gateway VPN attachment, see [IPv4 and IPv6 traffic in AWS Site-to-Site VPN](ipv4-ipv6.md "ipv4-ipv6.md").

###### To create a VPN attachment on a transit gateway using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN connections**.
3. Choose **Create VPN connection**.
4. (Optional) For **Name tag**, enter a name for the
   connection. Doing so creates a tag with a key of `Name` and the value
   that you specify.
5. For **Target gateway type**, choose **Transit
   gateway**, and then choose the transit gateway.
6. For **Customer gateway**, do one of the following:
   - To use an existing customer gateway, choose **Existing**,
     and then choose the **Customer gateway ID**.
   - To create a new customer gateway, choose **New**.
     1. For the **IP address** , enter a static
        **IPv4** or **IPv6**
        address.
     2. (Optional) For **Certificate ARN**, choose the
        ARN of your private certificate (if using certificate-based
        authentication).
     3. For **BGP ASN**, enter the Border Gateway
        Protocol (BGP) Autonomous System Number (ASN) of your customer
        gateway. For more information, see [Customer gateway options](cgw-options.md "cgw-options.md").

7. For **Routing options**, choose **Dynamic (requires
   BGP)** or **Static**.
8. For **Pre-shared key storage** choose either
   **Standard** or **Secrets Manager**. The
   default selection is **Standard**. For more information about using
   AWS Secrets Manager, see [Security](security.md "security.md").
9. For **Tunnel inside IP version**, choose
   **IPv4** or **IPv6**.
10. (Optional) For **Enable acceleration**, choose the check box to
    enable acceleration. For more information, see [Accelerated VPN connections](accelerated-vpn.md "accelerated-vpn.md").

If you enable acceleration, we create two accelerators that are used by your VPN
connection. Additional charges apply. 11. (Optional) Depending on which tunnel inside IP version you've chosen, do one of
the following:

    * IPv4 — For **Local IPv4 network CIDR**, specify the IPv4
     CIDR range on the customer gateway (on-premises) side that is allowed to
     communicate over the VPN tunnels. For **Remote IPv4 network
     CIDR**, choose the CIDR range on the AWS side that is allowed
     to communicate over VPN tunnels. The default value for both fields is
     `0.0.0.0/0`.
    * IPv6 — For **Local IPv6 network CIDR**, specify the IPv6
     CIDR range on the customer gateway (on-premises) side that is allowed to
     communicate over the VPN tunnels. For **Remote IPv6 network
     CIDR**, choose the CIDR range on the AWS side that is allowed
     to communicate over VPN tunnels. The default value for both fields is
     `::/0`

12. For **Outside IP address type**, choose one of the following
    options:
    - **Public IPv4** - (Default) Use IPv4 addresses for the
      outer tunnel IPs.
    - **Private IPv4** - Use a private IPv4 address for use
      within private networks.
    - **IPv6** - Use IPv6 addresses for the outer tunnel IPs.
      This option requires that your customer gateway device supports IPv6
      addressing.

###### Note

If you select **IPv6** for the outside IP address type, you
must create a customer gateway with an IPv6 address 13. (Optional) For **Tunnel 1 options**, you can specify the
following information for each tunnel:

    * A size /30 IPv4 CIDR block from the `169.254.0.0/16` range for
     the inside tunnel IPv4 addresses.
    * If you specified **IPv6** for **Tunnel inside IP
     version**, a /126 IPv6 CIDR block from the
     `fd00::/8` range for the inside tunnel IPv6 addresses.
    * The IKE pre-shared key (PSK). The following versions are supported: IKEv1
     or IKEv2.
    * To edit the advanced options for your tunnel, choose **Edit tunnel
     options**. For more information, see [VPN tunnel options](VPNTunnels.md "VPNTunnels.md").
    * (Optional) Choose **Enable** for the **Tunnel
     activity log** to capture log messages for IPsec activity and
     DPD protocol messages.
    * (Optional) Choose **Turn on** for **Tunnel
     endpoint lifecycle** to control the schedule for endpoint
     replacements. For more information about tunnel endpoint lifecycle, see
     [Tunnel endpoint lifecycle](tunnel-endpoint-lifecycle.md "tunnel-endpoint-lifecycle.md").

14. (Optional) Choose **Tunnel 2 options** and follow the previous
    steps to set up a second tunnel.
15. Choose **Create VPN connection**.

## Creating a VPN attachment using the CLI

Use the [create-vpn-connection](../../../cli/latest/reference/ec2/create-vpn-connection.md "../../../cli/latest/reference/ec2/create-vpn-connection.md") command and specify the transit gateway ID for the
`--transit-gateway-id` option.

Example for creating a VPN connection with IPv6 outer tunnel IPs and IPv6 inner tunnel IPs:

```
aws ec2 create-vpn-connection --type ipsec.1 --transit-gateway-id tgw-12312312312312312 --customer-gateway-id cgw-001122334455aabbc --options OutsideIPAddressType=Ipv6,TunnelInsideIpVersion=ipv6,TunnelOptions=[{StartupAction=start},{StartupAction=start}]
```

Example for creating a VPN connection with IPv6 outer tunnel IPs and IPv4 inner tunnel IPs:

```
aws ec2 create-vpn-connection --type ipsec.1 --transit-gateway-id tgw-12312312312312312 --customer-gateway-id cgw-001122334455aabbc --options OutsideIPAddressType=Ipv6,TunnelInsideIpVersion=ipv4,TunnelOptions=[{StartupAction=start},{StartupAction=start}]
```

## Viewing IPv6 addresses for your VPN connection

After creating a VPN connection with IPv6 outer tunnel IPs, you can view the assigned IPv6 addresses using the `describe-vpn-connections` CLI command:

```
aws ec2 describe-vpn-connections --vpn-connection-ids vpn-12345678901234567
```

In the response, look for the `OutsideIpAddress` field in the
`TunnelOptions` section. For IPv6 VPN connections, this field will
contain the IPv6 addresses assigned to the AWS side of the VPN tunnels.

Example response excerpt:

```

"Options": {
    "OutsideIPAddressType": "Ipv6",
    "TunnelInsideIpVersion": "ipv6",
    "TunnelOptions": [
        {
            "OutsideIpAddress": "2600:1f14:2dcf:d556:c3db:e57f:2414:2d9a",
            "TunnelInsideCidr": "2001:db8:1001:b110::/64",
            ...
        },
        {
            "OutsideIpAddress": "2600:1f14:2dcf:d57d:6318:60af:37c5:7ce1",
            "TunnelInsideCidr": "2001:db8:1001:b111::/64",
            ...
        }
    ]
}

```
