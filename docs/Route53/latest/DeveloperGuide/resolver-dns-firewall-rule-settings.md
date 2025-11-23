# Rule settings in

DNS Firewall

When you create or edit a rule in a DNS Firewall rule group, you specify the following
values:

**Name**

A unique identifier for the rule in the rule group.

**(Optional) Description**

A short description that provides more information about the rule.

**Domain list**

The list of domains that the rule inspects for. You can create and
manage your own domain list or you can subscribe to a domain list that
AWS manages for you. For more information, see [Route 53 Resolver DNS Firewall domain lists](resolver-dns-firewall-domain-lists.md "resolver-dns-firewall-domain-lists.md").

A rule can contain ether a domain list or a DNS Firewall Advanced protection, but
not both.

**Domain redirection setting (domain lists only)**

You can choose for the DNS Firewall rule to inspect only the first domain
or all (default) the domains in the DNS redirection chain, such as
CNAME, DNAME, etc. If you choose to inspect all the domains, you must
add the subsequent domains in the DNS redirection chain to the domain
list and set to the action you want the rule to take, either ALLOW,
BLOCK, or ALERT. For more information, see [Route 53 Resolver DNS Firewall components and
settings](resolver-dns-firewall-overview.md#resolver-dns-firewall-components "resolver-dns-firewall-overview.md#resolver-dns-firewall-components").

**Query type (domain lists only)**

The list of DNS query types that the rule inspects for. The following
are the valid
values:

- A: Returns an IPv4 address.
- AAAA: Returns an Ipv6 address.
- CAA: Restricts CAs that can create SSL/TLS certifications for
  the domain.
- CNAME: Returns another domain name.
- DS: Record that identifies the DNSSEC signing key of a
  delegated zone.
- MX: Specifies mail servers.
- NAPTR: Regular-expression-based rewriting of domain names.
- NS: Authoritative name servers.
- PTR: Maps an IP address to a domain name.
- SOA: Start of authority record for the zone.
- SPF: Lists the servers authorized to send emails from a
  domain.
- SRV: Application specific values that identify servers.
- TXT: Verifies email senders and application-specific values.
- A query type you define by using the DNS type ID, for example
  28 for AAAA. The values must be defined as TYPE`NUMBER`, where the `NUMBER`
  can be 1-65334, for example, TYPE28. For more information, see [List
  of DNS record types](https://en.wikipedia.org/wiki/List_of_DNS_record_types "https://en.wikipedia.org/wiki/List_of_DNS_record_types").

You can create one query type per rule.

###### Note

If you set up a firewall BLOCK rule with action NXDOMAIN
on query type equals AAAA,
this action will not be applied to synthetic IPv6 addresses
generated when DNS64 is enabled.

**DNS Firewall Advanced protection**

Detects suspicious DNS queries based on known threat signatures in DNS
queries. You can choose protection from:

- Domain Generation Algorithms (DGAs)

DGAs are used by attackers to generate a large number of
domains to launch malware attacks.

- DNS tunneling

DNS tunneling is used by attackers to exfiltrate data from the
client by using the DNS tunnel without making a network
connection to the client.

- Dictionary DGA

Dictionary DGAs are used by attackers to generate domains
using dictionary words to evade detection in malware
command-and-control communications.

In a DNS Firewall Advanced rule you can choose to either block, or alert on a
query that matches the threat.

For more information, see For more information, see [Route 53 Resolver DNS Firewall Advanced](firewall-advanced.md "firewall-advanced.md").

A rule can contain ether a DNS Firewall Advanced protection or a domain list, but
not both.

**Confidence threshold (DNS Firewall Advanced only)**

The confidence threshold for DNS Firewall Advanced.
You must provide this value when you create a DNS Firewall Advanced rule. The
confidence level values mean:

- High – Detects only the most well corroborated threats
  with a low rate of false positives.
- Medium – Provides a balance between detecting threats
  and false positives.
- Low – Provides the highest detection rate for threats,
  but also increases false positives.

For more information, see Rule settings in
DNS Firewall.

**Action**

How you want DNS Firewall to handle a DNS query whose domain name matches
the specifications in the rule's domain list. For more information, see [Rule actions in
DNS Firewall](resolver-dns-firewall-rule-actions.md "resolver-dns-firewall-rule-actions.md").

**Priority**

Unique positive integer setting for the rule within the rule group
that determines
processing order. DNS Firewall inspects DNS queries against the rules in a
rule group starting with the lowest numeric priority setting and going
up. You can change a rule's priority at any time, for example to change
the order of processing or make space for other rules.
