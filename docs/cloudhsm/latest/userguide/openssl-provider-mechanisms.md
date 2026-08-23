# OpenSSL Provider Supported Mechanisms

The AWS CloudHSM OpenSSL Provider SDK supports a comprehensive set of cryptographic mechanisms for various operations including digital signatures, asymmetric encryption, symmetric encryption, key exchange, and more.

## RSA signature types

The OpenSSL Provider supports RSA digital signatures with multiple hash algorithms and padding schemes:

SHA1withRSA

RSA signatures with SHA-1 hash algorithm

- PKCS#1 v1.5 padding
- PSS (Probabilistic Signature Scheme) padding

SHA224withRSA

RSA signatures with SHA-224 hash algorithm

- PKCS#1 v1.5 padding
- PSS padding

SHA256withRSA

RSA signatures with SHA-256 hash algorithm

- PKCS#1 v1.5 padding
- PSS padding

SHA384withRSA

RSA signatures with SHA-384 hash algorithm

- PKCS#1 v1.5 padding
- PSS padding

SHA512withRSA

RSA signatures with SHA-512 hash algorithm

- PKCS#1 v1.5 padding
- PSS padding

## ECDSA signature types

The OpenSSL Provider supports ECDSA digital signatures with multiple hash algorithms:

SHA1withECDSA

ECDSA signatures with SHA-1 hash algorithm

SHA224withECDSA

ECDSA signatures with SHA-224 hash algorithm

SHA256withECDSA

ECDSA signatures with SHA-256 hash algorithm

SHA384withECDSA

ECDSA signatures with SHA-384 hash algorithm

SHA512withECDSA

ECDSA signatures with SHA-512 hash algorithm

## EdDSA signature types

The OpenSSL Provider supports EdDSA digital signatures. Ed25519 is only available on non-FIPS clusters.

Ed25519

Ed25519 performs EdDSA signatures using Curve25519 (RFC 8032) with one-shot signing and an internal SHA-512 hash. You cannot select an external digest algorithm. Ed25519 supports TLS 1.3 signature negotiation.

## ML-DSA signature types

The OpenSSL Provider supports ML-DSA (Module-Lattice Digital Signature Algorithm) post-quantum digital signatures as defined in FIPS 204. ML-DSA is only available on non-FIPS clusters and requires OpenSSL 3.5 or later.

ML-DSA-44, ML-DSA-65, ML-DSA-87

ML-DSA provides post-quantum signatures at NIST security levels 2 (ML-DSA-44, 128-bit), 3 (ML-DSA-65, 192-bit), and 5 (ML-DSA-87, 256-bit). All variants use one-shot pure mode signing. You cannot select an external digest algorithm. ML-DSA supports TLS 1.3 signature negotiation.
