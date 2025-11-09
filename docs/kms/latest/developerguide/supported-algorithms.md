# Supported cryptographic algorithms

## Cryptographic algorithms

The following tables summarize the cryptographic algorithms, ciphers, modes, and key
sizes that AWS deploys across its services to protect your data. They should not be
considered to be an exhaustive list of all cryptography options available in AWS. The
algorithms fall into two categories:

- _Preferred_ algorithms meet the AWS security
  and performance standards.
- _Acceptable_ algorithms can be used for compatibility in
  some applications but are not preferred.

### Asymmetric cryptography

The following table lists supported asymmetric algorithms for
encryption, key agreement, and digital signatures.

| Type          | Algorithm                                                         | Status                                                  |
| ------------- | ----------------------------------------------------------------- | ------------------------------------------------------- |
| Encryption    | RSA-OAEP (2048 or 3072-bit modulus)                               | Acceptable                                              |
| Encryption    | HPKE (P-256 or P-384, HKDF and AES-GCM)                           | Acceptable                                              |
| Key Agreement | ML-KEM-768 or ML-KEM-1024                                         | Preferred (quantum-resistant)                           |
| Key Agreement | ECDH(E) with P-384                                                | Acceptable                                              |
| Key Agreement | ECDH(E) with P-256, P-521, or X25519                              | Acceptable                                              |
| Key Agreement | ECDH(E) with brainpoolP256r1, brainpoolP384r1, or brainpoolP512r1 | Acceptable                                              |
| Signatures    | ML-DSA-65 or ML-DSA-87                                            | Preferred (quantum-resistant)                           |
| Signatures    | SLH-DSA                                                           | Preferred (quantum-resistant software/firmware signing) |
| Signatures    | ECDSA with P-384                                                  | Acceptable                                              |
| Signatures    | ECDSA with P-256, P-521, or Ed25519                               | Acceptable                                              |
| Signatures    | RSA-2048 or RSA-3072                                              | Acceptable                                              |

### Symmetric cryptography

The following table lists supported symmetric algorithms for encryption, authenticated encryption, and key wrapping.

| Type                     | Algorithm                             | Status     |
| ------------------------ | ------------------------------------- | ---------- |
| Authenticated Encryption | AES-GCM-256                           | Preferred  |
| Authenticated Encryption | AES-GCM-128                           | Acceptable |
| Authenticated Encryption | ChaCha20/Poly1305                     | Acceptable |
| Encryption Modes         | AES-XTS-256 (for block storage)       | Preferred  |
| Encryption Modes         | AES-CBC / CTR (unauthenticated modes) | Acceptable |
| Key Wrapping             | AES-GCM-256                           | Preferred  |
| Key Wrapping             | AES-KW or AES-KWP with 256-bit keys   | Acceptable |

### Cryptographic functions

The following table lists supported algorithms for hashing, key derivation, message authentication, and password hashing.

| Type                        | Algorithm                           | Status     |
| --------------------------- | ----------------------------------- | ---------- |
| Hashing                     | SHA2-384                            | Preferred  |
| Hashing                     | SHA2-256                            | Acceptable |
| Hashing                     | SHA3                                | Acceptable |
| Key Derivation              | HKDF_Expand or HKDF with SHA2-256   | Preferred  |
| Key Derivation              | Counter Mode KDF with HMAC-SHA2-256 | Acceptable |
| Message Authentication Code | HMAC-SHA2-384                       | Preferred  |
| Message Authentication Code | HMAC-SHA2-256                       | Acceptable |
| Message Authentication Code | KMAC                                | Acceptable |
| Password Hashing            | scrypt with SHA384                  | Preferred  |
| Password Hashing            | PBKDF2                              | Acceptable |

For more details on cryptographic algorithms deployed in AWS, see [Cryptography algorithms and AWS services](../../../prescriptive-guidance/latest/encryption-best-practices/aws-cryptography-services.md#algorithms "../../../prescriptive-guidance/latest/encryption-best-practices/aws-cryptography-services.md#algorithms").
