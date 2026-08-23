# Known issues for the OpenSSL Provider for AWS CloudHSM

These are the known issues for OpenSSL Provider for AWS CloudHSM.

###### Topics

- [Issue: Errors in OpenSSL CLI when used with OpenSSL Provider](#ki-openssl-provider-1 "#ki-openssl-provider-1")
- [Issue: Ed25519 and ML-DSA TLS offload not supported on FIPS clusters](#ki-openssl-provider-3 "#ki-openssl-provider-3")
- [Issue: ML-DSA operations fail on platforms with OpenSSL earlier than 3.5](#ki-openssl-provider-4 "#ki-openssl-provider-4")
- [Issue: ML-DSA TLS handshake fails on Amazon Linux 2023 and RHEL with "no shared signature algorithms"](#ki-openssl-provider-5 "#ki-openssl-provider-5")

## Issue: Errors in OpenSSL CLI when used with OpenSSL Provider

- **Impact:**
  The AWS CloudHSM OpenSSL Provider did not support OpenSSL CLI operations (CSR creation, certificate signing). You had to use the OpenSSL Dynamic Engine for CSR and certificate operations.
- **Resolution status:** Client SDK 5.18.0 resolves this issue. The OpenSSL Provider now supports OpenSSL CLI operations for all key types (RSA, EC, Ed25519, and ML-DSA). Upgrade to version 5.18.0 or later to benefit from the fix.

## Issue: Ed25519 and ML-DSA TLS offload not supported on FIPS clusters

- **Impact:**
  Ed25519 and ML-DSA key types are not available on FIPS-mode clusters. Attempts to use these key types for TLS offload on a FIPS cluster fail.
- **Resolution:**
  Use Ed25519 and ML-DSA only on non-FIPS clusters. For FIPS clusters, use RSA or EC key types for TLS offload.

## Issue: ML-DSA operations fail on platforms with OpenSSL earlier than 3.5

- **Impact:**
  ML-DSA key types (ML-DSA-44, ML-DSA-65, ML-DSA-87) require OpenSSL 3.5 or later for CSR creation, certificate creation, and TLS offload. On platforms with an older system OpenSSL, ML-DSA operations fail with an "unsupported algorithm" error.
- **Resolution:**
  Use a platform with OpenSSL 3.5 or later, or build a custom OpenSSL 3.5+ binary for ML-DSA operations.

## Issue: ML-DSA TLS handshake fails on Amazon Linux 2023 and RHEL with "no shared signature algorithms"

- **Impact:**
  TLS connections using ML-DSA certificates fail on Amazon Linux 2023, RHEL 9, and RHEL 10 platforms with the error `tls1_set_server_sigalgs:no shared signature algorithms`. This occurs because the system-wide crypto-policies framework does not include ML-DSA signature algorithms (`mldsa44`, `mldsa65`, `mldsa87`) in the default `SignatureAlgorithms` allowlist. Non-TLS operations (key generation, signing, verification) are not affected. Ubuntu 26.04 LTS is not affected because it does not use the crypto-policies framework.
- **Resolution:**
  Enable the post-quantum (PQ) crypto sub-policy on your platform:

  - **Amazon Linux 2023** (requires AL2023.12+): Run `sudo update-crypto-policies --set DEFAULT:PQ`. For more information, see [Post-quantum cryptography policies](../../../linux/al2023/ug/crypto-policies-pq.md "../../../linux/al2023/ug/crypto-policies-pq.md") in the Amazon Linux 2023 User Guide.
  - **RHEL 9** (requires RHEL 9.8+): Run `sudo dnf update crypto-policies`, then `sudo update-crypto-policies --set DEFAULT:PQ`. For more information, see [Using system-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/using-the-system-wide-cryptographic-policies_security-hardening "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/using-the-system-wide-cryptographic-policies_security-hardening") in the RHEL 9 documentation.
  - **RHEL 10** (requires RHEL 10.1+): ML-DSA is enabled in the `DEFAULT` policy automatically. Run `sudo dnf update` to ensure you have the latest crypto-policies package. For more information, see [Using system-wide cryptographic policies](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies "https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/10/html/security_hardening/using-system-wide-cryptographic-policies") in the RHEL 10 documentation.
