

# Context-aware rules in AWS Network Firewall

Context-aware rules match traffic by the *context* of its source and destination: the AWS resources, such as a VPC or subnet, that send and receive it. You can use context in addition to, or instead of, IP addresses and ports. A rule references these resources by their IDs, called *context IDs*. A context ID is the ID of a VPC, Amazon VPC security group, subnet, or transit gateway attachment. You can use a context ID in a rule's source position, its destination position, or both. For example, a rule can allow only application subnets to reach database subnets, or alert on all traffic from a quarantined Amazon VPC security group. Because the match is based on resource identity, a rule applies to every resource in the boundaries that it references, including resources created after you write the rule. Context-aware rules work in both the firewall and IPS rule groups of a Next Generation Firewall policy, and in the stateful rule groups of a Classic Network Firewall policy. For the policy kinds, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md).

Context-aware rules are supported only on transit gateway-attached network firewalls (see [Transit gateway-attached firewalls in Network Firewall](tgw-firewall.md)) and require a context store associated with the transit gateway. To set this up, see [Onboarding your transit gateway to a context store](context-aware-rules-setup.md).

You can use context in the following ways:
+ **Match on the traffic source** – The sending resource's identity is available on every packet of every flow, for all protocols. See [Writing context-aware rules](context-aware-rules-writing.md).
+ **Match on the traffic destination** – Destination matching requires TCP-based rules, because the firewall learns the receiving resource from return traffic. See [Matching on destination context](context-aware-rules-destination.md).
+ **Context in your logs** – Flow logs record each flow's context, even when no rule matches. See [Context in your network firewall logs](context-aware-rules-logging.md).