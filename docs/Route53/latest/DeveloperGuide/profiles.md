

# What are Amazon Route 53 Profiles?
<a name="profiles"></a>

With Route 53 Profiles, you can apply and manage DNS-related Route 53 configurations across many VPCs and in different AWS accounts. Profiles make managing the DNS settings for many VPCs as easy as managing them for a single VPC and when you update a Profile, its settings are propagated to all the VPCs associated to the Profile. You can also share a Profile with AWS accounts in the same Regions by using AWS RAM. The currently Route 53 supported resources you can associate to a Profile are:
+ Private hosted zones and the settings specified in them. For more information about working with private hosted zones, see [Working with private hosted zones](hosted-zones-private.md).
+ Resolver rules, both forwarding and system. For more information about Resolver rules, see [Managing forwarding rules](resolver-rules-managing.md).
+ DNS Firewall rule groups. For more information about DNS Firewall rule groups, see [DNS Firewall rule groups and rules](resolver-dns-firewall-rule-groups.md).
+ Interface VPC endpoints. For more information about interface VPC endpoints, see [interface VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the *Amazon VPC User Guide*.
+ VPC Resolver query logging configurations. For more information about VPC Resolver query logging, see [Resolver query logging](resolver-query-logs.md).

Some of the VPC configurations are directly managed on the Profile. The configurations are:
+ Reverse DNS lookup configuration for Resolver Rules.
+ DNS Firewall failure mode configuration.
+ DNSSEC validation configuration.

For example, you can enable the DNS Firewall failure mode configuration for all the VPCs the Profile is associated to, but keep the VPC's existing DNSSEC validation configuration.

**Important**  
After you enable the Profile settings for the preceding configurations, and associate the Profile to a VPC, the Profile settings take effect immediately.

You can also use CloudFormation to set up consistent DNS settings for newly provisioned VPCs. 

You can associate up to two Profiles to a VPC. Each association between a Profile and a VPC has a *priority*, a value from 100 to 9900. A lower value means a higher priority. VPC Resolver evaluates the Profiles that are associated to a VPC in priority order. For more information, see [How Route 53 Profile settings are prioritized](#profiles-priority). The number of resources you can associate per Profile varies. For more information, see [Quotas on Route 53 Profiles](DNSLimitations.md#limits-api-entities-route53-profiles).

## How Route 53 Profile settings are prioritized
<a name="profiles-priority"></a>

You can have the local DNS settings and associations set for Profiles for migration, or other testing purposes. When a DNS query matches both the Resolver rule for a private hosted zone that is directly associated with the VPC and a Resolver rule for a private hosted zone that is associated to the Profile, the local DNS settings take precedence. When DNS query is made for a conflicting domain name, the most specific one wins. The following table includes examples of the evaluation order:


**DNS evaluation order examples**  

| DNS query | Profile rule | VPC rule | Evaluated rule | 
| --- | --- | --- | --- | 
| example.com | example.com | example.com | Local VPC | 
| test.example.com | test.example.com | example.com | Profile | 
| marketing.example.com | None | marketing.example.com | Local VPC | 

When more than one Profile is associated to a VPC, each association has a *priority*, a value from 100 to 9900. A lower value means a higher priority. VPC Resolver evaluates the Profiles in priority order, starting with the association that has the lowest priority value:
+ **Resolver rules and private hosted zones** – For each DNS query, VPC Resolver uses the first Profile, in priority order, that has a Resolver rule or a private hosted zone that matches the domain name in the query. VPC Resolver doesn't evaluate the remaining Profiles for that query, even if one of them has a more specific match. VPC Resolver then compares the settings in that Profile with the local VPC settings: the most specific domain name wins, and the local VPC settings take precedence when both are equally specific.
+ **Resolver DNS Firewall rule groups** – DNS Firewall evaluates the rule groups that are associated directly to the VPC together with the rule groups in the highest priority Profile association that has a rule that matches the query. The rule group priority determines the evaluation order, and a rule group that is associated directly to the VPC takes precedence over a Profile rule group that has the same rule group priority. DNS Firewall doesn't evaluate rule groups in the remaining Profiles for that query.
+ **VPC Resolver query logging configurations** – VPC Resolver logs queries to the query logging configurations in every Profile that is associated to the VPC, regardless of priority.
+ **Profile configurations** – For reverse DNS lookup configuration for Resolver rules, DNS Firewall failure mode configuration, and DNSSEC validation configuration, the setting in the highest priority Profile that sets the configuration applies. VPC Resolver skips Profiles that use the VPC's own setting. If no associated Profile sets the configuration, the VPC's own setting applies.

For example, Profile A is associated to a VPC with priority 100, Profile B is associated to the same VPC with priority 200, and the VPC has a local Resolver rule for `corp.example.com`. The following table shows which rule VPC Resolver uses for queries from this VPC.


| DNS query | Profile A rule (priority 100) | Profile B rule (priority 200) | VPC rule | Evaluated rule | 
| --- | --- | --- | --- | --- | 
| test.example.com | example.com | test.example.com | None | Profile A (example.com) | 
| app.example.net | None | example.net | None | Profile B (example.net) | 
| hr.corp.example.com | example.com | hr.corp.example.com | corp.example.com | Local VPC (corp.example.com) | 

If a VPC has no other Profile associations, you can omit the priority when you associate a Profile, and the association gets priority 100. When the VPC already has a Profile association, you must specify a priority, and each Profile association for the VPC must have a unique priority. Associations that were created before you could associate multiple Profiles to a VPC have priority 100. You can change the priority later. For more information, see [Updating the priority of a Route 53 Profile association with a VPC](profiles-vpc-update-priority.md).

Every Profile association for a VPC that isn't deleted keeps its priority and counts toward the quota for Profiles per VPC. This includes associations whose status is `FAILED` or `DELETING`. When you disassociate a Profile from a VPC, the other Profile associations for the VPC keep their priorities, and VPC Resolver evaluates the remaining Profiles in priority order.

## Route 53 Profiles Region availability
<a name="profiles-region-availability"></a>

To view the Region availability and the endpoints, see [Service endpoints for Route 53](https://docs.aws.amazon.com/general/latest/gr/r53.html) in the *AWS General Reference* guide.