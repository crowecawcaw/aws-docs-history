

# Amazon N2 certificates

Amazon N2 certificates are AWS Certificate Manager (ACM) certificates from the Amazon N2 certificate authorities (CAs), an Amazon-operated CA hierarchy. Use them for authentication outside web browsers, such as mutual TLS (mTLS). Choose them when WebPKI certificates do not fit, for example because you need a validity period longer than WebPKI allows (up to 395 days with the Amazon N2 roots), and private certificates do not fit either, for example because the clients or servers that verify your certificates are in another organization. In mTLS, the client and the server each present a certificate and verify the other's. This guide calls the client or server that verifies a certificate the verifying peer. Use Amazon N2 certificates between services in a mesh, between an application and an API endpoint, between an on-premises client and a service that you operate, or between your service and a partner's client.

An Amazon N2 certificate chains to the root hierarchy of your choice. Choose the Amazon N2 roots when you can add them to the trust store of each verifying peer. Choose the Starfield Services Root Certificate Authority - G2 (SFG2) when the verifying peers already include it in their trust stores, as many existing clients and devices do. For the root programs that include SFG2, see the [repository](https://www.amazontrust.com/repository/) on the Amazon Trust Services website. To compare the root hierarchies, see [Compare the Amazon N2 certificates root hierarchies](#acm-amazon-n2-hierarchy-comparison).

Do not use Amazon N2 certificates for browser clients. ACM does not record Amazon N2 certificates in certificate transparency (CT) logs, so browsers that require CT reject them.

**Topics**
+ [How Amazon N2 certificates work in ACM](#acm-amazon-n2-how-it-works)
+ [Amazon N2 roots and trust](#acm-amazon-n2-trust)
+ [Compare the Amazon N2 certificates root hierarchies](#acm-amazon-n2-hierarchy-comparison)
+ [When to use Amazon N2 certificates](#acm-amazon-n2-when-to-use)
+ [Amazon N2 certificate characteristics](acm-amazon-n2-characteristics.md)
+ [Request an Amazon N2 certificate](acm-amazon-n2-request.md)

## How Amazon N2 certificates work in ACM
<a name="acm-amazon-n2-how-it-works"></a>

You request an Amazon N2 certificate with the `RequestCertificate` action. Two optional parameters determine which certificate ACM issues: `RootHierarchyType` and `CertificateUsage`.

`RootHierarchyType`  
The root hierarchy that ACM issues the certificate from. To request an Amazon N2 certificate, specify one of these values:  
+ `N2_AMAZON_MANAGED`: chains to the Amazon N2 roots.
+ `N2_SFG2_AMAZON_MANAGED`: chains to the Starfield Services Root Certificate Authority - G2 (SFG2).
If you omit this parameter, ACM issues an ACM public certificate. Any other value fails with a `ValidationException`. You cannot specify `RootHierarchyType` together with `CertificateAuthorityArn`.  
This parameter selects a type of hierarchy, not a specific root or intermediate CA. ACM chooses the CA within the hierarchy, and that choice can change over time without any change to your request.

`CertificateUsage`  
The extended key usage (EKU) profile of the certificate: whether it can authenticate both a client and a server, or only a client. Specify this parameter only with an Amazon N2 `RootHierarchyType`. If you omit it, ACM issues the certificate with `CLIENT_AND_SERVER_AUTH`.

A request fails with a `ValidationException` if you specify `CertificateUsage` without an Amazon N2 `RootHierarchyType`, or if the combination is not supported. The following table lists the supported combinations.


| `RootHierarchyType` | `CertificateUsage` | Certificate can authenticate | 
| --- | --- | --- | 
| `N2_AMAZON_MANAGED` | `CLIENT_AND_SERVER_AUTH` (default when omitted) | A client and a server | 
| `N2_AMAZON_MANAGED` | `CLIENT_AUTH_ONLY` | A client only | 
| `N2_SFG2_AMAZON_MANAGED` | `CLIENT_AND_SERVER_AUTH` (default when omitted) | A client and a server | 

`N2_SFG2_AMAZON_MANAGED` does not support `CLIENT_AUTH_ONLY`, because certificates that chain to SFG2 always include server authentication.

`DescribeCertificate` returns `RootHierarchyType` and `CertificateUsage` for Amazon N2 certificates. The `Type` of an Amazon N2 certificate is `AMAZON_ISSUED`, the same as other ACM-issued certificates.

For the `RootHierarchyType` and `CertificateUsage` values that ACM reports for every certificate type, see [Types of certificates in AWS Certificate Manager](certificate-types.md).

## Amazon N2 roots and trust
<a name="acm-amazon-n2-trust"></a>

A peer validates an Amazon N2 certificate only if its trust store includes the root that the certificate chains to. Each verifying peer needs the following:
+ `N2_AMAZON_MANAGED`: all of the Amazon N2 roots. Browsers and operating systems do not include them by default, so add them to the trust store of each verifying peer. Add all of them, not only the root that matches your key algorithm, because ACM chooses the CA within the hierarchy and that choice can change over time.
+ `N2_SFG2_AMAZON_MANAGED`: the Starfield Services Root Certificate Authority - G2 (SFG2) root certificate. The peer must also not require certificate transparency.

The certificate chain that ACM returns with an Amazon N2 certificate depends on the root hierarchy:
+ `N2_AMAZON_MANAGED`: the intermediate CA that issued the certificate. The chain does not include the Amazon N2 roots, so each verifying peer must already have them in its trust store.
+ `N2_SFG2_AMAZON_MANAGED`: the intermediate CA that issued the certificate, and an Amazon SFG2 N2 root, which SFG2 cross-signs. That root chains to SFG2 in the verifying peer's trust store.

To download the Amazon N2 roots and the Amazon SFG2 N2 roots in PEM or DER format, see the [repository](https://www.amazontrust.com/repository/) on the Amazon Trust Services website. The repository also lists test sites that serve valid, revoked, and expired certificates for each root that has them.

The two root hierarchies are governed by different Certificate Policy and Certification Practice Statement (CP/CPS) documents. For the CP/CPS that applies to each root, see the [repository](https://www.amazontrust.com/repository/) on the Amazon Trust Services website.

**Note**  
The Amazon N2 roots are separate from the Amazon Trust Services WebPKI roots that ACM public certificates chain to. For those roots, see [AWS Certificate Manager public certificate characteristics and limitations](acm-certificate-characteristics.md).

## Compare the Amazon N2 certificates root hierarchies
<a name="acm-amazon-n2-hierarchy-comparison"></a>

The following table compares the two root hierarchies for Amazon N2 certificates. To compare Amazon N2 certificates with public, private, and imported certificates, see [Compare certificate types](certificate-types.md#certificate-types-compare).


| Characteristic | Amazon N2 roots (`N2_AMAZON_MANAGED`) | SFG2 (`N2_SFG2_AMAZON_MANAGED`) | 
| --- | --- | --- | 
| Choose it when | You can add the Amazon N2 roots to the trust store of each verifying peer, or you need a validity period longer than 98 days | The verifying peers already include SFG2 in their trust stores | 
| Chains to | The Amazon N2 roots, with no cross-signing | The Starfield Services Root Certificate Authority - G2 (SFG2) root certificate, through an Amazon SFG2 N2 root, which SFG2 cross-signs | 
| What each verifying peer needs | The Amazon N2 roots in its trust store | SFG2 in its trust store, and no certificate transparency requirement | 
| `CertificateUsage` values | `CLIENT_AND_SERVER_AUTH` (default) or `CLIENT_AUTH_ONLY` | `CLIENT_AND_SERVER_AUTH` only | 
| Maximum validity | 395 days | 98 days | 
| Chain that ACM returns | The issuing intermediate CA | The issuing intermediate CA and the cross-signed Amazon SFG2 N2 root | 

For domain validation, key algorithms, export, certificate transparency logging, listing, integrated services, quotas, and renewal, see [Amazon N2 certificate characteristics](acm-amazon-n2-characteristics.md).

## When to use Amazon N2 certificates
<a name="acm-amazon-n2-when-to-use"></a>

**Use an Amazon N2 certificate when:**
+ A certificate must authenticate a client, for example in mTLS. A certificate with `CLIENT_AND_SERVER_AUTH` also includes server authentication, so the same certificate can authenticate a server.
+ You want Amazon to operate the CAs, including for connections between your services and a partner's.

To choose a root hierarchy, see [Compare the Amazon N2 certificates root hierarchies](#acm-amazon-n2-hierarchy-comparison). To compare Amazon N2 certificates with public, private, and imported certificates, see [Types of certificates in AWS Certificate Manager](certificate-types.md).