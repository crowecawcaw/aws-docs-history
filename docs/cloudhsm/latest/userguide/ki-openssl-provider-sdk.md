

# Known issues for the OpenSSL Provider for AWS CloudHSM
<a name="ki-openssl-provider-sdk"></a>

These are the known issues for OpenSSL Provider for AWS CloudHSM.

**Topics**
+ [Issue: Errors in OpenSSL CLI when used with OpenSSL Provider](#ki-openssl-provider-1)
+ [Issue: Ed25519 TLS offload not supported on FIPS clusters](#ki-openssl-provider-3)
+ [Issue: ML-DSA operations fail on platforms with OpenSSL earlier than 3.5](#ki-openssl-provider-4)
+ [Issue: ML-DSA TLS handshake fails on Amazon Linux 2023 and RHEL with "no shared signature algorithms"](#ki-openssl-provider-5)
+ [Issue: Forked worker processes fail all TLS handshakes with "Object handle not found" errors](#ki-openssl-provider-6)

## Issue: Errors in OpenSSL CLI when used with OpenSSL Provider
<a name="ki-openssl-provider-1"></a>
+  **Impact: ** The AWS CloudHSM OpenSSL Provider did not support OpenSSL CLI operations (CSR creation, certificate signing). You had to use the OpenSSL Dynamic Engine for CSR and certificate operations. 
+  **Resolution status: **Client SDK 5.18.0 resolves this issue. The OpenSSL Provider now supports OpenSSL CLI operations for all key types (RSA, EC, Ed25519, and ML-DSA). Upgrade to version 5.18.0 or later to benefit from the fix. 

## Issue: Ed25519 TLS offload not supported on FIPS clusters
<a name="ki-openssl-provider-3"></a>
+  **Impact: ** Ed25519 key types are not available on FIPS-mode clusters. Attempts to use this key type for TLS offload on a FIPS cluster fail. 
+  **Resolution: ** Use Ed25519 only on non-FIPS clusters. For FIPS clusters, use RSA or EC key types for TLS offload. 

## Issue: ML-DSA operations fail on platforms with OpenSSL earlier than 3.5
<a name="ki-openssl-provider-4"></a>
+  **Impact: ** ML-DSA key types (ML-DSA-44, ML-DSA-65, ML-DSA-87) require OpenSSL 3.5 or later for CSR creation, certificate creation, and TLS offload. On platforms with an older system OpenSSL, ML-DSA operations fail with an "unsupported algorithm" error. 
+  **Resolution: ** Use a platform with OpenSSL 3.5 or later, or build a custom OpenSSL 3.5\+ binary for ML-DSA operations. 

## Issue: ML-DSA TLS handshake fails on Amazon Linux 2023 and RHEL with "no shared signature algorithms"
<a name="ki-openssl-provider-5"></a>
+  **Impact: ** TLS connections using ML-DSA certificates fail on Amazon Linux 2023, RHEL 9, and RHEL 10 platforms with the error `tls1_set_server_sigalgs:no shared signature algorithms`. This occurs because the system-wide crypto-policies framework does not include ML-DSA signature algorithms (`mldsa44`, `mldsa65`, `mldsa87`) in the default `SignatureAlgorithms` allowlist. Non-TLS operations (key generation, signing, verification) are not affected. Ubuntu 26.04 LTS is not affected because it does not use the crypto-policies framework. 
+  **Resolution: ** Enable the post-quantum (PQ) crypto sub-policy on your platform: 
  + **Amazon Linux 2023** (requires AL2023.12\+): Run `sudo update-crypto-policies --set DEFAULT:PQ`. For more information, see [Post-quantum cryptography policies](https://docs.aws.amazon.com/linux/al2023/ug/crypto-policies-pq.html) in the Amazon Linux 2023 User Guide.
  + **RHEL 9** (requires RHEL 9.8\+): Run `sudo dnf update crypto-policies`, then `sudo update-crypto-policies --set DEFAULT:PQ`. For more information, see [Using system-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/using-the-system-wide-cryptographic-policies_security-hardening) in the RHEL 9 documentation.
  + **RHEL 10** (requires RHEL 10.1\+): ML-DSA is enabled in the `DEFAULT` policy automatically. Run `sudo dnf update` to ensure you have the latest crypto-policies package. For more information, see [Using system-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies) in the RHEL 10 documentation.

## Issue: Forked worker processes fail all TLS handshakes with "Object handle not found" errors
<a name="ki-openssl-provider-6"></a>

 If your application loads the OpenSSL Provider before it forks worker processes, as NGINX and HAProxy do, a worker process can fail all cryptographic operations. You might see errors similar to the following in your client logs: 

```
cloudhsm_rsa_signature_newctx failed: Object manager operation failed: Object handle {{<object handle>}} not found
settable_ctx_params failed: WrongObjectType({{<object handle>}}, "CloudHsmProviderContext", "{{<object type>}}")
```
+  **Impact: ** After the issue occurs, the affected worker process fails every TLS handshake. It also fails every other operation that uses the OpenSSL Provider. The worker continues to fail until you replace it. If your application runs more than one worker process, the other worker processes are not affected, so you see some connections fail and others succeed. If it runs a single worker process, all connections fail. 

   The issue occurs more often after the client loses and restores its connection to an HSM, for example when an HSM restarts or during an HSM replacement. It can also occur without a disconnect, less often. 

   This issue affects OpenSSL Provider versions 5.17.0 through 5.18.0 with all supported key types. 
+  **Workaround: ** Reload the application to replace its worker processes. A reload lets existing connections finish before the old worker processes exit. Run the command for your application: 
  + NGINX: `sudo nginx -s reload`
  + HAProxy: `sudo systemctl reload haproxy`

   If the reload doesn't replace the affected worker, restart the application with `sudo systemctl restart nginx` or `sudo systemctl restart haproxy`. A restart closes open client connections. Reloading or restarting the application restores the affected worker, but the issue can recur. 
+  **Resolution status: **This issue has been resolved in [Client SDK 5.18.1](latest-releases.md#client-version-5-18-1). Upgrade to version 5.18.1 or later to benefit from the fix. 