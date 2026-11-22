

# Choose a domain for your Lightsail distribution

Every Lightsail distribution has a default domain, such as `d111111abcdef8.cloudfront.net`, that is always available. To serve your content at a name that's easier to remember, give your distribution one of the following:
+ **A Lightsail web address** – Lightsail web addresses are subdomains of `amazonlightsail.com`, such as `mysite.amazonlightsail.com`, that are automatically configured for HTTPS traffic. Lightsail creates and manages the DNS records and the SSL/TLS certificate for you. For instructions, see [Attach a Lightsail web address to your distribution](amazon-lightsail-distribution-web-address.md).
+ **A custom domain** – A domain that you own, such as `example.com` or `www.example.com`. You register the domain, manage its DNS records, create and validate an SSL/TLS certificate for it, and point your domain to your distribution. For instructions, see [Enable custom domains for your distribution](#enable-distribution-custom-domains).

**Note**  
The default domain keeps working after you attach a web address.

For more information about how they differ, see [Choose a web address or a custom domain](amazon-lightsail-web-addresses-and-domains.md#choose-web-address-or-domain).

A distribution can use a web address or a custom domain, but not both at the same time. You manage both on the **Domains** tab of your distribution's management page, which has two options: **Lightsail web address** and **Custom domain**. To change from one to the other, see [Switch between a web address and a custom domain](#switch-web-address-custom-domain).

## Use a custom domain with your distribution
<a name="distribution-custom-domain"></a>

Enable custom domains for your Amazon Lightsail distribution to use your registered domain names with your distribution. Before you enable custom domains, your distribution accepts traffic for its default domain, such as `d111111abcdef8.cloudfront.net`. When you enable custom domains, you must choose the Lightsail SSL/TLS certificate that you created for the domains that you want to use with your distribution. After you enable custom domains, your distribution accepts traffic for all of the domains that are associated with the certificate that you chose.

**Important**  
Only one certificate can be in use at a time per distribution. If you disable custom domains on your distribution, your distribution is no longer able to handle HTTPS traffic for your registered domain until you enable custom domains again.  
The domain names associated with the SSL/TLS certificate cannot be in use by another distribution across all Amazon Web Services (AWS) accounts, including distributions on the Amazon CloudFront service. You will be able to create the certificate for the domains, but you will not be able to use it with your distribution.

For more information about distributions, see [Content delivery network distributions](amazon-lightsail-content-delivery-network-distributions.md).

### Prerequisites
<a name="enable-distribution-custom-domains-prerequisite"></a>

Before you get started, you need to create a Lightsail distribution. For more information, see [Create a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md).

You also should have created and validated an SSL/TLS certificate for your distribution. For more information, see the following topics:
+ [Secure Lightsail CDN distributions with SSL/TLS certificates](amazon-lightsail-create-a-distribution-certificate.md)
+ [Validate SSL/TLS certificates for Lightsail distributions](amazon-lightsail-validating-a-distribution-certificate.md)

**Note**  
If a Lightsail web address is attached to your distribution, detach it first. For instructions, see [Detach a web address from your distribution](amazon-lightsail-distribution-web-address.md#distribution-web-address-detach).

### Enable custom domains for your distribution
<a name="enable-distribution-custom-domains"></a>

Complete the following procedure to enable custom domains for your distribution.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the name of the distribution for which you want to enable custom domains.

1. Choose the **Domains** tab on your distribution's management page, and then choose **Custom domain**.

1. Choose **Attach certificate**.

   If you have no certificates, then you must first create and validate an SSL/TLS certificate for your domains, before you can attach it to your distribution. For more information, see [Secure Lightsail CDN distributions with SSL/TLS certificates](amazon-lightsail-create-a-distribution-certificate.md).

1. In the dropdown menu that appears, select a valid certificate for the domain(s) that you want to use with your distribution.

1. Verify the certificate information is correct, then choose **Attach**.

1. The distribution's **Status** will change to **Updating**. After the status changes to **Enabled**, the certificate's domain will appear in the **Custom domains** section. 

1. Choose **Add domain assignment** to point the domain to your distribution.

1. Verify the certificate and DNS information are correct, then choose **Add assignment**. After a few moments, traffic for the domain that you selected will begin to be accepted by your distribution.

## Switch between a web address and a custom domain
<a name="switch-web-address-custom-domain"></a>

A distribution can use a Lightsail web address or a custom domain, but not both. While you switch, your distribution is reachable at its default domain.

**To switch from a web address to a custom domain**

1. Detach the web address from your distribution. It stops working within a few minutes. For instructions, see [Detach a web address from your distribution](amazon-lightsail-distribution-web-address.md#distribution-web-address-detach).

   In the Lightsail console, the **Custom domain** option isn't available until you detach the web address. To create and validate your certificate before you detach, use the [create-certificate](https://docs.aws.amazon.com/cli/latest/reference/lightsail/create-certificate.html) command of the AWS CLI.

1. Create an SSL/TLS certificate for your domain. For instructions, see [Secure Lightsail CDN distributions with SSL/TLS certificates](amazon-lightsail-create-a-distribution-certificate.md).

1. Validate your certificate. For instructions, see [Validate SSL/TLS certificates for Lightsail distributions](amazon-lightsail-validating-a-distribution-certificate.md).

1. Enable custom domains for your distribution. For instructions, see [Enable custom domains for your distribution](#enable-distribution-custom-domains).

1. Point your domain to your distribution. For instructions, see [Point custom domains to Lightsail distributions](amazon-lightsail-point-domain-to-distribution.md).

1. Keep or delete the web address. If you delete a web address that was attached, only your account can create a web address with the same name for 30 to 37 days. For more information, see [What happens to the name of a deleted web address](amazon-lightsail-delete-web-address.md#web-address-cooldown).
**Note**  
Each month, you get 24 hours of free unattached web address time. After that, we charge USD $1 per month for each unattached web address.

**To switch from a custom domain to a web address**

1. Disable custom domains for your distribution. Visitors to your custom domain get a 403 error until you point the domain somewhere else. For instructions, see [Disable custom domains for Lightsail distributions](amazon-lightsail-disabling-distribution-custom-domains.md).

1. Attach a web address to your distribution. For instructions, see [Attach a web address from your distribution's management page](amazon-lightsail-distribution-web-address.md#distribution-web-address-attach).

If the origin of your distribution is a WordPress instance, configure WordPress to use the new name after you switch. For instructions, see [Configure WordPress with a Lightsail content delivery network](amazon-lightsail-configure-wordpress-for-distribution.md).

**Topics**
+ [Use a custom domain with your distribution](#distribution-custom-domain)
+ [Switch between a web address and a custom domain](#switch-web-address-custom-domain)
+ [Attach a web address](amazon-lightsail-distribution-web-address.md)
+ [Point your domain to a distribution](amazon-lightsail-point-domain-to-distribution.md)
+ [Change custom domain](amazon-lightsail-changing-distribution-custom-domains.md)
+ [Disable distribution custom domains](amazon-lightsail-disabling-distribution-custom-domains.md)
+ [Add distribution domain to container service](amazon-lightsail-adding-distribution-default-domain-to-container-service.md)