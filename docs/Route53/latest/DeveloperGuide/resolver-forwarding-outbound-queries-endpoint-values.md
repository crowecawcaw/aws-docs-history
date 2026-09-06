

# Values that you specify when you create or edit outbound endpoints
<a name="resolver-forwarding-outbound-queries-endpoint-values"></a>

When you create or edit an outbound endpoint, you specify the following values:

**Outpost ID**  
If you are creating the endpoint for a VPC Resolver on an AWS Outposts VPC, this is the AWS Outposts ID.

**Endpoint name**  
A friendly name that lets you easily find an outbound endpoint on the dashboard.

**VPC in the *region-name* Region**  
All outbound DNS queries flow through this VPC on the way to your network.

**Security group for this endpoint**  
The ID of one or more security groups that you want to use to control access to this VPC. The security group that you specify must include one or more outbound rules. Outbound rules must allow TCP and UDP access on the port that you're using for DNS queries on your network. You can't change this value after you create an endpoint.   
Some security group rules will cause your connection to be tracked and potentially impact the maximum queries per second from outbound endpoint to your target name server. To avoid connection tracking caused by a security group, see [Untracked connections](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html#untracked-connections).  
For more information, see [Security groups for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) in the *Amazon VPC User Guide*.

**Endpoint type**  
The endpoint type can be either IPv4, IPv6, or dual-stack IP addresses. For a dual-stack endpoint, the endpoint has both IPv4 and IPv6 addresses that your DNS resolver on your network can forward DNS queries to.   
For security reasons, VPC Resolver denies direct IPv6 traffic access to the public internet for all dual-stack and IPv6 IP addresses by default. To enable this access, turn on **IPv6 internet access** when you create or edit the endpoint.

**IP addresses**  
The IP addresses in your VPC that you want VPC Resolver to forward DNS queries to on the way to resolvers on your network. These are not the IP addresses of the DNS resolvers on your network; you specify resolver IP addresses when you create the rules that you associate with one or more VPCs. You must specify a minimum of two IP addresses for redundancy.   
Resolver endpoint has a private IP address. These IP addresses will not change through the course of an endpoint's life.
Note the following:    
**Multiple Availability Zones**  
We recommend that you specify IP addresses in at least two Availability Zones. You can optionally specify additional IP addresses in those or other Availability Zones.  
**IP addresses and Amazon VPC elastic network interfaces**  
For each combination of Availability Zone, Subnet, and IP address that you specify, VPC Resolver creates an Amazon VPC elastic network interface. For the current maximum number of DNS queries per second per IP address in an endpoint, see [Quotas on Route 53 VPC Resolver](DNSLimitations.md#limits-api-entities-resolver). For information about pricing for each elastic network interface, see "Amazon Route 53" on the [Amazon Route 53 pricing page](https://aws.amazon.com/route53/pricing/).  
**Order of IP addresses**  
You can specify IP addresses in any order. When forwarding DNS queries, VPC Resolver doesn't choose IP addresses based on the order that the IP addresses are listed in.
For each IP address, specify the following values. Each IP address must be in an Availability Zone in the VPC that you specified in **VPC in the *region-name* Region**.    
**Availability Zone**  
The Availability Zone that you want DNS queries to pass through on the way to your network. The Availability Zone that you specify must be configured with a subnet.  
**Subnet**  
The subnet that contains the IP address that you want DNS queries to originate from on the way to your network. The subnet must have an available IP address.  
The subnet IP address must match the **Endpoint type**.  
We recommend using [VPC Resolver on AWS Outposts](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/outpost-resolver-getting-started.html) to create endpoints on AWS Outposts Racks.  
Outposts subnets with [Local Network Interface (LNI)](https://docs.aws.amazon.com/outposts/latest/server-userguide/local-network-interface.html) enabled are not compatible with VPC Resolver endpoints. If you enable LNI on a subnet that contains VPC Resolver endpoint elastic network interfaces (ENIs), those ENIs will stop functioning. For more information, see [Subnet compatibility for Resolver endpoints](best-practices-resolver-subnet-compatibility.md).  
**IP address**  
The IP address that you want DNS queries to originate from on the way to your network.  
Choose whether you want VPC Resolver to choose an IP address for you from among the available IP addresses in the specified subnet, or you want to specify the IP address yourself.  
If you choose to specify the IP address yourself, enter an IPv4 or IPv6 address, or both.

**Protocols**  
Endpoint protocol determines how data is transmitted from the outbound endpoint. Choose a protocol, or protocols, depending on the level of security needed.  
+ **Do53:** (Default) The data is relayed using the Route 53 VPC Resolver without additional encryption. While the data cannot be read by external parties, it can be viewed within the AWS networks.
+ **DoH:** The data is transmitted over an encrypted HTTPS session. DoH adds an added level of security where data can't be decrypted by unauthorized users, and can't be read by anyone except the intended recipient.
For an outbound endpoint you can apply the protocols as follows:  
+  Do53 and DoH in combination.
+ Do53 alone.
+ DoH alone.
+ None, which is treated as Do53.

**IPv6 internet access**  
Enable IPv6 internet access to allow the outbound endpoint to forward DNS queries to public IPv6 targets through an internet gateway. When enabled, the endpoint elastic network interfaces (ENIs) can send DNS queries to public IPv6 resolvers.  
When you enable IPv6 internet access, use network controls like security groups, NACLs, or egress-only internet gateways to protect the endpoint ENIs from unsolicited ingress traffic. Be aware that some network controls can affect DNS query throughput due to connection tracking. For more information, see [Amazon EC2 security group connection tracking](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/security-group-connection-tracking.html) and [Resolver endpoint scaling](best-practices-resolver-endpoint-scaling.html).

**Tags**  
Specify one or more keys and the corresponding values. For example, you might specify **Cost center** for **Key** and specify **456** for **Value**.