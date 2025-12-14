**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# How AWS Shield mitigates events

This page introduces how AWS Shield event mitigation works.

The mitigation logic that protects your application can vary depending on your application
architecture. When you protect a web application with Amazon CloudFront and Amazon Route 53, you benefit
from mitigations that are specific to web and DNS use cases and that protect all traffic for
the services. When your application's entry point is a resource that runs in an AWS
Region, the mitigation logic varies depending on the service, the resource type, and your
use of AWS Shield Advanced.

AWS DDoS mitigation systems are developed by Shield engineers and they're closely integrated
with AWS services. The engineers take into account aspects of your architecture such as
the capacity and health of targeted resources. Shield engineers continually monitor the
efficacy and performance of DDoS mitigation systems and are able to respond quickly when new
threats are discovered or anticipated.

You can architect your application to scale in response to elevated traffic or load, to help
ensure that it's not affected by smaller request floods. If you use Shield Advanced to protect your
resources, you receive coverage against unexpected increases in your cloud bill that might
occur as the result of a DDoS attack.

###### Infrastructure mitigations

For infrastructure layer attacks, AWS Shield DDoS mitigation systems are present at the
AWS network border and at AWS edge locations. The placement of multiple levels of
security controls throughout the AWS infrastructure provides defense-in-depth to your
cloud applications.

Shield maintains DDoS mitigation systems at all points of ingress from the internet. When
Shield detects a DDoS attack, for each point of ingress, it reroutes the traffic through the
DDoS mitigation systems in the same location. This doesn’t introduce any observable
additional latency, and provides a mitigation capacity of more than 100 TeraBits Per Second (Tbps) across all AWS
Regions and all edge locations. Shield protects your resource availability without rerouting
traffic to external or remote scrubbing centers, which could increase latency.

- At the AWS network border, for any AWS service or resource, DDoS mitigation systems
  mitigate infrastructure layer attacks coming from the internet. The systems perform
  their mitigations when signaled by Shield detection or by an engineer on the
  Shield Response Team (SRT).
- At AWS edge locations, DDoS mitigation systems continuously inspect every packet that's
  forwarded to Amazon CloudFront distributions and Amazon Route 53 hosted zones, regardless of their
  origin. When needed, the systems apply mitigations that are specifically designed
  for web and DNS traffic. An added benefit of using Amazon CloudFront and Amazon Route 53 to
  protect your web applications is that DDoS attacks are immediately mitigated, without
  requiring a signal from Shield detection.

###### Application layer mitigations

Shield Advanced provides web application layer mitigations for the Amazon CloudFront distributions and
Application Load Balancers where you've enabled Shield Advanced protections. When you enable protection, you
associate an AWS WAF web ACL with the resource, to enable web application layer
detection. Additionally, you have the option of enabling automatic application layer
mitigation, which instructs Shield Advanced to manage protections for you during a DDoS attack.

Shield only provides custom mitigations for application layer attacks on resources for which you've
enabled Shield Advanced and automatic application layer mitigation. With automatic mitigation,
Shield Advanced enforces AWS WAF rate limiting on requests from known DDoS sources,
and it automatically adds and manages custom AWS WAF protections
in response to detected DDoS attacks. For detailed information
about mitigations of this type, see [How Shield Advanced manages automatic mitigation](ddos-automatic-app-layer-response-behavior.md "ddos-automatic-app-layer-response-behavior.md").

A rate-based rule in your web ACL, whether added by you or added by the
Shield Advanced automatic application layer mitigation feature, can mitigate an attack before
it reaches a detectable level. For more information about detection, see [Shield Advanced detection logic for application layer threats (layer 7)](ddos-event-detection-application.md "ddos-event-detection-application.md").

###### Topics

- [List of AWS Shield DDoS mitigation features](ddos-event-mitigation-features.md "ddos-event-mitigation-features.md")
- [AWS Shield mitigation logic for CloudFront and Route 53](ddos-event-mitigation-logic-continuous-inspection.md "ddos-event-mitigation-logic-continuous-inspection.md")
- [AWS Shield mitigation logic for AWS
  Regions](ddos-event-mitigation-logic-regions.md "ddos-event-mitigation-logic-regions.md")
- [AWS Shield mitigation logic for
  AWS Global Accelerator standard accelerators](ddos-event-mitigation-logic-gax.md "ddos-event-mitigation-logic-gax.md")
- [AWS Shield Advanced mitigation logic
  for Elastic IPs](ddos-event-mitigation-logic-adv-eip.md "ddos-event-mitigation-logic-adv-eip.md")
- [AWS Shield Advanced mitigation
  logic for web applications](ddos-event-mitigation-logic-adv-web-app.md "ddos-event-mitigation-logic-adv-web-app.md")
