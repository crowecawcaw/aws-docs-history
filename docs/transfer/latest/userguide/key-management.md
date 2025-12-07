# Managing SSH and PGP keys in Transfer Family

In this section, you can find information about SSH keys, including how to generate them
and how to rotate them. For details about using Transfer Family with AWS Lambda to manage keys, see the
blog post [Enabling user self-service key management with AWS Transfer Family and AWS Lambda](https://aws.amazon.com/blogs/storage/enabling-user-self-service-key-management-with-aws-transfer-family-and-aws-lambda/ "https://aws.amazon.com/blogs/storage/enabling-user-self-service-key-management-with-aws-transfer-family-and-aws-lambda/"). For
automated deployment and management of users with multiple SSH keys, see [Transfer Family Terraform modules](terraform.md "terraform.md").

###### Note

AWS Transfer Family accepts RSA, ECDSA, and ED25519 keys for SSH authentication.

This section also covers how to generate and manage Pretty Good Privacy (PGP) keys.

For a comprehensive overview of all supported encryption and key algorithms, including
recommendations for different use cases, see [Encryption and key algorithms
overview](#encryption-algorithms-overview "#encryption-algorithms-overview").

## Encryption and key algorithms

overview

AWS Transfer Family supports different types of algorithms for different purposes. Understanding
which algorithms to use for your specific use case helps ensure secure and compatible
file transfers.

| Algorithm Quick Reference | Use Case                                  | Recommended Algorithm             | FIPS Compliant                              | Notes |
| ------------------------- | ----------------------------------------- | --------------------------------- | ------------------------------------------- | ----- |
| SSH/SFTP Authentication   | RSA (rsa-sha2-256/512), ECDSA, or ED25519 | RSA: Yes, ECDSA: Yes, ED25519: No | Compatible with all SSH clients and servers |
| PGP Key Generation        | RSA or ECC (NIST)                         | Yes                               | For workflow decryption                     |
| PGP File Encryption       | AES-256                                   | Yes                               | Determined by PGP software                  |

## SSH authentication algorithms

These algorithms are used for SSH/SFTP authentication between clients and AWS Transfer Family
servers. Choose one of these when generating SSH key pairs for user authentication or
server host keys.

RSA (Recommended)

**Compatible with all SSH clients and servers, and
FIPS-compliant.** Use with SHA-2 hashing for enhanced
security:

- `rsa-sha2-256` - Recommended for most use cases
- `rsa-sha2-512` - Higher security option

ED25519

**Modern and efficient.** Smaller key sizes
with strong security:

- `ssh-ed25519` - Fast and secure, but not
  FIPS-compliant

ECDSA

**Elliptic curve option.** Good balance of
security and performance:

- `ecdsa-sha2-nistp256` - Standard curve
- `ecdsa-sha2-nistp384` - Higher security curve
- `ecdsa-sha2-nistp521` - Highest security curve

###### Note

We support `ssh-rsa` with SHA1 for older security policies. For
details, see [Cryptographic algorithms](security-policies.md#cryptographic-algorithms "security-policies.md#cryptographic-algorithms").

Choosing the right SSH algorithm

- **For most users:** Use RSA with
  `rsa-sha2-256` or `rsa-sha2-512`
- **For FIPS compliance:** Use RSA or ECDSA
  algorithms
- **For modern environments:** ED25519 offers
  excellent security and performance

## PGP encryption and decryption

algorithms

PGP (Pretty Good Privacy) uses two types of algorithms working together to encrypt and
decrypt files in workflows:

1. **Key pair algorithms** - Used to generate the
   public/private key pairs for encryption and digital signatures
2. **Symmetric algorithms** - Used to encrypt the
   actual file data (the key pair algorithms encrypt the symmetric key)

### PGP key pair algorithms

Choose one of these algorithms when generating PGP key pairs for workflow
decryption:

RSA (Recommended)

**Recommended for most users.** Widely
supported, well-established, and FIPS-compliant. Provides good balance
of security and compatibility.

ECC (Elliptic Curve Cryptography)

**More efficient than RSA** with smaller
key sizes while maintaining strong security:

- **NIST curves** - Standard curves
  widely supported and FIPS-compliant
- **BrainPool curves** -
  Alternative curves for specific compliance requirements
- **Curve25519** -
  Modern high-performance curve offering strong security with efficient computation

ElGamal

**Legacy algorithm.** Supported for
compatibility with older systems. Use RSA or ECC for new
implementations.

For detailed instructions on generating PGP keys, see [Generate PGP keys](generate-pgp-keys.md "generate-pgp-keys.md").

### PGP symmetric encryption

algorithms

These algorithms encrypt your actual file data. The algorithm used depends on how
the PGP file was created by your PGP software:

FIPS-compliant algorithms (recommended for regulated
environments)

- **AES-128, AES-192, AES-256** - Advanced
  Encryption Standard (recommended)
- **3DES** - Triple Data Encryption Standard
  (legacy, use AES when possible)

Other supported algorithms

- IDEA, CAST5, Blowfish, DES, TwoFish, CAMELLIA-128, CAMELLIA-192,
  CAMELLIA-256

###### Note

You don't choose the symmetric algorithm directly when using AWS Transfer Family
workflows - it's determined by the PGP software used to create the encrypted
file. However, you can configure your PGP software to prefer FIPS-compliant
algorithms like AES-256.

For more information about supported symmetric algorithms, see [Supported symmetric encryption
algorithms](nominal-steps-workflow.md#symmetric-algorithms "nominal-steps-workflow.md#symmetric-algorithms").
