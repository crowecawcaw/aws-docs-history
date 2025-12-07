# How VPC Resolver determines whether the domain name

in a query matches any rules

Route 53 VPC Resolver compares the domain name in the DNS query with the domain name in the rules that are associated with the
VPC that the query originated from. VPC Resolver considers the domain names to match in the following cases:

- The domain names match exactly
- The domain name in the query is a subdomain of the domain name in the rule
  For example, if the domain name in the rule is acme.example.com, VPC Resolver considers the following domain names in a
  DNS query to be a match:

- acme.example.com
- zenith.acme.example.com
  The following domain names are not a match:

- example.com
- nadir.example.com
  If the domain name in a query matches the domain name in more than one rule (such as example.com and www.example.com),
  VPC Resolver routes outbound DNS queries using the rule that contains the most specific domain name (www.example.com).
