**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Automating application layer DDoS mitigation with Shield Advanced

This page introduces the topic of automatic application layer DDoS mitigation and lists associated caveats.

You can configure Shield Advanced to respond automatically to mitigate application layer (layer 7)
attacks against your protected application layer resources, by counting or blocking web
requests that are part of the attack. This option is an addition to the application
layer protection that you add through Shield Advanced with an AWS WAF web ACL and your own
rate-based rule.

When automatic mitigation is enabled for a resource, Shield Advanced maintains a rule group in the
resource's associated web ACL where it manages mitigation rules on behalf of the
resource. The rule group contains a rate-based rule that tracks the volume of requests
from IP addresses that are known to be sources of DDoS attacks.

Additionally, Shield Advanced compares current traffic patterns against historic traffic baselines
to detect deviations that might indicate a DDoS attack. Shield Advanced responds to detected
DDoS attacks by creating, evaluating, and deploying additional, custom AWS WAF rules
in the rule group.

## Caveats for using automatic application layer DDoS mitigation

The following list describes the caveats of Shield Advanced automatic application layer DDoS mitigation, and describes steps that you might want to take in response.

- Automatic application layer DDoS mitigation works only with protection packs (web ACLs) that were created using the latest version of AWS WAF (v2).
- Shield Advanced requires time to establish a baseline of your
  application's normal, historic traffic, which it leverages to detect and
  isolate attack traffic from normal traffic, to mitigate attack traffic.
  The time to establish a baseline is between 24 hours and 30 days from
  the time you associate a web ACL with the protected application resource.
  For additional information about traffic baselines, see [List of factors that affect application layer event detection and
  mititgation with Shield Advanced](ddos-app-layer-detection-mitigation.md "ddos-app-layer-detection-mitigation.md").
- Enabling automatic application layer DDoS mitigation adds a rule group to your protection pack (web ACL) that uses 150 web ACL capacity units
  (WCUs). These WCUs count against the WCU usage in your protection pack (web ACL). For more information, see [Protecting the application layer with the Shield Advanced
  rule group](ddos-automatic-app-layer-response-rg.md "ddos-automatic-app-layer-response-rg.md"), and [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md").
- The Shield Advanced rule group generates AWS WAF metrics, but they are not available to view. This is the same as for
  any other rule groups that you use in your protection pack (web ACL) but do not own, such as AWS Managed Rules rule groups.
  For more information about AWS WAF metrics, see [AWS WAF metrics and dimensions](waf-metrics.md "waf-metrics.md"). For information
  about this Shield Advanced protection option, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") .
- For web ACLs that protect multiple resources, automatic mitigation only deploys
  custom mitigations that don't negatively impact any of the protected resources.
- The time between the start of a DDoS attack and when Shield Advanced
  places custom automatic mitigation rules varies with each event. Some DDoS
  attacks might end before the custom rules are deployed. Other attacks
  might happen when a mitigation is already in place, and so might be mitigated
  by those rules from the start of the event. Additionally, rate-based rules in the web ACL
  and Shield Advanced rule group might mitigate attack traffic before it's detected as a possible event.
- For Application Load Balancers that receive any traffic through a content delivery network (CDN), such as Amazon CloudFront, the application-layer automatic mitigation capabilities of Shield Advanced for those Application Load Balancer resources will be reduced. Shield Advanced uses client traffic attributes to identify and isolate attack traffic from normal traffic to your application, and CDNs may not preserve or forward the original client traffic attributes. If you use CloudFront, we recommend enabling automatic mitigation on the CloudFront distribution.
- Automatic application layer DDoS mitigation does not interact with protection groups. You can enable automatic mitigation for resources that are in protection groups, but Shield Advanced does not automatically apply attack mitigations based on protection group findings. Shield Advanced applies automatic attack mitigations for individual resources.

###### Contents

- [Best practices for
  using automatic application layer DDoS mitigation](ddos-automatic-app-layer-response-bp.md "ddos-automatic-app-layer-response-bp.md")
- [Enabling automatic application layer DDoS mitigation](ddos-automatic-app-layer-response-config.md "ddos-automatic-app-layer-response-config.md")
  - [What happens
    when you enable automatic mitigation](ddos-automatic-app-layer-response-config.md#ddos-automatic-app-layer-response-enable "ddos-automatic-app-layer-response-config.md#ddos-automatic-app-layer-response-enable")

- [How Shield Advanced manages automatic mitigation](ddos-automatic-app-layer-response-behavior.md "ddos-automatic-app-layer-response-behavior.md")
  - [How
    Shield Advanced responds to DDoS attacks with automatic mitigation](ddos-automatic-app-layer-response-behavior.md#ddos-automatic-app-layer-response-ddos-attack "ddos-automatic-app-layer-response-behavior.md#ddos-automatic-app-layer-response-ddos-attack")
  - [How Shield Advanced manages the rule
    action setting](ddos-automatic-app-layer-response-behavior.md#ddos-automatic-app-layer-response-rule-action "ddos-automatic-app-layer-response-behavior.md#ddos-automatic-app-layer-response-rule-action")
  - [How
    Shield Advanced manages mitigations when an attack subsides](ddos-automatic-app-layer-response-behavior.md#ddos-automatic-app-layer-response-after-attack "ddos-automatic-app-layer-response-behavior.md#ddos-automatic-app-layer-response-after-attack")
  - [What happens
    when you disable automatic mitigation](ddos-automatic-app-layer-response-behavior.md#ddos-automatic-app-layer-response-disable "ddos-automatic-app-layer-response-behavior.md#ddos-automatic-app-layer-response-disable")

- [Protecting the application layer with the Shield Advanced
  rule group](ddos-automatic-app-layer-response-rg.md "ddos-automatic-app-layer-response-rg.md")
- [Viewing the
  automatic application layer DDoS mitigation configuration for a resource](view-automatic-app-layer-response-configuration.md "view-automatic-app-layer-response-configuration.md")
- [Enabling and disabling
  automatic application layer DDoS mitigation](enable-disable-automatic-app-layer-response.md "enable-disable-automatic-app-layer-response.md")
- [Changing the action used for automatic application layer DDoS mitigation](change-action-of-automatic-app-layer-response.md "change-action-of-automatic-app-layer-response.md")
- [Using AWS CloudFormation with
  automatic application layer DDoS mitigation](manage-automatic-mitigation-in-cfn.md "manage-automatic-mitigation-in-cfn.md")
