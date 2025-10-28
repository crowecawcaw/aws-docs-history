**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Configuring health-based detection

for your protections with Shield Advanced and Route 53

This page provides instructions for configuring Shield Advanced to use health-based detection.
This can help improve responsiveness and accuracy in
attack detection and mitigation.

Well-configured health checks are essential for accurate
detection of events. You can configure health-based detection for any
resource type except for Route 53 hosted zones.

To use health-based detection, define a health check for your resource in Route 53, and then
associate the health check with your Shield Advanced protection. It's important that the
health check that you configure accurately reflect the health of the resource. For
information and examples for configuring health checks to use with Shield Advanced, see
[Health-based detection using
health checks with Shield Advanced and Route 53](ddos-advanced-health-checks.md "ddos-advanced-health-checks.md").

Health checks are required for Shield Response Team (SRT) proactive engagement support.
For information about proactive engagement, see [Setting up proactive engagement for the SRT to contact you directly](ddos-srt-proactive-engagement.md "ddos-srt-proactive-engagement.md").

###### Note

Health checks must be reporting healthy when you associate them with your Shield Advanced
protections.

###### To configure health-based detection

1. Under **Associated Health Check**, choose the ID of the health check that you want to
   associate with the protection.

###### Note

If you do not see the health check you need, go to the Route 53 console and
verify the health check and its ID. For information, see [Creating and Updating Health Checks](../../../Route53/latest/DeveloperGuide/health-checks-creating.md "../../../Route53/latest/DeveloperGuide/health-checks-creating.md"). 2. Choose **Next**. The console wizard advances to the alarms and notifications page.
