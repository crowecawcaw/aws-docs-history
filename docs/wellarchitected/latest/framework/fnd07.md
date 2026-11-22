

# Networking and connectivity

 A strong networking foundation balances centralized governance with operational efficiency. Decisions about network topology, protection controls, and shared services such as DNS shape how workloads connect, how traffic is inspected, and how teams move through normal and exceptional scenarios. This capability covers the best practices for designing, securing, and centrally managing network connectivity across the enterprise. 


|  FND07: How do you design, secure, and centrally manage network connectivity across the enterprise?  | 
| --- | 
|  [FND07-BP01 Define your network and connectivity strategy and centralized resources](fnd07-bp01.md)  | 
|  [FND07-BP02 Implement centralized network protection controls](fnd07-bp02.md)  | 
|  [FND07-BP03 Establish centralized DNS management](fnd07-bp03.md)  | 

## Capability intent
<a name="fnd07-intent"></a>
+  The network is designed as a single enterprise foundation, with topology, address allocation, and hybrid connectivity governed centrally and sized for growth rather than stitched together per workload. 
+  Traffic flowing north-south, east-west, and to shared services passes through consistent protection and inspection controls, so security posture does not depend on which team built the workload. 
+  DNS is operated as a shared service with uniform resolution, filtering, and failover behavior, and it remains resolvable through component and Region failures. 
+  Segmentation and least-privilege connectivity are expressed in routing and access controls and are continuously validated, rather than assumed once and left alone. 
+  Workload teams consume the network through self-service patterns, infrastructure-as-code modules, and documented exception processes, so enterprise standards are the path of least resistance. 

## Common issues to watch for
<a name="fnd07-issues"></a>
+  IP address plans are sized to current need with no reserves for new Regions, acquisitions, or hybrid partners, forcing renumbering work that the organization is rarely able to execute cleanly. 
+  Internet egress and inspection are distributed across accounts without consistent policy, so security controls drift between teams and create gaps that are only discovered during incidents. 
+  Firewall, WAF, and segmentation rules accumulate but are never reviewed, leaving allow lists far wider than the threats they were written for and eroding the value of centralized controls. 
+  DNS hosted zones are spread across accounts and providers with no clear ownership, which slows troubleshooting, complicates certificate issuance, and leaves domain renewals dependent on individuals. 
+  Segmentation is assumed rather than verified, so routing and access-control changes quietly open paths between workloads that should not communicate, and the gap is invisible until something exploits it. 
+  The network foundation is run as a ticket queue rather than a self-service product, so workload teams route around standards to keep moving and the governance model collapses in practice. 