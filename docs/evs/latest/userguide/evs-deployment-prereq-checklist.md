

# Deployment prerequisite checklist

Use the following tables to collect the values that you need to deploy an Amazon Elastic VMware Service environment that runs VMware Cloud Foundation (VCF). The checklist has one table for each topic. Your environment deployment fails if a required value is missing or does not meet its requirement.

## How to use this checklist
<a name="evs-prereq-how-to-use"></a>

Use the checklist as follows.
+ Fill in one copy of the checklist for each environment. Write your values in the **Your value** column.
+ Check the **Mode** column. `Both` rows apply to Self-deployed and EVS-deployed environments. Rows marked `Self-deployed` or `EVS-deployed` apply only to that mode. For the differences between the modes, see [Differences between deployment modes](deployment-mode-differences.md).
+ Complete the tables in order. In an EVS-deployed environment, you need every value before you create the environment. In a Self-deployed environment, you need some values later, and the table says when.
+ Decide the network values carefully. You can’t change the VPC CIDR block, add VLAN subnets, or change the VLAN subnet CIDR blocks after you create the environment. For sizing, see [Plan your VPC and VLAN subnets](plan-network-sizing.md).
+ Use the example values only as a pattern. The examples use one consistent address plan, with the VPC CIDR block `10.1.0.0/20`.

## Account, Region, and capacity
<a name="evs-prereq-account"></a>

Collect the following account, Region, and capacity values.


| Item | Mode | Requirement | Example value | Your value | 
| --- | --- | --- | --- | --- | 
|  AWS account ID | Both | Access to an AWS account. You create the VPC, the subnets, and the environment in this account. | 111122223333 |  | 
|  AWS Region | Both | A Region where Amazon EVS is available. For the list, see [AWS Regions for Amazon EVS](regions-reference.md). | US West (Oregon) |  | 
|  AWS Support plan | Both | An AWS Business Support, AWS Enterprise On-Ramp, or AWS Enterprise Support plan. Environment creation fails if your account isn’t enrolled in one of these plans. |  AWS Business Support |  | 
| Service quotas | Both | A quota for the number of hosts in an environment that is high enough for your VCF topology. For more information, see [Service quotas for Amazon EVS](service-quotas-evs.md). | The number of hosts that you deploy |  | 
| Instance type | Both | An instance type that Amazon EVS supports for your VCF version. All hosts in a cluster use the same instance type. For more information, see [Choose instance types](plan-instance-types.md). |  `i4i.metal`  |  | 
| Amazon EC2 Capacity Reservation | Both | A Capacity Reservation. We recommend one, so that capacity is available when you add hosts. For more information, see [Reserve capacity for hosts](plan-capacity.md). | cr-0123456789abcdef0 |  | 

## External storage for diskless hosts
<a name="evs-prereq-diskless"></a>

This section applies to Self-deployed environments that run VCF 9.x.

Diskless instance types, such as `r7i.metal-24xl` and `r7i.metal-48xl`, have no local storage, so the VCF management domain and your workloads run on external storage. Collect the following value if you use diskless hosts.


| Item | Mode | Requirement | Example value | Your value | 
| --- | --- | --- | --- | --- | 
| External storage | Self-deployed | A datastore on external storage in the same VPC and Availability Zone as the environment, sized for the VCF management domain, that the VCF Installer accepts as principal storage. For more information, see [External storage options for diskless hosts](external-storage-diskless.md). | Amazon FSx for OpenZFS, 7,168 GiB, NFS v3 |  | 

## VCF subscriptions
<a name="evs-prereq-licenses"></a>

You bring your own VCF subscription in both modes. When you provide the license keys depends on the mode. For more information, see [VCF licensing](vcf-license-mgmt.md).


| Item | Mode | Requirement | Example value | Your value | 
| --- | --- | --- | --- | --- | 
| Broadcom Site ID | EVS-deployed | The Site ID that Broadcom gives you for the Broadcom support portal. You enter it when you create the environment. | 01234567 |  | 
| VCF solution key | EVS-deployed | A valid, active VCF license key for the VCF stack that no other Amazon EVS environment uses. You enter it when you create the environment. | ABCDE-FGHIJ-KLMNO-PQRSTU-VWXYZ |  | 
| vSAN license key | EVS-deployed | A valid, active vSAN license key that no other Amazon EVS environment uses. You enter it when you create the environment. | ABCDE-FGHIJ-KLMNO-PQRSTU-VWXYZ |  | 
| VCF license keys | Self-deployed | License keys that you add in your VCF management appliance after you install VCF. You don’t enter them when you create the environment. | ABCDE-FGHIJ-KLMNO-PQRSTU-VWXYZ |  | 

## VPC and service access subnet
<a name="evs-prereq-vpc"></a>

Collect the following VPC and service access subnet values.


| Item | Mode | Requirement | Example value | Your value | 
| --- | --- | --- | --- | --- | 
| VPC ID | Both | The VPC that Amazon EVS deploys the environment into. | vpc-0abcdef1234567890 |  | 
| VPC CIDR block | Both | An IPv4 CIDR block of /22 or larger, large enough for the service access subnet and all VLAN subnets. Use a CIDR block that is unique across your environments. Each environment needs its own VPC. You can’t change it after you create the environment. | 10.1.0.0/20 |  | 
| Service access subnet ID | Both | A standard VPC subnet that Amazon EVS uses for service access. For more information, see [Concepts and components of Amazon EVS](concepts.md). | subnet-abcdef1234567890e |  | 
| Service access subnet CIDR block | Both | A CIDR block inside a CIDR block that is associated with the VPC. We recommend a /24 netmask. | 10.1.0.0/24 |  | 
| Availability Zone | Both | One Availability Zone for all VPC subnets, identified by its Availability Zone ID. For more information, see [Create a VPC with subnets and route tables](network-create-vpc.md). | usw2-az1 |  | 

## VLAN subnets
<a name="evs-prereq-vlans"></a>

Amazon EVS creates these VLAN subnets when you create the environment, in both modes. Every CIDR block must have a netmask from /28 to /24 and must be inside a CIDR block that is associated with the VPC. It must not overlap with any other subnet in the VPC, including the other VLAN subnets and the service access subnet. You can’t add VLAN subnets or change their CIDR blocks after you create the environment. For sizing guidance, see [Plan your VPC and VLAN subnets](plan-network-sizing.md).


| Item | Mode | Requirement | Example value | Your value | 
| --- | --- | --- | --- | --- | 
| Host management VLAN CIDR block | Both | /28 to /24. | 10.1.1.0/24 |  | 
| vMotion VLAN CIDR block | Both | The same size as the host management VLAN. | 10.1.2.0/24 |  | 
| vSAN VLAN CIDR block | Both | The same size as the host management VLAN. | 10.1.3.0/24 |  | 
| VTEP VLAN CIDR block | Both | The same size as the host management VLAN. | 10.1.4.0/24 |  | 
| Edge VTEP VLAN CIDR block | Both | /28 to /24. | 10.1.5.0/24 |  | 
| Management VM VLAN CIDR block | Both | /28 to /24. | 10.1.6.0/24 |  | 
| HCX uplink VLAN CIDR block | Both | /28 to /24 for a private VMware Hybrid Cloud Extension (HCX) VLAN. Exactly /28 for a public HCX VLAN, using the public CIDR block in [HCX internet connectivity (optional)](#evs-prereq-hcx). | 10.1.7.0/24 |  | 
| NSX uplink VLAN CIDR block | Both | /28 to /24. The route server peer IP addresses come from this CIDR block. | 10.1.8.0/24 |  | 
| Expansion VLAN 1 CIDR block | Both | /28 to /24. | 10.1.9.0/24 |  | 
| Expansion VLAN 2 CIDR block | Both | /28 to /24. | 10.1.10.0/24 |  | 

## DNS, NTP, and the DHCP option set
<a name="evs-prereq-dns-ntp"></a>

Amazon EVS reads the DNS servers, the domain name and the NTP servers from the DHCP option set of your VPC. For the configuration steps, see [Configure DNS and NTP with a DHCP option set](network-dhcp-dns-ntp.md).


| Item | Mode | Requirement | Example value | Your value | 
| --- | --- | --- | --- | --- | 
| DHCP option set ID | Both | A DHCP option set with at least two DNS servers, your DNS domain name, and an NTP server. You can use Amazon Route 53 or your own DNS servers. | dopt-0a1b2c3d |  | 
| Primary DNS server IP address | Both | A reachable DNS server that answers queries. The VPC main route table must have a route to it. For Route 53, see [Create private hosted zones and a Resolver inbound endpoint](network-dhcp-dns-ntp.md#network-dhcp-dns-zones). | 10.1.0.10 |  | 
| Secondary DNS server IP address | Both | A second reachable DNS server. | 10.1.0.20 |  | 
| NTP server IP addresses | Both | At least one NTP server, and up to four, in the DHCP option set. Amazon EVS hosts use the Amazon Time Sync Service address `169.254.169.123`. For the VCF Installer, see [Time (NTP) settings](vcf-installer-settings.md#installer-settings-ntp). | IPv4 address of your NTP server |  | 
| DNS domain name | Both | A valid, unexpired domain name. The FQDN of each host and VCF management appliance, including this domain name, must not exceed 62 characters. An FQDN can contain only letters, digits, the minus sign (-), and periods between labels. |  `evs.example.com`  |  | 

## DNS records for hosts and appliances
<a name="evs-prereq-dns-records"></a>

Each host and each VCF management appliance needs an A record in a forward lookup zone and a pointer (PTR) record in a reverse lookup zone. The records must resolve through the DNS servers in your DHCP option set, with no duplicate host names or IP addresses.
+ In an EVS-deployed environment, create all records before you create the environment.
+ In a Self-deployed environment, create the ESX host records before you add each host, and the appliance records before you install VCF. For more information, see [Step 2: Create DNS records](self-deployed-host-dns-records.md).

We recommend host names of 15 characters or fewer, as a NetBIOS practice.


| Record | Mode | Example IP address | Example host name | Your value | 
| --- | --- | --- | --- | --- | 
| ESX host 1 | Both | 10.1.1.11 | esxi01 |  | 
| ESX host 2 | Both | 10.1.1.12 | esxi02 |  | 
| ESX host 3 | Both | 10.1.1.13 | esxi03 |  | 
| ESX host 4 | Both | 10.1.1.14 | esxi04 |  | 
| vCenter Server appliance | Both | 10.1.6.10 | vc01 |  | 
| NSX Manager cluster | Both | 10.1.6.11 | nsx |  | 
| NSX Manager 1 appliance | Both | 10.1.6.16 | nsx01 |  | 
| NSX Manager 2 appliance (three-node cluster only) | Both | 10.1.6.17 | nsx02 |  | 
| NSX Manager 3 appliance (three-node cluster only) | Both | 10.1.6.18 | nsx03 |  | 
| NSX Edge 1 appliance | Both | 10.1.6.14 | edge01 |  | 
| NSX Edge 2 appliance | Both | 10.1.6.15 | edge02 |  | 
| SDDC Manager appliance | EVS-deployed | 10.1.6.12 | sddcm01 |  | 
| Cloud Builder appliance | EVS-deployed | 10.1.6.13 | cb01 |  | 
| Other VCF management appliances for your VCF version | Self-deployed | An address in the Management VM VLAN subnet | The host name that you configure during VCF installation |  | 

ESX host records use addresses in the host management VLAN subnet. VCF management appliance records use addresses in the Management VM VLAN subnet.

## Route tables, network ACL, and transit gateway
<a name="evs-prereq-routing"></a>

Collect the following route table, network ACL, and transit gateway values.


| Item | Mode | Requirement | Example value | Your value | 
| --- | --- | --- | --- | --- | 
| Main route table ID | Both | A main route table with routes to your DNS servers and to any on-premises systems that the deployment needs. Amazon EVS associates the VLAN subnets with the main route table when it creates them. | rtb-0123456789abcdef0 |  | 
| Network ACL ID | Both | A network ACL that allows the traffic in [Required traffic](evs-env-nacl-cong.md#evs-env-nacl-rules). | acl-0f62c640e793a38a3 |  | 
| Transit gateway ID | Both | A transit gateway, which you need to connect the environment to on-premises networks. For the supported connections, see [Supported network configurations](plan-network-supported.md). | tgw-0262a0e521EXAMPLE |  | 
| On-premises connectivity method | Both |  Direct Connect, AWS Site-to-Site VPN, or both, with the transit gateway. For more information, see [Private IP AWS Site-to-Site VPN with Direct Connect](https://docs.aws.amazon.com/vpn/latest/s2svpn/private-ip-dx.html). | Site-to-Site VPN with Direct Connect |  | 

## Amazon VPC Route Server
<a name="evs-prereq-route-server"></a>

For the design rules, see [Plan NSX Edge and VPC Route Server design](plan-nsx-design.md).
+ In an EVS-deployed environment, you enter two route server peers when you create the environment, and Amazon EVS configures Border Gateway Protocol (BGP) on the NSX Edge nodes.
+ In a Self-deployed environment, you don’t enter peers when you create the environment. You configure BGP between the Tier-0 gateway and the route server after you install VCF. For more information, see [Step 5: Configure NSX networking](self-deployed-nsx-edge.md).


| Item | Mode | Requirement | Example value | Your value | 
| --- | --- | --- | --- | --- | 
| Route server ID | Both | A route server associated with your VPC. | rs-0a1b2c3d4e5f67890 |  | 
| Amazon-side ASN | Both | An autonomous system number (ASN) in the range 1 to 4294967295. We recommend a private ASN, 64512 to 65534 (16-bit) or 4200000000 to 4294967294 (32-bit). | 65022 |  | 
| NSX Edge Tier-0 ASN | Both | An ASN that matches the peer ASN on every route server peer. The NSX Edge default is 65000. | 65000 |  | 
| Route server endpoint IDs | Both | Two endpoints, both in the service access subnet. | rse-0123456789abcdef0, rse-fedcba9876543210f |  | 
| Route server peer 1 ID and IP address | Both | A unique, unused address from the NSX uplink VLAN CIDR block (`PeerAddress`). In an EVS-deployed environment, Amazon EVS assigns it to NSX Edge 1. | rsp-0123456789abcdef0, 10.1.8.10 |  | 
| Route server peer 2 ID and IP address | Both | A unique, unused address from the NSX uplink VLAN CIDR block. In an EVS-deployed environment, Amazon EVS assigns it to NSX Edge 2. | rsp-fedcba9876543210f, 10.1.8.200 |  | 
| Additional route server peers | Self-deployed | Two more route server peers. We recommend four peers in a full mesh, so that each Edge node peers with both endpoints. | Two more peer IDs |  | 
| Route server propagation | Both | Route server propagation that is enabled on the route table associated with the service access subnet. Each propagated route table must have at least one explicit subnet association. | rtb-0123456789abcdef0 |  | 

## EC2 key pair and Allowed AMIs
<a name="evs-prereq-ec2"></a>

Collect the following EC2 key pair value.


| Item | Mode | Requirement | Example value | Your value | 
| --- | --- | --- | --- | --- | 
| EC2 key pair name | Both | A unique key pair name. Amazon EVS uses the key pair to connect to your hosts. |  `my-ec2-key-pair`  |  | 

### EC2 Allowed AMIs (only if you restrict AMI usage)
<a name="evs-prereq-allowed-amis"></a>

If you use Allowed AMIs in your account, your image criteria must include the Amazon EVS AMIs, or you can’t create an environment or add a host. For more information, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) in the *Amazon EC2 User Guide*.


| Item | Mode | Requirement | Image criteria | Your value | 
| --- | --- | --- | --- | --- | 
| Allowed AMIs criteria | Both | Image criteria that include the Amazon EVS AMIs. |  `ImageProvider: amazon` `ImageName: AmazonEVS-*`  |  | 

## HCX internet connectivity (optional)
<a name="evs-prereq-hcx"></a>

You need these values only for HCX internet connectivity.

For the rules, see [Plan HCX connectivity](plan-hcx-connectivity.md).

For the steps that produce these values, see [Part 1 of Configure HCX public internet connectivity](evs-env-hcx-internet-access.md#hcx-internet-config). You complete Part 1 before you create the environment.


| Item | Mode | Requirement | Example value | Your value | 
| --- | --- | --- | --- | --- | 
| IPAM ID | Both | An Amazon VPC IP Address Manager (IPAM) that provides public IPv4 addresses. | ipam-0123456789abcdef0 |  | 
| IPAM pool ID | Both | A public IPv4 IPAM pool with Amazon-owned addresses, in the Region of your VPC. | ipam-pool-0123456789abcdef0 |  | 
| Public HCX VLAN CIDR block | Both | A /28 public IPv4 CIDR block from the IPAM pool. Add it to the VPC as an additional CIDR by entering it manually, and use it for the HCX uplink VLAN subnet. | 203.0.113.0/28 |  | 
| Elastic IP addresses | Both | At least two Elastic IP addresses from the same IPAM pool, for HCX Manager and HCX Interconnect (HCX-IX), plus one for each HCX network appliance. Up to 13. For the reserved addresses, see [Plan HCX connectivity](plan-hcx-connectivity.md). | eipalloc-0123456789abcdef0, eipalloc-0123456789abcdef1, eipalloc-0123456789abcdef2 |  | 

When you have all the values, build the network. For more information, see [Build the network foundation](network-foundation.md).