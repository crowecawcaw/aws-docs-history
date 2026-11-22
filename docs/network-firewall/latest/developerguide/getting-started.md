

# Getting started with AWS Network Firewall

AWS Network Firewall provides network traffic filtering protection for your Amazon Virtual Private Cloud VPCs. This chapter provides tutorials for getting started with Network Firewall using the AWS Management Console. You can also use Network Firewall API operations to create and manage your firewalls. For more information about working with Network Firewall API operations, see the [AWS Network Firewall API Reference](https://docs.aws.amazon.com/network-firewall/latest/APIReference/).

The first two tutorials create a firewall with the routed firewall capability, which preserves the client source IP address. Choose between them by the kind of firewall policy that you want to create. A Next Generation policy is recommended for new firewalls. For the differences between the two policy types, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md).
+ [Getting started with a Next Generation policy](getting-started-v2.md)
+ [Getting started with a Classic AWS Network Firewall policy](getting-started-classic.md)
+ [Getting started with a NAT/Proxy firewall](getting-started-proxy.md) – Create a NAT/Proxy firewall, which creates NAT gateways for you and acts as an explicit proxy. This tutorial has its own prerequisites, which are listed in the tutorial.

**Topics**
+ [Before you begin](#getting-started-prerequisites)
+ [Getting started with a Next Generation policy](getting-started-v2.md)
+ [Getting started with a Classic AWS Network Firewall policy](getting-started-classic.md)
+ [Getting started with a NAT/Proxy firewall](getting-started-proxy.md)

## Before you begin
<a name="getting-started-prerequisites"></a>

The routed firewall tutorials in this chapter walk you through configuring and implementing an AWS Network Firewall firewall for a VPC with a basic internet gateway architecture, like the one depicted at [Simple single zone architecture with an internet gateway using AWS Network Firewall](arch-single-zone-igw.md). 

To follow a routed firewall tutorial, you'll need a test VPC where you want to implement a network firewall. Additionally, you must know how to manage the subnets and route tables in your VPC. 
+ For information about managing subnets in your VPC, see [VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) in the *Amazon Virtual Private Cloud User Guide*. 
+ For information about managing route tables for your VPC, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon Virtual Private Cloud User Guide*. 

The test VPC that you use for a tutorial must have the following configuration in one Region: 
+ An internet gateway.
+ A customer subnet. 
+ Routing configured to send inbound traffic from the internet gateway to the subnet and to send the subnet's outbound traffic to the internet gateway. 
+ A second subnet to use as the firewall subnet. This subnet must not be used for other purposes and must have at least one available IP address. You'll select the Availability Zone and subnet ID when you create the firewall. 

If you have a different architecture that you'd like to add a firewall to, you can adjust the guidance in a tutorial accordingly. Network Firewall doesn't support some VPC architectures. For information, see [AWS Network Firewall example architectures with routing](architectures.md).