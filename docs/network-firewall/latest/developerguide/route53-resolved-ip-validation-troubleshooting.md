

# Monitoring and troubleshooting resolved IP validation
<a name="route53-resolved-ip-validation-troubleshooting"></a>

Use firewall logs and CloudWatch metrics to see how resolved IP validation is affecting your traffic.

**Flow and alert logs** – When logging is enabled, resolved IP validation adds fields such as `route53_resolved_ip` (and, for domain rules, `route53_domain`) to the flow and alert log events. For the full list of fields, see [Resolved IP validation log fields](firewall-logging-resolved-domain.md).

**Metrics** – The `DnsResolvedFlows`, `DnsUnresolvedFlows`, `DnsResolutionErrorFlows`, and `DnsAzUnavailableFlows` metrics report per-flow validation outcomes. For more information, see [AWS Network Firewall metrics in Amazon CloudWatch](monitoring-cloudwatch.md).

**Note**  
The logs don't distinguish *why* a flow wasn't validated. Unresolved destinations, unsupported Availability Zones, and transient resolution errors all appear as `route53_resolved_ip: false` (resolution errors omit the field). Use the metrics to tell them apart. For example, `DnsAzUnavailableFlows` counts flows in an Availability Zone that doesn't support the feature. For a transit gateway-attached firewall, this is your client's Availability Zone. For other firewalls, it's the zone where the firewall endpoint is deployed.

**Unsupported Availability Zones** – Resolved IP validation isn't available in every Availability Zone. When your traffic arrives from an unsupported zone (the firewall endpoint's zone, or the client's zone for a transit gateway-attached firewall), Network Firewall can't validate it. Network Firewall treats these connections as failing validation, applies your `Action` setting to them, and counts them in the `DnsAzUnavailableFlows` metric. Check this metric when you first enable the feature. If it is nonzero, keep `Action` set to `ALERT` for the affected firewall, or exclude the affected clients by using `SourceIPRanges`, until the traffic is served from a supported zone.

Resolved-domain rules behave differently from the policy-level check in an unsupported Availability Zone. A rule that uses the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type or the `aws_route_53_resolved_domain` keyword can't be evaluated there. Instead, Network Firewall drops the traffic that the rule inspects, regardless of the policy's `Action` setting or the rule's own action. For a rule whose only match condition is the resolved domain, that is all of the traffic that the rule applies to. Before you add resolved-domain rules, confirm that `DnsAzUnavailableFlows` is zero for the firewall.

**Investigating unresolved flows** – If you see connections with `route53_resolved_ip: false`, or a rising `DnsUnresolvedFlows`, the destination IP address wasn't one that the Amazon Route 53 Resolver returned for the domain. The following are common causes:
+ The client is legitimately connecting to a destination that it didn't resolve through the VPC's Route 53 Resolver (for example, a hardcoded IP address). If this is expected, add the destination to `BypassDestinationValidationIPRanges`, or remove the client from the `SourceIPRanges` scope.
+ The client is still using a cached DNS answer from before the feature was enabled. This typically clears as caches refresh. For more information, see the alert-mode recommendation in [Recommendations for configuring resolved IP validation](route53-resolved-ip-validation-recommendations.md).
+ The client keeps using an IP address long after the DNS record's time to live (TTL) has expired. This can happen because of an application-level cache or a resolver that ignores TTLs. Resolved IP validation keeps a resolution for longer than its DNS TTL, so a slightly stale client is still validated. When the resolution expires from the resolved IP cache, your DNS expiry exception policy handles connections that are already in progress. New connections fail as unresolved. Fix the client so that it re-resolves the domain when the TTL expires, or set the expiry exception policy to `CONTINUE` to tolerate in-progress connections.
+ The traffic is crossing Availability Zones to a firewall that isn't a transit gateway-attached firewall. See the transit gateway recommendation in [Recommendations for configuring resolved IP validation](route53-resolved-ip-validation-recommendations.md).

**Configuration error states** – Network Firewall detects some resolved IP validation problems asynchronously, after a create or update request has already succeeded. The policy's `Errors` list in `DescribeFirewallPolicy` reports the following, while the policy stays `ACTIVE`:
+ `ROUTE53_RESOLVED_IP_VALIDATION_MISSING` – A stateful rule group that uses the `aws_route_53_resolved_domain` keyword is associated with the policy, but the policy doesn't have resolved IP validation configured. To reactivate the affected rules, add resolved IP validation to the policy or remove the keyword rules.
+ `DNS_FIREWALL_RULE_GROUP_UNAVAILABLE` – The Amazon Route 53 Resolver DNS Firewall rule group that resolved IP validation references is unavailable. For example, it was deleted or is no longer accessible from your account. Update the rule group ID or remove the resolved IP validation configuration.

Network Firewall clears each error automatically after you resolve the underlying problem.

When you change the DNS Firewall rule group ID, the policy status shows `UPDATING` (`A DNS Firewall rule group change is in progress`) while Network Firewall swaps the rule group association. Network Firewall rejects further changes to resolved IP validation until the policy returns to `ACTIVE`. If the new rule group is unavailable, the swap doesn't complete and the policy reports `DNS_FIREWALL_RULE_GROUP_UNAVAILABLE`.

**Note**  
A policy configuration error also surfaces on the firewalls that use the policy. The affected firewall endpoints report an `ERROR` attachment status in `DescribeFirewall`, with the message "The firewall policy has configuration errors." The policy's rule configuration still syncs to the firewall. Only the affected resolved-domain rules are inactive.