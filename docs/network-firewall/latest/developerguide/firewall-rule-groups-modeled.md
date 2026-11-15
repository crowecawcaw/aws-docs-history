

# Fields of a modeled firewall rule
<a name="firewall-rule-groups-modeled"></a>

A modeled firewall rule has the following fields. **Action**, **Action scope**, **Hook**, and **Protocol** are required.
+ **Action** (in the console, **Rule Action**) – The action to apply when the rule matches: `ACCEPT` allows the traffic to continue; `DROP` blocks the traffic and discontinues inspection; `REJECT` blocks the traffic and sends a TCP reset packet back to the client (for non-TCP protocols, `REJECT` behaves the same as `DROP`); `REJECT_DST` blocks the traffic and sends a TCP reset packet to the destination; or `REJECT_BOTH` blocks the traffic and sends a TCP reset packet to both the client and the destination.
+ **Action scope** – How much of the traffic the rule's action applies to—a packet, a hook, a transaction, or the whole flow. The scopes that are valid for a rule depend on the kind of hook it uses. For more information, see [Firewall engine actions and scopes](firewall-rule-groups-verdicts.md).
+ **Hook** (in the console, **Connection state**) – The connection-state hook at which Network Firewall evaluates the rule. For the list of hooks, see [Firewall engine hooks](firewall-rule-groups-hooks.md).
+ **Protocol** – The protocol that the rule matches. The protocol must match the hook's protocol family.
+ **Source and destination** – The source and destination IP addresses and ports that the rule matches.
+ **Rule options** (in the console, **Additional Options**) – Additional Suricata compatible rule options, such as content matches and metadata, provided as keyword-and-setting pairs. The rule's signature ID is supplied here as a `sid` entry. For the SID uniqueness requirement for embedded rules, see [Signature ID uniqueness](firewall-policy-v2-sid-uniqueness.md).
+ **Accept prior hooks** – Whether Network Firewall automatically accepts the earlier hooks that the connection must pass to reach this rule's hook. For more information, see [Accepting prior hooks automatically](firewall-rule-groups-accept-prior-hooks.md).
+ **Alert enabled** – Whether the rule also writes an alert log entry when it matches.
+ **Bypass IPS enabled** – Whether an accept rule also bypasses the IPS engine for the matched traffic. For more information, see [Bypassing the IPS engine for accepted traffic](firewall-rule-ips-bypass.md).