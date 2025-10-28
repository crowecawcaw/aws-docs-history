# Supported mechanisms for OpenSSL Dynamic Engine for AWS CloudHSM

Client SDK 5

The AWS CloudHSM OpenSSL Dynamic Engine supports the following mechanisms for Sign and Verify functions with
Client SDK 5.

## Sign and verify functions

With Client SDK 5, the data is hashed locally in software. This means there is no limit on the size of the data that can be hashed.

RSA Signature Types

- SHA1withRSA
- SHA224withRSA
- SHA256withRSA
- SHA384withRSA
- SHA512withRSA

ECDSA Signature Types

- SHA1withECDSA
- SHA224withECDSA
- SHA256withECDSA
- SHA384withECDSA
- SHA512withECDSA
