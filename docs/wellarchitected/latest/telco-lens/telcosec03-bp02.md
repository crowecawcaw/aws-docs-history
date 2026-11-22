

# TELCOSEC03-BP02 Provide cloud infrastructure to support signaling firewall deployments on roaming and interconnect interfaces

 CSPs deploy signaling firewalls on roaming and interconnect interfaces following GSMA IR.77 and FS.11 guidelines. When those firewalls run on cloud infrastructure, the cloud must supply the connectivity, performance, and high availability they need, while the CSP keeps ownership of the firewall policy and rules. 

 **Desired outcome:** 
+  The cloud infrastructure provides dedicated network interfaces for signaling firewall connectivity to interconnect partners, with appropriate security group configurations. 
+  Signaling firewall instances have enough compute and network performance to inspect signaling traffic at peak rates without adding latency that violates protocol timer budgets. 
+  High availability comes from cloud-based mechanisms such as multi-AZ deployment, health checks, and automatic failover rather than firewall-vendor cloud-specific logic. 

 **Common anti-patterns:** 
+  Routing signaling traffic through NAT gateways or load balancers that don't understand signaling protocols, breaking SCTP associations or Diameter connections. 
+  Deploying signaling firewalls in a single Availability Zone without failover, creating a single point of failure on the interconnect path. 
+  Sizing firewall instances for raw throughput rather than the consistent low latency that signaling inspection requires. 
+  Placing protocol-unaware middleboxes in the signaling path, so inspection and associations break under load. 

 **Benefits of establishing this best practice:** 
+  A clear responsibility boundary keeps the cloud providing infrastructure while the CSP owns signaling policy and GSMA compliance. 
+  Dedicated interfaces and appropriately sized instances mean signaling inspection doesn't add protocol-violating latency. 
+  Cloud-based high availability reduces the operational burden compared with custom failover scripting. 
+  Protocol-aware connectivity keeps SCTP associations and Diameter connections intact through the firewall path. 

 **Level of risk exposed if this best practice is not established:** Medium \#\# Implementation guidance Signaling firewalls sit on the boundary between the operator's network and external interconnect partners, inspecting SS7, MAP, Diameter, and SIP signaling for the attack patterns documented by GSMA. What operators actually need is infrastructure that meets signaling-specific requirements, which is often incongruent with decisions like implementing a signaling firewall with standard cloud architecture. 

 Signaling firewalls require direct connectivity to interconnect partners, usually over dedicated connections or VPN tunnels, and the path must carry the signaling protocols natively. SCTP for Diameter and M3UA shows why: a NAT gateway or load balancer without SCTP support breaks the association. Firewall interfaces must connect to partners without protocol-breaking middleboxes in the path. On those interfaces, configure security groups to permit only the signaling protocols and ports in use, and deny everything else. 

 Signaling volumes are modest next to user-plane traffic (thousands of transactions per second, not millions of packets), but they are latency-sensitive. Transaction latency must stay low enough to avoid retransmissions and timer expiry, so choose instances for consistent low latency rather than raw bandwidth. Failover must complete within SCTP and Diameter association timeout windows. Use AWS Direct Connect for dedicated connectivity to partners. Host the firewalls on latency-consistent Amazon EC2 instance types. Use Network Load Balancer or Amazon Route 53 health checks to drive failover within those timer budgets. \#\#\# Implementation steps 
+  Provision dedicated interconnect connectivity: establish AWS Direct Connect connections or site-to-site VPN tunnels to interconnect partners, with dedicated subnets and security groups for the signaling firewall interfaces that face them. 
+  Size instances for consistent low latency: select Amazon EC2 instance types with consistent, non-burstable network performance, prioritizing low jitter over raw bandwidth for signaling inspection. 
+  Deploy across Availability Zones with automated failover: run firewall instances in at least two Availability Zones and configure Network Load Balancer or Amazon Route 53 health checks that redirect traffic within SCTP and Diameter timeout windows. 
+  Restrict interfaces to signaling protocols: configure security groups on interconnect-facing interfaces to permit only the signaling protocols and ports in use (for example, SCTP/3868 for Diameter, TCP/5060-5061 for SIP, SCTP/2905 for M3UA) and deny all else. 
+  Provide logging infrastructure for firewall events: give the firewall instances a path to send security event logs to the operator's security operations, without prescribing which events to log, since that follows the CSP's GSMA obligations. \#\# Resources **Key AWS services:** 
+  [AWS Direct Connect](https://aws.amazon.com/directconnect/) 
+  [Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/) 
+  [Amazon Route 53](https://aws.amazon.com/route53/) 
+  [Amazon EC2](https://aws.amazon.com/ec2/) 