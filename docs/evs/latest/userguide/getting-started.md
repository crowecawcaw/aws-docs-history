# Getting started with Amazon Elastic VMware Service

Use this guide to get started with Amazon Elastic VMware Service (Amazon EVS).
You’ll learn how to create an Amazon EVS environment with hosts within your own Amazon Virtual Private Cloud (VPC).

After you’re finished, you’ll have an Amazon EVS environment that you can use to migrate your VMware vSphere-based workloads to the AWS Cloud.

###### Important

To get started as simply and quickly as possible, this topic includes steps to create a VPC, and specifies minimum requirements for DNS server configuration and Amazon EVS environment creation.
Before creating these resources, we recommend that you plan out your IP address space and DNS record setup that meets your requirements.
You should also familiarize yourself with VCF 5.2.x requirements. See the [VCF 5.2.x release notes](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes.html") for relevant release information.

###### Important

For information about VCF versions provided by Amazon EVS, see [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md "versions-provided.md").

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Create a VPC with subnets and route tables](#getting-started-create-vpc "#getting-started-create-vpc")
- [Choose your HCX connectivity option](#hcx-connectivity-choice "#hcx-connectivity-choice")
- [Configure the VPC main route table](#getting-started-vpc-main-route-table-config "#getting-started-vpc-main-route-table-config")
- [Configure DNS and NTP servers using the VPC DHCP option set](#getting-started-config-dns-ntp-dhcp "#getting-started-config-dns-ntp-dhcp")
- [Set up a VPC Route Server instance with endpoints and peers](#getting-started-create-rs-resources "#getting-started-create-rs-resources")
- [Create a network ACL to control Amazon EVS VLAN subnet traffic](#getting-started-create-nacl-vlan-traffic "#getting-started-create-nacl-vlan-traffic")
- [Create an Amazon EVS environment](#getting-started-create-env "#getting-started-create-env")
- [Verify Amazon EVS environment creation](#verify-env-creation "#verify-env-creation")
- [Explicitly associate Amazon EVS VLAN subnets to a VPC route table](#getting-started-associate-vlans "#getting-started-associate-vlans")
- [Retrieve VCF credentials and access VCF management appliances](#access-vcf "#access-vcf")
- [Clean up](#cleanup "#cleanup")
- [Next steps](#getting-started-next-steps "#getting-started-next-steps")

## Prerequisites

Before getting started, you must complete the Amazon EVS prerequisite tasks. For more information, see [Setting up Amazon Elastic VMware Service](setting-up.md "setting-up.md").

## Create a VPC with subnets and route tables

###### Note

The VPC, subnets, and Amazon EVS environment must all be created in the same account.
Amazon EVS does not support cross-account sharing of VPC subnets or Amazon EVS environments.

###### Example

Amazon VPC console

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").
2. On the VPC dashboard, choose **Create VPC**.
3. For **Resources to create**, choose **VPC and more**.
4. Keep **Name tag auto-generation** selected to create Name tags for the VPC resources, or clear it to provide your own Name tags for the VPC resources.
5. For **IPv4 CIDR block**, enter an IPv4 CIDR block.
   A VPC must have an IPv4 CIDR block.
   Ensure that you create a VPC that is adequately sized to accommodate the Amazon EVS subnets.
   For more information, see [Amazon EVS networking considerations](architecture.md#evs-subnets "architecture.md#evs-subnets").

###### Note

Amazon EVS does not support IPv6 at this time. 6. Keep **Tenancy** as `Default`.
With this option selected, EC2 instances that are launched into this VPC will use the tenancy attribute specified when the instances are launched.
Amazon EVS launches bare metal EC2 instances on your behalf. 7. For **Number of Availability Zones (AZs)**, choose **1**.

###### Note

Amazon EVS only supports Single-AZ deployments at this time. 8. Expand **Customize AZs** and choose the AZ for your subnets.

###### Note

You must deploy in an AWS Region where Amazon EVS is supported.
For more information about Amazon EVS Region availability, see [Amazon Elastic VMware Service endpoints and quotas](../../../general/latest/gr/evs.md "../../../general/latest/gr/evs.md") in the _AWS General Reference Guide_. 9. (Optional) If you need internet connectivity, for **Number of public subnets**, choose **1**. 10. For **Number of private subnets**, choose **1**.
This private subnet will be used as the service access subnet that you provided to Amazon EVS during the environment creation step.
For more information, see [Service access subnet](concepts.md#concepts-service-access-subnet "concepts.md#concepts-service-access-subnet"). 11. To choose the IP address ranges for your subnets, expand **Customize subnets CIDR blocks**.

###### Note

Amazon EVS VLAN subnets will also need to be created from this VPC CIDR space.
Ensure that you leave enough space in the VPC CIDR block for the VLAN subnets that the service requires.
For more information, see [Amazon EVS networking considerations](architecture.md#evs-subnets "architecture.md#evs-subnets") 12. (Optional) To grant internet access over IPv4 to resources, for **NAT gateways**, choose **In 1 AZ**.
Note that there is a cost associated with NAT gateways.
For more information, see [Pricing for NAT gateways](../../../vpc/latest/userguide/nat-gateway-pricing.md "../../../vpc/latest/userguide/nat-gateway-pricing.md").

###### Note

Amazon EVS requires the use of a NAT gateway to enable outbound internet connectivity. 13. For **VPC endpoints**, choose **None**.

###### Note

Amazon EVS does not support gateway VPC endpoints for Amazon S3 at this time.
To enable Amazon S3 connectivity, you must set up an interface VPC endpoint using AWS PrivateLink for Amazon S3.
For more information, see [AWS PrivateLink for Amazon S3](../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md "../../../AmazonS3/latest/userguide/privatelink-interface-endpoints.md") in the _Amazon Simple Storage Service User Guide_. 14. For **DNS options**, keep the defaults selected.
Amazon EVS requires your VPC to have DNS resolution capability for all VCF components. 15. (Optional) To add a tag to your VPC, expand **Additional tags**, choose **Add new tag**, and enter a tag key and a tag value. 16. Choose **Create VPC**.

###### Note

During VPC creation, Amazon VPC automatically creates a main route table and implicitly associates subnets to it by default.

AWS CLI

1. Open a terminal session.
2. Create a VPC with a private subnet and optional public subnet in a single Availability Zone.

```
aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --instance-tenancy default \
  --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=evs-vpc}]'
---
. Store the VPC ID for use in subsequent commands.
+
[source,bash]
```

VPC_ID=$(aws ec2 describe-vpcs \
 --filters Name=tag:Name,Values=evs-vpc \
 --query 'Vpcs[0].VpcId' \
 --output text)

---

3. Enable DNS hostnames and DNS support.

```
aws ec2 modify-vpc-attribute \
  --vpc-id $VPC_ID \
  --enable-dns-hostnames
aws ec2 modify-vpc-attribute \
  --vpc-id $VPC_ID \
  --enable-dns-support
```

4. Create a private subnet in the VPC.

```
aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.1.0/24 \
  --availability-zone us-west-2a \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=evs-private-subnet}]'
```

5. Store the private subnet ID for use in subsequent commands.

```
PRIVATE_SUBNET_ID=$(aws ec2 describe-subnets \
  --filters Name=tag:Name,Values=evs-private-subnet \
  --query 'Subnets[0].SubnetId' \
  --output text)
```

6. (Optional) Create a public subnet if internet connectivity is needed.

```
aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.0.0/24 \
  --availability-zone us-west-2a \
  --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=evs-public-subnet}]'
```

7. (Optional) Store the public subnet ID for use in subsequent commands.

```
PUBLIC_SUBNET_ID=$(aws ec2 describe-subnets \
  --filters Name=tag:Name,Values=evs-public-subnet \
  --query 'Subnets[0].SubnetId' \
  --output text)
```

8. (Optional) Create and attach an internet gateway if the public subnet is created.

```
aws ec2 create-internet-gateway \
  --tag-specifications 'ResourceType=internet-gateway,Tags=[{Key=Name,Value=evs-igw}]'

IGW_ID=$(aws ec2 describe-internet-gateways \
  --filters Name=tag:Name,Values=evs-igw \
  --query 'InternetGateways[0].InternetGatewayId' \
  --output text)

aws ec2 attach-internet-gateway \
  --vpc-id $VPC_ID \
  --internet-gateway-id $IGW_ID
```

9. (Optional) Create a NAT gateway if internet connectivity is needed.

```
aws ec2 allocate-address \
  --domain vpc \
  --tag-specifications 'ResourceType=elastic-ip,Tags=[{Key=Name,Value=evs-nat-eip}]'

EIP_ID=$(aws ec2 describe-addresses \
  --filters Name=tag:Name,Values=evs-nat-eip \
  --query 'Addresses[0].AllocationId' \
  --output text)

aws ec2 create-nat-gateway \
  --subnet-id $PUBLIC_SUBNET_ID \
  --allocation-id $EIP_ID \
  --tag-specifications 'ResourceType=natgateway,Tags=[{Key=Name,Value=evs-nat}]'
```

10. Create and configure the necessary route tables.

```
aws ec2 create-route-table \
  --vpc-id $VPC_ID \
  --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=evs-private-rt}]'

PRIVATE_RT_ID=$(aws ec2 describe-route-tables \
  --filters Name=tag:Name,Values=evs-private-rt \
  --query 'RouteTables[0].RouteTableId' \
  --output text)

aws ec2 create-route-table \
  --vpc-id $VPC_ID \
  --tag-specifications 'ResourceType=route-table,Tags=[{Key=Name,Value=evs-public-rt}]'

PUBLIC_RT_ID=$(aws ec2 describe-route-tables \
  --filters Name=tag:Name,Values=evs-public-rt \
  --query 'RouteTables[0].RouteTableId' \
  --output text)
```

11. Add the necessary routes to the route tables.

```
aws ec2 create-route \
  --route-table-id $PUBLIC_RT_ID \
  --destination-cidr-block 0.0.0.0/0 \
  --gateway-id $IGW_ID

aws ec2 create-route \
  --route-table-id $PRIVATE_RT_ID \
  --destination-cidr-block 0.0.0.0/0 \
  --nat-gateway-id $NAT_GW_ID
```

12. Associate the route tables with your subnets.

```
aws ec2 associate-route-table \
  --route-table-id $PRIVATE_RT_ID \
  --subnet-id $PRIVATE_SUBNET_ID

aws ec2 associate-route-table \
  --route-table-id $PUBLIC_RT_ID \
  --subnet-id $PUBLIC_SUBNET_ID
```

###### Note

During VPC creation, Amazon VPC automatically creates a main route table and implicitly associates subnets to it by default.

## Choose your HCX connectivity option

Select one connectivity option for your Amazon EVS environment:

- **Private connectivity**: Provides high-performance network pathways for HCX, optimizing reliability and consistency.
  Requires use of AWS Direct Connect or Site-to-Site VPN for external network connectivity.
- **Internet connectivity**: Uses the public internet to establish a flexible migration path that is quick to set up.
  Requires use of VPC IP Address Manager (IPAM) and Elastic IP addresses.

For detailed analysis, see [HCX connectivity options](migrate-evs-hcx.md#migrate-evs-hcx-connectivity "migrate-evs-hcx.md#migrate-evs-hcx-connectivity").

**Choose your option:**

- **Option A: Private connectivity only** → Continue to [Configure the VPC main route table](#getting-started-vpc-main-route-table-config "#getting-started-vpc-main-route-table-config").
- **Option B: Internet connectivity** → Continue to [HCX internet connectivity setup](#hcx-internet-config "#hcx-internet-config").

###### Note

Skip this section if you chose HCX private connectivity and continue to [Configure the VPC main route table](#getting-started-vpc-main-route-table-config "#getting-started-vpc-main-route-table-config").

To enable HCX internet connectivity for Amazon EVS, you must:

- Ensure that your VPC IP Address Manager (IPAM) quota for Amazon-provided contiguous public IPv4 CIDR block netmask length is /28 or greater.

###### Important

Use of any Amazon-provided contiguous public IPv4 CIDR block with a netmask length smaller than /28 will result in HCX connectivity issues.
For more information about increasing IPAM quotas, see [Quotas for your IPAM](../../../vpc/latest/ipam/quotas-ipam.md "../../../vpc/latest/ipam/quotas-ipam.md").

- Create an IPAM and a public IPv4 IPAM pool with a CIDR that has a a minimum netmask length of /28.
- Allocate at least two Elastic IP addresses (EIPs) from the IPAM pool for the HCX Manager and HCX Interconnect (HCX-IX) appliances.
  Allocate an additional Elastic IP address for each HCX network appliance that you need to deploy.
- Add the public IPv4 CIDR block as an additional CIDR to your VPC.
  For more information about managing HCX internet connectivity after environment creation, see [Configure HCX public internet connectivity](evs-env-hcx-internet-access.md "evs-env-hcx-internet-access.md").

**Create an IPAM**

Follow these steps to [Create an IPAM](../../../vpc/latest/ipam/create-ipam.md "../../../vpc/latest/ipam/create-ipam.md").

###### Note

You can use IPAM Free Tier to create IPAM resources for use with Amazon EVS.
While IPAM itself is free with Free Tier, you are responsible for the costs of other AWS services used in conjunction with IPAM such as NAT gateways and any public IPv4 addresses you use that are beyond the free tier limit.
For more information about IPAM pricing, see the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing "https://aws.amazon.com/vpc/pricing").

###### Note

Amazon EVS does not support private IPv6 Global Unicast Address (GUA) CIDRs at this time.

**Create a public IPv4 IPAM pool**

Follow these steps to create a public IPv4 pool.

IPAM console

1. Open the [IPAM console](https://console.aws.amazon.com/ipam "https://console.aws.amazon.com/ipam").
2. In the navigation pane, choose **Pools**.
3. Choose the public scope. For more information about scopes, see [How IPAM works](../../../vpc/latest/ipam/how-it-works-ipam.md "../../../vpc/latest/ipam/how-it-works-ipam.md").
4. Choose Create pool.
5. (Optional) Add a **Name** tag for the pool and a **Description** for the pool.
6. Under **Address family**, choose **IPv4**.
7. Under **Resource planning**, leave **Plan IP space within the scope** selected.
8. Under **Locale**, choose the locale for the pool.
   The locale is the AWS Region where you want this IPAM pool to be available for allocations.
   The locale you choose must match the AWS Region that your VPC is deployed into.
9. Under **Service**, choose **EC2 (EIP/VPC)**.
   This will advertise CIDRs allocated from this pool for the Amazon EC2 service (for Elastic IP addresses).
10. Under **Public IP source**, choose **Amazon-owned**.
11. Under **CIDRs to provision**, choose **Add Amazon-owned public CIDR**.
12. Under **Netmask**, choose a CIDR netmask length.
    /28 is the required minimum netmask length.
13. Choose **Create pool**.

AWS CLI

1. Open a terminal session.
2. Get the public scope ID from your IPAM.

```
SCOPE_ID=$(aws ec2 describe-ipam-scopes \
  --filters Name=ipam-scope-type,Values=public \
  --query 'IpamScopes[0].IpamScopeId' \
  --output text)
```

3. Create an IPAM pool in the public scope.

```
aws ec2 create-ipam-pool \
  --ipam-scope-id $SCOPE_ID \
  --address-family ipv4 \
  --no-auto-import \
  --locale us-east-2 \
  --description "Public IPv4 pool for HCX" \
  --tag-specifications 'ResourceType=ipam-pool,Tags=[{Key=Name,Value=evs-hcx-public-pool}]' \
  --public-ip-source amazon \
  --aws-service ec2
```

4. Store the pool ID for use in subsequent commands.

```
POOL_ID=$(aws ec2 describe-ipam-pools \
  --filters Name=tag:Name,Values=evs-hcx-public-pool \
  --query 'IpamPools[0].IpamPoolId' \
  --output text)
```

5. Provision a CIDR block from the pool with a minimum netmask length of /28.

```
aws ec2 provision-ipam-pool-cidr \
  --ipam-pool-id $POOL_ID \
  --netmask-length 28
```

**Allocate Elastic IP addresses from the IPAM pool**

Follow these steps to allocate Elastic IP addresses (EIPs) from the IPAM pool for HCX Service Mesh appliances.

Amazon VPC console

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").
2. In the navigation pane, choose **Elastic IPs**.
3. Choose **Allocate Elastic IP address**.
4. Select **Allocate using an IPv4 IPAM pool**.
5. Select the Amazon-owned public IPv4 pool that you previously configured.
6. Under **Allocate IPAM method**, choose **Manually input address within the IPAM pool**.

###### Important

You cannot associate the first two EIPs or the last EIP from the public IPAM CIDR block to the VLAN subnet.
These EIPs are reserved as network, default gateway, and broadcast addresses.
Amazon EVS throws a validation error if you attempt to associate these EIPs with the VLAN subnet.

###### Important

Manually input addresses within the IPAM pool to ensure that the EIPs that Amazon EVS reserves are not allocated.
If you allow IPAM to choose the EIP, IPAM may allocate a EIP that Amazon EVS reserves, causing failure during EIP association to the VLAN subnet. 7. Specify the EIP to allocate from the IPAM pool. 8. Choose **Allocate**. 9. Repeat this process to allocate the remaining EIPs that you require.
You are required to allocate at least two EIPs from the IPAM pool for the HCX Manager and HCX Interconnect (HCX-IX) appliances.
Allocate an additional EIP for each HCX network appliance that you need to deploy.

AWS CLI

1. Open a terminal session.
2. Get the IPAM pool ID that you created earlier.

```
POOL_ID=$(aws ec2 describe-ipam-pools \
  --filters Name=tag:Name,Values=evs-hcx-public-pool \
  --query 'IpamPools[0].IpamPoolId' \
  --output text)
```

3. Allocate Elastic IP addresses from the IPAM pool.
   You are required to allocate at least two EIPs from the IPAM pool for the HCX Manager and HCX Interconnect (HCX-IX) appliances.
   Allocate an additional EIP for each HCX network appliance that you need to deploy.

###### Important

You cannot associate the first two EIPs or the last EIP from the public IPAM CIDR block with a VLAN subnet.
These EIPs are reserved as network, default gateway, and broadcast addresses.
Amazon EVS throws a validation error if you attempt to associate these EIPs with the VLAN subnet.

###### Important

Manually input addresses within the IPAM pool to ensure that the EIPs that Amazon EVS reserves are not allocated.
If you allow IPAM to choose the EIP, IPAM may allocate a EIP that Amazon EVS reserves, causing failure during EIP association to the VLAN subnet.

```
aws ec2 allocate-address \
  --domain vpc \
  --tag-specifications 'ResourceType=elastic-ip,Tags=[{Key=Name,Value=evs-hcx-manager-eip}]' \
  --ipam-pool-id $POOL_ID \
  --address xx.xx.xxx.3

aws ec2 allocate-address \
  --domain vpc \
  --tag-specifications 'ResourceType=elastic-ip,Tags=[{Key=Name,Value=evs-hcx-ix-eip}]' \
  --ipam-pool-id $POOL_ID \
  --address xx.xx.xxx.4

aws ec2 allocate-address \
  --domain vpc \
  --tag-specifications 'ResourceType=elastic-ip,Tags=[{Key=Name,Value=evs-hcx-ne-eip}]' \
  --ipam-pool-id $POOL_ID \
  --address xx.xx.xxx.5
```

**Add the public IPv4 CIDR block from the IPAM pool to the VPC for HCX internet connnectivity**

To enable HCX internet connectivity, you must add the public IPv4 CIDR block from the IPAM pool to your VPC as an additional CIDR.
Amazon EVS uses this CIDR block to connect VMware HCX to your network.
Follow these steps to add the CIDR block to your VPC.

###### Important

You must manually input the IPv4 CIDR block that you add to your VPC.
Amazon EVS does not support use of an IPAM-allocated CIDR block at this time.
Use of an IPAM-allocated CIDR block may result in EIP association failure.

Amazon VPC console

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").
2. In the navigation pane, choose **Your VPCs**.
3. Select the VPC that you previously created, and choose **Actions**, **Edit CIDRs**.
4. Choose **Add new IPV4 CIDR**.
5. Select **IPV4 CIDR manual input**.
6. Specify the CIDR block from the public IPAM pool that you previously created.

AWS CLI

1. Open a terminal session.
2. Get the IPAM pool ID and the provisioned CIDR block.

```
POOL_ID=$(aws ec2 describe-ipam-pools \
  --filters Name=tag:Name,Values=evs-hcx-public-pool \
  --query 'IpamPools[0].IpamPoolId' \
  --output text)

CIDR_BLOCK=$(aws ec2 get-ipam-pool-cidrs \
  --ipam-pool-id $POOL_ID \
  --query 'IpamPoolCidrs[0].Cidr' \
  --output text)
```

3. Add the CIDR block to your VPC.

```
aws ec2 associate-vpc-cidr-block \
  --vpc-id $VPC_ID \
  --cidr-block $CIDR_BLOCK
```

## Configure the VPC main route table

Amazon EVS VLAN subnets are implicitly associated to the VPC main route table.
To enable connectivity to dependent services such as DNS or on-premises systems for successful environment deployment, you must configure the main route table to allow traffic to these systems.
The main route table must include a route for the VPC’s CIDR.
Use of the main route table is only required for initial Amazon EVS environment deployment.
After environment deployment, you can configure your environment to use a custom route table.
For more information, see [Configure a custom route table for Amazon EVS subnets](evs-env-config-custom-rt.md "evs-env-config-custom-rt.md").

After environment deployment, you must explicitly associate each of the Amazon EVS VLAN subnets with a route table in your VPC.
NSX connectivity fails if your VLAN subnets are not explicitly associated with a VPC route table.
We strongly recommend that you explicitly associate your subnets with a custom route table after environment deployment.
For more information, see [Configure the VPC main route table](setting-up.md#vpc-main-rt "setting-up.md#vpc-main-rt").

###### Important

Amazon EVS supports the use of a custom route table only after the Amazon EVS environment is created.
Custom route tables should not be used during Amazon EVS environment creation, as this may result in connectivity issues.

## Configure DNS and NTP servers using the VPC DHCP option set

###### Important

Your environment deployment fails if you don’t meet these Amazon EVS requirements:

- Include a primary DNS server IP address and a secondary DNS server IP address in the DHCP option set.
- Include a DNS forward lookup zone with A records for each VCF management appliance and Amazon EVS host in your deployment.
- Include a DNS reverse lookup zone with PTR records for each VCF management appliance and Amazon EVS host in your deployment.
- Configure the VPC’s main route table to ensure a route to your DNS servers exist.
- Ensure that your domain name registration is valid and unexpired, and no duplicate hostnames or IP addresses exist.
- Configure your security groups and network access control lists (ACLs) to allow Amazon EVS to communicate with:
  - DNS servers over TCP/UDP port 53.
  - Host management VLAN subnet over HTTPS and SSH.
  - Management VLAN subnet over HTTPS and SSH.

Amazon EVS uses your VPC’s DHCP option set to retrieve the following:

- Domain Name System (DNS) servers for host IP address resolution.
- Domain names for DNS resolution.
- Network Time Protocol (NTP) servers for time synchronization.

You can create a DHCP option set using the Amazon VPC console or AWS CLI.
For more information, see [Create a DHCP option set](../../../vpc/latest/userguide/DHCPOptionSet.md#CreatingaDHCPOptionSet "../../../vpc/latest/userguide/DHCPOptionSet.md#CreatingaDHCPOptionSet") in the _Amazon VPC User Guide_.

### Configure DNS servers

DNS configuration enables hostname resolution in your Amazon EVS environment.
To successfully deploy an Amazon EVS environment, your VPC’s DHCP option set must have the following DNS settings:

- A primary DNS server IP address and a secondary DNS server IP address in the DHCP option set.
- A DNS forward lookup zone with A records for each VCF management appliance and Amazon EVS host in your deployment.
- A reverse lookup zone with PTR records for each VCF management appliance and Amazon EVS host in your deployment.
  For NTP configuration, you can use the the default Amazon NTP address `169.254.169.123`, or another IPv4 address that you prefer.

For more information about configuring DNS servers in a DHCP option set, see [Create a DHCP option set](../../../vpc/latest/userguide/DHCPOptionSet.md#CreatingaDHCPOptionSet "../../../vpc/latest/userguide/DHCPOptionSet.md#CreatingaDHCPOptionSet").

#### Configure DNS for on-premisis connectivity

For on-premises connectivity, we recommend the use of Route 53 private hosted zones with inbound resolvers.
This setup enables hybrid DNS resolution, where you can use Route 53 for internal DNS within your VPC and integrate it with your existing on-premises DNS infrastructure.
This allows resources within your VPC to resolve domain names hosted on your on-premises network, and vice versa, without requiring complex configurations.
If required, you can also use your own DNS server with Route 53 outbound resolvers.
For steps to configure, see [Creating a private hosted zone](../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md "../../../Route53/latest/DeveloperGuide/hosted-zone-private-creating.md") and [Forwarding inbound DNS queries to your VPC](../../../Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.md "../../../Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.md") in the _Amazon Route 53 Developer Guide_.

###### Note

Using both Route 53 and a custom Domain Name System (DNS) server in the DHCP option set may cause unexpected behavior.

###### Note

If you use custom DNS domain names defined in a private hosted zone in Route 53, or use private DNS with interface VPC endpoints (AWS PrivateLink), you must set both the `enableDnsHostnames` and `enableDnsSupport` attributes to `true`.
For more information, see [DNS attributes for your VPC](../../../vpc/latest/userguide/AmazonDNS-concepts.md#vpc-dns-support "../../../vpc/latest/userguide/AmazonDNS-concepts.md#vpc-dns-support").

#### Troubleshoot DNS reachability issues

Amazon EVS requires a persistent connection to SDDC Manager and DNS servers in your VPC’s DHCP option set to reach DNS records.
If the persistent connection to SDDC Manager becomes unavailable, Amazon EVS will no longer be able to validate environment status, and you may lose environment access.
For steps to troubleshoot this issue, see [Reachability check failed](troubleshooting.md#troubleshoot-reachability "troubleshooting.md#troubleshoot-reachability").

### Configure NTP servers

NTP servers provide the time to your network.
A consistent and accurate time reference on your Amazon EC2 instance is crucial for many VCF environment tasks and processes.
Time synchronization is essential for:

- System logging and auditing
- Security operations
- Distributed system management
- Troubleshooting

You can enter the IPv4 addresses of up to four NTP servers in your VPC’s DHCP option set.
You can specify the Amazon Time Sync Service at IPv4 address `169.254.169.123`.
By default, the Amazon EC2 instances that Amazon EVS deploys use the Amazon Time Sync Service at IPv4 address `169.254.169.123`.

For more information about NTP servers, see [RFC 2123](https://datatracker.ietf.org/doc/html/rfc2132#section-8.3 "https://datatracker.ietf.org/doc/html/rfc2132#section-8.3").
For more information about Amazon Time Sync Service, see [Precision clock and time synchronization in your EC2 instance](../../../AWSEC2/latest/UserGuide/set-time.md "../../../AWSEC2/latest/UserGuide/set-time.md") and [Configure NTP on VMware Cloud Foundation Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/configure-ntp-on-vmware-cloud-foundation-hosts.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/configure-ntp-on-vmware-cloud-foundation-hosts.html") in the VMware Cloud Foundation documentation.

**To configure NTP settings**

1. Choose your NTP source:
   - Amazon Time Sync Service (recommended)
   - Custom NTP servers

2. Add NTP servers to your DHCP options set.
   For more information, see [Create a DHCP option set](../../../vpc/latest/userguide/DHCPOptionSet.md#CreatingaDHCPOptionSet "../../../vpc/latest/userguide/DHCPOptionSet.md#CreatingaDHCPOptionSet") in the _Amazon VPC User Guide._
3. Verify time synchronization.
   For more information about DHCP option set configuration, see [Configure your VPC’s DHCP option set](setting-up.md#vpc-dhcp "setting-up.md#vpc-dhcp").

You can configure connectivity for your on-premises data center to your AWS infrastructure using Direct Connect with an associated transit gateway, or using an AWS Site-to-Site VPN attachment to a transit gateway.

To enable connectivity to on-premises systems for successful environment deployment, you must configure the VPC’s main route table to allow traffic to these systems.
For more information, see [Configure the VPC main route table](setting-up.md#vpc-main-rt "setting-up.md#vpc-main-rt").

After the Amazon EVS environment is created, you must update the transit gateway route tables with the VPC CIDRs created within the Amazon EVS environment.
For more information, see [Configure transit gateway route tables and Direct Connect prefixes for on-premises connectivity (optional)](#getting-started-config-tgw-assoc "#getting-started-config-tgw-assoc").

For more information about setting up an Direct Connect connection, see [Direct Connect gateways and transit gateway associations](../../../directconnect/latest/UserGuide/direct-connect-transit-gateways.md "../../../directconnect/latest/UserGuide/direct-connect-transit-gateways.md").
For more information about using AWS Site-to-Site VPN with AWS Transit Gateway, see [AWS Site-to-Site VPN attachments in Amazon VPC Transit Gateways](../../../vpc/latest/tgw/tgw-vpn-attachments.md "../../../vpc/latest/tgw/tgw-vpn-attachments.md") in the _Amazon VPC Transit Gateway User Guide_.

###### Note

Amazon EVS does not support connectivity via an AWS Direct Connect private virtual interface (VIF), or via an AWS Site-to-Site VPN connection that terminates directly into the underlay VPC.

## Set up a VPC Route Server instance with endpoints and peers

Amazon EVS uses Amazon VPC Route Server to to enable BGP-based dynamic routing to your VPC underlay network.
You must specify a route server that shares routes to at least two route server endpoints in the service access subnet.
The peer ASN configured on the route server peers must match, and the peer IP addresses must be unique.

If you are configuring Route Server for HCX internet connectivity, you must configure Route Server propagations for both the service access subnet and public subnet that you created in the [first step of this procedure](#getting-started-create-vpc "#getting-started-create-vpc").

###### Important

Your environment deployment fails if you don’t meet these Amazon EVS requirements for VPC Route Server configuration:

- You must configure at least two route server endpoints in the service access subnet.
- When configuring Border Gateway Protocol (BGP) for the Tier-0 gateway, the VPC Route Server peer ASN value must match the NSX Edge peer ASN value.
- When creating the two route server peers, you must use a unique IP address from the NSX uplink VLAN for each endpoint.
  These two IP addresses will be assigned to the NSX edges during Amazon EVS environment deployment.
- When enabling Route Server propagation, you must ensure that all route tables being propagated have at least one explicit subnet association.
  BGP route advertisement fails if propagated route tables do not have an explicit subnet association.

For more information about setting up VPC Route Server, see the [Route Server get started tutorial](../../../vpc/latest/userguide/route-server-tutorial.md "../../../vpc/latest/userguide/route-server-tutorial.md").

###### Important

When enabling Route Server propagation, ensure that all route tables being propagated have at least one explicit subnet association.
BGP route advertisement fails if the route table does have an explicit subnet association.

###### Note

For Route Server peer liveness detection, Amazon EVS only support the default BGP keepalive mechanism.
Amazon EVS does not support multi-hop Bidirectional Forwarding Detection (BFD).

###### Note

We recommend that you enable persistent routes for the route server instance with a persist duration between 1-5 minutes.
If enabled, routes will be preserved in the route server’s routing database even if all BGP sessions end.
For more information, see [Create a route server](../../../vpc/latest/userguide/route-server-tutorial-create.md "../../../vpc/latest/userguide/route-server-tutorial-create.md") in the _Amazon VPC User Guide_.

###### Note

If you are using a NAT gateway or a transit gateway, ensure that your route server is configured correctly to propagate NSX routes to the VPC route table(s).

### Troubleshooting

If you encounter issues:

- Verify that each route table has an explicit subnet association.
- Check that the peer ASN values entered for route server and the NSX Tier-0 gateway match.
- Confirm that Route Server endpoint IP addresses are unique.
- Review route propagation status in your route tables.
- Use VPC Route Server peer logging to monitor BGP session health and troubleshoot connection issues.
  For more information, see [Route server peer logging](../../../vpc/latest/userguide/route-server-peer-logging.md "../../../vpc/latest/userguide/route-server-peer-logging.md") in the _Amazon VPC User Guide_.

## Create a network ACL to control Amazon EVS VLAN subnet traffic

Amazon EVS uses a network access control list (ACL) to control traffic to and from Amazon EVS VLAN subnets.
You can use the default network ACL for your VPC, or you can create a custom network ACL for your VPC with rules that are similar to the rules for your security groups to add a layer of security to your VPC.
For more information, see [Create a network ACL for your VPC](../../../vpc/latest/userguide/create-network-acl.md "../../../vpc/latest/userguide/create-network-acl.md") in the _Amazon VPC User Guide_.

If you plan to configure HCX internet connectivity, ensure that the network ACL rules that you configure allow the necessary inbound and outbound connections for HCX components.
For more information about HCX port requirements, see the [VMware HCX User Guide](https://techdocs.broadcom.com/us/en/vmware-cis/hcx.html "https://techdocs.broadcom.com/us/en/vmware-cis/hcx.html").

###### Important

If you are connecting over the internet, associating an Elastic IP address with a VLAN provides direct internet access to all resources on that VLAN subnet.
Ensure that you have appropriate network access control lists configured to restrict access as needed for your security requirements.

###### Important

EC2 security groups do not function on elastic network interfaces that are attached to Amazon EVS VLAN subnets.
To control traffic to and from Amazon EVS VLAN subnets, you must use a network access control list.

## Create an Amazon EVS environment

###### Important

To get started as simply and quickly as possible, this topic includes steps to create an Amazon EVS environment with default settings.
Before creating an environment, we recommend that you familiarize yourself with all settings and deploy an environment with the settings that meet your requirements.
Environments can only be configured during initial environment creation.
Environments cannot be modified after you’ve created them.
For an overview of all possible Amazon EVS environment settings, see the [Amazon EVS API Reference Guide](../APIReference/Welcome.md "../APIReference/Welcome.md").

###### Note

You environment ID will be available to Amazon EVS across all AWS Regions for VCF license compliance needs.

###### Note

Amazon EVS environments must be deployed into the same Region and Availability Zone as the VPC and VPC subnets.

Complete this step to create an Amazon EVS environment with hosts and VLAN subnets.

###### Example

Amazon EVS console

1. Go to the Amazon EVS console.

###### Note

Ensure that the AWS Region shown in the upper right of your console is the AWS Region that you want to create your environment in.
If it’s not, choose the dropdown next to the AWS Region name and choose the AWS Region that you want to use. 2. In the navigation pane, choose **Environments**. 3. Choose **Create environment**. 4. On the **Validate Amazon EVS requirements** page, check that service requirements have been met.
For more information, see [Setting up Amazon Elastic VMware Service](setting-up.md "setting-up.md").

    1. (Optional) For **Name**, enter an environment name.
    2. For **Environment version**, choose your VCF version. For information about VCF versions provided by Amazon EVS, see [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md "versions-provided.md").
    3. For **Site ID**, enter your Broadcom Site ID.
    4. For **VCF Solution key**, enter a VCF solution key (VMware vSphere 8 Enterprise Plus for VCF).
    This license key cannot be in use by an existing environment.


    ###### Note

    The VCF solution key must have at least 256 cores.


    ###### Note

    Your VCF license will be available to Amazon EVS across all AWS Regions for license compliance.
    Amazon EVS does not validate license keys.
    To validate license keys, visit [Broadcom support](https://support.broadcom.com/web/ecx "https://support.broadcom.com/web/ecx").


    ###### Note

    Amazon EVS requires that you maintain a valid VCF solution key in SDDC Manager for the service to function properly.
    If you manage the VCF solution key using the vSphere Client post-deployment, you must ensure that the keys also appears in the licensing screen of the SDDC Manager user interface.
    5. For **vSAN license key**, enter a vSAN license key.
    This license key cannot be in use by an existing environment.


    ###### Note

    The vSAN license key must have at least 110 TiB of vSAN capacity.


    ###### Note

    Your VCF license will be available to Amazon EVS across all AWS Regions for license compliance.
    Amazon EVS does not validate license keys.
    To validate license keys, visit [Broadcom support](https://support.broadcom.com/web/ecx "https://support.broadcom.com/web/ecx").


    ###### Note

    Amazon EVS requires that you maintain a valid vSAN license key in SDDC Manager forchooose chose the service to function properly.
    If you manage the vSAN license key using the vSphere Client post-deployment, you must ensure that the keys also appears in the licensing screen of the SDDC Manager user interface.
    6. For **VCF license terms**, check the box to confirm that you have purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment.
    Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance.
    7. Choose **Next**.

5.  On the **Specify host details** page, complete the following steps four times to add four hosts to the environment.
    Amazon EVS environments require four hosts for initial deployment.

        1. Choose **Add host details**.
        2. For **DNS hostname**, enter the host name for the host.
        3. For **instance type**, choose the EC2 instance type.
        4. For **ESX host version**, during environment creation a default ESX version for the chosen VCF version will be used. See [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md "versions-provided.md") for more information.


        ###### Important

        Do not stop or terminate EC2 instances that Amazon EVS deploys.
        This action results in data loss.


        ###### Note

        Amazon EVS only supports i4i.metal EC2 instances at this time.
        5. For **SSH key pair**, choose an SSH key pair for SSH access into the host.
        6. Choose **Add host**.

6.  On the **Configure networks and connectivity** page, do the following.
    1. For **HCX connectivity requirements**, select whether you want to use HCX with private connectivity or over the internet.
    2. For **VPC**, choose the VPC that you previously created.
    3. (For HCX internet connectivy only) For **HCX network ACL**, choose which network ACL your HCX VLAN will be associated with.

    ###### Important

    We strongly recommend that you create a custom network ACL dedicated to the HCX VLAN.
    For more information, see [Configure a network access control list to control Amazon EVS VLAN subnet traffic](evs-env-nacl-cong.md "evs-env-nacl-cong.md"). 4. For **Service access subnet**, choose the private subnet that was created when you created the VPC. 5. For **Security group -_optional_**, you can choose up to two security groups that control communication between the Amazon EVS control plane and VPC.
    Amazon EVS uses the default security group if no security group is chosen.

    ###### Note

    Ensure that the security groups that you choose provide connectivity to your DNS servers and Amazon EVS VLAN subnets. 6. Under **Management connectivity**, enter the CIDR blocks to be used for the Amazon EVS VLAN subnets.
    For **HCX uplink VLAN CIDR block**, if configuring a public HCX VLAN, you must specify a CIDR block with a netmask length of exactly /28.
    Amazon EVS throws a validation error if any other CIDR block size is specified for the public HCX VLAN.
    For a private HCX VLAN and all other VLANs CIDR blocks, the minimum netmask length that you can use is /28 and the maximum is /24.

    ###### Important

    Amazon EVS VLAN subnets can only be created during Amazon EVS environment creation, and cannot be modified after the environment is created.
    You must ensure that the VLAN subnet CIDR blocks are properly sized before creating the environment.
    You will not be able to add VLAN subnets after the environment is deployed.
    For more information, see [Amazon EVS networking considerations](architecture.md#evs-subnets "architecture.md#evs-subnets"). 7. Under **Expansion VLANs**, enter the CIDR blocks for additional Amazon EVS VLAN subnets that can be used to expand VCF capabilities within Amazon EVS, such as enabling NSX Federation. 8. Under **Workload/VCF connectivity**, enter the CIDR block for the NSX uplink VLAN, and choose two VPC Route Server peer IDs that peer to Route Server endpoints over the NSX uplink.

    ###### Note

    Amazon EVS requires a VPC Route Server instance that is associated with two Route Server endpoints and two Route Server peers prior to EVS deployment.
    This configuration enables dynamic BGP-based routing over the NSX uplink.
    For more information, see [Set up a VPC Route Server instance with endpoints and peers](#getting-started-create-rs-resources "#getting-started-create-rs-resources"). 9. Choose **Next**.

7.  On the **Specify Management DNS hostnames** page, do the following.
    1. Under **Management appliance DNS hostnames**, enter the DNS hostnames for the virtual machines to host VCF management appliances. If using Route 53 as your DNS provider, also choose the hosted zone that contains your DNS records.
    2. Under **Credentials**, choose whether you’d like to use the AWS managed KMS key for Secrets Manager or a customer managed KMS key that you provide.
       This key is used to encrypt the VCF credentials that are required to use SDDC Manager, NSX Manager, and vCenter appliances.

    ###### Note

    There are usage costs associated with customer managed KMS keys.
    For more information, see the [AWS KMS pricing page](https://aws.amazon.com/kms/pricing "https://aws.amazon.com/kms/pricing"). 3. Choose **Next**.

8.  (Optional) On the **Add tags** page, add any tags that you would like to be assigned to this environment and choose **Next**.

###### Note

Hosts created as part of this environment will receive the following tag: `DoNotDelete-EVS-<environmentid>-<hostname>`.

###### Note

Tags that are associated with the Amazon EVS environment do not propagate to underlying AWS resources such as EC2 instances. You can create tags on underlying AWS resources using the respective service console or the AWS CLI. 9. On the **Review and create** page, review your configuration and choose **Create environment**.

###### Important

During environment deployment, Amazon EVS creates the EVS VLAN subnets and implicitly associates them with the main route table.
After the deployment completes, you must explicitly associate the Amazon EVS VLAN subnets with a route table for NSX connectivity purposes.
For more information, see [Explicitly associate Amazon EVS VLAN subnets to a VPC route table](#getting-started-associate-vlans "#getting-started-associate-vlans").

###### Note

Amazon EVS deploys a recent bundled version of VMware Cloud Foundation which may not include individual product updates, known as async patches.
Upon completion of this deployment, we strongly recommend that you review and update individual products using Broadcom’s Async Patch Tool (AP Tool) or SDDC Manager in-product LCM automation.
NSX upgrades must be done outside of SDDC Manager.

###### Note

Environment creation can take several hours.

AWS CLI

1. Open a terminal session.
2. Create an Amazon EVS environment.
   Below is a sample `aws evs create-environment` request.

###### Important

Before running the `aws evs create-environment` command, check that all Amazon EVS prerequisites have been met.
Environment deployment fails if prerequisites have not been met.
For more information, see [Setting up Amazon Elastic VMware Service](setting-up.md "setting-up.md").

###### Important

During environment deployment, Amazon EVS creates the EVS VLAN subnets and implicitly associates them with the main route table.
After the deployment completes, you must explicitly associate the Amazon EVS VLAN subnets with a route table for NSX connectivity purposes.
For more information, see [Explicitly associate Amazon EVS VLAN subnets to a VPC route table](#getting-started-associate-vlans "#getting-started-associate-vlans").

###### Note

Amazon EVS deploys a recent bundled version of VMware Cloud Foundation which may not include individual product updates, known as async patches.
Upon completion of this deployment, we strongly recommend you review and update individual products using Broadcom’s Async Patch Tool (AP Tool) or SDDC Manager in-product LCM automation.
NSX upgrades must be done outside of SDDC Manager.

###### Note

Environment deployment can take several hours.

    * For `--vpc-id`, specify the VPC that you previously created with a minimum IPv4 CIDR range of /22.
    * For `--service-access-subnet-id`, specify the unique ID of the private subnet that was created when you created the VPC.
    * For `--vcf-version`, See [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md "versions-provided.md") for VCF versions provided by Amazon EVS,
    * With `--terms-accepted`, you confirm that you have purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment.
    Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance.
    * For `--license-info`, enter your VCF solution key (VMware vSphere 8 Enterprise Plus for VCF) and vSAN license key.


    ###### Note

    The VCF solution key must have at least 256 cores.
    The vSAN license key must have at least 110 TiB of vSAN capacity.


    ###### Note

    Amazon EVS requires that you maintain a valid VCF solution key and vSAN license key in SDDC Manager for the service to function properly.
    If you manage these license keys using the vSphere Client post-deployment, you must ensure that they also appear in the licensing screen of the SDDC Manager user interface.


    ###### Note

    The VCF solution key and vSAN license key cannot be in use by an existing Amazon EVS environment.
    * For `--initial-vlans` specify the CIDR ranges for the Amazon EVS VLAN subnets that Amazon EVS creates on your behalf.
    These VLANs are used to deploy VCF management appliances.
    If configuring a public HCX VLAN, you must specify a CIDR block with a netmask length of exactly /28.
    Amazon EVS throws a validation error if any other CIDR block size is specified for the public HCX VLAN.
    For a private HCX VLAN and all other VLANs CIDR blocks, the minimum netmask length that you can use is /28 and the maximum is /24.
    * `hcxNetworkAclId` is used if configuring HCX internet connectivity.
    Specify a custom network ACL for the public HCX VLAN.


    ###### Important

    We strongly recommend that you create a custom network ACL dedicated to the HCX VLAN.
    For more information, see [Configure a network access control list to control Amazon EVS VLAN subnet traffic](evs-env-nacl-cong.md "evs-env-nacl-cong.md").


    ###### Important

    Amazon EVS VLAN subnets can only be created during Amazon EVS environment creation, and cannot be modified after the environment is created.
    You must ensure that the VLAN subnet CIDR blocks are properly sized before creating the environment.
    You will not be able to add VLAN subnets after the environment is deployed.
    For more information, see [Amazon EVS networking considerations](architecture.md#evs-subnets "architecture.md#evs-subnets").
    * For `--hosts`, specify host details for the hosts that Amazon EVS requires for environment deployment.
    Include DNS hostname, EC2 SSH key name, and EC2 instance type for each host.
    The dedicated host ID is optional.


    ###### Important

    Do not stop or terminate EC2 instances that Amazon EVS deploys.
    This action results in data loss.


    ###### Note

    Amazon EVS only supports i4i.metal EC2 instances at this time.
    * For `--connectivity-info`, specify the 2 VPC Route Server peer IDs that you created in the previous step.


    ###### Note

    Amazon EVS requires a VPC Route Server instance that is associated with two Route Server endpoints and two Route Server peers prior to EVS deployment.
    This configuration enables dynamic BGP-based routing over the NSX uplink.
    For more information, see [Set up a VPC Route Server instance with endpoints and peers](#getting-started-create-rs-resources "#getting-started-create-rs-resources").
    * For `--vcf-hostnames`, enter the DNS hostnames for the virtual machines to host VCF management appliances.
    * For `--site-id`, enter your unique Broadcom site ID.
    This ID allows access to the Broadcom portal, and is provided to you by Broadcom at the close of your software contract or contract renewal.
    * (Optional) For `--region`, enter the Region that your environment will be deployed into.
    If the Region isn’t specified, your default Region is used.



    ```
    aws evs create-environment \
    --environment-name testEnv \
    --vpc-id vpc-1234567890abcdef0 \
    --service-access-subnet-id subnet-01234a1b2cde1234f \
    --vcf-version VCF-5.2.2 \
    --terms-accepted \
    --license-info "{
          \"solutionKey\": \"00000-00000-00000-abcde-11111\",
          \"vsanKey\": \"00000-00000-00000-abcde-22222\"
        }" \
       --initial-vlans "{
          \"isHcxPublic\": true,
          \"hcxNetworkAclId\": \"nacl-abcd1234\",
          \"vmkManagement\": {
            \"cidr\": \"10.10.0.0/24\"
          },
          \"vmManagement\": {
            \"cidr\": \"10.10.1.0/24\"
          },
          \"vMotion\": {
            \"cidr\": \"10.10.2.0/24\"
          },
          \"vSan\": {
            \"cidr\": \"10.10.3.0/24\"
          },
          \"vTep\": {
            \"cidr\": \"10.10.4.0/24\"
          },
          \"edgeVTep\": {
            \"cidr\": \"10.10.5.0/24\"
          },
          \"nsxUplink\": {
            \"cidr\": \"10.10.6.0/24\"
          },
          \"hcx\": {
            \"cidr\": \"10.10.7.0/24\"
          },
          \"expansionVlan1\": {
            \"cidr\": \"10.10.8.0/24\"
          },
          \"expansionVlan2\": {
              \"cidr\": \"10.10.9.0/24\"
          }
        }" \
    --hosts "[
        {
          \"hostName\": \"esx01\",
          \"keyName\": \"sshKey-04-05-45\”,
          \"instanceType\": \"i4i.metal\",
          \"dedicatedHostId\": \"h-07879acf49EXAMPLE\"
        },
        {
          \"hostName\": \"esx02\",
          \"keyName\": \"sshKey-04-05-45\",
          \"instanceType\": \"i4i.metal\",
          \"dedicatedHostId\": \"h-07878bde50EXAMPLE\"
        },
        {
          \"hostName\": \"esx03\",
          \"keyName\": \"sshKey-04-05-45\",
          \"instanceType\": \"i4i.metal\",
          \"dedicatedHostId\": \"h-07877eio51EXAMPLE\"
        },
        {
          \"hostName\": \"esx04\",
          \"keyName\": \"sshKey-04-05-45\",
          \"instanceType\": \"i4i.metal\",
          \"dedicatedHostId\": \"h-07863ghi52EXAMPLE\"
        }
      ]" \
    --connectivity-info "{
        \"privateRouteServerPeerings\": [\"rsp-1234567890abcdef0\",\"rsp-abcdef01234567890\"]
      }" \
      --vcf-hostnames "{
        \"vCenter\": \"vcf-vc01\",
        \"nsx\": \"vcf-nsx\",
        \"nsxManager1\": \"vcf-nsxm01\",
        \"nsxManager2\": \"vcf-nsxm02\",
        \"nsxManager3\": \"vcf-nsxm03\",
        \"nsxEdge1\": \"vcf-edge01\",
        \"nsxEdge2\": \"vcf-edge02\",
        \"sddcManager\": \"vcf-sddcm01\",
        \"cloudBuilder\": \"vcf-cb01\"
      }" \
    --site-id my-site-id \
    --region us-east-2
    ```

    The following is a sample response.



    ```
    {
        "environment": {
            "environmentId": "env-abcde12345",
            "environmentState": "CREATING",
            "stateDetails": "The environment is being initialized, this operation may take some time to complete.",
            "createdAt": "2025-04-13T12:03:39.718000+00:00",
            "modifiedAt": "2025-04-13T12:03:39.718000+00:00",
            "environmentArn": "arn:aws:evs:us-east-2:111122223333:environment/env-abcde12345",
            "environmentName": "testEnv",
            "vpcId": "vpc-1234567890abcdef0",
            "serviceAccessSubnetId": "subnet-01234a1b2cde1234f",
            "vcfVersion": "VCF-5.2.2",
            "termsAccepted": true,
            "licenseInfo": [
                {
                    "solutionKey": "00000-00000-00000-abcde-11111",
                    "vsanKey": "00000-00000-00000-abcde-22222"
                }
            ],
            "siteId": "my-site-id",
            "connectivityInfo": {
                "privateRouteServerPeerings": [
                    "rsp-1234567890abcdef0",
                    "rsp-abcdef01234567890"
                ]
            },
            "vcfHostnames": {
                "vCenter": "vcf-vc01",
                "nsx": "vcf-nsx",
                "nsxManager1": "vcf-nsxm01",
                "nsxManager2": "vcf-nsxm02",
                "nsxManager3": "vcf-nsxm03",
                "nsxEdge1": "vcf-edge01",
                "nsxEdge2": "vcf-edge02",
                "sddcManager": "vcf-sddcm01",
                "cloudBuilder": "vcf-cb01"
            }
        }
    }
    ```

## Verify Amazon EVS environment creation

###### Example

Amazon EVS console

1. Go to the Amazon EVS console.
2. In the navigation pane, choose **Environments**.
3. Select the environment.
4. Select the **Details** tab.
5. Check that the **Environment status** is **Passed** and the **Environment state** is **Created**.
   This lets you know that the environment is ready to use.

###### Note

Environment creation can take several hours.
If the **Environment state** still shows **Creating**, refresh the page.

AWS CLI

1. Open a terminal session.
2. Run the following command, using the environment ID for your environment and the Region name that contains your resources.
   The environment is ready to use when the `environmentState` is `CREATED`.

###### Note

Environment creation can take several hours.
If the `environmentState` still shows `CREATING`, run the command again to refresh the output.

```
aws evs get-environment  --environment-id env-abcde12345
```

The following is a sample response.

```
{
    "environment": {
        "environmentId": "env-abcde12345",
        "environmentState": "CREATED",
        "createdAt": "2025-04-13T13:39:49.546000+00:00",
        "modifiedAt": "2025-04-13T13:40:39.355000+00:00",
        "environmentArn": "arn:aws:evs:us-east-2:111122223333:environment/env-abcde12345",
        "environmentName": "testEnv",
        "vpcId": "vpc-0c6def5b7b61c9f41",
        "serviceAccessSubnetId": "subnet-06a3c3b74d36b7d5e",
        "vcfVersion": "VCF-5.2.2",
        "termsAccepted": true,
        "licenseInfo": [
            {
                "solutionKey": "00000-00000-00000-abcde-11111",
                "vsanKey": "00000-00000-00000-abcde-22222"
            }
        ],
        "siteId": "my-site-id",
        "checks": [],
        "connectivityInfo": {
            "privateRouteServerPeerings": [
                "rsp-056b2b1727a51e956",
                "rsp-07f636c5150f171c3"
            ]
        },
        "vcfHostnames": {
            "vCenter": "vcf-vc01",
            "nsx": "vcf-nsx",
            "nsxManager1": "vcf-nsxm01",
            "nsxManager2": "vcf-nsxm02",
            "nsxManager3": "vcf-nsxm03",
            "nsxEdge1": "vcf-edge01",
            "nsxEdge2": "vcf-edge02",
            "sddcManager": "vcf-sddcm01",
            "cloudBuilder": "vcf-cb01"
        },
        "credentials": []
    }
}
```

## Explicitly associate Amazon EVS VLAN subnets to a VPC route table

Explicitly associate each of the Amazon EVS VLAN subnets with a route table in your VPC.
This route table is used to allow AWS resources to communicate with virtual machines on NSX network segments, running with Amazon EVS.
If you’ve created a public HCX VLAN, be sure to explicitly associate the public HCX VLAN subnet with a public route table in your VPC that routes to an internet gateway.

###### Example

Amazon VPC console

1. Go to the [VPC console](https://console.aws.amazon.com/vpc "https://console.aws.amazon.com/vpc").
2. In the navigation pane, choose **Route tables**.
3. Choose the route table that you want to associate with Amazon EVS VLAN subnets.
4. Select the **Subnet associations** tab.
5. Under **Explicit subnet associations**, select **Edit subnet associations**.
6. Select all of the Amazon EVS VLAN subnets.
7. Choose **Save associations**.

AWS CLI

1. Open a terminal session.
2. Identify the Amazon EVS VLAN subnet IDs.

```
aws ec2 describe-subnets
```

3. Associate your Amazon EVS VLAN subnets with a route table in your VPC.

```
aws ec2 associate-route-table \
--route-table-id rtb-0123456789abcdef0 \
--subnet-id subnet-01234a1b2cde1234f
```

Follow these steps to associate Elastic IP address (EIPs) from the IPAM pool to the HCX public VLAN for HCX internet connectivity.
You are required to associate at least two EIPs for the HCX Manager and HCX Interconnect (HCX-IX) appliances.
Associate an additional EIP for each HCX network appliance that you need to deploy.
You can have up to 13 EIPs from the IPAM pool associated with the HCX public VLAN.

###### Important

HCX public internet connectivity fails if you do not associate at least two EIPs from the IPAM pool with an HCX public VLAN subnet.

###### Note

Amazon EVS only supports associating EIPs with the HCX VLAN at this time.

###### Note

You cannot associate the first two EIPs or the last EIP from the public IPAM CIDR block with the VLAN subnet.
These EIPs are reserved as network, default gateway, and broadcast addresses.
Amazon EVS throws a validation error if you attempt to associate these EIPs with the VLAN subnet.

Amazon EVS console

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs "https://console.aws.amazon.com/evs").
2. On the navigation menu, choose **Environments**.
3. Select the environment.
4. Under the **Networks and connectivity** tab, select the HCX public VLAN.
5. Choose **Associate EIP to VLAN**.
6. Select the Elastic IP address(es) to associate with the HCX public VLAN.
7. Choose **Associate EIPs**.
8. Check the **EIP associations** to confirm that the EIPs have been associated with the HCX public VLAN.

AWS CLI

1.  To associate an Elastic IP address with a VLAN, use the example `associate-eip-to-vlan` command.
    - `environment-id` - The ID of your Amazon EVS environment.
    - `vlan-name` - The name of the VLAN to associate with the Elastic IP address.
    - `allocation-id` - The allocation ID of the Elastic IP address.

    ```
    aws evs associate-eip-to-vlan \
      --environment-id "env-605uove256" \
      --vlan-name "hcx" \
      --allocation-id "eipalloc-0429268f30c4a34f7"
    ```

    The command returns details about the VLAN, including the new EIP association:

    ```
    {
        "vlan": {
            "vlanId": 80,
            "cidr": "18.97.137.0/28",
            "availabilityZone": "us-east-2c",
            "functionName": "hcx",
            "subnetId": "subnet-02f9a4ee9e1208cfc",
            "createdAt": "2025-08-22T23:42:16.200000+00:00",
            "modifiedAt": "2025-08-23T13:42:28.155000+00:00",
            "vlanState": "CREATED",
            "stateDetails": "VLAN successfully created",
            "eipAssociations": [
                {
                    "associationId": "eipassoc-09e966faad7ecc58a",
                    "allocationId": "eipalloc-0429268f30c4a34f7",
                    "ipAddress": "18.97.137.2"
                }
            ],
            "isPublic": true,
            "networkAclId": "acl-02fa8ab4ad3ddfb00"
        }
    }
    ```

    The `eipAssociations` array shows the new association, including:

        + `associationId` - The unique ID for this EIP association, used for disassociation.
        + `allocationId` - The allocation ID of the associated Elastic IP address.
        + `ipAddress` - The IP address assigned to the VLAN.

2.  Repeat the step to associate additional EIPs.

If you are configuring on-premises network connectivity using Direct Connect or AWS Site-to-Site VPN with a transit gateway, you must update the transit gateway route tables with the VPC CIDRs created within the Amazon EVS environment.
For more information, see [Transit gateway route tables in Amazon VPC Transit Gateways](../../../vpc/latest/tgw/tgw-route-tables.md "../../../vpc/latest/tgw/tgw-route-tables.md").

If you are using AWS Direct Connect, you may need to also update your Direct Connect prefixes to send and receive updated routes from the VPC.
For more information, see [Allows prefixes interactions for AWS Direct Connect gateways](../../../directconnect/latest/UserGuide/allowed-to-prefixes.md "../../../directconnect/latest/UserGuide/allowed-to-prefixes.md").

## Retrieve VCF credentials and access VCF management appliances

Amazon EVS uses AWS Secrets Manager to create, encrypt, and store managed secrets in your account.
These secrets contain the VCF credentials needed to install and access VCF management appliances such as vCenter Server, NSX, and SDDC Manager, as well as the ESX root password.
For more information about retrieving secrets, see [Get secrets from AWS Secrets Manager](../../../secretsmanager/latest/userguide/retrieving-secrets.md "../../../secretsmanager/latest/userguide/retrieving-secrets.md") in the _AWS Secrets Manager User Guide_.

###### Note

Amazon EVS does not provide managed rotation of your secrets.
We recommend that you rotate your secrets regularly on a set rotation window to ensure that secrets are not long-lived.

After you have retrieved your VCF credentials from AWS Secrets Manager, you can use them to log into your VCF management appliances.
For more information, see [Log in to the SDDC Manager User Interface](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/getting-started-with-sddc-manager-admin/log-in-to-the-sddc-manager-dashboard-admin.html "https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/getting-started-with-sddc-manager-admin/log-in-to-the-sddc-manager-dashboard-admin.html") and [How to Use and Configure Your vSphere Client](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/using-the-vsphere-client-host-management/working-with-the-vsphere-client-host-management.html#GUID-CE128B59-E236-45FF-9976-D134DADC8178-en "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/using-the-vsphere-client-host-management/working-with-the-vsphere-client-host-management.html#GUID-CE128B59-E236-45FF-9976-D134DADC8178-en") in the VMware product documentation.

By default, Amazon EVS enables the ESX Shell on newly deployed Amazon EVS hosts.
This configuration allows access to the Amazon EC2 instance’s serial port through the EC2 serial console, which you can use to troubleshoot boot, network configuration, and other issues.
The serial console does not require your instance to have any networking capabilities.
With the serial console, you can enter commands to a running EC2 instance as if your keyboard and monitor are directly attached to the instance’s serial port.

The EC2 serial console can be accessed using the EC2 console or the AWS CLI.
For more information, see [EC2 Serial Console for instances](../../../AWSEC2/latest/UserGuide/ec2-serial-console.md "../../../AWSEC2/latest/UserGuide/ec2-serial-console.md") in the _Amazon EC2 User Guide_.

###### Note

The EC2 serial console is the only Amazon EVS supported mechanism to access the Direct Console User Interface (DCUI) to interact with an ESX host locally.

###### Note

Amazon EVS disables remote SSH by default.
For more information about enabling SSH to access the remote ESX Shell, see [Remote ESX Shell Access with SSH](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/getting-started-with-esxcli-8-0/running-host-management-commands-in-the-esxi-shell/remote-esxi-shell-access-with-ssh.html "https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/getting-started-with-esxcli-8-0/running-host-management-commands-in-the-esxi-shell/remote-esxi-shell-access-with-ssh.html") in the VMware vSphere product documentation.

**Connect to the EC2 Serial Console**

To connect to the EC2 serial console and use your chosen tool for troubleshooting, certain prerequisite tasks must be completed.
For more information, see [Prerequisites for the EC2 Serial Console](../../../AWSEC2/latest/UserGuide/ec2-serial-console-prerequisites.md "../../../AWSEC2/latest/UserGuide/ec2-serial-console-prerequisites.md") and [Connect to the EC2 Serial Console](../../../AWSEC2/latest/UserGuide/connect-to-serial-console.md "../../../AWSEC2/latest/UserGuide/connect-to-serial-console.md") in the _Amazon EC2 User Guide_.

###### Note

To connect to the EC2 serial console, your EC2 instance state must be `running`.
You can’t connect to the serial console if the instance is in the `pending`, `stopping`, `stopped`, `shutting-down`, or `terminated` state.
For more information about instance state changes, see [Amazon EC2 instance state change](../../../AWSEC2/latest/UserGuide/ec2-instance-lifecycle.md "../../../AWSEC2/latest/UserGuide/ec2-instance-lifecycle.md") in the _Amazon EC2 User Guide_.

**Configure access to the EC2 Serial Console**

To configure access to the EC2 serial console, you or your administrator must grant serial console access at the account level and then configure IAM policies to grant access to your users.
For Linux instances, you must also configure a password-based user on every instance so that your users can use the serial console for troubleshooting.
For more information, see [Configure access to the EC2 Serial Console](../../../AWSEC2/latest/UserGuide/configure-access-to-serial-console.md "../../../AWSEC2/latest/UserGuide/configure-access-to-serial-console.md") in the _Amazon EC2 User Guide_.

## Clean up

Follow these steps to delete the AWS resources that were created.

### Delete the Amazon EVS hosts and environment

Follow these steps to delete the Amazon EVS hosts and environment.
This action deletes the VMware VCF installation that runs in your Amazon EVS environment.

###### Note

To delete an Amazon EVS environment, you must first delete all hosts within the environment.
An environment cannot be deleted if there are hosts associated with the environment.

###### Example

Amazon EVS console

1. Go to the Amazon EVS console.
2. In the navigation pane, choose **Environment**.
3. Select the environment that contains the hosts to delete.
4. Select the **Hosts** tab.
5. Select the host and choose **Delete** within the **Hosts** tab.
   Repeat this step for each host in the environment.
6. At the top of the **Environments** page, choose **Delete** and then **Delete environment**.

###### Note

Environment deletion also deletes the Amazon EVS VLAN subnets and AWS Secrets Manager secrets that Amazon EVS created.
AWS resources that you create are not deleted.
These resources may continue to incur costs. 7. If you have Amazon EC2 Capacity Reservations in place that you no longer require, ensure that you’ve canceled them.
For more information, see [Cancel a Capacity Reservation](../../../AWSEC2/latest/UserGuide/capacity-reservations-release.md "../../../AWSEC2/latest/UserGuide/capacity-reservations-release.md") in the _Amazon EC2 User Guide_.

AWS CLI

1. Open a terminal session.
2. Identify the environment that contains the host to delete.

```
aws evs list-environments
```

The following is a sample response.

```
{
    "environmentSummaries": [
        {
            "environmentId": "env-abcde12345",
            "environmentName": "testEnv",
            "vcfVersion": "VCF-5.2.2",
            "environmentState": "CREATED",
            "createdAt": "2025-04-13T14:42:41.430000+00:00",
            "modifiedAt": "2025-04-13T14:43:33.412000+00:00",
            "environmentArn": "arn:aws:evs:us-east-2:111122223333:environment/env-abcde12345"
        },
        {
            "environmentId": "env-edcba54321",
            "environmentName": "testEnv2",
            "vcfVersion": "VCF-5.2.2",
            "environmentState": "CREATED",
            "createdAt": "2025-04-13T13:39:49.546000+00:00",
            "modifiedAt": "2025-04-13T13:52:13.342000+00:00",
            "environmentArn": "arn:aws:evs:us-east-2:111122223333:environment/env-edcba54321"
        }
    ]
}
```

3. Delete the hosts from the environment.
   Below is a sample `aws evs delete-environment-host` request.

###### Note

To be able to delete an environment, you must first delete all of the hosts that are contained in the environment.

```
aws evs delete-environment-host \
--environment-id env-abcde12345 \
--host esx01
```

4. Repeat the previous steps to delete the remaining hosts in your environment.
5. Delete the environment.

```
aws evs delete-environment --environment-id env-abcde12345
```

###### Note

Environment deletion also deletes the Amazon EVS VLAN subnets and AWS Secrets Manager secrets that Amazon EVS created.
Other AWS resources that you create are not deleted.
These resources may continue to incur costs. 6. If you have Amazon EC2 Capacity Reservations in place that you no longer require, ensure that you’ve canceled them.
For more information, see [Cancel a Capacity Reservation](../../../AWSEC2/latest/UserGuide/capacity-reservations-release.md "../../../AWSEC2/latest/UserGuide/capacity-reservations-release.md") in the _Amazon EC2 User Guide_.

If you’ve configured HCX internet connectivity, follow these steps to delete your IPAM resources.

1. Release EIP allocations from the public IPAM pool.
   For more information, see [Release an allocation](../../../vpc/latest/ipam/release-alloc-ipam.md "../../../vpc/latest/ipam/release-alloc-ipam.md") in the _VPC IP Address Manager User Guide_.
2. Deprovision the public IPv4 CIDR from the IPAM pool.
   For more information, see [Deprovision CIDRs from a pool](../../../vpc/latest/ipam/depro-pool-cidr-ipam.md "../../../vpc/latest/ipam/depro-pool-cidr-ipam.md") in the _VPC IP Address Manager User Guide_.
3. Delete the public IPAM pool.
   For more information, see [Delete a pool](../../../vpc/latest/ipam/delete-pool-ipam.md "../../../vpc/latest/ipam/delete-pool-ipam.md") in the _VPC IP Address Manager User Guide_.
4. Delete the IPAM.
   For more information, see [Delete an IPAM](../../../vpc/latest/ipam/delete-ipam.md "../../../vpc/latest/ipam/delete-ipam.md") in the _VPC IP Address Manager User Guide_.

### Delete the VPC Route Server components

For steps to delete the Amazon VPC Route Server components that you created, see [Route Server cleanup](../../../vpc/latest/userguide/route-server-tutorial-cleanup.md "../../../vpc/latest/userguide/route-server-tutorial-cleanup.md") in the _Amazon VPC User Guide_.

### Delete the network access control list (ACL)

For steps to delete a network access control list, see [Delete a network ACL for your VPC](../../../vpc/latest/userguide/delete-network-acl.md "../../../vpc/latest/userguide/delete-network-acl.md") in the _Amazon VPC User Guide_.

### Disassociate and delete subnet route tables

For steps to disassociate and delete subnet route tables, see [Subnet route tables](../../../vpc/latest/userguide/subnet-route-tables.md "../../../vpc/latest/userguide/subnet-route-tables.md") in the _Amazon VPC User Guide_.

### Delete subnets

Delete the VPC subnets, including the service access subnet.
For steps to delete VPC subnets, see [Delete a subnet](../../../vpc/latest/userguide/subnet-deleting.md "../../../vpc/latest/userguide/subnet-deleting.md") in the _Amazon VPC User Guide_.

###### Note

If you’re using Route 53 for DNS, remove the inbound endpoints before you attempt to delete the service access subnet.
Otherwise, you will not be able to delete the service access subnet.

###### Note

Amazon EVS deletes the VLAN subnets on your behalf when the environment is deleted.
Amazon EVS VLAN subnets can only be deleted when the environment is deleted.

### Delete the VPC

For steps to delete the VPC, see [Delete your VPC](../../../vpc/latest/userguide/delete-vpc.md "../../../vpc/latest/userguide/delete-vpc.md") in the _Amazon VPC User Guide_.

## Next steps

Migrate your workloads to Amazon EVS using VMware Hybrid Cloud Extension (VMware HCX).
For more information, see [Migrate workloads to Amazon EVS using VMware HCX](migrate-evs-hcx.md "migrate-evs-hcx.md").
