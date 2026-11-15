

# Example firewall rules
<a name="firewall-rule-groups-examples"></a>

The following examples show complete firewall rulesets for common access-control tasks, covering TLS, HTTP/1.1, HTTP/2, DNS, and SSH traffic. Each ruleset assumes a policy whose firewall default action is **Drop**, so that traffic is allowed only when a rule accepts it. For the actions and accept scopes these rules use, see [Firewall engine actions and scopes](firewall-rule-groups-verdicts.md). For the accept-prior-hooks form (`<`), see [Accepting prior hooks automatically](firewall-rule-groups-accept-prior-hooks.md).

**Important**  
An application-layer matcher (for example, a TLS SNI or HTTP host match) only takes effect if the connection first passes the TCP layer. Each TCP-based ruleset in this section therefore begins with a pair of *carrier rules* that accept the TCP layer in both directions, and the application-layer matcher uses the accept-prior-hooks form (`<`) to accept the intermediate hooks up to its own. If you provide the application-layer matcher without the carrier rules, the connection is dropped at the TCP layer by the default action and the matcher never runs. For more information, see [Accepting prior hooks automatically](firewall-rule-groups-accept-prior-hooks.md).

**Example Allow TLS traffic to a specific domain by SNI**  
This ruleset allows an outbound TLS connection only when its server name indication (SNI) is `www.example.com`. The two carrier rules accept the TCP layer in both directions; the third rule accepts the whole flow when the SNI matches, using the accept-prior-hooks form to accept the earlier TLS states automatically. A TLS connection to any other SNI is never accepted, so it falls through to the drop default action.  

```
accept:hook tcp:all $HOME_NET any -> $EXTERNAL_NET any (tcp.session:setup,established; app-layer-protocol:unknown|tls; sid:1;)
accept:hook tcp:all $EXTERNAL_NET any -> $HOME_NET any (tcp.session:setup,established; app-layer-protocol:unknown|tls; sid:2;)
accept:flow tls:<client_hello $HOME_NET any -> $EXTERNAL_NET any (tls.sni; content:"www.example.com"; startswith; endswith; nocase; sid:3;)
```

**Example Allow HTTP/1.1 and HTTP/2 traffic to a specific host**  
This ruleset allows an outbound HTTP connection only when its host is `example.com`, for both HTTP/1.1 and HTTP/2 (cleartext). The carrier rules advertise `unknown|http|http2|websocket` so that the connection can be identified as either HTTP version, and so that a flow that upgrades from HTTP to WebSocket keeps matching; the ruleset then includes one matcher for each version, because HTTP/1.1 and HTTP/2 reach their request-headers states at different hooks. A connection whose host is anything else falls through to the drop default action.  

```
accept:hook tcp:all $HOME_NET any -> $EXTERNAL_NET any (tcp.session:setup,established; app-layer-protocol:unknown|http|http2|websocket; sid:1;)
accept:hook tcp:all $EXTERNAL_NET any -> $HOME_NET any (tcp.session:setup,established; app-layer-protocol:unknown|http|http2|websocket; sid:2;)
accept:flow http1:<request_headers $HOME_NET any -> $EXTERNAL_NET any (http.host; content:"example.com"; startswith; endswith; sid:3;)
accept:flow http2:stream:<request_headers $HOME_NET any -> $EXTERNAL_NET any (http.host; content:"example.com"; startswith; endswith; sid:4;)
```

**Example Block DNS queries for a specific domain**  
This ruleset drops a UDP DNS query when the queried name contains `example.com` and lets other DNS queries through. Because the firewall engine is drop by default, letting the other queries through takes more than the drop rule alone: the two `udp:all` carrier rules accept the UDP layer in both directions, the `dns:request_started` accept carries the flow to the `dns:request_complete` hook where the full query name is available, the drop matcher blocks the names you deny, and the final `accept:flow` lets every other query through. The `alert` modifier records the match in your logs. DNS over UDP is a single request-response exchange rather than a long-lived connection, so a denylist—dropping the queries you don't want rather than using an allow list—is the most reliable pattern for DNS. For DNS over TCP, use a `tcp:all` carrier rule pair instead of `udp:all` and match at the same `dns` hooks.  

```
accept:hook udp:all $HOME_NET any -> $EXTERNAL_NET 53 (sid:1;)
accept:hook udp:all $EXTERNAL_NET 53 -> $HOME_NET any (sid:2;)
accept:hook dns:request_started $HOME_NET any -> $EXTERNAL_NET 53 (sid:3;)
drop:flow dns:request_complete $HOME_NET any -> $EXTERNAL_NET 53 (dns.query; content:"example.com"; nocase; msg:"blocked DNS query"; alert; sid:4;)
accept:flow dns:request_complete $HOME_NET any -> $EXTERNAL_NET 53 (sid:5;)
```

**Example Allow SSH only to a specific destination**  
This ruleset allows Secure Shell (SSH) only to the `10.0.3.0/24` subnet and only when the traffic on port 22 is actually the SSH protocol. The carrier rules use `app-layer-protocol:unknown|ssh` so that a non-SSH protocol tunneled over port 22 isn't carried. SSH exchanges identification banners in both directions—the server usually sends its banner first—so the ruleset accepts the flow on both the server banner and the client banner. Whichever side's banner the firewall engine processes first then carries the whole flow, so the other direction isn't blocked by the drop default action. SSH to any other destination falls through to the drop default action.  

```
accept:hook tcp:all $HOME_NET any -> 10.0.3.0/24 22 (tcp.session:setup,established; app-layer-protocol:unknown|ssh; sid:1;)
accept:hook tcp:all 10.0.3.0/24 22 -> $HOME_NET any (tcp.session:setup,established; app-layer-protocol:unknown|ssh; sid:2;)
accept:flow ssh:<response_banner_done 10.0.3.0/24 22 -> $HOME_NET any (sid:3;)
accept:flow ssh:<request_banner_done $HOME_NET any -> 10.0.3.0/24 22 (sid:4;)
```

**Example Allow traffic only to a destination country**  
This rule accepts the flow only when the destination IP address is in Germany (`DE`), using the `geoip` keyword. Because `geoip` matches at the packet layer, the rule uses the `tcp:all` hook and doesn't need separate carrier rules. Traffic to any other country falls through to the drop default action.  

```
accept:flow tcp:all $HOME_NET any -> $EXTERNAL_NET any (msg:"Allow traffic to DE"; geoip:dst,DE; sid:1;)
```

**Example Block a specific TLS version**  
To block connections that *negotiate* a particular TLS version, use an IPS rule rather than a firewall-engine rule. A connection's negotiated version isn't known until the server replies with its `ServerHello`, so the match has to inspect the server-to-client direction. At the `tls:client_hello` hook—which is the client-to-server direction—`tls.version` is the highest version the *client offered*, not the version the connection ends up using, so a drop there wouldn't catch a connection that negotiates down to an older version. The following IPS rule drops a connection whose negotiated version is TLS 1.0. Because the IPS engine inspects traffic that the firewall engine has already accepted, the rule blocks a disallowed version even when a firewall rule allowed the connection's SNI. For more information, see [Working with IPS rule groups in AWS Network Firewall](ips-rule-groups.md).  

```
drop tls $EXTERNAL_NET any -> $HOME_NET any (flow:established,to_client; tls.version:1.0; msg:"TLS 1.0 not allowed"; sid:1; rev:1;)
```

**Example Allow a domain and all of its subdomains**  
To allow a whole domain tree—for example, a SaaS provider that serves content from many subdomains—match the SNI with the `dotprefix` and `endswith` keywords. `dotprefix` anchors the match on a domain boundary, so `.example.com` matches `example.com` and any subdomain such as `api.example.com`, but not a lookalike such as `notexample.com`. This is the most common building block of a corporate egress allow list.  

```
accept:hook tcp:all $HOME_NET any -> $EXTERNAL_NET any (tcp.session:setup,established; app-layer-protocol:unknown|tls; sid:1;)
accept:hook tcp:all $EXTERNAL_NET any -> $HOME_NET any (tcp.session:setup,established; app-layer-protocol:unknown|tls; sid:2;)
accept:flow tls:<client_hello $HOME_NET any -> $EXTERNAL_NET any (tls.sni; dotprefix; content:".example.com"; endswith; nocase; sid:3;)
```

**Example Allow egress only to approved IP ranges**  
To restrict outbound traffic to a set of approved destination CIDR ranges accept the flow to those ranges at the packet layer. Because this match is at the packet layer, it doesn't need carrier rules. Traffic to any other destination falls through to the drop default action.  

```
accept:flow tcp:all $HOME_NET any -> [10.0.0.0/25,10.0.0.128/25] any (msg:"Allow approved egress ranges"; sid:1;)
```

**Example Enforce that a port carries only its expected protocol**  
A common hardening control is to ensure that a well-known port carries only its intended protocol—for example, that nothing tunnels a non-TLS protocol over port 443, or a non-SSH protocol over port 22. These rules drop a flow on the port when the detected application protocol isn't the expected one. Add them ahead of your allow rules.  

```
drop:flow tcp:all $HOME_NET any -> $EXTERNAL_NET 443 (app-layer-protocol:!tls; msg:"non-TLS traffic on port 443"; sid:1;)
drop:flow tcp:all $HOME_NET any -> $EXTERNAL_NET 22 (app-layer-protocol:!ssh; msg:"non-SSH traffic on port 22"; sid:2;)
```

**Example Restrict DNS to an approved resolver**  
To prevent clients from reaching unauthorized DNS servers (a common data-exfiltration path), allow UDP DNS only to your approved resolver and let the drop-by-default policy block the rest. In this example, `10.0.0.2` is the approved resolver: the first rule accepts DNS to it, and the second rule drops—and alerts on—DNS to any other server. Under a drop-by-default policy the second rule isn't strictly required, because the default action already blocks the other queries, but writing it explicitly records the blocked attempts in your logs.  

```
accept:flow udp:all $HOME_NET any -> 10.0.0.2/32 53 (msg:"DNS allowed only to approved resolver"; sid:1;)
drop:flow udp:all $HOME_NET any -> !10.0.0.2/32 53 (msg:"DNS to unapproved resolver"; alert; sid:2;)
```

**Note**  
These examples are illustrative starting points. The available hooks and the keywords that each hook supports depend on the Suricata version that Network Firewall runs. For the authoritative hook list and keyword reference, see the [Firewall design](https://docs.suricata.io/en/suricata-8.0.3/firewall/firewall-design.html) documentation. For the rules that govern which actions, scopes, hooks, and keywords you can combine, see [Valid combinations and constraints for firewall rules](firewall-rule-constraints.md).