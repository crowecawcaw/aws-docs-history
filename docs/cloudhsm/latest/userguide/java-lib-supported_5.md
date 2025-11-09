# Supported mechanisms for JCE provider for AWS CloudHSM

Client SDK 5

This topic provides information about supported mechanisms for JCE provider with AWS CloudHSM Client SDK 5.
For information about the Java Cryptography Architecture (JCA) interfaces and engine classes
supported by AWS CloudHSM, see the following topics.

###### Topics

- [Generate key and key pair functions](#java-gen-key-pairs-5 "#java-gen-key-pairs-5")
- [Cipher functions](#java-ciphers_5 "#java-ciphers_5")
- [Sign and verify functions](#java-sign-verify_5 "#java-sign-verify_5")
- [Digest functions](#java-digests_5 "#java-digests_5")
- [Hash-based message authentication code (HMAC) functions](#java-mac_5 "#java-mac_5")
- [Cipher-based message authentication code (CMAC) functions](#java-cmac_5 "#java-cmac_5")
- [Key Agreement Functions](#java-key-derivation_5 "#java-key-derivation_5")
- [Convert keys to key specifications using key factories](#java-key-factories "#java-key-factories")
- [Mechanism annotations](#w20aac25c21c23c15c23 "#w20aac25c21c23c15c23")

## Generate key and key pair functions

The AWS CloudHSM software library for Java allows you to use the following operations for generate key and key pair functions.

- `RSA`
- `EC`
- `AES`
- `DESede (Triple DES)`see note [1](#java-gen-key-pairs-5-note-1 "#java-gen-key-pairs-5-note-1")
- `GenericSecret`

## Cipher functions

The AWS CloudHSM software library for Java supports the following algorithm, mode, and
padding combinations.

| Algorithm           | Mode | Padding                                                                                                                                                                                                                                                                                                                                            | Notes                                                                                                                                                                                                                                                                                                                             |
| ------------------- | ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AES                 | CBC  | `AES/CBC/NoPadding`<br>`AES/CBC/PKCS5Padding`                                                                                                                                                                                                                                                                                                      | Implements `Cipher.ENCRYPT_MODE` and `Cipher.DECRYPT_MODE`.<br>Implements `Cipher.UNWRAP_MODE for AES/CBC NoPadding`                                                                                                                                                                                                              |
| AES                 | ECB  | `AES/ECB/PKCS5Padding`<br>`AES/ECB/NoPadding`                                                                                                                                                                                                                                                                                                      | Implements `Cipher.ENCRYPT_MODE` and `Cipher.DECRYPT_MODE`.                                                                                                                                                                                                                                                                       |
| AES                 | CTR  | `AES/CTR/NoPadding`                                                                                                                                                                                                                                                                                                                                | Implements `Cipher.ENCRYPT_MODE` and<br>`Cipher.DECRYPT_MODE`.                                                                                                                                                                                                                                                                    |
| AES                 | GCM  | `AES/GCM/NoPadding`                                                                                                                                                                                                                                                                                                                                | Implements `Cipher.WRAP_MODE`, `Cipher.UNWRAP_MODE`, `Cipher.ENCRYPT_MODE`, and `Cipher.DECRYPT_MODE`.When performing<br>AES-GCM encryption, the HSM ignores the initialization vector (IV)<br>in the request and uses an IV that it generates. When the operation<br>completes, you must call `Cipher.getIV()` to get the<br>IV. |
| AESWrap             | ECB  | `AESWrap/ECB/NoPadding`<br>`AESWrap/ECB/PKCS5Padding`<br>`AESWrap/ECB/ZeroPadding`                                                                                                                                                                                                                                                                 | Implements `Cipher.WRAP_MODE` and `Cipher.UNWRAP_MODE`.                                                                                                                                                                                                                                                                           |
| DESede (Triple DES) | CBC  | `DESede/CBC/PKCS5Padding`<br>`DESede/CBC/NoPadding`                                                                                                                                                                                                                                                                                                | Implements `Cipher.ENCRYPT_MODE` and<br>`Cipher.DECRYPT_MODE`. See note [1](#java-gen-key-pairs-5-note-1 "#java-gen-key-pairs-5-note-1") below for an upcoming change.                                                                                                                                                            |
| DESede (Triple DES) | ECB  | `DESede/ECB/NoPadding`<br>`DESede/ECB/PKCS5Padding`                                                                                                                                                                                                                                                                                                | Implements `Cipher.ENCRYPT_MODE` and<br>`Cipher.DECRYPT_MODE`. See note [1](#java-gen-key-pairs-5-note-1 "#java-gen-key-pairs-5-note-1") below for an upcoming change.                                                                                                                                                            |
| RSA                 | ECB  | `RSA/ECB/PKCS1Padding` **see note [1](#java-gen-key-pairs-5-note-1 "#java-gen-key-pairs-5-note-1")**<br>`RSA/ECB/OAEPPadding`<br>`RSA/ECB/OAEPWithSHA-1ANDMGF1Padding`<br>`RSA/ECB/OAEPWithSHA-224ANDMGF1Padding`<br>`RSA/ECB/OAEPWithSHA-256ANDMGF1Padding`<br>`RSA/ECB/OAEPWithSHA-384ANDMGF1Padding`<br>`RSA/ECB/OAEPWithSHA-512ANDMGF1Padding` | Implements `Cipher.WRAP_MODE`, `Cipher.UNWRAP_MODE`, `Cipher.ENCRYPT_MODE`, and `Cipher.DECRYPT_MODE`.                                                                                                                                                                                                                            |
| RSA                 | ECB  | `RSA/ECB/NoPadding`                                                                                                                                                                                                                                                                                                                                | Implements `Cipher.ENCRYPT_MODE` and `Cipher.DECRYPT_MODE`.                                                                                                                                                                                                                                                                       |
| RSAAESWrap          | ECB  | `RSAAESWrap/ECB/OAEPPadding`<br>`RSAAESWrap/ECB/OAEPWithSHA-1ANDMGF1Padding`<br>`RSAAESWrap/ECB/OAEPWithSHA-224ANDMGF1Padding`<br>`RSAAESWrap/ECB/OAEPWithSHA-256ANDMGF1Padding`<br>`RSAAESWrap/ECB/OAEPWithSHA-384ANDMGF1Padding`<br>`RSAAESWrap/ECB/OAEPWithSHA-512ANDMGF1Padding`                                                               | Implements `Cipher.WRAP_MODE` and `Cipher.UNWRAP_MODE`.                                                                                                                                                                                                                                                                           |

## Sign and verify functions

The AWS CloudHSM software library for Java supports the following types of signature and
verification. With Client SDK 5 and signature algorithms with hashing, the data is hashed
locally in software before being sent to the HSM for the signature/verification. This means there
is no limit on the size of the data that can be hashed by the SDK.

**RSA Signature Types**

- `NONEwithRSA`
- `RSASSA-PSS`
- `SHA1withRSA`
- `SHA1withRSA/PSS`
- `SHA1withRSAandMGF1`
- `SHA224withRSA`
- `SHA224withRSAandMGF1`
- `SHA224withRSA/PSS`
- `SHA256withRSA`
- `SHA256withRSAandMGF1`
- `SHA256withRSA/PSS`
- `SHA384withRSA`
- `SHA384withRSAandMGF1`
- `SHA384withRSA/PSS`
- `SHA512withRSA`
- `SHA512withRSAandMGF1`
- `SHA512withRSA/PSS`

**ECDSA Signature Types**

- `NONEwithECDSA`
- `SHA1withECDSA`
- `SHA224withECDSA`
- `SHA256withECDSA`
- `SHA384withECDSA`
- `SHA512withECDSA`

## Digest functions

The AWS CloudHSM software library for Java supports the following message digests. With Client SDK 5,
the data is hashed locally in software. This means there
is no limit on the size of the data that can be hashed by the SDK.

- `SHA-1`
- `SHA-224`
- `SHA-256`
- `SHA-384`
- `SHA-512`

## Hash-based message authentication code (HMAC) functions

The AWS CloudHSM software library for Java supports the following HMAC algorithms.

- `HmacSHA1` (Maximum data size in bytes: 16288)
- `HmacSHA224` (Maximum data size in bytes: 16256)
- `HmacSHA256` (Maximum data size in bytes: 16288)
- `HmacSHA384` (Maximum data size in bytes: 16224)
- `HmacSHA512` (Maximum data size in bytes: 16224)

## Cipher-based message authentication code (CMAC) functions

CMACs (Cipher-based message authentication codes)
create message authentication codes (MACs) using a block cipher and a secret key. They differ from HMACs in that they use a block
symmetric key method for the MACs rather than a hashing method.

The AWS CloudHSM software library for Java supports the following CMAC algorithms.

- `AESCMAC`

## Key Agreement Functions

The AWS CloudHSM software library for Java supports ECDH with Key Derivation Functions (KDF). The following KDF types are supported:

- `ECDHwithX963SHA1KDF` Supports X9.63 KDF SHA1 algorithm[2](#kdf2 "#kdf2")
- `ECDHwithX963SHA224KDF` Supports X9.63 KDF SHA224 algorithm[2](#kdf2 "#kdf2")
- `ECDHwithX963SHA256KDF` Supports X9.63 KDF SHA256 algorithm[2](#kdf2 "#kdf2")
- `ECDHwithX963SHA384KDF` Supports X9.63 KDF SHA384 algorithm[2](#kdf2 "#kdf2")
- `ECDHwithX963SHA512KDF` Supports X9.63 KDF SHA512 algorithm[2](#kdf2 "#kdf2")

## Convert keys to key specifications using key factories

You can use key factories to convert keys to key specifications. AWS CloudHSM has two types of key factories for JCE:

**SecretKeyFactory:** Used to import or derive symmetric keys. Using SecretKeyFactory,
you can pass a supported Key or a supported KeySpec to import or derive symmetric keys into AWS CloudHSM. Following are the supported specs for KeyFactory:

- For SecretKeyFactory's `generateSecret` method following [KeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/KeySpec.html "https://docs.oracle.com/javase/8/docs/api/java/security/spec/KeySpec.html") classes are supported:
  - **KeyAttributesMap**can be used to import a key bytes with additional attributes as a CloudHSM Key. An example can be found here
    [here](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/sdk5/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/sdk5/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java").
  - **[SecretKeySpec](https://docs.oracle.com/javase/8/docs/api/javax/crypto/spec/SecretKeySpec.html "https://docs.oracle.com/javase/8/docs/api/javax/crypto/spec/SecretKeySpec.html")**can be used to
    import a symmetric key spec as a CloudHSM Key.
  - **AesCmacKdfParameterSpec**can be used to derive symmetric keys using another CloudHSM AES Key.

###### Note

SecretKeyFactory's `translateKey` method takes any key that implements the [key](https://docs.oracle.com/javase/8/docs/api/java/security/Key.html "https://docs.oracle.com/javase/8/docs/api/java/security/Key.html") interface.

**KeyFactory:** Used for importing asymmetric keys. Using KeyFactory, you can pass a supported Key or supported KeySpec to
import an asymmetric key into AWS CloudHSM. For more information, refer to the following resources:

- For KeyFactory's `generatePublic` method, following [KeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/KeySpec.html "https://docs.oracle.com/javase/8/docs/api/java/security/spec/KeySpec.html") classes are supported:
- CloudHSM KeyAttributesMap for both RSA and EC KeyTypes, including:
  - CloudHSM KeyAttributesMap for both RSA and EC public KeyTypes. An example can be found
    [here](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/sdk5/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/sdk5/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java")
  - [X509EncodedKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/X509EncodedKeySpec.html "https://docs.oracle.com/javase/8/docs/api/java/security/spec/X509EncodedKeySpec.html") for both RSA and EC Public Key
  - [RSAPublicKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/RSAPublicKeySpec.html "https://docs.oracle.com/javase/8/docs/api/java/security/spec/RSAPublicKeySpec.html") for RSA Public Key
  - [ECPublicKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/ECPublicKeySpec.html "https://docs.oracle.com/javase/8/docs/api/java/security/spec/ECPublicKeySpec.html") for EC Public Key

- For KeyFactory's `generatePrivate` method, following [KeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/KeySpec.html "https://docs.oracle.com/javase/8/docs/api/java/security/spec/KeySpec.html") classes are supported:
- CloudHSM KeyAttributesMap for both RSA and EC KeyTypes, including:
  - CloudHSM KeyAttributesMap for both RSA and EC public KeyTypes. An example can be found
    [here](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/sdk5/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/sdk5/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java")
  - [PKCS8EncodedKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/PKCS8EncodedKeySpec.html "https://docs.oracle.com/javase/8/docs/api/java/security/spec/PKCS8EncodedKeySpec.html") for both EC and RSA Private Key
  - [RSAPrivateCrtKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/RSAPrivateCrtKeySpec.html "https://docs.oracle.com/javase/8/docs/api/java/security/spec/RSAPrivateCrtKeySpec.html") for RSA Private Key
  - [ECPrivateKeySpec](https://docs.oracle.com/javase/8/docs/api/java/security/spec/ECPrivateKeySpec.html "https://docs.oracle.com/javase/8/docs/api/java/security/spec/ECPrivateKeySpec.html") for EC Private Key

For KeyFactory's `translateKey` method, it takes in any Key that implements the [Key Interface](https://docs.oracle.com/javase/8/docs/api/java/security/Key.html "https://docs.oracle.com/javase/8/docs/api/java/security/Key.html").

## Mechanism annotations

[1] In accordance with NIST guidance, this is disallowed for clusters in FIPS mode after 2023. For clusters in non-FIPS mode, it is still allowed after 2023. See [FIPS 140 Compliance: 2024 Mechanism Deprecation](compliance-dep-notif.md#compliance-dep-notif-1 "compliance-dep-notif.md#compliance-dep-notif-1") for details.

[2] Key derivation functions (KDFs) are specified in [RFC 8418, Section 2.1](https://datatracker.ietf.org/doc/html/rfc8418 "https://datatracker.ietf.org/doc/html/rfc8418").
