

# Protect your Lightsail distribution with the Web Application Firewall (WAF)
<a name="amazon-lightsail-distribution-waf"></a>

The Web Application Firewall (WAF) helps protect your website or web application from common web threats and security vulnerabilities. When you enable WAF for your distribution, it inspects requests before they reach your instance, container service, load balancer, or bucket.

## Prerequisites
<a name="amazon-lightsail-distribution-waf-prerequisites"></a>

Before you get started, you need to create a Lightsail distribution. For more information, see [Create and configure a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md).

**Note**  
WAF isn't supported on the USD $2.50/month distribution plan. To use WAF, change your distribution to the USD $10/month or USD $35/month plan. For more information, see [Web Application Firewall (WAF) by distribution plan](amazon-lightsail-distribution-plans.md#distribution-plans-waf).

## Enable WAF for your distribution
<a name="enable-distribution-waf"></a>

Complete the following procedure to enable WAF for your distribution and select the WAF rule groups that you want to use.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the distribution where you want to enable WAF.

1. Choose the **Security** tab on your distribution's management page.

1. In the **Web Application Firewall (WAF)** section, choose **Enable WAF**. No WAF rule groups are enabled automatically.  
![The Security tab of a Lightsail distribution, showing the Web Application Firewall (WAF) section with the Enable WAF button.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-distribution-waf-security-tab.png)

1. In the **WAF rule groups** section, use the toggle in the **Change status** column to enable or disable individual WAF rule groups.  
![The WAF rule groups section of a Lightsail distribution's Security tab, showing the toggles in the Change status column for each managed WAF rule group.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-distribution-waf-managed-rule-groups.png)

1. (USD $35/month distribution plan only) The custom WAF rule groups are **Account takeover prevention**, **Account creation fraud prevention**, and **Bot control**. To use one of these rule groups, choose the edit icon in the **Action** column, configure the required settings, and then enable the rule group. For more information, see [Custom WAF rule groups](amazon-lightsail-distribution-security.md#distribution-waf-advanced-rule-groups).  
![The custom WAF rule groups in the WAF rule groups section, showing the Edit icon in the Action column for each custom WAF rule group.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-distribution-waf-custom-rule-groups.png)

After you enable WAF, you can monitor the requests that your WAF rule groups allow and block. For more information, see [Distribution metrics](amazon-lightsail-viewing-distribution-health-metrics.md#distribution-metrics).

## Disable WAF for your distribution
<a name="disable-distribution-waf"></a>

Complete the following procedure to disable WAF for your distribution.

**Important**  
When you disable WAF, all of your WAF configuration is permanently deleted, including the WAF rule groups that you enabled and the settings of your custom WAF rule groups. This action can't be undone.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the distribution where you want to disable WAF.

1. Choose the **Security** tab on your distribution's management page.

1. In the **Web Application Firewall (WAF)** section, choose **Disable WAF**.  
![The Security tab of a Lightsail distribution, showing the Web Application Firewall (WAF) section with the Disable WAF button.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-distribution-waf-disable.png)