# Mutual authentication with TLS in Application Load Balancer

Mutual TLS authentication is a variation of transport layer security (TLS). Traditional TLS
establishes secure communications between a server and client, where the server needs to
provide its identity to its clients. With mutual TLS, a load balancer negotiates mutual
authentication between the client and the server while negotiating TLS. When you use
mutual TLS with your Application Load Balancer, you simplify authentication management and reduce the load
on your applications.

By using mutual TLS, your load balancer can manage client authentication to help ensure that
only trusted clients communicate with your backend applications. When you use this
feature, the load balancer authenticates clients using certificates from third-party
certificate authority (CA) or by using the AWS Private Certificate Authority (PCA), optionally, with revocation
checks. The load balancer passes the client certificate information to the backend using
HTTP headers, which your applications can use for authorization.

Mutual TLS for Application Load Balancers provides the following options for validating your X.509v3 client
certificates:

- **Mutual TLS passthrough:** The load balancer sends the entire client
  certificate chain to the target, without verifying it. Targets should verify the
  client certificate chain. Then, using the client certificate chain, you can
  implement the load balancer authentication and target authorization logic in
  your application.
- **Mutual TLS verify:** The load balancer performs X.509 client certificate
  authentication for clients when a load balancer negotiates TLS
  connections.
  To use mutual TLS passthrough, you must configure the listener to accept the certificates
  from clients. To use mutual TLS with verification, see [Configuring mutual TLS on an Application Load Balancer](configuring-mtls-with-elb.md "configuring-mtls-with-elb.md").

## Before you begin configuring mutual TLS on your Application Load Balancer

Before you begin configuring mutual TLS on your Application Load Balancer, be aware of the following:

**Quotas**
Application Load Balancers include certain limits related to the amount of trust stores, CA certificates, and certificate revocation lists in use within your AWS account.

For more information, see [Quotas for your Application Load Balancers](load-balancer-limits.md "load-balancer-limits.md").

**Requirements for certificates**
Application Load Balancers support the following for certificates used with mutual TLS authentication:

- Supported certificate: X.509v3
- Supported public keys: RSA 2K – 8K or ECDSA secp256r1, secp384r1, secp521r1
- Supported signature algorithms: SHA256, 384, 512 with RSA/SHA256, 384, 512 with EC/SHA256,384,512 hash
  with RSASSA-PSS with MGF1

**CA certificate bundles**
The following applies to certificate authority (CA) bundles:

- Application Load Balancers upload each certificate authority (CA) certificate bundle as a batch. Application Load Balancers don't support uploading
  individual certificates. If you need to add new certificates, you must upload the certificates bundle file.
- To replace a CA certificate bundle, use the [ModifyTrustStore](../APIReference/API_ModifyTrustStore.md "../APIReference/API_ModifyTrustStore.md") API.

**Certificate order for passthrough**
When you use mutual TLS passthrough, the Application Load Balancer inserts headers
to present the clients certificate chain to the backend targets. The order of
presentation starts with the leaf certificates and finishes with the root
certificate.

**Session resumption**
Session resumption is not supported while using mutual TLS
passthrough or verify modes with an Application Load Balancer.

**HTTP headers**
Application Load Balancers use `X-Amzn-Mtls` headers to send certificate information when it negotiates client connections
using mutual TLS. For more information and example headers, see [HTTP headers and mutual TLS](#mtls-http-headers "#mtls-http-headers").

**CA certificate files**
CA certificate files must satisfy the following requirements:

- Certificate file must use PEM (Privacy Enhanced Mail) format.
- Certificate contents must be enclosed within the `-----BEGIN CERTIFICATE-----` and `-----END CERTIFICATE-----` boundaries.
- Comments must be preceded by a `#` character and must not contain any `-` characters.
- There cannot be any blank lines.

Example certificate that is not accepted (invalid):

```
# comments

Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 01
    Signature Algorithm: ecdsa-with-SHA384
        Issuer: C=US, O=EXAMPLE, OU=EXAMPLE, CN=EXAMPLE
        Validity
            Not Before: Jan 11 23:57:57 2024 GMT
            Not After : Jan 10 00:57:57 2029 GMT
        Subject: C=US, O=EXAMPLE, OU=EXAMPLE, CN=EXAMPLE
        Subject Public Key Info:
            Public Key Algorithm: id-ecPublicKey
                Public-Key: (384 bit)
                pub:
                    00:01:02:03:04:05:06:07:08
                ASN1 OID: secp384r1
                NIST CURVE: P-384
        X509v3 extensions:
            X509v3 Key Usage: critical
                Digital Signature, Key Encipherment, Certificate Sign, CRL Sign
            X509v3 Basic Constraints: critical
                CA:TRUE
            X509v3 Subject Key Identifier:
                00:01:02:03:04:05:06:07:08
            X509v3 Subject Alternative Name:
                URI:EXAMPLE.COM
    Signature Algorithm: ecdsa-with-SHA384
         00:01:02:03:04:05:06:07:08
-----BEGIN CERTIFICATE-----
Base64–encoded certificate
-----END CERTIFICATE-----
```

Example certificates that are accepted (valid):

1. Single certificate (PEM–encoded):

```
# comments
-----BEGIN CERTIFICATE-----
Base64–encoded certificate
-----END CERTIFICATE-----
```

2. Multiple certificates (PEM–encoded):

```
# comments
-----BEGIN CERTIFICATE-----
Base64–encoded certificate
-----END CERTIFICATE-----
# comments
-----BEGIN CERTIFICATE-----
Base64–encoded certificate
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
Base64–encoded certificate
-----END CERTIFICATE-----
```

## HTTP headers and mutual TLS

This section describes the HTTP headers that Application Load Balancers use to send certificate information when negotiating connections
with clients using mutual TLS. The specific `X-Amzn-Mtls` headers that the Application Load Balancer uses depends on the mutual TLS mode that you've
specified: passthrough mode or verify mode.

For information about other HTTP headers supported by Application Load Balancers, see [HTTP headers and Application Load Balancers](x-forwarded-headers.md "x-forwarded-headers.md").

### HTTP header for passthrough mode

For mutual TLS in passthrough mode, Application Load Balancers use the following header.

This header contains the URL-encoded PEM format
of the entire client certificate chain presented in the connection, with `+=/` as safe characters.

**Example header contents:**

```
X-Amzn-Mtls-Clientcert: -----BEGIN%20CERTIFICATE-----%0AMIID<...reduced...>do0g%3D%3D%0A-----END%20CERTIFICATE-----%0A-----BEGIN%20CERTIFICATE-----%0AMIID1<...reduced...>3eZlyKA%3D%3D%0A-----END%20CERTIFICATE-----%0A
```

### HTTP headers for verify mode

For mutual TLS in verify mode, Application Load Balancers use the following headers.

This header contains a hexadecimal representation of the leaf certificate serial number.

**Example header contents:**

```
X-Amzn-Mtls-Clientcert-Serial-Number: 03A5B1
```

This header contains an RFC2253 string representation of the issuer's distinguished name (DN).

**Example header contents:**

```
X-Amzn-Mtls-Clientcert-Issuer: CN=rootcamtls.com,OU=rootCA,O=mTLS,L=Seattle,ST=Washington,C=US
```

This header contains an RFC2253 string representation of the subject's distinguished name (DN).

**Example header contents:**

```
X-Amzn-Mtls-Clientcert-Subject: CN=client_.com,OU=client-3,O=mTLS,ST=Washington,C=US
```

This header contains an ISO8601 format of the `notBefore` and `notAfter` date.

**Example header contents:**

```
X-Amzn-Mtls-Clientcert-Validity: NotBefore=2023-09-21T01:50:17Z;NotAfter=2024-09-20T01:50:17Z
```

This header contains a URL-encoded PEM format of the leaf certificate, with `+=/` as safe characters.

**Example header contents:**

```
X-Amzn-Mtls-Clientcert-Leaf: -----BEGIN%20CERTIFICATE-----%0AMIIG<...reduced...>NmrUlw%0A-----END%20CERTIFICATE-----%0A
```

## Advertise Certificate Authority (CA) subject name

Advertising Certificate Authority (CA) subject names enhances the authentication
process by helping clients determine which certificates will be accepted during mutual
TLS authentication.

When you enable Advertise CA subject names, the Application Load Balancer will advertise the list
of Certificate Authorities (CAs) subject names that it trusts, based on the
trust store it's associated with. When a client connects to a target through
the Application Load Balancer, the client receives the list of trusted CA subject names.

During the TLS handshake, when the Application Load Balancer requests a client certificate it includes a
list of trusted CA Distinguished Names (DNs) in its Certificate Request message.
This helps clients select valid certificates that match the advertised CA subject
names, streamlining the authentication process and reducing connection errors.

You can enable Advertise CA subject name on new and existing listeners. For
more information, see [Add an HTTPS listener](create-https-listener.md#add-https-listener "create-https-listener.md#add-https-listener").

## Connection logs for Application Load Balancers

ELB provides connection logs that capture attributes about the requests
sent to your Application Load Balancers. Connection logs contain information such as the
client IP address and port, client certificate information, connection results,
and TLS ciphers being used. These connection logs can then be used to review
request patterns, and other trends.

To learn more about connection logs, see [Connection logs for your Application Load Balancer](load-balancer-connection-logs.md "load-balancer-connection-logs.md")
