

# Create and configure a Lightsail content delivery network distribution
<a name="amazon-lightsail-creating-content-delivery-network-distribution"></a>

In this guide, we show you how to create an Amazon Lightsail distribution using the Lightsail console, and describe the distribution settings that you can configure. For more information about distributions, see [Content delivery network distributions](amazon-lightsail-content-delivery-network-distributions.md).

**Contents**
+ [Prerequisites](#distribution-prerequisites)
+ [Creating a distribution](#creating-a-distribution)
+ [Add a web address when you create a distribution](#distribution-web-address-create-time)
+ [Next steps](#creating-distribution-next-steps)

## Prerequisites
<a name="distribution-prerequisites"></a>

Complete the following prerequisites before you get started with creating a distribution:

1. Complete one of the following, depending on whether you want to use an instance, container service, or a bucket with your distribution.
   + **Create a Lightsail instance to host your content.** The instance serves as the origin of your distribution. The origin stores the original, definitive version of your content. For more information, see [Create an instance](how-to-create-amazon-lightsail-instance-virtual-private-server-vps.md).

     1. **For IPv4-only and dual-stack instances**, attach a Lightsail static IP to your instance. Your instance's default public IPv4 address changes if you stop and start your instance, which will break the connection between your distribution and your origin instance. A static IP does not change if you stop and start your instance. For more information, see [Create a static IP and attach it to an instance](lightsail-create-static-ip.md).

     1. **For IPv6-only instances**, a static IP is not required. The IPv6 address persists when you stop and start your instance. It's released only when you delete your instance, or disable IPv6 for your instance. You cannot get the IPv6 address back after you perform either of those actions.

     **Upload your content and files to your instance.** Your files, also known as *objects*, typically include web pages, images, and media files, but can be anything that can be served over HTTP.
   + **Create a Lightsail container service to host your website or web application.** The container service serves as the origin of your distribution. The origin stores the original, definitive version of your content. For more information, see [Creating Amazon Lightsail container services](amazon-lightsail-creating-container-services.md).
   + **Create a Lightsail bucket to store your static content.** The bucket serves as the origin of your distribution. The origin stores the original, definitive version of your content. For more information, see [Create a bucket](amazon-lightsail-creating-buckets.md).

     Upload files to your bucket using the Lightsail console, AWS Command Line Interface (AWS CLI), and AWS APIs. For more information about uploading files, see [Upload files to a bucket](amazon-lightsail-uploading-files-to-a-bucket.md).

1. (Optional) Create a Lightsail load balancer if your website requires fault tolerance. Then attach multiple copies of your instance to your load balancer. You can configure your load balancer (with one or more instances attached to it) as the origin of your distribution, instead of configuring your instance as the origin. For more information, see [Create a load balancer and attach instances to it](create-lightsail-load-balancer-and-attach-lightsail-instances.md).

## Create a distribution
<a name="creating-a-distribution"></a>

Complete the following procedure to create a distribution.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose **Create distribution**.

1. In the **Choose your origin** section of the page, choose the AWS Region in which your origin resource was created.

   Distributions are global resources. They can reference an origin in any AWS Region, and distribute its content globally.

1. <a name="distribution-origin-resource"></a>Choose your origin. An origin can be a Lightsail instance, container service, bucket, or a load balancer (with one or more instances attached to it). For more information, see [Understand distribution origins](amazon-lightsail-distribution-origins.md).
**Important**  
If you choose a Lightsail container service as the origin of your distribution, Lightsail automatically adds the default domain name of your distribution as a custom domain on your container service. This enables traffic to be routed between your distribution and your container service. However, there are some circumstances in which you might need to manually add the default domain name of your distribution to your container service. For more information, see [Add the default domain of a distribution to a container service](amazon-lightsail-adding-distribution-default-domain-to-container-service.md).

1. (Optional) To change your origin protocol policy, choose the pencil icon displayed next to the current origin protocol policy that your distribution uses. For more information, see [Understand distribution origins](amazon-lightsail-distribution-origins.md).

   This option is listed in the **Choose your origin** section of the page, under the origin resource you selected for your distribution.
**Note**  
When you select a Lightsail bucket as the origin of your distribution, the **Origin protocol policy** defaults to **HTTP only**. You cannot change the origin protocol policy when a bucket is the origin of your distribution.  
![Origin protocol policy](https://docs.aws.amazon.com/lightsail/latest/userguide/images/origin-protocol-policy.png)

1. <a name="distribution-caching-preset"></a>Choose the caching behavior (also known as a caching preset) for your distribution. For more information, see [Caching preset](amazon-lightsail-changing-default-cache-behavior.md#changing-caching-behavior-distribution-caching-preset).
**Note**  
The caching preset options are not available when you select a Lightsail bucket as the origin of your distribution. We automatically apply distribution settings that are best for static content being stored in a bucket.

1. <a name="distribution-caching-behavior"></a>(Optional) Choose **Show all settings** to view additional caching behavior settings for your distribution.
**Note**  
The caching behavior settings are not available when you select a Lightsail bucket as the origin of your distribution. We automatically apply distribution settings that are best for static content being stored in a bucket.

1. <a name="distribution-default-behavior"></a>(Optional) Choose the default behavior for your distribution. For more information, see [Default behavior](amazon-lightsail-changing-default-cache-behavior.md#changing-caching-behavior-distribution-default-behavior).
**Note**  
The default behavior options are not available when you select a Lightsail bucket as the origin of your distribution. We automatically apply distribution settings that are best for static content being stored in a bucket.

1. <a name="distribution-directory-file-overrides"></a>(Optional) Choose **Add path** to add a directory and file override to your distribution's caching behavior. For more information, see [Directory and file overrides](amazon-lightsail-changing-default-cache-behavior.md#changing-caching-behavior-distribution-directory-file-overrides).
**Note**  
The directory and file override options are not available when you select a Lightsail bucket as the origin of your distribution. We automatically apply distribution settings that are best for static content being stored in a bucket.

1. (Optional) Choose the pencil icon displayed next to the advanced setting you want to edit for your distribution. For more information, see [Advanced cache settings](amazon-lightsail-changing-default-cache-behavior.md#changing-caching-behavior-distribution-advanced-settings).
**Note**  
The advanced cache settings are not available on the **Create distribution** page when you select a Lightsail bucket as the origin of your distribution. We automatically apply distribution settings that are best for static content being stored in a bucket. However, you can modify the advanced cache settings in the distribution management page after your distribution is created.

1. Choose your distribution plan. For more information, see [Understand distribution plans](amazon-lightsail-distribution-plans.md).

1. In the **Security controls** section, keep **Enable WAF** selected to enable the Web Application Firewall (WAF) for your distribution. After you create your distribution, you can enable WAF rule groups on the **Security** tab on your distribution's management page. For more information, see [Protect your distribution with WAF](amazon-lightsail-distribution-waf.md).
**Note**  
WAF isn't supported on the USD $2.50/month distribution plan. To use WAF, choose the USD $10/month or USD $35/month plan. For more information, see [Web Application Firewall (WAF) by distribution plan](amazon-lightsail-distribution-plans.md#distribution-plans-waf).  
![The Security controls section of the Create distribution page, with the Enable WAF check box selected.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-create-distribution-waf.png)

1. Enter a name for your distribution.

   Resource names:
   + Must be unique within each AWS Region in your Lightsail account.
   + Must contain 2 to 255 characters.
   + Must start and end with an alphanumeric character or number.
   + Can include alphanumeric characters, numbers, periods, dashes, and underscores.

1. <a name="distribution-add-web-address"></a>(Optional) Under **Add-ons**, select **Add a web address** to give your distribution a Lightsail web address, such as `mysite.amazonlightsail.com`. Lightsail web addresses are names that end in `amazonlightsail.com`, and Lightsail creates the DNS records and the SSL/TLS certificate for you. For more information, see [Add a web address when you create a distribution](#distribution-web-address-create-time).

   For **Web address name**, enter a name for a new web address. You can choose **Check availability** to check whether the name is available. For the naming rules, see [Web address naming rules](amazon-lightsail-create-attach-web-address.md#web-address-naming-rules).

   If you don't add a web address, your distribution uses its default domain. You can attach a web address or a custom domain after you create your distribution.  
![The Add-ons section of the create distribution page, with Add a web address selected and mysite entered.](https://docs.aws.amazon.com/lightsail/latest/userguide/images/amazon-lightsail-create-distribution-add-web-address.png)

1. Review the cost of your distribution.

1. Choose **Create distribution**.

   Your distribution is created after a few moments.

## Add a web address when you create a distribution
<a name="distribution-web-address-create-time"></a>

You can create a Lightsail web address and attach it to your distribution when you create the distribution. In the Lightsail console, select **Add a web address** under **Add-ons**, as described in [Create a distribution](#creating-a-distribution). With the AWS CLI, use the `--subdomain-name` option of the [create-distribution](https://docs.aws.amazon.com/cli/latest/reference/lightsail/create-distribution.html) command.

**Note**  
In the Lightsail API and AWS CLI, web addresses are called *subdomains*.

When you create a distribution with a web address, Lightsail creates a new web address for your distribution. You can't add a web address that already exists, including one that you already created. To use a web address that you already created, attach it after you create your distribution. For instructions, see [Attach a Lightsail web address to your distribution](amazon-lightsail-distribution-web-address.md).

Lightsail attaches the web address after your distribution is deployed, which can take several minutes. If Lightsail can't create or attach the web address, your distribution is still created, and the **Domains** tab shows that attaching the web address failed:
+ If the web address was created but not attached, it has the **Unattached** status. Attach it to your distribution, or delete it. For instructions, see [Attach a Lightsail web address to your distribution](amazon-lightsail-distribution-web-address.md).
+ If the web address couldn't be created, it has the **Create failed** status and counts toward your quota of 30 web addresses. Delete it, and then create a web address again. For instructions, see [Delete a Lightsail web address](amazon-lightsail-delete-web-address.md).
+ If the name isn't available, or you already have 30 web addresses, no web address is created. Create a web address with a different name, and then attach it to your distribution. For instructions, see [Create and attach a Lightsail web address](amazon-lightsail-create-attach-web-address.md).

**Note**  
Each month, you get 24 hours of free unattached web address time. After that, we charge USD $1 per month for each unattached web address. For more information, see [What do Lightsail web addresses cost?](amazon-lightsail-frequently-asked-questions-faq-billing-and-account-management.md#what-do-lightsail-web-addresses-cost).

## Next steps
<a name="creating-distribution-next-steps"></a>

After your distribution is up and running, complete the following steps to configure it so that it serves your website or web application over HTTPS at a Lightsail web address or your own domain.

1. If your distribution's origin is a WordPress instance, you must edit the WordPress configuration file in your instance to make your WordPress website work with your distribution. For more information, see [Configure your WordPress instance to work with your distribution](amazon-lightsail-configure-wordpress-for-distribution.md).

1. Give your distribution a domain that's easy to remember. Choose one of the following:
   + **Use a Lightsail web address.** If you didn't add one when you created your distribution, attach a web address. Lightsail web addresses are names that end in `amazonlightsail.com`, and Lightsail creates the DNS records and the SSL/TLS certificate for you. For instructions, see [Attach a Lightsail web address to your distribution](amazon-lightsail-distribution-web-address.md).
   + **Use a custom domain.** Complete the following steps:

     1. (Optional) Create a Lightsail DNS zone to manage your domain's DNS in the Lightsail console. This allows you to easily map your domain to your Lightsail resources. For more information, see [Create a DNS zone to manage your domain's DNS records](lightsail-how-to-create-dns-entry.md). Alternately, you can continue hosting your domain's DNS where it's currently being hosted.

     1. Create a Lightsail SSL/TLS certificate for your domain to use it with your distribution. Lightsail distributions require HTTPS, so you must request an SSL/TLS certificate for your domain before you can use it with your distribution. For more information, see [Create SSL/TLS certificates for your distribution](amazon-lightsail-create-a-distribution-certificate.md).

     1. Enable custom domains for your distribution to use your domain with your distribution. Enabling custom domains requires that you specify the Lightsail SSL/TLS certificate that you created for your domain. This adds your domain to your distribution and enables HTTPS. For more information, see [Enable custom domains for your distribution](amazon-lightsail-enabling-distribution-custom-domains.md#enable-distribution-custom-domains).

     1. Add an alias record to your domain's DNS to begin routing traffic for your domain to your distribution. After you add the alias record, users who visit your domain are routed through your distribution. For more information, see [Point your domain to a distribution](amazon-lightsail-point-domain-to-distribution.md).

1. Test that your distribution is caching your content. For more information, see [Test your distribution](amazon-lightsail-testing-distribution.md).