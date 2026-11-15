

# Matching a keyword at the right hook
<a name="firewall-rule-constraints-keyword-hook"></a>

This is the most common reason a firewall rule fails to validate, so it's worth understanding well. A protocol matching keyword is valid only at the one hook where the data it matches becomes available—not at any hook, and not at every hook after that point. If you place a keyword at a different hook, Network Firewall rejects the rule.

For example, the TLS server name indication (SNI) is sent in the TLS client hello, so the `tls.sni` keyword is valid only at the `tls:client_hello` hook. It isn't valid at a later TLS hook such as `tls:client_finished`, even though the client hello has already gone by. Likewise, the HTTP `Host` header is matched with `http.host` at the `http1:request_headers` hook, not at `http1:request_complete`.

**Important**  
A keyword does not carry forward to a later hook. In particular, a `...:request_complete` hook is *not* a catch-all that accepts every request-side keyword—it accepts only the keywords that specifically become available when the request completes. A common mistake is to place every match at `request_complete`; most protocol keywords are rejected there. Use the hook where the keyword's data appears.

Two points determine the right hook:
+ If your rule matches a protocol field (such as `tls.sni`, `http.host`, or a DNS query name), use the hook where that field becomes available. The [Common hooks for common protocols](firewall-rule-constraints-protocol-hooks.md) table lists the hook to use for the common protocols, and the [Firewall design](https://docs.suricata.io/en/suricata-8.0.3/firewall/firewall-design.html) documentation lists every hook and keyword.
+ If your rule matches no protocol field—for example, an allow or deny rule based only on protocol, address, and port—any valid hook for the protocol works. Using the protocol's `request_complete` hook is a reliable default in that case, because the whole request has been seen by then.

When a keyword is at the wrong hook, Network Firewall rejects the rule with a message of the form `engine progress value {{N}} doesn't match hook {{M}}`, where the two numbers are the keyword's required connection state and the state of the hook you chose. If you see this message, move the keyword to the hook named for it in the protocol reference.