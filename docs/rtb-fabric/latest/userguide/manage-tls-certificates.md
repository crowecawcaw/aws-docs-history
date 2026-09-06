

# Manage TLS certificates
<a name="manage-tls-certificates"></a>

If you use HTTPS for your custom domain, you must configure TLS certificates that match the hostnames clients use to connect. RTB Fabric uses Server Name Indication (SNI) to select the correct certificate during the TLS handshake. This section describes certificate configuration, the resolution process, and operational considerations. If you use HTTP only, you can skip this section. For general information about encryption in transit, see Data protection in RTB Fabric.

## Certificate requirements
<a name="certificate-requirements"></a>

Certificates used for inbound external links with custom domains must meet the following requirements:
+ **Common name (CN) or SANs must cover your custom domains.** RTB Fabric uses the CN and SANs from your ACM certificate for SNI-based hostname matching. Ensure the certificate covers all hostnames that partners use to reach your custom domain.
+ **Same region as the gateway.** The ACM certificate must be in the same AWS Region as the responder gateway.
+ **Associated via the AssociateCertificate API.** Use the AssociateCertificate API to associate the certificate with the gateway. This ensures RTB Fabric treats the certificate as a customer certificate. See [Customer vs. service certificates](#customer-vs-service-certificates).

**Important**  
Ensure all custom domain certificates are associated using the AssociateCertificate API. See [Customer vs. service certificates](#customer-vs-service-certificates) for how customer and service certificates are isolated.

## ACM integration
<a name="acm-integration"></a>

RTB Fabric loads certificate material through AWS Certificate Manager (ACM). When you associate a certificate using the AssociateCertificate API, RTB Fabric retrieves the certificate chain, encrypted private key, CN, and SANs from ACM. You provide only the `acmCertificateArn` — RTB Fabric handles the rest.

RTB Fabric decrypts the certificate's private key within the VPC boundary. At no point does the unencrypted private key leave the VPC.

## How certificate resolution works (SNI)
<a name="certificate-resolution-sni"></a>

When a client initiates a TLS connection, it sends a Server Name Indication (SNI) hostname in the ClientHello message. RTB Fabric uses this hostname to select the appropriate certificate through a two-tier resolution process.

**Resolution order:**

1. **Exact hostname lookup** — RTB Fabric checks the exact hostname index for a certificate whose CN or SANs match the SNI hostname exactly. Ensure the CN and SANs on your ACM certificate use lowercase characters, because certificate resolution uses case-sensitive lookup.

1. **Wildcard pattern matching** — If no exact match is found, RTB Fabric iterates through the wildcard hostname entries. Wildcard matching uses suffix-based matching, which can match across multiple DNS labels.

1. **Service certificate fallback** — If no customer certificate matches, RTB Fabric falls back to service certificates using the following preference order: 
   + ECDSA certificate, if the client's ClientHello indicates support for ECDSA.
   + RSA certificate, if ECDSA is not supported.
   + ECDSA certificate as a last resort, if no RSA certificate is available.

## Customer vs. service certificates
<a name="customer-vs-service-certificates"></a>

RTB Fabric enforces a hard isolation boundary between customer certificates and service certificates.

**Customer certificates** (associated via the AssociateCertificate API):
+ Served only when the client's SNI hostname matches the certificate's CN or SANs.
+ Never served as a fallback for non-customer traffic.
+ Use customer certificates for all HTTPS inbound external links with custom domains configurations.

**Service certificates** (managed by RTB Fabric):
+ Served as a fallback when no customer certificate matches the client's SNI hostname.
+ Cover the default RTB Fabric gateway hostnames (for example, `*.rtbfabric.us-east-1.amazonaws.com`).

This isolation ensures that your custom domain certificate is never inadvertently presented to clients connecting via a different hostname, and that service certificates are never presented to clients connecting via your custom domain (assuming your certificate is correctly configured).

**Warning**  
If the CN and SANs on your ACM certificate do not match the SNI hostname clients send, the customer certificate lookup fails and RTB Fabric falls back to a service certificate. Clients then see a certificate domain mismatch error. Double-check that your ACM certificate's CN and SANs cover all DNS hostnames used by your custom domain.

## Certificate rotation
<a name="certificate-rotation-renewal"></a>

**Note**  
Rotation of ACM-managed certificates will be handled automatically by RTB Fabric with no action required from you.

**Best practices for rotation:**
+ **Monitor certificate expiry.** Ensure your ACM certificates are renewed before they expire. An expired certificate causes TLS handshake failures, which prevent RTB Fabric from serving the certificate. Set up Amazon CloudWatch alarms or EventBridge rules on ACM certificate expiration events and plan to rotate certificates at least 30 days before expiry. If you need to rotate certificates, disassociate the old certificate before associating the new one, or use ACM in-place renewal.
**Note**  
Rotation of ACM-managed certificates will be handled automatically by RTB Fabric with no action required from you.
+ **Test before cutover.** After updating the configuration, verify the new certificate by sending a test request and inspecting the TLS handshake (for example, using `openssl s_client -servername bid.example.com -connect bid.example.com:443`).
+ **Maintain key type consistency.** If your original certificate uses ECDSA, continue using ECDSA for the renewed certificate.