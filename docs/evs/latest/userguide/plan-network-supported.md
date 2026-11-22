

# Supported network configurations

Amazon Elastic VMware Service supports the following network connections and VPC configurations in both deployment modes. The tables also list what Amazon EVS doesn’t support. In each table, the **Supported** column shows `Yes`, `No`, or `Required`, and the **Notes** column gives the condition or the alternative.

## Connections to on-premises networks and other VPCs
<a name="plan-network-supported-external"></a>

The following table lists the supported and unsupported connections to on-premises networks and other VPCs.


| Configuration | Supported | Notes | 
| --- | --- | --- | 
|  AWS Transit Gateway | Required | You must use a transit gateway to connect an Amazon EVS environment to your on-premises networks. The transit gateway does not learn NSX routes from Amazon VPC Route Server. After you create the environment, add static routes for the NSX overlay networks to the transit gateway route tables. | 
|  Direct Connect with a transit gateway | Yes | Associate the transit gateway with a Direct Connect gateway. For more information, see [Direct Connect gateways and transit gateway associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html). | 
|  AWS Site-to-Site VPN attached to a transit gateway | Yes | For more information, see [AWS Site-to-Site VPN attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html) in the * Amazon VPC Transit Gateway User Guide*. You can combine Site-to-Site VPN with Direct Connect. For more information, see [Private IP AWS Site-to-Site VPN with Direct Connect](https://docs.aws.amazon.com/vpn/latest/s2svpn/private-ip-dx.html). | 
|  AWS Cloud WAN | Yes | Like a transit gateway, Cloud WAN does not learn NSX routes from VPC Route Server. Add static routes for the NSX overlay networks. | 
|  Direct Connect private virtual interface (VIF) to the Amazon EVS VPC | No | Use a transit gateway with Direct Connect. | 
|  AWS Site-to-Site VPN that terminates directly in the Amazon EVS VPC | No | Attach the Site-to-Site VPN connection to a transit gateway. | 
| VPC peering | No | Use a transit gateway or Cloud WAN to connect to other VPCs. | 

For steps to connect on-premises networks, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md).

## Internet access
<a name="plan-network-supported-internet"></a>

The following table lists the supported options for internet access.


| Configuration | Supported | Notes | 
| --- | --- | --- | 
| NAT gateway for outbound internet access | Yes | Amazon EVS requires a NAT gateway for outbound internet connectivity. In Self-deployed mode, the VMware Cloud Foundation (VCF) Installer reaches the Broadcom online depot through it. For the subnet and route rules, see [Gateway route requirements](network-create-vpc.md#vpc-main-rt-reqs). | 
| Elastic IP addresses on the HCX VLAN subnet | Yes | Amazon EVS supports associating Elastic IP addresses only with the HCX VLAN subnet, for HCX internet connectivity. For more information, see [Plan HCX connectivity](plan-hcx-connectivity.md). | 
| Inspection of north-south traffic | Yes | You can place AWS Network Firewall or partner firewalls behind a Gateway Load Balancer at the internet ingress and egress points of the VPC. | 

## VPC and subnets
<a name="plan-network-supported-vpc"></a>

The following table lists the supported and unsupported VPC and subnet configurations.


| Configuration | Supported | Notes | 
| --- | --- | --- | 
| IPv4 VPC CIDR block of /22 or larger | Required | For sizing, see [Plan your VPC and VLAN subnets](plan-network-sizing.md). | 
| More than one Amazon EVS environment in the same VPC | No | Each Amazon EVS environment needs its own VPC. A VPC can’t be used by another deployed Amazon EVS environment. | 
| IPv6 | No | Amazon EVS supports IPv4 only. Amazon EVS also does not support private IPv6 Global Unicast Address (GUA) CIDRs. | 
| Subnets in more than one Availability Zone | No | An Amazon EVS environment runs in one Availability Zone. All VPC subnets that Amazon EVS uses must be in that Availability Zone. | 
| VPC, subnets, and environment in different accounts | No | You must create the VPC, the subnets, and the Amazon EVS environment in the same account. Amazon EVS does not support cross-account sharing of VPC subnets or of environments. | 
| Secondary VPC CIDR block for the public HCX CIDR | Required | Required for HCX internet connectivity. You add the public IPv4 CIDR block from your IPAM pool to the VPC as an additional CIDR. For more information, see [Plan HCX connectivity](plan-hcx-connectivity.md). | 
| Custom route table during environment creation | No | During creation, the VLAN subnets are implicitly associated with the VPC main route table. Configure the main route table with routes to your DNS servers and on-premises systems. Use a custom route table only after the environment is created. | 
| Explicit route table association of the VLAN subnets after creation | Required | After the environment is created, associate the VLAN subnets explicitly with a route table. Without this, NSX connectivity fails. For more information, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md). | 
| Gateway VPC endpoint for Amazon S3  | No | Use an interface VPC endpoint with AWS PrivateLink for Amazon S3. For more information, see [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) in the *Amazon Simple Storage Service User Guide*. | 

## Traffic control and workload placement
<a name="plan-network-supported-traffic"></a>

The following table lists the supported and unsupported options for traffic control and workload placement.


| Configuration | Supported | Notes | 
| --- | --- | --- | 
| Security groups on the network interfaces in VLAN subnets | No | Security groups do not apply to traffic on the elastic network interfaces in Amazon EVS VLAN subnets. Use a network ACL to control traffic to and from the VLAN subnets. For more information, see [Create a network ACL for VLAN subnet traffic](evs-env-nacl-cong.md). | 
| Network ACLs on VLAN subnets | Yes | You can use the default network ACL of the VPC or a custom network ACL. For HCX internet connectivity, we strongly recommend a custom network ACL dedicated to the HCX VLAN subnet. | 
| VCF management appliances on VLAN subnets | Yes | vCenter, NSX Manager, the NSX Edge nodes, SDDC Manager, and HCX appliances run on the VLAN subnets. | 
| Guest workload VMs on VLAN subnets | No | The VLAN subnets carry VCF underlay traffic only. Deploy workload VMs on NSX overlay networks. | 
| NSX Federation | Yes | Use the expansion VLAN subnets for Federation traffic. For more information, see [Set up NSX Federation](nsx-federation.md). | 

For the NSX Edge and routing limits, see [Plan NSX Edge and VPC Route Server design](plan-nsx-design.md).