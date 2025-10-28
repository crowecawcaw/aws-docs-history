# Best practices for writing

Suricata compatible rules for AWS Network Firewall

A stateful rule group is a rule group that uses Suricata compatible intrusion
prevention system (IPS) specifications. Suricata is an open source network
IPS that includes a standard rule-based language for stateful network
traffic inspection.
You can enter any stateful rule in Suricata compatible strings.

When you write your stateful rules, verify the configuration of the firewall policy where
you intend to use them, to make sure that all of your rules evaluate as you want
them to. For information about how AWS Network Firewall handles network traffic and
when it sends it to the stateful engine, see [How AWS Network Firewall filters network traffic](firewall-policy-processing.md "firewall-policy-processing.md").

For example, many stateful rules rely on seeing a complete bidirectional traffic
flow for correct evaluation, such as rules with options like `flow:
 established`. To use rules like this, you must configure your stateless
rules and default actions to ensure forwarding of traffic for both directions to the
stateful engine. For information about these action options, see [Defining rule actions in AWS Network Firewall](rule-action.md "rule-action.md").
