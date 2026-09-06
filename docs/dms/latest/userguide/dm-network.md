

# Setting up a network for homogeneous data migrations in AWS DMS
<a name="dm-network"></a>

With AWS DMS, you can create a serverless environment for homogeneous data migrations which uses networking connectivity model that relies on network interfaces. For each data migration, AWS DMS assigns a private IP within one of the subnets defined in the instance profile DMS subnet group. Additionally, a non-static public IP may be assigned if the instance profile is configured for public access. The subnets used in the instance profile should provide access to both source and target hosts, as defined in the data providers. This access can be within the local VPC or established through VPC peering, Direct Connect, VPN, etc.

Also, for ongoing data replication, you must set up interaction between your source and target databases. These configurations depend on the location of your source data provider and your network settings. The following sections provide descriptions of common network configurations.

**Topics**
+ [Configuring a network using a single virtual private cloud (VPC)](#dm-network-one-vpc)
+ [Configuring a network using different virtual private clouds (VPCs)](#dm-network-different-vpc)
+ [Using Direct Connect or a VPN to configure a network to a VPC](#dm-networking_Direct_Connect)
+ [Resolving domain endpoints using DNS](#dm-networking-resolving_endpoints)

## Configuring a network using a single virtual private cloud (VPC)
<a name="dm-network-one-vpc"></a>

In this configuration, AWS DMS connects to your source and target data providers within the private network.

**To configure a network when your source and target data providers are in the same VPC**

1. Create the subnet group in the AWS DMS console with the VPC and subnets that your source and target data providers use. For more information, see [Creating a subnet group](subnet-group.md).

1. Create the instance profile in the AWS DMS console with the VPC and the subnet group that you created. Also, choose VPC security groups that your source and target data providers use. For more information, see [Creating instance profiles](instance-profiles.md).

1. Ensure that the security group used for the source and target database allows connections from the security group attached to instance profile used by data migration or CIDR block of subnets, specified in replication subnet group.

This configuration doesn't require you to use the public IP address for data migrations.

## Configuring a network using different virtual private clouds (VPCs)
<a name="dm-network-different-vpc"></a>

In this configuration, AWS DMS uses a private network to connect to your source or target data provider. For another data provider, AWS DMS uses a public network. Depending on which data provider you have in the same VPC as your instance profile, choose one of the following configurations.

### To connect through a private network
<a name="dm-network-different-vpc.privatenetwork"></a>

1. Create the subnet group in the AWS DMS console with the VPC and subnets that your source data provider uses. For more information, see [Creating a subnet group](subnet-group.md).

1. Create the instance profile in the AWS DMS console with the VPC and the subnet group that you created. Also, choose VPC security groups that your source data provider uses. For more information, see [Creating instance profiles](instance-profiles.md).

1. Configure VPC peering connection between source and target database VPCs. For more information see, [Work with VPC peering connections](https://docs.aws.amazon.com/vpc/latest/peering/working-with-vpc-peering.html).

1. Make sure to enable DNS resolution for both directions if you plan to use endpoints instead of private IPs directly. For more information see, [Enable DNS resolution for a VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/vpc-peering-dns.html).

1. Allow access from the CIDR block of source database’s VPC for target database security group. For more information, see [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html).

1. Allow access from the CIDR block of target database’s VPC for target database security group. For more information, see [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html).

### To connect through a Public network
<a name="dm-network-different-vpc.publicnetwork"></a>

If your database accepts connections from any address:

1. Create the subnet group in the AWS DMS console with the VPC and public subnets. For more information, see [Creating a subnet group](subnet-group.md).

1. Create the instance profile in the AWS DMS console with the VPC and the subnet group that you created. Set the **Publicly Available** option to **On** for the instance profile.

If you require a persistent public IP address that can be associated to the data migration:

1. Create the subnet group in the AWS DMS console with the VPC and private subnets. For more information, see [Creating a subnet group](subnet-group.md).

1. Create the instance profile in the AWS DMS console with the VPC and the subnet group that you created. Set the **Publicly Available** option to **Off** for the instance profile.

1. Setup NAT Gateway. For more information see [Work with NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-working-with.html).

1. Setup Routing table for NAT gateway. For more information see [NAT gateway use cases](https://docs.aws.amazon.com/vpc/latest/userguide/nat-gateway-scenarios.html).

1. Allow access from the public IP address of your NAT Gateway in your database security group. For more information, see [Controlling access with security groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.RDSSecurityGroups.html).

## Using Direct Connect or a VPN to configure a network to a VPC
<a name="dm-networking_Direct_Connect"></a>

You can connect remote networks to your VPC through Direct Connect or VPN connections (software or hardware). These options enable you to extend your internal network into AWS Cloud and integrate existing on-premises services such as monitoring, authentication, security, and data systems with your AWS resources. For this configuration, your VPC security group must include a routing rule that directs traffic to a host capable of bridging VPC traffic to your on-premises VPN. This traffic can be designated using either your VPC CIDR range or specific IP addresses. The NAT host must have its own security group configured to allow traffic from your VPC CIDR range or security group into the NAT instance, ensuring seamless communication between your VPC and on-premises infrastructure. For more information, see [step 5](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-create-vpn-connection) for [Get started with AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html#vpn-create-vpn-connection) procedure in the AWS Site-to-Site VPN User Guide.

## Resolving domain endpoints using DNS
<a name="dm-networking-resolving_endpoints"></a>

For DNS resolution in AWS DMS homogeneous migrations, the service primarily uses the Amazon ECS DNS resolver to resolve domain endpoints. If you need additional DNS resolution capabilities, Amazon Route 53 Resolver is available as an alternative solution. For more information, see [Getting started with Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver-getting-started.html) in the Amazon Route 53 user guide. For more information, regarding configuring endpoint resolution using your on-premises name server with Amazon Route 53 Resolver, see [Using your own on-premises name server](CHAP_BestPractices.md#CHAP_BestPractices.Rte53DNSResolver).

**Note**  
If your data migration log shows the message "Initiating connection - Networking model: VPC Peering", refer to [VPC peering network configurations](vpc-peering.md) topic.