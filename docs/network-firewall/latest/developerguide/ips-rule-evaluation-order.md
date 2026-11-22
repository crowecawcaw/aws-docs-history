

# Managing evaluation order for IPS rules

The IPS engine evaluates rules by action order. The order in which the IPS engine evaluates rules is determined by the following settings, listed in order of precedence:

1. The Suricata `action` specification. This takes highest precedence.

   Actions are processed in the following order:

   1. `pass`

   1. `drop`

   1. `reject`

   1. `alert`
**Note**  
If a packet within a flow matches a rule containing `pass` action, then Suricata doesn't scan the other packets in that flow and it passes the unscanned packets.

   For more information about the action specification, see [Suricata.yaml: Action-order](https://docs.suricata.io/en/suricata-8.0.3/configuration/suricata-yaml.html?highlight=action+order#action-order) in the [Suricata User Guide](https://docs.suricata.io/en/suricata-8.0.3/index.html).

1. The Suricata `priority` keyword. Within a specific action group, you can use the priority setting to indicate the processing order. By default, Suricata processes from the lowest numbered priority setting on up. The `priority` keyword has a mandatory numeric value ranging from 1 to 65535.

   For more information about priority, see [Meta Keywords: priority](https://docs.suricata.io/en/suricata-8.0.3/rules/meta.html?highlight=priority#priority) in the [Suricata User Guide](https://docs.suricata.io/en/suricata-8.0.3/index.html).

For example, the IPS engine evaluates all `pass` rules before evaluating any `drop`, `reject`, or `alert` rules, regardless of the value of priority settings. Within all `pass` rules, if priority keywords are present, Suricata orders the processing according to them.

The protocol layer does not impact the rule evaluation order. If you want to avoid matching against lower-level protocol packets before higher-level application protocols can be identified, consider using the `flow` keyword in your rules. This is needed because, for example, a TCP rule might match on the first packet of a TCP handshake before the engine can identify the application protocol. For information about the `flow` keyword, see [Flow Keywords](https://docs.suricata.io/en/suricata-8.0.3/rules/flow-keywords.html).