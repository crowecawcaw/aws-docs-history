# Key spec reference

When you create an asymmetric KMS key or an HMAC KMS key, you select its [key spec](create-keys.md#key-spec "create-keys.md#key-spec"). The _key spec_,
which is a property of every AWS KMS key, represents the cryptographic configuration of
your KMS key. You choose the key spec when you create the KMS key, and you cannot change
it. If you've selected the wrong key spec, [delete the
KMS key](deleting-keys.md "deleting-keys.md"), and create a new one.

###### Note

The key spec for a KMS key was known as a "customer master key spec." The
`CustomerMasterKeySpec` parameter of the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation is deprecated.
Instead, use the `KeySpec` parameter. The response of the
`CreateKey` and [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md") operations includes a `KeySpec` and
`CustomerMasterKeySpec` member with the same value.

The key spec determines whether the KMS key is symmetric or asymmetric, the type of key
material in the KMS key, and the encryption algorithms, signing algorithms, or message
authentication code (MAC) algorithms that AWS KMS supports for the KMS key. The key spec
that you choose is typically determined by your use case and regulatory requirements.
However, cryptographic operations on KMS keys with different key specs are priced
differently and are subject to different quotas. For pricing details, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/"). For information about request quotas,
see [Request quotas](requests-per-second.md "requests-per-second.md").

To limit the key specs that principals can use when creating KMS keys, use the [kms:KeySpec](conditions-kms.md#conditions-kms-key-spec "conditions-kms.md#conditions-kms-key-spec") condition key. You can also use the
`kms:KeySpec` condition key to allow principals to call AWS KMS operations only
on KMS keys with a particular key spec. For example, you can deny permission to schedule
deletion of any KMS key with an `RSA_4096` key spec.

AWS KMS supports the following key specs for KMS keys:

[Symmetric encryption key spec](#symmetric-cmks "#symmetric-cmks")
(default)

- SYMMETRIC_DEFAULT

[RSA key specs](#key-spec-rsa "#key-spec-rsa") (encryption and decryption -or-
signing and verification)

- RSA_2048
- RSA_3072
- RSA_4096

[Elliptic curve key specs](#key-spec-ecc "#key-spec-ecc")

- Asymmetric NIST-standard [elliptic curve
  key pairs](https://datatracker.ietf.org/doc/html/rfc5753/ "https://datatracker.ietf.org/doc/html/rfc5753/") (signing and verification -or- deriving shared
  secrets)
  - ECC_NIST_P256 (secp256r1)
  - ECC_NIST_P384 (secp384r1)
  - ECC_NIST_P521 (secp521r1)
  - ECC_NIST_EDWARDS25519 (ed25519) - signing and verification only
    - **Note:** For ECC_NIST_EDWARDS25519 KMS keys, the
      ED25519_SHA_512 signing algorithm requires [`MessageType:RAW`](../APIReference/API_Sign.md#KMS-Sign-request-MessageType "../APIReference/API_Sign.md#KMS-Sign-request-MessageType"), while ED25519_PH_SHA_512 requires [`MessageType:DIGEST`](../APIReference/API_Sign.md#KMS-Sign-request-MessageType "../APIReference/API_Sign.md#KMS-Sign-request-MessageType"). These message types cannot be used interchangeably.

- Other asymmetric elliptic curve key pairs (signing and
  verification)
  - ECC_SECG_P256K1 ([secp256k1](https://en.bitcoin.it/wiki/Secp256k1 "https://en.bitcoin.it/wiki/Secp256k1")), commonly used for cryptocurrency.

[SM2 key spec](#key-spec-sm "#key-spec-sm") (encryption and decryption -or-
signing and verification -or- deriving shared secrets)

- SM2 (China Regions only)

[HMAC key specs](#hmac-key-specs "#hmac-key-specs")

- HMAC_224
- HMAC_256
- HMAC_384
- HMAC_512

[ML-DSA key specs](#key-spec-mldsa "#key-spec-mldsa")

- ML_DSA_44
- ML_DSA_65
- ML_DSA_87

## SYMMETRIC_DEFAULT key spec

The default key spec, SYMMETRIC_DEFAULT, is the key spec for symmetric encryption
KMS keys. When you select the **Symmetric** key type and the
**Encrypt and decrypt** key usage in the AWS KMS console, it selects
the `SYMMETRIC_DEFAULT` key spec. In the [CreateKey](../APIReference/API_CreateKey.md "../APIReference/API_CreateKey.md") operation, if you don't
specify a `KeySpec` value, SYMMETRIC_DEFAULT is selected. If you don't have a
reason to use a different key spec, SYMMETRIC_DEFAULT is a good choice.

SYMMETRIC_DEFAULT represents AES-256-GCM, a symmetric algorithm based on [Advanced Encryption Standard](https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf "https://csrc.nist.gov/csrc/media/publications/fips/197/final/documents/fips-197.pdf") (AES) in [Galois
Counter Mode](http://csrc.nist.gov/publications/nistpubs/800-38D/SP-800-38D.pdf "http://csrc.nist.gov/publications/nistpubs/800-38D/SP-800-38D.pdf") (GCM) with 256-bit keys, an industry standard for secure
encryption. The ciphertext that this algorithm generates supports additional
authenticated data (AAD), such as an [encryption
context](encrypt_context.md "encrypt_context.md"), and GCM provides an additional integrity check on the
ciphertext.

Data encrypted under AES-256-GCM is protected now and in the future. Cryptographers
consider this algorithm to be _quantum resistant_.
Theoretical future, large-scale quantum computing attacks on ciphertexts created under
256-bit AES-GCM keys [reduce the effective security of the key to 128 bits](https://www.etsi.org/images/files/ETSIWhitePapers/QuantumSafeWhitepaper.pdf "https://www.etsi.org/images/files/ETSIWhitePapers/QuantumSafeWhitepaper.pdf"). But, this security
level is sufficient to make brute force attacks on AWS KMS ciphertexts infeasible.

The only exception in China Regions, where SYMMETRIC_DEFAULT represents a 128-bit
symmetric key that uses SM4 encryption. You can only create a 128-bit SM4 key within
China Regions. You cannot create a 256-bit AES-GCM KMS key in China Regions.

You can use a symmetric encryption KMS key in AWS KMS to encrypt, decrypt, and
re-encrypt data, and to protect generated data keys and data key pairs. AWS services
that are integrated with AWS KMS use symmetric encryption KMS keys to encrypt your data
at rest. You can [import your own key material](importing-keys.md "importing-keys.md") into
a symmetric encryption KMS key and create symmetric encryption KMS keys in [custom key stores](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview"). For a table comparing
the operations that you can perform on symmetric and asymmetric KMS keys, see [Comparing Symmetric and Asymmetric
KMS keys](symm-asymm-compare.md "symm-asymm-compare.md").

You can use a symmetric encryption KMS key in AWS KMS to encrypt, decrypt, and
re-encrypt data, and generate data keys and data key pairs. You can create [multi-Region](multi-region-keys-overview.md "multi-region-keys-overview.md") symmetric encryption
KMS keys, [import your own key material](importing-keys.md "importing-keys.md") into a
symmetric encryption KMS key, and create symmetric encryption KMS keys in [custom key stores](key-store-overview.md#custom-key-store-overview "key-store-overview.md#custom-key-store-overview"). For a table comparing
the operations that you can perform on KMS keys of different types, see [Key type reference](symm-asymm-compare.md "symm-asymm-compare.md").

## RSA key specs

When you use an RSA key spec, AWS KMS creates an asymmetric KMS key with an RSA key
pair. The private key never leaves AWS KMS unencrypted. You can use the public key within
AWS KMS, or download the public key for use outside of AWS KMS.

###### Warning

When you encrypt data outside of AWS KMS, be sure that you can decrypt your
ciphertext. If you use the public key from a KMS key that has been deleted from
AWS KMS, the public key from a KMS key configured for signing and verification, or
an encryption algorithm that is not supported by the KMS key, the data is
unrecoverable.

In AWS KMS, you can use asymmetric KMS keys with RSA key pairs for encryption and
decryption, or signing and verification, but not both. This property, known as _[Key usage](create-keys.md#key-usage "create-keys.md#key-usage")_, is
determined separately from the key spec, but you should make that decision before you
select a key spec.

AWS KMS supports the following RSA key specs for encryption and decryption or signing
and verification:

- RSA_2048
- RSA_3072
- RSA_4096

RSA key specs differ by the length of the RSA key in bits. The RSA key spec that you
choose might be determined by your security standards or the requirements of your task.
In general, use the largest key that is practical and affordable for your task.
Cryptographic operations on KMS keys with different RSA key specs are priced
differently. For information about AWS KMS pricing, see [AWS Key Management Service Pricing](https://aws.amazon.com/kms/pricing/ "https://aws.amazon.com/kms/pricing/"). For
information about request quotas, see [Request quotas](requests-per-second.md "requests-per-second.md").

### RSA key specs for encryption and

decryption

When an RSA asymmetric KMS key is used for encryption and decryption, you
encrypt with the public key and decrypt with the private key. When you call the
`Encrypt` operation in AWS KMS for an RSA KMS key, AWS KMS uses the
public key in the RSA key pair and the encryption algorithm you specify to encrypt
your data. To decrypt the ciphertext, call the `Decrypt` operation and
specify the same KMS key and encryption algorithm. AWS KMS then uses the private key
in the RSA key pair to decrypt your data.

You can also download the public key and use it to encrypt data outside of AWS KMS.
Be sure to use an encryption algorithm that AWS KMS supports for RSA KMS keys. To
decrypt the ciphertext, call the `Decrypt` function with the same
KMS key and encryption algorithm.

AWS KMS supports two encryption algorithms for KMS keys with RSA key specs. These
algorithms, which are defined in [PKCS #1 v2.2](https://tools.ietf.org/html/rfc8017 "https://tools.ietf.org/html/rfc8017"), differ in the hash function they use internally. In
AWS KMS, the RSAES_OAEP algorithms always use the same hash function for both hashing
purposes and for the [mask generation function](https://tools.ietf.org/html/rfc8017#appendix-B.2 "https://tools.ietf.org/html/rfc8017#appendix-B.2") (MGF1). You are required to
specify an encryption algorithm when you call the [Encrypt](../APIReference/API_Encrypt.md "../APIReference/API_Encrypt.md") and [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") operations. You can choose a
different algorithm for each request.

| Supported encryption algorithms for RSA key specs | Encryption algorithm                                                                                                                                                | Algorithm description |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| RSAES_OAEP_SHA_1                                  | PKCS #1 v2.2, Section 7.1. RSA encryption with OAEP Padding using<br>SHA-1 for both the hash and in the MGF1 mask generation function<br>along with an empty label. |
| RSAES_OAEP_SHA_256                                | PKCS #1, Section 7.1. RSA encryption with OAEP Padding using<br>SHA-256 for both the hash and in the MGF1 mask generation function<br>along with an empty label.    |

You cannot configure a KMS key to use a particular encryption algorithm.
However, you can use the [kms:EncryptionAlgorithm](conditions-kms.md#conditions-kms-encryption-algorithm "conditions-kms.md#conditions-kms-encryption-algorithm") policy condition to specify the encryption
algorithms that principals are allowed to use with the KMS key.

To get the encryption algorithms for a KMS key, [view the cryptographic configuration](finding-keys.md#viewing-console-details "finding-keys.md#viewing-console-details") of
the KMS key in the AWS KMS console or use the [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md") operation. AWS KMS
also provides the key spec and encryption algorithms when you download your public
key, either in the AWS KMS console or by using the [GetPublicKey](../APIReference/API_GetPublicKey.md "../APIReference/API_GetPublicKey.md") operation.

You might choose an RSA key spec based on the length of the
plaintext data that you can encrypt in each request. The following table shows the
maximum size, in bytes, of the plaintext that you can encrypt in a single call to
the [Encrypt](../APIReference/API_Encrypt.md "../APIReference/API_Encrypt.md") operation. The values
differ with the key spec and encryption algorithm. To compare, you can use a
symmetric encryption KMS key to encrypt up to 4096 bytes at one time.

To compute the maximum plaintext length in bytes for these algorithms, use the
following formula: (`key_size_in_bits` / 8) - (2 \*
`hash_length_in_bits`/8) - 2. For example, for RSA_2048
with SHA-256, the maximum plaintext size in bytes is (2048/8) - (2 \* 256/8) -2 = 190.

| Maximum plaintext size (in bytes) in an Encrypt operation |                  | Encryption algorithm |
| --------------------------------------------------------- | ---------------- | -------------------- |
| Key spec                                                  | RSAES_OAEP_SHA_1 | RSAES_OAEP_SHA_256   |
| **RSA_2048**                                              | 214              | 190                  |
| **RSA_3072**                                              | 342              | 318                  |
| **RSA_4096**                                              | 470              | 446                  |

### RSA key specs for signing and

verification

When an RSA asymmetric KMS key is used for signing and verification, you
generate the signature for a message with the private key and verify the signature
with the public key.

When you call the `Sign` operation in AWS KMS for an asymmetric
KMS key, AWS KMS uses the private key in the RSA key pair, the message, and the
signing algorithm you specify, to generate a signature. To verify the signature,
call the [Verify](../APIReference/API_Verify.md "../APIReference/API_Verify.md") operation. Specify
the signature, plus the same KMS key, message, and signing algorithm. AWS KMS then
uses the public key in the RSA key pair to verify the signature. You can also
download the public key and use it to verify the signature outside of AWS KMS.

AWS KMS supports the following signing algorithms for all KMS keys with an RSA key
spec. You are required to specify a signing algorithm when you call the [Sign](../APIReference/API_Sign.md "../APIReference/API_Sign.md") and [Verify](../APIReference/API_Verify.md "../APIReference/API_Verify.md") operations. You can choose a
different algorithm for each request. When signing with RSA key pairs, RSASSA-PSS
algorithms are preferred. We include RSASSA-PKCS1-v1_5 algorithms for compatibility
with existing applications.

| Supported signing algorithms for RSA key specs | Signing algorithm                                                                                                                                                         | Algorithm description |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| RSASSA_PSS_SHA_256                             | PKCS #1 v2.2, Section 8.1, RSA signature with PSS padding using<br>SHA-256 for both the message digest and the MGF1 mask generation<br>function along with a 256-bit salt |
| RSASSA_PSS_SHA_384                             | PKCS #1 v2.2, Section 8.1, RSA signature with PSS padding using<br>SHA-384 for both the message digest and the MGF1 mask generation<br>function along with a 384-bit salt |
| RSASSA_PSS_SHA_512                             | PKCS #1 v2.2, Section 8.1, RSA signature with PSS padding using<br>SHA-512 for both the message digest and the MGF1 mask generation<br>function along with a 512-bit salt |
| RSASSA_PKCS1_V1_5_SHA_256                      | PKCS #1 v2.2, Section 8.2, RSA signature with PKCS #1v1.5 Padding<br>and SHA-256                                                                                          |
| RSASSA_PKCS1_V1_5_SHA_384                      | PKCS #1 v2.2, Section 8.2, RSA signature with PKCS #1v1.5 Padding<br>and SHA-384                                                                                          |
| RSASSA_PKCS1_V1_5_SHA_512                      | PKCS #1 v2.2, Section 8.2, RSA signature with PKCS #1v1.5 Padding<br>and SHA-512                                                                                          |

You cannot configure a KMS key to use particular signing algorithms. However,
you can use the [kms:SigningAlgorithm](conditions-kms.md#conditions-kms-signing-algorithm "conditions-kms.md#conditions-kms-signing-algorithm") policy condition to specify the signing algorithms
that principals are allowed to use with the KMS key.

To get the signing algorithms for a KMS key, [view the cryptographic configuration](finding-keys.md#viewing-console-details "finding-keys.md#viewing-console-details") of
the KMS key in the AWS KMS console or by using the [DescribeKey](../APIReference/API_DescribeKey.md "../APIReference/API_DescribeKey.md") operation. AWS KMS
also provides the key spec and signing algorithms when you download your public key,
either in the AWS KMS console or by using the [GetPublicKey](../APIReference/API_GetPublicKey.md "../APIReference/API_GetPublicKey.md") operation.

## Elliptic curve key specs

When you use an elliptic curve (ECC) key spec, AWS KMS creates an asymmetric KMS key
with an ECC key pair for signing and verification or deriving shared secrets (but not
both). The private key that generates signatures or derives shared secrets never leaves
AWS KMS unencrypted. You can use the public key to [verify signatures](../APIReference/API_Verify.md "../APIReference/API_Verify.md") within AWS KMS, or [download the public key](importing-keys-get-public-key-and-token.md "importing-keys-get-public-key-and-token.md") for
use outside of AWS KMS.

When you use an Edwards Curve key spec, AWS KMS creates an asymmetric KMS key with an
Ed25519 key pair for signing and verification. The private key that generates
signatures never leaves AWS KMS unencrypted. You can use the
public key to [verify signatures](../APIReference/API_Verify.md "../APIReference/API_Verify.md") within
AWS KMS, or [download the public
key](importing-keys-get-public-key-and-token.md "importing-keys-get-public-key-and-token.md") for use outside of AWS KMS.

AWS KMS supports the following ECC key specs for asymmetric KMS keys.

- Asymmetric NIST-standard elliptic curve key pairs (signing and verification
  -or- deriving shared secrets)
  - ECC_NIST_P256 (secp256r1)
  - ECC_NIST_P384 (secp384r1)
  - ECC_NIST_P521 (secp521r1)
  - ECC_NIST_EDWARDS25519 (ed25519) - signing and verification only
    - **Note:** For ECC_NIST_EDWARDS25519 KMS keys, the
      ED25519_SHA_512 signing algorithm requires [`MessageType:RAW`](../APIReference/API_Sign.md#KMS-Sign-request-MessageType "../APIReference/API_Sign.md#KMS-Sign-request-MessageType"), while ED25519_PH_SHA_512 requires [`MessageType:DIGEST`](../APIReference/API_Sign.md#KMS-Sign-request-MessageType "../APIReference/API_Sign.md#KMS-Sign-request-MessageType"). These message types cannot be used interchangeably.

- Other asymmetric elliptic curve key pairs (signing and verification)
  - ECC_SECG_P256K1 ([secp256k1](https://en.bitcoin.it/wiki/Secp256k1 "https://en.bitcoin.it/wiki/Secp256k1")), commonly used for cryptocurrencies.

The ECC key spec that you choose might be determined by your security standards or the
requirements of your task. In general, use the curve with the most points that is
practical and affordable for your task.

If you're creating an asymmetric KMS key to [derive shared secrets](../APIReference/API_DeriveSharedSecret.md "../APIReference/API_DeriveSharedSecret.md"), use
one of the NIST-standard elliptic curve key specs (except ECC_SECG_P256K1 and ECC_NIST_EDWARDS25519).
The only supported key agreement algorithm for deriving shared secrets is the [Elliptic Curve Cryptography Cofactor Diffie-Hellman Primitive](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Ar3.pdf#page=60 "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Ar3.pdf#page=60") (ECDH). For
an example of how to derive shared secrets offline, see [Deriving shared secrets offline](offline-operations.md#key-spec-ecc-offline "offline-operations.md#key-spec-ecc-offline").

If you're creating an asymmetric KMS key to use with cryptocurrencies, use the
ECC_SECG_P256K1 key spec. You can also use this key spec for other purposes, but it is
required for Bitcoin, and other cryptocurrencies.

The following table shows the signing algorithms that AWS KMS supports for each of the
ECC key specs. You cannot configure a KMS key to use particular signing algorithms.
However, you can use the [kms:SigningAlgorithm](conditions-kms.md#conditions-kms-signing-algorithm "conditions-kms.md#conditions-kms-signing-algorithm") policy condition to specify the signing algorithms that
principals are allowed to use with the KMS key.

| Supported signing algorithms for ECC key specs | Key spec           | Signing algorithm                                                                                                                                                                                                                                                                                     | Algorithm description |
| ---------------------------------------------- | ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| ECC_NIST_P256                                  | ECDSA_SHA_256      | NIST FIPS 186-4, Section 6.4, ECDSA signature using the curve<br>specified by the key and SHA-256 for the message digest.                                                                                                                                                                             |
| ECC_NIST_P384                                  | ECDSA_SHA_384      | NIST FIPS 186-4, Section 6.4, ECDSA signature using the curve<br>specified by the key and SHA-384 for the message digest.                                                                                                                                                                             |
| ECC_NIST_P521                                  | ECDSA_SHA_512      | NIST FIPS 186-4, Section 6.4, ECDSA signature using the curve<br>specified by the key and SHA-512 for the message digest.                                                                                                                                                                             |
| ECC_SECG_P256K1                                | ECDSA_SHA_256      | NIST FIPS 186-4, Section 6.4, ECDSA signature using the curve<br>specified by the key and SHA-256 for the message digest.                                                                                                                                                                             |
| ECC_NIST_EDWARDS25519                          | ED25519_SHA_512    | NIST FIPS 186-5, Section 7, EdDSA signature using the curve specified<br>by the key and SHA-512 for the message digest. KMS requires [`MessageType:RAW`](../APIReference/API_Sign.md#KMS-Sign-request-MessageType "../APIReference/API_Sign.md#KMS-Sign-request-MessageType") with this algorithm.    |
| ECC_NIST_EDWARDS25519                          | ED25519_PH_SHA_512 | NIST FIPS 186-5, Section 7, EdDSA signature using the curve<br>specified by the key and SHA-512 for the message digest. KMS requires [`MessageType:DIGEST`](../APIReference/API_Sign.md#KMS-Sign-request-MessageType "../APIReference/API_Sign.md#KMS-Sign-request-MessageType") with this algorithm. |

## Key specs for HMAC KMS keys

AWS KMS supports symmetric HMAC keys in varying lengths. The key spec that you select
can depend on your security, regulatory, or business requirements. The length of the key
determines the MAC algorithm that is used in [GenerateMac](../APIReference/API_GenerateMac.md "../APIReference/API_GenerateMac.md") and [VerifyMac](../APIReference/API_VerifyMac.md "../APIReference/API_VerifyMac.md") operations. In general,
longer keys are more secure. Use the longest key that is practical for your use
case.

| HMAC key spec | MAC algorithm |
| ------------- | ------------- |
| HMAC_224      | HMAC_SHA_224  |
| HMAC_256      | HMAC_SHA_256  |
| HMAC_384      | HMAC_SHA_384  |
| HMAC_512      | HMAC_SHA_512  |

## ML-DSA key specs

An ML-DSA key is a cryptographic key used in the Module-Lattice-Based Digital
Signature Algorithm (ML-DSA), which is designed for post-quantum cryptography. This
algorithm is part of the NIST (National Institute of Standards and Technology)
standardization effort, specifically outlined in [Federal Information Processing
Standards (FIPS) 204](https://csrc.nist.gov/pubs/fips/204/final "https://csrc.nist.gov/pubs/fips/204/final").

ML-DSA keys are used in a public-private key pair system. The private key is used for
signing data, while the public key is used for verifying the signature. This system
ensures the authenticity, integrity, and non-repudiation of digital messages or
documents, even in the face of potential quantum computer threats.

When you create a key with the ML-DSA key spec, AWS KMS creates an asymmetric KMS key
with a ML-DSA key pair for signing and verification. The private key that generates
signatures never leaves AWS KMS unencrypted. You can use the public key to [verify
signatures](../APIReference/API_Verify.md "../APIReference/API_Verify.md") within AWS KMS, or [download the public key](importing-keys-get-public-key-and-token.md "importing-keys-get-public-key-and-token.md") for use outside of AWS KMS.

AWS KMS supports the following ML-DSA key specs for asymmetric KMS keys:

- ML_DSA_44
- ML_DSA_65
- ML_DSA_87

AWS KMS supports the ML_DSA_SHAKE_256 signing algorithm for all of the ML-DSA key
specs.

## SM2 key spec (China Regions only)

The SM2 key spec is an elliptic curve key spec defined within the GM/T series of
specifications published by [China's Office of State Commercial
Cryptography Administration (OSCCA)](https://www.oscca.gov.cn/ "https://www.oscca.gov.cn/"). The SM2 key spec is available only in
China Regions. When you use the SM2 key spec, AWS KMS creates an asymmetric KMS key
with an SM2 key pair. You can use your SM2 key pair within AWS KMS, or download the public
key for use outside of AWS KMS. For more information, see [Offline verification with SM2 key pairs
(China Regions only)](offline-operations.md#key-spec-sm-offline-verification "offline-operations.md#key-spec-sm-offline-verification").

Each KMS key can have only one [Key usage](create-keys.md#key-usage "create-keys.md#key-usage"). You can use an SM2 KMS key for signing and verification, encryption and
decryption, _or_ deriving shared secrets. You must specify the key
usage when you create the KMS key, and you cannot change it after the key is
created.

If you're creating an asymmetric KMS key to [derive shared secrets](../APIReference/API_DeriveSharedSecret.md "../APIReference/API_DeriveSharedSecret.md"), use
the SM2 key spec. The only supported key agreement algorithm for deriving shared secrets
is the [Elliptic Curve Cryptography Cofactor Diffie-Hellman Primitive](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Ar3.pdf#page=60 "https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-56Ar3.pdf#page=60")
(ECDH).

AWS KMS supports the following SM2 encryption and signing algorithms:

- SM2PKE encryption algorithm

SM2PKE is an elliptic curve based encryption algorithm defined by
OSCCA in GM/T 0003.4-2012.

- SM2DSA signing algorithm

SM2DSA is an elliptic curve based signing algorithm defined by
OSCCA in GM/T 0003.2-2012. SM2DSA requires a distinguishing ID that
is hashed with the SM3 hashing algorithm and then combined with the
message, or message digest, that you passed to AWS KMS. This
concatenated value is then hashed and signed by AWS KMS.
