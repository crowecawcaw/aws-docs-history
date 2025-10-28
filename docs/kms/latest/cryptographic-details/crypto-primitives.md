# Cryptographic primitives

AWS KMS uses configurable cryptographic algorithms so that the system can quickly migrate from
one approved algorithm, or mode, to another. The initial default set of cryptographic algorithms
has been selected from Federal Information Processing Standard (FIPS-approved) algorithms for
their security properties and performance.

## Entropy and random number generation

AWS KMS key generation is performed on the AWS KMS HSMs. The HSMs implement a hybrid random
number generator that uses the [NIST
SP800-90A Deterministic Random Bit Generator (DRBG) CTR_DRBG using AES-256](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf"). It is
seeded with a nondeterministic random bit generator with 384-bits of entropy and updated with
additional entropy to provide prediction resistance on every call for cryptographic
material.

## Symmetric key operations (encryption only)

All symmetric key encrypt commands used within HSMs use the [Advanced Encryption
Standards (AES)](http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf "http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf"), in [Galois Counter Mode
(GCM)](http://csrc.nist.gov/publications/nistpubs/800-38D/SP-800-38D.pdf "http://csrc.nist.gov/publications/nistpubs/800-38D/SP-800-38D.pdf") using 256-bit keys. The analogous calls to decrypt use the inverse function.

AES-GCM is an authenticated encryption scheme. In addition to encrypting plaintext to
produce ciphertext, it computes an authentication tag over the ciphertext and any additional
data for which authentication is required (additionally authenticated data, or AAD). The
authentication tag helps ensure that the data is from the purported source and that the
ciphertext and AAD have not been modified.

Frequently, AWS omits the inclusion of the AAD in our descriptions, especially when
referring to the encryption of data keys. It is implied by surrounding text in these cases
that the structure to be encrypted is partitioned between the plaintext to be encrypted and
the cleartext AAD to be protected.

AWS KMS provides an option for you to import key material into an AWS KMS key instead of
relying on AWS KMS to generate the key material. This imported key material can be encrypted
using [RSAES-OAEP](https://datatracker.ietf.org/doc/html/rfc8017#section-7.1 "https://datatracker.ietf.org/doc/html/rfc8017#section-7.1") or [RSAES-PKCS1-v1_5](https://datatracker.ietf.org/doc/html/rfc8017#section-7.2 "https://datatracker.ietf.org/doc/html/rfc8017#section-7.2") to
protect the key during transport to the AWS KMS HSM. The RSA key pairs are generated on AWS KMS
HSMs. The imported key material is decrypted on an AWS KMS HSM and re-encrypted under AES-GCM
before being stored by the service.

## Asymmetric key operations (encryption, digital signing

and signature verification)

AWS KMS supports the use of asymmetric key operations for both encryption and digital
signature operations. Asymmetric key operations rely on a mathematically related public key
and private key pair that you can use for encryption and decryption or signing and signature
verification, but not both. The private key never leaves AWS KMS unencrypted. You can use the
public key within AWS KMS by calling the AWS KMS API operations, or download the public key and
use it outside of AWS KMS.

AWS KMS supports three types of asymmetric ciphers.

- **RSA-OAEP (for encryption) & RSA-PSS and RSA-PKCS-#1-v1_5
  (for signing and verification)** – Supports RSA key lengths (in bits):
  2048, 3072, and 4096 for different security requirements.
- **Elliptic Curve (ECC)** – Used exclusively for
  signing and verification. Supports ECC curves: NIST P256, P384, P521, SECP 256k1.
- **Post Quantum Cryptography** - New public-key cryptographic
  algorithms that are resistant to quantum computing. Supports the [NIST FIPS 204 Module-Lattice Digital
  Signature Algorithm (ML-DSA)](https://csrc.nist.gov/pubs/fips/204/final "https://csrc.nist.gov/pubs/fips/204/final") with ML_DSA_44, ML_DSA_65, and ML_DSA_87 key
  sizes.

## Key derivation functions

A key derivation function is used to derive additional keys from an initial secret or key.
AWS KMS uses a key derivation function (KDF) to derive per-call keys for every encryption under
an AWS KMS key. All KDF operations use the [KDF in
counter mode](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-108.pdf "https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-108.pdf") using HMAC [[FIPS197]](http://csrc.nist.gov/publications/fips/fips198-1/FIPS-198-1_final.pdf "http://csrc.nist.gov/publications/fips/fips198-1/FIPS-198-1_final.pdf") with SHA256 [[FIPS180]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf"). The
256-bit derived key is used with AES-GCM to encrypt or decrypt customer data and keys.

## AWS KMS internal use of digital signatures

Digital signatures are also used to authenticate commands and communications between AWS KMS
entities. All service entities have an elliptic curve digital signature algorithm (ECDSA) key
pair. They perform ECDSA as defined in [Use of Elliptic Curve Cryptography
(ECC) Algorithms in Cryptographic Message Syntax (CMS)](https://datatracker.ietf.org/doc/html/rfc5753/ "https://datatracker.ietf.org/doc/html/rfc5753/") and X9.62-2005:
_Public Key Cryptography for the Financial Services Industry: The Elliptic Curve
Digital Signature Algorithm (ECDSA)_. The entities use the secure hash algorithm
defined in [Federal
Information Processing Standards Publications, FIPS PUB 180-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf"), known as SHA384. The
keys are generated on the curve secp384r1 (NIST-P384).

## Envelope encryption

A basic construction used within many cryptographic systems is envelope encryption.
Envelope encryption uses two or more cryptographic keys to secure a message. Typically, one
key is derived from a longer-term static key _k_, and another key is a
per-message key, _msgKey_, which is generated to encrypt the message. The
envelope is formed by encrypting the message: _ciphertext = Encrypt(msgKey, message)_ . Then the message key is encrypted with the long-term static key: _encKey
= Encrypt(k, msgKey)_ . Finally, the two values _(encKey, ciphertext)_ are packaged into a single structure, or envelope encrypted message.

The recipient, with access to _k_, can open the enveloped
message by first decrypting the encrypted key and then decrypting the message.

AWS KMS provides the ability to manage these longer-term static keys and automate the
process of envelope encryption of your data.

In addition to the encryption capabilities provided within the AWS KMS service, the [AWS
Encryption SDK](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md") provides client-side envelope encryption libraries. You can use these
libraries to protect your data and the encryption keys that are used to encrypt that
data.
