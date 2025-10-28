**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Configuring application layer (layer 7) DDoS

protections with AWS WAF

This page provides instructions for configuring application layer protections with AWS WAF web ACLs.

To protect an application layer resource, Shield Advanced uses an AWS WAF web ACL with a
rate-based rule as a starting point. AWS WAF is a web application firewall that lets you monitor the HTTP
and HTTPS requests that are forwarded to your application layer resources, and lets
you control access to your content based on the characteristics of the requests. A
rate-based rule limits the volume of traffic based on your request aggregation criteria, providing
basic DDoS protection to your application. For more information, see [How AWS WAF works](how-aws-waf-works.md "how-aws-waf-works.md") and [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md "waf-rule-statement-type-rate-based.md").

You can also optionally enable Shield Advanced automatic application layer DDoS mitigation, to have
Shield Advanced rate limit requests from known DDoS sources and automatically provide incident-specific protections for you.

###### Important

If you manage your Shield Advanced protections through AWS Firewall Manager using a Shield Advanced policy, you
can't manage application layer protections here. You must manage them in your
Firewall Manager Shield Advanced policy.

###### Shield Advanced subscriptions and AWS WAF costs

Your Shield Advanced subscription covers the costs of using standard AWS WAF capabilities for resources that you protect with Shield Advanced. The standard AWS WAF fees that are covered by your Shield Advanced protections are the
cost per protection pack (web ACL), the cost per rule, and the base price per million requests for web request inspection, up to 1,500 WCUs and up to the default body size.

Enabling Shield Advanced automatic application layer DDoS mitigation adds a rule group to your protection pack (web ACL) that uses 150 web ACL capacity units
(WCUs). These WCUs count against the WCU usage in your protection pack (web ACL). For more information, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") , [Protecting the application layer with the Shield Advanced
rule group](ddos-automatic-app-layer-response-rg.md "ddos-automatic-app-layer-response-rg.md"), and [Web ACL capacity units (WCUs) in AWS WAF](aws-waf-capacity-units.md "aws-waf-capacity-units.md").

Your subscription to Shield Advanced does not cover the use of AWS WAF for resources that you do not protect using Shield Advanced. It also does not cover any additional non-standard AWS WAF costs for protected resources. Examples of non-standard AWS WAF costs are those for Bot Control, for the CAPTCHA rule action, for web ACLs that use more than 1,500 WCUs, and for inspecting the request body beyond the default body size. The full list is provided on the AWS WAF pricing page. Your subscription to Shield Advanced includes access to the Layer 7 Anti-DDoS Amazon Managed Rule group. As part of your subscription, you will get up to 50 billion requests to Shield Advanced protected AWS WAF resources in a calendar month. Requests beyond 50 billion will be billed as per the AWS Shield Advanced pricing page.

For full information and pricing examples, see [Shield Pricing](https://aws.amazon.com/shield/pricing/ "https://aws.amazon.com/shield/pricing/") and [AWS WAF Pricing](https://aws.amazon.com/waf/pricing/ "https://aws.amazon.com/waf/pricing/").

###### To configure layer 7

DDoS protections for a Region

Shield Advanced gives you the option to configure layer 7 DDoS mitigation for each Region where
your chosen resources are located. If you're adding protections in multiple
regions, the wizard walks you through the following procedure for each Region.

1. The **Configure layer 7 DDoS protections** page lists each resource that
   isn't yet associated with a web ACL. For each of these, either choose an
   existing web ACL or create a new web ACL. For any resource that already has
   an associated web ACL, you can change web ACLs by first disassociating the
   current one through AWS WAF. For more information, see [Associating or disassociating protection with an AWS resource](web-acl-associating-aws-resource.md "web-acl-associating-aws-resource.md").

For web ACLs that don't already have a rate-based rule, the configuration wizard prompts
you to add one. A rate-based rule limits traffic from IP addresses when they
are sending a high volume of requests. Rate-based rules help protect your
application against web request floods and can provide alerts about sudden
spikes in traffic that might indicate a potential DDoS attack. Add a
rate-based rule to a web ACL by choosing **Add rate limit
rule** and then providing a rate limit and rule action. You can
configure additional protections in the web ACL through AWS WAF.

For information about using web ACLs and rate-based rules in your Shield Advanced
protections, including additional configuration options for rate-based
rules, see [Protecting the application layer with AWS WAF web ACLs and Shield Advanced](ddos-app-layer-web-ACL-and-rbr.md "ddos-app-layer-web-ACL-and-rbr.md"). 2. For **Automatic application layer DDoS mitigation**, if you want to have Shield Advanced
automatically mitigate DDoS attacks against your application layer
resources, choose **Enable** and then select the AWS WAF rule
action that you want Shield Advanced to use in its custom rules. This setting
applies to all of the web ACLs for the resources that you are managing in
this wizard session.

With automatic application layer DDoS mitigation, Shield Advanced maintains a rate-based rule in the
resource's AWS WAF web ACL that limits the volume of requests from known
DDoS sources. Additionally, Shield Advanced compares current traffic patterns
against historic traffic baselines to detect deviations that might indicate
a DDoS attack. When Shield Advanced detects a DDoS attack, it responds by creating,
evaluating, and deploying custom AWS WAF rules to respond. You specify
whether the custom rules count or block attacks on your behalf.

###### Note

Automatic application layer DDoS mitigation works only with protection packs (web ACLs) that were created using the latest version of AWS WAF (v2).

For more information about Shield Advanced automatic application layer DDoS mitigation, including caveats and
best practices for using this feature, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") . 3. Choose **Next**. The console wizard advances to the health-based detection page.
