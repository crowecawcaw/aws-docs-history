# Supported key types for JCE provider for AWS CloudHSM Client SDK 5

The AWS CloudHSM software library for Java enables you to generate the following key
types.

| Key Type                      | Description                                                                                                                                                                                                      |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AES**                       | Generate 128, 192, and 256-bit AES keys.                                                                                                                                                                         |
| **Triple DES (3DES, DESede)** | Generate a 192-bit Triple DES Key [\*](#java-lib-keys_5-note-1 "#java-lib-keys_5-note-1").                                                                                                                       |
| **EC**                        | Generate EC key pairs – NIST curves secp224r1 (P-224), secp256r1 (P-256), secp256k1<br>(Blockchain), secp384r1 (P-384), secp521r1 (P-521), and ed25519[\*\*](#java-lib-keys_5-note-2 "#java-lib-keys_5-note-2"). |
| **GENERIC\_SECRET**           | Generate 1 to 800 bytes generic secrets.                                                                                                                                                                         |
| **HMAC**                      | Hash support for SHA1, SHA224, SHA256, SHA384, SHA512.                                                                                                                                                           |
| **ML-DSA**                    | Generate ML-DSA key pairs with parameter sets ML-DSA-44, ML-DSA-65, and ML-DSA-87.                                                                                                                               |
| **RSA**                       | Generate 2048-bit to 4096-bit RSA keys, in increments of 256 bits.                                                                                                                                               |

\* In accordance with NIST guidance, this is disallowed for clusters in FIPS mode after 2023. For clusters in non-FIPS mode, it is still allowed after 2023. See [FIPS 140 Compliance: 2024 Mechanism Deprecation](compliance-dep-notif.md#compliance-dep-notif-1 "compliance-dep-notif.md#compliance-dep-notif-1") for details.

\*\* Only supported on hsm2m.medium instances in non-FIPS mode.
