

# How Network Firewall filters traffic with a Next Generation policy

A Next Generation policy doesn't use stateless rule groups. Traffic travels through a firewall engine and then an IPS engine.

**1. Firewall engine**  
The firewall engine evaluates the traffic at each connection-state hook (in the console, a **Connection state**) that the connection reaches, in the priority order of the firewall section's rules. The firewall engine is drop by default, so a connection advances only if it's accepted at every required hook. Traffic that isn't accepted is handled by the policy's firewall default action. You configure the firewall default action: it's **Drop** by default (recommended), and you can also choose **Accept**, **Alert**, or **Reject**. For more information, see [Firewall default action](firewall-policy-v2-default-action.md).

**2. IPS engine**  
Traffic that the firewall engine accepts advances to the IPS engine. The IPS engine inspects the traffic for threats using Suricata compatible rules, in the context of the traffic flow. The IPS engine is pass by default and evaluates its rules in the default action order, so traffic that doesn't match a drop or reject rule continues to its destination. This engine behaves the same way as the stateful rules engine in a Classic Network Firewall policy that evaluates rules in the default action order.

A firewall rule can allow a connection to skip IPS inspection entirely. When you accept a connection in the firewall engine, you can also direct that connection to bypass the IPS engine, so that accepted traffic advances to its destination without threat inspection. For information about authoring this behavior, see [Bypassing the IPS engine for accepted traffic](firewall-rule-ips-bypass.md).

For more information about the two engines and how to author rules for them, see [Next Generation policies](firewall-policies-v2.md) and [Rule groups for Next Generation policies](rule-groups-v2.md).