

# REL02-BP02 Provision redundant connectivity between private networks in the cloud and on-premises environments

 Workloads in the cloud often depend on systems that stay in a corporate data center or private network. A single connection between the two environments is a single point of failure: if it drops, the dependent services stop communicating. Redundant connectivity uses two or more independent links and traffic paths, so the failure of one link does not sever the connection between environments. 

 **Desired outcome:** 
+  Your cloud and private networks stay connected when a single link, device, or location fails. 
+  You have two or more independent connections that follow diverse physical paths. 
+  Dynamic routing moves traffic to a healthy path automatically, without operator action. 
+  You know the bandwidth each path can carry and have sized backup paths for the traffic they must handle. 

 **Common anti-patterns:** 
+  Teams depend on a single network connection, which creates a single point of failure. 
+  Teams use one VPN tunnel, or multiple tunnels that terminate in the same Availability Zone. 
+  Teams rely on a single internet service provider for VPN connectivity, so there is no alternate path if that connection is interrupted. 
+  Teams omit dynamic routing protocols such as BGP that reroute traffic during a disruption. 
+  Teams ignore the bandwidth limits of VPN tunnels and overestimate their value as a backup. 

 **Benefits of establishing this best practice:** 
+  Dependent services across both environments communicate reliably during a link or device failure. 
+  Automatic rerouting keeps traffic flowing without operator action when a path fails. 
+  Diverse physical paths and providers reduce the chance that one event takes down all connectivity. 
+  Known bandwidth and sized backup paths prevent congestion when traffic shifts to a surviving link. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A dedicated connection such as [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) offers consistent bandwidth and low, predictable latency over a private link. A [Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-redundant-connection.html) runs over the public internet, costs less, and provisions faster, but its throughput and latency depend on internet conditions. Neither connection is resilient on its own. Resilience comes from how many independent paths you run and how physically diverse those paths are. 

 Maximum resilience, with a service level agreement of 99.99 percent, uses separate connections on distinct devices in more than one on-premises location and more than one Direct Connect location. This design withstands a device failure, a connectivity fault, or the loss of an entire location. High resilience, at 99.9 percent, uses two connections to two Direct Connect locations, which still protects against a fiber cut or device failure. A single connection protects against neither failure. The [AWS Direct Connect Resiliency Toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) provides a wizard that builds these topologies for you. 

 Use a VPN as a cost-effective backup to a primary Direct Connect link. A single Site-to-Site VPN connection provides two tunnels. Each tunnel must terminate in a different Availability Zone so that the loss of one zone does not take down both. Terminate a VPN on [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) to use equal-cost multipath (ECMP) routing across several tunnels. This raises aggregate throughput well beyond the roughly 1.25 Gbps limit of a single tunnel. Use more than one internet service provider, with separate physical routes to AWS, to keep connectivity alive when one provider fails. Measure a VPN's actual throughput under load, because its spare capacity is often less than expected. 

 Border Gateway Protocol (BGP) is the dynamic routing protocol that decides which path traffic takes and reroutes it when a path fails. Without dynamic routing, a backup link stays idle until an operator reroutes traffic manually. With BGP, the network detects the failure and shifts traffic to a surviving path in seconds, using the routing policies you define. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose a connectivity resilience target:** Decide whether the dependency between environments needs maximum resilience (99.99 percent) or high resilience (99.9 percent), and design the topology to match. Use the [AWS Direct Connect Resiliency Toolkit](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) to generate a connection layout for the target you choose. 

1.  **Deploy redundant dedicated connections:** Provision two or more AWS Direct Connect connections that terminate on distinct devices across more than one Direct Connect location. If your availability needs span geography, extend redundant connections to more than one AWS Region. 

1.  **Add a VPN backup over diverse paths:** Provision an AWS Site-to-Site VPN as a backup, and terminate it on [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html) to allow ECMP across tunnels. Terminate each tunnel in a different Availability Zone, use redundant on-premises hardware, and connect through more than one internet service provider. 

1.  **Enable BGP dynamic routing:** Run [BGP across your connections](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html) so traffic reroutes automatically when a path fails. Set routing policies and communities that reflect your primary and backup path preferences. 

1.  **Evaluate network appliances where needed:** If you use third-party appliances to terminate VPNs or [extend an SD-WAN to AWS](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/aws-transit-gateway-sd-wan.html), deploy redundant instances across different Availability Zones. Review [AWS Marketplace network infrastructure appliances](https://aws.amazon.com/marketplace/b/3141913d-a073-4452-8473-843f58081505) for options. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL02-BP01 Use highly available network connectivity for your workload public endpoints](rel02-bp01.md) 
+  [REL10-BP01 Deploy the workload to multiple locations](rel10-bp01.md) 
+  [REL10-BP02 Automate recovery for components constrained to a single location](rel10-bp02.md) 

 **Related documents:** 
+  [AWS Direct Connect resiliency recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/) 
+  [Redundant AWS Site-to-Site VPN connections for failover](https://docs.aws.amazon.com/vpn/latest/s2svpn/vpn-redundant-connection.html) 
+  [Direct Connect routing policies and BGP communities](https://docs.aws.amazon.com/directconnect/latest/UserGuide/routing-and-bgp.html) 
+  [Active/Active and Active/Passive Configurations in AWS Direct Connect](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/electronics-hpc/active-active-and-active-passive-configurations-in-aws-direct-connect.html) 
+  [Introduction](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/introduction.html) 
+  [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) 
+  [Connect your VPC to services using AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-overview.html) 
+  [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) 
+  [What is AWS Transit Gateway for Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) 
+  [What is AWS Site-to-Site VPN?](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) 
+  [Direct Connect gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-gateways.html) 
+  [APN Partner: partners that can help plan your networking](https://partners.amazonaws.com/search/partners?keyword=network) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Advanced VPC design and new capabilities (NET340)](https://www.youtube.com/watch?v=40QfxdvDGsw) 
+  [AWS re:Invent 2025 - Hybrid connectivity at scale: A deep dive into AWS Direct Connect (NET403)](https://www.youtube.com/watch?v=OXfOwjDd6lY) 