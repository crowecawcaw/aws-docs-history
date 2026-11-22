

# Requirements and considerations for a NAT/Proxy firewall

Before you create a NAT/Proxy firewall, review the following requirements and considerations.

**VPC**  
A NAT/Proxy firewall is a VPC firewall. Network Firewall creates the firewall's NAT gateways and firewall endpoints in one VPC, which you can't change after you create the firewall. You can't attach a NAT/Proxy firewall to a transit gateway.

**Subnets**  
In each Availability Zone that you want the firewall to run in, you need two subnets:  
+ A *NAT subnet*, where Network Firewall creates the NAT gateway. For a public NAT gateway, this subnet needs a route to an internet gateway.
+ A *firewall endpoint subnet*, where Network Firewall creates the firewall endpoint. This subnet must be in the same Availability Zone as the NAT subnet, and it can't be the NAT subnet or the firewall endpoint subnet of another Availability Zone. Use a subnet that's dedicated to the firewall endpoint. For information about firewall endpoint subnets, see [VPC subnets](vpc-config-subnets.md).
Each NAT gateway and firewall endpoint pair must be in a different Availability Zone. The firewall can have only one NAT gateway and one firewall endpoint in each Availability Zone.

**NAT gateway connectivity type and IP addresses**  
You choose one connectivity type for all of the firewall's NAT gateways:  
+ **Public** – The NAT gateways use Elastic IP addresses to reach the internet. Allocate at least one Elastic IP address for each NAT gateway, and pick one available private IP address from the NAT subnet for each Elastic IP address. The Elastic IP addresses must not be associated with another resource. For information, see [Elastic IP addresses](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-eips.html) in the *Amazon Virtual Private Cloud User Guide*.
+ **Private** – The NAT gateways use only private IP addresses to reach other VPCs or your on-premises network. Pick at least one available private IP address from each NAT subnet. The first address that you specify is the NAT gateway's primary address.
Each NAT gateway can have up to 8 IP addresses. For a public NAT gateway, an Elastic IP address and its paired private IP address count as one address. Private IP addresses must be in the NAT subnet's IPv4 CIDR block. AWS reserves the first four IP addresses and the last IP address in each subnet, so you can't use those. You can't specify the same Elastic IP address or private IP address more than once in a request.  
For information about Amazon VPC NAT gateways, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon Virtual Private Cloud User Guide*.

**Settings that you can't change after you create the firewall**  
The firewall capability, the VPC, the NAT gateway connectivity type and IP addresses, the certificate and custom hostname, and the **Enable NAT on non-proxy traffic** setting are fixed when you create the firewall. You can change the proxy listener ports, add and remove Availability Zones, associate a different firewall policy, and change the other firewall settings that are described in [Firewall settings in AWS Network Firewall](firewall-settings.md).

**Firewall creation is all or nothing**  
If Network Firewall can't create the NAT gateway in an Availability Zone when it creates the firewall, that Availability Zone shows a failed status with the error message from Amazon EC2, and the whole firewall shows a failed status, even if other Availability Zones are ready. Common causes are a NAT gateway or Elastic IP address quota, an Elastic IP address that's already in use, and invalid parameters. To recover, delete the firewall and create it again. When you delete a firewall that failed to create, Network Firewall also deletes the NAT gateways that it created for that firewall. For information, see [Troubleshooting a NAT/Proxy firewall in AWS Network Firewall](troubleshooting-nfw-proxy.md).

**Permissions**  
Network Firewall creates, attaches, and detaches the NAT gateways and associates Route 53 private hosted zones using your own credentials. Your IAM policies, and any service control policies that apply to your account, must allow these actions in addition to the Network Firewall actions. For information about the required permissions, see [Permissions for a NAT/Proxy firewall](nfw-proxy-permissions.md).

**Resilience**  
The proxy hostname resolves only to the firewall endpoint in the client's own Availability Zone, and there's no failover to another Availability Zone. For resilience, run the firewall in more than one Availability Zone, and run clients in each of those Availability Zones.