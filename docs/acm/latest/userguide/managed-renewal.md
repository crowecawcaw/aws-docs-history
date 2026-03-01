# Managed certificate renewal in AWS Certificate Manager

ACM provides managed renewal for your Amazon-issued SSL/TLS certificates. This means
that ACM will either renew your certificates automatically (if you are using DNS
validation), or it will send you email notices when expiration is approaching. These
services are provided for both public and private ACM certificates.

A certificate is eligible for automatic renewal subject to the following
considerations:

- ELIGIBLE if associated with another AWS service, such as Elastic Load Balancing or CloudFront.
- ELIGIBLE if exported since being issued or last renewed.
- ELIGIBLE if it is a private certificate issued by calling the ACM [RequestCertificate](../APIReference/API_RequestCertificate.md "../APIReference/API_RequestCertificate.md") API
  _and_ then exported or associated with another
  AWS service.
- ELIGIBLE if it is a private certificate issued through the [management console](gs-acm-request-private.md "gs-acm-request-private.md")
  _and_ then exported or associated with another
  AWS service.
- NOT ELIGIBLE if it is a private certificate issued by calling the AWS Private CA
  [IssueCertificate](../../../privateca/latest/APIReference/API_IssueCertificate.md "../../../privateca/latest/APIReference/API_IssueCertificate.md")
  API.
- NOT ELIGIBLE if [imported](import-certificate.md "import-certificate.md").
- NOT ELIGIBLE if already expired.
  Additionally, the following [Punycode](https://datatracker.ietf.org/doc/html/rfc3492 "https://datatracker.ietf.org/doc/html/rfc3492") requirements relating to [Internationalized Domain
  Names](https://www.icann.org/resources/pages/idn-2012-02-25-en "https://www.icann.org/resources/pages/idn-2012-02-25-en") must be fulfilled:

1. Domain names beginning with the pattern "<character><character>--" must
   match "xn--".
2. Domain names beginning with "xn--" must also be valid Internationalized Domain
   Names.

| Punycode examples | Domain Name | Fulfills #1 | Fulfills #2 | Allowed                                                  | Note |
| ----------------- | ----------- | ----------- | ----------- | -------------------------------------------------------- | ---- |
| example.com       | n/a         | n/a         | ✓           | Does not start with "<character><character>--"           |
| a--example.com    | n/a         | n/a         | ✓           | Does not start with "<character><character>--"           |
| abc--example.com  | n/a         | n/a         | ✓           | Does not start with "<character><character>--"           |
| xn--xyz.com       | Yes         | Yes         | ✓           | Valid Internationalized Domain Name (resolves to 简.com) |
| xn--example.com   | Yes         | No          | ✗           | Not a valid Internationalized Domain Name                |
| ab--example.com   | No          | No          | ✗           | Must start with "xn--"                                   |

When ACM renews a certificate, the certificate's Amazon Resource Name (ARN) remains the
same. Also, ACM certificates are [regional resources](acm-overview.md#acm-regions "acm-overview.md#acm-regions"). If
you have certificates for the same domain name in multiple AWS Regions, each of these
certificates must be renewed independently.

###### Topics

- [Renew ACM public certificates](renew-publicly-trusted.md "renew-publicly-trusted.md")
- [Private certificate renewal in AWS Certificate Manager](renew-private-cert.md "renew-private-cert.md")
- [Check a certificate's renewal status](check-certificate-renewal-status.md "check-certificate-renewal-status.md")
