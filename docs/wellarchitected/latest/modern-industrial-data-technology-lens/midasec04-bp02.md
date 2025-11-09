# MIDASEC04-BP02 Use firewalls, perimeter networks, and dedicated network zones

Implement perimeter defenses such as firewalls, perimeter networks and dedicated network
zones to manage and secure traffic flows between cloud, IT, and OT systems.

**Desired outcome:** Traffic is filtered and restricted at each
trust boundary to enforce zero trust and layered defense.

**Benefits of establishing this best practice:** Helps improve
network security posture, prevent direct exposure of OT systems, and support layered
defense-in-depth architecture.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Deploy AWS Network Firewall, private subnets, and multi-tier perimeter network
architectures to filter and control inbound and outbound traffic.

### Implementation steps

- Deploy AWS Network Firewall or third-party appliances in VPCs.
- Create perimeter networks between public internet and sensitive workloads using
  public and private subnet models.
- Enforce rule groups that restrict IPs, ports, and protocols.
- Continuously monitor and update firewall rules and network configurations.

## Resources

- [What is AWS Network Firewall?](../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md "../../../network-firewall/latest/developerguide/what-is-aws-network-firewall.md")
- [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://aws.amazon.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure/ "https://aws.amazon.com/whitepapers/building-a-scalable-and-secure-multi-vpc-aws-network-infrastructure/")
