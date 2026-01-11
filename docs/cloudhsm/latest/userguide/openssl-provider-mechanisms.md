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
