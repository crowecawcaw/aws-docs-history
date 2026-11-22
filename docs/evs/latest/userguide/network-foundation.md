

# Build the network foundation

Amazon Elastic VMware Service deploys your environment into a VPC that you create and configure. Both deployment modes use the same network foundation, so you complete these tasks once before you follow the Self-deployed or the EVS-deployed path.

Before you start, plan your CIDR blocks and VLAN subnets. For more information, see [Plan your VPC and VLAN subnets](plan-network-sizing.md).

Complete the tasks in the following table in order. Each task uses resources from the task before it. The **When** column shows which tasks you complete before you create the environment, after you create it, and after you delete it.


| Task | What it produces | When | 
| --- | --- | --- | 
|  [Create a VPC with subnets and route tables](network-create-vpc.md)  | A VPC, a service access subnet, an optional public subnet, route tables, and the gateway routes on the main route table. | Before you create the environment. | 
|  [Configure DNS and NTP with a DHCP option set](network-dhcp-dns-ntp.md)  | Optional private hosted zones and a Resolver inbound endpoint, a DHCP option set with DNS servers, a domain name, and NTP servers, the DNS record requirements, and an optional instance to reach the VPC. | Before you create the environment. | 
|  [Set up VPC Route Server and on-premises connectivity](network-route-server.md)  | A route server in Amazon VPC Route Server with two endpoints, peers, and propagation, and optional on-premises connectivity through a transit gateway. | Before you create the environment. Update the transit gateway route tables after you create it. | 
|  [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md)  | A network ACL with the rules that the VLAN subnets need. | Before you create the environment. Associate the network ACL with the VLAN subnets after you create the environment. Update the rules when your traffic rules change. | 
|  [Part 1 of Configure HCX public internet connectivity](evs-env-hcx-internet-access.md#hcx-internet-config) (optional) | An IPAM, a public IPv4 pool, Elastic IP addresses, and a public CIDR block in your VPC for the public HCX VLAN subnet. You need them only if you use VMware HCX over the internet. | Before you create the environment, because you can’t change VLAN CIDR blocks later. Associate the Elastic IP addresses after you create the environment, as described in Part 2 of the same topic. | 
|  [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md)  | Explicit route table associations for every VLAN subnet. | After you create the environment. | 
|  [Clean up network resources](cleanup.md)  | No new resources. Deletes the network resources that you created. | After you delete the environment. | 

When the network foundation is ready, continue with your deployment mode:
+ For VMware Cloud Foundation (VCF) 9.x, see [Deploy in Self-deployed mode](getting-started-self-deployed.md).
+ For VCF 5.2.x, see [Deploy in EVS-deployed mode](evs-deployed-overview.md).

**Topics**
+ [Create a VPC with subnets and route tables](network-create-vpc.md)
+ [Configure DNS and NTP with a DHCP option set](network-dhcp-dns-ntp.md)
+ [Set up VPC Route Server and on-premises connectivity](network-route-server.md)
+ [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md)
+ [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md)
+ [Clean up network resources](cleanup.md)