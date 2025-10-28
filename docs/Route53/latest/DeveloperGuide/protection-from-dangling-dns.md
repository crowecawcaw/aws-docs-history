# Protection from dangling delegation records in Route 53

With Route 53, a customer can create a hosted zone, such as `example.com`, to host their DNS records.
Each hosted zone comes with a "delegation set", which is a set of four name servers that a customer
can use
to configure NS records in the parent domain.
These NS records can be called "delegation NS records", or "delegation records".

In order for the `example.com` Route 53 hosted zone to become authoritative, the rightful owner of
the `example.com` domain needs to configure delegation records in their ".com" parent
domain through the domain registrar. In cases where a customer loses access to the four name servers
configured in the parent domain, for example because the associated hosted zone is deleted,
it can create a risk that an attacker can exploit.
This is referred to as a "dangling delegation records" risk.

Route 53 protects against the dangling delegation record risk in the case where a hosted
zone is deleted. After deletion, if a new hosted zone is being created with the same
domain name, Route 53 will check if the delegation records pointing to the deleted
hosted zone are still present in the parent domain. If they are, Route 53 will prevent
any overlapping name servers from being assigned. This is scenario 1 in the
following examples.

However, there are other dangling delegation record risks, which Route 53 can't protect against, as detailed in scenarios 2 and 3 in the following examples.
To protect yourself against this broader set of risks, make sure the parent NS records match the delegation set
for the Route 53 hosted zone.
You can find the delegation set of a hosted zone through the Route 53 console or AWS CLI.
For more information, see [Listing records](resource-record-sets-listing.md "resource-record-sets-listing.md")
or [get-hosted-zone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-hosted-zone.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/get-hosted-zone.html").

Additionally, enabling DNSSEC signing for a Route 53 hosted zone can serve as another layer of protection beyond the best practices mentioned above.
DNSSEC authenticates that DNS answers come from the authoritative source, effectively protecting against this risk.
For more information see [Configuring DNSSEC signing in Amazon Route 53](dns-configuring-dnssec.md "dns-configuring-dnssec.md").

## Examples

In the following examples, we assume you have a domain `example.com`, and its child
domain `child.example.com`. We will explain how in various scenarios dangling
delegation records can get created, how Route 53 protects your domain against
abuse and how to effectively mitigate the risks associated with dangling
delegation records.

**Scenario 1:**
You create a hosted zone `child.example.com` with four name servers:
<ns1>, <ns2>, <ns3>, and <ns4>. You properly setup the delegation in hosted zone `example.com`,
creating delegation NS records for `child.example.com` with four name servers <ns1>, <ns2>, <ns3>, and <ns4>.
When `child.example.com` hosted zone gets deleted without removing the delegation NS records
in `example.com`, Route 53 protects `child.example.com` from dangling delegation records risk
by preventing <ns1>, <ns2>, <ns3>, and <ns4> from being assigned to newly created hosted zones
with the same domain name.

**Scenario 2:**
Similar to scenario 1, but this time you delete child hosted zone AND the delegation NS records in hosted zone `example.com`.
However, you add back delegation NS records <ns1>, <ns2>, <ns3>, and <ns4> without creating a child hosted zone.
Here, <ns1>, <ns2>, <ns3>, and <ns4> are dangling delegation records, because Route 53 removes the hold,
which was preventing <ns1>, <ns2>, <ns3>, and <ns4> from being assigned and will now allow newly
created hosted zones to use above name servers.
To mitigate the risk, remove <ns1>, <ns2>, <ns3>, and <ns4> from the delegation records
and only add them back once the child hosted zone has been created.

**Scenario 3:**
In this scenario, you create a Route 53 reusable delegation set with
name servers <ns1>, <ns2>, <ns3>, and <ns4>.
Then, you delegate the domain `example.com` to these name servers in the parent
domain `.com`. However, you haven’t created the hosted zone for `example.com` on the reusable delegation set yet.
Here, <ns1>, <ns2>, <ns3>, and <ns4> are dangling delegation records. To mitigate the risk,
create the hosted zone using the reusable delegation set with name servers <ns1>, <ns2>, <ns3>, and <ns4>.
