

# Firewall engine actions and scopes

A firewall rule applies one of the following actions when it matches:
+ **Accept** – Allow the traffic.
+ **Drop** – Block the traffic and discontinue inspection.
+ **Reject** – Block the traffic and send a TCP reset packet back to the client. Reject applies to TCP traffic; for non-TCP protocols, reject behaves the same as drop.
+ **Reject destination** (`REJECT_DST`) – Block the traffic and send a TCP reset packet to the destination.
+ **Reject both** (`REJECT_BOTH`) – Block the traffic and send a TCP reset packet to both the client and the destination.

**Note**  
A `drop` or `reject` rule blocks matching traffic but doesn't record an alert log entry unless you add the `alert` keyword to the rule—either chained to the action, as in `drop:flow,alert`, or as a rule option. Traffic that the firewall default action blocks is logged without this.

Every action has a *scope* that controls how much of the traffic the action applies to:
+ `packet` – The current packet only.
+ `hook` – Advance past the current hook only. The firewall engine evaluates the connection again at the next hook.
+ `tx` – The current transaction. The firewall engine continues to evaluate later transactions on the connection.
+ `flow` – The entire connection. For an accept action, the connection skips the firewall engine's remaining hooks and advances to the IPS engine.

You combine an action and a scope in a rule, for example `accept:flow`, `accept:tx`, `accept:hook`, or `drop:packet`. The scopes that are valid for a rule depend on both the action and the kind of hook the rule uses:
+ At an application-layer hook, `accept` supports `flow`, `tx`, `hook`, and—only when the hook's protocol runs over UDP, such as a DNS hook—`packet`. At a TCP-only application-layer hook, such as a TLS or HTTP/1 hook, the `packet` scope is rejected. `drop` and the reject actions support only `flow`, and also `packet` at a UDP application-layer hook.
+ At a packet hook (such as a TCP, UDP, or IP hook), `accept` supports `packet`, `flow`, `hook`, and `tx`. `drop` and the reject actions support only `packet` and `flow`.

You can chain a secondary `pass` action to an `accept` rule to bypass the IPS engine for the matched traffic, in the form `accept:flow,pass:flow`. For more information, see [Bypassing the IPS engine for accepted traffic](firewall-rule-ips-bypass.md).

For the complete set of valid action-and-scope combinations, see [Actions and scopes](firewall-rule-constraints-action-scope.md). For more about how actions and scopes behave, see the [Suricata firewall mode documentation](https://docs.suricata.io/en/suricata-8.0.3/firewall/firewall-design.html).