# Elastic IP address concepts and rules

To use an Elastic IP address, you first allocate it for use in your account. Then, you
can associate it with an instance or network interface in your VPC. Your Elastic IP
address remains allocated to your AWS account until you explicitly release it.

An Elastic IP address is a property of a network interface. You can associate an
Elastic IP address with an instance by updating the network interface attached to the
instance. The advantage of associating the Elastic IP address with the network interface
instead of directly with the instance is that you can move all the attributes of the
network interface from one instance to another in a single step. For more information,
see [Elastic network interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the
_Amazon EC2 User Guide_.

The following rules apply:

- An Elastic IP address can be associated with a single instance or network
  interface at a time.
- You can move an Elastic IP address from one instance or network interface to
  another.
- If you associate an Elastic IP address with the primary network interface of your
  instance, its current public IPv4 address (if it had one) is released to the
  public IP address pool. If you disassociate the Elastic IP address, the
  primary network interface is automatically assigned a new public IPv4 address
  within a few minutes. This doesn't apply if you've attached a second network
  interface to your instance.
- You're limited to five Elastic IP addresses. To help conserve them, you can
  use a NAT device. For more information, see [Connect to the internet or other networks using NAT devices](vpc-nat.md "vpc-nat.md").
- Elastic IP addresses for IPv6 are not supported.
- You can tag an Elastic IP address that's allocated for use in a VPC, however,
  cost allocation tags are not supported. If you recover an Elastic IP address,
  tags are not recovered.
- You can access an Elastic IP address from the internet when the security group
  and network ACL allow traffic from the source IP address. The reply traffic from
  within the VPC back to the internet requires an internet gateway. For more
  information, see [Security groups](vpc-security-groups.md "vpc-security-groups.md")
  and [Network ACLs](vpc-network-acls.md "vpc-network-acls.md").
- You can use any of the following options for the Elastic IP addresses:
  - Have Amazon provide the Elastic IP addresses. When you select this
    option, you can associate the Elastic IP addresses with a network border
    group. This is the location from which we advertise the CIDR block.
    Setting the network border group limits the CIDR block to this group.
  - Use your own IP addresses. For information about bringing your own IP
    addresses, see [Bring your own
    IP addresses (BYOIP)](../../../AWSEC2/latest/UserGuide/ec2-byoip.md "../../../AWSEC2/latest/UserGuide/ec2-byoip.md") in the*Amazon EC2 User Guide*.

- Public IPv4 addresses support cost allocation tags. If you apply tags to Elastic IP addresses, you can use those tags to track public IPv4 address costs in AWS Cost Explorer.

Before you can use tags as cost allocation tags, you must activate the tags. For more information, see [Activating user-defined cost allocation tags](../../../awsaccountbilling/latest/aboutv2/activating-tags.md "../../../awsaccountbilling/latest/aboutv2/activating-tags.md") in the _AWS Billing User Guide_. Note that after you create and apply user-defined tags to your resources, it can take up to 24 hours for the tag keys to appear on your cost allocation tags page for activation.

Once the cost allocation tags are activated...

    + For all public IPv4 addresses (including public IPv4 addresses assigned to EC2 instances and Elastic IP addresses) that are associated with an elastic network interface, you can view the costs associated with public IPv4 addresses in Cost Explorer by choosing **Usage type** > **PublicIPv4InUseAddress (Hrs)**.
    + If a tagged Elastic IP address is not associated with an ENI or is associated with a stopped resource (like a stopped EC2 instance), it's considered an idle IPv4 address. You can view the costs associated with idle IPv4 addresses in Cost Explorer by choosing **Usage type** > **PublicIPv4IdleAddress (Hrs)**.

For more information about Cost Explorer, see [Analyzing your costs with AWS Cost Explorer](../../../cost-management/latest/userguide/ce-what-is.md "../../../cost-management/latest/userguide/ce-what-is.md") in the _AWS Billing User Guide_.
Elastic IP addresses are regional. For more information about using Global Accelerator to provision
global IP addresses, see [Using
global static IP addresses instead of regional static IP addresses](../../../global-accelerator/latest/dg/about-accelerators.md "../../../global-accelerator/latest/dg/about-accelerators.md") in the
_AWS Global Accelerator Developer Guide_.

For more information about pricing for Elastic IP addresses, see _Public IPv4 address_ in [Amazon VPC Pricing](https://aws.amazon.com/vpc/pricing/ "https://aws.amazon.com/vpc/pricing/").
