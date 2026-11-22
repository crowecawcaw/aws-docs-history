

# Accepting prior hooks automatically

Because the firewall engine is drop by default, a connection reaches a rule's hook only if it was accepted at every earlier hook. Without help, allowing a single kind of traffic can require you to author several rules: one for the *target hook* (the hook where your match rule applies), plus one for each earlier hook that the connection must pass first.

The *accept prior hooks* setting removes most of this burden. When you set accept prior hooks to true on a modeled rule, or use the equivalent syntax in a raw rule string, Network Firewall automatically accepts the earlier application-layer hooks that the connection must pass to reach the target hook, up to but not including the TCP layer. You author only the rule for the target hook, and Network Firewall handles the earlier application-layer hooks for you.

**Example Allowing TLS traffic by SNI without accept prior hooks**  
Suppose you want to allow TLS traffic to `example.com` while letting the rest of the handshake proceed. The match you care about is on the SNI, which is available at the `client_hello` state, so that's the target hook. You accept the whole flow there with `accept:flow`, which carries every later state of the connection forward on a match. But because `client_hello` isn't the first state of the flow, you also need to accept the one earlier client state, `client_started`, so that the connection can reach `client_hello` in the first place:  

```
accept:hook tls:client_started $HOME_NET any -> $EXTERNAL_NET any (sid:100;)
accept:flow tls:client_hello   $HOME_NET any -> $EXTERNAL_NET any (tls.sni; content:"example.com"; startswith; endswith; nocase; sid:101;)
```
The SNI rule uses `accept:flow`, not `accept:hook`, so that a match on the SNI carries the whole flow forward—this is what makes the later client states and all of the server states unnecessary to accept individually. An `accept:hook` at `client_hello` alone wouldn't let the rest of the handshake through. If you anchored the match at a target hook with more than one earlier state, you'd need an `accept:hook` rule for each of those earlier states.

**Example Allowing the same traffic with accept prior hooks**  
A single rule has the same effect as the pair of rules in the previous example:  

```
accept:flow tls:<client_hello $HOME_NET any -> $EXTERNAL_NET any (tls.sni; content:"example.com"; startswith; endswith; nocase; sid:101;)
```
Here, `accept:flow` accepts the whole TLS flow from the moment the rule matches, so every later state is accepted without an explicit rule. This applies to a connection that isn't in scope of TLS inspection. When a connection *is* TLS-inspected, an accept at the connection or TLS handshake stage allows the connection only through that stage—Network Firewall evaluates the decrypted request as a separate stage that needs its own rule. For more information, see [How rules are evaluated for TLS-inspected traffic](tls-inspection-policy-v2-tls-gate.md). The `<` modifier in `tls:<client_hello` is the accept-prior-hooks form: it also accepts the earlier states up to and including `client_hello`, so you don't need the separate `client_started` rule. When you author the rule as a modeled rule, set accept prior hooks to true to get the same result.

**Important**  
Accept prior hooks accepts the earlier application-layer hooks only. It doesn't accept the TCP layer, so a connection still has to pass the TCP hooks before it reaches an application-layer hook such as a TLS or HTTP hook. You provide *carrier rules* that accept the TCP layer in both directions, so that the connection can advance to the hook where your rule matches. The following pair of carrier rules accepts the TCP handshake for traffic that the firewall engine inspects at the application layer:  

```
accept:hook tcp:all $HOME_NET any -> $EXTERNAL_NET any (tcp.session:setup,established; app-layer-protocol:unknown|http|tls|http2|websocket; sid:1;)
accept:hook tcp:all $EXTERNAL_NET any -> $HOME_NET any (tcp.session:setup,established; app-layer-protocol:unknown|http|tls|http2|websocket; sid:2;)
```
In the console, the **Accept prior hooks** option in the visual rule builder sets the accept-prior-hooks behavior for a rule, which handles the earlier application-layer hooks. See [Creating a rule group for a Next Generation policy](rule-groups-v2-creating.md). You still author the TCP carrier rules yourself, as shown above.

**Note**  
`client_hello` is the most common target hook for an allow-by-SNI rule, because the SNI is available there and every TLS flow passes through that state. It isn't the only valid TLS hook, though—you can anchor a rule at a later state when your match needs data that appears there. For example, a rule that inspects the negotiated cipher or the server certificate anchors at a server-side state such as `server_hello` or `server_cert`. When you choose a target hook, keep in mind which flows reach it: if you anchor an allow rule at a state that some flows never reach—for example, a TLS 1.3 session that closes before `client_finished`—those flows don't match the rule and are handled by the policy's firewall default action. For more information about the firewall default action, see [Firewall default action](firewall-policy-v2-default-action.md).

**Note**  
In a policy that uses TLS inspection, an `accept:flow` rule at the TCP layer (for example, `accept:flow tcp:all`) allows the connection only at the connection stage. Network Firewall still evaluates the TLS handshake and the decrypted request, so under a **Drop** or **Reject** default action you also need allow rules at those stages. For more information, see [How rules are evaluated for TLS-inspected traffic](tls-inspection-policy-v2-tls-gate.md).