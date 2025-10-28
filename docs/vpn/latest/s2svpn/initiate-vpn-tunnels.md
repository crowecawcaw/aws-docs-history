# AWS Site-to-Site VPN tunnel initiation options

By default, your customer gateway device must bring up the tunnels for your Site-to-Site VPN connection
by generating traffic and initiating the Internet Key Exchange (IKE) negotiation process.
You can configure your VPN tunnels to specify that AWS must initiate or restart the IKE
negotiation process instead.

## VPN tunnel IKE initiation options

The following IKE initiation options are available. You can implement either or both
options, for one or both of the tunnels in your Site-to-Site VPN connection. See [VPN tunnel options](VPNTunnels.md "VPNTunnels.md") for more details on these
and other tunnel option settings.

- **Startup action**: The action to take when
  establishing the VPN tunnel for a new or modified VPN connection. By default,
  your customer gateway device initiates the IKE negotiation process to bring the
  tunnel up. You can specify that AWS must initiate the IKE negotiation process
  instead.
- **DPD timeout action**: The action to take after
  dead peer detection (DPD) timeout occurs. By default, the IKE session is
  stopped, the tunnel goes down, and the routes are removed. You can specify that
  AWS must restart the IKE session when DPD timeout occurs, or you can specify
  that AWS must take no action when DPD timeout occurs.

## Rules and limitations

The following rules and limitations apply:

- To initiate IKE negotiation, AWS requires the public IP address of your customer
  gateway device. If you configured certificate-based authentication for your VPN
  connection and you did not specify an IP address when you created the customer
  gateway resource in AWS, you must create a new customer gateway and specify the
  IP address. Then, modify the VPN connection and specify the new customer
  gateway. For more information, see [Change the customer gateway for an AWS Site-to-Site VPN connection](change-vpn-cgw.md "change-vpn-cgw.md").
- IKE initiation (startup action) from the AWS side of the VPN connection is
  supported for IKEv2 only.
- If using IKE initiation from the AWS side of the VPN connection, it does not include a timeout setting. It will continuously try to establish a connection until one is made. Additionally, the AWS side of VPN connection will re-initiate IKE negotiation when it receives a delete SA message from your customer gateway.
- If your customer gateway device is behind a firewall or other device using
  Network Address Translation (NAT), it must have an identity (IDr) configured.
  For more information about IDr, see [RFC 7296](https://datatracker.ietf.org/doc/html/rfc7296 "https://datatracker.ietf.org/doc/html/rfc7296").

If you do not configure IKE initiation from the AWS side for your VPN tunnel and the
VPN connection experiences a period of idle time (usually 10 seconds, depending on your
configuration), the tunnel might go down. To prevent this, you can use a network
monitoring tool to generate keepalive pings.

## Working with VPN tunnel initiation

options

For more information about working with VPN tunnel initiation options, see the following
topics:

- To create a new VPN connection and specify the VPN tunnel initiation options:
  [Step 5: Create a VPN connection](SetUpVPNConnections.md#vpn-create-vpn-connection "SetUpVPNConnections.md#vpn-create-vpn-connection")
- To modify the VPN tunnel initiation options for an existing VPN connection: [Modify AWS Site-to-Site VPN tunnel options](modify-vpn-tunnel-options.md "modify-vpn-tunnel-options.md")
