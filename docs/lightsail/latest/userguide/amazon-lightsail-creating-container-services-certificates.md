

# Create SSL/TLS certificates for secure Lightsail container service domains
<a name="amazon-lightsail-creating-container-services-certificates"></a>

You can create Amazon Lightsail TLS/SSL certificates for your Lightsail container service. When you create a certificate, you specify the primary and alternate domain names for the certificate. When you enable custom domains for your container service, and choose the certificate, you can choose up to four domains from the certificate that will be added as the custom domains of your container service. After you update the DNS record of your domains to direct traffic to your container service, your service accepts the traffic and serves your content using HTTPS. There is a quota for the number of certificates that you can create. For more information, see [Lightsail service quotas](https://docs.aws.amazon.com/general/latest/gr/lightsail.html).

For more information about SSL/TLS certificates, see [Container service certificates](understanding-tls-ssl-certificates-in-lightsail-https.md).

## Prerequisites
<a name="creating-container-service-certificate-prerequisites"></a>

Before you get started, you need to create a Lightsail container service. For more information, see [Create a container services](amazon-lightsail-creating-container-services.md) and [Container services](amazon-lightsail-container-services.md).

## Create an SSL/TLS certificate for your container service
<a name="creating-container-service-certificate"></a>

Complete the following procedure to create an SSL/TLS certificate for your container service.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/).

1. In the left navigation pane, choose **Containers**.

1. Choose the name of the container service for which want to create a certificate.

1. Choose the **Custom domains** tab on your container service management page.

1. Scroll down to the **Attached certificates** section of the page.

   All of your certificates are listed under the Attached certificates section of the page, including certificates created for other Lightsail resources, and certificates that are in use and not in use.

1. Choose **Create certificate**.

1. Enter a unique name in the **Certificate name** text box to identify your certificate. Then, choose **Continue**.

1. Enter the primary domain name (e.g., `example.com`) that you want to use with the certificate into the **Specify up to 10 domains or subdomains** field.

1. (Optional) Enter another domain name (e.g., www.example.com) into the **Specify up to 10 domains or subdomains** field.

   You can add up to nine alternate domains to your certificate. You can use up to four of your certificate's domains with your container service after you enable custom domains and select the certificate for your service.

1. Choose **Create certificate**.

   Your certificate request is submitted, and the status of your new certificate is changed to **Attempting to validate your certificate**. During this time, Lightsail attempts to add the certificate's validation record to the DNS of the primary domain. After a while, the status will change to **Valid**.

   If automatic validation fails you will be required to validate the certificate with your domains before you can use it with your container service. For more information, see [Validate container service SSL/TLS certificates](amazon-lightsail-validating-container-services-certificates.md).

**Topics**
+ [Prerequisites](#creating-container-service-certificate-prerequisites)
+ [Create an SSL/TLS certificate for your container service](#creating-container-service-certificate)
+ [Validate certificates](amazon-lightsail-validating-container-services-certificates.md)
+ [View certificates](amazon-lightsail-viewing-container-services-certificates.md)