# IPv6 support for your VPC

If you have an existing VPC that supports IPv4 only, and resources in your subnet that are configured to use IPv4 only, you can add IPv6 support for your VPC and resources. Your VPC can operate in dual-stack mode — your resources can communicate over IPv4, or IPv6, or both. IPv4 and IPv6 communication are independent of each other.

You cannot disable IPv4 support for your VPC and subnets; this is the default IP
addressing system for Amazon VPC and Amazon EC2.

###### Considerations

- There is no migration path from IPv4-only subnets to IPv6-only subnets.
- This example assumes that you have an existing VPC with public and private
  subnets. For information about creating a new VPC for use with IPv6, see
  [Create a VPC](create-vpc.md "create-vpc.md").
- Before you begin using IPv6, ensure that you have read the features of IPv6
  addressing for Amazon VPC: [Compare IPv4 and IPv6](ipv4-ipv6-comparison.md "ipv4-ipv6-comparison.md").

###### Contents

- [Add IPv6 support for your VPC](vpc-migrate-ipv6-add.md "vpc-migrate-ipv6-add.md")
- [Example dual-stack VPC configuration](vpc-migrate-ipv6-example.md "vpc-migrate-ipv6-example.md")
