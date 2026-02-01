# Delete unused SSL/TLS

certificates from Lightsail distributions

###### Warning

Deleting an SSL/TLS certificate is final and can't be undone.

You can delete Amazon Lightsail SSL/TLS certificates that you're no longer using on your
distributions. For example, your certificate might be expired and you've already attached an
updated certificate that's validated. For more information about certificates, see [SSL/TLS certificates](understanding-tls-ssl-certificates-in-lightsail-https.md "understanding-tls-ssl-certificates-in-lightsail-https.md").
For more information about distributions, see [Content delivery network
distributions](amazon-lightsail-content-delivery-network-distributions.md "amazon-lightsail-content-delivery-network-distributions.md").

You have a quota of certificates that you can create over a 365-day period. For more information, see [Lightsail service quotas](../../../general/latest/gr/lightsail.md#limits_lightsail "../../../general/latest/gr/lightsail.md#limits_lightsail") in the _AWS General Reference_.

## Delete an SSL/TLS certificate for your

distribution

###### Important

The **Delete** option is unavailable if the certificate you want to delete is in use. To delete certificates that are in use, you must
first change the custom domains of the distribution that are using the certificate, or disable custom domains on the distribution that are using the certificate.

Complete the following procedure to delete an SSL/TLS certificate for your
distribution.

1. Sign in to the [Lightsail console](https://lightsail.aws.amazon.com/ "https://lightsail.aws.amazon.com/").
2. In the left navigation pane, choose **Networking**.
3. Choose the name of the distribution from which you want to delete the SSL/TLS
   certificate. If the certificate is not currently in use, then you can choose any
   distribution because all of your certificates are listed in every distribution.
4. Choose the **Custom domains** tab on your distribution's management
   page.
5. In the **Certificates** section of the page, choose the ellipsis icon
   (⋮) for the certificate that you want to delete, and choose
   **Delete**.

The **Delete** option is unavailable if the certificate you want to
delete is in use. To delete certificates that are in use, you need to first change the
custom domains of the distribution that is using the certificate, or disable custom
domains on the distribution that is using the certificate. For more information, see [Change custom domains
for your distribution](amazon-lightsail-changing-distribution-custom-domains.md "amazon-lightsail-changing-distribution-custom-domains.md") and [Enable custom
domains for your distribution](amazon-lightsail-disabling-distribution-custom-domains.md#amazon-lightsail-disabling-distribution-custom-domains.title "amazon-lightsail-disabling-distribution-custom-domains.md#amazon-lightsail-disabling-distribution-custom-domains.title"). 6. Choose **Yes, delete** to confirm the deletion.
