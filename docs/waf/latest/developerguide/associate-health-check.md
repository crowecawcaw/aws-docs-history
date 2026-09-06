

**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console. For more details, see [Working with the console](https://docs.aws.amazon.com/waf/latest/developerguide/working-with-console.html). 

# Associating a health check with your resource protected by Shield Advanced
<a name="associate-health-check"></a>

The following procedure shows how to associate an Amazon Route 53 health check with a protected resource. 

**Note**  
Before you associate a health check with a Shield Advanced protection, make sure that it's in a healthy state. For information, see [Monitoring health check status and getting notifications](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-monitor-view-status.html) in the Amazon Route 53 Developer Guide. 

**To associate a health check**

1. Sign in to the AWS Management Console and open the AWS WAF & Shield console at [https://console.aws.amazon.com/wafv2/](https://console.aws.amazon.com/wafv2/). 

1. In the AWS Shield navigation pane, choose **Protected resources**.

1. On the **Protections** tab, select the resource that you want to associate with a health check. 

1. Choose **Configure protections**.

1. Choose **Next** until you get to the page **Configure health check based DDoS detection - *optional***.

1. Under **Associated Health Check**, choose the ID of the health check that you want to associate with the protection. 
**Note**  
If you do not see the health check you need, go to the Route 53 console and verify the health check and its ID. For information, see [Creating and Updating Health Checks](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/health-checks-creating.html).

1. Walk through the rest of the pages until you finish the configuration. On the **Protections** page, your updated health check association is listed for the resource.

1. On the **Protections** page, check that your newly associated health check is reporting healthy. 

   You can't successfully begin using a health check in Shield Advanced while the health check is reporting unhealthy. Doing so causes Shield Advanced to detect false positives at very low thresholds and can also negatively impact the ability of the Shield Response Team (SRT) to provide proactive engagement for the resource. 

   If the newly associated health check is reporting unhealthy, do the following: 

   1. Disassociate the health check from your protection in Shield Advanced.

   1. Revisit your health check specifications in Amazon Route 53 and verify your overall application performance and availability. 

   1. When your application is performing within your parameters for good health and your health check is reporting healthy, try again to associate the health check in Shield Advanced.

The health check association procedure is complete when you've established your new health check association and it reports healthy in Shield Advanced.