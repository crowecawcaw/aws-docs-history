# Serve content with

custom domains for your Lightsail distribution

Enable custom domains for your Amazon Lightsail distribution to use your registered domain
names with your distribution. Before you enable custom domains, your distribution accepts
traffic only for the default domain that is associated with your distribution when you first
create it (e.g., `123456abcdef.cloudfront.net`). When you enable custom domains, you
must choose the Lightsail SSL/TLS certificate that you created for the domains that you want
to use with your distribution. After you enable custom domains, your distribution accepts
traffic for all of the domains that are associated with the certificate that you chose.

###### Important

Only one certificate can be in use at a time per distribution. If you disable custom
domains on your distribution, your distribution is no longer able to handle HTTPS traffic for
your registered domain until you enable custom domains again.

The domain names associated with the SSL/TLS certificate cannot be in use by another
distribution across all Amazon Web Services (AWS) accounts, including distributions on the Amazon CloudFront
service. You will be able to create the certificate for the domains, but you will not be able
to use it with your distribution.

For more information about distributions, see [Content delivery network
distributions](amazon-lightsail-content-delivery-network-distributions.md "amazon-lightsail-content-delivery-network-distributions.md").

## Prerequisites

Before you get started, you need to create a Lightsail distribution. For more
information, see [Create a
distribution](amazon-lightsail-creating-content-delivery-network-distribution.md "amazon-lightsail-creating-content-delivery-network-distribution.md").

You also should have created and validated an SSL/TLS certificate for your distribution.
For more information, see [Create SSL/TLS certificates for your distribution](amazon-lightsail-create-a-distribution-certificate.md "amazon-lightsail-create-a-distribution-certificate.md") and [Validate SSL/TLS
certificates for your distribution](amazon-lightsail-validating-a-distribution-certificate.md "amazon-lightsail-validating-a-distribution-certificate.md").

## Enable custom domains for your

distribution

Complete the following procedure to enable custom domains for your distribution.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/ "https://lightsail.aws.amazon.com/").
2. In the left navigation pane, choose **Networking**.
3. Choose the name of the distribution for which want to enable custom domains.
4. Choose the **Custom domains** tab on your distribution's management
   page.
5. Choose **Attach certificate**.

If you have no certificates, then you must first create and validate an SSL/TLS
certificate for your domains, before you can attach it to your distribution. For more
information, see [Create
SSL/TLS certificates for your distribution](amazon-lightsail-create-a-distribution-certificate.md "amazon-lightsail-create-a-distribution-certificate.md"). 6. In the dropdown menu that appears, select a valid certificate for the domain(s) that
you want to use with your distribution. 7. Verify the certificate information is correct, then choose
**Attach**. 8. The distribution's **Status** will change to
**Updating**. After the status changes to **Enabled**,
the certificate's domain will appear in the **Custom domains** section. 9. Choose **Add domain assignment** to point the domain to your
distribution. 10. Verify the certificate and DNS information are correct, then choose **Add
assignment**. After a few moments, traffic for the domain that you selected
will begin to be accepted by your distribution.

###### Topics

- [Point your domain to a distribution](amazon-lightsail-point-domain-to-distribution.md "amazon-lightsail-point-domain-to-distribution.md")
- [Change custom domain](amazon-lightsail-changing-distribution-custom-domains.md "amazon-lightsail-changing-distribution-custom-domains.md")
- [Disable distribution custom domains](amazon-lightsail-disabling-distribution-custom-domains.md "amazon-lightsail-disabling-distribution-custom-domains.md")
- [Add distribution domain to container service](amazon-lightsail-adding-distribution-default-domain-to-container-service.md "amazon-lightsail-adding-distribution-default-domain-to-container-service.md")
