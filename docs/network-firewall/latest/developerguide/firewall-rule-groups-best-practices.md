

# Best practices for firewall rules

The following recommendations help you build firewall rule groups that behave predictably and are easy to maintain. The IPS engine uses standard Suricata compatible rules, so you can author IPS rules the same way you'd author rules for any Suricata deployment.
+ **Start from a drop-by-default posture.** Keep the firewall default action set to **Drop** and write accept rules only for the traffic you intend to allow. This is the firewall engine's security model—an allow list is easier to reason about than a denylist, and anything you forget to allow is blocked rather than exposed. Change the default action to **Accept** only when you have a specific reason to allow traffic by default.
+ **Validate in monitor mode before you enforce.** Roll out a new policy or a change in monitor mode, confirm from your alert logs and the `FirewallDefaultActionApplied` metric that the policy allows the traffic you expect, and only then switch to enforce mode. For the workflow, see [Policy mode: enforce and monitor](firewall-policy-v2-policy-mode.md).
+ **Include carrier rules for application-layer matches.** An application-layer rule (for example, a TLS SNI or HTTP host match) runs only after the connection passes the TCP layer. Pair each such rule with the `accept:hook tcp:all` carrier rules in both directions, or use the accept-prior-hooks setting. For more information, see [Accepting prior hooks automatically](firewall-rule-groups-accept-prior-hooks.md).
+ **Match a keyword at its own hook.** Place each protocol keyword at the hook where its data becomes available, rather than guessing or defaulting to `request_complete`. For the hook to use, see [Common hooks for common protocols](firewall-rule-constraints-protocol-hooks.md).
+ **Prefer transaction scope over flow scope.** For a firewall rule that accepts, drops, or rejects on a protocol that carries multiple transactions on one connection—such as HTTP keep-alive, where a single connection carries many requests—prefer scoping the rule to a transaction (`accept:tx`) rather than to a flow (`accept:flow`). Scoping to `tx` inspects each transaction on the connection, whereas scoping to `flow` applies the action to the whole flow and stops inspecting later transactions on that connection—so a reused connection that carries multiple requests is inspected only once. For example, prefer

  ```
  accept:tx http1:<request_headers any any -> any any (http.host; content:"example.com"; sid:1;)
  ```

  over

  ```
  accept:flow http1:<request_headers any any -> any any (http.host; content:"example.com"; sid:1;)
  ```

  TLS carries a single handshake transaction per flow, so `accept:tx` and `accept:flow` behave the same at a TLS hook. For example, the following rule allows TLS traffic by SNI and uses the accept-prior-hooks form (`<`) so that the earlier TLS states are accepted and the flow reaches `client_hello` under a drop-by-default policy:

  ```
  accept:tx tls:<client_hello any any -> any any (tls.sni; content:"example.com"; sid:1;)
  ```
+ **Set rule group capacity with room to grow.** You can't change a rule group's capacity after you create it, so estimate the number of rules you expect over its lifetime and leave headroom. For more information, see [Setting rule group capacity in AWS Network Firewall](rule-group-capacity-v2.md).
+ **Give each rule a descriptive `msg` and a stable SID.** A clear `msg` makes your alert logs readable, and a stable, unique SID makes a rule easy to find in logs and to manage over time. For the SID uniqueness requirement for embedded rules, see [Signature ID uniqueness](firewall-policy-v2-sid-uniqueness.md).
+ **Add alert logging to your blocking rules.** A `drop` or `reject` rule doesn't produce an alert log entry on a match unless you add the `alert` keyword—either chained to the action (`drop:flow,alert`) or as a rule option. Add it so that your logs show which traffic your blocking rules matched.
+ **Know what monitor mode does and doesn't block.** In monitor mode, a policy doesn't drop or reject traffic based on your rules, the firewall default action, or the stream exception policy. The exceptions are in TLS inspection, which still blocks these connections in monitor mode: connections with a revoked or unknown-status certificate when certificate revocation checking uses **Drop** or **Reject**, connections whose Server Name Indication (SNI) is missing or invalid, and connections where the server's certificate doesn't match the SNI. PostgreSQL (`pgsql`) connections can also be dropped in monitor mode because `pgsql` support is limited. Keep this in mind when you use monitor mode to validate a policy.
+ **Deploy in monitor mode before you enforce.** Deploy a new or changed Next Generation policy in monitor mode first, then switch to enforce mode after you've validated it against real traffic. In monitor mode the stream exception policy is **Continue**, so mid-stream connections aren't dropped. When you switch to enforce mode, your configured **Drop** or **Reject** stream exception policy takes effect and can drop or reset mid-stream connections that are affected by the change, so plan the cutover accordingly.
+ **Reuse rule groups instead of embedding rules when you can.** A referenced rule group can be shared across policies and accounts and managed independently. Reserve embedded rules for policy-specific rules that you don't need to reuse. For more information, see [The firewall section and the IPS section](firewall-policy-v2-sections.md).