# IP address ranges of Amazon Route 53 servers

Amazon Web Services (AWS) publishes its current IP address ranges in JSON format. If your firewalls or security groups restrict
incoming traffic based on source IP addresses, confirm that your configuration allows traffic from the applicable IP address ranges.

To view the current IP address ranges for Route 53, download
[ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json "https://ip-ranges.amazonaws.com/ip-ranges.json"), and search the file for the following values:

- `"service": "ROUTE53"`
- `"service": "ROUTE53_HEALTHCHECKS"`
- `"service": "ROUTE53_HEALTHCHECKS_PUBLISHING"`
  For more information about IP addresses for AWS resources, see
  [AWS IP address ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md") in the _Amazon Web Services General Reference_.

## IP address ranges of Route 53 name servers

`"service": "ROUTE53"` – These IP address ranges are used by Route 53
name servers. Add these ranges to the list of allowed IP address ranges if you're using
Route 53 as the DNS service for one or more domains and you want to be able to use the
`dig` or `nslookup` commands to query Route 53 name
servers.

###### Note

Route 53 name server IP addresses are static.

## IP address ranges of Route 53 health

checks

`"service": "ROUTE53_HEALTHCHECKS"` – These IP address ranges are
used by Route 53 health checkers. Add these ranges to the list of allowed IP address ranges
if you're using Route 53 health checks to check the health of resources on your
network.

###### Note

We rarely change the IP address ranges of health checkers. Monitor the [ip-ranges.json](https://ip-ranges.amazonaws.com/ip-ranges.json "https://ip-ranges.amazonaws.com/ip-ranges.json") file
for any updates to these ranges.

For more information about IP addresses for health checks, see [Configuring router and firewall
rules for Amazon Route 53 health checks](dns-failover-router-firewall-rules.md "dns-failover-router-firewall-rules.md").

## Referencing prefix lists

A _prefix list_ is a set of one or more CIDR block entries that you can
use to configure security groups. Your router and firewall for the rules for the Amazon EC2
instance must allow inbound traffic from the IP addresses that the Route 53 health
checkers use. A reference to a prefix list helps you to simplify the management of the
CIDR blocks in your rules. If you frequently use the same CIDRs across multiple rules,
you can manage those CIDRs in a single prefix list, instead of repeatedly referencing
the same CIDRs in each rule. If you need to remove a CIDR block, you can remove its
entry from the prefix list instead of removing the CIDR from every affected rule. For more information about
prefix lists in general, see [Group CIDR blocks using managed prefix lists](../../../vpc/latest/userguide/managed-prefix-lists.md "../../../vpc/latest/userguide/managed-prefix-lists.md") in the _Amazon VPC User Guide_.

AWS-managed prefix lists are sets of IP address ranges for AWS services. AWS-managed prefix lists are created and maintained by AWS and can be used by
anyone with an AWS account. You cannot create, modify, share, or delete an AWS-managed prefix list.

For more information about AWS-managed prefix lists, see [Work with AWS-managed prefix lists](../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md "../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md") in the _Amazon VPC User Guide_.

## Internal IP address ranges of Route 53 health checks

`"service": "ROUTE53_HEALTHCHECKS_PUBLISHING"` –. Route 53 uses these IP address ranges only internally. You don't need to add these ranges to the list of allowed ranges.
