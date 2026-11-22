

# Firewall engine hooks

The firewall engine evaluates rules at *hooks*—connection-state inspection points that a connection reaches as it progresses through the protocol stack. A rule's hook determines when Network Firewall evaluates it. For example, a rule at a TLS hook is evaluated when the connection reaches that point in the TLS handshake. In the console, these are called **Connection state**. You can read more about the available hooks and the connection states they correspond to in the [Suricata firewall mode documentation](https://docs.suricata.io/en/suricata-8.0.3/firewall/firewall-design.html).

Because the firewall engine is drop by default, a connection advances through the hooks only as long as it keeps being accepted. A rule at a later hook is reached only if the connection is accepted at every earlier hook. To avoid having to author those earlier accepts yourself, use the accept prior hooks setting described in [Accepting prior hooks automatically](firewall-rule-groups-accept-prior-hooks.md).