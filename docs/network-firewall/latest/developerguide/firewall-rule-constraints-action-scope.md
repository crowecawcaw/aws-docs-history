

# Actions and scopes

Every firewall rule begins with an action and an explicit scope, written as `{{action}}:{{scope}}` (for example, `accept:flow` or `drop:packet`). Two rules govern which combinations are valid:
+ The primary action must be `accept`, `drop`, `reject`, `rejectdst`, or `rejectboth`. `rejectsrc` is accepted as a synonym for `reject`. A firewall rule can't use `pass` or `alert` as its primary action. (`pass` is available only as a secondary action that bypasses the IPS engine, and `alert` only as a modifier that adds logging. For the IPS bypass, see [Bypassing the IPS engine for accepted traffic](firewall-rule-ips-bypass.md).)
+ The scope is mandatory. A firewall rule that omits the scope is rejected.

Each action supports a different set of scopes, and the hook further restricts which of those scopes are valid. The following table shows the valid scopes for each action. For what each scope means, see [Firewall engine actions and scopes](firewall-rule-groups-verdicts.md).


| Action | Valid scopes | Notes | 
| --- | --- | --- | 
| accept | flow, tx, hook, packet | The only action that supports the tx and hook scopes. Use accept:flow to carry a whole connection forward on a match. | 
| drop | flow, packet | The hook and tx scopes aren't valid for drop. | 
| reject | flow, packet | Same scopes as drop. reject blocks the traffic and also sends a TCP reset to the client. | 
| rejectdst | flow, packet | Same scopes as reject. rejectdst blocks the traffic and sends a TCP reset to the destination (modeled rule value REJECT\_DST). | 
| rejectboth | flow, packet | Same scopes as reject. rejectboth blocks the traffic and sends a TCP reset to both the client and the destination (modeled rule value REJECT\_BOTH). | 

The hook adds one more restriction: the `packet` scope is valid only at a packet hook (such as `tcp:all`) or at an application-layer hook for a protocol that runs over UDP (such as a DNS hook). The `packet` scope isn't valid at an application-layer hook for a protocol that runs only over TCP, such as a TLS or HTTP/2 hook—at those hooks, use `flow`, `tx`, or `hook` instead. The following table summarizes the valid action-and-scope combinations for each kind of hook.


| Action and scope | Packet hook (for example, `tcp:all`) | TCP application hook (for example, `tls:client_hello`) | UDP application hook (for example, `dns:request_complete`) | 
| --- | --- | --- | --- | 
| accept:flow, accept:hook, accept:tx | Valid | Valid | Valid | 
| accept:packet | Valid | Not valid | Valid | 
| drop:flow, reject:flow | Valid | Valid | Valid | 
| drop:packet, reject:packet | Valid | Not valid | Valid | 
| Any action with no scope | Not valid | Not valid | Not valid | 
| pass or alert as the primary action | Not valid | Not valid | Not valid | 

**Note**  
The accept-prior-hooks form of a hook, written with a leading `<` (for example, `tls:<client_hello`), is valid only with `accept:flow`, `accept:tx`, or `accept:hook`. You can't use it with a `drop` or `reject` action. For more information, see [Accepting prior hooks automatically](firewall-rule-groups-accept-prior-hooks.md).

For more about how the underlying actions and action scopes behave, see [Firewall design](https://docs.suricata.io/en/suricata-8.0.3/firewall/firewall-design.html) in the [Suricata User Guide](https://docs.suricata.io/en/suricata-8.0.3/index.html).