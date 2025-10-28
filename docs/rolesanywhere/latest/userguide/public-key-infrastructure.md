# Public key infrastructure in IAM Roles Anywhere

AWS Identity and Access Management Roles Anywhere relies on public key infrastructure (PKI) to establish trust between your
AWS account and certificate authorities that issue certificates to workloads running in your
data centers. PKI involves the generation, distribution, and verification of digital
certificates through public key encryption. Trust requires either
uploading your CA's digital certificate as a trust anchor or referencing an existing
[AWS Private Certificate Authority (AWS Private CA)](../../../privateca/latest/userguide/PcaWelcome.md "../../../privateca/latest/userguide/PcaWelcome.md").
Once a trust anchor is created, you can use client certificates issued by that certificate to
authenticate and receive temporary credentials from IAM Roles Anywhere.

## Certificate authorities

_Certificate authorities_ are entities that are trusted to issue
certificates. The CA issues signed digital certificates that affirm the identity of the certificate subject and bind that identity to the public key contained in the certificate. The CA signs a certificate by hashing the contents and then encrypting the hash with the private key related to the public key in the certificate. A client application such as a web browser that needs to affirm the identity of a subject uses the public key to verify the certificate signature. It then hashes the certificate contents and compares the hashed value to the decrypted signature to determine whether they match. Certificates can have constraints on the uses of the keys associated with the certificate. For more information about trust path validation, see [RFC
5280](https://datatracker.ietf.org/doc/html/rfc5280 "https://datatracker.ietf.org/doc/html/rfc5280").

## Certificates

Certificates, specifically X.509 certificates, bind an identity to public key, using a signature
generated from a corresponding private key.

## Key management

PKI uses a pair of keys to perform cryptographic operations such as encryption and generating digital signatures. One of the keys is public and is typically made available in an X.509 certificate. The other key is private and should be stored securely. Take care to ensure that your private keys are not shared.
