

# Managing evaluation order for firewall rules
<a name="firewall-rule-evaluation-order"></a>

You control the order in which the firewall engine evaluates rule groups through the priority that you assign to each entry in the policy's firewall section. Each entry—whether it references a rule group or embeds one directly in the policy—has a unique priority. The firewall engine evaluates the entries by order of priority, starting from the lowest number, and within each rule group it processes the rules in the order in which they're defined. For information about adding entries and setting their priority, see [The firewall section and the IPS section](firewall-policy-v2-sections.md).

The firewall engine matches rules in this defined order regardless of each rule's action. It does not reorder rules by action—a rule that comes earlier in the order is evaluated before a later rule even if the later rule has a different action. This differs from the IPS engine, which evaluates rules by action order. For how the IPS engine orders rules, see [Managing evaluation order for IPS rules](ips-rule-evaluation-order.md).

Within a connection, the firewall engine evaluates rules at each connection-state hook that the connection reaches. For how a rule's hook and action scope determine when and how much of the traffic a rule applies to, see [Firewall engine hooks](firewall-rule-groups-hooks.md) and [Firewall engine actions and scopes](firewall-rule-groups-verdicts.md).

**Firewall default action**  
The firewall engine is drop by default. When a connection passes through a hook that no firewall rule handles, the firewall engine applies the policy's *firewall default action*. You configure the firewall default action as one of the following:
+ **Accept** – Allow the traffic at the hook.
+ **Drop** – Block the traffic. This is the default.
+ **Reject** – Block the traffic and send a TCP reset packet back to the client.
+ **Alert** – Allow the traffic at the hook, the same as **Accept**, and also record an alert log entry. The difference between **Alert** and **Accept** is that **Alert** produces alert logs in addition to accepting the hook.

For more information about the firewall default action, see [Firewall default action](firewall-policy-v2-default-action.md).