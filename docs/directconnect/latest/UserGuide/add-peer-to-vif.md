# Add a BGP peer to an AWS Direct Connect virtual interface

Add or delete an IPv4 or IPv6 BGP peering session to your virtual
interface using either the AWS Direct Connect console or using the command line or API.

A virtual interface can support a single IPv4 BGP peering session and a single IPv6 BGP
peering session. You cannot specify your own peer IPv6 addresses for an IPv6 BGP peering
session. Amazon automatically allocates you a /125 IPv6 CIDR.

Multi-protocol BGP is not supported. IPv4 and IPv6 operate in dual-stack mode for the
virtual interface.

AWS enables MD5 by default. You cannot modify this option.

Use the following procedure to add a BGP peer.

###### To add a BGP peer

1.  Open the **AWS Direct Connect** console at [https://console.aws.amazon.com/directconnect/v2/home](https://console.aws.amazon.com/directconnect/v2/home "https://console.aws.amazon.com/directconnect/v2/home").
2.  In the navigation pane, choose **Virtual
    Interfaces**.
3.  Select the virtual interface and then choose **View
    details**.
4.  Choose **Add peering**.
5.  (Private virtual interface) To add IPv4 BGP peers, do the
    following:
    - Choose **IPv4**.
    - To specify these IP addresses yourself, for **Your router
      peer ip**, enter the destination IPv4 CIDR address to
      which Amazon should send traffic. For **Amazon router peer
      ip**, enter the IPv4 CIDR address to use to send
      traffic to AWS.

6.  (Public virtual interface) To add IPv4 BGP peers, do the following:
    - For **Your router peer ip**, enter the IPv4 CIDR
      destination address where traffic should be sent.
    - For **Amazon router peer IP**, enter the IPv4
      CIDR address to use to send traffic to AWS.

    ###### Important

    When configuring AWS Direct Connect virtual interfaces, you can specify your own IP addresses using RFC 1918, use other addressing schemes, or opt for AWS assigned IPv4 /29 CIDR addresses allocated from the RFC 3927 169.254.0.0/16 IPv4 Link-Local range for point-to-point connectivity. These point-to-point connections should be used exclusively for eBGP peering between your customer gateway router and the Direct Connect endpoint. For VPC traffic or tunnelling purposes, such as AWS Site-to-Site Private IP VPN, or Transit Gateway Connect, AWS recommends using a loopback or LAN interface on your customer gateway router as the source or destination address instead of the point-to-point connections.

        + For more information about RFC 1918, see
         [Address Allocation for Private
         Internets](https://datatracker.ietf.org/doc/html/rfc1918 "https://datatracker.ietf.org/doc/html/rfc1918").
        + For more information about RFC 3927, see
         [Dynamic Configuration of IPv4 Link-Local
         Addresses](https://datatracker.ietf.org/doc/html/rfc3927 "https://datatracker.ietf.org/doc/html/rfc3927").

7.  (Private or public virtual interface) To add IPv6 BGP peers, choose
    **IPv6**. The peer IPv6 addresses are automatically
    assigned from Amazon's pool of IPv6 addresses; you cannot specify custom
    IPv6 addresses.
8.  For **BGP ASN**, enter the Border Gateway Protocol Autonomous System
    Number of your on-premises peer router for the new virtual interface.

For a public virtual interface, the ASN must be private or already on the allow list for the
virtual interface.

The valid values are 1 to 4294967294. This includes support for both ASNs (1-2147483646) and long ASNs (1-4294967294). For more information about ASNs and long ASNs see [Long ASN support in AWS Direct Connect](long-asn-support.md "long-asn-support.md").

Note that if you do not enter a value, we automatically assign
one. 9. To provide your own BGP key, for **BGP Authentication
Key**, enter your BGP MD5 key. 10. Choose **Add peering**.

###### To create a BGP peer using the command line or API

- [create-bgp-peer](../../../cli/latest/reference/directconnect/create-bgp-peer.md "../../../cli/latest/reference/directconnect/create-bgp-peer.md") (AWS CLI)
- [CreateBGPPeer](../APIReference/API_CreateBGPPeer.md "../APIReference/API_CreateBGPPeer.md")
  (AWS Direct Connect API)
