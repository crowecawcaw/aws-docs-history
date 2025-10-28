# Using session holding with TLS inspection in AWS Network Firewall

###### Before you use session holding

To use session holding, you must have TLS Inspection configuration and TLS Inspection enabled in your firewall policy. For information, see [Creating a firewall policy in AWS Network Firewall](firewall-policy-creating.md "firewall-policy-creating.md").

Network Firewall session holding enhances TLS inspection security by controlling when TCP and TLS establishment packets reach destination servers. When enabled, Network Firewall holds these packets until it evaluates TLS Inspection rules for Server Name Indication (SNI).

###### Session holding behavior

You can enable session holding in your firewall policy when you have an associated TLS Inspection configuration. The behavior differs depending on whether session holding is enabled.

Without session holding, Network Firewall immediately initiates TCP/TLS handshakes with downstream servers when client connections begin. This means the handshake between the firewall and downstream server occurs before SNI information is available. While deny rules can still block connections after evaluation, downstream servers receive the initial connection attempts.

With session holding, Network Firewall waits for SNI information from the client's TLS handshake before initiating downstream connections. This lets the firewall evaluate TLS SNI-based rules first, preventing any connection attempts to blocked domains from reaching downstream servers.

###### Rule evaluation

Session holding affects how Network Firewall evaluates TLS.SNI and HTTP rules.

Without session holding, Network Firewall evaluates TLS.SNI and HTTP rules simultaneously after establishing the downstream server connection.

With session holding, Network Firewall evaluates TLS.SNI rules first while holding the client-side connection, then evaluates HTTP rules. When a connection passes a TLS rule, Network Firewall stops evaluating HTTP rules for that connection.

###### Tip

For best results with session holding, configure TLS rules that match on SNI in a deny list format. Use HTTP-based rules to process connections that aren't in the deny list.
