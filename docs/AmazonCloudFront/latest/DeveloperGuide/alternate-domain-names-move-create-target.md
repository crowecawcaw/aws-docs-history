# Set up the target

standard distribution or distribution tenant

Before you can move an alternate domain name, you must set up the target resource.
This is the target standard distribution or distribution tenant that you're moving the alternate domain name
to.

Standard distribution

###### To set up a target standard distribution

1. Request a TLS certificate. This certificate includes the alternate
   domain name as the Subject or Subject Alternative Domain (SAN), or a
   wildcard (\*) that covers the alternate domain name that you’re
   moving. If you don’t have one, you can request one from AWS Certificate Manager
   (ACM) or from another certificate authority (CA) and import it
   into ACM.

###### Note

You must request or import the certificate in the
US East (N. Virginia) (`us-east-1`) Region.

For more information, see [Request a public certificate using the
console](../../../acm/latest/userguide/acm-public-certificates.md#request-public-console "../../../acm/latest/userguide/acm-public-certificates.md#request-public-console") and [Import a certificate](../../../acm/latest/userguide/import-certificate-api-cli.md "../../../acm/latest/userguide/import-certificate-api-cli.md") in the
AWS Certificate Manager in the _AWS Certificate Manager User Guide_. 2. If you haven’t created the target standard distribution, create one now. As
part of creating the standard distribution, associate the certificate with this
standard distribution. For more information, see [Create a distribution](distribution-web-creating-console.md "distribution-web-creating-console.md").

If you already have a target standard distribution, associate the certificate
with the standard distribution. For more information, see [Update a distribution](HowToUpdateDistribution.md "HowToUpdateDistribution.md"). 3. **If you’re moving alternate domain names
within the same AWS account, skip this step.**

To move an alternate domain name from one AWS account to
another, you must create a TXT record in your DNS configuration.
This verification step helps prevent unauthorized domain transfers.
CloudFront uses this TXT record to validate your ownership of the
alternate domain name.

In your DNS configuration, create a DNS TXT record that associates
the alternate domain name with the target standard distribution. The TXT record
format can vary, depending on the domain type.

    * For subdomains, specify an underscore (`_`) in
     front of the alternate domain name. The following shows an
     example TXT record.


    `_www.example.com TXT
     d111111abcdef8.cloudfront.net`
    * For an apex (or root domain), specify an underscore and
     period ( `_.`) in front of the domain name. The
     following shows an example TXT record.


    `_.example.com TXT d111111abcdef8.cloudfront.net`

Distribution tenant

###### To set up the target distribution tenant

1. Request a TLS certificate. This certificate includes the alternate
   domain name as the Subject or Subject Alternative Domain (SAN), or a
   wildcard (\*) that covers the alternate domain name that you’re
   moving. If you don’t have one, you can request one from AWS Certificate Manager
   (ACM) or from another certificate authority (CA) and import it
   into ACM.

###### Note

You must request or import the certificate in the
US East (N. Virginia) (`us-east-1`) Region.

For more information, see [Request a public certificate using the
console](../../../acm/latest/userguide/acm-public-certificates.md#request-public-console "../../../acm/latest/userguide/acm-public-certificates.md#request-public-console") and [Import a certificate](../../../acm/latest/userguide/import-certificate-api-cli.md "../../../acm/latest/userguide/import-certificate-api-cli.md") in the
AWS Certificate Manager in the _AWS Certificate Manager User Guide_. 2. If you haven’t created the target distribution tenant, create one now. As
part of creating the distribution tenant, associate the certificate with the
distribution tenant. For more information, see [Create a distribution](distribution-web-creating-console.md "distribution-web-creating-console.md").

If you already have a target distribution tenant, associate the certificate
with the distribution tenant. For more information, see [Add a domain and certificate
(distribution tenant)](managed-cloudfront-certificates.md#vanity-domain-tls-tenant "managed-cloudfront-certificates.md#vanity-domain-tls-tenant"). 3. **If you’re moving alternate domain names
within the same AWS account, skip this step.**

To move an alternate domain name from one AWS account to
another, you must create a TXT record in your DNS configuration.
This verification step helps prevent unauthorized domain transfers,
and CloudFront uses this TXT record to validate your ownership of the
alternate domain name.

In your DNS configuration, create a DNS TXT record that associates
the alternate domain name with the target distribution tenant. The TXT record
format can vary, depending on the domain type.

    * For subdomains, specify an underscore (`_`) in
     front of the alternate domain name. The following shows an
     example TXT record.


    `_www.example.com TXT
     d111111abcdef8.cloudfront.net`
    * For an apex (or root domain), specify an underscore and
     period ( `_.`) in front of the domain name. The
     following shows an example TXT record.


    `_.example.com TXT d111111abcdef8.cloudfront.net`

Next, see the following topic to find the source standard distribution or distribution tenant that is already
associated with the alternate domain name.
