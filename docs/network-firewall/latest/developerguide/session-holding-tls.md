

# Using session holding with TLS inspection in AWS Network Firewall

**Before you use session holding**  
To use session holding, you must have TLS Inspection configuration and TLS Inspection enabled in your firewall policy. For information, see [Creating a firewall policy in AWS Network Firewall](firewall-policy-creating.md).  
Application drop established (bidirectional) and Application drop established (server-directed only) default rules are incompatible with a session-holding configuration. For more information, see [Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md).

Network Firewall session holding enhances TLS inspection security by controlling when TCP and TLS establishment packets reach destination servers. When enabled, Network Firewall holds these packets until it evaluates TLS Inspection rules for Server Name Indication (SNI).

**Turning on session holding**  
How you turn on session holding depends on your firewall policy type.
+ For a Classic Network Firewall policy, session holding is optional and off by default. In the firewall policy's traffic inspection settings, under **TLS inspection configurations**, select a TLS inspection configuration, and then select **Enable session holding**. The option is available only after you select a TLS inspection configuration. You can change this setting after you create the policy: on the policy's details page, in the **TLS inspection configuration** section, choose **Manage TLS inspection configuration**. The policy's details show a **Session holding** column that reads **Active** or **Inactive**.
+ With the API or AWS CLI, set `EnableTLSSessionHolding` to `true` on the firewall policy. This requires an associated TLS inspection configuration.
+ 
**Important**  
For a Next Generation policy, session holding is always on. The **Enable session holding** option appears already selected and can't be cleared, and there is no corresponding API field. For more information, see [TLS inspection with a Next Generation policy in AWS Network Firewall](tls-inspection-policy-v2.md).

**Session holding behavior**  
You can enable session holding in your firewall policy when you have an associated TLS Inspection configuration. The behavior differs depending on whether session holding is enabled.

Without session holding, Network Firewall immediately initiates TCP/TLS handshakes with downstream servers when client connections begin. This means the handshake between the firewall and downstream server occurs before SNI information is available. Although deny rules can still block connections after evaluation, downstream servers receive the initial connection attempts.

With session holding, Network Firewall waits for SNI information from the client's TLS handshake before initiating downstream connections. This lets the firewall evaluate TLS SNI-based rules first, preventing any connection attempts to blocked domains from reaching downstream servers.

**Rule evaluation**  
Session holding affects how Network Firewall evaluates TLS.SNI and HTTP rules.

Without session holding, Network Firewall evaluates TLS.SNI and HTTP rules simultaneously after establishing the downstream server connection.

With session holding, Network Firewall evaluates TLS.SNI rules first while holding the client-side connection, then evaluates HTTP rules. When a connection passes a TLS rule, Network Firewall stops evaluating HTTP rules for that connection.

**Tip**  
For best results with session holding, configure TLS rules that match on SNI in a deny list format. Use HTTP-based rules to process connections that aren't in the deny list.

**Note**  
With session holding enabled, both `TLS.SNI`-based rules and L3/L4 rules become match candidates. This applies to the packet that contains the `TLS.SNI` when the Client Hello is sent. Because Network Firewall treats this packet as belonging to a not-established flow, Network Firewall can match rules that use keywords such as `flow:not_established`. Your L3/L4 rules must account for this flow state to avoid unexpected behavior.