# Enable provisioning private IPv6 GUA CIDRs

If you want your private networks to support IPv6 and have no intention of routing traffic
from these addresses to the internet, you can provision a private IPv6 ULA or GUA range to
an IPAM pool in a private scope.

For important details about private IPv6 addressing, see [Private
IPv6 addresses](../userguide/vpc-ip-addressing.md#vpc-ipv6-addresses-private "../userguide/vpc-ip-addressing.md#vpc-ipv6-addresses-private") in the _Amazon VPC User Guide_.

There are two types of private IPv6 addresses:

- **IPv6 ULA ranges**: IPv6 addresses as defined in [RFC4193](https://datatracker.ietf.org/doc/html/rfc4193 "https://datatracker.ietf.org/doc/html/rfc4193"). These
  address ranges will always start with “fc” or “fd”, which makes them easily
  identifiable. Valid IPv6 ULA space is anything under fd00::/8 that does not overlap
  with the Amazon reserved range fd00::/16.
- **IPv6 GUA ranges**: IPv6 addresses as defined in
  [RFC3587](https://datatracker.ietf.org/doc/html/rfc3587 "https://datatracker.ietf.org/doc/html/rfc3587"). The
  option to use IPv6 GUA ranges as private IPv6 addresses is disabled by default and
  must be enabled before you can use it.
  To use an IPv6 ULA address ranges, you choose the IPv6 option when you provision a CIDR to
  an IPAM pool and enter the IPv6 ULA range. To use your own IPv6 GUA ranges as private IPv6
  addresses, however, you must first complete the steps in this section. The option is
  disabled by default.

###### Note

- When you use private IPv6 GUA ranges, we require that you use IPv6 GUA ranges
  owned by you.
- IPAM discovers resources with IPv6 ULA and GUA addresses and monitors pools
  for overlapping IPv6 ULA and GUA address space.
- If you want to connect to the internet from a resource that has a private IPv6
  address, you can do it, but you must route traffic through a resource in another
  subnet with a public IPv6 address to accomplish it.
- If you have a private IPv6 GUA range allocated to a VPC, you cannot use public IPv6 GUA space that overlaps the private IPv6 GUA space in the same VPC.
- Communication between resources with private IPv6 ULA and GUA address ranges is supported (such as across Direct Connect. VPC peering, transit gateway, or VPN connections).
- A private GUA IPv6 range cannot be converted to a publicly-advertised IPv6 GUA
  range.

AWS Management Console

###### To enable provisioning private IPv6 GUA CIDRs

1. Open the IPAM console at
   [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2. In the navigation pane, choose **IPAMs**.
3. Choose your IPAM and choose **Actions** > **Edit**.
4. Under **Private IPv6 GUA CIDRs**, choose **Enable provisioning GUA CIDR space into private IPv6 IPAM pools**.
5. Choose **Save changes**.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to enable provisioning private IPv6 GUA CIDRs:

1. View current IPAMs with [describe-ipams](../../../cli/latest/reference/ec2/describe-ipams.md "../../../cli/latest/reference/ec2/describe-ipams.md")
2. Modify the IPAM with [modify-ipam](../../../cli/latest/reference/ec2/modify-ipam.md "../../../cli/latest/reference/ec2/modify-ipam.md") and include the option to
   `enable-private-gua`.

Once you enable the option to provision private IPv6 GUA CIDRs, you can provision a private IPv6 GUA CIDR to a pool. For more information, see [Provision CIDRs to a pool](prov-cidr-ipam.md "prov-cidr-ipam.md").
