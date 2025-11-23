# AWS Site-to-Site VPN Concentrators

AWS Site-to-Site VPN Concentrator is a new feature that simplifies multi-site connectivity for
distributed enterprises. VPN Concentrator is suitable for customers who need to connect 25+
remote sites to AWS, with each site needing low bandwidth (under 100 Mbps).

## Supported gateway services and

features

VPN Concentrators are only supported with Transit Gateway. This feature is not supported
with Cloud WAN or Virtual Private Gateway.

The following table describes Site-to-Site VPN Concentrator supported features:

| Feature                                              | Supported?                                                                                     |
| ---------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| IPv6                                                 | Yes                                                                                            |
| Private Direct Connect VPN connections               | No                                                                                             |
| Accelerated VPN                                      | Yes                                                                                            |
| Multiple customer gateway devices from the same site | Yes. However, each customer gateway device must have a unique IP address.                      |
| Geographical restrictions                            | No. You can attach a site located in any region to a Concentrator in<br>any AWS Region.        |
| Site-to-Site VPN logs                                | Yes. You can generate VPN logs for all sites connected to the<br>Concentrator or individually. |
| Transit Gateway Encryption Support                   | No                                                                                             |

## Bandwidth

Currently, Site-to-Site VPN Concentrators support 5 Gbps aggregate bandwidth. Each site can support
a maximum of 100 Mbps bandwidth. However, if you need higher bandwidth, reach out to
AWS Support.

## Routing

Site-to-Site VPN Concentrators support BGP (Border Gateway Protocol) routing only. Static routing is not supported.

All customer gateways connected to the Site-to-Site VPNConcentrator use the same Site-to-Site VPN
Concentrator attachment to the transit gateway for routing. Each site connecting to the Site-to-Site VPN
Concentrator can send a maximum of 5,000 routes from the transit gateway to a customer gateway and 1,000
routes from the customer gateway to the transit gateway.

## IP address allocation

Each VPN connection through the Site-to-Site VPN Concentrator will still have a unique AWS IP address (one
per tunnel).

## Monitoring

VPN connections via Site-to-Site VPN Concentrators support the same metrics as regular VPN connections.

When you enable Transit gateway flow logs on the VPN Concentrator attachment, you will see flow logs for
all the traffic coming in and going out of all the remote sites connected to the concentrator.

## Tunnel maintenance

The tunnel maintenance works the same way as existing standard Site-to-Site VPN
tunnels for both endpoints when using a Site-to-Site VPN Concentrator. See [Endpoint replacements](endpoint-replacements.md "endpoint-replacements.md") for
more information.

## Pricing

Information about pricing for Site-to-Site VPN Concentrator can be found on the [AWS VPN pricing](http://aws.amazon.com/vpn/pricing/ "http://aws.amazon.com/vpn/pricing/") page.
