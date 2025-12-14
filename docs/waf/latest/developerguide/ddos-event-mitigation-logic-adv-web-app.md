**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS Shield Advanced mitigation

logic for web applications

AWS Shield Advanced uses AWS WAF to mitigate web application layer attacks. AWS WAF is included with
Shield Advanced at no additional cost.

###### Standard application layer protection

When you protect an Amazon CloudFront distribution or Application Load Balancer with Shield Advanced, you can use
Shield Advanced to associate an AWS WAF web ACL with your protected resource, if you don't
already have one associated. If you haven't already configured a web ACL, you can
use the Shield Advanced console wizard to create one and add a rate-based rule to it. A
rate-based rule limits the number of requests per five minute time window for each
IP address, providing basic protections against web application layer request
floods. You can configure the rate, starting as low as 10. For
more information, see [Protecting the application layer with AWS WAF web ACLs and Shield Advanced](ddos-app-layer-web-ACL-and-rbr.md "ddos-app-layer-web-ACL-and-rbr.md").

You can also use the AWS WAF service to manage the web ACL. Through AWS WAF, you can expand the web ACL configuration to do things such as inspect specific web request components for string matches or patterns, add custom request and response handling, and match against the geolocation of the request origin. For more information about AWS WAF rules, see [AWS WAF rules](waf-rules.md "waf-rules.md").

###### Automatic application layer mitigation

For enhanced protection, enable Shield Advanced automatic application layer mitigation.
With this option, Shield Advanced maintains an AWS WAF rate limiting rule for
requests from known DDoS sources and it provides custom mitigations for
detected DDoS attacks.

When Shield Advanced detects an attack on a protected resource, it
attempts to identify an attack signature that isolates the attack traffic from the
normal traffic to your application. Shield Advanced evaluates the identified attack
signature against the historical traffic patterns for the resource that's under
attack, as well as for any other resource that's associated with the same web ACL.

If Shield Advanced determines that the attack signature isolates only the traffic that's
involved in the DDoS attack, it implements the signature in AWS WAF rules inside the
associated web ACL. You can instruct Shield Advanced to place mitigations that only count the
traffic that they match against, or that block it, and you can change the setting at any
time. When Shield Advanced determines that its mitigating rules are no longer needed, it
removes them from the web ACL. For more information about application layer event mitigation, see [Automating application layer DDoS mitigation with Shield Advanced](ddos-automatic-app-layer-response.md "ddos-automatic-app-layer-response.md") .

For more information about Shield Advanced application layer mitigations, see [Protecting the application layer (layer 7) with AWS Shield Advanced and AWS WAF](ddos-app-layer-protections.md "ddos-app-layer-protections.md").
