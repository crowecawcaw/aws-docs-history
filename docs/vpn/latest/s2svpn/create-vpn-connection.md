# Create an AWS Site-to-Site VPN connection

You can create Site-to-Site VPN connections that attach to transit gateways or Cloud WAN global networks. Both attachment types support IPv4 and IPv6 protocols and can optionally use Site-to-Site VPN Concentrators for connecting multiple remote sites cost-effectively.

## Create a VPN connection using the console

###### To create a VPN connection using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Site-to-Site VPN connections**.
3. Choose **Create VPN connection**.
4. (Optional) For **Name tag**, enter a name for the
   connection. Doing so creates a tag with a key of `Name` and the value
   that you specify.
5. For **Target gateway type**, choose one of the following:
   - **Virtual private gateway** - Create a new virtual
     private gateway VPN connection by choosing an existing **Virtual
     private gateway**.
   - **Transit gateway** - Create a new transit gateway
     VPN connection by choosing an existing **Transit
     gateway**. For more information about creating a transit
     gateway, see [Transit
     gateways](../../../vpc/latest/tgw/tgw-transit-gateways.md "../../../vpc/latest/tgw/tgw-transit-gateways.md") in _Amazon VPC Transit Gateways_.
   - **Site-to-Site VPN Concentrator** - Create a new Site-to-Site VPN
     Concentrator connection by using an existing Site-to-Site VPN Concentrator or
     creating a new one. Choose one of the following:
     - **Existing** - Create a new Site-to-Site VPN Concentrator
       VPN connection using an existing Concentrator.
     - **New** - Enter an optional name for the
       Site-to-Site VPN Concentrator and then choose the transit gateway to
       associate with it.

   - **Not associated** - Create an unattached VPN connection that can later be associated with Cloud WAN through the Network Manager console or API. For more information about VPN attachments and Cloud WAN, see [Site-to-site VPN attachments in AWS Cloud WAN](../../../network-manager/latest/cloudwan/cloudwan-s2s-vpn-attachment.md "../../../network-manager/latest/cloudwan/cloudwan-s2s-vpn-attachment.md") in the _AWS Cloud WAN User Guide_.

6. For **Customer gateway**, do one of the following:
   - To use an existing customer gateway, choose
     **Existing**, and then choose the
     **Customer gateway ID**.
   - To create a new customer gateway, choose **New**,
     and then do the following:
     - For the **IP address** , enter a static
       **IPv4** or **IPv6**
       address.
     - (Optional) For **Certificate ARN**, choose
       the ARN of your private certificate (if using certificate-based
       authentication).
     - For **BGP ASN**, enter the Border Gateway
       Protocol (BGP) Autonomous System Number (ASN) of your customer
       gateway. For more information, see [Customer gateway options](cgw-options.md "cgw-options.md").

7. For **Routing options**, choose **Dynamic (requires
   BGP)** or **Static**.

###### Note

Cloud WAN VPN connections and VPN connections using Concentrators only support BGP routing. Static routing is not supported for these connection types. 8. For **Pre-shared key storage** choose either
**Standard** or **Secrets Manager**. The
default selection is **Standard**. For more information about using
AWS Secrets Manager, see [Security](security.md "security.md"). 9. For **Tunnel inside IP version**, choose
**IPv4** or **IPv6**. 10. (Optional) For **Enable acceleration**, choose the check box to
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
