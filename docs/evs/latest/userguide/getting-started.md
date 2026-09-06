

# Getting started with Amazon Elastic VMware Service
<a name="getting-started"></a>

Use this guide to get started with Amazon Elastic VMware Service (Amazon EVS). You’ll learn how to create an Amazon EVS environment with hosts within your own Amazon Virtual Private Cloud (VPC).

After you’re finished, you’ll have an Amazon EVS environment that you can use to migrate your VMware vSphere-based workloads to the AWS Cloud.

Amazon EVS can deploy VCF 5.2.x for you, or you can use **Self-deployed** mode to install VCF yourself. For the VCF versions that Amazon EVS supports, see [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md).

For Self-deployed mode, see [Creating an Amazon EVS environment with Self-deployed mode](#getting-started-self-deployed). The procedures under [Create an Amazon EVS environment](#getting-started-create-env) cover environment creation where Amazon EVS deploys VCF for you.

**Important**  
To get started as simply and quickly as possible, this topic includes steps to create a VPC, and specifies minimum requirements for DNS server configuration and Amazon EVS environment creation. Before creating these resources, we recommend that you plan out your IP address space and DNS record setup that meets your requirements. You should also familiarize yourself with VCF 5.2.x requirements. See the [VCF 5.2.x release notes](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/vcf-release-notes.html) for relevant release information.

**Important**  
For information about VCF versions provided by Amazon EVS, see [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md).

**Topics**
+ [Prerequisites](#getting-started-prerequisites)
+ [Create a VPC with subnets and route tables](#getting-started-create-vpc)
+ [Choose your HCX connectivity option](#hcx-connectivity-choice)
+ [Configure the VPC main route table](#getting-started-vpc-main-route-table-config)
+ [Configure DNS and NTP servers using the VPC DHCP option set](#getting-started-config-dns-ntp-dhcp)
+ [Set up a VPC Route Server instance with endpoints and peers](#getting-started-create-rs-resources)
+ [Create a network ACL to control Amazon EVS VLAN subnet traffic](#getting-started-create-nacl-vlan-traffic)
+ [Creating an Amazon EVS environment with Self-deployed mode](#getting-started-self-deployed)
+ [Create an Amazon EVS environment](#getting-started-create-env)
+ [Verify Amazon EVS environment creation](#verify-env-creation)
+ [Explicitly associate Amazon EVS VLAN subnets to a VPC route table](#getting-started-associate-vlans)
+ [Retrieve VCF credentials and access VCF management appliances](#access-vcf)
+ [Clean up](#cleanup)
+ [Next steps](#getting-started-next-steps)

## Prerequisites
<a name="getting-started-prerequisites"></a>

Before getting started, you must complete the Amazon EVS prerequisite tasks. For more information, see [Setting up Amazon Elastic VMware Service](setting-up.md).

## Create a VPC with subnets and route tables
<a name="getting-started-create-vpc"></a>

**Note**  
The VPC, subnets, and Amazon EVS environment must all be created in the same account. Amazon EVS does not support cross-account sharing of VPC subnets or Amazon EVS environments.

**Example**  

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc).

1. On the VPC dashboard, choose **Create VPC**.

1. For **Resources to create**, choose **VPC and more**.

1. Keep **Name tag auto-generation** selected to create Name tags for the VPC resources, or clear it to provide your own Name tags for the VPC resources.

1. For **IPv4 CIDR block**, enter an IPv4 CIDR block. A VPC must have an IPv4 CIDR block. Ensure that you create a VPC that is adequately sized to accommodate the Amazon EVS subnets. For more information, see [Amazon EVS networking considerations](architecture.md#evs-subnets).
**Note**  
Amazon EVS does not support IPv6 at this time.

1. Keep **Tenancy** as `Default`. With this option selected, EC2 instances that are launched into this VPC will use the tenancy attribute specified when the instances are launched. Amazon EVS launches bare metal EC2 instances on your behalf.

1. For **Number of Availability Zones (AZs)**, choose **1**.
**Note**  
Amazon EVS only supports Single-AZ deployments at this time.

1. Expand **Customize AZs** and choose the AZ for your subnets.
**Note**  
You must deploy in an AWS Region where Amazon EVS is supported. For more information about Amazon EVS Region availability, see [Amazon Elastic VMware Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/evs.html) in the * AWS General Reference Guide*.

1. (Optional) If you need internet connectivity, for **Number of public subnets**, choose **1**.

1. For **Number of private subnets**, choose **1**. This private subnet will be used as the service access subnet that you provided to Amazon EVS during the environment creation step. For more information, see [Service access subnet](concepts.md#concepts-service-access-subnet).

1. To choose the IP address ranges for your subnets, expand **Customize subnets CIDR blocks**.
**Note**  
Amazon EVS VLAN subnets will also need to be created from this VPC CIDR space. Ensure that you leave enough space in the VPC CIDR block for the VLAN subnets that the service requires. For more information, see [Amazon EVS networking considerations](architecture.md#evs-subnets) 

1. (Optional) To grant internet access over IPv4 to resources, for **NAT gateways**, choose **In 1 AZ**. Note that there is a cost associated with NAT gateways. For more information, see [Pricing for NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-pricing.html).
**Note**  
Amazon EVS requires the use of a NAT gateway to enable outbound internet connectivity.

1. For **VPC endpoints**, choose **None**.
**Note**  
Amazon EVS does not support gateway VPC endpoints for Amazon S3 at this time. To enable Amazon S3 connectivity, you must set up an interface VPC endpoint using AWS PrivateLink for Amazon S3. For more information, see [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) in the *Amazon Simple Storage Service User Guide*.

1. For **DNS options**, keep the defaults selected. Amazon EVS requires your VPC to have DNS resolution capability for all VCF components.

1. (Optional) To add a tag to your VPC, expand **Additional tags**, choose **Add new tag**, and enter a tag key and a tag value.

1. Choose **Create VPC**.
**Note**  
During VPC creation, Amazon VPC automatically creates a main route table and implicitly associates subnets to it by default.

1. Open a terminal session.

1. Create a VPC with a private subnet and optional public subnet in a single Availability Zone.

   ```
   aws ec2 create-vpc \
     --cidr-block 10.0.0.0/16 \
     --instance-tenancy default \
     --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=evs-vpc}]'
   ```

1. Store the VPC ID for use in subsequent commands.

   ```
   VPC_ID=$(aws ec2 describe-vpcs \
     --filters Name=tag:Name,Values=evs-vpc \
     --query 'Vpcs[0].VpcId' \
     --output text)
   ```

1. Enable DNS hostnames and DNS support.

   ```
   aws ec2 modify-vpc-attribute \
     --vpc-id $VPC_ID \
     --enable-dns-hostnames
   aws ec2 modify-vpc-attribute \
     --vpc-id $VPC_ID \
     --enable-dns-support
   ```

1. Create a private subnet in the VPC.

   ```
   aws ec2 create-subnet \
     --vpc-id $VPC_ID \
     --cidr-block 10.0.1.0/24 \
     --availability-zone us-west-2a \
     --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=evs-private-subnet}]'
   ```

1. Store the private subnet ID for use in subsequent commands.

   ```
   PRIVATE_SUBNET_ID=$(aws ec2 describe-subnets \
     --filters Name=tag:Name,Values=evs-private-subnet \
     --query 'Subnets[0].SubnetId' \
     --output text)
   ```

1. (Optional) Create a public subnet if internet connectivity is needed.

   ```
   aws ec2 create-subnet \
     --vpc-id $VPC_ID \
     --cidr-block 10.0.0.0/24 \
     --availability-zone us-west-2a \
     --tag-specifications 'ResourceType=subnet,Tags=[{Key=Name,Value=evs-public-subnet}]'
   ```

1. (Optional) Store the public subnet ID for use in subsequent commands.

   ```
   PUBLIC_SUBNET_ID=$(aws ec2 describe-subnets \
     --filters Name=tag:Name,Values=evs-public-subnet \
     --query 'Subnets[0].SubnetId' \
     --output text)
   ```

1. (Optional) Create and attach an internet gateway if the public subnet is created.

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

1. (Optional) Create a NAT gateway if internet connectivity is needed.

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
   
   NAT_GW_ID=$(aws ec2 describe-nat-gateways \
     --filter Name=tag:Name,Values=evs-nat \
     --query 'NatGateways[0].NatGatewayId' \
     --output text)
   ```
**Note**  
The NAT gateway must be in the `available` state before you create a route that references it. To check, run `aws ec2 describe-nat-gateways --nat-gateway-ids $NAT_GW_ID --query 'NatGateways[0].State'`.

1. Create and configure the necessary route tables.

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

1. Add the necessary routes to the route tables.

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

1. Associate the route tables with your subnets.

   ```
   aws ec2 associate-route-table \
     --route-table-id $PRIVATE_RT_ID \
     --subnet-id $PRIVATE_SUBNET_ID
   
   aws ec2 associate-route-table \
     --route-table-id $PUBLIC_RT_ID \
     --subnet-id $PUBLIC_SUBNET_ID
   ```
**Note**  
During VPC creation, Amazon VPC automatically creates a main route table and implicitly associates subnets to it by default.

## Choose your HCX connectivity option
<a name="hcx-connectivity-choice"></a>

Select one connectivity option for your Amazon EVS environment:
+  **Private connectivity**: Provides high-performance network pathways for HCX, optimizing reliability and consistency. Requires use of AWS Direct Connect or Site-to-Site VPN for external network connectivity.
+  **Internet connectivity**: Uses the public internet to establish a flexible migration path that is quick to set up. Requires use of VPC IP Address Manager (IPAM) and Elastic IP addresses.

For detailed analysis, see [HCX connectivity options](migrate-evs-hcx.md#migrate-evs-hcx-connectivity).

 **Choose your option:** 
+  **Option A: Private connectivity only** → Continue to [Configure the VPC main route table](#getting-started-vpc-main-route-table-config).
+  **Option B: Internet connectivity** → Continue to [HCX internet connectivity setup](#hcx-internet-config).

### HCX internet connectivity setup
<a name="hcx-internet-config"></a>

**Note**  
Skip this section if you chose HCX private connectivity and continue to [Configure the VPC main route table](#getting-started-vpc-main-route-table-config).

To enable HCX internet connectivity for Amazon EVS, you must:
+ Ensure that your VPC IP Address Manager (IPAM) quota for Amazon-provided contiguous public IPv4 CIDR block netmask length is /28 or greater.
**Important**  
Use of any Amazon-provided contiguous public IPv4 CIDR block with a netmask length smaller than /28 will result in HCX connectivity issues. For more information about increasing IPAM quotas, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html).
+ Create an IPAM and a public IPv4 IPAM pool with a CIDR that has a a minimum netmask length of /28.
+ Allocate at least two Elastic IP addresses (EIPs) from the IPAM pool for the HCX Manager and HCX Interconnect (HCX-IX) appliances. Allocate an additional Elastic IP address for each HCX network appliance that you need to deploy.
+ Add the public IPv4 CIDR block as an additional CIDR to your VPC.

For more information about managing HCX internet connectivity after environment creation, see [Configure HCX public internet connectivity](evs-env-hcx-internet-access.md).

 **Create an IPAM** 

Follow these steps to [Create an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/create-ipam.html).

**Note**  
You can use IPAM Free Tier to create IPAM resources for use with Amazon EVS. While IPAM itself is free with Free Tier, you are responsible for the costs of other AWS services used in conjunction with IPAM such as NAT gateways and any public IPv4 addresses you use that are beyond the free tier limit. For more information about IPAM pricing, see the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing).

**Note**  
Amazon EVS does not support private IPv6 Global Unicast Address (GUA) CIDRs at this time.

 **Create a public IPv4 IPAM pool** 

Follow these steps to create a public IPv4 pool.

------
#### [ IPAM console ]

1. Open the [IPAM console](https://console.aws.amazon.com/ipam).

1. In the navigation pane, choose **Pools**.

1. Choose the public scope. For more information about scopes, see [How IPAM works](https://docs.aws.amazon.com/vpc/latest/ipam/how-it-works-ipam.html).

1. Choose Create pool.

1. (Optional) Add a **Name** tag for the pool and a **Description** for the pool.

1. Under **Address family**, choose **IPv4**.

1. Under **Resource planning**, leave **Plan IP space within the scope** selected.

1. Under **Locale**, choose the locale for the pool. The locale is the AWS Region where you want this IPAM pool to be available for allocations. The locale you choose must match the AWS Region that your VPC is deployed into.

1. Under **Service**, choose **EC2 (EIP/VPC)**. This will advertise CIDRs allocated from this pool for the Amazon EC2 service (for Elastic IP addresses).

1. Under **Public IP source**, choose **Amazon-owned**.

1. Under **CIDRs to provision**, choose **Add Amazon-owned public CIDR**.

1. Under **Netmask**, choose a CIDR netmask length. /28 is the required minimum netmask length.

1. Choose **Create pool**.

------
#### [  AWS CLI  ]

1. Open a terminal session.

1. Get the public scope ID from your IPAM.

   ```
   SCOPE_ID=$(aws ec2 describe-ipam-scopes \
     --filters Name=ipam-scope-type,Values=public \
     --query 'IpamScopes[0].IpamScopeId' \
     --output text)
   ```

1. Create an IPAM pool in the public scope.

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

1. Store the pool ID for use in subsequent commands.

   ```
   POOL_ID=$(aws ec2 describe-ipam-pools \
     --filters Name=tag:Name,Values=evs-hcx-public-pool \
     --query 'IpamPools[0].IpamPoolId' \
     --output text)
   ```

1. Provision a CIDR block from the pool with a minimum netmask length of /28.

   ```
   aws ec2 provision-ipam-pool-cidr \
     --ipam-pool-id $POOL_ID \
     --netmask-length 28
   ```

------

 **Allocate Elastic IP addresses from the IPAM pool** 

Follow these steps to allocate Elastic IP addresses (EIPs) from the IPAM pool for HCX Service Mesh appliances.

------
#### [  Amazon VPC console ]

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc).

1. In the navigation pane, choose **Elastic IPs**.

1. Choose **Allocate Elastic IP address**.

1. Select **Allocate using an IPv4 IPAM pool**.

1. Select the Amazon-owned public IPv4 pool that you previously configured.

1. Under **Allocate IPAM method**, choose **Manually input address within the IPAM pool**.
**Important**  
You cannot associate the first two EIPs or the last EIP from the public IPAM CIDR block to the VLAN subnet. These EIPs are reserved as network, default gateway, and broadcast addresses. Amazon EVS throws a validation error if you attempt to associate these EIPs with the VLAN subnet.
**Important**  
Manually input addresses within the IPAM pool to ensure that the EIPs that Amazon EVS reserves are not allocated. If you allow IPAM to choose the EIP, IPAM may allocate a EIP that Amazon EVS reserves, causing failure during EIP association to the VLAN subnet.

1. Specify the EIP to allocate from the IPAM pool.

1. Choose **Allocate**.

1. Repeat this process to allocate the remaining EIPs that you require. You are required to allocate at least two EIPs from the IPAM pool for the HCX Manager and HCX Interconnect (HCX-IX) appliances. Allocate an additional EIP for each HCX network appliance that you need to deploy.

------
#### [  AWS CLI  ]

1. Open a terminal session.

1. Get the IPAM pool ID that you created earlier.

   ```
   POOL_ID=$(aws ec2 describe-ipam-pools \
     --filters Name=tag:Name,Values=evs-hcx-public-pool \
     --query 'IpamPools[0].IpamPoolId' \
     --output text)
   ```

1. Allocate Elastic IP addresses from the IPAM pool. You are required to allocate at least two EIPs from the IPAM pool for the HCX Manager and HCX Interconnect (HCX-IX) appliances. Allocate an additional EIP for each HCX network appliance that you need to deploy.
**Important**  
You cannot associate the first two EIPs or the last EIP from the public IPAM CIDR block with a VLAN subnet. These EIPs are reserved as network, default gateway, and broadcast addresses. Amazon EVS throws a validation error if you attempt to associate these EIPs with the VLAN subnet.
**Important**  
Manually input addresses within the IPAM pool to ensure that the EIPs that Amazon EVS reserves are not allocated. If you allow IPAM to choose the EIP, IPAM may allocate a EIP that Amazon EVS reserves, causing failure during EIP association to the VLAN subnet.

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

------

 **Add the public IPv4 CIDR block from the IPAM pool to the VPC for HCX internet connnectivity** 

To enable HCX internet connectivity, you must add the public IPv4 CIDR block from the IPAM pool to your VPC as an additional CIDR. Amazon EVS uses this CIDR block to connect VMware HCX to your network. Follow these steps to add the CIDR block to your VPC.

**Important**  
You must manually input the IPv4 CIDR block that you add to your VPC. Amazon EVS does not support use of an IPAM-allocated CIDR block at this time. Use of an IPAM-allocated CIDR block may result in EIP association failure.

------
#### [  Amazon VPC console ]

1. Open the [Amazon VPC console](https://console.aws.amazon.com/vpc).

1. In the navigation pane, choose **Your VPCs**.

1. Select the VPC that you previously created, and choose **Actions**, **Edit CIDRs**.

1. Choose **Add new IPV4 CIDR**.

1. Select **IPV4 CIDR manual input**.

1. Specify the CIDR block from the public IPAM pool that you previously created.

------
#### [  AWS CLI  ]

1. Open a terminal session.

1. Get the IPAM pool ID and the provisioned CIDR block.

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

1. Add the CIDR block to your VPC.

   ```
   aws ec2 associate-vpc-cidr-block \
     --vpc-id $VPC_ID \
     --cidr-block $CIDR_BLOCK
   ```

------

## Configure the VPC main route table
<a name="getting-started-vpc-main-route-table-config"></a>

Amazon EVS VLAN subnets are implicitly associated to the VPC main route table. To enable connectivity to dependent services such as DNS or on-premises systems for successful environment deployment, you must configure the main route table to allow traffic to these systems. The main route table must include a route for the VPC’s CIDR. Use of the main route table is only required for initial Amazon EVS environment deployment. After environment deployment, you can configure your environment to use a custom route table. For more information, see [Configure a custom route table for Amazon EVS subnets](evs-env-config-custom-rt.md).

After environment deployment, you must explicitly associate each of the Amazon EVS VLAN subnets with a route table in your VPC. NSX connectivity fails if your VLAN subnets are not explicitly associated with a VPC route table. We strongly recommend that you explicitly associate your subnets with a custom route table after environment deployment. For more information, see [Configure the VPC main route table](setting-up.md#vpc-main-rt).

**Important**  
Amazon EVS supports the use of a custom route table only after the Amazon EVS environment is created. Custom route tables should not be used during Amazon EVS environment creation, as this may result in connectivity issues.

## Configure DNS and NTP servers using the VPC DHCP option set
<a name="getting-started-config-dns-ntp-dhcp"></a>

**Important**  
Your environment deployment fails if you don’t meet these Amazon EVS requirements:  
Include a primary DNS server IP address and a secondary DNS server IP address in the DHCP option set.
Include a DNS forward lookup zone with A records for each VCF management appliance and Amazon EVS host in your deployment.
Include a DNS reverse lookup zone with PTR records for each VCF management appliance and Amazon EVS host in your deployment.
Configure the VPC’s main route table to ensure a route to your DNS servers exist.
Ensure that your domain name registration is valid and unexpired, and no duplicate hostnames or IP addresses exist.
Configure your security groups and network access control lists (ACLs) to allow Amazon EVS to communicate with:  
DNS servers over TCP/UDP port 53.
Host management VLAN subnet over HTTPS and SSH.
Management VLAN subnet over HTTPS and SSH.

Amazon EVS uses your VPC’s DHCP option set to retrieve the following:
+ Domain Name System (DNS) servers for host IP address resolution.
+ Domain names for DNS resolution.
+ Network Time Protocol (NTP) servers for time synchronization.

You can create a DHCP option set using the Amazon VPC console or AWS CLI. For more information, see [Create a DHCP option set](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html#CreatingaDHCPOptionSet) in the * Amazon VPC User Guide*.

### Configure DNS servers
<a name="getting-started-config-dns"></a>

DNS configuration enables hostname resolution in your Amazon EVS environment. To successfully deploy an Amazon EVS environment, your VPC’s DHCP option set must have the following DNS settings:
+ A primary DNS server IP address and a secondary DNS server IP address in the DHCP option set. Both DNS server IPs must be reachable and responding to queries when the Amazon EVS connector launches. All required DNS records (forward A records and reverse PTR records) must be resolvable through those servers at that time.
+ A DNS forward lookup zone with A records for each VCF management appliance and Amazon EVS host in your deployment.
+ A reverse lookup zone with PTR records for each VCF management appliance and Amazon EVS host in your deployment. For NTP configuration, you can use the default Amazon NTP address `169.254.169.123`, or another IPv4 address that you prefer.

For more information about configuring DNS servers in a DHCP option set, see [Create a DHCP option set](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html#CreatingaDHCPOptionSet).

#### Configure DNS for on-premises connectivity
<a name="getting-started-config-dns-on-prem"></a>

For on-premises connectivity, we recommend the use of Route 53 private hosted zones with inbound resolvers. This setup enables hybrid DNS resolution, where you can use Route 53 for internal DNS within your VPC and integrate it with your existing on-premises DNS infrastructure. This allows resources within your VPC to resolve domain names hosted on your on-premises network, and vice versa, without requiring complex configurations. If required, you can also use your own DNS server with Route 53 outbound resolvers. For steps to configure, see [Creating a private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zone-private-creating.html) and [Forwarding inbound DNS queries to your VPC](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-forwarding-inbound-queries.html) in the *Amazon Route 53 Developer Guide*.

**Note**  
Using both Route 53 and a custom Domain Name System (DNS) server in the DHCP option set may cause unexpected behavior.

**Note**  
If you use custom DNS domain names defined in a private hosted zone in Route 53, or use private DNS with interface VPC endpoints (AWS PrivateLink), you must set both the `enableDnsHostnames` and `enableDnsSupport` attributes to `true`. For more information, see [DNS attributes for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/AmazonDNS-concepts.html#vpc-dns-support).

#### Troubleshoot DNS reachability issues
<a name="evs-env-dns-reachability"></a>

Amazon EVS requires a persistent connection to SDDC Manager and DNS servers in your VPC’s DHCP option set to reach DNS records. If the persistent connection to SDDC Manager becomes unavailable, Amazon EVS will no longer be able to validate environment status, and you may lose environment access. For steps to troubleshoot this issue, see [Reachability check failed](troubleshooting.md#troubleshoot-reachability).

### Configure NTP servers
<a name="getting-started-config-ntp"></a>

NTP servers provide the time to your network. A consistent and accurate time reference on your Amazon EC2 instance is crucial for many VCF environment tasks and processes. Time synchronization is essential for:
+ System logging and auditing
+ Security operations
+ Distributed system management
+ Troubleshooting

You can enter the IPv4 addresses of up to four NTP servers in your VPC’s DHCP option set. You can specify the Amazon Time Sync Service at IPv4 address `169.254.169.123`. By default, the Amazon EC2 instances that Amazon EVS deploys use the Amazon Time Sync Service at IPv4 address `169.254.169.123`.

For more information about NTP servers, see [RFC 2123](https://datatracker.ietf.org/doc/html/rfc2132#section-8.3). For more information about Amazon Time Sync Service, see [Precision clock and time synchronization in your EC2 instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html) and [Configure NTP on VMware Cloud Foundation Hosts](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/configure-ntp-on-vmware-cloud-foundation-hosts.html) in the VMware Cloud Foundation documentation.

 **To configure NTP settings** 

1. Choose your NTP source:
   + Amazon Time Sync Service (recommended)
   + Custom NTP servers

1. Add NTP servers to your DHCP options set. For more information, see [Create a DHCP option set](https://docs.aws.amazon.com/vpc/latest/userguide/DHCPOptionSet.html#CreatingaDHCPOptionSet) in the *Amazon VPC User Guide.* 

1. Verify time synchronization. For more information about DHCP option set configuration, see [Configure your VPC’s DHCP option set](setting-up.md#vpc-dhcp).

#### Configure on-premises network connectivity (optional)
<a name="getting-started-connect-on-prem"></a>

You can configure connectivity for your on-premises data center to your AWS infrastructure using Direct Connect with an associated transit gateway, or using an AWS Site-to-Site VPN attachment to a transit gateway.

To enable connectivity to on-premises systems for successful environment deployment, you must configure the VPC’s main route table to allow traffic to these systems. For more information, see [Configure the VPC main route table](setting-up.md#vpc-main-rt).

After the Amazon EVS environment is created, you must update the transit gateway route tables with the VPC CIDRs created within the Amazon EVS environment. For more information, see [Configure transit gateway route tables and Direct Connect prefixes for on-premises connectivity (optional)](#getting-started-config-tgw-assoc).

For more information about setting up an Direct Connect connection, see [Direct Connect gateways and transit gateway associations](https://docs.aws.amazon.com/directconnect/latest/UserGuide/direct-connect-transit-gateways.html). For more information about using AWS Site-to-Site VPN with AWS Transit Gateway, see [AWS Site-to-Site VPN attachments in Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html) in the * Amazon VPC Transit Gateway User Guide*.

**Note**  
Amazon EVS does not support connectivity via an AWS Direct Connect private virtual interface (VIF), or via an AWS Site-to-Site VPN connection that terminates directly into the underlay VPC.

## Set up a VPC Route Server instance with endpoints and peers
<a name="getting-started-create-rs-resources"></a>

Amazon EVS uses Amazon VPC Route Server to to enable BGP-based dynamic routing to your VPC underlay network. You must specify a route server that shares routes to at least two route server endpoints in the service access subnet. The peer ASN configured on the route server peers must match, and the peer IP addresses must be unique.

If you are configuring Route Server for HCX internet connectivity, you must configure Route Server propagations for both the service access subnet and public subnet that you created in the [first step of this procedure](#getting-started-create-vpc).

**Important**  
Your environment deployment fails if you don’t meet these Amazon EVS requirements for VPC Route Server configuration:  
You must configure at least two route server endpoints in the service access subnet.
When configuring Border Gateway Protocol (BGP) for the Tier-0 gateway, the VPC Route Server peer ASN value must match the NSX Edge peer ASN value.
When creating the two route server peers, you must use a unique IP address from the NSX uplink VLAN for each endpoint. These two IP addresses will be assigned to the NSX edges during Amazon EVS environment deployment.
When enabling Route Server propagation, you must ensure that all route tables being propagated have at least one explicit subnet association. BGP route advertisement fails if propagated route tables do not have an explicit subnet association.

**Note**  
The NSX uplink VLAN subnet does not exist yet when you create the route server peers — Amazon EVS creates it during environment creation. Choose the two peer IP addresses from the **planned** NSX uplink VLAN CIDR block (the value you will pass as `initialVlans.nsxUplink`). The two IP addresses must fall within that planned CIDR block and remain unused.

For more information about setting up VPC Route Server, see the [Route Server get started tutorial](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial.html).

When you follow that tutorial, use the following Amazon EVS-specific values:
+  **Amazon-side ASN** — the BGP ASN of the VPC Route Server. Use any private ASN (for example, `65022`). The NSX Edge Tier-0 gateway uses this value as its BGP neighbor (remote) ASN in [Step 5: Configure NSX networking](#self-deployed-nsx-edge), so note the value you choose.
+  **Route server endpoints** — create two endpoints, both in the service access subnet.
+  **Route server peers** — We recommend that you create four route server peers and configure a full mesh, so that each of the two NSX Edge nodes peers with both route server endpoints. A full mesh keeps routes propagating if a route server endpoint goes into maintenance. At minimum, you must create two peers. Use a unique IP address from your planned NSX uplink VLAN CIDR for each peer, and set the peer ASN to the NSX Edge Tier-0 ASN that you configure in [Step 5: Configure NSX networking](#self-deployed-nsx-edge) (for example, `65000`).
+  **Propagation** — enable route server propagation on the route table associated with your service access subnet. That route table must have at least one explicit subnet association.

**Important**  
When enabling Route Server propagation, ensure that all route tables being propagated have at least one explicit subnet association. BGP route advertisement fails if the route table does not have an explicit subnet association.

**Note**  
For Route Server peer liveness detection, Amazon EVS only support the default BGP keepalive mechanism. Amazon EVS does not support multi-hop Bidirectional Forwarding Detection (BFD).

**Note**  
We recommend that you enable persistent routes for the route server instance with a persist duration between 1-5 minutes. If enabled, routes will be preserved in the route server’s routing database even if all BGP sessions end. For more information, see [Create a route server](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial-create.html) in the * Amazon VPC User Guide*.

**Note**  
If you are using a NAT gateway or a transit gateway, ensure that your route server is configured correctly to propagate NSX routes to the VPC route table(s).

### Troubleshooting
<a name="evs-env-rs-troubleshoot"></a>

If you encounter issues:
+ Verify that each route table has an explicit subnet association.
+ Check that the peer ASN values entered for route server and the NSX Tier-0 gateway match.
+ Confirm that Route Server endpoint IP addresses are unique.
+ Review route propagation status in your route tables.
+ Use VPC Route Server peer logging to monitor BGP session health and troubleshoot connection issues. For more information, see [Route server peer logging](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-peer-logging.html) in the *Amazon VPC User Guide*.

## Create a network ACL to control Amazon EVS VLAN subnet traffic
<a name="getting-started-create-nacl-vlan-traffic"></a>

Amazon EVS uses a network access control list (ACL) to control traffic to and from Amazon EVS VLAN subnets. You can use the default network ACL for your VPC, or you can create a custom network ACL for your VPC with rules that are similar to the rules for your security groups to add a layer of security to your VPC. For more information, see [Create a network ACL for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/create-network-acl.html) in the *Amazon VPC User Guide*.

If you plan to configure HCX internet connectivity, ensure that the network ACL rules that you configure allow the necessary inbound and outbound connections for HCX components. For more information about HCX port requirements, see the [VMware HCX User Guide](https://techdocs.broadcom.com/us/en/vmware-cis/hcx.html).

**Important**  
If you are connecting over the internet, associating an Elastic IP address with a VLAN provides direct internet access to all resources on that VLAN subnet. Ensure that you have appropriate network access control lists configured to restrict access as needed for your security requirements.

**Important**  
EC2 security groups do not function on elastic network interfaces that are attached to Amazon EVS VLAN subnets. To control traffic to and from Amazon EVS VLAN subnets, you must use a network access control list.

## Creating an Amazon EVS environment with Self-deployed mode
<a name="getting-started-self-deployed"></a>

Amazon EVS supports a Self-deployed mode that provides you full control over your VCF deployment using the VCF Installer or your preferred Infrastructure as Code solutions to automate the deployment. For example scripts that automate your VCF deployment, see the [Solutions for Amazon EVS](https://github.com/aws/solutions-for-amazon-evs) repository on GitHub.

For the VCF versions currently supported in Self-deployed mode, see [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md).

### Overview
<a name="self-deployed-process"></a>

In Self-deployed mode, you create an Amazon EVS environment, add hosts, and then install and configure VCF yourself. Amazon EVS provisions the AWS networking and VLAN subnets; you deploy VCF with the VCF Installer (or your own IaC) and connect it back to Amazon EVS with connectors.

Before you begin, complete the AWS networking and account prerequisites for your environment. For more information, see [Setting up Amazon Elastic VMware Service](setting-up.md) and the prerequisite checklist in [Amazon EVS deployment prerequisite checklist](evs-deployment-prereq-checklist.md).

Then complete these steps in order:

1.  ** [Create the environment](#self-deployed-create-env) ** — Amazon EVS provisions your VLAN subnets.

1.  ** [Create DNS records](#self-deployed-host-dns-records) ** — Create A and PTR records for your ESX hosts and VCF management appliances.

1.  ** [Add hosts](#self-deployed-add-hosts) ** — Add bare-metal EC2 hosts to your environment.

1.  ** [Install VCF](#self-deployed-install-vcf) ** — Install VCF on your hosts using the VCF Installer.

1.  ** [Configure NSX networking](#self-deployed-nsx-edge) ** — Create your overlay networks on the NSX Edges and configure routing to your VPC.

1.  ** [Create connectors](#self-deployed-create-connectors) ** — Create connectors so that Amazon EVS can monitor your deployment and report license usage.

1.  ** [Verify your environment](#self-deployed-verify) ** — Confirm that your hosts, management appliances, and connectors are healthy.

### Billing
<a name="self-deployed-costs"></a>

After you add hosts to your environment, you accrue AWS charges for the EC2 bare-metal instances as you would for any other EC2 instance, regardless of whether you have installed VCF on them yet.

If you have created an environment in Self-deployed mode but not yet added hosts or installed VCF, AWS may reach out to you using the email address associated with your AWS account, requesting that you either complete setup or remove the environment.

To stop accruing charges for hosts that you are no longer using, delete those hosts. For more information, see [Clean up an Amazon EVS environment with Self-deployed mode](#self-deployed-cleanup).

### Step 1: Create the environment
<a name="self-deployed-create-env"></a>

In Self-deployed mode, environment creation provisions the Amazon EVS VLAN subnets that you specify. It does not deploy VCF or create hosts.

**Example**  

1. Go to the Amazon EVS console.
**Note**  
Ensure that the AWS Region shown in the upper right of your console is the AWS Region that you want to create your environment in.

1. In the navigation pane, choose **Environments**.

1. Choose **Create environment**.

1. On the **Configure environment** step, do the following.

   1. Review the ** AWS account requirements** panel to confirm that your account meets Amazon EVS prerequisites.

   1. (Optional) For **Name**, enter an environment name.

   1. For **VCF version**, choose **Self-deployed**.

   1. Choose **Next**.

1. On the **Configure networks and connectivity** step, do the following.

   1. For **VPC**, choose the VPC that you previously created.

   1. For **Service access subnet**, choose the private subnet that you previously created.

   1. (Optional) For **Service access security group - optional**, choose up to two security groups that control communication between the Amazon EVS control plane and your VPC. Amazon EVS uses the default security group if no security group is chosen.
**Note**  
Ensure that the security groups you choose provide connectivity to the Amazon EVS VLAN subnets.

   1. Under **Management connectivity**, enter CIDR blocks for the Amazon EVS VLAN subnets. Amazon EVS creates these VLAN subnets as part of environment creation.
**Important**  
Amazon EVS VLAN subnets can only be created during environment creation, and cannot be modified after the environment is created. You must ensure that the VLAN subnet CIDR blocks are properly sized before creating the environment. For sizing guidance, see [VLAN subnet sizing guidance](#self-deployed-vlan-sizing).

   1. Under **Expansion VLANs**, enter CIDR blocks for additional Amazon EVS VLAN subnets that you can use to extend your VCF deployment.

   1. Under **Workload/VCF connectivity**, enter the CIDR block for the NSX uplink VLAN.
**Note**  
In Self-deployed mode, you do not select VPC Route Server peers when you create the environment. You configure BGP peering between the NSX Edge Tier-0 gateway and your VPC Route Server yourself, after you install VCF. For more information, see [Step 5: Configure NSX networking](#self-deployed-nsx-edge) and [Set up a VPC Route Server instance with endpoints and peers](#getting-started-create-rs-resources).

   1. Choose **Next**.

1. (Optional) On the **Add tags** step, add tags and choose **Next**.
**Note**  
Hosts that you subsequently add to this environment receive the following tag: `DoNotDelete-EVS-[<environmentId>]-[<hostname>]`. Do not delete, stop, or shut down these hosts outside of Amazon EVS. Doing so causes Amazon EVS to lose visibility into the host and can put your environment into an impaired state.
**Note**  
Tags associated with the Amazon EVS environment do not propagate to underlying AWS resources such as EC2 instances.

1. On the **Review and create** step, review your configuration and choose **Create environment**.

   An information alert on the **Review** page confirms: "Your environment infrastructure will be provisioned now. After creation, add hosts and deploy VCF from the Environment Detail page."

1. Open a terminal session.

1. Run the `aws evs create-environment` command, specifying `--vcf-version SELF_DEPLOYED`.

   In Self-deployed mode, the following parameters are **not supported** and should be omitted. Providing them causes a validation error: `--license-info`, `--hosts`, `--vcf-hostnames`, `--site-id`, `--connectivity-info`.

   The following example creates an Amazon EVS environment in Self-deployed mode. The VLAN CIDR blocks are examples — use values sized for your VPC.

   ```
   aws evs create-environment \
       --environment-name my-self-deployed-env \
       --vpc-id vpc-0abcdef1234567890 \
       --service-access-subnet-id subnet-0fdd7dcd7f1dc0fb4 \
       --vcf-version SELF_DEPLOYED \
       --terms-accepted \
       --initial-vlans '{
         "vmkManagement":   { "cidr": "10.10.0.0/24" },
         "vmManagement":    { "cidr": "10.10.1.0/24" },
         "vMotion":         { "cidr": "10.10.2.0/24" },
         "vSan":            { "cidr": "10.10.3.0/24" },
         "vTep":            { "cidr": "10.10.4.0/24" },
         "edgeVTep":        { "cidr": "10.10.5.0/24" },
         "nsxUplink":       { "cidr": "10.10.6.0/24" },
         "hcx":             { "cidr": "10.10.7.0/24" },
         "expansionVlan1":  { "cidr": "10.10.8.0/24" },
         "expansionVlan2":  { "cidr": "10.10.9.0/24" }
       }' \
       --region us-west-2
   ```

When the environment reaches the `CREATED` state, you can proceed to Step 2.

### Step 2: Create DNS records
<a name="self-deployed-host-dns-records"></a>

Before you add hosts and install VCF, create forward (A record) and reverse (PTR record) DNS entries for each ESX host and for each VCF management appliance you plan to deploy. Amazon EVS performs a DNS lookup of each host’s fully qualified domain name (FQDN) during host creation, and host creation fails if the records do not already exist.

The host FQDN is `<hostName>.<domain>`, where `<hostName>` is the name you will pass to `CreateEnvironmentHost` and `<domain>` is the domain name configured in your VPC’s DHCP option set (see [Configure DNS and NTP servers using the VPC DHCP option set](#getting-started-config-dns-ntp-dhcp)).

**Important**  
The fully qualified domain name (FQDN) for each host and VCF management appliance must not exceed 62 characters. The FQDN is the hostname combined with the domain name from your VPC DHCP option set. When you plan hostnames, include the length of your domain name so that the combined FQDN stays within 62 characters. An FQDN longer than 62 characters causes a `ValidationException` when you call `CreateEnvironment`.

**Note**  
As a NetBIOS best practice, we recommend that you keep each hostname to 15 characters or fewer. This is a recommendation only. A hostname longer than 15 characters does not cause a deployment failure, unlike the 62-character FQDN limit described above.

 **Host records** must:
+ Use the A record IP address within the host management (vmkManagement) VLAN CIDR that you specified in `initialVlans`. Amazon EVS assigns each host its management IP from the A record that you create.
+ Have a matching PTR record in your reverse lookup zone.
+ Be resolvable through DNS from the Amazon EVS service access subnet (both forward and reverse lookups must succeed).

 **VCF management appliance records** (for vCenter Server, NSX Manager, and the other appliances for your VCF version) must:
+ Use FQDNs that match the hostnames you will configure during VCF installation.
+ Fall within the IP address range of the appropriate VLAN subnet.
+ Resolve through DNS from the Amazon EVS management VLAN and from any network from which you reach the VCF management appliances.

**Important**  
Create the A and PTR records for every host **before** you run `CreateEnvironmentHost` for that host. If the records do not resolve, the host transitions to `CREATE_FAILED`.

For more information about DNS configuration for Amazon EVS, see [Configure DNS and NTP servers using the VPC DHCP option set](#getting-started-config-dns-ntp-dhcp).

### Step 3: Add hosts to your environment
<a name="self-deployed-add-hosts"></a>

Add enough hosts to serve your target VCF version topology. For minimum host counts, including vSAN requirements, see the [VMware Cloud Foundation documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0.html).

All hosts in a VCF cluster must use the same instance type. For the list of ESX versions or instance types available to your account, see [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md) or run `aws evs get-versions`. If you do not specify `--esx-version`, Amazon EVS uses the current default ESX version for Self-deployed mode, which is reported as `defaultEsxVersion` by `aws evs get-versions`. To use a specific version such as ESX 9.0.2 or later, pass `--esx-version` explicitly. Confirm that the ESX version you choose is compatible with your VCF release in the [Broadcom Interoperability Matrix](https://interopmatrix.broadcom.com/Interoperability?col=1).

The following example adds a host running ESX 9.0.2 to an Amazon EVS environment.

```
aws evs create-environment-host \
    --environment-id env-0123456789abcdef0 \
    --esx-version ESXi-9.0.2.0.25148076 \
    --host '{
        "hostName": "esx01",
        "keyName": "my-ec2-key-pair",
        "instanceType": "i4i.metal"
    }' \
    --region us-west-2
```

Repeat this command for each host that your VCF topology requires.

### Step 4: Install VCF on your hosts
<a name="self-deployed-install-vcf"></a>

After your hosts are in the `CREATED` state and your DNS records resolve, install VCF using the VMware Cloud Foundation Installer.

Follow the installation guidance for your target VCF version in the Broadcom VCF product documentation. See the [VMware Cloud Foundation documentation](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0.html).

This section describes the Amazon EVS-specific configuration you provide during installation. The installation mechanics themselves (running the VCF Installer, the bringup workflow) follow Broadcom’s standard VCF process and are documented by Broadcom.

 **Installation overview** 

At a high level, installing VCF on your Amazon EVS hosts involves the following. Before you start, review the [Amazon EVS network settings](#sd-install-network) that you apply throughout installation.

1.  ** [Prepare the VCF Installer host](#sd-install-hosts) ** by setting the VM management VLAN ID on the ESX host where the VCF Installer will run.

1.  ** [Prepare a temporary datastore](#sd-install-datastore) ** for the VCF Installer appliance. The vSAN datastore does not exist until bringup completes, so the Installer needs somewhere to run first.

1.  ** [Deploy the VCF Installer appliance and download the VCF software](#sd-install-deploy) ** using a Broadcom download token.

1.  ** [Run VCF bringup](#sd-install-bringup) **, which deploys the VCF management appliances and creates the vSAN datastore.

1.  ** [Reclaim the temporary datastore](#sd-install-reclaim) ** after VCF is fully installed and the Installer appliance is running on vSAN.

You supply Amazon EVS-specific network, storage, and credential settings during bringup. The rest of the process follows Broadcom’s standard VCF installation.

**Note**  
Amazon EVS provides automated procedures that perform this installation end to end, including the Amazon EVS-specific configuration described in this section. For a worked example, see the [Solutions for Amazon EVS](https://github.com/aws/solutions-for-amazon-evs) repository on GitHub.

<a name="sd-install-network"></a> **Amazon EVS network settings for VCF** 

Amazon EVS assigns a VLAN ID to each network function in your environment. To find the VLAN ID for a function, open the Amazon EVS console (**Environments** → your environment → **Networks and connectivity** tab), or run `aws evs list-environment-vlans` and match on the function name (for example, `vmManagement`). Use these VLAN IDs when you configure the distributed switch, port groups, and host networking during VCF installation.


| Network function | MTU | Used for | 
| --- | --- | --- | 
| Host management (vmkManagement) | 1500 | ESX host management | 
| VM management (vmManagement) | 1500 | VCF management appliances (vCenter Server, NSX Manager, and SDDC Manager or VCF Operations) | 
| vMotion | 8500 | vMotion traffic | 
| vSAN | 8500 | vSAN storage traffic | 
| Host overlay (vTep) | 8500 | Host overlay (Geneve) tunnel endpoints | 
| Edge overlay (edgeVTep) | 8500 | NSX Edge overlay tunnel endpoints | 
| NSX uplink (nsxUplink) | 1500 | Tier-0 gateway north-south uplink | 

**Important**  
Configure jumbo frames (MTU 8500) on the vMotion, vSAN, and overlay (TEP) networks. The management and uplink networks use MTU 1500. The MTU must be consistent across the network path, or vSAN and overlay traffic will fail.

When you configure the management cluster during bringup, also apply these Amazon EVS-specific settings:
+  **vSAN** — Use vSAN ESA (Express Storage Architecture) with failures-to-tolerate (FTT) set to at least 1.
+  **Uplink teaming** — Use a failover teaming policy (active uplink with a standby uplink) for the distributed switch port groups, rather than a load-balancing policy.
+  **EVC mode** — Set the cluster Enhanced vMotion Compatibility (EVC) mode to match your instance type: `INTEL_ICELAKE` for `i4i.metal`, or `INTEL_SAPPHIRERAPIDS` for `i7i.metal-24xl` and `i7i.metal-48xl`.

#### Prepare the VCF Installer host
<a name="sd-install-hosts"></a>

On the ESX host where you will run the VCF Installer appliance, set the `VM Network` port group to the Amazon EVS-assigned VM management VLAN ID. This makes sure the VCF Installer appliance can communicate on the VM management VLAN. The host management network port group `Management` must remain untagged with VLAN ID `0`. The VCF Installer migrates host networking to a distributed switch during bringup. You do not need to enable SSH on the hosts.

1. Find the VLAN ID of the VM management network. In the Amazon EVS console, open **Environments**, choose your environment, and then choose the **Networks and connectivity** tab. Alternatively, run `aws evs list-environment-vlans` and match the `vmManagement` function.

1. On the VCF Installer host, set the `VM Network` port group VLAN ID to the VM management VLAN ID. Leave the host management port group `Management` untagged with VLAN ID `0`.

#### Prepare a temporary datastore for the VCF Installer
<a name="sd-install-datastore"></a>

Amazon EVS hosts have no local VMFS datastores, and the vSAN datastore does not exist until bringup completes, so the VCF Installer appliance needs a temporary datastore to run from. Choose one host to run the Installer.

1. In the Amazon EC2 console, create an encrypted General Purpose SSD (`gp3`) Amazon EBS volume in the same Availability Zone as the host you chose. Size it to hold the VCF Installer appliance and the VCF installation bundles: at least 256 GB.

1. Attach the newly created EBS volume to the ESX host you chose earlier. For instructions, see [Attach an Amazon EBS volume to an instance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-attaching-volume.html) in the *Amazon EBS User Guide*.

1. Using the VMware Host Client or the vSphere APIs, create a local VMFS datastore on the attached EBS volume.

#### Deploy the VCF Installer and download the VCF software
<a name="sd-install-deploy"></a>

1. Make sure that your Broadcom account has a valid VCF entitlement so you can generate a download token. Download the VCF Installer OVA for your target VCF version, and generate a Broadcom download token from the [Broadcom Support Portal](https://support.broadcom.com/). You use this token in the VCF Installer to enable the software depot.

1. Deploy the VCF Installer OVA onto the local VMFS datastore. Attach it to the `VM Network` port group, set its management IP address to the SDDC Manager address from your DNS plan, and set the appliance password. The VCF Installer appliance becomes SDDC Manager during bringup, so it uses the SDDC Manager address. (On VCF 9.0.x and 9.1.x, VCF Operations is a separate appliance.)

1. In the VCF Installer, enable the software depot using your Broadcom download token, then sync the VCF version you want. Syncing pulls that version of the VCF software into the Installer’s local depot.
**Note**  
Enabling the depot and syncing software requires outbound internet access from the Installer. The NAT gateway in your network foundation provides this access. For more information, see [Create a VPC with subnets and route tables](#getting-started-create-vpc).

#### Run VCF bringup
<a name="sd-install-bringup"></a>

With the software synced, create your VCF deployment specification, validate it, and run the deployment.

1. In the VCF Installer, create the deployment specification for your management domain. Apply the Amazon EVS-specific network, storage, teaming, and validation settings described in this step.

1. Run validation against the specification, and resolve any errors that it reports.

1. Run the deployment.
**Note**  
Bringup is the longest part of the installation and accounts for most of the setup time. When you use vSAN, forming the datastore and deploying the management appliances can take several hours.

#### Reclaim the temporary datastore
<a name="sd-install-reclaim"></a>

When bringup finishes, the management appliances run on the vSAN datastore, and the temporary VMFS datastore is empty. Reclaim the temporary datastore:

1. In the vSphere Client, unmount the temporary VMFS datastore from the host.

1. In the Amazon EC2 console or using the AWS CLI, detach the EBS volume from the host instance. For instructions, see [Detach an Amazon EBS volume from an instance](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-detaching-volume.html) in the *Amazon EBS User Guide*.

1. Wait until the volume state is `available`, then delete the volume through the EC2 console or the AWS CLI to stop accruing storage charges. To check the volume state, see [View Amazon EBS volume information](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-describing-volumes.html). To delete the volume, see [Delete an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-volume.html) in the *Amazon EBS User Guide*.

#### VCF appliance passwords
<a name="sd-install-passwords"></a>

During bringup you set passwords for the VCF management appliances. Each appliance enforces its own password complexity requirements, which are defined by VCF. If an appliance rejects a password, the validation error states the specific requirement that the password must meet.

#### Bringup validation settings for VCF Installer
<a name="sd-install-validation"></a>

Several VCF Installer standard validation checks do not apply to the Amazon EVS network environment. How you handle them depends on whether you drive bringup with a spec file or the VCF Installer wizard.
+  **Gateway ping validation** – Amazon EVS VLAN subnet gateways do not respond to ICMP ping from outside the subnet, so the gateway reachability check fails on Amazon EVS even when routing is correct.
  +  **Spec file** – set `skipGatewayPingValidation` to `true`.
  +  **Wizard** – acknowledge the failing gateway ping check and continue.
+  **ESX host thumbprint validation** 
  +  **Spec file** – set `skipEsxThumbprintValidation` to `true` or extract and enter correct thumbprints for all hosts in the spec.
  +  **Wizard** – thumbprint validation is mandatory. Review and accept the thumbprint to continue at the hosts step.
+  **Distributed switch teaming** – Set the NSX teaming policy to `FAILOVER_ORDER`, consistent with the failover teaming described earlier in this step.

**Note**  
When you run bringup through the VCF Installer wizard, use the wizard to identify and correct spec errors. The wizard surfaces validation problems more clearly than the API, whose errors are less descriptive.

**Note**  
For a validated bringup spec, refer to the [Solutions for Amazon EVS](https://github.com/aws/solutions-for-amazon-evs) repository on GitHub.

**Note**  
Amazon EVS does not support running ESX outside of a full VCF deployment. VMware workload virtual machines must be deployed onto NSX overlay networks. Attaching a large number of virtual machines directly to the underlay VLAN networks may result in stability and performance issues.

**Important**  
In Self-deployed mode, Amazon EVS does not manage VCF installation. If you have VCF-specific requests, you can use your active VCF subscription entitlements to contact Broadcom directly through the Broadcom Support Portal. For more information about support boundaries, see [Troubleshooting](#self-deployed-troubleshooting).

### Step 5: Configure NSX networking
<a name="self-deployed-nsx-edge"></a>

Create your overlay networks using Tier-0/Tier-1 routers on the NSX Edges directly, or by configuring VPCs, a centralized transit gateway, and edge clusters. After the VCF Installer completes bringup, the NSX Manager is operational, but the NSX Edge cluster and Tier-0 gateway are not fully configured for connectivity with the VPC Route Server.

**Note**  
NSX defines its own **VPC** and **transit gateway** abstractions, which are different from Amazon VPC and AWS Transit Gateway. In this guide, "VPC" and "transit gateway" refer to the AWS resources unless prefixed with "NSX".

Before you begin, confirm that the following are in place:
+ VCF installation completed successfully (NSX Manager and your VCF management appliance, Operations Manager for VCF 9.x or SDDC Manager for VCF 5.2.x, are all accessible).
+ Your VPC Route Server is created with endpoints, peers, and propagations. For more information, see [Set up a VPC Route Server instance with endpoints and peers](#getting-started-create-rs-resources).
+ You have the two Route Server endpoint IP addresses. Both endpoints are in the service access subnet, which provides redundancy.
+ You choose two private BGP ASNs, which must match the values you configured on the VPC Route Server peers (see [Set up a VPC Route Server instance with endpoints and peers](#getting-started-create-rs-resources)):
  + NSX Edge Tier-0 local ASN (for example, `65000`)
  + VPC Route Server (remote) ASN (for example, `65022`)

    Private ASNs are in the range 64512–65534 (16-bit) or 4200000000–4294967294 (32-bit).

<a name="sd-nsx-uplink-profile"></a> **Create an uplink profile** 

Before you deploy the NSX Edge cluster, create an uplink profile in NSX Manager. The uplink profile defines the teaming policy, transport VLAN, and MTU that Edge transport nodes use for overlay (Geneve) traffic.

For version-specific field labels and screenshots, see:
+ VCF 9.0.x: [Create an Uplink Profile](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/transport-zones-and-transport-nodes/configuring-profiles/create-an-uplink-profile.html) in the VMware Cloud Foundation documentation.
+ VCF 9.1.x: [Add an Uplink Profile](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/advanced-network-management/transport-zones-and-transport-nodes/configuring-profiles/create-an-uplink-profile.html) in the VMware Cloud Foundation documentation.

Configure the profile with the following Amazon EVS-specific values:


| Parameter | Value | 
| --- | --- | 
| Name | For example, `edge-uplink-profile`. | 
| Teaming policy | Failover Order. | 
| Active Uplinks |  `uplink1`. | 
| Standby Uplinks | Leave empty. NSX Edge VMs do not support standby uplinks. | 
| Transport VLAN | The Amazon EVS-assigned Edge TEP VLAN ID. Look up the ID for your environment in the Amazon EVS console (**Environments** → your environment → **Networks and connectivity** tab), or by running `aws evs list-environment-vlans` and matching on the `edgeVTep` function. | 
| MTU |  `8500`. | 

Use the uplink name `uplink1` when you configure each Edge transport node in the following **Deploy the NSX Edge cluster** step.

 **Deploy the NSX Edge cluster** 

Deploy two Edge transport nodes and group them into an Edge cluster using the NSX Manager UI. The workflow order differs by VCF version. VCF 9.0.x creates Edge transport nodes individually and then creates the Edge cluster as a separate action. VCF 9.1.x begins with an Edge cluster workflow and adds nodes within it.

For the complete procedure, refer to the Broadcom documentation for your VCF version:
+ VCF 9.0.x: [Create an Edge Transport Node](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/create-an-edge-transport-node.html) and [Create an Edge Cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-0/advanced-network-management/administration-guide/installing-nsx-edge/create-an-edge-cluster.html).
+ VCF 9.1.x: [Create an NSX Edge Cluster and Add Edge Nodes](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-9-0-and-later/9-1/advanced-network-management/installing-nsx-edge/create-an-edge-transport-node.html).

When configuring the Edge nodes for your Amazon EVS environment, select the following:


| Parameter | Value | 
| --- | --- | 
| Name | A unique name for each Edge node (for example, `edge-node-01` and `edge-node-02`). | 
| Form factor | Large (recommended). | 
| Compute and datastore | A compute resource and datastore appropriate for your deployment. | 
| Management IP | An IP address from the EVS VM management subnet. | 
| Default gateway | The default gateway for the EVS VM management subnet. | 
| Management interface | The VM management port group. | 
| Transport networking | The EVS-assigned transport VLAN and applicable uplink profile for datapath connectivity. | 

 **Create the Tier-0 gateway** 

1. In NSX Manager, navigate to **Networking** → **Tier-0 Gateways**.

1. Choose **Add Tier-0 Gateway** and configure the following:

   1.  **Name** — for example, `evs-tier0-gw`.

   1.  **HA mode** — **Active-Standby** with failover mode set to **Non-preemptive**.

   1.  **Edge cluster** — select the Edge cluster that you created.

1. Save the Tier-0 gateway.

**Note**  
Ensure both the Tier-0 and Tier-1 gateways have **Non-preemptive** failover. Non-preemptive is the NSX default and avoids an unnecessary BGP session drop when a recovered Edge node would otherwise fail back to the preferred node.

 **Configure BGP** 

1. Select the Tier-0 gateway and expand **BGP**.

1. Enable **BGP** and set the **Local AS** number to the NSX Edge Tier-0 ASN you chose (for example, `65000`).

1. Under **BGP Neighbors**, configure peering between the Edge nodes and the VPC Route Server endpoints. We recommend a **full mesh**: each of the two Edge nodes peers with **both** Route Server endpoints, for four BGP sessions in total. A full mesh keeps routes propagating if a Route Server endpoint goes into maintenance. At minimum, configure two sessions, with each Edge node peering with one endpoint.

   For a full mesh, add four neighbors. Set the **Remote AS** of every neighbor to the VPC Route Server ASN (for example, `65022`) and the **Address family** to IPv4 Unicast.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/evs/latest/userguide/getting-started.html)
**Note**  
The Edge uplink interfaces and the Route Server endpoints are in different subnets, so these are multihop BGP sessions. Set the BGP multihop limit to at least 2, and ensure the Tier-0 gateway can reach each Route Server endpoint IP address (for example, with a static route to the endpoint by way of the uplink gateway).

1. Choose **Save**.

1. Wait for the BGP sessions to establish.

1. To advertise only overlay-network routes to the VPC Route Server, configure route redistribution and an outbound route filter on the Tier-0 gateway in NSX Manager.

   1. On the Tier-0 gateway, expand **Route Re-Distribution** and enable redistribution into BGP for your overlay network route types, for example, **Tier-1 Connected** (workload segment subnets), **Tier-1 NAT**, and **Tier-1 Static Routes**.

      Do not select **External Interface Subnet** and do not select Tier-0 **Static Routes**. Redistributing **External Interface Subnet** advertises the NSX uplink subnet to AWS, and **Static Routes** re-advertises the Route Server endpoint host routes; neither is wanted.

   1. (Optional) Apply an outbound route filter for RFC 1918 networks to limit the CIDRs that are advertised to your VPC. Create an IP prefix list that permits `10.0.0.0/8`, `172.16.0.0/12`, and `192.168.0.0/16` (including more-specific routes within them), denies all other prefixes, and apply it as the out-filter on each BGP neighbor.

 **Verify BGP peering** 

1. In NSX Manager, navigate to **Networking** → **Tier-0 Gateways** → **BGP** → **BGP Neighbors**, and confirm that both neighbors show status **Established**.

1. In the AWS console, navigate to **VPC** → **Route Server** → **Routes**, and confirm that NSX overlay routes appear.

1. In NSX Manager, verify that VPC routes are learned under **Routing** → **Forwarding Table**.

The following table lists common BGP peering issues.


| Symptom | Likely cause | Resolution | 
| --- | --- | --- | 
| BGP session stuck in `Active` state | Firewall or network ACL blocking TCP port 179 | Verify that your network ACL allows TCP 179 between the Edge uplink IP addresses and the Route Server endpoint IP addresses, and that the security group attached to the Route Server endpoints also allows inbound TCP 179. | 
| BGP session flaps repeatedly | MTU mismatch on the uplink path | Ensure that the MTU is consistent along the NSX uplink path. The NSX uplink network uses MTU 1500; the overlay (TEP) networks use MTU 8500. | 
| Routes not appearing in the VPC route table | Route Server propagation not enabled | Verify that Route Server propagation is enabled on the target route table. | 
| One-sided peering (only one session is up) | Edge node connectivity issue | Verify that both Edge nodes have reachability to both Route Server endpoints. | 

After the BGP sessions are established and routes are propagating, proceed to [Step 6: Create connectors](#self-deployed-create-connectors).

### Step 6: Create connectors
<a name="self-deployed-create-connectors"></a>

After VCF is installed and its management appliances are reachable over your VCF management network, create connectors so that Amazon EVS can monitor your deployment and report license usage. A connector is an Amazon EVS sub-resource that represents a persistent connection from Amazon EVS to a specific VCF management appliance. For more information, see [Connector](concepts.md#concepts-connector).

**Important**  
Before you create a connector, store the credentials for the target VCF management appliance in AWS Secrets Manager. Tag the secret and the AWS KMS key that encrypts it with `EvsAccess=true`. Without this tag, Amazon EVS cannot access the secret and connector creation fails.

The connector type you create depends on your VCF version. VCF 9.x requires an Operations Manager (`OPERATIONS_MANAGER`) connector. VCF 5.2.x requires an SDDC Manager (`SDDC_MANAGER`) connector. You can also create a vCenter connector (`VCENTER`). For the connector types, required secret keys, and descriptions, see [Create an Amazon EVS environment connector](evs-env-create-connector.md).

### Step 7: Verify the environment
<a name="self-deployed-verify"></a>

After you have added hosts, installed VCF, and created at least one connector, verify that:
+ Your hosts are in the `CREATED` state.
+ Your VCF management appliances are reachable from the management VLAN.
+ The connectors you created reach the `ACTIVE` state and the **Environment status** on the **Environments** page aggregates to healthy.

For guidance on interpreting environment status and connector health, see [Monitor your environment's status and resources](evs-env-status-check.md).

### VLAN subnet sizing guidance
<a name="self-deployed-vlan-sizing"></a>

Amazon EVS VLAN subnets cannot be modified after environment creation. Size each VLAN based on the number of IP addresses your VCF components consume now and over the lifetime of the environment. Consider the following when sizing:
+  **Host management (vmkManagement) VLAN** — one IP per host. Plan for the maximum number of hosts you expect in this environment.
+  **vMotion, vSAN, VTEP VLANs** — one or more IPs per host depending on your VCF configuration.
+  **Management VM (vmManagement) VLAN** — IPs for the VCF management appliances you plan to deploy: vCenter, NSX Manager cluster, NSX Edge nodes, and SDDC Manager or Operations Manager.
+  **Edge VTEP, HCX uplink, NSX uplink VLANs** — IPs for NSX Edge uplinks and HCX appliances, if used.
+  **Expansion VLANs** — reserve space for future features such as NSX Federation.

As a starting point, use `/24` for each VLAN unless you have a specific reason to choose otherwise. VLAN subnets have a minimum size of `/28` and a maximum of `/24`.

### Security considerations
<a name="self-deployed-security"></a>

In Self-deployed mode, you install and operate the VCF software stack, so you are responsible for its security. AWS secures the underlying AWS infrastructure that Amazon EVS provisions. This split of responsibilities is in addition to the shared responsibility model described in [Security in Amazon Elastic VMware Service](security.md).

Your side of the shared responsibility model includes:
+ Installing, patching, and upgrading VCF components including vCenter Server, NSX, SDDC Manager or Operations Manager, and ESX.
+ Configuring VCF authentication, role-based access control, and password rotation for all VCF management appliances.
+ Hardening your VCF management network in accordance with Broadcom guidance and your organization’s security requirements.
+ Rotating the secrets in AWS Secrets Manager that Amazon EVS connectors use to access your VCF management appliances.
+ Monitoring your VCF deployment for security events.
+ Maintaining valid VCF licenses in your VCF management appliance. For more information, see [VCF subscriptions](vcf-license-mgmt.md).

Amazon EVS is responsible for:
+ Securing the Amazon EVS control plane and Amazon EVS-provisioned AWS resources.
+ Encrypting customer credentials that you store in Secrets Manager (via AWS KMS) and restricting service access to those credentials using resource tags.
+ Monitoring the health of the connectors that you create and reporting aggregate environment health.

### Troubleshooting
<a name="self-deployed-troubleshooting"></a>


| Symptom | Where to get help | 
| --- | --- | 
|  `aws evs create-environment` returns `ValidationException` mentioning a parameter such as `licenseInfo`, `hosts`, `vcfHostnames`, `siteId`, or `connectivityInfo`. | Remove the indicated parameter from your request. These parameters are not supported when `vcfVersion=SELF_DEPLOYED`. | 
| Environment remains in the `CREATING` state longer than expected. | Open a support case with AWS Support. Include the environment ID. | 
|  `aws evs create-environment-host` fails with an ESX version error. | Verify the ESX version string using `aws evs get-versions --region <region>`. Your account may not have access to the requested version. For more information, see [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md). | 
| A host is stuck in `CREATING` or moves to `CREATE_FAILED` state. | Open a support case with AWS Support. Include the environment ID and host ID. | 
| VCF Installer fails during VCF deployment. | Contact AWS Support for any Amazon EVS issue. For VCF-specific requests, you can also contact Broadcom directly using your VCF subscription entitlements. | 
|  `aws evs create-environment-connector` fails with a Secrets Manager access error. | Confirm that your secret and its AWS KMS encryption key are both tagged with `EvsAccess=true`. For more information, see [Create an Amazon EVS environment connector](evs-env-create-connector.md). | 
| Connector reaches `ACTIVE` but its reachability check remains `FAILED`. | Confirm that the appliance FQDN resolves from the Amazon EVS control plane and that the stored credentials are valid. For more information, see [Monitor your environment's status and resources](evs-env-status-check.md). | 

### Clean up an Amazon EVS environment with Self-deployed mode
<a name="self-deployed-cleanup"></a>

When you no longer need your Amazon EVS environment:

1. Delete all connectors. For more information, see [Delete an Amazon EVS environment connector](evs-env-delete-connector.md).

1. Delete all hosts. For more information, see [Delete an Amazon EVS host](evs-env-delete-host.md).

1. Delete the environment. For more information, see [Delete the Amazon EVS hosts and environment](#getting-started-cleanup-env-hosts).

Deleting the environment removes the Amazon EVS VLAN subnets that Amazon EVS created. It does not delete the VPC, VPC Route Server, or other AWS resources that you created outside of Amazon EVS.

## Create an Amazon EVS environment
<a name="getting-started-create-env"></a>

**Important**  
To get started as simply and quickly as possible, this topic includes steps to create an Amazon EVS environment with default settings. Before creating an environment, we recommend that you familiarize yourself with all settings and deploy an environment with the settings that meet your requirements. Environments can only be configured during initial environment creation. Environments cannot be modified after you’ve created them. For an overview of all possible Amazon EVS environment settings, see the [Amazon EVS API Reference Guide](https://docs.aws.amazon.com/evs/latest/APIReference/Welcome.html).

**Note**  
You environment ID will be available to Amazon EVS across all AWS Regions for VCF license compliance needs.

**Note**  
Amazon EVS environments must be deployed into the same Region and Availability Zone as the VPC and VPC subnets.

Complete this step to create an Amazon EVS environment with hosts and VLAN subnets.

**Example**  

1. Go to the Amazon EVS console.
**Note**  
Ensure that the AWS Region shown in the upper right of your console is the AWS Region that you want to create your environment in. If it’s not, choose the dropdown next to the AWS Region name and choose the AWS Region that you want to use.

1. In the navigation pane, choose **Environments**.

1. Choose **Create environment**.

1. On the **Validate Amazon EVS requirements** page, check that service requirements have been met. For more information, see [Setting up Amazon Elastic VMware Service](setting-up.md).

   1. (Optional) For **Name**, enter an environment name.

   1. For **Environment version**, choose your VCF version. For information about VCF versions provided by Amazon EVS, see [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md).
**Note**  
The VCF version dropdown also includes a **Self-deployed** option. If you select this option, the wizard uses the Self-deployed flow instead of the steps below. For more information, see [Creating an Amazon EVS environment with Self-deployed mode](#getting-started-self-deployed).

   1. For **Site ID**, enter your Broadcom Site ID.

   1. For **VCF Solution key**, enter a VCF solution key (VMware vSphere 8 Enterprise Plus for VCF). This license key cannot be in use by an existing environment.
**Note**  
The VCF solution key must have sufficient cores. For more information, see [VCF subscriptions](vcf-license-mgmt.md).
**Note**  
Your VCF license will be available to Amazon EVS across all AWS Regions for license compliance. Amazon EVS does not validate license keys. To validate license keys, visit [Broadcom support](https://support.broadcom.com/web/ecx).
**Note**  
Amazon EVS requires that you maintain a valid VCF solution key in SDDC Manager for the service to function properly. If you manage the VCF solution key using the vSphere Client post-deployment, you must ensure that the keys also appear in the licensing screen of the SDDC Manager user interface.

   1. For **vSAN license key**, enter a vSAN license key. This license key cannot be in use by an existing environment.
**Note**  
The vSAN license key must have sufficient vSAN capacity. For more information, see [VCF subscriptions](vcf-license-mgmt.md).
**Note**  
Your VCF license will be available to Amazon EVS across all AWS Regions for license compliance. Amazon EVS does not validate license keys. To validate license keys, visit [Broadcom support](https://support.broadcom.com/web/ecx).
**Note**  
Amazon EVS requires that you maintain a valid vSAN license key in SDDC Manager for the service to function properly. If you manage the vSAN license key using the vSphere Client post-deployment, you must ensure that the keys also appear in the licensing screen of the SDDC Manager user interface.

   1. For **VCF license terms**, check the box to confirm that you have purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance.

   1. Choose **Next**.

1. On the **Specify host details** page, complete the following steps four times to add four hosts to the environment. Amazon EVS environments require four hosts for initial deployment.

   1. Choose **Add host details**.

   1. For **DNS hostname**, enter the host name for the host.

   1. For **instance type**, choose the EC2 instance type.

   1. For **ESX host version**, during environment creation a default ESX version for the chosen VCF version will be used. See [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md) for more information.
**Important**  
Do not stop or terminate EC2 instances that Amazon EVS deploys. This action results in data loss.

   1. For **SSH key pair**, choose an SSH key pair for SSH access into the host.

   1. Choose **Add host**.

1. On the **Configure networks and connectivity** page, do the following.

   1. For **HCX connectivity requirements**, select whether you want to use HCX with private connectivity or over the internet.

   1. For **VPC**, choose the VPC that you previously created.

   1. (For HCX internet connectivy only) For **HCX network ACL**, choose which network ACL your HCX VLAN will be associated with.
**Important**  
We strongly recommend that you create a custom network ACL dedicated to the HCX VLAN. For more information, see [Configure a network access control list to control Amazon EVS VLAN subnet traffic](evs-env-nacl-cong.md).

   1. For **Service access subnet**, choose the private subnet that was created when you created the VPC.

   1. For **Security group -*optional* **, you can choose up to two security groups that control communication between the Amazon EVS control plane and VPC. Amazon EVS uses the default security group if no security group is chosen.
**Note**  
Ensure that the security groups that you choose provide connectivity to your DNS servers and Amazon EVS VLAN subnets.

   1. Under **Management connectivity**, enter the CIDR blocks to be used for the Amazon EVS VLAN subnets. For **HCX uplink VLAN CIDR block**, if configuring a public HCX VLAN, you must specify a CIDR block with a netmask length of exactly /28. Amazon EVS throws a validation error if any other CIDR block size is specified for the public HCX VLAN. For a private HCX VLAN and all other VLANs CIDR blocks, the minimum netmask length that you can use is /28 and the maximum is /24.
**Important**  
Amazon EVS VLAN subnets can only be created during Amazon EVS environment creation, and cannot be modified after the environment is created. You must ensure that the VLAN subnet CIDR blocks are properly sized before creating the environment. You will not be able to add VLAN subnets after the environment is deployed. For more information, see [Amazon EVS networking considerations](architecture.md#evs-subnets).

   1. Under **Expansion VLANs**, enter the CIDR blocks for additional Amazon EVS VLAN subnets that can be used to expand VCF capabilities within Amazon EVS, such as enabling NSX Federation.

   1. Under **Workload/VCF connectivity**, enter the CIDR block for the NSX uplink VLAN, and choose two VPC Route Server peer IDs that peer to Route Server endpoints over the NSX uplink.
**Note**  
Amazon EVS requires a VPC Route Server instance that is associated with two Route Server endpoints and two Route Server peers prior to EVS deployment. This configuration enables dynamic BGP-based routing over the NSX uplink. For more information, see [Set up a VPC Route Server instance with endpoints and peers](#getting-started-create-rs-resources).

   1. Choose **Next**.

1. On the **Specify Management DNS hostnames** page, do the following.

   1. Under **Management appliance DNS hostnames**, enter the DNS hostnames for the virtual machines to host VCF management appliances. If using Route 53 as your DNS provider, also choose the hosted zone that contains your DNS records.

   1. Under **Credentials**, choose whether you’d like to use the AWS managed KMS key for Secrets Manager or a customer managed KMS key that you provide. This key is used to encrypt the VCF credentials that are required to use SDDC Manager, NSX Manager, and vCenter appliances.
**Note**  
There are usage costs associated with customer managed KMS keys. For more information, see the [AWS KMS pricing page](https://aws.amazon.com/kms/pricing).

   1. Choose **Next**.

1. (Optional) On the **Add tags** page, add any tags that you would like to be assigned to this environment and choose **Next**.
**Note**  
Hosts created as part of this environment will receive the following tag: `DoNotDelete-EVS-[<environmentId>]-[<hostname>]`.
**Note**  
Tags that are associated with the Amazon EVS environment do not propagate to underlying AWS resources such as EC2 instances. You can create tags on underlying AWS resources using the respective service console or the AWS CLI.

1. On the **Review and create** page, review your configuration and choose **Create environment**.
**Important**  
During environment deployment, Amazon EVS creates the EVS VLAN subnets and implicitly associates them with the main route table. After the deployment completes, you must explicitly associate the Amazon EVS VLAN subnets with a route table for NSX connectivity purposes. For more information, see [Explicitly associate Amazon EVS VLAN subnets to a VPC route table](#getting-started-associate-vlans).
**Note**  
Amazon EVS deploys a recent bundled version of VMware Cloud Foundation which may not include individual product updates, known as async patches. Upon completion of this deployment, we strongly recommend that you review and update individual products using Broadcom’s Async Patch Tool (AP Tool) or SDDC Manager in-product LCM automation. NSX upgrades must be done outside of SDDC Manager.
**Note**  
Environment creation can take several hours.

1. Open a terminal session.

1. Create an Amazon EVS environment. Below is a sample `aws evs create-environment` request.
**Important**  
Before running the `aws evs create-environment` command, check that all Amazon EVS prerequisites have been met. Environment deployment fails if prerequisites have not been met. For more information, see [Setting up Amazon Elastic VMware Service](setting-up.md).
**Important**  
During environment deployment, Amazon EVS creates the EVS VLAN subnets and implicitly associates them with the main route table. After the deployment completes, you must explicitly associate the Amazon EVS VLAN subnets with a route table for NSX connectivity purposes. For more information, see [Explicitly associate Amazon EVS VLAN subnets to a VPC route table](#getting-started-associate-vlans).
**Note**  
Amazon EVS deploys a recent bundled version of VMware Cloud Foundation which may not include individual product updates, known as async patches. Upon completion of this deployment, we strongly recommend you review and update individual products using Broadcom’s Async Patch Tool (AP Tool) or SDDC Manager in-product LCM automation. NSX upgrades must be done outside of SDDC Manager.
**Note**  
Environment deployment can take several hours.
   + For `--vpc-id`, specify the VPC that you previously created with a minimum IPv4 CIDR range of /22.
   + For `--service-access-subnet-id`, specify the unique ID of the private subnet that was created when you created the VPC.
   + For `--vcf-version`, See [VCF versions and EC2 instance types provided by Amazon EVS](versions-provided.md) for VCF versions provided by Amazon EVS,
   + With `--terms-accepted`, you confirm that you have purchased and will continue to maintain the required number of VCF software licenses to cover all physical processor cores in the Amazon EVS environment. Information about your VCF software in Amazon EVS will be shared with Broadcom to verify license compliance.
   + For `--license-info`, enter your VCF solution key (VMware vSphere 8 Enterprise Plus for VCF) and vSAN license key.
**Note**  
The requirements for the VCF solution key (including minimum core count) and vSAN license key (including minimum vSAN capacity) vary depending on the instance type. For specific thresholds for your configuration, see [VCF subscriptions](vcf-license-mgmt.md).
**Note**  
Amazon EVS requires that you maintain a valid VCF solution key and vSAN license key in SDDC Manager for the service to function properly. If you manage these license keys using the vSphere Client post-deployment, you must ensure that they also appear in the licensing screen of the SDDC Manager user interface.
**Note**  
The VCF solution key and vSAN license key cannot be in use by an existing Amazon EVS environment.
   + For `--initial-vlans` specify the CIDR ranges for the Amazon EVS VLAN subnets that Amazon EVS creates on your behalf. These VLANs are used to deploy VCF management appliances. If configuring a public HCX VLAN, you must specify a CIDR block with a netmask length of exactly /28. Amazon EVS throws a validation error if any other CIDR block size is specified for the public HCX VLAN. For a private HCX VLAN and all other VLANs CIDR blocks, the minimum netmask length that you can use is /28 and the maximum is /24.
   +  `hcxNetworkAclId` is used if configuring HCX internet connectivity. Specify a custom network ACL for the public HCX VLAN.
**Important**  
We strongly recommend that you create a custom network ACL dedicated to the HCX VLAN. For more information, see [Configure a network access control list to control Amazon EVS VLAN subnet traffic](evs-env-nacl-cong.md).
**Important**  
Amazon EVS VLAN subnets can only be created during Amazon EVS environment creation, and cannot be modified after the environment is created. You must ensure that the VLAN subnet CIDR blocks are properly sized before creating the environment. You will not be able to add VLAN subnets after the environment is deployed. For more information, see [Amazon EVS networking considerations](architecture.md#evs-subnets).
   + For `--hosts`, specify host details for the hosts that Amazon EVS requires for environment deployment. Include DNS hostname, EC2 SSH key name, and EC2 instance type for each host. The dedicated host ID is optional.
**Important**  
Do not stop or terminate EC2 instances that Amazon EVS deploys. This action results in data loss.
   + For `--connectivity-info`, specify the 2 VPC Route Server peer IDs that you created in the previous step.
**Note**  
Amazon EVS requires a VPC Route Server instance that is associated with two Route Server endpoints and two Route Server peers prior to EVS deployment. This configuration enables dynamic BGP-based routing over the NSX uplink. For more information, see [Set up a VPC Route Server instance with endpoints and peers](#getting-started-create-rs-resources).
   + For `--vcf-hostnames`, enter the DNS hostnames for the virtual machines to host VCF management appliances.
   + For `--site-id`, enter your unique Broadcom site ID. This ID allows access to the Broadcom portal, and is provided to you by Broadcom at the close of your software contract or contract renewal.
   + (Optional) For `--region`, enter the Region that your environment will be deployed into. If the Region isn’t specified, your default Region is used.

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
<a name="verify-env-creation"></a>

**Example**  

1. Go to the Amazon EVS console.

1. In the navigation pane, choose **Environments**.

1. Select the environment.

1. Select the **Details** tab.

1. Check that the **Environment status** is **Passed** and the **Environment state** is **Created**. This lets you know that the environment is ready to use.
**Note**  
Environment creation can take several hours. If the **Environment state** still shows **Creating**, refresh the page.

1. Open a terminal session.

1. Run the following command, using the environment ID for your environment and the Region name that contains your resources. The environment is ready to use when the `environmentState` is `CREATED`.
**Note**  
Environment creation can take several hours. If the `environmentState` still shows `CREATING`, run the command again to refresh the output.

   ```
   aws evs get-environment --environment-id env-abcde12345 --region us-east-2
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
<a name="getting-started-associate-vlans"></a>

Explicitly associate each of the Amazon EVS VLAN subnets with a route table in your VPC. This route table is used to allow AWS resources to communicate with virtual machines on NSX network segments, running with Amazon EVS. If you’ve created a public HCX VLAN, be sure to explicitly associate the public HCX VLAN subnet with a public route table in your VPC that routes to an internet gateway.

**Example**  

1. Go to the [VPC console](https://console.aws.amazon.com/vpc).

1. In the navigation pane, choose **Route tables**.

1. Choose the route table that you want to associate with Amazon EVS VLAN subnets.

1. Select the **Subnet associations** tab.

1. Under **Explicit subnet associations**, select **Edit subnet associations**.

1. Select all of the Amazon EVS VLAN subnets.

1. Choose **Save associations**.

1. Open a terminal session.

1. Identify the Amazon EVS VLAN subnet IDs.

   ```
   aws ec2 describe-subnets
   ```

1. Associate your Amazon EVS VLAN subnets with a route table in your VPC.

   ```
   aws ec2 associate-route-table \
   --route-table-id rtb-0123456789abcdef0 \
   --subnet-id subnet-01234a1b2cde1234f
   ```

### Associate EIPs to the HCX public VLAN subnet (For HCX internet connectivity)
<a name="getting-started-eip-assoc"></a>

Follow these steps to associate Elastic IP address (EIPs) from the IPAM pool to the HCX public VLAN for HCX internet connectivity. You are required to associate at least two EIPs for the HCX Manager and HCX Interconnect (HCX-IX) appliances. Associate an additional EIP for each HCX network appliance that you need to deploy. You can have up to 13 EIPs from the IPAM pool associated with the HCX public VLAN.

**Important**  
HCX public internet connectivity fails if you do not associate at least two EIPs from the IPAM pool with an HCX public VLAN subnet.

**Note**  
Amazon EVS only supports associating EIPs with the HCX VLAN at this time.

**Note**  
You cannot associate the first two EIPs or the last EIP from the public IPAM CIDR block with the VLAN subnet. These EIPs are reserved as network, default gateway, and broadcast addresses. Amazon EVS throws a validation error if you attempt to associate these EIPs with the VLAN subnet.

------
#### [ Amazon EVS console ]

1. Go to the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. On the navigation menu, choose **Environments**.

1. Select the environment.

1. Under the **Networks and connectivity** tab, select the HCX public VLAN.

1. Choose **Associate EIP to VLAN**.

1. Select the Elastic IP address(es) to associate with the HCX public VLAN.

1. Choose **Associate EIPs**.

1. Check the **EIP associations** to confirm that the EIPs have been associated with the HCX public VLAN.

------
#### [  AWS CLI  ]

1. To associate an Elastic IP address with a VLAN, use the example `associate-eip-to-vlan` command.
   +  `environment-id` - The ID of your Amazon EVS environment.
   +  `vlan-name` - The name of the VLAN to associate with the Elastic IP address.
   +  `allocation-id` - The allocation ID of the Elastic IP address.

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
     +  `associationId` - The unique ID for this EIP association, used for disassociation.
     +  `allocationId` - The allocation ID of the associated Elastic IP address.
     +  `ipAddress` - The IP address assigned to the VLAN.

1. Repeat the step to associate additional EIPs.

------

### Configure transit gateway route tables and Direct Connect prefixes for on-premises connectivity (optional)
<a name="getting-started-config-tgw-assoc"></a>

If you are configuring on-premises network connectivity using Direct Connect or AWS Site-to-Site VPN with a transit gateway, you must update the transit gateway route tables with the VPC CIDRs created within the Amazon EVS environment. For more information, see [Transit gateway route tables in Amazon VPC Transit Gateways](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-route-tables.html).

If you are using AWS Direct Connect, you may need to also update your Direct Connect prefixes to send and receive updated routes from the VPC. For more information, see [Allows prefixes interactions for AWS Direct Connect gateways](https://docs.aws.amazon.com/directconnect/latest/UserGuide/allowed-to-prefixes.html).

## Retrieve VCF credentials and access VCF management appliances
<a name="access-vcf"></a>

Amazon EVS uses AWS Secrets Manager to create, encrypt, and store managed secrets in your account. These secrets contain the VCF credentials needed to install and access VCF management appliances such as vCenter Server, NSX, and SDDC Manager, as well as the ESX root password. For more information about retrieving secrets, see [Get secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the * AWS Secrets Manager User Guide*.

**Note**  
Amazon EVS does not provide managed rotation of your secrets. We recommend that you rotate your secrets regularly on a set rotation window to ensure that secrets are not long-lived.

After you have retrieved your VCF credentials from AWS Secrets Manager, you can use them to log into your VCF management appliances. For more information, see [Log in to the SDDC Manager User Interface](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/getting-started-with-sddc-manager-admin/log-in-to-the-sddc-manager-dashboard-admin.html) and [How to Use and Configure Your vSphere Client](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management-8-0/using-the-vsphere-client-host-management/working-with-the-vsphere-client-host-management.html#GUID-CE128B59-E236-45FF-9976-D134DADC8178-en) in the VMware product documentation.

### Configure the EC2 Serial Console (optional)
<a name="access-ec2-serial-console"></a>

By default, Amazon EVS enables the ESX Shell on newly deployed Amazon EVS hosts. This configuration allows access to the Amazon EC2 instance’s serial port through the EC2 serial console, which you can use to troubleshoot boot, network configuration, and other issues. The serial console does not require your instance to have any networking capabilities. With the serial console, you can enter commands to a running EC2 instance as if your keyboard and monitor are directly attached to the instance’s serial port.

The EC2 serial console can be accessed using the EC2 console or the AWS CLI. For more information, see [EC2 Serial Console for instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console.html) in the *Amazon EC2 User Guide*.

**Note**  
The EC2 serial console is the only Amazon EVS supported mechanism to access the Direct Console User Interface (DCUI) to interact with an ESX host locally.

**Note**  
Amazon EVS disables remote SSH by default. For more information about enabling SSH to access the remote ESX Shell, see [Remote ESX Shell Access with SSH](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere-sdks-tools/8-0/getting-started-with-esxcli-8-0/running-host-management-commands-in-the-esxi-shell/remote-esxi-shell-access-with-ssh.html) in the VMware vSphere product documentation.

 **Connect to the EC2 Serial Console** 

To connect to the EC2 serial console and use your chosen tool for troubleshooting, certain prerequisite tasks must be completed. For more information, see [Prerequisites for the EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-serial-console-prerequisites.html) and [Connect to the EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-serial-console.html) in the *Amazon EC2 User Guide*.

**Note**  
To connect to the EC2 serial console, your EC2 instance state must be `running`. You can’t connect to the serial console if the instance is in the `pending`, `stopping`, `stopped`, `shutting-down`, or `terminated` state. For more information about instance state changes, see [Amazon EC2 instance state change](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-lifecycle.html) in the *Amazon EC2 User Guide*.

 **Configure access to the EC2 Serial Console** 

To configure access to the EC2 serial console, you or your administrator must grant serial console access at the account level and then configure IAM policies to grant access to your users. For Linux instances, you must also configure a password-based user on every instance so that your users can use the serial console for troubleshooting. For more information, see [Configure access to the EC2 Serial Console](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-access-to-serial-console.html) in the *Amazon EC2 User Guide*.

## Clean up
<a name="cleanup"></a>

Follow these steps to delete the AWS resources that were created.

### Delete the Amazon EVS hosts and environment
<a name="getting-started-cleanup-env-hosts"></a>

Follow these steps to delete the Amazon EVS hosts and environment. This action deletes the VMware VCF installation that runs in your Amazon EVS environment.

**Note**  
To delete an Amazon EVS environment, you must first delete all hosts within the environment. An environment cannot be deleted if there are hosts associated with the environment.

**Example**  

1. Go to the Amazon EVS console.

1. In the navigation pane, choose **Environment**.

1. Select the environment that contains the hosts to delete.

1. Select the **Hosts** tab.

1. Select the host and choose **Delete** within the **Hosts** tab. Repeat this step for each host in the environment.

1. At the top of the **Environments** page, choose **Delete** and then **Delete environment**.
**Note**  
Environment deletion also deletes the Amazon EVS VLAN subnets and AWS Secrets Manager secrets that Amazon EVS created. AWS resources that you create are not deleted. These resources may continue to incur costs.

1. If you have Amazon EC2 Capacity Reservations in place that you no longer require, ensure that you’ve canceled them. For more information, see [Cancel a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-release.html) in the *Amazon EC2 User Guide*.

1. Open a terminal session.

1. Identify the environment that contains the host to delete.

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

1. Delete the hosts from the environment. Below is a sample `aws evs delete-environment-host` request.
**Note**  
To be able to delete an environment, you must first delete all of the hosts that are contained in the environment.

   ```
   aws evs delete-environment-host \
   --environment-id env-abcde12345 \
   --host esx01
   ```

1. Repeat the previous steps to delete the remaining hosts in your environment.

1. Delete the environment.

   ```
   aws evs delete-environment --environment-id env-abcde12345
   ```
**Note**  
Environment deletion also deletes the Amazon EVS VLAN subnets and AWS Secrets Manager secrets that Amazon EVS created. Other AWS resources that you create are not deleted. These resources may continue to incur costs.

1. If you have Amazon EC2 Capacity Reservations in place that you no longer require, ensure that you’ve canceled them. For more information, see [Cancel a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-release.html) in the *Amazon EC2 User Guide*.

#### Delete IPAM resources (For HCX internet connectivity)
<a name="getting-started-cleanup-ipam"></a>

If you’ve configured HCX internet connectivity, follow these steps to delete your IPAM resources.

1. Release EIP allocations from the public IPAM pool. For more information, see [Release an allocation](https://docs.aws.amazon.com/vpc/latest/ipam/release-alloc-ipam.html) in the *VPC IP Address Manager User Guide*.

1. Deprovision the public IPv4 CIDR from the IPAM pool. For more information, see [Deprovision CIDRs from a pool](https://docs.aws.amazon.com/vpc/latest/ipam/depro-pool-cidr-ipam.html) in the *VPC IP Address Manager User Guide*.

1. Delete the public IPAM pool. For more information, see [Delete a pool](https://docs.aws.amazon.com/vpc/latest/ipam/delete-pool-ipam.html) in the *VPC IP Address Manager User Guide*.

1. Delete the IPAM. For more information, see [Delete an IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/delete-ipam.html) in the *VPC IP Address Manager User Guide*.

### Delete the VPC Route Server components
<a name="getting-started-cleanup-rs"></a>

For steps to delete the Amazon VPC Route Server components that you created, see [Route Server cleanup](https://docs.aws.amazon.com/vpc/latest/userguide/route-server-tutorial-cleanup.html) in the *Amazon VPC User Guide*.

### Delete the network access control list (ACL)
<a name="getting-started-cleanup-nacl"></a>

For steps to delete a network access control list, see [Delete a network ACL for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/delete-network-acl.html) in the *Amazon VPC User Guide*.

### Disassociate and delete subnet route tables
<a name="getting-started-cleanup-subnet-rt"></a>

For steps to disassociate and delete subnet route tables, see [Subnet route tables](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-route-tables.html) in the *Amazon VPC User Guide*.

### Delete subnets
<a name="getting-started-cleanup-subnets"></a>

Delete the VPC subnets, including the service access subnet. For steps to delete VPC subnets, see [Delete a subnet](https://docs.aws.amazon.com/vpc/latest/userguide/subnet-deleting.html) in the *Amazon VPC User Guide*.

**Note**  
If you’re using Route 53 for DNS, remove the inbound endpoints before you attempt to delete the service access subnet. Otherwise, you will not be able to delete the service access subnet.

**Note**  
Amazon EVS deletes the VLAN subnets on your behalf when the environment is deleted. Amazon EVS VLAN subnets can only be deleted when the environment is deleted.

### Delete the VPC
<a name="getting-started-cleanup-vpc"></a>

For steps to delete the VPC, see [Delete your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/delete-vpc.html) in the *Amazon VPC User Guide*.

## Next steps
<a name="getting-started-next-steps"></a>

Migrate your workloads to Amazon EVS using VMware Hybrid Cloud Extension (VMware HCX). For more information, see [Migrate workloads to Amazon EVS using VMware HCX](migrate-evs-hcx.md).