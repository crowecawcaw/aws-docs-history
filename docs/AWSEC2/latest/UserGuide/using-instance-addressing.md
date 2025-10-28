# Amazon EC2 instance IP addressing

Amazon EC2 and Amazon VPC support both the IPv4 and IPv6 addressing protocols. By default, Amazon VPC
uses the IPv4 addressing protocol; you can't disable this behavior. When you create a VPC,
you must specify an IPv4 CIDR block (a range of private IPv4 addresses). You can optionally
assign an IPv6 CIDR block to your VPC and assign IPv6 addresses from that block to instances
in your subnets.

When you launch an EC2 instance, you specify a VPC and a subnet. The instance receives a
private IPv4 address from the CIDR range of the subnet. You can optionally configure your
instances with public IPv4 addresses and IPv6 addresses. If EC2 instances in different VPCs
communicate using public IP addresses, the traffic stays in the AWS private global network
and does not traverse the public internet.

###### Contents

- [Private IPv4 addresses](#concepts-private-addresses "#concepts-private-addresses")
- [Public IPv4 addresses](#concepts-public-addresses "#concepts-public-addresses")
- [Public IPv4 address
  optimization](#concepts-public-ip-address-opt "#concepts-public-ip-address-opt")
- [IPv6 addresses](#ipv6-addressing "#ipv6-addressing")
- [Multiple IP addresses](#multiple-ip-addresses "#multiple-ip-addresses")
- [EC2 instance hostnames](#amazon-dns "#amazon-dns")
- [Link-local addresses](#link-local-addresses "#link-local-addresses")
- [Manage the IPv4 addresses for your EC2
  instances](working-with-ip-addresses.md "working-with-ip-addresses.md")
- [Manage the IPv6 addresses for your EC2
  instances](working-with-ipv6-addresses.md "working-with-ipv6-addresses.md")
- [Secondary IP addresses for your EC2
  instances](instance-secondary-ip-addresses.md "instance-secondary-ip-addresses.md")
- [Configure secondary private IPv4 addresses for Windows instances](config-windows-multiple-ip.md "config-windows-multiple-ip.md")

## Private IPv4 addresses

A private IPv4 address is an IP address that's not reachable over the Internet. You
can use private IPv4 addresses for communication between instances in the same VPC. For
more information about the standards and specifications of private IPv4 addresses, see
[RFC 1918](http://www.faqs.org/rfcs/rfc1918.html "http://www.faqs.org/rfcs/rfc1918.html"). We allocate
private IPv4 addresses to instances using DHCP.

###### Note

You can create a VPC with a publicly routable CIDR block that falls outside of the
private IPv4 address ranges specified in RFC 1918. However, for the purposes of this
documentation, we refer to private IPv4 addresses (or 'private IP addresses') as the
IP addresses that are within the IPv4 CIDR range of your VPC.

VPC subnets can be one of the following types:

- IPv4-only subnets – You can only create resources in these subnets with
  IPv4 addresses assigned to them.
- IPv6-only subnets – You can only create resources in these subnets with
  IPv6 addresses assigned to them.
- IPv4 and IPv6 subnets – You can create resources in these subnets with
  either IPv4 or IPv6 addresses assigned to them.

When you launch an EC2 instance into an IPv4-only or dual stack (IPv4 and IPv6)
subnet, the instance receives a primary private IP address from the IPv4 address range
of the subnet. For more information, see [IP addressing](../../../vpc/latest/userguide/vpc-ip-addressing.md "../../../vpc/latest/userguide/vpc-ip-addressing.md") in the
_Amazon VPC User Guide_. If you don't specify a primary private IP
address when you launch the instance, we select an available IP address in the subnet's
IPv4 range for you. Each instance has a default network interface (index 0) that is
assigned the primary private IPv4 address. You can also specify additional private IPv4
addresses, known as _secondary private IPv4 addresses_. Unlike
primary private IP addresses, secondary private IP addresses can be reassigned from one
instance to another. For more information, see [Multiple IP addresses](#multiple-ip-addresses "#multiple-ip-addresses").

A private IPv4 address, regardless of whether it is a primary or secondary address,
remains associated with the network interface when the instance is stopped and started,
or hibernated and started, and is released when the instance is terminated.

## Public IPv4 addresses

A public IP address is an IPv4 address that's reachable from the Internet. You can use
public addresses for communication between your instances and the Internet.

When you launch an instance in a default VPC, we assign it a public IP address by
default. When you launch an instance into a nondefault VPC, the subnet has an attribute
that determines whether instances launched into that subnet receive a public IP address
from the public IPv4 address pool. By default, we don't assign a public IP address to
instances launched in a nondefault subnet.

You can control whether your instance receives a public IP address as follows:

- Modify the public IP addressing attribute of your
  subnet. For more information, see [Modify the public IPv4 addressing
  attribute for your subnet](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md") in the
  _Amazon VPC User Guide_.
- Enable or disable the public IP addressing feature
  during launch. This overrides the subnet's public IP addressing
  attribute. For more information, see [Assign a public IPv4 address at launch](working-with-ip-addresses.md#public-ip-addresses "working-with-ip-addresses.md#public-ip-addresses").
- Unassign a public IP address from your instance after
  launch. For more information, see [Manage the IP addresses for your network interface](managing-network-interface-ip-addresses.md "managing-network-interface-ip-addresses.md").

A public IP address is assigned to your instance from Amazon's pool of public IPv4
addresses, and is not associated with your AWS account. When a public IP address is
disassociated from your instance, it is released back into the public IPv4 address pool,
and you cannot reuse it.

We release the public IP address from your instance and assign a new one in the
following cases:

- We release the public IP address when the instance is stopped, hibernated, or
  terminated. We assign a new public IP address when you start your stopped or
  hibernated instance.
- We release the public IP address when you associate an Elastic IP address with
  the instance. We assign a new public IP address when you disassociate the
  Elastic IP address from your instance.
- If we release the public IP address of your instance and it has a secondary
  network interface, we do not assign a new public IP address.
- If we release the public IP address of your instance and it has a secondary
  private IP address that is associated with an Elastic IP address, we do not
  assign a new public IP address.

If you require a persistent public IP address that can be associated to and from
instances as you require, use an Elastic IP address instead.

If you use dynamic DNS to map an existing DNS name to a new instance's public IP
address, it might take up to 24 hours for the IP address to propagate through the
Internet. As a result, new instances might not receive traffic while terminated
instances continue to receive requests. To solve this problem, use an Elastic IP
address. You can allocate your own Elastic IP address, and associate it with your
instance. For more information, see [Elastic IP addresses](elastic-ip-addresses-eip.md "elastic-ip-addresses-eip.md").

If you are using Amazon VPC IP Address Manager (IPAM), you can get a contiguous block of public IPv4
addresses from AWS and use it to allocate Elastic IP addresses to AWS resources.
Using contiguous IPv4 address blocks can significantly reduce management overhead for
security access control lists and simplify IP address allocation and tracking for
enterprises scaling on AWS. For more information, see [Allocate sequential Elastic IP
addresses from an IPAM pool](../../../vpc/latest/ipam/tutorials-eip-pool.md "../../../vpc/latest/ipam/tutorials-eip-pool.md") in the
_Amazon VPC IPAM User Guide_.

###### Considerations

- AWS charges for all public IPv4 addresses, including public IPv4 addresses
  associated with running instances and Elastic IP addresses. For more information, see the **Public IPv4 Address**
  tab on the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").
- Instances that access other instances through their public NAT IP address are
  charged for regional or Internet data transfer, depending on whether the
  instances are in the same Region.

## Public IPv4 address

optimization

AWS charges for all public IPv4 addresses, including public IPv4 addresses
associated with running instances and Elastic IP addresses. For more information, see the **Public IPv4 Address**
tab on the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

The following list contains actions you can take to optimize the number of public IPv4
addresses you use:

- Use an [elastic load balancer](../../../elasticloadbalancing/latest/userguide/load-balancer-getting-started.md "../../../elasticloadbalancing/latest/userguide/load-balancer-getting-started.md") to load balance traffic to your EC2 instances
  and [disable Auto-assign public IP on the primary ENI assigned
  to the instances](managing-network-interface-ip-addresses.md "managing-network-interface-ip-addresses.md"). Load balancers use a single public IPv4 address, so
  this reduces your public IPv4 address count. You may also want consolidate
  existing load balancers to further reduce the public IPv4 address count.
- If the only reason for using a NAT gateway is to SSH into an EC2 instance in a
  private subnet for maintenance or emergencies, consider using [EC2 Instance Connect Endpoint](connect-using-eice.md "connect-using-eice.md") instead. With
  EC2 Instance Connect Endpoint, you can connect to an instance from the internet without
  requiring the instance to have a public IPv4 address.
- If your EC2 instances are in a public subnet with public IP addresses
  allocated to them, consider moving the instances to a private subnet, removing
  the public IP addresses, and using a [public NAT gateway](../../../vpc/latest/userguide/vpc-nat-gateway.md "../../../vpc/latest/userguide/vpc-nat-gateway.md")
  to allow access to and from your EC2 instances. There are cost considerations
  for using NAT gateways. Use this calculation method to decide if NAT gateways
  are cost effective. You can get the `Number of public IPv4 addresses`
  required for this calculation by [creating an AWS Billing Cost and Usage Report](https://aws.amazon.com/blogs/networking-and-content-delivery/identify-and-optimize-public-ipv4-address-usage-on-aws/ "https://aws.amazon.com/blogs/networking-and-content-delivery/identify-and-optimize-public-ipv4-address-usage-on-aws/").

```
NAT gateway per hour + NAT gateway public IPs + NAT gateway transfer / Existing public IP cost
```

Where:

    + `NAT gateway per hour = $0.045 * 730 hours in a month * Number of
     Availability Zones the NAT gateways are in`
    + `NAT gateway public IPs = $0.005 * 730 hours in a month * Number
     of IPs associated with your NAT gateways`
    + `NAT gateway transfer = $0.045 * Number of GBs that will go
     through the NAT gateway in a month`
    + `Existing public IP cost = $0.005 * 730 hours in a month * Number
     of public IPv4 addresses`

If the total is less than 1, NAT gateways are cheaper than public IPv4
addresses.

- Use [AWS PrivateLink](../../../vpc/latest/userguide/endpoint-services-overview.md "../../../vpc/latest/userguide/endpoint-services-overview.md") to connect privately to AWS services or services
  hosted by other AWS accounts rather than using public IPv4 addresses and
  internet gateways.
- [Bring your own IP address range (BYOIP) to
  AWS](ec2-byoip.md "ec2-byoip.md") and use the range for public IPv4 addresses rather than using
  Amazon-owned public IPv4 addresses.
- Turn off [auto-assign public IPv4
  address for instances launched into subnets](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md"). This option is
  generally disabled by default for VPCs when you create a subnet, but you should
  check your existing subnets to ensure it’s disabled.
- If you have EC2 instances that do not need public IPv4 addresses, [check that the network
  interfaces attached to your instances have Auto-assign
  public IP disabled](managing-network-interface-ip-addresses.md "managing-network-interface-ip-addresses.md").
- [Configure
  accelerator endpoints in AWS Global Accelerator](../../../global-accelerator/latest/dg/about-endpoints.md "../../../global-accelerator/latest/dg/about-endpoints.md") for EC2 instances in private
  subnets to enable internet traffic to flow directly to the endpoints in your
  VPCs without requiring public IP addresses. You can also [bring your own addresses to AWS Global Accelerator](../../../global-accelerator/latest/dg/using-byoip.md "../../../global-accelerator/latest/dg/using-byoip.md") and use your own IPv4
  addresses for your accelerator’s static IP addresses.

## IPv6 addresses

IPv6 addresses are globally unique and can be configured to remain private or
reachable over the Internet. Both public and private IPv6 addressing is available in
AWS:

- **Private IPv6**: AWS considers private IPv6
  addresses those that are not advertised and cannot be advertised on the Internet
  from AWS.
- **Public IPv6**: AWS considers public IPv6
  addresses those that are advertised on the Internet from AWS.

For more information about public and private IPv6 addresses, see [IPv6
addresses](../../../vpc/latest/userguide/vpc-ip-addressing.md#vpc-ipv6-addresses "../../../vpc/latest/userguide/vpc-ip-addressing.md#vpc-ipv6-addresses") in the _Amazon VPC User Guide_.

All instance types support IPv6 addresses except for the following:
C1, M1, M2, M3, and T1.

Your EC2 instances receive an IPv6 address if an IPv6 CIDR block is associated with
your VPC and subnet, and if one of the following is true:

- Your subnet is configured to automatically assign an IPv6 address to an
  instance during launch. For more information, see [Modify the IP addressing
  attributes of your subnet](../../../vpc/latest/userguide/subnet-public-ip.md "../../../vpc/latest/userguide/subnet-public-ip.md").
- You assign an IPv6 address to your instance during launch.
- You assign an IPv6 address to the primary network interface of your instance
  after launch.
- You assign an IPv6 address to a network interface in the same subnet, and
  attach the network interface to your instance after launch.

When your instance receives an IPv6 address during launch, the address is associated
with the primary network interface (index 0) of the instance. You can manage the IPv6
addresses for your instances primary network interface as follows:

- Assign and unassign IPv6 addresses from the network interface. The number of
  IPv6 addresses you can assign to a network interface and the number of network
  interfaces you can attach to an instance varies per instance type. For more
  information, see [Maximum IP addresses per network interface](AvailableIpPerENI.md "AvailableIpPerENI.md").
- Enable a primary IPv6 address. A primary IPv6 address enables you to avoid
  disrupting traffic to instances or ENIs. For more information, see [Create a network interface for your EC2 instance](create-network-interface.md "create-network-interface.md") or [Manage the IP addresses for your network interface](managing-network-interface-ip-addresses.md "managing-network-interface-ip-addresses.md").

An IPv6 address persists when you stop and start, or hibernate and start, your
instance, and is released when you terminate your instance. You cannot reassign an IPv6
address while it's assigned to another network interface—you must first unassign
it.

You can control whether instances are reachable via their IPv6 addresses by
controlling the routing for your subnet or by using security group and network ACL
rules. For more information, see [Internetwork traffic privacy](../../../IAM/latest/UserGuide/access.md "../../../IAM/latest/UserGuide/access.md") in the
_Amazon VPC User Guide_.

For more information about reserved IPv6 address ranges, see [IANA IPv6 Special-Purpose Address Registry](http://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml "http://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml") and [RFC4291](https://tools.ietf.org/html/rfc4291 "https://tools.ietf.org/html/rfc4291").

## Multiple IP addresses

You can specify multiple private IPv4 and IPv6 addresses for your instances. The
number of network interfaces and private IPv4 and IPv6 addresses that you can specify
for an instance depends on the instance type. For more information, see [Maximum IP addresses per network interface](AvailableIpPerENI.md "AvailableIpPerENI.md").

###### Use cases

- Host multiple websites on a single server by using multiple SSL certificates
  on a single server and associating each certificate with a specific IP
  address.
- Operate network appliances, such as firewalls or load balancers, that have
  multiple IP addresses for each network interface.
- Redirect internal traffic to a standby instance in case your instance fails,
  by reassigning the secondary IP address to the standby instance.

###### How multiple IP addresses work

- You can assign a secondary private IPv4 address to any network
  interface.
- You can assign multiple IPv6 addresses to a network interface that's in a
  subnet that has an associated IPv6 CIDR block.
- You must choose a secondary IPv4 address from the IPv4 CIDR block range of the
  subnet for the network interface.
- You must choose IPv6 addresses from the IPv6 CIDR block range of the subnet
  for the network interface.
- You associate security groups with network interfaces, not individual IP
  addresses. Therefore, each IP address you specify in a network interface is
  subject to the security group of its network interface.
- Multiple IP addresses can be assigned and unassigned to network interfaces
  attached to running or stopped instances.
- Secondary private IPv4 addresses that are assigned to a network interface can
  be reassigned to another one if you explicitly allow it.
- An IPv6 address cannot be reassigned to another network interface; you must
  first unassign the IPv6 address from the existing network interface.
- When assigning multiple IP addresses to a network interface using the command
  line tools or API, the entire operation fails if one of the IP addresses can't
  be assigned.
- Primary private IPv4 addresses, secondary private IPv4 addresses, Elastic IP
  addresses, and IPv6 addresses remain with a secondary network interface when it
  is detached from an instance or attached to an instance.
- Although you can't detach the primary network interface from an instance, you
  can reassign the secondary private IPv4 address of the primary network interface
  to another network interface.

For more information, see [Secondary IP addresses for your EC2
instances](instance-secondary-ip-addresses.md "instance-secondary-ip-addresses.md").

## EC2 instance hostnames

When you create an EC2 instance, AWS creates a hostname for that instance. For more
information on the types of hostnames and how they're provisioned by AWS, see [EC2 instance hostnames and domains](ec2-instance-naming.md "ec2-instance-naming.md"). Amazon provides
a DNS server that resolves Amazon-provided hostnames to IPv4 and IPv6 addresses. The
Amazon DNS server is located at the base of your VPC network range plus two. For more
information, see [DNS attributes for your
VPC](../../../vpc/latest/userguide/vpc-dns.md "../../../vpc/latest/userguide/vpc-dns.md") in the _Amazon VPC User Guide_.

## Link-local addresses

Link-local addresses are well-known, non-routable IP addresses. Amazon EC2 uses addresses
from the link-local address space to provide services that are accessible only from an
EC2 instance. These services do not run on the instance, they run on the underlying
host. When you access the link-local addresses for these services, you're communicating
with either the Xen hypervisor or the Nitro controller.

###### Link-local address ranges

- IPv4 – 169.254.0.0/16 (169.254.0.0 to 169.254.255.255)
- IPv6 – fe80::/10

###### Services that you access using link-local addresses

- [Instance Metadata
  Service](instancedata-data-retrieval.md "instancedata-data-retrieval.md")
- [Amazon Route 53 Resolver](../../../vpc/latest/userguide/vpc-dns.md#AmazonDNS "../../../vpc/latest/userguide/vpc-dns.md#AmazonDNS") (also
  known as the Amazon DNS server)
- [Amazon Time Sync Service](set-time.md "set-time.md")
- [AWS KMS servers](common-messages.md#activate-windows "common-messages.md#activate-windows")
