# How Resolver determines where to forward

DNS queries

When an application that runs on an EC2 instance in a VPC submits a DNS query, Route 53 Resolver performs the following steps:

1. Resolver checks for domain names in rules.

If the domain name in a query matches the domain name in a default forward rule, Resolver forwards
the query to the IP address that you specified when you created the
outbound endpoint. The outbound endpoint then forwards the query to the
IP addresses of resolvers on your network, which you specified when you
created the rule.

If the delegation record in response matches the delegation rule, then the Resolver delegate the authority
to on-prem resolvers through the outbound endpoint associated with the delegation rule.

For more information, see
[How Resolver determines whether the domain name
in a query matches any rules](resolver-overview-forward-vpc-to-network-domain-name-matches.md "resolver-overview-forward-vpc-to-network-domain-name-matches.md"). 2. Resolver endpoint forwards DNS queries based on the settings in the "." rule.

If the domain name in a query doesn't match the domain name in any other rules, Resolver forwards the query based on
the settings in the autodefined "." (dot) rule. The dot rule applies to all domain names except some AWS internal domain names and
record names in private hosted zones. This rule causes Resolver to forward DNS queries to public name servers if the
domain names in queries don't match any names in your custom forwarding rules. If you want to forward all queries to the
DNS resolvers on your network, you can create a custom forwarding rule, specify "." for the domain name, specify
**Forwarding** for **Type**, and specify the IP addresses of those resolvers. 3. Resolver returns the response to the application that submitted the query.
