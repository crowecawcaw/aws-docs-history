# Standard

stateful rule groups in AWS Network Firewall

AWS Network Firewall supports easy entry for standard stateful
rules for network traffic inspection. The match criteria for
this stateful rule type is similar to the Network Firewall
stateless rule.

All rule groups have the common settings that are defined at
[Common rule group settings in AWS Network Firewall](rule-group-settings.md "rule-group-settings.md").

###### General settings

A stateful basic rule has the following general
settings.

- **Action**
  – Defines how Network Firewall handles a
  packet that matches the rule match settings. Valid
  values are pass, drop, reject, and alert. For more
  information about actions, see [Defining rule actions in AWS Network Firewall](rule-action.md "rule-action.md").

###### Match settings

A basic stateful rule has the following match
settings. These specify what the Network Firewall
stateful rules engine looks for in a packet. To be a
match, a packet must satisfy all of the match
settings in the rule.

- **Protocol**
  – Transport protocol. Choose the protocol
  that you want to inspect. For all protocols, you
  can use `IP`, because all traffic on
  AWS and on the internet is IP.
- **Source IP**
  – Source IP addresses and ranges. If
  specified, a packet must come from a source
  address that's included in this list in order to
  match.
- **Source port**
  – Source ports and port ranges. If
  specified, a packet must have a source port that's
  included in this list in order to match.
- **Destination IP**
  – Destination IP addresses and ranges. If
  specified, a packet must have a destination
  address that's included in this list in order to
  match.
- **Destination
  port** – Destination ports and
  port ranges. If specified, a packet must have a
  destination port that's included in this list in
  order to match.
- **Traffic
  direction** – Direction of traffic
  flow. Valid settings are `Any` and
  `Forward`. `Forward` matches
  packets whose origination matches the rule's
  source settings and whose destination matches the
  rule's destination settings. `Any`
  matches the forward match, and also matches
  packets whose origination matches the rule's
  destination settings, and whose destination
  matches the rule's source settings.
- **Rule options**
  – Define the specifics of the rule, in
  keyword, settings pairs.

###### Note

The console doesn't currently allow entry of rule options. Rule options are usually required
for complete specification of this rule type. If you need to specify rule options, use one of the
APIs or AWS CloudFormation. For information, see [StatefulRule](../APIReference/API_StatefulRule.md "../APIReference/API_StatefulRule.md") in the
_AWS Network Firewall API Reference_ and [AWS::NetworkFirewall::RuleGroup StatefulRule](../../../AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-networkfirewall-rulegroup-statefulrule.md") in the
_AWS CloudFormation User Guide_.
For an example rule specification and the
Suricata compatible rule that Network Firewall generates
from it, see [Stateful rules examples: standard stateful rule groups](suricata-examples.md#suricata-example-basic "suricata-examples.md#suricata-example-basic").
