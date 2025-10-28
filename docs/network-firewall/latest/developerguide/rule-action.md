# Defining rule actions in AWS Network Firewall

The rule action setting tells AWS Network Firewall how to handle a packet that matches the
rule's match criteria.

## Actions for stateless rules

The action options for stateless rules are the same as for the firewall policy's
default stateless rule actions.

You are required to specify one of the following options:

- **Pass** – Discontinue all inspection of the packet and permit it to go to its intended destination.
- **Drop** – Discontinue all inspection of the packet and block it from going to its intended destination.
- **Forward to stateful rules** –
  Discontinue stateless inspection of the packet and forward it to the stateful rule engine for inspection.

Additionally, you can optionally specify a named custom action to apply. For this action, Network Firewall
assigns a dimension to Amazon CloudWatch metrics with the name set to `CustomAction` and a value that you specify.
For more information, see [AWS Network Firewall metrics in Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

After you define a named custom action, you
can use it by name in the same context as where you defined it. You can reuse a custom action setting among the rules in a rule group and you
can reuse a custom action setting between the two default stateless custom action settings for a firewall policy.

## Actions for stateful rules

The actions that you specify for your stateful rules help determine the
order in which the Suricata stateful rules engine processes them.
Network Firewall supports the Suricata rule actions pass, drop, reject, and alert. By default, the engine processes rules in the order of pass
action, drop action, reject action, and then finally alert action. Within each action, you
can set a priority to indicate processing order. For more
information, see [Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md "suricata-rule-evaluation-order.md").

Stateful rules can send alerts to the firewall's logs, if you have logging
configured. To see the alerts, you must enable logging for the firewalls that use
the rules. Logging incurs additional costs. For more information, see [Logging network traffic from AWS Network Firewall](firewall-logging.md "firewall-logging.md").

The options for stateful action settings vary by rule type.

###### Standard rules and Suricata compatible strings

You specify one of the following action options for both the rules
that you provide in Suricata compatible strings and the
rules that you specify using the standard stateless rules interface
in Network Firewall. These options are a subset of the action
options that are defined by Suricata. For more information,
see [Working with stateful rule groups in
AWS Network Firewall](stateful-rule-groups-ips.md "stateful-rule-groups-ips.md").

- **Pass** – Discontinue inspection of
  the matching packet and permit it to go to its intended destination. Rules with pass
  action are evaluated before rules with other action settings.
- **Drop** or **Alert**– Evaluate
  the packet against all rules with drop or alert action settings. If the firewall has alert logging
  configured, send a message to the firewall's alert logs for each matching rule. The first log entry
  for the packet will be for the first rule that matched the packet.

After all rules have been evaluated, handle the packet according to the the action setting in the
first rule that matched the packet. If the first rule has a drop action, block the packet. If it has an alert action,
continue evaluation.

- **Reject** – Drop traffic that matches the conditions of the stateful rule and send a TCP reset packet back to sender of the packet. A TCP reset packet is a packet with no payload and a `RST` bit contained in the TCP header flags. `Reject` is available only for TCP traffic. This option doesn't support FTP and IMAP protocols.

###### Note

Matching a `drop` or `alert` rule for a packet doesn't necessarily mean the end of rule
processing for that packet. The engine continues evaluating other rules for matches. For example, if there's a
`drop` match that drops a packet, the packet can still go on to match an `alert` rule
that generates alert logs. Matching an `alert` rule also doesn't imply a `pass`. The packet can
go on to match a `drop` rule, and drop the packet after it's previously matched an `alert` rule.

For information about what you can do to manage the evaluation order of your stateful rules, see
[Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md "suricata-rule-evaluation-order.md").

###### Domain lists

The domain list rule group has one action setting at the rule
group level. You specify one of the following options:

- **Allow** – Indicates that the domain
  name list is to be used as an allow list for all traffic that matches
  the specified protocols. For matching packets, discontinue
  inspection of the packet and permit it to pass to its intended destination.
  For non-matching packets, discontinue inspection of the packet, block it from
  going to its intended destination, and send a message to the firewall's alert
  logs if the firewall has alert logging configured.
- **Deny** – Indicates that the domain
  name list is to be used as a deny list for traffic that matches
  the specified protocols. For matching packets, discontinue inspection of the
  packet, block it from going to its intended destination, and send a message
  to the firewall's alert logs if the firewall has alert logging configured.
  For non-matching packets, take no action.
