**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Health-based detection using

health checks with Shield Advanced and Route 53

You can configure Shield Advanced to use health-based detection for improved responsiveness and
accuracy in attack detection and mitigation. You can use this option with any resource type
except for Route 53 hosted zones.

To configure health-based detection, you define a health check for your resource in Route 53,
verify that it's reporting healthy, and then associate it with your Shield Advanced protection. For
information about Route 53 health checks, see [How Amazon Route 53 checks the
health of your resources](../../../Route53/latest/DeveloperGuide/welcome-health-checks.md "../../../Route53/latest/DeveloperGuide/welcome-health-checks.md") and [Creating, updating, and deleting
health checks](../../../Route53/latest/DeveloperGuide/health-checks-creating-deleting.md "../../../Route53/latest/DeveloperGuide/health-checks-creating-deleting.md") in the Amazon Route 53 Developer Guide.

###### Note

Health checks are required for Shield Response Team (SRT) proactive engagement support. For information
about proactive engagement, see [Setting up proactive engagement for the SRT to contact you directly](ddos-srt-proactive-engagement.md "ddos-srt-proactive-engagement.md").

Health checks measure the health of your resources based on the requirements that you define.
The health check status provides vital input to the Shield Advanced detection mechanisms, giving
them greater sensitivity to the current state of your specific applications.

You can enable health-based detection for any resource type except for Route 53 hosted
zones.

- **Network and transport layer (layer 3/layer 4) resources**
  – Health-based detection improves the accuracy of network-layer and
  transport-layer event detection and mitigation for Network Load Balancers, Elastic IP addresses, and
  Global Accelerator standard accelerators. When you protect these resource types with Shield Advanced, Shield Advanced
  can provide mitigations for smaller attacks and faster mitigation for attacks, even
  when traffic is within the application’s capacity.

When you add health-based detection, during periods when the associated health
check is unhealthy, Shield Advanced can place mitigations even more quickly and at even
lower thresholds.

- **Application layer (layer 7) resources** –
  Health-based detection improves the accuracy of web request flood detection for CloudFront
  distributions and Application Load Balancers. When you protect these resource types with Shield Advanced, you
  receive web request flood detection alerts when there's a statistically significant
  deviation in traffic volume that's combined with significant changes in traffic
  patterns, based on request characteristics.

With health-based detection, when the associated Route 53 health check is unhealthy, Shield Advanced
requires smaller deviations to alert and it reports events more quickly. Conversely,
when the associated Route 53 health check is healthy, Shield Advanced requires larger
deviations to alert.
You'll benefit the most from using a health check with Shield Advanced if the health check only
reports healthy when your application is running within acceptable parameters and only
reports unhealthy when it's not. Use the guidance in this section to manage your health
check associations in Shield Advanced.

###### Note

Shield Advanced doesn't automatically manage your health checks.

The following are required to use a health check with Shield Advanced:

- The health check must report healthy when you associate it with your Shield Advanced
  protection.
- The health check must be relevant to the health of your protected resource.
  You are responsible for defining and maintaining health checks that accurately
  report the health of your application, based on your application's specific
  requirements.
- The health check must remain available for use by the Shield Advanced protection.
  Don't delete a health check in Route 53 that you're using for a Shield Advanced
  protection.

###### Contents

- [Best practices for using health checks with
  Shield Advanced](health-checks-best-practices.md "health-checks-best-practices.md")
- [CloudWatch metrics commonly used for health checks with Shield Advanced](health-checks-metrics.md "health-checks-metrics.md")
  - [Metrics used to monitor application health](health-checks-metrics.md#health-checks-metrics-common "health-checks-metrics.md#health-checks-metrics-common")
  - [Amazon CloudWatch metrics for each resource type](health-checks-metrics.md#health-checks-protected-resource-metrics "health-checks-metrics.md#health-checks-protected-resource-metrics")

- [Associating a health check with your
  resource protected by Shield Advanced](associate-health-check.md "associate-health-check.md")
- [Disassociating a health check from your
  resource protected by Shield Advanced](disassociate-health-check.md "disassociate-health-check.md")
- [Viewing health check association status in Shield Advanced](health-check-association-status.md "health-check-association-status.md")
- [Health check examples for Shield Advanced](health-checks-examples.md "health-checks-examples.md")
  - [Amazon CloudFront distributions](health-checks-examples.md#health-checks-example-cloudfront "health-checks-examples.md#health-checks-example-cloudfront")
  - [Load balancers](health-checks-examples.md#health-checks-example-load-balancer "health-checks-examples.md#health-checks-example-load-balancer")
  - [Amazon EC2 elastic IP address (EIP)](health-checks-examples.md#health-checks-example-elastic-ip "health-checks-examples.md#health-checks-example-elastic-ip")
