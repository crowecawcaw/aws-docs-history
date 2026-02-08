# HNPERF02-BP05 Plan for bandwidth scaling

High-speed dedicated connections can offer bandwidth up to hundreds
of gigabits per second. LAG enables bundling multiple physical
connections to increase total available bandwidth. Additionally,
implementing load balancing across multiple connections using ECMP
routing provides enhanced bandwidth scaling and improved
reliability. For virtual private network implementations, similar
scaling can be achieved by establishing multiple VPN connections and
utilizing ECMP to distribute traffic effectively across these paths.
Understanding these scaling options and their appropriate use cases
is crucial for designing network architectures that can grow with
business demands while maintaining performance and reliability.

**Desired outcome:**

- Achieve optimal network performance and capacity that meets
  growing business demands.
- Scalable network infrastructure capable of increasing traffic
  volumes

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Enables strategic bandwidth scaling decisions based on actual
  business needs while optimizing costs.
- Provides flexibility to adjust network capacity through various
  technical approaches as requirements evolve.
- Load balancing across multiple connections using BGP ECMP,
  ensuring optimal traffic distribution.

## Implementation guidance

- Assess current and projected bandwidth requirements,
  considering both peak usage patterns and growth trajectories.
- Evaluate infrastructure limitations and compatibility at both
  connection endpoints, including port speeds, hardware
  capabilities, and routing protocol support.
- Design for operational efficiency with centralized management,
  monitoring, and clear maintenance procedures.
- Consider cost implications and geographical requirements when
  choosing between scaling approaches, such as dedicated
  connections vs IPSec VPNs.

## Resources

- [AWS Direct Connect link aggregation groups (LAGs)](../../../directconnect/latest/UserGuide/lags.md "../../../directconnect/latest/UserGuide/lags.md")
- [AWS Direct Connect routing policies and BGP communities](../../../directconnect/latest/UserGuide/routing-and-bgp.md "../../../directconnect/latest/UserGuide/routing-and-bgp.md")
- [Active/Active
  and Active/Passive Configurations in AWS Direct Connect](../../../architecture-diagrams/latest/active-active-and-active-passive-configurations-in-aws-direct-connect/active-active-and-active-passive-configurations-in-aws-direct-connect.md "../../../architecture-diagrams/latest/active-active-and-active-passive-configurations-in-aws-direct-connect/active-active-and-active-passive-configurations-in-aws-direct-connect.md")
- [Scaling
  your VPN throughput using Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-vpn-throughput-using-aws-transit-gateway/ "https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-vpn-throughput-using-aws-transit-gateway/")
