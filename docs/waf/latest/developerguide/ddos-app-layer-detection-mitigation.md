**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# List of factors that affect application layer event detection and

mititgation with Shield Advanced

This section describes the factors that affect the detection and mitigation of application
layer events by Shield Advanced.

###### Health checks

Health checks that accurately report the overall health of your application
provide Shield Advanced with information about the traffic conditions that
your application is experiencing. Shield Advanced requires less information pointing to
a potential attack when your application is reporting unhealthy and it requires
more evidence of an attack if your application is reporting healthy.

It's important to configure your health checks so that they accurately report
application health. For more information and guidance, see [Health-based detection using
health checks with Shield Advanced and Route 53](ddos-advanced-health-checks.md "ddos-advanced-health-checks.md").

###### Traffic baselines

Traffic baselines give Shield Advanced information about the characteristics of normal
traffic for your application. Shield Advanced uses these baselines to recognize when your application
isn't receiving normal traffic, so it can notify you and, as configured, start devising and testing mitigation
options to counter a potential attack. For additional information about how Shield Advanced uses traffic
baselines to detect potential events, see the overview section [Shield Advanced detection logic for application layer threats (layer 7)](ddos-event-detection-application.md "ddos-event-detection-application.md").

Shield Advanced creates its baselines from information provided by the web ACL that's associated
with the protected resource. The web ACL must be associated with the resource for at least 24 hours and up to
30 days before Shield Advanced can reliably determine the application's baselines. The time required
begins when you associate the web ACL, either through Shield Advanced or through AWS WAF.

For more information about using a web ACL with your Shield Advanced application layer protections, see [Protecting the application layer with AWS WAF web ACLs and Shield Advanced](ddos-app-layer-web-ACL-and-rbr.md "ddos-app-layer-web-ACL-and-rbr.md").

###### Rate-based rules

Rate-based rules can help mitigate attacks. They can also obscure attacks,
by mitigating them before they become a large enough problem to show up against
normal traffic baselines or in health check status reporting.

We recommend using rate-based rules in your web ACL when you protect an application
resource with Shield Advanced. Even though their mitigations can obscure a potential attack, they are a valuable
first line of defense, helping ensure that your application stays available to your
legitimate customers. The traffic that your rate-based rules detect and rate limit is visible in your AWS WAF
metrics.

In addition to your own rate-based rules, if you enable automatic application layer DDoS mitigation, Shield Advanced adds a
rule group to your web ACL that it uses to mitigate attacks. In this rule group, Shield Advanced
always has a rate-based rule in place that limits the volume of
requests from IP addresses that are known to be sources of DDoS attacks.
Metrics for the traffic that the Shield Advanced rules mitigate aren't available
for you to view.

For more information about rate-based rules, see [Using rate-based rule statements in AWS WAF](waf-rule-statement-type-rate-based.md "waf-rule-statement-type-rate-based.md"). For information about the rate-based rule
that Shield Advanced uses for automatic application layer DDoS mitigation, see [Protecting the application layer with the Shield Advanced
rule group](ddos-automatic-app-layer-response-rg.md "ddos-automatic-app-layer-response-rg.md").

For more information about Shield Advanced and AWS WAF metrics, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
