# What are Amazon Route 53 Profiles?

With Route 53 Profiles, you can apply and manage DNS-related Route 53 configurations across many VPCs
and in different AWS accounts. Profiles make managing the DNS settings for many VPCs as
easy as managing them for a single VPC and when you update a Profile, its settings are propagated
to all the VPCs associated to the Profile. You can also share a Profile with AWS accounts in
the same Regions by using AWS RAM. The currently Route 53 supported resources you can associate
to a Profile are:

- Private hosted zones and the settings specified in them. For more information
  about working with private hosted zones, see [Working with private hosted zones](hosted-zones-private.md "hosted-zones-private.md").
- Resolver rules, both forwarding and system. For more information about Resolver
  rules, see [Managing forwarding rules](resolver-rules-managing.md "resolver-rules-managing.md").
- DNS Firewall rule groups. For more information about DNS Firewall rule groups, see [DNS Firewall rule groups and
  rules](resolver-dns-firewall-rule-groups.md "resolver-dns-firewall-rule-groups.md").
- Interface VPC endpoints. For more information about interface VPC endpoints, see
  [interface VPC
  endpoints](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md") in the _Amazon VPC User Guide_.
- VPC Resolver query logging configurations. For more information about VPC Resolver query
  logging, see [Resolver query logging](resolver-query-logs.md "resolver-query-logs.md").
  Some of the VPC configurations are directly managed on the Profile. The configurations
  are:

- Reverse DNS lookup configuration for Resolver Rules.
- DNS Firewall failure mode configuration.
- DNSSEC validation configuration.
  For example, you can enable the DNS Firewall failure mode configuration for all the VPCs the
  Profile is associated to, but keep the VPC's existing DNSSEC validation
  configuration.

###### Important

Once you enable the Profile settings for the preceding configurations, and associate the
Profile to a VPC, the Profile settings take effect immediately.

You can also use CloudFormation to set up consistent DNS settings for newly provisioned VPCs.

You can associate one Profile per VPC and the number of resources you can associate per
Profile varies. For more information, see [Quotas on
Route 53 Profiles](DNSLimitations.md#limits-api-entities-route53-profiles "DNSLimitations.md#limits-api-entities-route53-profiles") .

## How Route 53 Profile settings are prioritized

You can have the local DNS settings and associations set for Profiles for migration, or
other testing purposes. When a DNS query matches both the Resolver rule for a private
hosted zone that is directly associated with the VPC and a Resolver rule for a private
hosted zone that is associated to the Profile, the local DNS settings take precedence.
When DNS query is made for a conflicting domain name, the most specific one wins. The
following table includes examples of the evaluation order:

| DNS query             | Profile rule     | VPC rule              | Evaluated rule |
| --------------------- | ---------------- | --------------------- | -------------- |
| example.com           | example.com      | example.com           | Local VPC      |
| test.example.com      | test.example.com | example.com           | Profile        |
| marketing.example.com | None             | marketing.example.com | Local VPC      |

## Route 53 Profiles Region availability

To view the Region availability and the endpoints, see [Service endpoints for Route 53](../../../general/latest/gr/r53.md "../../../general/latest/gr/r53.md") in the
_AWS General Reference_ guide.
