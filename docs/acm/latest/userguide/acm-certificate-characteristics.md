# AWS Certificate Manager public certificate

characteristics and limitations

Public certificates provided by ACM have the following characteristics and
limitations. These apply only to certificates provided by ACM. They might not apply to
[imported certificates](import-certificate.md "import-certificate.md").

**Browser and application trust**

ACM certificates are trusted by all major browsers including Google
Chrome, Microsoft Edge, Mozilla Firefox, and Apple Safari. Browsers display
a lock icon when connected by TLS to sites using ACM certificates. Java
also trusts ACM certificates.

**Certificate authority and
hierarchy**

Public certificates requested through ACM come from [Amazon Trust
Services](https://www.amazontrust.com/repository/ "https://www.amazontrust.com/repository/"), an Amazon-managed public [certificate authority (CA)](acm-concepts.md#concept-ca "acm-concepts.md#concept-ca"). Amazon Root CAs 1 to 4 are
cross-signed by Starfield G2 Root Certificate Authority – G2.
Starfield root is trusted on Android (later Gingerbread versions) and iOS
(version 4.1+). Amazon roots are trusted by iOS 11+. Browsers, applications,
or OSes including Amazon or Starfield roots will trust ACM public
certificates.

ACM issues leaf or end-entity certificates to customers through
intermediate CAs, randomly assigned based on the certificate type (RSA or
ECDSA). ACM doesn't provide intermediate CA information due to this random
selection.

**Domain
Validation (DV)**

ACM certificates are domain validated, identifying only a domain name.
When requesting an ACM certificate, you must prove ownership or control of
all specified domains. You can validate ownership using email or DNS. For
more information, see [AWS Certificate Manager email validation](email-validation.md "email-validation.md") and [AWS Certificate Manager DNS validation](dns-validation.md "dns-validation.md").

**HTTP
validation**

ACM supports HTTP validation for domain ownership verification when
issuing public TLS certificates for use with CloudFront. This method uses HTTP
redirects to prove domain ownership and offers automatic renewal similar to
DNS validation. HTTP validation is currently only available through the CloudFront
Distribution Tenants feature.

**HTTP redirect**

For HTTP validation, ACM provides a `RedirectFrom` URL and a
`RedirectTo` URL. You must set up a redirect from
`RedirectFrom` to `RedirectTo` to demonstrate
domain control. The `RedirectFrom` URL includes the validated
domain, while `RedirectTo` points to an ACM-controlled location
in the CloudFront infrastructure containing a unique validation token.

**Managed by**

Certificates in ACM managed by another service show that service's
identity in the `ManagedBy` field. For certificates using HTTP
validation with CloudFront, this field displays "CLOUDFRONT". These certificates
can only be used through CloudFront. The `ManagedBy` field appears in
the **DescribeCertificate** and
**ListCertificates** APIs, and on the certificates
inventory and details pages in the ACM console.

The `ManagedBy` field is mutually exclusive with the "Can be
used with" attribute. For CloudFront-managed certificates, you can't add new
usages through other AWS services. You can only use these certificates
with more resources through the CloudFront API.

**Intermediate and root CA
rotation**

Amazon may discontinue an intermediate CA without notice to maintain a
resilient certificate infrastructure. These changes don't impact customers.
For more information, see ["Amazon introduces dynamic intermediate certificate
authorities"](https://aws.amazon.com/blogs/security/amazon-introduces-dynamic-intermediate-certificate-authorities/ "https://aws.amazon.com/blogs/security/amazon-introduces-dynamic-intermediate-certificate-authorities/").

If Amazon discontinues a root CA, the change will occur as quickly as
needed. Amazon will use all available methods to notify AWS customers,
including the AWS Health Dashboard, email, and outreach to technical account
managers.

**Firewall access for
revocation**

Revoked end-entity certificates use OCSP and CRLs to verify and publish
revocation information. Some customer firewalls may need additional rules to
allow these mechanisms.

Use these URL wildcard patterns to identify revocation traffic:

- **OCSP**

`http://ocsp.?????.amazontrust.com`

`http://ocsp.*.amazontrust.com`

- **CRL**

`http://crl.?????.amazontrust.com/?????.crl`

`http://crl.*.amazontrust.com/*.crl`

An asterisk (\*) represents one or more alphanumeric characters, a question
mark (?) represents a single alphanumeric character, and a hash mark (#)
represents a numeral.

**Key algorithms**

Certificates must specify an algorithm and key size. ACM supports these
RSA and ECDSA public key algorithms:

- RSA 1024 bit (`RSA_1024`)
- RSA 2048 bit (`RSA_2048`)\*
- RSA 3072 bit (`RSA_3072`)
- RSA 4096 bit (`RSA_4096`)
- ECDSA 256 bit (`EC_prime256v1`)\*
- ECDSA 384 bit (`EC_secp384r1`)\*
- ECDSA 521 bit (`EC_secp521r1`)

ACM can request new certificates using algorithms marked with an
asterisk (\*). Other algorithms are for [imported](import-certificate.md "import-certificate.md") certificates only.

###### Note

For private PKI certificates signed by a AWS Private CA CA, the signing
algorithm family (RSA or ECDSA) must match the CA's secret key algorithm
family.

ECDSA keys are smaller and more computationally efficient than RSA keys of
comparable security, but not all network clients support ECDSA. This table,
adapted from [NIST](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf"), compares RSA and ECDSA key sizes (in bits) for equivalent
security strengths:

| Comparing security for algorithms and keys | Security strength | RSA key size | ECDSA key size |
| ------------------------------------------ | ----------------- | ------------ | -------------- |
| 128                                        | 3072              | 256          |
| 192                                        | 7680              | 384          |
| 256                                        | 15360             | 521          |

Security strength, as a power of 2, relates to the number of guesses
needed to break the encryption. For example, both a 3072-bit RSA key and a
256-bit ECDSA key can be retrieved with no more than
2128 guesses.

For help choosing an algorithm, see the AWS blog post [How to evaluate and use ECDSA certificates in AWS Certificate Manager](https://aws.amazon.com/blogs/security/how-to-evaluate-and-use-ecdsa-certificates-in-aws-certificate-manager/ "https://aws.amazon.com/blogs/security/how-to-evaluate-and-use-ecdsa-certificates-in-aws-certificate-manager/").

###### Important

[Integrated services](acm-services.md "acm-services.md")
allow only supported algorithms and key sizes for their resources.
Support varies based on whether the certificate is imported into IAM
or ACM. For details, see each service's documentation:

- For ELB, see [HTTPS Listeners for Your Application Load
  Balancer](../../../elasticloadbalancing/latest/application/create-https-listener.md "../../../elasticloadbalancing/latest/application/create-https-listener.md").
- For CloudFront, see [Supported SSL/TLS Protocols and Ciphers](../../../AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.md "../../../AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.md").

**Managed Renewal and
Deployment**

ACM manages the renewal and provisioning of ACM certificates.
Automatic renewal helps prevent downtime from misconfigured, revoked, or
expired certificates. For more information, see [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md "managed-renewal.md").

**Multiple
Domain Names**

Each ACM certificate must include at least one fully qualified domain
name (FQDN) and can include additional names. For example, a certificate for
`www.example.com` can also include
`www.example.net`. This applies to bare domains (zone apex or
naked domains) too. You can request a certificate for www.example.com and
include example.com. For more information, see [AWS Certificate Manager public certificates](gs-acm-request-public.md "gs-acm-request-public.md").

**Punycode**

The following [Punycode](https://datatracker.ietf.org/doc/html/rfc3492 "https://datatracker.ietf.org/doc/html/rfc3492") requirements for [Internationalized Domain Names](https://www.icann.org/resources/pages/idn-2012-02-25-en "https://www.icann.org/resources/pages/idn-2012-02-25-en") must be met:

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

**Validity Period**

ACM certificates are valid for 13 months (395 days).

**Wildcard Names**

ACM allows an asterisk (\*) in the domain name to create a wildcard
certificate protecting multiple sites in the same domain. For example,
`*.example.com` protects `www.example.com` and
`images.example.com`.

In a wildcard certificate, the asterisk (`*`) must be leftmost
in the domain name and protects only one subdomain level. For instance,
`*.example.com` protects `login.example.com` and
`test.example.com`, but not
`test.login.example.com`. Also, `*.example.com`
protects _only_ subdomains, not the bare or apex domain
(`example.com`). You can request a certificate for both a
bare domain and its subdomains by specifying multiple domain names, such as
`example.com` and `*.example.com`.

###### Important

If you use CloudFront, note that HTTP validation does not support wildcard
certificates. For wildcard certificates, you must use either DNS
validation or email validation. We recommend DNS validation because it
supports automatic certificate renewal.
