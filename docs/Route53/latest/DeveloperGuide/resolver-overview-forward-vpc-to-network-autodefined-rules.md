# Domain names that VPC Resolver creates autodefined system rules for

Resolver automatically creates autodefined system rules that define how queries for selected domains are resolved by default:

- For private hosted zones and for Amazon EC2–specific domain names (such as compute.amazonaws.com and
  compute.internal), autodefined rules ensure that your private hosted zones and EC2 instances continue to resolve
  if you create conditional forwarding rules for less specific domain names such as "." (dot) or "com".
- For publicly reserved domain names (such as localhost and 10.in-addr.arpa), DNS best practices recommend
  that queries are answered locally instead of being forwarded to public name servers. See
  [RFC 6303, Locally Served DNS Zones](https://tools.ietf.org/html/rfc6303 "https://tools.ietf.org/html/rfc6303").

###### Note

If you create a conditional forwarding rule for "." (dot) or "com", we recommend that you also create a system rule
for amazonaws.com. (System rules cause VPC Resolver to locally resolve DNS queries for specific domains and subdomains.)
Creating this system rule improves performance, reduces the number of queries that are forwarded to your network,
and reduces VPC Resolver charges.

If you want to override an autodefined rule, you can create a conditional forwarding rule for the same domain name.

You can also disable some of the autodefined rules. For more information, see [Forwarding rules for
reverse DNS queries in VPC Resolver](resolver-rules-managing.md#resolver-automatic-forwarding-rules-reverse-dns "resolver-rules-managing.md#resolver-automatic-forwarding-rules-reverse-dns").

VPC Resolver creates the following autodefined rules.

**Rules for private hosted zones**
For each private hosted zone that you associate with a VPC, VPC Resolver creates a rule and associates it with
the VPC. If you associate the private hosted zone with multiple VPCs, VPC Resolver associates the rule with the same VPCs.

The rule has a type of **Forward**.

**Rules for various AWS internal domain names**

All rules for the internal domain names in this section have a type of
**Forward**. VPC Resolver forwards DNS queries for
these domain names to the authoritative name servers for the
VPC.

###### Note

VPC Resolver creates most of these rules when you set the `enableDnsHostnames` flag for a VPC to `true`.
VPC Resolver creates the rules even if you aren't using Resolver endpoints.

VPC Resolver creates the following autodefined rules and associates them with a VPC when you set the `enableDnsHostnames` flag
for the VPC to `true`:

- `Region-name`.compute.internal, for example, eu-west-1.compute.internal.
  The us-east-1 Region doesn't use this domain name.
- `Region-name`.compute.`amazon-domain-name`, for example,
  eu-west-1.compute.amazonaws.com or cn-north-1.compute.amazonaws.com.cn.
  The us-east-1 Region doesn't use this domain name.
- ec2.internal. Only the us-east-1 Region uses this domain name.
- compute-1.internal. Only the us-east-1 Region uses this domain name.
- compute-1.amazonaws.com. Only the us-east-1 Region uses this domain name.

The following autodefined rules are for the reverse DNS lookup for the rules that VPC Resolver creates when you set the
`enableDnsHostnames` flag for the VPC to `true`.

- 10.in-addr.arpa
- 16.172.in-addr.arpa through 31.172.in-addr.arpa
- 168.192.in-addr.arpa
- 254.169.254.169.in-addr.arpa
- Rules for each of the CIDR ranges for the VPC. For example, if a VPC that has a CIDR range of
  10.0.0.0/23, VPC Resolver creates the following rules:
  - 0.0.10.in-addr.arpa
  - 1.0.10.in-addr.arpa

The following autodefined rules, for localhost-related domains, also are created and associated with a VPC when you
set the `enableDnsHostnames` flag for the VPC to `true`:

- localhost
- localdomain
- 127.in-addr.arpa
- 1.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa
- 0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.ip6.arpa

VPC Resolver creates the following autodefined rules and associates them with your VPC when
you connect the VPC with another VPC through transit gateway or VPC
peering, and with DNS support enabled:

- The reverse DNS lookup for the peer VPC's IP address ranges, for example, 0.192.in-addr.arpa

If you add an IPv4 CIDR block to a VPC, VPC Resolver adds an autodefined rule for the new IP address range.

- If the other VPC is in another Region, the following domain names:
  - `Region-name`.compute.internal.
    The us-east-1 Region doesn't use this domain name.
  - `Region-name`.compute.`amazon-domain-name`.
    The us-east-1 Region doesn't use this domain name.
  - ec2.internal. Only the us-east-1 Region uses this domain name.
  - compute-1.amazonaws.com. Only the us-east-1 Region uses this domain name.

**A rule for all other domains**
VPC Resolver creates a "." (dot) rule that applies to all domain names that aren't specified earlier in this topic.
The "." rule has a type of **Recursive**, which means that the rule causes VPC Resolver to act as a recursive resolver.
