

# Secure Lightsail CDN distributions with SSL/TLS certificates
<a name="amazon-lightsail-create-a-distribution-certificate"></a>

You can create Amazon Lightsail TLS/SSL certificates for your Lightsail distributions. When you create a certificate, you specify the primary and alternate domain names for the certificate. When you enable custom domains for your distribution, and choose the certificate, those domains are added as the custom domains of your distribution. After you update the DNS record of your domains to point to your distribution, your distribution accepts the traffic and serves your content using HTTPS. There is a quota for the number of certificates that you can create. For more information, see [Lightsail service quotas](https://docs.aws.amazon.com/general/latest/gr/lightsail.html#limits_lightsail).

For more information about SSL/TLS certificates, see [SSL/TLS certificates](understanding-tls-ssl-certificates-in-lightsail-https.md).

**Important**  
The domain names you specify when creating an SSL/TLS certificate for your distribution cannot be in use by another distribution across all Amazon Web Services (AWS) accounts, including distributions on the Amazon CloudFront service. You will be able to create the certificate for the domains, but you will not be able to use the certificate with your distribution.

## Prerequisite
<a name="create-distribution-prerequisite"></a>

Before you get started, you need to create a Lightsail distribution. For more information, see [Create a distribution](amazon-lightsail-creating-content-delivery-network-distribution.md) and [Content delivery network distributions](amazon-lightsail-content-delivery-network-distributions.md).

## Create an SSL/TLS certificate for your distribution
<a name="create-distribution-certificate"></a>

Complete the following procedure to create an SSL/TLS certificate for your distribution.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Networking**.

1. Choose the name of the distribution for which want to create a certificate.

1. Choose the **Custom domains** tab on your distribution's management page.

1. Scroll down to the **Attached certificates** section of the page.

   All of your distribution certificates are listed under the **Attached certificates** section of the page, including certificates created for other distributions, and certificates that are in use and not in use.

1. Choose **Create certificate**.

1. Enter a unique name in the **Certificate name** text box to identify your certificate. Then, choose **Continue**.

1. Enter the primary domain name (e.g., `example.com`) that you want to use with the certificate into the **Specify up to 10 domains or subdomains** field.

1. (Optional) Enter alternate domain names (e.g., `www.example.com`) into the remaining **Specify up to 10 domains or subdomains** fields.

   You can add up to nine alternate domains to your certificate. You will be able to use all of your certificate's domains with your distribution after you enable custom domains and select the certificate for your distribution.

1. Choose **Create**.

   Your certificate request is submitted, and the status of your new certificate is changed to **Attempting to validate your certificate**. During this time, Lightsail attempts to add the certificate's validation record to the DNS of the primary domain. After a while, the status will change to **Valid**.

   If automatic validation fails, you will be required to validate the certificate with your domains before you can use it with your distribution. For more information, see [Validate SSL/TLS certificates for your distribution](amazon-lightsail-validating-a-distribution-certificate.md).

**Topics**
+ [Prerequisite](#create-distribution-prerequisite)
+ [Create an SSL/TLS certificate for your distribution](#create-distribution-certificate)
+ [View SSL/TLS certificates](amazon-lightsail-viewing-distribution-certificates.md)
+ [Validate SSL/TLS certificates](amazon-lightsail-validating-a-distribution-certificate.md)
+ [Configure TLS protocol](amazon-lightsail-configure-distribution-tls-version.md)
+ [Delete distribution certificates](amazon-lightsail-deleting-distribution-certificates.md)