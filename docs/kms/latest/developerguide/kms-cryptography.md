# AWS KMS cryptography essentials

AWS KMS uses configurable cryptographic algorithms so that the system can quickly migrate
from one approved algorithm, or mode, to another. The initial default set of cryptographic
algorithms has been selected from Federal Information Processing Standard (FIPS-approved)
algorithms for their security properties and performance.

For more information on prefered and acceptable cryptographic algorithms, see [Supported cryptographic algorithms](supported-algorithms.md "supported-algorithms.md").

## Entropy and random number generation

AWS KMS key generation is performed in the AWS KMS HSMs. The HSMs implement a hybrid random
number generator that uses the [NIST
SP800-90A Deterministic Random Bit Generator (DRBG) CTR_DRBG using AES-256](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90Ar1.pdf"). It is
seeded with a nondeterministic random bit generator with 384-bits of entropy and updated
with additional entropy to provide prediction resistance on every call for cryptographic
material.

## Symmetric key operations (encryption only)

All symmetric key encrypt commands used within HSMs use the [Advanced Encryption
Standards (AES)](http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf "http://csrc.nist.gov/publications/fips/fips197/fips-197.pdf"), in [Galois Counter
Mode (GCM)](http://csrc.nist.gov/publications/nistpubs/800-38D/SP-800-38D.pdf "http://csrc.nist.gov/publications/nistpubs/800-38D/SP-800-38D.pdf") using 256-bit keys. The analogous calls to decrypt use the inverse
function.

AES-GCM is an authenticated encryption scheme. In addition to encrypting plaintext to
produce ciphertext, it computes an authentication tag over the ciphertext and any additional
data for which authentication is required (additionally authenticated data, or AAD). The
authentication tag helps ensure that the data is from the purported source and that the
ciphertext and AAD have not been modified.

Frequently, AWS omits the inclusion of the AAD in our descriptions, especially when
referring to the encryption of data keys. It is implied by surrounding text in these cases
that the structure to be encrypted is partitioned between the plaintext to be encrypted and
the cleartext AAD to be protected.

AWS KMS provides an option for you to import key material into an AWS KMS key instead
of relying on AWS KMS to generate the key material. This imported key material can be
encrypted using [RSAES-OAEP](https://datatracker.ietf.org/doc/html/rfc8017#section-7.1 "https://datatracker.ietf.org/doc/html/rfc8017#section-7.1") to protect the key during transport to the AWS KMS HSM. The RSA key
pairs are generated on AWS KMS HSMs. The imported key material is decrypted on an AWS KMS HSM
and re-encrypted under AES-GCM before being stored by the service.

## Asymmetric key operations (encryption, digital signing

and signature verification)

AWS KMS supports the use of asymmetric key operations for both encryption, digital
signature, and key agreement operations. Asymmetric key operations rely on a mathematically
related public key and private key pair that you can use for encryption and decryption,
signing and signature verification, _or_ deriving shared secrets. The
private key never leaves AWS KMS unencrypted. You can use the public key within AWS KMS by
calling the AWS KMS API operations, or download the public key and use it outside of AWS KMS.

AWS KMS supports the following asymmetric ciphers.

- **RSA-OAEP (for encryption) & RSA-PSS and RSA-PKCS-#1-v1_5
  (for signing and verification)** – Supports RSA key lengths (in bits):
  2048, 3072, and 4096 for different security requirements.
- **Elliptic Curve (ECC)** – Used for signing and
  verification or deriving shared secrets, but not both. Supports ECC curves: NIST P256,
  P384, P521, SECP 256k1, Ed25519.
- **ML-DSA** – Used for signing and verification.
  Supported ML-DSA key specs are: ML_DSA_44, ML_DSA_65, and ML_DSA_87.
- **SM2 (China Regions only)** – Used for
  encryption and decryption, signing and verification, or deriving shared secrets, but you
  must choose one key usage. Supports SM2PKE for encryption and SM2DSA for signing.

## Key derivation functions

A key derivation function is used to derive additional keys from an initial secret or
key. AWS KMS uses an key derivation function (KDF) to derive per-call keys for every
encryption under an AWS KMS key. All KDF operations use the [KDF in
counter mode](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-108.pdf "https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-108.pdf") using HMAC [[FIPS197]](http://csrc.nist.gov/publications/fips/fips198-1/FIPS-198-1_final.pdf "http://csrc.nist.gov/publications/fips/fips198-1/FIPS-198-1_final.pdf") with SHA256 [[FIPS180]](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf"). The
256-bit derived key is used with AES-GCM to encrypt or decrypt customer data and
keys.

## AWS KMS internal use of digital signatures

Digital signatures are also used to authenticate commands and communications between
AWS KMS entities. All service entities have an elliptic curve digital signature algorithm
(ECDSA) key pair. They perform ECDSA as defined in [Use of Elliptic Curve Cryptography
(ECC) Algorithms in Cryptographic Message Syntax (CMS)](https://datatracker.ietf.org/doc/html/rfc5753/ "https://datatracker.ietf.org/doc/html/rfc5753/") and X9.62-2005:
_Public Key Cryptography for the Financial Services Industry: The Elliptic Curve
Digital Signature Algorithm (ECDSA)_. The entities use the secure hash algorithm
defined in [Federal
Information Processing Standards Publications, FIPS PUB 180-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf "https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.180-4.pdf"), known as SHA384.
The keys are generated on the curve secp384r1 (NIST-P384).

## Envelope encryption

When you encrypt your data, your data is protected, but you have to protect your
encryption key. One strategy is to encrypt it. _Envelope
encryption_ is the practice of encrypting plaintext data with a data key, and
then encrypting the data key under another key.

You can even encrypt the data encryption key under another encryption key, and encrypt
that encryption key under another encryption key. But, eventually, one key must remain in
plaintext so you can decrypt the keys and your data. This top-level plaintext key encryption
key is known as the _root key_.

![Envelope encryption](images/key-hierarchy-root.png)

AWS KMS helps you to protect your encryption keys by storing and managing them securely.
Root key stored in AWS KMS, known as AWS KMS keys, never leave the AWS KMS [FIPS 140-3 Security Level 3 validated hardware security
modules](https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884 "https://csrc.nist.gov/projects/cryptographic-module-validation-program/certificate/4884") unencrypted. To use a KMS key, you must call AWS KMS.

A basic construction used within many cryptographic systems is envelope encryption.
Envelope encryption uses two or more cryptographic keys to secure a message. Typically, one
key is derived from a longer-term static key _k_, and another key is a
per-message key, _msgKey_, which is generated to encrypt the message. The
envelope is formed by encrypting the message: _ciphertext = Encrypt(msgKey,
message)_ . Then the message key is encrypted with the long-term static key:
_encKey = Encrypt(k, msgKey)_ . Finally, the two values _(encKey, ciphertext)_ are packaged into a single structure, or envelope
encrypted message.

The recipient, with access to _k_, can open the
enveloped message by first decrypting the encrypted key and then decrypting the
message.

AWS KMS provides the ability to manage these longer-term static keys and automate the
process of envelope encryption of your data.

In addition to the encryption capabilities provided within the AWS KMS service, the [AWS
Encryption SDK](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md") provides client-side envelope encryption libraries. You can use
these libraries to protect your data and the encryption keys that are used to encrypt that
data.

![Envelope encryption with multiple key encryption keys](images/key-hierarchy-kms-key.png)

Envelope encryption offers several benefits:

- **Protecting data keys**

When you encrypt a data key, you don't have to worry about storing the encrypted
data key, because the data key is inherently protected by encryption. You can safely
store the encrypted data key alongside the encrypted data.

- **Encrypting the same data under multiple keys**

Encryption operations can be time consuming, particularly when the data being
encrypted are large objects. Instead of re-encrypting raw data multiple times with
different keys, you can re-encrypt only the data keys that protect the raw data.

- **Combining the strengths of multiple
  algorithms**

In general, symmetric key algorithms are faster and produce smaller ciphertexts than
public key algorithms. But public key algorithms provide inherent separation of roles
and easier key management. Envelope encryption lets you combine the strengths of each
strategy.

## Cryptographic operations

In AWS KMS, _cryptographic operations_ are API operations
that use KMS keys to protect data. Because KMS keys remain within AWS KMS, you must call
AWS KMS to use a KMS key in a cryptographic operation.

To perform cryptographic operations with KMS keys, use the AWS SDKs, AWS Command Line Interface
(AWS CLI), or the AWS Tools for PowerShell. You cannot perform cryptographic operations in the AWS KMS
console. For examples of calling the cryptographic operations in several programming
languages, see [Code examples for AWS KMS using AWS SDKs](service_code_examples.md "service_code_examples.md").

The following table lists the AWS KMS cryptographic operations. It also shows the key type
and [key usage](create-keys.md#key-usage "create-keys.md#key-usage") requirements for KMS keys used in the
operation.

| Operation                                                                                                                                                      | Key type                                                        | Key usage             |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | --------------------- |
| [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md")                                                                                     | Symmetric or asymmetric                                         | `ENCRYPT_DECRYPT`     |
| [DeriveSharedSecret](../APIReference/API_DeriveSharedSecret.md "../APIReference/API_DeriveSharedSecret.md")                                                    | Asymmetric                                                      | `KEY_AGREEMENT`       |
| [Encrypt](../APIReference/API_Encrypt.md "../APIReference/API_Encrypt.md")                                                                                     | Symmetric or asymmetric                                         | `ENCRYPT_DECRYPT`     |
| [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md")                                                             | Symmetric                                                       | `ENCRYPT_DECRYPT`     |
| [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md")                                                 | Symmetric [1]Not supported on KMS keys in custom key<br>stores. | `ENCRYPT_DECRYPT`     |
| [GenerateDataKeyPairWithoutPlaintext](../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md "../APIReference/API_GenerateDataKeyPairWithoutPlaintext.md") | Symmetric [1]Not supported on KMS keys in custom key<br>stores. | `ENCRYPT_DECRYPT`     |
| [GenerateDataKeyWithoutPlaintext](../APIReference/API_GenerateDataKeyWithoutPlaintext.md "../APIReference/API_GenerateDataKeyWithoutPlaintext.md")             | Symmetric                                                       | `ENCRYPT_DECRYPT`     |
| [GenerateMac](../APIReference/API_GenerateMac.md "../APIReference/API_GenerateMac.md")                                                                         | HMAC                                                            | `GENERATE_VERIFY_MAC` |
| [GenerateRandom](../APIReference/API_GenerateRandom.md "../APIReference/API_GenerateRandom.md")                                                                | N/A. This operation doesn't use a KMS key.                      | N/A                   |
| [ReEncrypt](../APIReference/API_ReEncrypt.md "../APIReference/API_ReEncrypt.md")                                                                               | Symmetric or asymmetric                                         | `ENCRYPT_DECRYPT`     |
| [Sign](../APIReference/API_Sign.md "../APIReference/API_Sign.md")                                                                                              | Asymmetric                                                      | `SIGN_VERIFY`         |
| [Verify](../APIReference/API_Verify.md "../APIReference/API_Verify.md")                                                                                        | Asymmetric                                                      | `SIGN_VERIFY`         |
| [VerifyMac](../APIReference/API_VerifyMac.md "../APIReference/API_VerifyMac.md")                                                                               | HMAC                                                            | `GENERATE_VERIFY_MAC` |

[1] Generates an asymmetric data key pair that is protected by a symmetric encryption KMS key.

For information about the permissions for cryptographic operations, see the [AWS KMS permissions](kms-api-permissions-reference.md "kms-api-permissions-reference.md").

To make AWS KMS responsive and highly functional for all users, AWS KMS establishes quotas
on number of cryptographic operations called in each second. For details, see [Shared quotas for cryptographic operations](requests-per-second.md#rps-shared-limit "requests-per-second.md#rps-shared-limit").
