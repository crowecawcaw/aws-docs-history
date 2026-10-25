

# 1:1 NAT in AWS Cloud WAN
<a name="cloudwan-nat"></a>

1:1 NAT on AWS Cloud WAN provides static, stateless network address translation (NAT) in the core network, delivered as a Regional private NAT gateway embedded directly in your core network. There's no separate NAT appliance or NAT gateway resource to deploy or manage. You define Classless Inter-Domain Routing (CIDR) to CIDR mappings on each attachment, and Cloud WAN translates the IPv4 addresses of traffic that matches those mappings in both inbound and outbound directions. Each address in the original CIDR always maps to the same position in the NAT CIDR. The host bits are kept, and ports aren't changed. For example, if `10.10.100.0/24` is mapped to `100.64.100.0/24`, then `10.10.100.5` is translated to `100.64.100.5`; the host portion (here, the last octet) stays the same.

Each rule works in both directions, so you don't need a separate reverse rule:
+ **Source NAT (SNAT)** – Traffic arriving from the attachment with a source address in the original CIDR is translated to the NAT CIDR.
+ **Destination NAT (DNAT)** – Traffic sent to the attachment with a destination address in the NAT CIDR is translated back to the original CIDR.

Translation doesn't depend on connection state. Return traffic is translated automatically, and other networks can also start connections to the NAT addresses.

## Key properties
<a name="cloudwan-nat-key-properties"></a>
+ **Per-CIDR, per-attachment** – A rule maps one source CIDR on an attachment to one NAT CIDR. For example, attachment A's `10.0.0.0/24` is translated to `100.64.1.0/24`.
+ **Multiple rules per attachment** – Each CIDR can be translated or left untranslated independently. Each rule is a single 1:1 mapping that covers both directions. Rules have no priority order. Overlap between any rule CIDRs (original or NAT) on an attachment is rejected, so each IP matches at most one rule.
+ **Direction is implicit** – If a packet's source IP address falls in an original CIDR on the source attachment, SNAT translates it to the NAT CIDR. If a packet's destination IP address falls in a NAT CIDR on the destination attachment, DNAT translates it back to the original CIDR. If both apply, both the source and destination addresses are translated.
+ **Translation happens at the attachment where the rule is defined** – SNAT at the source attachment's core network edge, and DNAT at the destination attachment's core network edge, including when the two attachments are in different Regions.
+ **Equal prefix lengths, host bits preserved** – The original and NAT CIDRs must have the same prefix length, and host bits carry over unchanged (`10.0.0.5` becomes `100.64.1.5`). Every address in the NAT CIDR maps to exactly one address in the original CIDR, so traffic can be started from either side.
+ **Stateless translation** – The mapping is determined by the rule alone. There is no port translation (this isn't NAPT), no NAT session state, no port allocation.
+ **IPv4 only** – IPv6 isn't supported. IPv6 traffic passes through untranslated.

## Use cases
<a name="cloudwan-nat-use-cases"></a>
+ **Overlapping IP addresses** – Enterprises run into IP address conflicts from mergers and acquisitions, third-party partner integrations, multi-cloud connectivity, or decentralized IP governance across teams. When two networks share the same RFC 1918 address ranges, they can't communicate over a shared transit gateway unless one network is re-addressed or NAT appliances are deployed at multiple points. With 1:1 NAT, you configure a mapping at the attachment level, and the transit gateway translates traffic to and from the mapped CIDRs. No IP reconfiguration is needed.
+ **IP obfuscation** – Network administrators often need to give external partners or other business units access to private applications in VPCs while controlling which addresses those parties see. With 1:1 NAT, those parties see only the translated (private or CGNAT) addresses, and your internal addressing stays hidden.
+ **IPv4 exhaustion** – Large enterprises can run out of RFC 1918 address space. 1:1 NAT supports carrier-grade NAT (CGNAT) ranges (RFC 6598, `100.64.0.0/10`) as NAT CIDRs, which extends your addressable space without renumbering existing networks.

## Supported attachment types
<a name="cloudwan-nat-supported-attachments"></a>

**Supported:** VPC, AWS Direct Connect gateway, Connect, and Site-to-Site VPN

**Unsupported:** Transit gateway route table attachments and Tunnelless Connect (TLC) attachments.

**Additional restrictions:**
+ You can't enable NAT on a VPC attachment that has appliance mode enabled. Disable one before enabling the other.
+ You can't enable NAT on a VPC attachment that is the transport for a tunnel-less Connect attachment.
+ A Connect attachment and its transport attachment can't both have NAT enabled.

**Topics**
+ [Key properties](#cloudwan-nat-key-properties)
+ [Use cases](#cloudwan-nat-use-cases)
+ [Supported attachment types](#cloudwan-nat-supported-attachments)
+ [How 1:1 NAT works](cloudwan-nat-how-it-works.md)
+ [Routing behavior for 1:1 NAT](cloudwan-nat-routing.md)
+ [Configure 1:1 NAT](cloudwan-nat-configure.md)
+ [Permissions and IAM for 1:1 NAT](cloudwan-nat-permissions.md)