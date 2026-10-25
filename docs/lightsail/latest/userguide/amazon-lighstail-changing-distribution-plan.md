

# Adjust the data transfer quota for your Lightsail distribution
<a name="amazon-lighstail-changing-distribution-plan"></a>

When you create a Amazon Lightsail distribution, you choose a distribution plan that specifies the monthly data transfer quota and cost of your distribution. If your distribution transfers more data than your plan's monthly data transfer quota, you are charged an overage. For details about how data transfer is aggregated, what counts toward your quota, and overage pricing by AWS Region, see [Understand data transfer for your distribution](amazon-lightsail-distribution-plans.md#amazon-lightsail-distribution-data-transfer).

To avoid an overage fee, change your distribution's current plan to a different plan that offers a greater amount of monthly data transfer before your distribution exceeds its monthly quota. You can change your distribution's plan only one time during each AWS billing cycle. In this guide, we show you how to change your distribution's plan.

**Note**  
Your distribution plan also determines which Web Application Firewall (WAF) rule groups you can use. Before you change your plan, review the WAF rule groups that each plan includes. For more information, see [Web Application Firewall (WAF) by distribution plan](amazon-lightsail-distribution-plans.md#distribution-plans-waf).

For more information about distributions, see [Content delivery network distributions](amazon-lightsail-content-delivery-network-distributions.md).

## Change your distribution plan
<a name="changing-distribution-plan"></a>

Complete the following procedure to change your distribution's plan.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the name of the distribution for which you want to change the plan.

1. Choose the **Details** tab on your distribution's management page.

1. In the **Data transfer** section of the page, choose **Change distribution plan**.

1. In the **Choose your new distribution plan** dialog, choose the new plan for your distribution, and then choose **Change plan**. The new plan is applied to your distribution.  
![The Choose your new distribution plan dialog, comparing the cost, data transfer, DDoS protection, and WAF support of each distribution plan.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lighstail-changing-distribution-plan.png)