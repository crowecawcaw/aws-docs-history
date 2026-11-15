

# Generating firewall rules from domain names
<a name="firewall-rule-groups-fqdn"></a>

A firewall rule group can generate rules from a list of domain names, so that you can allow traffic to a set of domains without authoring the matching rules yourself. Domain name rule generation in the firewall engine supports allow lists only: it generates accept rules for the domains you list. To block a domain, you don't add it to an allow list, which is consistent with the firewall engine's drop-by-default behavior.

You can match a domain by one or more of the following target types, individually or combined:
+ **TLS SNI** – Match the server name indication (SNI) in the TLS handshake.
+ **HTTP host** – Match the `Host` header in an HTTP request.
+ **Route 53 resolved domain** – Match traffic to the IP addresses that Amazon Route 53 resolved for the domain.

By default, the generated rules match traffic from `HOME_NET`—the CIDR range of the VPC where the firewall is deployed. To match a different source range, in the console choose **Custom** under **Source IPs** and enter the ranges, or through the API define a `HOME_NET` IP set in the rule group's `RuleVariables`.

You can use a wildcard to match a domain and all of its subdomains by starting the domain with a dot, for example `.example.com`. 
+ Explicit names. For example, `abc.example.com` matches only the domain `abc.example.com`.
+ Names that use a domain wildcard, which you indicate with an initial '`.`'. For example,`.example.com` matches `example.com` and matches all subdomains of `example.com`, such as `abc.example.com` and `www.example.com`. 

The rules that Network Firewall generates from your domain names count toward the firewall rule limit for the policy. If you generate rules for a large number of domains, keep this limit in mind. For the limit, see [AWS Network Firewall quotas](quotas.md).

**Note**  
Domain name rule generation is available for firewall rule groups. It isn't available for IPS rule groups.