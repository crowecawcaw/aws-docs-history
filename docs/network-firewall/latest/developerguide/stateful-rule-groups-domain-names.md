# Stateful

domain list rule groups in AWS Network Firewall

AWS Network Firewall supports domain name stateful network
traffic inspection. You can create allow lists and deny
lists with domain names that the stateful rules engine looks
for in network traffic.

All rule groups have the common settings that are defined at
[Common rule group settings in AWS Network Firewall](rule-group-settings.md "rule-group-settings.md").

## General settings

A domain list rule group has the following general settings.

- **Action** – Defines how Network Firewall handles
  traffic that matches the rule match settings. Valid values for domain rules are
  `Allow` `Deny`, `Reject`, and `Alert`:
  - For `Allow`, traffic of the specified protocol type that does not
    match the domain specifications is denied.
  - For `Deny`, traffic matching the domain specifications is blocked.
    Non-matching traffic is allowed to pass.
  - For `Reject`, traffic matching the domain specifications is blocked
    and a TCP reset packet is sent back to the source. This option is only available
    for TCP traffic.
  - For `Alert`, traffic matching the domain specifications generates
    an alert in the firewall's logs (when logging is enabled). Then, traffic either passes, is rejected,
    or drops based based on other rules in the firewall policy.

###### For firewall policies that use default action ordering

We recommend that you avoid combining `Reject` or
`Alert` domain list rule groups with `Allow` domain list rule groups. When this combination of rule groups
is defined in a firewall policy that uses default action ordering, the default drop rule added by the `Allow` rule group will
take effect before the `Reject` and `Alert` rules.

For more information about actions, see [Defining rule actions in AWS Network Firewall](rule-action.md "rule-action.md").

- **(Optional) `HOME_NET` rule group variable**
  – Used to expand the local network definition beyond the CIDR range of the VPC
  where you deploy Network Firewall. For additional information about this setting, see [Domain list inspection for traffic from outside
  the deployment VPC](#stateful-rule-groups-domain-names-home-net "#stateful-rule-groups-domain-names-home-net").

See the caveats for the `HOME_NET` and `EXTERNAL_NET`
settings at [Suricata features that Network Firewall supports with caveats](suricata-limitations-caveats.md#suricata-supported-with-caveats "suricata-limitations-caveats.md#suricata-supported-with-caveats").

###### Note

The console doesn't currently allow entry of all rule group variables. To specify
other rule group variables, use one of the APIs or AWS CloudFormation. For information, see
[StatefulRule](../APIReference/API_StatefulRule.md "../APIReference/API_StatefulRule.md") in the _AWS Network Firewall API Reference_ and [AWS::NetworkFirewall::RuleGroup StatefulRule](../../../AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.md") in the
_AWS CloudFormation User Guide_.

## Match settings

A domain list rule group has the following match
settings. These specify what the Network Firewall
stateful rules engine looks for in a packet. A
packet must satisfy all match settings to be a
match.

- **Domain list**
  – List of strings specifying the domain
  names that you want to match. A packet must match
  one of the domain specifications in the list to be
  a match for the rule group. Valid domain name
  specifications are the following:
  - Explicit names. For example,
    `abc.example.com` matches only the
    domain `abc.example.com`.
  - Names that use a domain wildcard, which you
    indicate with an initial '`.`'. For
    example,`.example.com` matches
    `example.com` and matches all
    subdomains of `example.com`, such as
    `abc.example.com` and
    `www.example.com`.

- **Protocols**
  – You can inspect HTTP or HTTPS protocols,
  or both.

For HTTPS traffic, Network Firewall uses the Server Name
Indication (SNI) extension in the TLS handshake to determine
the hostname, or domain name, that the client is trying to
connect to. For HTTP traffic, Network Firewall uses the HTTP
host header to get the name. In both cases, Network Firewall
doesn't pause connections to do out-of-band DNS lookups. It
uses the SNI or host header, not the IP addresses, when
evaluating domain list rule groups. If you want to inspect
IP addresses, to mitigate situations where the SNI or host
headers have been manipulated, write separate rules for that
and use them in conjunction with or in place of your domain
list rules.

For examples of domain list specifications and the
Suricata compatible rules that Network Firewall generates
from them, see [Stateful rules examples: domain list rules](suricata-examples.md#suricata-example-domain-filtering "suricata-examples.md#suricata-example-domain-filtering").

## Domain list inspection for traffic from outside

the deployment VPC

To use domain name filtering for traffic from outside
the VPC where you've deployed Network Firewall, you
must manually set the `HOME_NET` variable
for the rule group. The most common use case for
this is a central firewall VPC with traffic coming
from other VPCs through a transit gateway.

By default, domain list inspection uses a
`HOME_NET` that is set to the CIDR
range of the VPC where Network Firewall is deployed.
Only traffic from that range is passed through the
domain list filtering. To filter traffic from
outside the deployment VPC, you must provide a
`HOME_NET` setting that includes the
other CIDR ranges that you want to inspect, along
with the CIDR range of the VPC where Network Firewall
is deployed.

For example, say that the VPC where you deploy
Network Firewall has the CIDR range
`192.0.2.0/24`. In addition to the
traffic for that VPC, you want to filter traffic for
two other VPCs that have CIDR ranges
`10.0.0.0/16` and
`10.1.0.0/16`. You're using a domain
list rule group named `domains`.

The following command line call retrieves the JSON
listing for the rule group:

```
aws network-firewall describe-rule-group --type STATEFUL \
--rule-group-name domains --region us-west-2
```

The following shows the example JSON response. This
rule group has only `RulesSource`
defined, which contains the domain list inspection
specifications.

```
{
    "UpdateToken": "a4648a25-e315-4d17-8553-283c2eb33118",
    "RuleGroup": {
        "RulesSource": {
            "RulesSourceList": {
                "Targets": [
                    ".example.com",
                    "www.example.org"
                ],
                "TargetTypes": [
                    "HTTP_HOST",
                    "TLS_SNI"
                ],
                "GeneratedRulesType": "DENYLIST"
            }
        }
    },
    "RuleGroupResponse": {
        "RuleGroupArn": "arn:aws:network-firewall:us-west-2:111122223333:stateful-rulegroup/domains",
        "RuleGroupName": "domains",
        "RuleGroupId": "f3333333-fb99-11c1-bbe3-1d1caf1d1111",
        "Type": "STATEFUL",
        "Capacity": 100,
        "RuleGroupStatus": "ACTIVE",
        "Tags": []
    }
}
```

Variable settings are defined for a rule group in a
`RuleVariables` setting. This rule
group currently has no `HOME_NET`
variable declaration, so we know that
`HOME_NET` is set to the default. In
our example case, it's `192.0.2.0/24`.

To add CIDR ranges to the `HOME_NET`
setting, we update the rule group with our variable
declaration. The following shows a file named
`variables.json` that contains the rule
group JSON with the added variables settings:

```
{
    "RuleVariables": {
        "IPSets": {
           "HOME_NET": {
             "Definition": [
               "10.0.0.0/16",
               "10.1.0.0/16",
               "192.0.2.0/24"
             ]
           }
        }
    },
    "RulesSource": {
        "RulesSourceList": {
           "Targets": [
               ".example.com",
               "www.example.org"
           ],
           "TargetTypes": [
               "HTTP_HOST",
               "TLS_SNI"
           ],
           "GeneratedRulesType": "DENYLIST"
        }
    }
}
```

The following command uses the
`variables.json` file to update the
rule group definition with the correct
`HOME_NET` settings:

```
aws network-firewall update-rule-group \
--rule-group-arn arn:aws:network-firewall:us-west-2:111122223333:stateful-rulegroup/domains \
--update-token a4648a25-e315-4d17-8553-283c2eb33118 \
--rule-group file://variables.json \
--region us-west-2
```

The following shows an example response to the call:

```
{
    "UpdateToken": "32ebfb82-40a2-4896-b34d-91dada978f67",
    "RuleGroupResponse": {
        "RuleGroupArn": "arn:aws:network-firewall:us-west-2:111122223333:stateful-rulegroup/domains",
        "RuleGroupName": "domains",
        "RuleGroupId": "f3333333-fb99-11c1-bbe3-1d1caf1d1111",
        "Type": "STATEFUL",
        "Capacity": 100,
        "RuleGroupStatus": "ACTIVE",
        "Tags": []
    }
}
```

If we retrieve the `domains` rule group
again, we see that the rule group has the added
variable definition:

```
aws network-firewall describe-rule-group --type STATEFUL \
--rule-group-name domains --region us-west-2
```

The response JSON contains the added variable:

```
{
    "UpdateToken": "42ffac91-20b5-5512-a24c-85cbca797e23",
    "RuleGroup": {
        "RuleVariables": {
            "IPSets": {
                "HOME_NET": {
                    "Definition": [
                        "10.0.0.0/16",
                        "10.1.0.0/16",
                        "192.0.2.0/24"
                    ]
                }
            }
        },
        "RulesSource": {
            "RulesSourceList": {
                "Targets": [
                    ".example.com",
                    "www.example.org"
                ],
                "TargetTypes": [
                    "HTTP_HOST",
                    "TLS_SNI"
                ],
                "GeneratedRulesType": "DENYLIST"
            }
        }
    },
    "RuleGroupResponse": {
        "RuleGroupArn": "arn:aws:network-firewall:us-west-2:111122223333:stateful-rulegroup/domains",
        "RuleGroupName": "domains",
        "RuleGroupId": "f3333333-fb99-11c1-bbe3-1d1caf1d1111",
        "Type": "STATEFUL",
        "Capacity": 100,
        "RuleGroupStatus": "ACTIVE",
        "Tags": []
    }
}
```
