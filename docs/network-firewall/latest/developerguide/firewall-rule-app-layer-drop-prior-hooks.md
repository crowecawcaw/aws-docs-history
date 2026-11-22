

# Dropping at an application-layer hook under a drop-by-default policy

When your firewall default action is drop, Network Firewall applies that default at every hook a flow passes through. An application-layer `drop` or `reject` rule—for example, one at `tls:client_hello` or `http1:request_headers`—therefore matches only if the flow is explicitly accepted at the TCP layer and at every earlier application-layer hook of the same protocol. Otherwise, the default action drops the flow before the rule's matcher runs.

Pair the matcher with the two `accept:hook tcp:all` carrier rules and with an `accept:hook` rule for each preceding hook. For TLS, accept `tls:client_started`. For HTTP/1, accept `http1:request_started` and `http1:request_line`. The accept-prior-hooks `<` form, which accepts these earlier hooks automatically, is valid only with an `accept` action, so you can't use it with `drop` or `reject`—write these accepts explicitly. For more information about accepting prior hooks, see [Accepting prior hooks automatically](firewall-rule-groups-accept-prior-hooks.md).

**Important**  
Without the earlier accepts, the default action drops the flow before the matcher runs. Under a drop-by-default policy the traffic is still blocked, but by the default action rather than by your rule—and the same rule under an allow-by-default policy would let the traffic through. Always verify that an application-layer drop or reject rule drops the matching flow on its own.