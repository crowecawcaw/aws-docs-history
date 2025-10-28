# Supported mechanisms for Client SDK 3 for AWS CloudHSM

Client SDK 3

This topic provides information about supported mechanisms for JCE provider with AWS CloudHSM Client SDK 3.
For information about the Java Cryptography Architecture (JCA) interfaces and engine classes
supported by AWS CloudHSM, see the following topics.

###### Topics

- [Supported keys](#java-keys "#java-keys")
- [Supported ciphers](#java-ciphers "#java-ciphers")
- [Supported digests](#java-digests "#java-digests")
- [Supported hash-based message authentication code (HMAC)
  algorithms](#java-mac "#java-mac")
- [Supported sign/verify mechanisms](#java-sign-verify "#java-sign-verify")
- [Mechanism annotations](#w20aac25c23c25c11c17 "#w20aac25c23c25c11c17")

## Supported keys

The AWS CloudHSM software library for Java enables you to generate the following key
types.

- AES – 128, 192, and 256-bit AES keys.
- DESede – 92 bit 3DES key. See note [1](#java-keys-note-1 "#java-keys-note-1") below for an upcoming change.
- ECC key pairs for NIST curves secp256r1 (P-256), secp384r1 (P-384), and secp256k1
  (Blockchain).
- RSA – 2048-bit to 4096-bit RSA keys, in increments of 256 bits.

In addition to standard parameters, we support the following parameters for each key
that is generated.

- **Label**: A key label that you can use to search
  for keys.
- **isExtractable**: Indicates whether the key can
  be exported from the HSM.
- **isPersistent**: Indicates whether the key
  remains on the HSM when the current session ends.

###### Note

Java library version 3.1 provides the ability to specify parameters in greater detail. For
more information, see [Supported Java
Attributes](java-lib-attributes.md "java-lib-attributes.md").

## Supported ciphers

The AWS CloudHSM software library for Java supports the following algorithm, mode, and
padding combinations.

| Algorithm           | Mode | Padding                                                                                                                                                                                                                     | Notes                                                                                                                                                                                                                                                                                                                    |
| ------------------- | ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AES                 | CBC  | `AES/CBC/NoPadding` `AES/CBC/PKCS5Padding`                                                                                                                                                                                  | Implements `Cipher.ENCRYPT_MODE` and `Cipher.DECRYPT_MODE`.                                                                                                                                                                                                                                                              |
| AES                 | ECB  | `AES/ECB/NoPadding` `AES/ECB/PKCS5Padding`                                                                                                                                                                                  | Implements `Cipher.ENCRYPT_MODE` and `Cipher.DECRYPT_MODE`. Use Transformation AES.                                                                                                                                                                                                                                      |
| AES                 | CTR  | `AES/CTR/NoPadding`                                                                                                                                                                                                         | Implements `Cipher.ENCRYPT_MODE` and `Cipher.DECRYPT_MODE`.                                                                                                                                                                                                                                                              |
| AES                 | GCM  | `AES/GCM/NoPadding`                                                                                                                                                                                                         | Implements `Cipher.ENCRYPT_MODE` and `Cipher.DECRYPT_MODE`, `Cipher.WRAP_MODE`, and `Cipher.UNWRAP_MODE`.When performing AES-GCM encryption, the HSM ignores the initialization vector (IV) in the request and uses an IV that it generates. When the operation completes, you must call `Cipher.getIV()` to get the IV. |
| AESWrap             | ECB  | `AESWrap/ECB/ZeroPadding` `AESWrap/ECB/NoPadding` `AESWrap/ECB/PKCS5Padding`                                                                                                                                                | Implements `Cipher.WRAP_MODE`, and `Cipher.UNWRAP_MODE`. Use Transformation AES.                                                                                                                                                                                                                                         |
| DESede (Triple DES) | CBC  | `DESede/CBC/NoPadding` `DESede/CBC/PKCS5Padding`                                                                                                                                                                            | Implements `Cipher.ENCRYPT_MODE` and `Cipher.DECRYPT_MODE`. The key generation routines accept a size of 168 or 192 bits. However, internally, all DESede keys are 192 bits. See note [1](#java-keys-note-1 "#java-keys-note-1") below for an upcoming change.                                                           |
| DESede (Triple DES) | ECB  | `DESede/ECB/NoPadding``DESede/ECB/PKCS5Padding`                                                                                                                                                                             | Implements `Cipher.ENCRYPT_MODE` and `Cipher.DECRYPT_MODE`. The key generation routines accept a size of 168 or 192 bits. However, internally, all DESede keys are 192 bits. See note [1](#java-keys-note-1 "#java-keys-note-1") below for an upcoming change.                                                           |
| RSA                 | ECB  | `RSA/ECB/NoPadding``RSA/ECB/PKCS1Padding`                                                                                                                                                                                   | Implements `Cipher.ENCRYPT_MODE` and `Cipher.DECRYPT_MODE`. See note [1](#java-keys-note-1 "#java-keys-note-1") below for an upcoming change.                                                                                                                                                                            |
| RSA                 | ECB  | `RSA/ECB/OAEPPadding` `RSA/ECB/OAEPWithSHA-1ANDMGF1Padding` `RSA/ECB/OAEPWithSHA-224ANDMGF1Padding` `RSA/ECB/OAEPWithSHA-256ANDMGF1Padding` `RSA/ECB/OAEPWithSHA-384ANDMGF1Padding` `RSA/ECB/OAEPWithSHA-512ANDMGF1Padding` | Implements `Cipher.ENCRYPT_MODE`, `Cipher.DECRYPT_MODE`, `Cipher.WRAP_MODE`, and `Cipher.UNWRAP_MODE`. `OAEPPadding` is `OAEP` with the `SHA-1` padding type.                                                                                                                                                            |
| RSAAESWrap          | ECB  | `OAEPPADDING`                                                                                                                                                                                                               | Implements `Cipher.WRAP_Mode` and `Cipher.UNWRAP_MODE`.                                                                                                                                                                                                                                                                  | ## Supported digests The AWS CloudHSM software library for Java supports the following message digests. <br>• `SHA-1` <br>• `SHA-224` <br>• `SHA-256` <br>• `SHA-384` <br>• `SHA-512` ###### Note Data under 16 KB in length are hashed on the HSM, while larger data are hashed locally in software. ## Supported hash-based message authentication code (HMAC) algorithms The AWS CloudHSM software library for Java supports the following HMAC algorithms. <br>• `HmacSHA1` <br>• `HmacSHA224` <br>• `HmacSHA256` <br>• `HmacSHA384` <br>• `HmacSHA512` ## Supported sign/verify mechanisms The AWS CloudHSM software library for Java supports the following types of signature and verification. **RSA Signature Types** <br>• `NONEwithRSA` <br>• `SHA1withRSA` <br>• `SHA224withRSA` <br>• `SHA256withRSA` <br>• `SHA384withRSA` <br>• `SHA512withRSA` <br>• `SHA1withRSA/PSS` <br>• `SHA224withRSA/PSS` <br>• `SHA256withRSA/PSS` <br>• `SHA384withRSA/PSS` <br>• `SHA512withRSA/PSS` **ECDSA Signature Types** <br>• `NONEwithECDSA` <br>• `SHA1withECDSA` <br>• `SHA224withECDSA` <br>• `SHA256withECDSA` <br>• `SHA384withECDSA` <br>• `SHA512withECDSA` ## Mechanism annotations [1] In accordance with NIST guidance, this is disallowed for clusters in FIPS mode after 2023. For clusters in non-FIPS mode, it is still allowed after 2023. See [FIPS 140 Compliance: 2024 Mechanism Deprecation](compliance-dep-notif.md#compliance-dep-notif-1 "compliance-dep-notif.md#compliance-dep-notif-1") for details. |
