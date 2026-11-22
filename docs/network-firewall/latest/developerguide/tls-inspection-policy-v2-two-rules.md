

# Authoring a TLS rule and an HTTP rule for each allowed domain

To allow TLS-inspected traffic to a domain through the firewall engine, you must author **two rules** for that domain:
+ A **TLS rule** that matches the server name indication (SNI) in the TLS handshake. This rule uses the `accept:flow` or `accept:tx` action at the TLS `client_hello` hook to allow the connection past the TLS handshake stage—it doesn't by itself allow the requests inside the connection. For more information, see [How rules are evaluated for TLS-inspected traffic](tls-inspection-policy-v2-tls-gate.md).
+ An **HTTP rule** that matches the `Host` header in the decrypted HTTP request. This rule grants the actual accept for the connection.

Under a **Drop** or **Reject** firewall default action, both rules are required. A TLS rule by itself allows the connection past the TLS handshake stage, but the decrypted request then has no matching rule and falls through to the default action, which drops it. An HTTP rule by itself is never reached, because the connection can't get past the TLS handshake stage without the TLS rule. Under an **Accept** or **Alert** default action, traffic you don't write rules for is allowed, so you author rules only for the traffic you want to block.

**Why a TLS rule alone isn't enough**  
With session holding, the firewall engine evaluates the SNI before any decrypted traffic exists. The SNI is presented by the client and can be spoofed, so allowing the entire connection on the SNI alone would admit all of the connection's later HTTP traffic based on an attacker-controllable value. Requiring an HTTP rule as well means the accept decision is made against the decrypted HTTP request, not just the SNI.

**Note**  
In a Next Generation policy, an IPS engine `pass` rule that matches the TLS SNI doesn't stop inspection of the decrypted HTTP traffic. IPS engine HTTP rules still evaluate the decrypted request, so a `drop` rule on the HTTP `Host` header can block a request whose host differs from its SNI.

The following firewall ruleset allows HTTPS traffic to `example.com` end to end under a **Drop** default action, and nothing else. It has one allow rule for each stage. After the TLS handshake, a client can negotiate either HTTP/1.1 or HTTP/2 through ALPN, so the ruleset allows both:

```
accept:hook tcp:all $HOME_NET any -> $EXTERNAL_NET any (tcp.session:setup,established; app-layer-protocol:unknown|http|tls|http2|websocket; sid:1;)
accept:hook tcp:all $EXTERNAL_NET any -> $HOME_NET any (tcp.session:setup,established; app-layer-protocol:unknown|http|tls|http2|websocket; sid:2;)
accept:flow tls:<client_hello $HOME_NET any -> $EXTERNAL_NET any (tls.sni; content:"example.com"; startswith; endswith; nocase; sid:3;)
accept:tx http1:<request_headers $HOME_NET any -> $EXTERNAL_NET any (http.host; content:"example.com"; startswith; endswith; sid:4;)
accept:tx http2:global:request_started $HOME_NET any -> $EXTERNAL_NET any (sid:5;)
accept:tx http2:global:response_started $EXTERNAL_NET any -> $HOME_NET any (sid:6;)
accept:tx http2:stream:<request_headers $HOME_NET any -> $EXTERNAL_NET any (http.host; content:"example.com"; startswith; endswith; sid:7;)
```

Rules `1` and `2` allow the connection (stage 1), rule `3` allows the website name (stage 2), and rules `4` through `7` allow the decrypted requests (stage 3). HTTP/2 carries two kinds of traffic: the requests themselves, each with its own host, and connection housekeeping messages (settings, keep-alives, and flow control) that belong to no request and carry no host. Rules `5` and `6` allow the housekeeping messages in each direction—without them, an HTTP/2 connection is dropped before its first request is evaluated, even when the request would be allowed. Rule `7` allows the HTTP/2 requests to the host. Note the reversed direction on rule `6`: responses travel from the server back to the client.

To allow all inspected HTTPS traffic while still inspecting it, keep one rule per stage but remove the `content` match from the stage 2 and stage 3 rules. You still need a rule at each stage—a single `tcp:all` rule isn't enough.

Keep the following in mind when you author rules for TLS-inspected traffic:
+ **Each request is checked on its own with `accept:tx`.** An `accept:tx` rule allows one request (transaction) at a time. If a client reuses the same connection for a request to a host that isn't allowed, that request is checked on its own and blocked. To allow the whole connection after its first allowed request, use `accept:flow` instead.
+ **The website name and the request host are checked independently.** A client can request one name in the handshake (`allowed.com`) and then send requests for a different host inside the connection (`blocked.com`), a technique called *domain fronting*. Both stages are evaluated, so under a **Drop** or **Reject** default action the fronted request is blocked at stage 3 even though the handshake was allowed.
+ **WebSocket connections.** A WebSocket connection starts as an HTTP/1.1 request and then switches protocols; after the switch, the traffic carries no host. If you author your own rules, add allow rules at the `websocket:request_started` and `websocket:response_started` hooks. A domain list rule group handles this for you. For more information, see [Allowing inspected traffic with a domain list](tls-inspection-policy-v2-domain-lists.md).
+ **Name matching.** Match the SNI without regard to case by using the `nocase` keyword. To match a domain and all of its subdomains, use the `dotprefix` keyword with a leading dot, as in `content:".example.com"`.
+ **The IPS engine still runs.** Allowing traffic at a stage doesn't skip your IPS rule groups—they still inspect the decrypted traffic and can block it. The exception is a firewall engine accept rule that also bypasses the IPS engine. That bypass is the secondary `pass` action, which is valid only at the `flow` or `packet` scope—so for a TLS-inspected connection it must sit on a `flow`- or `packet`-scoped accept rule, such as `accept:flow,pass:flow` on the outer flow, not on the `accept:tx` rule at the decrypted request stage. A flow-scoped bypass applies to the whole flow. For more information, see [Bypassing the IPS engine for accepted traffic](firewall-rule-ips-bypass.md).
+ **Traffic outside your TLS inspection scope isn't decrypted.** For a connection that your TLS inspection configuration doesn't cover, only stages 1 and 2 apply, and a stage 1 `accept:flow` rule allows the whole connection as usual.