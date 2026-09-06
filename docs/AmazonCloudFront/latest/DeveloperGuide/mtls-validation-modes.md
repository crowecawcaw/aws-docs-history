

# Additional validation modes
<a name="mtls-validation-modes"></a>

Required mode is the default for CloudFront mutual TLS — CloudFront validates every client certificate and denies connections that fail. However, to support additional use cases — such as applications that serve a mix of mTLS-authenticated and unauthenticated clients, or environments where the origin server performs its own mTLS validation — CloudFront supports two additional modes.

**Optional mode** is designed for applications with mixed client populations. For example, a portal that serves public content to unauthenticated browsers while restricting API endpoints to clients presenting valid certificates. Or a migration scenario where you are gradually onboarding clients to mTLS and need to allow both authenticated and unauthenticated connections during the transition.

**Passthrough mode** is designed for customers whose origin servers already perform mTLS validation. For example, services migrating from on-premises reverse proxies, other CDNs, or Application Load Balancers that already handle certificate verification. Passthrough mode allows these customers to place CloudFront in front of their applications without re-implementing validation logic at the edge.

## Optional mode
<a name="optional-mode-details"></a>

### Client certificate validation Optional mode
<a name="optional-mode-overview"></a>

CloudFront offers an alternative Optional client certificate validation mode that validates client certificates that are presented but allows access to clients that don't present certificates.

### Optional mode behavior
<a name="optional-mode-behavior-details"></a>
+ Grants connection to clients with valid certificates (invalid certificates are denied).
+ Allows connection to clients without certificates.
+ Allows mixed client authentication scenarios through a single distribution.

Optional mode is ideal for gradual migration to mTLS authentication, supporting clients with certificates and clients without certificates, or maintaining backward compatibility with legacy clients.

**Note**  
In optional mode, Connection Functions are still invoked even when clients don't present certificates. This allows you to implement custom logic such as logging client IP addresses or applying different policies based on whether certificates are presented.

### To configure optional mode (Console)
<a name="configure-optional-mode-console-new"></a>

1. In your distribution settings, navigate to the **General** tab, choose **Edit**.

1. Scroll to the **Viewer mutual authentication (mTLS)** section within the **Connectivity** container.

1. For **Client certificate validation mode**, select **Optional**.

1. Save changes.

### To configure optional mode (AWS CLI)
<a name="configure-optional-mode-cli-new"></a>

The following example shows how to configure optional mode:

```
"ViewerMtlsConfig": {
    "Mode": "optional",
    ...other settings
}
```

**Customize certificate headers**

Use the mTLS helper functions in viewer-request CloudFront Functions to rename, reformat, or combine the certificate headers before they reach your origin. This is useful when migrating from other services that use different header names or certificate encoding formats.

## Passthrough mode
<a name="passthrough-mode-details"></a>

Passthrough mode allows customers with existing mTLS implementations at their origins to use CloudFront. CloudFront terminates the TLS connection and forwards the client certificate to your origin as HTTP headers. Your origin performs all certificate validation — including chain verification, revocation checking, and custom policy enforcement.

### How passthrough mode works
<a name="passthrough-how-it-works"></a>

1. The client connects to CloudFront and presents a client certificate during the TLS handshake.

1. CloudFront completes the TLS handshake without validating the certificate against a trust store.

1. CloudFront adds the client certificate and certificate chain as HTTP headers on the request.

1. The request is forwarded to your origin. No content is cached.

1. Your origin validates the certificate and processes the request.

Clients can also connect without presenting a certificate. Your origin or Connection Function handles empty certificate scenarios.

**Note**  
In passthrough mode, Connection Functions are still invoked even when clients don't present certificates. This allows you to implement custom logic such as logging client IP addresses or applying different policies based on whether certificates are presented.

### Configuration requirements
<a name="passthrough-configuration-requirements"></a>
+ **No trust store** — The distribution must have zero trust store associations.
+ **Caching disabled** — All cache behaviors must use the managed `CachingDisabled` cache policy.
+ **Origin Shield prohibited** — Origin Shield cannot be enabled.
+ **Lambda@Edge prohibited** — Lambda@Edge function associations are not allowed.
+ **Origin request policy required** — You must allowlist the `Client-Cert` and `Client-Cert-Chain` headers in your origin request policy for the origin to receive them.
+ **Certificate-chain-depth** — CloudFront allows a maximum depth of 4 for client certificate chain to be forwarded to the origins.

### Enable passthrough mode
<a name="enable-passthrough-mode"></a>

#### Console
<a name="enable-passthrough-console"></a>

1. Update all cache behaviors to use the managed `CachingDisabled` cache policy.

1. Open the CloudFront console and choose your distribution.

1. Choose the **General** tab, then choose **Edit** under Settings.

1. Under **Viewer mutual authentication (mTLS)**, select **Passthrough**.

1. Choose **Save changes**.

#### AWS CLI
<a name="enable-passthrough-cli"></a>

Ensure all cache behaviors reference the managed `CachingDisabled` policy, then update the distribution configuration:

```
{
  "ViewerMtlsConfig": {
    "Mode": "passthrough"
  }
}
```

### Headers forwarded to origin
<a name="passthrough-headers-forwarded"></a>

CloudFront adds the following headers to the request sent to your origin:
+ `Client-Cert` — The end-entity (leaf) certificate presented by the client, base64-encoded.
+ `Client-Cert-Chain` — The certificate chain (excluding the leaf), as a structured field list. Each certificate is base64-encoded. `Client-Cert-Chain` is a List type header. It may appear multiple times in a request. Concatenating all values preserves the original chain order. `Client-Cert-Chain` is omitted when the client presents only a single certificate.

CloudFront drops any incoming `Client-Cert` or `Client-Cert-Chain` headers from the client request before adding the actual certificate data. This prevents header spoofing.

**Customize certificate headers**

Use the mTLS helper functions in viewer-request CloudFront Functions to rename, reformat, or combine the certificate headers before they reach your origin. This is useful when migrating from other services that use different header names or certificate encoding formats.