# View SSL/TLS certificates

for Lightsail distributions

You can view the Amazon Lightsail SSL/TLS certificates that you created for your Lightsail
distributions. You do this by accessing the management page of any distribution in the
Lightsail console.

For more information about SSL/TLS certificates, see [SSL/TLS
certificates](understanding-tls-ssl-certificates-in-lightsail-https.md "understanding-tls-ssl-certificates-in-lightsail-https.md").

## Prerequisites

Before you get started, you need to create a Lightsail distribution. For more
information, see [Create a
distribution](amazon-lightsail-creating-content-delivery-network-distribution.md "amazon-lightsail-creating-content-delivery-network-distribution.md") and [Content delivery network
distributions](amazon-lightsail-content-delivery-network-distributions.md "amazon-lightsail-content-delivery-network-distributions.md").

You also should have created an SSL/TLS certificate for your distribution. For more
information, see [Create
SSL/TLS certificates for your distribution](amazon-lightsail-create-a-distribution-certificate.md "amazon-lightsail-create-a-distribution-certificate.md").

## View your distribution SSL/TLS

certificates

Complete the following procedure to view your distribution SSL/TLS certificates.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/ "https://lightsail.aws.amazon.com/").
2. In the left navigation pane, choose **Networking**.
3. Choose the name of a distribution.

You can view all of your certificates regardless of the distribution you
choose. 4. Choose the **Custom domains** tab on your distribution's management
page. 5. Scroll down to the **Attached certificates** section of the
page.

All of your distribution certificates are listed under the **Attached
certificates** section of the page. Expand **Validation
details** to view your certificate's important dates, encryption details,
identification, and validation records. Your certificates are valid for 13 months from the
date you created them, after which time Lightsail attempts to automatically revalidate
them. Don't delete the CNAME records that you added to your domain because they are
required when your certificate is re-validated on the **Valid until**
date listed.

After you have a valid SSL/TLS certificate to use with your distribution, you should
enable custom domains so that you can use the domain names of the certificate on your
distribution. For more information, see [Enable custom domains
for your distribution](amazon-lightsail-enabling-distribution-custom-domains.md "amazon-lightsail-enabling-distribution-custom-domains.md").
