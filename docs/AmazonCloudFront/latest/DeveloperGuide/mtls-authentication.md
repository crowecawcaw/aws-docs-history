

# Mutual TLS authentication with CloudFront (Viewer mTLS)
<a name="mtls-authentication"></a>

Mutual TLS Authentication (Mutual Transport Layer Security Authentication — mTLS) is a security protocol that extends standard TLS authentication by requiring bidirectional certificate-based authentication, where both client and server must prove their identity before establishing a secure connection. Using mutual TLS, you can ensure that only clients presenting trusted TLS certificates gain access to your CloudFront distributions.

## How it works
<a name="how-mtls-works"></a>

In a standard TLS handshake, only the server presents a certificate to prove its identity to the client. With mutual TLS, the authentication process becomes bidirectional. When a client attempts to connect to your CloudFront distribution, CloudFront requests a client certificate during the TLS handshake. The client must present a valid X.509 certificate that CloudFront validates against your configured trust store before establishing the secure connection.

CloudFront performs this certificate validation at AWS edge locations, offloading the authentication complexity from your origin servers while maintaining CloudFront's global performance benefits. You can configure mTLS in three modes:
+ **Required mode** (default) — CloudFront validates the client certificate against a trust store. If validation fails or no certificate is presented, CloudFront denies the connection. Use required mode when every client must authenticate with a valid certificate.
+ **Optional mode** — CloudFront validates the client certificate if one is presented, but allows connections without a certificate. Certificate metadata is available in Connection Functions and HTTP headers for your origin to make authorization decisions. Use optional mode when you support both authenticated and unauthenticated clients.
+ **Passthrough mode** — CloudFront does not validate the client certificate against a trust store. CloudFront only validates that the client possesses the corresponding private key. It forwards the certificate to your origin as HTTP headers for your origin to perform validation. No trust store is required and no caching occurs. Use passthrough mode when you have existing mTLS implementations at your origin.

## Use cases
<a name="mtls-use-cases"></a>

Mutual TLS authentication with CloudFront addresses several critical security scenarios where traditional authentication methods are insufficient:
+ **Device authentication with content caching** - You can authenticate gaming consoles, IoT devices, or corporate hardware before allowing access to firmware updates, game downloads, or internal resources. Each device contains a unique certificate that proves its authenticity while benefiting from CloudFront's caching capabilities.
+ **API-to-API authentication** - You can secure machine-to-machine communication between trusted business partners, payment systems, or micro-services. Certificate-based authentication eliminates the need for shared secrets or API keys while providing strong identity verification for automated data exchanges.

**Topics**
+ [How it works](#how-mtls-works)
+ [Use cases](#mtls-use-cases)
+ [Trust stores and certificate management](trust-stores-certificate-management.md)
+ [Enable mutual TLS for CloudFront distributions](enable-mtls-distributions.md)
+ [Associate a CloudFront Connection Function](connection-functions.md)
+ [Configuring additional settings](configuring-additional-settings.md)
+ [Viewer mTLS headers for cache policies and forwarded to origin](viewer-mtls-headers.md)
+ [Certificate revocation](certificate-revocation.md)
+ [Helper methods for mutual TLS](mtls-helper-methods-link.md)
+ [Additional validation modes](mtls-validation-modes.md)
+ [Observability using connection logs](connection-logs.md)