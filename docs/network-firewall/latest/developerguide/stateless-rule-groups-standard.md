# Working with stateless rule groups in

AWS Network Firewall

For stateless rule groups, the AWS Network Firewall stateless rules engine examines each packet
in isolation. Network Firewall doesn't consider context such as traffic direction or other
related packets.

Network Firewall supports standard network connection identifiers (source IP address, source port, destination IP address, destination port, and protocol) for network traffic inspection. When Network Firewall finds a match between a rule's inspection
criteria and a packet, we say that the packet matches the rule and its rule group, and
Network Firewall applies the rule's specified action to the packet.

You can add multiple stateless rules to your stateless rule group.

All rule groups have the common settings that are defined at [Common rule group settings in AWS Network Firewall](rule-group-settings.md "rule-group-settings.md").

###### General settings

A stateless rule has the following general settings.

- **Priority** – Number that indicates the processing
  order of the stateless rule within the rule group. This must
  be unique within the stateless rule group and it must be a
  positive integer. Network Firewall processes the rules starting
  from the lowest numbered priority setting. When you plan the
  rules in your rule group, provide priority settings with
  space in between, to leave yourself room to add rules later.
  For example, you might start by using priority settings that
  are multiples of 100.
- **Actions** – Defines how Network Firewall handles a
  packet that matches the rule match settings. You assign one standard setting,
  from among pass, drop, and forward to stateful. You can optionally add a custom
  setting, for example, to send metrics for the rule match to Amazon CloudWatch metrics.
  For more information about actions, see [Defining rule actions in AWS Network Firewall](rule-action.md "rule-action.md").

###### Match settings

A stateless rule has the following match settings. These specify what the
Network Firewall stateless rules engine looks for in a packet. To be a match, a packet
must satisfy all of the match settings in the rule.

- **Protocol** – Valid settings include
  `ALL` and specific protocol settings, like `UDP` and
  `TCP`. You can choose more than one specific setting.
- **Source IP** – Source IP addresses and
  ranges. If specified, a packet must come from a source address that's included
  in this list in order to match.
- **Source port range** – Source ports and
  port ranges. If specified, a packet must have a source port that's included in
  this list in order to match.
- **Destination IP** – Destination IP addresses
  and ranges. If specified, a packet must have a destination address that's
  included in this list in order to match.
- **Destination port range** – Destination
  ports and port ranges. If specified, a packet must have a destination port
  that's included in this list in order to match.
- **Optional TCP flags** – Optional, standard TCP flag
  settings, which indicate which flags to inspect and the values to inspect for.
  Each flag can be either enabled or disabled. You indicate the flags that you
  want to inspect in a masks setting, and then you indicate which of those flags
  must be enabled in the flags setting in order to match. The flags that you
  specify in the masks setting and don't specify in the flags setting must be
  unset in order to match.

###### Example

To create a very simple stateless rule group that passes all traffic from two CIDR blocks,
you could provide the following stateless rule settings in a single rule:

- **Priority** – `100`
- **Action** – `PASS`
- **Protocol** – `ALL`
- **Source** – `192.0.2.0/8`,
  `198.51.100.0/16`
  To block all other traffic, you would set the firewall policy's stateless default
  actions to `Drop`. For more information, see [Firewall policy settings in AWS Network Firewall](firewall-policy-settings.md "firewall-policy-settings.md").
