# HNREL04-BP03 Use dynamic routing for automatic failover

Implement dynamically routing for dedicated connections and IPSec
VPN connections using BGP to enable automatic load balancing and
failover across redundant links.

**Desired outcome:** Ensure seamless
failover and traffic distribution across all available network
paths, minimizing downtime and manual intervention.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enables automatic failover in the event of a connection failure
- Balances network traffic for optimal performance
- Reduces manual intervention and operational overhead
- Increases resilience of hybrid connectivity

## Implementation guidance

- Use BGP for dynamic routing between on-premises and cloud
  networks.
- Regularly validate routing and failover with controlled tests.

## Resources

- [BGP
  Negotiation over AWS Site-to-Site VPN and Direct Connect:
  Troubleshooting Strategies for Efficient Networking](https://repost.aws/articles/ARIKYhXEYyQQqtO2ulKERrbw/bgp-negotiation-over-aws-site-to-site-vpn-and-direct-connect-troubleshooting-strategies-for-efficient-networking "https://repost.aws/articles/ARIKYhXEYyQQqtO2ulKERrbw/bgp-negotiation-over-aws-site-to-site-vpn-and-direct-connect-troubleshooting-strategies-for-efficient-networking")
