# Mutual TLS (origin) with CloudFront

Mutual TLS Authentication (Mutual Transport Layer Security Authentication — mTLS) is a security protocol that extends standard TLS authentication by requiring bidirectional certificate-based authentication, where both client and server must prove their identity before establishing a secure connection.

## Viewer mTLS vs Origin mTLS

Mutual authentication (mTLS) can be enabled between viewers and your CloudFront distribution (viewer mTLS) and/or also between your CloudFront distribution and the origin (origin mTLS). This documentation pertains to origin mTLS configuration. For viewer mTLS configuration refer to: [Mutual TLS authentication with CloudFront (Viewer mTLS)](mtls-authentication.md "mtls-authentication.md").

Mutual TLS (origin) enables CloudFront to authenticate itself to your origin servers using client certificates. With mutual TLS (origin), you can ensure that only your authorized CloudFront distributions can establish connections with your application servers, helping protect against unauthorized access attempts.

###### Note

In mutual TLS (origin) connections, CloudFront acts as the client and presents its client certificate to your origin server during the TLS handshake. CloudFront does not perform validation of the client certificate's validity or revocation status—this is the responsibility of your origin server. Your origin infrastructure must be configured to validate the client certificate against its trust store, check certificate expiration, and perform revocation checks (such as CRL or OCSP validation) according to your security requirements. CloudFront's role is limited to presenting the certificate; all certificate validation logic and security policies are enforced by your origin servers.

## How it works

In a standard TLS handshake between CloudFront and an origin, only the origin server presents a certificate to prove its identity to CloudFront. With mutual TLS (origin), the authentication process becomes bidirectional. When CloudFront attempts to connect to your origin server, CloudFront presents a client certificate during the TLS handshake. Your origin server validates this certificate against its trust store before establishing the secure connection.

## Use cases

Mutual TLS (origin) addresses several critical security scenarios where traditional authentication methods create operational overhead:

- **Hybrid and multi-cloud security** - You can secure connections between CloudFront and origins hosted outside AWS or public origins on AWS. This eliminates the need to manage IP allowlists or custom header solutions, providing consistent certificate-based authentication across AWS, on-premises data centers, and third-party providers. Media companies, retailers, and enterprises operating distributed infrastructure benefit from standardized security controls across their entire infrastructure.
- **B2B API and backend security** - You can protect your backend APIs and microservices from direct access attempts while maintaining CloudFront's performance benefits. SaaS platforms, payment processing systems, and enterprise applications with strict authentication requirements can verify that API requests originate only from authorized CloudFront distributions, preventing man-in-the-middle attacks and unauthorized access attempts.

## Important: Origin Server Requirements

Mutual TLS (origin) requires your origin servers to be configured to support mutual TLS authentication. Your origin infrastructure must be capable of:

- Requesting and validating client certificates during TLS handshakes
- Maintaining a trust store with the Certificate Authority certificates that issued CloudFront's client certificates
- Logging and monitoring mutual TLS connection events
- Managing certificate validation policies and handling authentication failures

CloudFront handles the client-side certificate presentation, but your origin servers are responsible for validating these certificates and managing the mutual TLS connection. Ensure your origin infrastructure is properly configured before enabling mutual TLS (origin) in CloudFront.

## Getting started

To implement mutual TLS (origin) with CloudFront, you'll need to import the client certificate in AWS Certificate Manager, configure your origin server to require mutual TLS, and enable mutual TLS (origin) on your CloudFront distribution. The following sections provide step-by-step instructions for each configuration task.

###### Topics

- [Certificate management with AWS Certificate Manager](origin-certificate-management-certificate-manager.md "origin-certificate-management-certificate-manager.md")
- [Enable mutual TLS(origin) for CloudFront distributions](origin-enable-mtls-distributions.md "origin-enable-mtls-distributions.md")
- [Using CloudFront Functions with mutual TLS (origin)](origin-mtls-cloudfront-functions.md "origin-mtls-cloudfront-functions.md")
