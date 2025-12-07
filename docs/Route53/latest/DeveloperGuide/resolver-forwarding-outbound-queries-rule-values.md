# Values that you specify when you create or edit rules

When you create or edit a forwarding rule, you specify the following values:

**Rule name**
A friendly name that lets you easily find a rule on the dashboard.

**Rule type**
Choose the applicable value:

- **Forward** – Choose this option when
  you want to forward DNS queries for a specified domain name to resolvers on your network.
- **Delegate** – Choose this option when you want to
  delegate authority for a subdomain, hosted in a private hosted
  zone, to your on-premises resolver (or to a VPC Resolver on another
  VPC).
- **System** – Choose this option when
  you want VPC Resolver to selectively override the behavior that is defined in a forwarding rule. When you create a system rule,
  VPC Resolver resolves DNS queries for specified subdomains that would otherwise be resolved by DNS resolvers on your network.

By default, forwarding rules apply to a domain name and all its subdomains. If you want to forward queries for a domain
to a resolver on your network but you don't want to forward queries for some subdomains, you create a system rule for the subdomains.
For example, if you create a forwarding rule for example.com but you don't want to forward queries for acme.example.com, you create a
system rule and specify acme.example.com for the domain name.

**Delegation record – for delegate rule only**
DNS queries that mach to this domain are forwarded to the resolvers on your network.

###### Note

As a prerequisite for a delegate rule you must create NS records in the private hosted zone,
when using private hosted zone to outbound delegation The record is:
NS - Nameservers to delegate via the Resolver outbound endpoint with
delegate rule. For more information, see [NS record type](ResourceRecordTypes.md#NSFormat "ResourceRecordTypes.md#NSFormat").

**VPCs that use this rule**
The VPCs that use this rule to forward DNS queries for the specified domain name or names.
You can apply a rule to as many VPCs as you want.

**Domain name – for forward rule only**
DNS queries for this domain name are forwarded to the IP addresses that you specify in
**Target IP addresses**. For example, you can
specify a specific domain (example.com), a top-level domain (com), or a
dot (.) to forward all DNS queries. For more information, see [How VPC Resolver determines whether the domain name
in a query matches any rules](resolver-overview-forward-vpc-to-network-domain-name-matches.md "resolver-overview-forward-vpc-to-network-domain-name-matches.md").

**Outbound endpoint**
VPC Resolver forwards DNS queries through the outbound endpoint that you specify here to the
IP addresses that you specify in **Target IP addresses**.

**Target IP addresses**
When a DNS query matches the name that you specify in **Domain name**, the outbound endpoint
forwards the query to the IP addresses that you specify here. These are typically the IP addresses for DNS resolvers on your
network.

**Target IP addresses** is available only when the value of **Rule type**
is **Forward**.

Specify IPv4 or IPv6 addresses, the protocols, and ServerNameIndication you want to use for the endpoint.
ServerNameIndication is applicable only when selected protocol is DoH.

Resolving the target IP address of the FQDN of a DoH resolver on your network over the outbound endpoint
is not supported. Outbound endpoints need the target IP address of DoH resolver on your network to forward
the DoH queries to. If the DoH resolver on your network needs the FQDN in the TLS SNI and in the HTTP Host header,
ServerNameIndication must be provided.

**ServerNameIndication**
The Server Name Indication of the DoH server that you want to forward queries to. This is only used if the Protocol is DoH.

**Tags**
Specify one or more keys and the corresponding values. For example, you might specify
**Cost center** for **Key** and specify **456** for **Value**.

These are the tags that AWS Billing and Cost Management provides for organizing your AWS bill. For more information about using tags
for cost allocation, see [Using cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")
in the _AWS Billing User Guide_.
