

# Resolved IP validation with Network Firewall
<a name="resolver-dns-firewall-resolved-ip-validation"></a>

With AWS Network Firewall resolved IP validation, you can detect and block connections that try to bypass domain-based filtering by connecting directly to an IP address. A standard Network Firewall domain rule matches the host name that a client asserts. Examples include the TLS Server Name Indication (SNI) and the HTTP `Host` header. If a client sets a `Host` header for an allowed domain but connects to an unrelated IP address, resolved IP validation detects the mismatch.

When a connection reaches the firewall, Network Firewall checks whether the Route 53 VPC Resolver returned the connection's destination IP address for any domain. You can also add Network Firewall rules that check whether the VPC Resolver returned the destination IP address for the domain that the connection targets. Network Firewall checks resolutions only for the VPCs that are associated with the Resolver DNS Firewall rule group that you specify.

Because resolved IP validation doesn't rely on an application-layer header, you can also apply domain-based filtering to traffic that has no domain name, such as protocols other than HTTP and HTTPS.

To get started, see [Resolved IP validation in AWS Network Firewall](https://docs.aws.amazon.com/network-firewall/latest/developerguide/route53-resolved-ip-validation.html) in the *Network Firewall Developer Guide*.

## Using resolved IP validation with and without DNS Firewall rules
<a name="resolver-dns-firewall-resolved-ip-validation-with-rules"></a>

DNS Firewall rules filter outbound DNS queries, whereas resolved IP validation acts on the connections that your VPCs make after those queries resolve. You can use resolved IP validation with or without DNS Firewall rules.

**Without DNS Firewall rules**  
To use resolved IP validation without DNS Firewall domain filtering, associate a rule group that contains no rules with the VPCs whose traffic the firewall inspects. DNS Firewall doesn't filter any queries, but resolved IP validation still works.

**With DNS Firewall rules**  
When you add rules to the rule group, DNS Firewall filtering and resolved IP validation work as two independent layers of protection. If a rule blocks a DNS query, the VPC Resolver never returns an IP address for that query. As a result, Network Firewall doesn't allow connections based on it. If a rule only alerts on a query, the query still resolves and the connection can pass validation.

A rule group with no rules that you use only for resolved IP validation doesn't incur DNS Firewall charges. Standard DNS Firewall pricing applies after you add rules to the rule group.