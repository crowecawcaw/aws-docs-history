

# High-level steps for implementing AWS Network Firewall

To install and use an AWS Network Firewall firewall in your Amazon Virtual Private Cloud VPC, you configure the firewall components and your VPC's subnets and route tables in the following high-level steps. These steps are for a firewall with the routed firewall capability. For a NAT/Proxy firewall, see [Getting started with a NAT/Proxy firewall](getting-started-proxy.md).
+ **Configure the primary VPC subnets for your firewall endpoints** – In the primary VPC where you use the firewall, in each Availability Zone where you want a firewall endpoint, create a subnet specifically for use by Network Firewall. A firewall endpoint can't protect applications that run in the same subnet, so reserve these subnets for exclusive use by the firewall. The subnets that you use for your primary firewall endpoints must belong to a single AWS Region and must be in different Availability Zones within the Region. 

  Network Firewall is available in the Regions listed at [AWS service endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html). 

  For information about managing subnets in your VPC, see [VPCs and subnets](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html) in the *Amazon Virtual Private Cloud User Guide*. 
+ **Create the firewall** – Create a Network Firewall firewall and provide it with the specifications for each of your firewall subnets. Network Firewall creates a firewall endpoint in each subnet that you specify, available to monitor and protect the resources for the subnets whose traffic you send through it. 
+ **Configure the firewall policy** – Define the firewall policy for your firewall by specifying its rule groups and other behavior that you want the firewall to provide. 
+ **Modify your VPC route tables to include the firewall** – Using Amazon VPC ingress routing enhancements, change your routing tables to route traffic through the Network Firewall firewall. These changes must insert the firewall between the subnets that you want to protect and outside locations. The exact routing that you need to do depends on your architecture and its components. 

  For information about managing route tables for your VPC, see [Route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html) in the *Amazon Virtual Private Cloud User Guide*. 
**Note**  
These route table changes apply to a routed firewall. For a NAT/Proxy firewall, you don't configure route tables to send explicit proxy traffic to the firewall. Instead, you specify a VPC when you create the firewall, and Network Firewall creates the NAT gateway and firewall endpoint in that VPC for you. Clients send HTTP and HTTPS requests directly to the firewall's proxy hostname.  
Route configuration isn't required for explicit proxy traffic. Non-proxy traffic that you want the NAT/Proxy firewall to inspect still reaches the firewall endpoint through your VPC route tables. For more information, see [NAT/Proxy firewall in AWS Network Firewall](nfw-proxy.md).

After you implement a firewall, you can expand its protections to additional VPCs and to multiple subnets within a single Availability Zone for any VPC. To do this, you manage the VPCs, subnets, and route tables as described in the previous high level steps, but you create the firewall endpoints in VPC endpoint associations, using the firewall that you've already defined. For more information about managing firewalls and VPC endpoint associations, see [Firewalls and firewall endpoints in AWS Network Firewall](firewalls.md).