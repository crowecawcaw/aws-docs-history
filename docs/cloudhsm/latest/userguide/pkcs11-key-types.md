# Supported key types for the PKCS #11 library for AWS CloudHSM

Client SDK 5

The PKCS #11 library for AWS CloudHSM Client SDK 5supports the following key types.

| Key Type                      | Description                                                                                                                           |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **AES**                       | Generate 128, 192, and 256-bit AES keys.                                                                                              |
| **Triple DES (3DES, DESede)** | Generate 192-bit Triple DES keys. See note [1](#key-types-1 "#key-types-1") below for an upcoming change.                             |
| **EC**                        | Generate keys with the secp224r1 (P-224), secp256r1 (P-256), secp256k1 (Blockchain), secp384r1 (P-384), and secp521r1 (P-521) curves. |
| **GENERIC_SECRET**            | Generate 1 to 800 bytes generic secrets.                                                                                              |
| **RSA**                       | Generate 2048-bit to 4096-bit RSA keys, in increments of 256 bits.                                                                    | [1] In accordance with NIST guidance, this is disallowed for clusters in FIPS mode after 2023. For clusters in non-FIPS mode, it is still allowed after 2023. See [FIPS 140 Compliance: 2024 Mechanism Deprecation](compliance-dep-notif.md#compliance-dep-notif-1 "compliance-dep-notif.md#compliance-dep-notif-1") for details. |
