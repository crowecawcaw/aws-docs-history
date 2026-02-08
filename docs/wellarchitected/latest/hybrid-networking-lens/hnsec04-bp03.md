# HNSEC04-BP03 Implement network traffic security

inspection

Network traffic security inspection provides a layered security
approach to ensure traffic between your cloud and on-premises
resources is properly monitored and protected against threats.

**Desired outcome:** Deploy
inspection and security enforcement on ingress and egress network
paths as needed.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enables deep packet inspection
- Provides scalable firewall for hybrid network traffic
- Enables advanced rule sets for protocol, domain, and threat
  filtering
- Simplifies compliance with perimeter defense requirements

## Implementation guidance

- Route traffic through the firewall appliances
- Define and maintain firewall rule groups for hybrid traffic.
- Monitor firewall activity and adapt rules as threats evolve.

## Resources

- [Gateway
  Load Balancer](../../../elasticloadbalancing/latest/gateway/introduction.md "../../../elasticloadbalancing/latest/gateway/introduction.md")
- [Centralized Traffic Inspection with Gateway Load Balancer on AWS](https://aws.amazon.com/blogs/apn/centralized-traffic-inspection-with-gateway-load-balancer-on-aws/ "https://aws.amazon.com/blogs/apn/centralized-traffic-inspection-with-gateway-load-balancer-on-aws/")
- [AWS Network Firewall Documentation](../../../network-firewall/latest/developerguide.md "../../../network-firewall/latest/developerguide.md")
