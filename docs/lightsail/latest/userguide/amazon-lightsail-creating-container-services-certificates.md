# Create SSL/TLS

certificates for secure Lightsail container service domains

You can create Amazon Lightsail TLS/SSL certificates for your Lightsail container service.
When you create a certificate, you specify the primary and alternate domain names for the
certificate. When you enable custom domains for your container service, and choose the
certificate, you can choose up to four domains from the certificate that will be added as the
custom domains of your container service. After you update the DNS record of your domains to
direct traffic to your container service, your service accepts the traffic and serves your
content using HTTPS. There is a quota for the number of certificates that you can create. For
more information, see [Lightsail service quotas](../../../general/latest/gr/lightsail.md "../../../general/latest/gr/lightsail.md").

For more information about SSL/TLS certificates, see [Container service
certificates](understanding-tls-ssl-certificates-in-lightsail-https.md "understanding-tls-ssl-certificates-in-lightsail-https.md").

## Prerequisites

Before you get started, you need to create a Lightsail container service. For more
information, see [Create a
container services](amazon-lightsail-creating-container-services.md "amazon-lightsail-creating-container-services.md") and [Container
services](amazon-lightsail-container-services.md "amazon-lightsail-container-services.md").

## Create an SSL/TLS certificate for

your container service

Complete the following procedure to create an SSL/TLS certificate for your container
service.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/ "https://lightsail.aws.amazon.com/").
2. In the left navigation pane, choose **Containers**.
3. Choose the name of the container service for which want to create a
   certificate.
4. Choose the **Custom domains** tab on your container service
   management page.
5. Scroll down to the **Attached certificates** section of the
   page.

All of your certificates are listed under the Attached certificates section of the
page, including certificates created for other Lightsail resources, and certificates
that are in use and not in use. 6. Choose **Create certificate**. 7. Enter a unique name in the **Certificate name** text box to identify
your certificate. Then, choose **Continue**. 8. Enter the primary domain name (e.g., `example.com`) that you want to use
with the certificate into the **Specify up to 10 domains or subdomains**
field. 9. (Optional) Enter another domain name (e.g., www.example.com) into the
**Specify up to 10 domains or subdomains** field.

You can add up to nine alternate domains to your certificate. You can use up to four
of your certificate's domains with your container service after you enable custom domains
and select the certificate for your service. 10. Choose **Create certificate**.

Your certificate request is submitted, and the status of your new certificate is
changed to **Attempting to validate your certificate**. During this time,
Lightsail attempts to add the certificate's validation record to the DNS of the primary
domain. After a while, the status will change to **Valid**.

If automatic validation fails you will be required to validate the certificate with
your domains before you can use it with your container service. For more information, see
[Validate
container service SSL/TLS certificates](amazon-lightsail-validating-container-services-certificates.md "amazon-lightsail-validating-container-services-certificates.md").

###### Topics

- [Validate certificates](amazon-lightsail-validating-container-services-certificates.md "amazon-lightsail-validating-container-services-certificates.md")
- [View certificates](amazon-lightsail-viewing-container-services-certificates.md "amazon-lightsail-viewing-container-services-certificates.md")
