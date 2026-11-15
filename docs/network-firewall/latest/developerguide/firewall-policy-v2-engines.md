

# The firewall engine and the IPS engine
<a name="firewall-policy-v2-engines"></a>

A Next Generation policy inspects traffic with two engines, in sequence. Traffic that an engine allows advances to the next engine; traffic that an engine blocks is dropped or rejected and does not advance.
+ **Firewall engine** – An access-control engine that inspects traffic at connection-state *hooks* as a connection progresses through the protocol stack. One way to think about the firewall engine is that it models the state machine of each protocol: a connection moves from one protocol state to the next (for example, through the states of a TLS handshake), and the engine evaluates your rules at each state. The firewall engine is *drop by default*, so an explicit accept is required to advance from one state to the next; traffic that isn't accepted is handled by the policy's firewall default action. You use the firewall engine to define which traffic is allowed into your network. For information about authoring firewall rules, see [Working with firewall rule groups in AWS Network Firewall](firewall-rule-groups.md).
+ **IPS engine** – An intrusion detection and prevention engine that inspects traffic for threats using Suricata compatible rules, in the same way as the stateful rules engine in a Classic Network Firewall policy. The IPS engine is *pass by default*: traffic that doesn't match a rule is allowed. You use the IPS engine to detect and block known threats in traffic that the firewall engine has already allowed. For information about authoring IPS rules, see [Working with IPS rule groups in AWS Network Firewall](ips-rule-groups.md).

Only traffic that the firewall engine accepts at every required hook advances to the IPS engine. For a detailed description of how traffic travels through the two engines, see [How Network Firewall filters traffic with a Next Generation policy](firewall-policy-processing-v2.md). The firewall engine is built on Suricata's firewall mode. To learn more about how firewall mode evaluates traffic at hooks, see the [Suricata firewall mode documentation](https://docs.suricata.io/en/suricata-8.0.3/firewall/firewall-design.html).

**Note**  
Next Generation policies don't use stateless rule groups. The functions that stateless rules provide in a Classic Network Firewall policy are provided by the firewall engine in a Next Generation policy.