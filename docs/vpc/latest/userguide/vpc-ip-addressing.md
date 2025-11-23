# IP addressing for your VPCs and subnets

IP addresses enable resources in your VPC to communicate with each other, and with resources
over the internet.

Classless Inter-Domain Routing (CIDR) notation is a way to represent an IP address and
its network mask. The format of these addresses is as follows:

- An individual IPv4 address is 32 bits, with 4 groups of up to 3 decimal digits, 0-255.
  For example, 10.0.1.0.
- An IPv4 CIDR block has an IPv4 address followed by a slash and a number from 0 to 32.
  For example, 10.0.0.0/16 represents 65,536 IPv4 addresses from 10.0.0.0 to 10.0.255.255.
- An individual IPv6 address is 128 bits, with 8 segments of 4 hexadecimal digits. For
  example, 2001:0db8:85a3:0000:0000:8a2e:0370:7334. It is not necessary to include the leading
  zeros in a segment. You can also replace consecutive all-zero segments with double colons
  (::) one time in an address. Therefore, the example address can be compressed as
  2001:db8:85a3::8a2e:370:7334.
- An IPv6 CIDR block has an IPv6 address that ends with all-zero segments, with the
  all-zero segments replaced by a double colon, followed by a slash and a number from
  0 to 128. For example, 2001:db8:1234:1a00::/56 represents 2^72 IPv6 addresses from
  2001:db8:1234:1a00:0000:0000:0000:0000 to 2001:db8:1234:1aff:ffff:ffff:ffff:ffff.
  For more information, see [What is CIDR?](https://aws.amazon.com/what-is/cidr/ "https://aws.amazon.com/what-is/cidr/")

###### Contents

- [Private IPv4 addresses](#vpc-private-ipv4-addresses "#vpc-private-ipv4-addresses")
- [Public IPv4 addresses](#vpc-public-ipv4-addresses "#vpc-public-ipv4-addresses")
- [IPv6 addresses](#vpc-ipv6-addresses "#vpc-ipv6-addresses")
- [Use your own IP addresses](#vpc-using-own-ip-address "#vpc-using-own-ip-address")
- [Use Amazon VPC IP Address Manager](#vpc-using-ipam "#vpc-using-ipam")
- [VPC CIDR blocks](vpc-cidr-blocks.md "vpc-cidr-blocks.md")
- [Subnet CIDR blocks](subnet-sizing.md "subnet-sizing.md")
- [Compare IPv4 and IPv6](ipv4-ipv6-comparison.md "ipv4-ipv6-comparison.md")
- [Managed prefix lists](managed-prefix-lists.md "managed-prefix-lists.md")
- [AWS IP address ranges](aws-ip-ranges.md "aws-ip-ranges.md")
- [IPv6 support for your VPC](vpc-migrate-ipv6.md "vpc-migrate-ipv6.md")
- [IPv6 support on AWS](aws-ipv6-support.md "aws-ipv6-support.md")

## Private IPv4 addresses

Private IPv4 addresses (also referred to as _private IP addresses_ in
this topic) are not reachable over the internet, and can be used for communication
between the instances in your VPC. When you launch an instance into a VPC, a primary
private IP address from the IPv4 address range of the subnet is assigned to the primary
network interface (for example, eth0) of the instance. Each instance is also given a private
(internal) DNS hostname that resolves to the private IP address of the instance.
The hostname can be of two types: resource-based or IP-based. For more information,
see [EC2 instance naming](../../../AWSEC2/latest/UserGuide/ec2-instance-naming.md "../../../AWSEC2/latest/UserGuide/ec2-instance-naming.md"). If you
don't specify a primary private IP address, we select an available IP address in the
subnet range for you. For more information about network interfaces, see [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the
_Amazon EC2 User Guide_.

You can assign additional private IP addresses, known as secondary private IP addresses,
to instances that are running in a VPC. Unlike a primary private IP address, you can reassign
a secondary private IP address from one network interface to another. A private IP address
remains associated with the network interface when the instance is stopped and restarted, and
is released when the instance is terminated. For more information about primary and secondary
IP addresses, see [Multiple IP Addresses](../../../AWSEC2/latest/UserGuide/MultipleIP.md "../../../AWSEC2/latest/UserGuide/MultipleIP.md") in the _Amazon EC2 User Guide_.

We refer to private IP addresses as the IP addresses that are within the IPv4 CIDR range
of the VPC. Most VPC IP address ranges fall within the private (non-publicly
routable) IP address ranges specified in RFC 1918; however, you can use publicly
routable CIDR blocks for your VPC. Regardless of the IP address range of your VPC,
we do not support direct access to the internet from your VPC's CIDR block,
including a publicly-routable CIDR block. You must set up internet access through a
gateway; for example, an internet gateway, virtual private gateway, a AWS Site-to-Site VPN connection,
or Direct Connect.

We never advertise the IPv4 address range of a subnet to the internet.

## Public IPv4 addresses

All subnets have an attribute that determines whether a network interface created in the
subnet automatically receives a public IPv4 address (also referred to as a _public IP address_ in this topic). Therefore, when you launch an
instance into a subnet that has this attribute enabled, a public IP address is assigned to the
primary network interface that's created for the instance. A public IP address is
mapped to the primary private IP address through network address translation (NAT).

###### Note

AWS charges for all public IPv4 addresses, including public IPv4 addresses
associated with running instances and Elastic IP addresses. For more information, see the **Public IPv4 Address**
tab on the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

You can control whether your instance receives a public IP address by doing the following:

- Modifying the public IP addressing attribute of your subnet. For more information, see
  [Modify the IP addressing attributes of your subnet](subnet-public-ip.md "subnet-public-ip.md").
- Enabling or disabling the public IP addressing feature during instance launch, which
  overrides the subnet's public IP addressing attribute.
- You can unassign a public IP address from your instance after launch by managing the IP addresses
  associated with a network interface. For more information, see [Manage IP addresses](../../../AWSEC2/latest/UserGuide/using-eni.md#managing-network-interface-ip-addresses "../../../AWSEC2/latest/UserGuide/using-eni.md#managing-network-interface-ip-addresses") in the _Amazon EC2 User Guide_.

A public IP address is assigned from Amazon's pool of public IP addresses; it's not
associated with your account. When a public IP address is disassociated from your instance,
it's released back into the pool, and is no longer available for you to use. In certain cases,
we release the public IP address from your instance, or assign it a new one. For more
information, see [Public IP
addresses](../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#concepts-public-addresses "../../../AWSEC2/latest/UserGuide/using-instance-addressing.md#concepts-public-addresses") in the _Amazon EC2 User Guide_.

If you require a persistent public IP address allocated to your account that can be
assigned to and removed from instances as you require, use an Elastic IP address
instead. For more information, see [Associate Elastic IP addresses with resources in your VPC](vpc-eips.md "vpc-eips.md").

If your VPC is enabled to support DNS hostnames, each instance that receives a public IP
address or an Elastic IP address is also given a public DNS hostname. We resolve a public DNS
hostname to the public IP address of the instance outside the instance network, and to the
private IP address of the instance from within the instance network. For more information, see
[DNS attributes for your VPC](vpc-dns.md "vpc-dns.md").

If you are using Amazon VPC IP Address Manager (IPAM), you can get a contiguous block of public IPv4 addresses from
AWS and use it to allocate sequential Elastic IP addresses to AWS resources. Using contiguous IPv4 address
blocks can significantly reduce management overhead for security access control lists and
simplify IP address allocation and tracking for enterprises scaling on AWS. For more information, see [Allocate sequential Elastic IP addresses from an IPAM pool](../ipam/tutorials-eip-pool.md "../ipam/tutorials-eip-pool.md") in the _Amazon VPC IPAM User Guide_.

## IPv6 addresses

As the internet continues to grow, so does the need for IP addresses. The most common
format for IP addresses is IPv4. The new format for IP addresses is IPv6, which provides a
larger address space than IPv4. IPv6 resolves the IPv4 address exhaustion issue and enables
you to connect more devices to the internet. The transition is gradual, but as IPv6 adoption
grows, you can simplify your networks and take advantage of IPv6 advanced capabilities for
better connectivity, performance, and security.

Many AWS services, such as Amazon EC2, Amazon S3, and Amazon CloudFront, offer either
dual-stack (IPv4 and IPv6) or IPv6-only support, allowing resources to be assigned IPv6
addresses and accessed over the IPv6 protocol and simplifying network configuration and
management for those customers adopting IPv6. Other services offer limited or partial
dual-stack and IPv6-only support.

For more information about services that support IPv6, see
[AWS services that support IPv6](aws-ipv6-support.md "aws-ipv6-support.md").

Note that some IPv6 addresses are reserved by the Internet Engineering Task Force.
For more information about reserved IPv6 address ranges, see
[IANA IPv6 Special-Purpose Address Registry](http://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml "http://www.iana.org/assignments/iana-ipv6-special-registry/iana-ipv6-special-registry.xhtml") and [RFC4291](https://tools.ietf.org/html/rfc4291 "https://tools.ietf.org/html/rfc4291").

###### Note

Both public and private IPv6 addressing is available in AWS. AWS defines
public IP addresses as those advertised on the internet from AWS, while private IP
addresses are not and cannot be advertised on the internet from AWS.

###### Contents

- [Public IPv6 addresses](#vpc-ipv6-addresses-public "#vpc-ipv6-addresses-public")
- [Private IPv6 addresses](#vpc-ipv6-addresses-private "#vpc-ipv6-addresses-private")

### Public IPv6 addresses

Amazon-provided IPv6 addresses are always advertised on the internet. They are
globally unique, and therefore reachable over the internet. You can control whether
resources such as EC2 instances are reachable using their IPv6 addresses by
controlling routing for your subnets, or by using security groups and network ACLs.

These are some of the ways you can prepare to use public IPv6 addresses for your
workloads:

- Create an IPAM with Amazon VPC IP Address Manager and provision an Amazon-owned
  public IPv6 address range to an IPAM address pool. For more information, see [Create IPv6
  pools](../ipam/intro-create-ipv6-pools.md "../ipam/intro-create-ipv6-pools.md") in the _Amazon VPC IPAM User Guide_.
- If you have an IPAM and you own a public IPv6 address range, bring some or all of
  the public IPv6 address range to IPAM and provision the public IPv6 address range to an
  IPAM address pool. For more information, see [Tutorial: Bring your IP addresses to
  IPAM](../ipam/tutorials-byoip-ipam.md "../ipam/tutorials-byoip-ipam.md") in the _Amazon VPC IPAM User Guide_.
- If you don't have an IPAM but you own a public IPv6 address range, bring some or all
  of the public IPv6 address range to AWS. For more information, see [Bring your own IP
  addresses (BYOIP) to Amazon EC2](../../../AWSEC2/latest/UserGuide/ec2-byoip.md "../../../AWSEC2/latest/UserGuide/ec2-byoip.md") in the
  _Amazon EC2 User Guide_.

When you are prepared to use public IPv6 addresses, you can assign public IPv6 addresses
to instances (see [IPv6 addresses](../../../AWSEC2/latest/UserGuide/working-with-ipv6-addresses.md "../../../AWSEC2/latest/UserGuide/working-with-ipv6-addresses.md") in the _Amazon EC2 User Guide_), you can allocate a public
IPv6 CIDR block to your VPC (see [Add or remove a CIDR block from your VPC](add-ipv4-cidr.md "add-ipv4-cidr.md"))
and associate the IPv6 CIDR block with your subnets (see [Modify the IP addressing attributes of your subnet](subnet-public-ip.md "subnet-public-ip.md")).

### Private IPv6 addresses

Private IPv6 addresses are IPv6 addresses that are not advertised and cannot be
advertised on the Internet from AWS.

You can use a private IPv6 address if you want your private networks to support IPv6 and
you have no intention of routing traffic from these addresses to the Internet. If you want
to connect to the internet from a resource that has a private IPv6 address, you can, but you
must route traffic through a resource in another subnet with a public IPv6 address to do so.

There are two types of private IPv6 addresses:

- **IPv6 ULA ranges**: IPv6 addresses as defined in [RFC4193](https://datatracker.ietf.org/doc/html/rfc4193 "https://datatracker.ietf.org/doc/html/rfc4193"). These address
  ranges always start with “fc” or “fd”, which makes them easily identifiable. Valid IPv6
  ULA space is anything under fd00::/8 that does not overlap with the Amazon reserved
  range fd00::/16.
- **IPv6 GUA ranges**: IPv6 addresses as defined in [RFC3587](https://datatracker.ietf.org/doc/html/rfc3587 "https://datatracker.ietf.org/doc/html/rfc3587"). The option to use
  IPv6 GUA ranges as private IPv6 addresses is disabled by default and must be enabled
  before you can use it. For more information, see [Enable provisioning private IPv6 GUA CIDRs](../ipam/enable-prov-ipv6-gua.md "../ipam/enable-prov-ipv6-gua.md") in the _Amazon VPC IPAM User Guide_.

Note the following:

- Private IPv6 addresses are only available through [Amazon VPC IP Address Manager
  (IPAM)](../ipam/what-it-is-ipam.md "../ipam/what-it-is-ipam.md"). IPAM discovers resources with IPv6 ULA and GUA addresses and monitors
  pools for overlapping IPv6 ULA and GUA address space.
- When you use private IPv6 GUA ranges, we require that you use IPv6 GUA ranges owned
  by you.
- Private IPv6 addresses are not and cannot be advertised on the internet by AWS. AWS does
  not allow direct egress to the public internet from a private IPv6 range even if there
  is an internet gateway or egress only internet gateway in the VPC. Private IPv6
  addresses are automatically dropped at the internet gateway edge ensuring that they are
  not routed publicly.
- AWS reserves the first 4 subnet private IPv6 addresses and the last one.
- Valid ranges for private IPv6 ULA are /9 to /60 starting with fd80::/9.
- If you have a private IPv6 GUA range allocated to a VPC, you cannot use public IPv6 GUA space
  that overlaps the private IPv6 GUA space in the same VPC.
- Communication between resources with private IPv6 ULA and GUA address ranges is supported
  (such as across Direct Connect, VPC peering, transit gateway, or VPN
  connections).
- You can use private IPv6 addresses with IPv6-only and dual-stack [VPC subnets](configure-subnets.md#subnet-ip-address-range "configure-subnets.md#subnet-ip-address-range"), [elastic
  load balancers](../../../elasticloadbalancing/latest/userguide/load-balancer-getting-started.md "../../../elasticloadbalancing/latest/userguide/load-balancer-getting-started.md") and [AWS Global Accelerator
  endpoints](../../../global-accelerator/latest/dg/about-endpoints.md "../../../global-accelerator/latest/dg/about-endpoints.md").
- There is no charge for private IPv6 addresses.

These are some of the ways you can prepare to use private IPv6 addresses for your
workloads:

- Create an IPAM with Amazon VPC IP Address Manager and provision a private IPv6
  _ULA_ range to an IPAM address pool. For more
  information, see [Create IPv6 pools](../ipam/intro-create-ipv6-pools.md "../ipam/intro-create-ipv6-pools.md") in the
  _Amazon VPC IPAM User Guide_.
- Create an IPAM with Amazon VPC IP Address Manager and provision a private IPv6
  _GUA_ range to an IPAM address pool. The option to
  use IPv6 GUA ranges as private IPv6 addresses is disabled by default and must be enabled
  on your IPAM before you can use it. For more information, see [Enable
  provisioning private IPv6 GUA CIDRs](../ipam/enable-prov-ipv6-gua.md "../ipam/enable-prov-ipv6-gua.md") in the
  _Amazon VPC IPAM User Guide_.

When you are prepared to use private IPv6 addresses, you can allocate a private IPv6
CIDR block from an IPAM pool to your VPC (see [Add or remove a CIDR block from your VPC](add-ipv4-cidr.md "add-ipv4-cidr.md")) and associate the IPv6 CIDR block with your subnets (see
[Modify the IP addressing attributes of your subnet](subnet-public-ip.md "subnet-public-ip.md")).

## Use your own IP addresses

You can bring part or all of your own public IPv4 address range or IPv6 address range
to your AWS account. You continue to own the address range, but AWS advertises it on the
internet by default. After you bring the address range to AWS, it appears in your
account as an address pool. You can create an Elastic IP address from your IPv4 address
pool, and you can associate an IPv6 CIDR block from your IPv6 address pool with a
VPC.

For more information, see [Bring your own IP
addresses (BYOIP)](../../../AWSEC2/latest/UserGuide/ec2-byoip.md "../../../AWSEC2/latest/UserGuide/ec2-byoip.md") in the _Amazon EC2 User Guide_.

## Use Amazon VPC IP Address Manager

Amazon VPC IP Address Manager (IPAM) is a VPC feature that makes it easier for you to
plan, track, and monitor IP addresses for your AWS workloads. You can use IPAM to allocate
IP address CIDRs to VPCs using specific business rules.

For more information, see [What is IPAM?](../ipam/what-it-is-ipam.md "../ipam/what-it-is-ipam.md") in the _Amazon VPC IPAM User Guide_.
