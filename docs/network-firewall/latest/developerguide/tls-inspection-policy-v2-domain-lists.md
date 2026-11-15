

# Allowing inspected traffic with a domain list
<a name="tls-inspection-policy-v2-domain-lists"></a>

Instead of authoring the stage rules by hand, you can create a domain list firewall rule group that targets the following, and Network Firewall generates the full set of rules for you:
+ `TLS_SNI` – Allows the website name at the TLS handshake stage.
+ `HTTP_HOST` – Allows the matching requests at the decrypted request stage.

When you target `HTTP_HOST`, Network Firewall generates the connection rules, the website-name rules, the HTTP/1.1 and HTTP/2 request rules, the HTTP/2 housekeeping rules, and WebSocket support. This is the recommended way to build an allowlist of websites for TLS-inspected traffic. For more information about domain list rule groups, see [Generating firewall rules from domain names](firewall-rule-groups-fqdn.md).

If you view a domain list rule group as rules, you see some generated service rules that have no domain in them: the HTTP/2 housekeeping rules, which allow HTTP/2 connection messages, and the WebSocket rules, which allow a WebSocket connection only when an HTTP/1.1 request on the same connection matched one of your domains. The HTTP/2 housekeeping rules take effect ahead of rule groups with a lower priority, but they never allow a request on their own—every HTTP/2 request is still checked against your domains.

In a domain list, a leading dot (`.example.com`) matches the domain and all of its subdomains.