# Route 53 Resolver DNS Firewall Advanced

DNS Firewall Advanced detects suspicious DNS queries based on known threat signatures in DNS
queries. You can specify a threat type in a rule that you use in a DNS Firewall rule,
inside a rule group. When you associate a rule group with a VPC, DNS Firewall compares
your DNS queries against the domains that are flagged in the rules. If it finds a match,
it handles the DNS query according to the matching rule's action.

DNS Firewall Advanced works by identifying suspicious DNS threat signatures by inspecting a range of key
identifiers in the DNS payload including the timestamp of requests, frequency of request
and responses, the DNS query strings, and the length, type or size of both outbound and
inbound DNS queries. Based on the type of threat signature, you can configure policies
to block, or simply log and alert on the query. By using an expanded set of threat
identifiers, you can protect against DNS threats from domain sources that may yet be
unclassified by threat intelligence feeds maintained by the broader security
community.

Currently, DNS Firewall Advanced offers protections from:

- Domain Generation Algorithms (DGAs)

DGAs are used by attackers to generate a large number of domains to launch malware
attacks.

- DNS
  tunneling

DNS tunneling is used by attackers to exfiltrate data from the client by using the DNS tunnel without making a network connection to the client.
To learn how to create rules, see [Creating a rule group
and rules](resolver-dns-firewall-rule-group-adding.md "resolver-dns-firewall-rule-group-adding.md")
and [Rule settings in
DNS Firewall](resolver-dns-firewall-rule-settings.md "resolver-dns-firewall-rule-settings.md").

###### Mitigating false positive scenarios

If you are encountering false-positive scenarios in rules that use DNS Firewall Advanced
protections to block queries, perform the following steps:

1. In the Resolver logs, identify the rule group and DNS Firewall Advanced protections that are
   causing the false positive. You do this by finding the log for the query that
   DNS Firewall is blocking, but that you want to allow through. The log record lists
   the rule group, rule action, and the DNS Firewall Advanced protection. For
   information about the logs, see [Values that appear in Resolver query logs](resolver-query-logs-format.md "resolver-query-logs-format.md").
2. Create a new rule in the rule group that explicitly allows the blocked
   query through. When you create the rule, you can define your own domain list
   with just the domain specification that you want to allow. Follow the
   guidance for rule group and rule management at [Creating a rule group
   and rules](resolver-dns-firewall-rule-group-adding.md "resolver-dns-firewall-rule-group-adding.md").
3. Prioritize the new rule inside the rule group so that it runs before the
   rule that's using the managed list. To do this, give the new rule a lower
   numeric priority setting.
   When you have updated your rule group, the new rule will explicitly allow the
   domain name that you want to allow before the blocking rule runs.
