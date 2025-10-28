# CDN integration security best practices for

MediaTailor

This section explains how to implement security best practices for your AWS Elemental MediaTailor content
delivery network (CDN) integration. Proper security configuration helps protect your content
and infrastructure from unauthorized access and potential threats.

Securing your CDN integration is crucial for protecting your content, preventing
unauthorized access, and ensuring compliance with security requirements. Implementing these
best practices helps create a robust security posture for your streaming workflow.

## CDN security configuration

Before configuring your CDN routing and cache settings, implement these security best
practices to protect your content and infrastructure:

### Transport security

MediaTailor only uses HTTPS for all communication and does not allow HTTP connections.
To ensure secure communication between all components in your streaming workflow,
complete the following steps:

1. Configure HTTPS for all communication between your CDN and MediaTailor
   endpoints. MediaTailor requires HTTPS and will not accept HTTP connections.
2. Use TLS 1.2 or later for all HTTPS connections.
3. Configure your CDN to enforce HTTPS-only connections from viewers.

### Access control

To protect your content and infrastructure from unauthorized access, implement the following access controls:

1. Configure geo-restriction settings if you need to limit content access to
   specific regions.
2. Implement signed URLs or signed cookies for content that requires viewer
   authentication.
3. Set up IP-based allowlists for administrative access to CDN
   configuration.

### Security monitoring

To detect and respond to security events effectively, implement the following monitoring practices:

1. Enable access logging for your CDN distribution.
2. Set up alerts for unusual traffic patterns or access attempts.
3. Regularly review security configurations and update as needed.

## Advanced security features

The following advanced security features provide enhanced protection for your CDN integration:

**Web Application Firewall (WAF)**

If your CDN supports WAF functionality, configure it to protect against
common web vulnerabilities and attacks.

**DDoS protection**

Enable DDoS protection features provided by your CDN to mitigate
distributed denial-of-service attacks.

**Origin access control**

Configure your origin servers to accept requests only from your CDN to
prevent direct access attempts.

**Content encryption**

For highly sensitive content, consider implementing additional encryption
mechanisms beyond transport security.

## Next steps

After implementing security best practices, the next step is to test and troubleshoot
your CDN integration. See [Troubleshoot CDN integration](cdn-troubleshooting.md "cdn-troubleshooting.md") for comprehensive testing and troubleshooting instructions.
