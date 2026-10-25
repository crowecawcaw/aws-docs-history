

# Stateful domain list rule groups in AWS Network Firewall
<a name="stateful-rule-groups-domain-names"></a>

AWS Network Firewall supports domain name stateful network traffic inspection. You can create allow lists and deny lists with domain names that the stateful rules engine looks for in network traffic. 

You can also match on the domain that a connection's destination IP address was resolved for, not only the domain that the client asserts in its TLS Server Name Indication (SNI) or HTTP `Host` header. To do this, use the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type. For more information, see [Resolved IP validation in AWS Network Firewall](route53-resolved-ip-validation.md).

**Note**  
AWS Marketplace managed rule groups use a `stateful-domain-rulegroup` resource type that is available only with managed rules. This resource type uses capacity from your firewall policy's total available domain capacity. Only AWS Marketplace managed rule groups can use this capacity. For more information, see [Firewall policy settings in AWS Network Firewall](firewall-policy-settings.md) and [AWS Network Firewall quotas](quotas.md).

All rule groups have the common settings that are defined at [Common rule group settings in AWS Network Firewall](rule-group-settings.md).

## General settings
<a name="stateful-rule-groups-domain-names-general-settings"></a>

A domain list rule group has the following general settings.
+ **Action** – Defines how Network Firewall handles traffic that matches the rule match settings. Valid values for domain rules are `Allow`, `Deny`, `Reject`, and `Alert`:
  + For `Allow`, the firewall denies traffic of the specified protocol type that does not match the domain specifications. This denial applies only when the firewall policy uses default action order. Under strict order, this denial does not apply.
  + For `Deny`, traffic matching the domain specifications is blocked. Non-matching traffic is allowed to pass.
  + For `Reject`, traffic matching the domain specifications is blocked and a TCP reset packet is sent back to the source. This option is only available for TCP traffic.
  + For `Alert`, traffic matching the domain specifications generates an alert in the firewall's logs (when logging is enabled). Then, traffic either passes, is rejected, or drops based on other rules in the firewall policy.
**For firewall policies that use default action ordering**  
We recommend that you avoid combining `Reject` or `Alert` domain list rule groups with `Allow` domain list rule groups. When this combination of rule groups is defined in a firewall policy that uses default action ordering, the default drop rule added by the `Allow` rule group will take effect before the `Reject` and `Alert` rules.

  For more information about actions, see [Defining rule actions in AWS Network Firewall](rule-action.md).
+ **(Optional) `HOME_NET` rule group variable** – Used to expand the local network definition beyond the CIDR range of the VPC where you deploy Network Firewall. For additional information about this setting, see [Domain list inspection for traffic from outside the deployment VPC](#stateful-rule-groups-domain-names-home-net).

  See the caveats for the `HOME_NET` and `EXTERNAL_NET` settings at [Suricata features that Network Firewall supports with caveats](suricata-limitations-caveats.md#suricata-supported-with-caveats).
**Note**  
The console doesn't allow entry of all rule group variables. To specify other rule group variables, use one of the APIs or AWS CloudFormation. For information, see [StatefulRule](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_StatefulRule.html) in the *AWS Network Firewall API Reference* and [AWS::NetworkFirewall::RuleGroup StatefulRule](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.html) in the *AWS CloudFormation User Guide*.

## Match settings
<a name="stateful-rule-groups-domain-names-match-settings"></a>

A domain list rule group has the following match settings. These specify what the Network Firewall stateful rules engine looks for in a packet. A packet must satisfy all match settings to be a match. 
+ **Domain list** – List of strings specifying the domain names that you want to match. A packet must match one of the domain specifications in the list to be a match for the rule group. Valid domain name specifications are the following: 
  + Explicit names. For example, `abc.example.com` matches only the domain `abc.example.com`.
  + Names that use a domain wildcard, which you indicate with an initial '`.`'. For example,`.example.com` matches `example.com` and matches all subdomains of `example.com`, such as `abc.example.com` and `www.example.com`. 
+ **Protocols** – You can inspect HTTP or HTTPS protocols, or both. You can also match on the domain that the connection's destination IP address was resolved for, by using the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type. For more information, see [Resolved IP validation in AWS Network Firewall](route53-resolved-ip-validation.md).

For HTTPS traffic, Network Firewall uses the Server Name Indication (SNI) extension in the TLS handshake to determine the hostname, or domain name, that the client is trying to connect to. For HTTP traffic, Network Firewall uses the HTTP host header to get the name. In both cases, Network Firewall doesn't pause connections to do out-of-band DNS lookups. It uses the SNI or host header, not the IP addresses, when evaluating domain list rule groups. If you want to inspect IP addresses, to mitigate situations where the SNI or host headers have been manipulated, write separate rules for that and use them together with or instead of your domain list rules. Alternatively, to match on the domain that a connection's destination IP address was resolved for, add the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type.

When you include the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type, how it combines with `TLS_SNI` and `HTTP_HOST` depends on the generated rules type:
+ In an allow list that also uses a protocol target type, the rule allows traffic only when *both* conditions match: the SNI or `Host` header matches the domain, *and* the destination IP address was resolved for that domain. If a client sets the `Host` header to an allowed domain but connects to an IP address that was never resolved for that domain, the check fails and the connection isn't allowed.
+ In a deny list, or when `AWS_ROUTE_53_RESOLVED_DOMAIN` is the only target type, Network Firewall enforces each condition independently. A match on either the SNI or `Host` header, or on the resolved destination IP address, triggers the rule.

**Note**  
An allow list whose only target type is `AWS_ROUTE_53_RESOLVED_DOMAIN` is additive: it allows matching traffic but doesn't add a default rule that drops non-matching traffic. Only the `TLS_SNI` and `HTTP_HOST` target types add that default drop. To allow only the resolved domains and drop all other traffic, include a protocol target type as well.

When you save a domain list rule group, Network Firewall generates Suricata compatible rules from your domain list and target types. Which traffic those rules match depends on the target type:
+ `TLS_SNI` generates rules that match *HTTPS only*, using the TLS SNI.
+ `HTTP_HOST` generates rules that match *HTTP only*, using the HTTP `Host` header.
+ `AWS_ROUTE_53_RESOLVED_DOMAIN` generates rules that match at the IP layer, *across all protocols*. A resolved IP match is a property of the destination IP address, not of an application protocol. Therefore, a standalone resolved-domain rule matches any traffic to that IP address, regardless of protocol. The exception is an allow list that also uses `TLS_SNI` or `HTTP_HOST`. In that case, Network Firewall combines the resolved-domain condition into the protocol rule, and the condition inherits that rule's protocol scope.

A domain list rule group therefore inspects only HTTP and HTTPS (`TLS_SNI` and `HTTP_HOST`), or all protocols (`AWS_ROUTE_53_RESOLVED_DOMAIN`). It can't scope matching to a single specific protocol or to particular ports. If you want to match a domain for one specific protocol only, or restrict matching by port, don't use a domain list rule group. Instead, write Suricata compatible stateful rules, in which you specify the protocol, ports, and keywords explicitly, or use standard stateful (5-tuple) rules. For more information, see [Suricata compatible rule strings in AWS Network Firewall](stateful-rule-groups-suricata.md) and [Standard stateful rule groups in AWS Network Firewall](stateful-rule-groups-basic.md).

**Note**  
The `Reject` action applies only to TCP. When you use `Reject` with the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type, Network Firewall generates the resolved-domain rule on TCP only (instead of all protocols) so that it can send the TCP reset. Because the generated rule matches TCP only, non-TCP traffic to a resolved IP address doesn't match the rule at all. Network Firewall neither rejects nor drops that traffic. Use `Deny` instead to block a resolved domain across all protocols.

For examples of domain list specifications and the Suricata compatible rules that Network Firewall generates from them, see [Stateful rules examples: domain list rules](suricata-examples.md#suricata-example-domain-filtering).

## Domain list inspection for traffic from outside the deployment VPC
<a name="stateful-rule-groups-domain-names-home-net"></a>

To use domain name filtering for traffic from outside the VPC where you've deployed Network Firewall, you must manually set the `HOME_NET` variable for the rule group. The most common use case for this is a central firewall VPC with traffic coming from other VPCs through a transit gateway. 

By default, domain list inspection uses a `HOME_NET` that is set to the CIDR range of the VPC where Network Firewall is deployed. Only traffic from that range is passed through the domain list filtering. To filter traffic from outside the deployment VPC, you must provide a `HOME_NET` setting that includes the other CIDR ranges that you want to inspect, along with the CIDR range of the VPC where Network Firewall is deployed. 

For example, say that the VPC where you deploy Network Firewall has the CIDR range `192.0.2.0/24`. In addition to the traffic for that VPC, you want to filter traffic for two other VPCs that have CIDR ranges `10.0.0.0/16` and `10.1.0.0/16`. You're using a domain list rule group named `domains`. 

The following command line call retrieves the JSON listing for the rule group:

```
aws network-firewall describe-rule-group --type STATEFUL \
--rule-group-name domains --region us-west-2
```

The following shows the example JSON response. This rule group has only `RulesSource` defined, which contains the domain list inspection specifications. 

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

Variable settings are defined for a rule group in a `RuleVariables` setting. This rule group currently has no `HOME_NET` variable declaration, so we know that `HOME_NET` is set to the default. In our example case, it's `192.0.2.0/24`. 

To add CIDR ranges to the `HOME_NET` setting, we update the rule group with our variable declaration. The following shows a file named `variables.json` that contains the rule group JSON with the added variables settings:

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

The following command uses the `variables.json` file to update the rule group definition with the correct `HOME_NET` settings:

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

If we retrieve the `domains` rule group again, we see that the rule group has the added variable definition:

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