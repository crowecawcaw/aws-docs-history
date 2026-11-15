

# Attach a Lightsail web address to your distribution
<a name="amazon-lightsail-distribution-web-address"></a>

Attach a Lightsail web address, such as `mysite.amazonlightsail.com`, to your distribution from the distribution's management page, so that visitors can reach your content over HTTPS. You can also detach the web address from the same page.

You can also manage web addresses on the **Lightsail web addresses** page of the Lightsail console. For instructions, see the following topics:
+ [Create and attach a Lightsail web address](amazon-lightsail-create-attach-web-address.md)
+ [Detach or transfer a Lightsail web address](amazon-lightsail-detach-transfer-web-address.md)

## Prerequisites
<a name="distribution-web-address-prerequisites"></a>

Before you attach a web address to your distribution, make sure that you have the following:
+ An origin for your distribution that's set up to serve your content, such as an instance, bucket, container service, or load balancer. For more information, see [Understand distribution origins in Amazon Lightsail](amazon-lightsail-distribution-origins.md).
+ A distribution with the **Deployed** status that isn't currently using a custom domain.
+ The other prerequisites for a web address, including the IAM permissions that you need. For the full list, see [Prerequisites](amazon-lightsail-create-attach-web-address.md#attach-web-address-prerequisites) in *Create and attach a Lightsail web address*.

## Attach a web address from your distribution's management page
<a name="distribution-web-address-attach"></a>

Complete the following procedure to attach a web address to your distribution.

**Tip**  
You can also add a web address when you create a distribution. For more information, see [Add a web address when you create a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md#distribution-web-address-create-time).

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the name of your distribution.

1. Choose the **Getting started** tab or the **Domains** tab on your distribution's management page, and then choose **Lightsail web address**.  
![The Domains tab of a distribution, with the Lightsail web address option in use and mysite.amazonlightsail.com attached.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-distribution-domains-tab-web-address.png)

1. Do one of the following:
   + To attach a web address that you already created, choose **Attach web address**. For **Select web address**, choose a web address with the **Unattached** status, and then choose **Attach web address**.
   + To create a web address, choose **Create web address**. For **Web address name**, enter a name, and then choose **Create web address**. For the naming rules, see [Web address naming rules](amazon-lightsail-create-attach-web-address.md#web-address-naming-rules). When your web address has the **Unattached** status, attach it as described in the previous option.

1. Wait for your web address to be attached. An attach usually takes about a minute. The first time that you attach a web address, setting up HTTPS for it can take a few minutes longer. When your web address is attached, it appears on the **Domains** tab and in the **Web address** field at the top of your distribution's management page.
**Note**  
If you visited your web address in a browser before it was attached, it can take up to 15 minutes after it's attached before it works for you.

1. (Optional) If the origin of your distribution is a WordPress instance, configure WordPress to use your web address. For instructions, see [Configure WordPress with a Lightsail content delivery network](amazon-lightsail-configure-wordpress-for-distribution.md).

   If your instance uses WordPress packaged by Bitnami, see the [Bitnami version](amazon-lightsail-configure-wordpress-for-distribution-bitnami.md) of that tutorial.

## Detach a web address from your distribution
<a name="distribution-web-address-detach"></a>

When you detach a web address, it stops working within a few minutes, and your distribution will only be reachable using its default domain. Your web address will keep its name and will have the **Unattached** status.

**Note**  
Each month, you get 24 hours of free unattached web address time. After that, we charge USD $1 per month for each unattached web address. For more information, see [What do Lightsail web addresses cost?](amazon-lightsail-frequently-asked-questions-faq-billing-and-account-management.md#what-do-lightsail-web-addresses-cost).

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the name of your distribution.

1. Choose the **Domains** tab, and then choose **Lightsail web address**.

1. Choose **Detach web address**, and then choose **Detach** to confirm.

**Note**  
You can't delete a distribution while a web address is attached to it. Detach the web address first.