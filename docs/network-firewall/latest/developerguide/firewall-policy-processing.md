# How AWS Network Firewall filters network traffic

When AWS Network Firewall inspects a packet, it evaluates the packet against the rules in the
policy's stateless rule groups first, using the stateless rules engine. Then,
depending on that inspection and on other settings in the policy, it might evaluate
the packets against the rules in the policy's stateful rule groups, using the
stateful rules engine.

###### 1. Stateless rules engine

Network Firewall evaluates each packet against the firewall policy's stateless rules until it
finds a match or exhausts all of the stateless rules. Network Firewall evaluates
the rule groups in the order that they are prioritized in the policy, starting
from the lowest setting. Within each rule group, Network Firewall evaluates the
rules in the order that they are prioritized in the rule group, starting from
the lowest setting. When you create a stateless rule group, you set the priority
of the rules in the rule group. When you create a firewall policy, you set the
priority of the stateless rule groups in the policy. For more information, see
[Working with stateless rule groups in
AWS Network Firewall](stateless-rule-groups-standard.md "stateless-rule-groups-standard.md") and [Firewall policies in AWS Network Firewall](firewall-policies.md "firewall-policies.md").

When Network Firewall finds a match, it handles the packet according to the matching rule's
configuration. You configure a stateless rule to pass the packet through, drop it,
or forward it to your stateful rules. Additionally, you can configure a stateless
rule to perform a custom action, for example you can publish metrics for the packet
to Amazon CloudWatch. For more information, see [Defining rule actions in AWS Network Firewall](rule-action.md "rule-action.md").

###### 2. Default stateless rule actions

If a packet doesn't match any stateless rule, Network Firewall performs the firewall policy's
default stateless rule action for full packet or UDP packet fragment, depending on
the packet type. Network Firewall only applies the fragment action setting to UDP packet fragments,
and silently drops packet fragments for other protocols.
The options for these actions settings are the same as for
stateless rules. For more information, see [Defining rule actions in AWS Network Firewall](rule-action.md "rule-action.md").

###### 3. Stateful rules engine

When Network Firewall forwards a packet to the stateful engine for inspection, it inspects
each packet against the stateful rule groups, in the context of the packet's
traffic flow. You can configure a stateful rule to pass the packet through, with
or without an alert, or drop it and send an alert. Alerts require logging to be
configured for the firewall.

The Suricata stateful rules engine controls how the stateful rules in your firewall policy
are processed. The engine evaluates the packet's traffic flow against the conditions
in the policy's stateful rules until it finds a match or exhausts all of the rules.
When the engine finds a match, it handles the packet according to the rule's
configuration. By default, the Suricata stateful rules engine orders rule processing
according to the rule action setting, processing first the rules with pass action,
then drop, then alert. For more information, see [Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md "suricata-rule-evaluation-order.md") and the [Suricata Action-order documentation](https://suricata.readthedocs.io/en/suricata-7.0.8/configuration/suricata-yaml.html#action-order "https://suricata.readthedocs.io/en/suricata-7.0.8/configuration/suricata-yaml.html#action-order").

Depending on the Suricata compatible rules that you provide, the stateful engine
might perform deep packet inspection of your traffic. Deep packet inspection works
on the payload data within your packets, rather than on the header information.

For more information about stateful rules, see [Managing your own rule groups in AWS Network Firewall](rule-groups.md "rule-groups.md").
