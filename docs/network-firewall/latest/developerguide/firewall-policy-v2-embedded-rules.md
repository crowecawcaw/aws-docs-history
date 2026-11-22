

# Embedded rules in a Next Generation policy

*Embedded rules* (also called inline rules) are rules that you author directly in a Next Generation policy's firewall section or IPS section, rather than in a separate, referenced rule group. An embedded rule is part of the policy and shares the policy's lifecycle. For how to add rules to a section, see [The firewall section and the IPS section](firewall-policy-v2-sections.md).

**Capacity benefit**  
The main advantage of embedded rules is that they don't require you to commit capacity up front. A referenced rule group has a fixed capacity that you set when you create it and can't change afterward, so you have to estimate how many rules you'll need over the rule group's lifetime. Embedded rules have no such fixed reservation: their capacity is drawn automatically from the engine section's remaining capacity. For more information about how capacity works, see [Setting rule group capacity in AWS Network Firewall](rule-group-capacity-v2.md).

Embedded rules share a combined limit of 30,000 rules total across the policy's firewall section and IPS section, and a combined rule-string size limit of 5 MB across the two sections. For the full set of quotas, see [AWS Network Firewall quotas](quotas.md).

**Limitations**  
Embedded rules have the following limitations:
+ **No sharing or reuse** – Embedded rules can't be shared or reused across policies. They don't have their own Amazon Resource Name (ARN) and belong to the one policy that contains them. They travel with the policy only when you share the whole policy through AWS Resource Access Manager. When you want to reuse or share rules across policies or accounts, use a referenced rule group instead.
+ **No domain lists** – An embedded entry can't be a domain list (an FQDN rule group that uses a `RulesSourceList`). To use a domain list, add it as a referenced firewall rule group instead.