

# Resolved IP validation in AWS Network Firewall
<a name="route53-resolved-ip-validation"></a>

A standard domain rule matches on the host name that a client *asserts*—the TLS Server Name Indication (SNI) or the HTTP `Host` header. Resolved IP validation adds a check on the *provenance of the destination IP address*: whether your VPC's Amazon Route 53 Resolver returned this IP address when it resolved the domain. This closes the gap where a client sets `Host: allowed.example.com` but connects to an unrelated IP address.

Because the check is based on the destination IP address rather than on an application-layer header, it also extends domain-based rules to traffic that carries no domain name at all. This includes protocols other than HTTP and HTTPS, which standard domain rules can't inspect.

Resolved IP validation works at two levels. You can enable the policy level on its own, or add rule-level matching for specific domains on top of it:
+ **Policy level** – Resolved IP validation, a firewall policy setting. It verifies that your VPC's Amazon Route 53 Resolver resolved the connection's destination IP address for *a* domain (any domain). It then applies an enforcement action to connections that fail the check. You can use this level on its own. See [Configuring resolved IP validation on the firewall policy](route53-resolved-ip-validation-policy-setting.md).
+ **Rule level** – Matching on *specific* domains. This level *requires* the policy-level setting. You can match specific domains either with the `AWS_ROUTE_53_RESOLVED_DOMAIN` domain list target type or with the `aws_route_53_resolved_domain` Suricata rule keyword.

  This guide calls these *resolved-domain rules*. It calls the policy-level setting *resolved IP validation*. See [Matching specific domains with resolved-domain rules](route53-resolved-ip-validation-rules.md).