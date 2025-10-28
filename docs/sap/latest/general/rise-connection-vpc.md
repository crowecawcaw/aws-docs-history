# Connecting to RISE using AWS VPN

Enable access to your remote network from RISE with SAP VPC using [AWS Site-to-Site VPN](../../../vpn/latest/s2svpn/VPC_VPN.md "../../../vpn/latest/s2svpn/VPC_VPN.md"). Traffic between AWS cloud and your on-premises location is encrypted via Internet Protocol security (IPsec) and transferred through a secure tunnel on internet. This option is efficient, and faster to implement when compared to AWS Direct Connect. For more information, see [Connect your VPC to remote networks using AWS Virtual Private Network](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md").

You can get a maximum bandwidth of up to 1.25 Gbps per VPN tunnel. For more information, see [Site-to-Site VPN quotas](../../../vpn/latest/s2svpn/vpn-limits.md "../../../vpn/latest/s2svpn/vpn-limits.md").

To scale beyond the default maximum limit of 1.25 Gbps throughput of a single VPN tunnel, see [How can I achieve ECMP routing with multiple Site-to-Site VPN tunnels that are associated with a transit gateway?](https://repost.aws/knowledge-center/transit-gateway-ecmp-multiple-tunnels "https://repost.aws/knowledge-center/transit-gateway-ecmp-multiple-tunnels")

When using this option, SAP requires the following details:

- BGP ASN
- IP address of your device
  You can obtain these details from your AWS VPN device on-premises.

When connecting your remote network directly to RISE using AWS Site-to-Site AWS VPN, the cost for the AWS VPN Connection and the cost for data transfer out are included in the RISE subscription.

For more information see: [AWS Site-to-Site AWS VPN Pricing](https://aws.amazon.com/vpn/pricing/ "https://aws.amazon.com/vpn/pricing/").

Note: Because the cost associated with the lifecycle and operation of a "Customer gateway device" (a physical device or software application on your side of the Site-to-Site AWS VPN connection) varies, this is not taken into consideration in this document.
