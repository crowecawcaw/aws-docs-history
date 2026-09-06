

# AWS Certificate Manager public certificate characteristics and limitations
<a name="acm-certificate-characteristics"></a>

Public certificates provided by ACM have the following characteristics and limitations. These apply only to certificates provided by ACM. They might not apply to [imported certificates](import-certificate.md).

**Browser and application trust**  <a name="trust-term"></a>
ACM certificates are trusted by all major browsers including Google Chrome, Microsoft Edge, Mozilla Firefox, and Apple Safari. Browsers display a lock icon when connected by TLS to sites using ACM certificates. Java also trusts ACM certificates.

**Certificate authority and hierarchy**  <a name="authority-term"></a>
Public certificates requested through ACM come from [Amazon Trust Services](https://www.amazontrust.com/repository/), an Amazon-managed public [certificate authority (CA)](https://docs.aws.amazon.com/acm/latest/userguide/acm-concepts.html#concept-ca). Amazon Root CAs 1 to 4 are cross-signed by Starfield G2 Root Certificate Authority – G2. Starfield root is trusted on Android (later Gingerbread versions) and iOS (version 4.1\+). Amazon roots are trusted by iOS 11\+. Browsers, applications, or OSes including Amazon or Starfield roots will trust ACM public certificates.  
ACM issues leaf or end-entity certificates to customers through intermediate CAs, randomly assigned based on the certificate type (RSA or ECDSA). ACM doesn't provide intermediate CA information due to this random selection.

**Domain Validation (DV)**  <a name="domain-validation-term"></a>
ACM certificates are domain validated, identifying only a domain name. When requesting an ACM certificate, you must prove ownership or control of all specified domains. You can validate ownership using email or DNS. For more information, see [AWS Certificate Manager email validation](email-validation.md) and [AWS Certificate Manager DNS validation](dns-validation.md).

**HTTP validation**  <a name="http-validation-term"></a>
ACM supports HTTP validation for domain ownership verification when issuing public TLS certificates for use with CloudFront. This method uses HTTP redirects to prove domain ownership and offers automatic renewal similar to DNS validation. HTTP validation is currently only available through the CloudFront Distribution Tenants feature.

**HTTP redirect**  <a name="http-redirect-term"></a>
For HTTP validation, ACM provides a `RedirectFrom` URL and a `RedirectTo` URL. You must set up a redirect from `RedirectFrom` to `RedirectTo` to demonstrate domain control. The `RedirectFrom` URL includes the validated domain, while `RedirectTo` points to an ACM-controlled location in the CloudFront infrastructure containing a unique validation token.

**Managed by**  <a name="managed-by-term"></a>
Certificates in ACM managed by another service show that service's identity in the `ManagedBy` field. For certificates using HTTP validation with CloudFront, this field displays "CLOUDFRONT". These certificates can only be used through CloudFront. The `ManagedBy` field appears in the **DescribeCertificate** and **ListCertificates** APIs, and on the certificates inventory and details pages in the ACM console.  
The `ManagedBy` field is mutually exclusive with the "Can be used with" attribute. For CloudFront-managed certificates, you can't add new usages through other AWS services. You can only use these certificates with more resources through the CloudFront API.

**Intermediate and root CA rotation**  <a name="rotation-term"></a>
Amazon may discontinue an intermediate CA without notice to maintain a resilient certificate infrastructure. These changes don't impact customers. For more information, see ["Amazon introduces dynamic intermediate certificate authorities"](https://aws.amazon.com/blogs/security/amazon-introduces-dynamic-intermediate-certificate-authorities/).  
If Amazon discontinues a root CA, the change will occur as quickly as needed. Amazon will use all available methods to notify AWS customers, including the Health Dashboard, email, and outreach to technical account managers.

**Firewall access for revocation**  <a name="revocation-term"></a>
Revoked end-entity certificates use OCSP and CRLs to verify and publish revocation information. Some customer firewalls may need additional rules to allow these mechanisms.  
Use these URL wildcard patterns to identify revocation traffic:  
+ **OCSP**

  `http://ocsp.?????.amazontrust.com`

  `http://ocsp.*.amazontrust.com`
+ **CRL**

  `http://crl.?????.amazontrust.com/?????.crl`

  `http://crl.*.amazontrust.com/*.crl`
An asterisk (\*) represents one or more alphanumeric characters, a question mark (?) represents a single alphanumeric character, and a hash mark (\#) represents a numeral.  
For revocation information for ACME certificates, see [Revocation](acm-acme.md#acm-acme-revocation).

**Key algorithms**  <a name="algorithms-term"></a>
Certificates must specify an algorithm and key size. ACM supports these RSA and ECDSA public key algorithms:  
+ RSA 1024 bit (`RSA_1024`)
+ RSA 2048 bit (`RSA_2048`)\*
+ RSA 3072 bit (`RSA_3072`)
+ RSA 4096 bit (`RSA_4096`)
+ ECDSA 256 bit (`EC_prime256v1`)\*
+ ECDSA 384 bit (`EC_secp384r1`)\*
+ ECDSA 521 bit (`EC_secp521r1`)
ACM can request new certificates using algorithms marked with an asterisk (\*). Other algorithms are for [imported](import-certificate.md) certificates only.  
For private PKI certificates signed by a AWS Private CA CA, the signing algorithm family (RSA or ECDSA) must match the CA's secret key algorithm family.
ECDSA keys are smaller and more computationally efficient than RSA keys of comparable security, but not all network clients support ECDSA. This table, adapted from [NIST](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-57pt1r5.pdf), compares RSA and ECDSA key sizes (in bits) for equivalent security strengths:    
**Comparing security for algorithms and keys**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/acm/latest/userguide/acm-certificate-characteristics.html)
Security strength, as a power of 2, relates to the number of guesses needed to break the encryption. For example, both a 3072-bit RSA key and a 256-bit ECDSA key can be retrieved with no more than 2128 guesses.  
For help choosing an algorithm, see the AWS blog post [How to evaluate and use ECDSA certificates in AWS Certificate Manager](https://aws.amazon.com/blogs/security/how-to-evaluate-and-use-ecdsa-certificates-in-aws-certificate-manager/).  
[Integrated services](https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html) allow only supported algorithms and key sizes for their resources. Support varies based on whether the certificate is imported into IAM or ACM. For details, see each service's documentation:  
+ For Elastic Load Balancing, see [HTTPS Listeners for Your Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html).
+ For CloudFront, see [Supported SSL/TLS Protocols and Ciphers](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/secure-connections-supported-viewer-protocols-ciphers.html).

**Managed Renewal and Deployment**  <a name="renewal-term"></a>
ACM manages the renewal and provisioning of ACM certificates. Automatic renewal helps prevent downtime from misconfigured, revoked, or expired certificates. For more information, see [Managed certificate renewal in AWS Certificate Manager](managed-renewal.md).

**Multiple Domain Names**  <a name="multiple-domains-term"></a>
Each ACM certificate must include at least one fully qualified domain name (FQDN) and can include additional names. For example, a certificate for `www.example.com` can also include `www.example.net`. This applies to bare domains (zone apex or naked domains) too. You can request a certificate for www.example.com and include example.com. For more information, see [AWS Certificate Manager public certificates](gs-acm-request-public.md).

**Punycode**  <a name="punycode-term"></a>
The following [Punycode](https://datatracker.ietf.org/doc/html/rfc3492) requirements for [Internationalized Domain Names](https://www.icann.org/resources/pages/idn-2012-02-25-en) must be met:  

1. Domain names beginning with the pattern "<character><character>--" must match "xn--".

1. Domain names beginning with "xn--" must also be valid Internationalized Domain Names.  
**Punycode examples**    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/acm/latest/userguide/acm-certificate-characteristics.html)

**Validity Period**  <a name="validity-term"></a>
ACM certificates are valid for 198 days.

**Wildcard Names**  <a name="wildcard-term"></a>
ACM allows an asterisk (\*) in the domain name to create a wildcard certificate protecting multiple sites in the same domain. For example, `*.example.com` protects `www.example.com` and `images.example.com`.  
In a wildcard certificate, the asterisk (`*`) must be leftmost in the domain name and protects only one subdomain level. For instance, `*.example.com` protects `login.example.com` and `test.example.com`, but not `test.login.example.com`. Also, `*.example.com` protects *only* subdomains, not the bare or apex domain (`example.com`). You can request a certificate for both a bare domain and its subdomains by specifying multiple domain names, such as `example.com` and `*.example.com`.  
If you use CloudFront, note that HTTP validation does not support wildcard certificates. For wildcard certificates, you must use either DNS validation or email validation. We recommend DNS validation because it supports automatic certificate renewal.