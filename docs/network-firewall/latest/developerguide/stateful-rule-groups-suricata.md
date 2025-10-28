# Suricata compatible rule strings in

AWS Network Firewall

When you use this rule group type, you provide match and action
settings in a string, in a Suricata compatible
specification. Your specification fully defines what the
stateful rules engine looks for in a traffic flow and the
action to take on the packets in a flow that matches the
inspection criteria.

All rule groups have the common settings that are defined at
[Common rule group settings in AWS Network Firewall](rule-group-settings.md "rule-group-settings.md").

You can provide your Suricata compatible specification to
Network Firewall in rules strings or files, depending on how
you're accessing Network Firewall.

- **Console** – In the AWS Management Console, provide
  the rules string in the text box that appears for the stateful rule group
  option **Import Suricata compatible rules**. For
  information about using the console to manage your rule group, see [Creating a stateful rule group](rule-group-stateful-creating.md "rule-group-stateful-creating.md").
- **API** – Through the
  API, you can provide either the rules or the name
  of the file that contains the rules. In a file,
  Suricata compatible rules are usually written
  one rule per line.

You provide either the file or the rules string in the
`RulesString` field within the `RuleGroup`
structure when you create or update the rule group. For information, see
[CreateRuleGroup](../APIReference/API_CreateRuleGroup.md "../APIReference/API_CreateRuleGroup.md") in the
_AWS Network Firewall API Reference_.

- **CLI** – Through the CLI, you can
  provide the rules, the name of a file that contains the rules, or the name
  of a file that contains the rule group structure in JSON format, with the
  rules defined in that.

The following listing shows the syntax for providing the rules in a file.
To use a command like this, substitute in your new rule group name, its
calculated capacity, and the JSON rules file name.

```
aws network-firewall create-rule-group --rule-group-name <ruleGroupName> --capacity <capacityCalculation> --type STATEFUL --rules <rules file name>
```
