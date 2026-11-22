

# Types of certificates in AWS Certificate Manager

AWS Certificate Manager (ACM) provides three types of certificates: public, private, and imported. ACM can also issue Amazon N2 certificates from the Amazon N2 CA hierarchy, for authentication outside web browsers, including mutual TLS (mTLS).

Public certificates  
ACM issues public certificates from Amazon Trust Services certificate authorities (CAs) in the web public key infrastructure (WebPKI). Major browsers and operating systems include the Amazon Trust Services WebPKI roots in their trust stores.

Private certificates  
ACM issues private certificates from a CA in your own AWS Private CA hierarchy. Browsers and operating systems do not include your private roots in their trust stores.

Imported certificates  
You obtain certificates from a CA outside ACM, such as a third-party CA or your own AWS Private CA CA, and import them into ACM.

Amazon N2 certificates  
ACM issues Amazon N2 certificates from the Amazon N2 CAs, for authentication outside web browsers, such as mutual TLS (mTLS). They chain to the Amazon N2 roots or to the Starfield Services Root Certificate Authority - G2 (SFG2) root certificate. Amazon N2 certificates have the same `Type` as public certificates (`AMAZON_ISSUED`). You request them with the `RootHierarchyType` parameter. For more information, see [Amazon N2 certificates](acm-amazon-n2-certificates.md).

## Choose a certificate type
<a name="certificate-types-choose"></a>


| Certificate | Use it when | Who operates the CA | To get started | 
| --- | --- | --- | --- | 
| Public | Browsers or other clients that you do not control must accept the certificate without configuration. This includes certificates on AWS integrated services, such as Elastic Load Balancing or CloudFront, that serve browser clients. | Amazon | [Request a public certificate](gs-acm-request-public.md), or use [ACME certificate automation](acm-acme.md) | 
| Amazon N2 | You need certificates for authentication outside web browsers, such as mTLS between services or between organizations. They can authenticate a client, a server, or both. ACM validates your domains, and with the Amazon N2 roots a certificate can be valid for up to 395 days. | Amazon | [Request an Amazon N2 certificate](acm-amazon-n2-request.md) | 
| Private | You want to operate your own CA hierarchy and control the certificate profile and validity period, for example for internal traffic or mTLS between your services. | You, in AWS Private CA | [Request a private certificate](gs-acm-request-private.md) | 
| Imported | You already have a certificate from a CA outside AWS and want to use it with ACM integrated services. | The CA that issued it | [Import a certificate](import-certificate.md) | 

## Compare certificate types
<a name="certificate-types-compare"></a>


| Characteristic | Public | Amazon N2 | Private | Imported | 
| --- | --- | --- | --- | --- | 
| What the client or server that verifies the certificate needs in its trust store | Nothing. Major browsers and operating systems include the Amazon Trust Services WebPKI roots. | The Amazon N2 roots or SFG2, depending on the root hierarchy. See [Compare the Amazon N2 certificates root hierarchies](acm-amazon-n2-certificates.md#acm-amazon-n2-hierarchy-comparison). | The root certificate of your private CA | The root certificate of the CA that issued it | 
| Domain validation | DNS, email, or HTTP | DNS only | None | None | 
| Certificate transparency logging | Yes | No | No | Depends on the CA that issued it | 
| Export from ACM | Only if you request the certificate with `Export` set to `ENABLED` | Yes, unless you request the certificate with `Export` set to `DISABLED` | Yes | No. You already hold the private key. | 

## How ACM identifies each certificate
<a name="certificate-types-identify"></a>

`DescribeCertificate` returns `Type` for every certificate, and `RootHierarchyType` and `CertificateUsage` only for Amazon N2 certificates. The following table shows how you get each certificate and the values that ACM returns.


| Certificate | How you get it | `Type` | `RootHierarchyType` | `CertificateUsage` | 
| --- | --- | --- | --- | --- | 
| Public | `RequestCertificate` without `RootHierarchyType` | `AMAZON_ISSUED` | Not returned | Not returned | 
| Amazon N2 | `RequestCertificate` with `RootHierarchyType` set to `N2_AMAZON_MANAGED` or `N2_SFG2_AMAZON_MANAGED` | `AMAZON_ISSUED` | The value that you specified | `CLIENT_AND_SERVER_AUTH` or `CLIENT_AUTH_ONLY` | 
| Private | `RequestCertificate` with `CertificateAuthorityArn` | `PRIVATE` | Not returned | Not returned | 
| Imported | `ImportCertificate` | `IMPORTED` | Not returned | Not returned | 

In a request, `RootHierarchyType` accepts only `N2_AMAZON_MANAGED` and `N2_SFG2_AMAZON_MANAGED`. Any other value fails with a `ValidationException`. To request a public certificate, omit `RootHierarchyType`. To request a private certificate, specify `CertificateAuthorityArn` instead. You cannot specify both `RootHierarchyType` and `CertificateAuthorityArn`.

`CertificateUsage` accepts `CLIENT_AND_SERVER_AUTH` and `CLIENT_AUTH_ONLY`, and only with an Amazon N2 `RootHierarchyType`. For the supported combinations, see [How Amazon N2 certificates work in ACM](acm-amazon-n2-certificates.md#acm-amazon-n2-how-it-works).

By default, `ListCertificates` does not return Amazon N2 certificates. To list them, specify `N2_AMAZON_MANAGED`, `N2_SFG2_AMAZON_MANAGED`, or both in the `RootHierarchyTypes` filter. With the filter, `ListCertificates` returns only certificates from the hierarchies that you specify. For an example command, see [Listing and finding](acm-amazon-n2-characteristics.md#amazon-n2-listing).