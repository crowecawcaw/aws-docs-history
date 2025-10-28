# Elastic IP addresses

An _Elastic IP address_ is a static IPv4 address designed for dynamic
cloud computing. An Elastic IP address is allocated to your AWS account, and is yours until
you release it. By using an Elastic IP address, you can mask the failure of an instance or
software by rapidly remapping the address to another instance in your account. Alternatively,
you can specify the Elastic IP address in a DNS record for your domain, so that your domain
points to your instance. For more information, see the documentation for your domain registrar.

An Elastic IP address is a public IPv4 address, which is reachable from the internet. If
you need to connect to an instance that does not have a public IPv4 address, you can
associate an Elastic IP address with your instance to enable communication with the
internet.

###### Contents

- [Elastic IP address pricing](#eip-pricing "#eip-pricing")
- [Elastic IP address basics](#eip-basics "#eip-basics")
- [Elastic IP address quota](#using-instance-addressing-limit "#using-instance-addressing-limit")
- [Associate an Elastic IP address with an instance](working-with-eips.md "working-with-eips.md")
- [Transfer an Elastic IP address between AWS accounts](transfer-EIPs-intro-ec2.md "transfer-EIPs-intro-ec2.md")
- [Release an Elastic IP address](using-instance-addressing-eips-releasing.md "using-instance-addressing-eips-releasing.md")
- [Create a reverse DNS record for email on Amazon EC2](Using_Elastic_Addressing_Reverse_DNS.md "Using_Elastic_Addressing_Reverse_DNS.md")

## Elastic IP address pricing

There is a charge for all Elastic IP addresses whether they are in use (allocated to a
resource, like an EC2 instance) or idle (created in your account but
unallocated).

AWS charges for all public IPv4 addresses, including public IPv4 addresses
associated with running instances and Elastic IP addresses. For more information, see the **Public IPv4 Address**
tab on the [Amazon VPC pricing page](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").

## Elastic IP address basics

The following are the basic characteristics of an Elastic IP address:

- An Elastic IP address is static; it does not change over time.
- An Elastic IP address is for use in a specific Region only, and cannot be
  moved to a different Region.
- An Elastic IP address comes from Amazon's pool of IPv4 addresses, or from a
  custom IPv4 address pool that you have brought to your AWS account. We do not
  support Elastic IP addresses for IPv6.
- To use an Elastic IP address, you first allocate one to your account, and then
  associate it with your instance or a network interface.
- When you associate an Elastic IP address with an instance, it is also associated
  with the instance's primary network interface. When you associate an Elastic IP
  address with a network interface that is attached to an instance, it is also
  associated with the instance.
- When you associate an Elastic IP address with an instance or its primary network interface, if the instance already has a public IPv4 address associated with it, that public IPv4 address is released back into Amazon's pool of public IPv4 addresses and the Elastic IP address is associated with the instance instead. You cannot reuse the public IPv4 address previously associated with the instance and you cannot convert that public IPv4 address to an Elastic IP address. For more information, see [Public IPv4 addresses](using-instance-addressing.md#concepts-public-addresses "using-instance-addressing.md#concepts-public-addresses").
- You can disassociate an Elastic IP address from a resource, and then associate it with a
  different resource. To avoid unexpected behavior, ensure that all active connections to the
  resource named in the existing association are closed before you make the change. After you
  have associated your Elastic IP address to a different resource, you can reopen your connections
  to the newly associated resource.
- A disassociated Elastic IP address remains allocated to your account until you
  explicitly release it. You are charged for all Elastic IP addresses in your
  account, regardless of whether they are associated or disassociated with an
  instance. For more information, see the **Public IPv4 Address**
  tab on the [Amazon VPC pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/") page.
- When you associate an Elastic IP address with an instance that previously had a public
  IPv4 address, the public DNS host name of the instance changes to match the
  Elastic IP address.
- We resolve a public DNS host name to the public IPv4 address or the Elastic IP
  address of the instance outside the network of the instance, and to the private
  IPv4 address of the instance from within the network of the instance.
- When you allocate an Elastic IP address from an IP address pool that you have brought to
  your AWS account, it does not count toward your Elastic IP address limits. For
  more information, see [Elastic IP address quota](#using-instance-addressing-limit "#using-instance-addressing-limit").
- When you allocate the Elastic IP addresses, you can associate the Elastic IP addresses
  with a network border group. This is the location from which we advertise the
  CIDR block. Setting the network border group limits the CIDR block to this
  group. If you do not specify the network border group, we set the border group
  containing all of the Availability Zones in the Region (for example,
  `us-west-2`).
- An Elastic IP address is for use in a specific network border group
  only.

## Elastic IP address quota

By default, all AWS accounts have a quota of five (5) Elastic IP addresses per Region,
because public (IPv4) internet addresses are a scarce public resource. We strongly
recommend that you use Elastic IP addresses primarily for their ability to remap the
address to another instance in the case of instance failure, and to use [DNS
hostnames](../../../vpc/latest/userguide/AmazonDNS-concepts.md#vpc-dns-hostnames "../../../vpc/latest/userguide/AmazonDNS-concepts.md#vpc-dns-hostnames") for all other inter-node communication.

If you think your architecture warrants additional Elastic IP addresses,
you can request a quota increase directly from the Service Quotas console. To request a quota
increase, choose **Request increase at account-level**. For more
information, see [Amazon EC2 service quotas](ec2-resource-limits.md "ec2-resource-limits.md").
