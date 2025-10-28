# Using rules to control which queries are forwarded

to your network

Rules control which DNS queries Route 53 Resolver endpoint forwards to DNS resolvers on your
network and which queries Resolver answers itself.

You can categorize rules in a couple of ways. One way is by who creates the rules:

- **Autodefined rules** – Resolver automatically creates autodefined rules and
  associates the rules with your VPCs. Most of these rules apply to the AWS-specific domain names that Resolver answers queries for.
  For more information, see
  [Domain names that Resolver creates autodefined system rules for](resolver-overview-forward-vpc-to-network-autodefined-rules.md "resolver-overview-forward-vpc-to-network-autodefined-rules.md").
- **Custom rules** – You create custom rules and associate
  the rules with VPCs. Currently, you can create two types of custom
  rules, **conditional forwarding rules**, also known as
  forwarding rules, and **delegation rules**.
  **Forwarding** rules cause Resolver to forward DNS
  queries from your VPCs to the IP addresses for DNS resolvers on your
  network.

If you create a forwarding rule for the same domain as an autodefined rule, Resolver forwards queries for that domain name
to DNS resolvers on your network based on the settings in the forwarding rule.

**Delegation rules** forward DNS queries with the delegation records in
the delegation rule that match the NS records in response to the resolvers
on your network.
Another way to categorize rules is by what they do:

- **Conditional forwarding rules** – You create conditional forwarding rules
  (also known as forwarding rules) when you want to forward DNS queries for specified domain names to DNS resolvers
  on your network.
- **System rules** – System rules cause Resolver to selectively override the behavior
  that is defined in a forwarding rule. When you create a system rule, Resolver resolves DNS queries for specified subdomains
  that would otherwise be resolved by DNS resolvers on your network.

By default, forwarding rules apply to a domain name and all its subdomains. If you want to forward queries for a domain
to a resolver on your network but you don't want to forward queries for some subdomains, you create a system rule for the subdomains.
For example, if you create a forwarding rule for example.com but you don't want to forward queries for acme.example.com, you create a
system rule and specify acme.example.com for the domain name.

- **Recursive rule** – Resolver automatically creates a recursive rule named
  **Internet Resolver**. This rule causes Route 53 Resolver to act as a recursive resolver for any domain names
  that you didn't create custom rules for and that Resolver didn't create autodefined rules for. For information about how to
  override this behavior, see "Forwarding All Queries to Your Network" later in this topic.
  You can create custom rules that apply to specific domain names (yours or most AWS domain names), to public AWS domains names, or
  to all domain names.

**Forwarding queries for specific domain names to your network**
To forward queries for a specific domain name, such as example.com, to your network, you
create a rule and specify that domain name. For **forwarding** rules you
also specify the IP addresses of the DNS resolvers on your network
that you want to forward the queries to, or, for **delegation** rules,
create the delegation record for which you would like to delegate
the authority to on-prem resolvers. You then associate each rule
with the VPCs for which you want to forward DNS queries to your
network. For example, you can create separate rules for example.com,
example.org, and example.net. Then you can associate the rules with
the VPCs in an AWS Region in any combination.

**Forwarding queries for amazonaws.com to your network**
The domain name amazonaws.com is the public domain name for AWS resources such as EC2
instances and S3 buckets. If you want to forward queries for
amazonaws.com to your network, create a rule, specify amazonaws.com
for the domain name, and specify **Forward** or
**Delegation** for the rule type depending on
which method you want to use.

###### Note

Resolver doesn't automatically forward DNS queries for some amazonaws.com subdomains even if you create a
forwarding rule for amazonaws.com. For more information, see
[Domain names that Resolver creates autodefined system rules for](resolver-overview-forward-vpc-to-network-autodefined-rules.md "resolver-overview-forward-vpc-to-network-autodefined-rules.md"). For information about how to override
this behavior, see "Forwarding All Queries to Your Network," immediately following.

**Forwarding all queries to your network**

If you want to forward all queries to your network, you create a rule, specify "." (dot) for the domain name,
and associate the rule with the VPCs for which you want to forward all DNS queries to your network.
Resolver still doesn't forward all DNS queries to your network because using a DNS resolver outside of AWS would break
some functionality. For example, some internal AWS domain names have internal IP address ranges that aren't accessible
from outside of AWS. For a list of the domain names for which queries aren't forwarded to your network when you
create a rule for ".", see
[Domain names that Resolver creates autodefined system rules for](resolver-overview-forward-vpc-to-network-autodefined-rules.md "resolver-overview-forward-vpc-to-network-autodefined-rules.md").

However, autodefined system rules for reverse DNS can be disabled, allowing the "." rule to forward all reverse DNS queries to your network.
For more information on how to turn off the autodefined rules, see [Forwarding rules for
reverse DNS queries in Resolver](resolver-rules-managing.md#resolver-automatic-forwarding-rules-reverse-dns "resolver-rules-managing.md#resolver-automatic-forwarding-rules-reverse-dns").

If you want to try forwarding DNS queries for all domain names to your network, including the domain names
that are excluded from forwarding by default, you can create a "." rule and do one of the following:

- Set the `enableDnsHostnames` flag for the VPC to `false`
- Create rules for the domain names that are listed in
  [Domain names that Resolver creates autodefined system rules for](resolver-overview-forward-vpc-to-network-autodefined-rules.md "resolver-overview-forward-vpc-to-network-autodefined-rules.md")

###### Important

If you forward all domain names to your network, including the domain names that Resolver excludes when you create
a "." rule, some features might stop working.
