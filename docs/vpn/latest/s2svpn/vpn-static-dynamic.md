# Static and dynamic routing in AWS Site-to-Site VPN

The type of routing that you select can depend on the make and model of your customer
gateway device. If your customer gateway device supports Border Gateway Protocol (BGP),
specify dynamic routing when you configure your Site-to-Site VPN connection. If your customer
gateway device does not support BGP, specify static routing.

If you use a device that supports BGP advertising, you don't specify static routes to
the Site-to-Site VPN connection because the device uses BGP to advertise its routes to the virtual
private gateway. If you use a device that doesn't support BGP advertising, you must
select static routing and enter the routes (IP prefixes) for your network that should be
communicated to the virtual private gateway.

We recommend that you use BGP-capable devices, when available, because the BGP
protocol offers robust liveness detection checks that can assist failover to the
second VPN tunnel if the first tunnel goes down. Devices that don't support BGP
may also perform health checks to assist failover to the second tunnel when
needed.

You must configure your customer gateway device to route traffic from your on-premises
network to the Site-to-Site VPN connection. The configuration depends on the make and model of your
device. For more information, see [AWS Site-to-Site VPN customer gateway devices](your-cgw.md "your-cgw.md").
