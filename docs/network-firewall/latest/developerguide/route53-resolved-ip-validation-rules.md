

# Matching specific domains with resolved-domain rules
<a name="route53-resolved-ip-validation-rules"></a>

The policy-level check is domain-agnostic. To allow or deny *specific* domains based on how the destination IP address was resolved, add resolved-domain rules to a stateful rule group. You can do this in any of three ways:
+ **Domain list** – Add `AWS_ROUTE_53_RESOLVED_DOMAIN` to the target types of a stateful domain list, alongside or instead of `TLS_SNI` and `HTTP_HOST`. For domain list settings (targets, target types, generated rules type, and domain formats) and how the target types combine, see [Stateful domain list rule groups in AWS Network Firewall](stateful-rule-groups-domain-names.md).
+ **Suricata rule** – Use the `aws_route_53_resolved_domain` keyword in a Suricata-compatible stateful rule with a double-quoted domain value. The rule matches when the Amazon Route 53 Resolver resolved the connection's destination IP address for that domain.
+ **Standard stateful rule** – Add the `aws_route_53_resolved_domain` keyword as a rule option on a standard stateful rule. In the API, add a `RuleOption` with the keyword `aws_route_53_resolved_domain` and a single setting that contains the domain names in double quotation marks, for example `"example.com,cdn.example.com"`. In the console, choose **Standard stateful rule** for the rule group type. Then, in the rule's filtering options, choose **Domain filtering** and enter the domain names. Network Firewall writes the keyword into the rule's options for you. For the other settings of this rule type, see [Standard stateful rule groups in AWS Network Firewall](stateful-rule-groups-basic.md).

**Note**  
Resolved-domain rules take effect only when you configure resolved IP validation on the firewall policy. See [Configuring resolved IP validation on the firewall policy](route53-resolved-ip-validation-policy-setting.md).

The following examples use the `aws_route_53_resolved_domain` keyword. This rule drops traffic whose destination IP address was resolved for `example.com`:

```
drop ip $HOME_NET any -> $EXTERNAL_NET any (aws_route_53_resolved_domain:"example.com"; flow:to_server, established; sid:1;)
```

Use a leading dot for a wildcard that also matches subdomains. This rule allows the domain and its subdomains:

```
pass ip $HOME_NET any -> $EXTERNAL_NET any (aws_route_53_resolved_domain:".example.com"; flow:to_server, established; sid:2;)
```

To reject connections (send a TCP reset), use the `tcp` protocol. `reject` isn't supported on the `ip` protocol:

```
reject tcp $HOME_NET any -> $EXTERNAL_NET any (aws_route_53_resolved_domain:".ads.example.com"; flow:to_server, established; sid:3;)
```

Match multiple domains with a single comma-separated value. The rule matches if any of the domains applies:

```
drop ip $HOME_NET any -> $EXTERNAL_NET any (aws_route_53_resolved_domain:"api.example.com,cdn.example.com"; flow:to_server, established; sid:4;)
```

Combine the keyword with an application-layer match to require both conditions. This rule allows traffic only when the TLS Server Name Indication (SNI) is `example.com` *and* the destination IP address was resolved for `example.com`:

```
pass tls $HOME_NET any -> $EXTERNAL_NET any (tls.sni; content:"example.com"; nocase; startswith; endswith; aws_route_53_resolved_domain:"example.com"; flow:to_server, established; sid:5;)
```

Keep the following in mind when you write these rules:
+ Enclose the domain value in double quotation marks, and use only one `aws_route_53_resolved_domain` keyword in each rule.
+ Write wildcards with a leading dot (`.example.com`), not with an asterisk.