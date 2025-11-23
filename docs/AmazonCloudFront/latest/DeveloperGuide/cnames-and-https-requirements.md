# Requirements for using SSL/TLS certificates with

CloudFront

The requirements for SSL/TLS certificates are described in this topic. They apply to both
of the following, except as noted:

- Certificates for using HTTPS between viewers and CloudFront
- Certificates for using HTTPS between CloudFront and your origin

###### Topics

- [Certificate issuer](#https-requirements-certificate-issuer "#https-requirements-certificate-issuer")
- [AWS Region for AWS Certificate Manager](#https-requirements-aws-region "#https-requirements-aws-region")
- [Certificate format](#https-requirements-certificate-format "#https-requirements-certificate-format")
- [Intermediate
  certificates](#https-requirements-intermediate-certificates "#https-requirements-intermediate-certificates")
- [Key type](#https-requirements-key-type "#https-requirements-key-type")
- [Private key](#https-requirements-private-key "#https-requirements-private-key")
- [Permissions](#https-requirements-permissions "#https-requirements-permissions")
- [Size of the certificate key](#https-requirements-size-of-public-key "#https-requirements-size-of-public-key")
- [Supported types of certificates](#https-requirements-supported-types "#https-requirements-supported-types")
- [Certificate expiration date and
  renewal](#https-requirements-cert-expiration "#https-requirements-cert-expiration")
- [Domain names in the CloudFront distribution
  and in the certificate](#https-requirements-domain-names-in-cert "#https-requirements-domain-names-in-cert")
- [Minimum SSL/TLS protocol
  version](#https-requirements-minimum-ssl-protocol-version "#https-requirements-minimum-ssl-protocol-version")
- [Supported HTTP versions](#https-requirements-supported-http-versions "#https-requirements-supported-http-versions")

## Certificate issuer

We recommend that you use a public certificate issued by [AWS Certificate Manager (ACM)](https://aws.amazon.com/certificate-manager/ "https://aws.amazon.com/certificate-manager/"). For
information about getting a certificate from ACM, see the _[AWS Certificate Manager User Guide](../../../acm/latest/userguide.md "../../../acm/latest/userguide.md")_. To use an ACM certificate with a
CloudFront distribution, make sure you request (or import) the certificate in the
US East (N. Virginia) Region (`us-east-1`).

CloudFront supports the same certificate authorities (CAs) as Mozilla, so if you don’t use
ACM, use a certificate issued by a CA on the [Mozilla Included CA
Certificate List](https://wiki.mozilla.org/CA/Included_Certificates "https://wiki.mozilla.org/CA/Included_Certificates").

TLS certificates used by the origin that you specified for your CloudFront
distribution also need to be issued from the CA on the Mozilla Included CA
Certificate List.

For more information about getting and installing a certificate, refer to the
documentation for your HTTP server software and to the documentation for the
CA.

## AWS Region for AWS Certificate Manager

To use a certificate in AWS Certificate Manager (ACM) to require HTTPS between viewers and
CloudFront, make sure you request (or import) the certificate in the
US East (N. Virginia) Region (`us-east-1`).

If you want to require HTTPS between CloudFront and your origin, and you’re using a load
balancer in ELB as your origin, you can request or import the certificate in
any AWS Region.

## Certificate format

The certificate must be in X.509 PEM format. This is the default format if you’re using
AWS Certificate Manager.

## Intermediate

certificates

If you’re using a third-party certificate authority (CA), list all of the intermediate
certificates in the certificate chain that’s in the `.pem`
file, beginning with one for the CA that signed the certificate for your domain.
Typically, you’ll find a file on the CA website that lists intermediate and root
certificates in the proper chained order.

###### Important

Do not include the following: the root certificate, intermediate certificates that are
not in the trust path, or your CA’s public key certificate.

Here’s an example:

```
-----BEGIN CERTIFICATE-----
`Intermediate certificate 2`
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
`Intermediate certificate 1`
-----END CERTIFICATE-----
```

## Key type

CloudFront supports RSA and ECDSA public–private key pairs.

CloudFront supports HTTPS connections to both viewers and origins using RSA and
ECDSA certificates. With [AWS Certificate Manager
(ACM)](https://console.aws.amazon.com/acm "https://console.aws.amazon.com/acm"), you can request and import RSA or ECDSA certificates and then associate them with your CloudFront distribution.

For lists of the RSA and ECDSA ciphers supported by CloudFront that you can
negotiate in HTTPS connections, see [Supported
protocols and ciphers between viewers and CloudFront](secure-connections-supported-viewer-protocols-ciphers.md "secure-connections-supported-viewer-protocols-ciphers.md") and [Supported
protocols and ciphers between CloudFront and the origin](secure-connections-supported-ciphers-cloudfront-to-origin.md "secure-connections-supported-ciphers-cloudfront-to-origin.md").

## Private key

If you're using a certificate from a third-party certificate authority (CA),
note the following:

- The private key must match the public key that is in the
  certificate.
- The private key must be in PEM format.
- The private key cannot be encrypted with a password.

If AWS Certificate Manager (ACM) provided the certificate, ACM doesn’t release the private key. The
private key is stored in ACM for use by AWS services that are integrated
with ACM.

## Permissions

You must have permission to use and import the SSL/TLS certificate. If you’re using
AWS Certificate Manager (ACM), we recommend that you use AWS Identity and Access Management permissions to restrict
access to the certificates. For more information, see [Identity
and access management](../../../acm/latest/userguide/security-iam.md "../../../acm/latest/userguide/security-iam.md") in the
_AWS Certificate Manager User Guide_.

## Size of the certificate key

The certificate key size that CloudFront supports depends on the type of key and
certificate.

**For RSA certificates:**

CloudFront supports 1024-bit, 2048-bit, and 3072-bit, and 4096-bit RSA keys. The maximum key length for an RSA certificate that
you use with CloudFront is 4096 bits.

Note that ACM issues RSA certificates with up to 2048-bit keys.
To use a 3072-bit or 4096-bit RSA certificate, you need to obtain the certificate externally and import it into ACM, after which it will be available for you to use with CloudFront.

For information about how to determine the size of an RSA key, see
[Determine the size of the public key in
an SSL/TLS RSA certificate](cnames-and-https-size-of-public-key.md "cnames-and-https-size-of-public-key.md").

**For ECDSA certificates:**

CloudFront supports 256-bit keys. To use an ECDSA certificate in ACM
to require HTTPS between viewers and CloudFront, use the prime256v1
elliptic curve.

## Supported types of certificates

CloudFront supports all types of certificates issued by a trusted certificate authority.

## Certificate expiration date and

renewal

If you’re using certificates that you get from a third-party certificate authority (CA),
you must monitor certificate expiration dates and renew the certificates that
you import into AWS Certificate Manager (ACM) or upload to the AWS Identity and Access Management certificate store
before they expire.

###### Important

To avoid certificate expiration issues, renew or reimport your certificate
at least 24 hours before the `NotAfter` value of your current
certificate. If your certificate expires within 24 hours, request a new
certificate from ACM or import a new certificate to ACM. Next, associate
the new certificate to the CloudFront distribution.

CloudFront might continue to use the previous certificate while your certificate
renewal or reimport is in progress. This is an asynchronous process that can
take up to 24 hours before CloudFront shows your changes.

If you’re using ACM provided certificates, ACM manages certificate renewals for you.
For more information, see [Managed renewal](../../../acm/latest/userguide/managed-renewal.md "../../../acm/latest/userguide/managed-renewal.md") in the
_AWS Certificate Manager User Guide_.

## Domain names in the CloudFront distribution

and in the certificate

When you’re using a custom origin, the SSL/TLS certificate on your origin includes a
domain name in the **Common Name** field, and possibly several
more in the **Subject Alternative Names** field. (CloudFront supports
wildcard characters in certificate domain names.)

One of the domain names in the certificate must match the domain name that you
specify for Origin Domain Name. If no domain name matches, CloudFront returns HTTP
status code `502 (Bad Gateway)` to the viewer.

###### Important

When you add an alternate domain name to a distribution, CloudFront checks that the alternate
domain name is covered by the certificate that you’ve attached. The
certificate must cover the alternate domain name in the subject alternate
name (SAN) field of the certificate. This means the SAN field must contain
an exact match for the alternate domain name, or contain a wildcard at the
same level of the alternate domain name that you’re adding.

For more information, see [Requirements for using alternate domain
names](CNAMEs.md#alternate-domain-names-requirements "CNAMEs.md#alternate-domain-names-requirements").

## Minimum SSL/TLS protocol

version

If you’re using dedicated IP addresses, set the minimum SSL/TLS protocol version for the
connection between viewers and CloudFront by choosing a security policy.

For more information, see [Security policy (minimum
SSL/TLS version)](DownloadDistValuesGeneral.md#DownloadDistValues-security-policy "DownloadDistValuesGeneral.md#DownloadDistValues-security-policy") in the topic [All distribution settings reference](distribution-web-values-specify.md "distribution-web-values-specify.md").

## Supported HTTP versions

If you associate one certificate with more than one CloudFront distribution, all the
distributions associated with the certificate must use the same option for [Supported HTTP
versions](DownloadDistValuesGeneral.md#DownloadDistValuesSupportedHTTPVersions "DownloadDistValuesGeneral.md#DownloadDistValuesSupportedHTTPVersions"). You specify this
option when you create or update a CloudFront distribution.
