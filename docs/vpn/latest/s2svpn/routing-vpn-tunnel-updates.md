# Routing during VPN tunnel endpoint

updates

A Site-to-Site VPN connection consists of two VPN tunnels between a customer gateway device
and a virtual private gateway or a transit gateway. We recommend that you configure both
tunnels for redundancy. From time to time, AWS also performs routine maintenance on
your VPN connection, which might briefly disable one of the two tunnels of your VPN
connection. For more information, see [Tunnel endpoint replacement notifications](monitoring-vpn-health-events.md#tunnel-replacement-notifications "monitoring-vpn-health-events.md#tunnel-replacement-notifications").

When we perform updates on one VPN tunnel, we set a lower outbound multi-exit
discriminator (MED) value on the other tunnel. If you have configured your customer
gateway device to use both tunnels, your VPN connection uses the other (up) tunnel
during the tunnel endpoint update process.

###### Note

- To ensure that the up tunnel with the lower MED is preferred, ensure that
  your customer gateway device uses the same Weight and Local Preference
  values for both tunnels (Weight and Local Preference have higher priority
  than MED).
