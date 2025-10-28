**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Associating a health check with your

resource protected by Shield Advanced

The following procedure shows how to associate an Amazon Route 53 health check with a
protected resource.

###### Note

Before you associate a health check with a Shield Advanced protection, make sure that
it's in a healthy state. For information, see [Monitoring health check status and getting notifications](../../../Route53/latest/DeveloperGuide/health-checks-monitor-view-status.md "../../../Route53/latest/DeveloperGuide/health-checks-monitor-view-status.md") in the
Amazon Route 53 Developer Guide.

###### To associate a health check

1. Sign in to the AWS Management Console and open the AWS WAF & Shield console at
   [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/ "https://console.aws.amazon.com/wafv2/").
2. In the AWS Shield navigation pane, choose **Protected
   resources**.
3. On the **Protections** tab, select the resource that you
   want to associate with a health check.
4. Choose **Configure protections**.
5. Choose **Next** until you get to the page
   **Configure health check based DDoS detection - _optional_**.
6. Under **Associated Health Check**, choose the ID of the health check that you want to
   associate with the protection.

###### Note

If you do not see the health check you need, go to the Route 53 console and
verify the health check and its ID. For information, see [Creating and Updating Health Checks](../../../Route53/latest/DeveloperGuide/health-checks-creating.md "../../../Route53/latest/DeveloperGuide/health-checks-creating.md"). 7. Walk through the rest of the pages until you finish the configuration. On
the **Protections** page, your updated health check
association is listed for the resource. 8. On the **Protections** page, check that your newly
associated health check is reporting healthy.

You can't successfully begin using a health check in Shield Advanced while the
health check is reporting unhealthy. Doing so causes Shield Advanced to detect
false positives at very low thresholds and can also negatively impact the
ability of the Shield Response Team (SRT) to provide proactive engagement for the
resource.

If the newly associated health check is reporting unhealthy, do the
following:

    1. Disassociate the health check from your protection in
     Shield Advanced.
    2. Revisit your health check specifications in Amazon Route 53 and verify
     your overall application performance and availability.
    3. When your application is performing within your parameters for
     good health and your health check is reporting healthy, try again to
     associate the health check in Shield Advanced.

The health check association procedure is complete when you've established your
new health check association and it reports healthy in Shield Advanced.
