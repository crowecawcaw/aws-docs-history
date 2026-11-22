

# Authenticate clients using mutual TLS for Network Load Balancers

Mutual TLS authentication is a variation of transport layer security (TLS). Traditional TLS establishes secure communications between a server and client, where the server needs to provide its identity to its clients. With mutual TLS, a load balancer negotiates mutual authentication between the client and the server while negotiating TLS. When you use mutual TLS with your Network Load Balancer, you simplify authentication management and reduce the load on your applications.

By using mutual TLS, your load balancer can manage client authentication to help ensure that only trusted clients communicate with your backend applications. When you use this feature, the load balancer authenticates clients using certificates from a third-party certificate authority (CA), or by using AWS Private Certificate Authority (AWS Private CA), optionally, with revocation checks.

Network Load Balancers support mutual TLS in verify mode only. In verify mode, the load balancer performs X.509v3 client certificate authentication for clients when it negotiates TLS connections.

The load balancer admits a connection in the following order. First, it verifies that the client certificate chains to a certificate authority (CA) in the trust store. Next, it evaluates any client certificate identity filters that you configure, and admits only connections whose certificate matches at least one filter. Finally, it applies any revocation checks that you configure.

## Before you begin configuring mutual TLS on your Network Load Balancer
<a name="mtls-before-you-begin"></a>

Before you configure mutual TLS on your Network Load Balancer, be aware of the following.

**Quotas**  
Quotas apply to the resources that mTLS uses, such as trust stores, CA certificates, and certificate revocation lists. For more information, see [Quotas for your Network Load Balancers](load-balancer-limits.md).

**Requirements for certificates**  
Network Load Balancers support the following for the client certificates used with mutual TLS authentication:  
+ Supported certificate: X.509v3
+ Supported public keys: RSA 2K–8K, or ECDSA secp256r1, secp384r1, and secp521r1
+ Supported signature algorithms: SHA256, SHA384, and SHA512 with RSA; SHA256, SHA384, and SHA512 with ECDSA; and SHA256, SHA384, and SHA512 hash with RSASSA-PSS (MGF1)

**Key usage**  
By default, Network Load Balancers enforce the Extended Key Usage (EKU) and Key Usage (KU) extensions on the leaf client certificate during the TLS handshake:  
+ If the certificate includes an EKU extension, it must contain `clientAuth` (OID 1.3.6.1.5.5.7.3.2).
+ If the certificate includes a KU extension, it must assert `digitalSignature` or `keyAgreement`.
If a certificate omits one of these extensions, that check does not apply and the certificate is accepted. This follows RFC 5280, which treats an absent extension as placing no restriction on how the key may be used.

**Client certificate limits**  
The following limits apply to client certificates:  
+ Maximum client certificate chain depth: 4
+ Maximum client certificate chain size: 16 KB
+ Maximum leaf certificate subject distinguished name (DN): 1,024 bytes

**CA certificate bundles**  
+ Network Load Balancers upload each certificate authority (CA) certificate bundle as a batch. You cannot upload individual certificates. To add new certificates, upload the certificate bundle file.
+ To replace a CA certificate bundle, use the `ModifyTrustStore` API operation. For more information, see [Replace a CA certificate bundle](configure-mutual-authentication.md#replace-ca-bundle-mtls).

**Session resumption**  
Session resumption is not supported while using mutual TLS verify mode with a Network Load Balancer.

**CA certificate files**  
CA certificate files must meet the following requirements:  
+ The certificate file must use PEM (Privacy Enhanced Mail) format.
+ Certificate contents must be enclosed within the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` boundaries.
+ Comments must be preceded by a `#` character and must not contain any `-` characters.
+ There cannot be any blank lines.
The following example shows a certificate that is not accepted (invalid):  

```
# comments

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 01
-----BEGIN CERTIFICATE-----
Base64-encoded certificate
-----END CERTIFICATE-----
```
The following examples show certificates that are accepted (valid).  
Single certificate (PEM-encoded):  

```
# comments
-----BEGIN CERTIFICATE-----
Base64-encoded certificate
-----END CERTIFICATE-----
```
Multiple certificates (PEM-encoded):  

```
# comments
-----BEGIN CERTIFICATE-----
Base64-encoded certificate
-----END CERTIFICATE-----
# comments
-----BEGIN CERTIFICATE-----
Base64-encoded certificate
-----END CERTIFICATE-----
```

**Listener settings**  
You configure all mTLS settings in the `MutualAuthenticationAttributes` structure on the listener. For more information, see [Configure mutual TLS](configure-mutual-authentication.md).

**Access logs**  
The load balancer records client certificate details (subject, validity, serial number, and verification status) in access logs. For more information, see [Access log entries](load-balancer-access-logs.md#access-log-entry-format).