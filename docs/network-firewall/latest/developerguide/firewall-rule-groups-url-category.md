

# URL and domain category filtering

With URL and domain category filtering, you can filter network traffic based on predefined content categories. Firewall rules support the same two keywords as Classic Network Firewall stateful rules. For the Classic version of this feature, including the full list of supported categories and the URL-evaluation details, see [URL and domain category filtering in Suricata compatible AWS Network Firewall rule groups](rule-groups-url-filtering.md).
+ `aws_url_category` – Evaluates complete URLs and domains in HTTP/HTTPS traffic.
+ `aws_domain_category` – Evaluates only domain information from the TLS SNI or the HTTP host header.

To use URL and domain category filtering, you provide either the `aws_url_category` or `aws_domain_category` keyword followed by the category you want to filter for, for example `aws_url_category:Malicious;`. You can specify multiple categories in a single rule by separating them with commas. The `aws_url_category` keyword applies to HTTP traffic; for HTTPS traffic it requires TLS inspection to evaluate URLs. The `aws_domain_category` keyword applies to TLS and HTTP traffic and doesn't require TLS inspection to evaluate the domain.

Because these keywords match at an application-layer hook, a rule that drops matching traffic depends on the connection reaching that hook. Under a drop-by-default firewall engine, you accept the TCP layer with carrier rules and then explicitly accept every earlier application-layer hook of the protocol, so that the connection advances to the hook where the category rule evaluates. You can't use the `<` accept-prior-hooks form to accept those earlier hooks in this case, because that form is valid only with an `accept` action, not with `drop` or `reject`. For more information, see [Dropping at an application-layer hook under a drop-by-default policy](firewall-rule-app-layer-drop-prior-hooks.md).

The following example accepts the TCP layer and the earlier HTTP hooks, then drops HTTP traffic whose URL is categorized as `Cryptocurrency`. HTTP/1 passes through `request_started` and `request_line` before `request_headers`, so both must be accepted for the drop matcher at `request_headers` to run under a drop-by-default policy. This example covers HTTP/1; to also block HTTP/2, add a parallel matcher at `http2:stream:request_data` (where the URL becomes available for an HTTP/2 stream) with the earlier HTTP/2 stream hooks accepted:

```
accept:hook tcp:all $HOME_NET any -> $EXTERNAL_NET any (tcp.session:setup,established; app-layer-protocol:unknown|http|http2|websocket; sid:1;)
accept:hook tcp:all $EXTERNAL_NET any -> $HOME_NET any (tcp.session:setup,established; app-layer-protocol:unknown|http|http2|websocket; sid:2;)
accept:hook http1:request_started $HOME_NET any -> $EXTERNAL_NET any (sid:3;)
accept:hook http1:request_line $HOME_NET any -> $EXTERNAL_NET any (sid:4;)
drop:flow http1:request_headers $HOME_NET any -> $EXTERNAL_NET any (aws_url_category:Cryptocurrency; msg:"Block Cryptocurrency URL"; sid:5;)
```

The following example drops TLS traffic whose SNI domain is categorized as `Cryptocurrency`. The two `accept:hook tcp:all` rules carry the connection through the TCP layer, and `accept:hook tls:client_started` accepts the TLS state that precedes `client_hello`, so the flow survives the drop-by-default policy long enough for the drop matcher at `tls:client_hello` to evaluate:

```
accept:hook tcp:all $HOME_NET any -> $EXTERNAL_NET any (tcp.session:setup,established; app-layer-protocol:unknown|tls; sid:1;)
accept:hook tcp:all $EXTERNAL_NET any -> $HOME_NET any (tcp.session:setup,established; app-layer-protocol:unknown|tls; sid:2;)
accept:hook tls:client_started $HOME_NET any -> $EXTERNAL_NET any (sid:3;)
drop:flow tls:client_hello $HOME_NET any -> $EXTERNAL_NET any (aws_domain_category:Cryptocurrency; msg:"Block Cryptocurrency domain"; sid:4;)
```

For HTTPS traffic that you inspect with TLS inspection, the usual Next Generation policy requirements apply: you provide both a TLS rule and an HTTP rule to pass a domain. For more information, see [TLS inspection with a Next Generation policy in AWS Network Firewall](tls-inspection-policy-v2.md).