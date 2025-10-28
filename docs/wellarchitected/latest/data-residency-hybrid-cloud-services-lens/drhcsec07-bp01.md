# DRHCSEC07-BP01 Implement network traffic inspection-based protection

Set up traffic inspection points between your network layers to
make sure data in transit matches the expected categories and
patterns. Analyze traffic flows, metadata, and patterns to help
identify, detect, and respond to events more effectively. Traffic
Inspection can be implemented using EC2 instances, including those
running on Outposts or Local Zones.

**Desired outcome:** Traffic that
traverses between your network layers is inspected and authorized.
Allow and deny decisions are based on explicit rules, threat
intelligence, and deviations from baseline behaviors. Protections
become stricter as traffic moves closer to sensitive
data**.**

**Common anti-patterns**

- Relying solely on rules based on ports and protocols.

**Benefits of establishing this best
practice:** Inspection systems help you author
intelligent rules, such as allowing or denying traffic only when
certain conditions within the traffic data are met.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

- Be aware that while Local Zones and Outposts support VPC
  security groups and network ACLs (NACLs), these Edge
  services do not support AWS WAF, AWS Network Firewall, and
  the Advanced level of AWS Shield. Local Zones support the
  standard level of AWS Shield, while Outposts does not.
- Implement network inspection through
  [hybrid
  inspection architectures with AWS Local Zones](https://aws.amazon.com/blogs/networking-and-content-delivery/hybrid-inspection-architectures-with-aws-local-zone/ "https://aws.amazon.com/blogs/networking-and-content-delivery/hybrid-inspection-architectures-with-aws-local-zone/") or
  by [implementing
  network traffic inspection on AWS Outposts rack](https://aws.amazon.com/blogs/compute/implementing-network-traffic-inspection-on-aws-outposts-rack/ "https://aws.amazon.com/blogs/compute/implementing-network-traffic-inspection-on-aws-outposts-rack/").
- AWS WAF support can be implemented using
  [F5
  on Outposts for AWS WAF and security inspection](https://community.f5.com/kb/technicalarticles/living-on-the-aws-edge---big-ip-on-aws-outposts/313673 "https://community.f5.com/kb/technicalarticles/living-on-the-aws-edge---big-ip-on-aws-outposts/313673").

## Resources

**Related best practices:**

- [SEC05-BP03
  Implement inspection-based protection](../security-pillar/sec_network_protection_inspection.md "../security-pillar/sec_network_protection_inspection.md")

**Related documentation:**

- [Hybrid
  inspection architectures with AWS Local Zones](https://aws.amazon.com/blogs/networking-and-content-delivery/hybrid-inspection-architectures-with-aws-local-zone/ "https://aws.amazon.com/blogs/networking-and-content-delivery/hybrid-inspection-architectures-with-aws-local-zone/")
- [Implementing
  network traffic inspection on AWS Outposts rack](https://aws.amazon.com/blogs/compute/implementing-network-traffic-inspection-on-aws-outposts-rack/ "https://aws.amazon.com/blogs/compute/implementing-network-traffic-inspection-on-aws-outposts-rack/")
