# AWS CloudHSM deprecated Client SDK releases

Versions 5.8.0 and earlier are deprecated. We do not recommend using deprecated
releases in
production workloads. We do not provide backwards compatible updates for deprecated
releases, nor do we host deprecated releases for download. If you experience production
impact while using deprecated releases, you must upgrade to obtain software fixes.

## Deprecated Client SDK 5 releases

This section lists deprecated Client SDK 5 releases.

Version 5.8.0 introduces quorum authentication for CloudHSM CLI, SSL/TLS
offload with JSSE, multi-slot support for PKCS #11,
multi-cluster/multi-user support for JCE, key extraction with JCE, supported
keyFactory for JCE, new retry configurations for non-terminal return codes,
and
includes improved stability and bug fixes for all SDKs.

###### PKCS #11 library

- Added support for multi-slot configuration.

###### JCE provider

- Added configuration based key extraction.
- Added support for multi-cluster and multi-user configurations.
- Added support for SSL and TLS offload with JSSE.
- Added unwrap support for AES/CBC/NoPadding.
- Added new types of key factories: SecretKeyFactory and KeyFactory.

###### CloudHSM CLI

- Added support for quorum authentication
  Version 5.7.0 introduces CloudHSM CLI and includes a new cipher-based
  message authentication code (CMAC) algorithm. This release adds ARM
  architecture on Amazon Linux 2. JCE provider Javadocs are now available for AWS CloudHSM.

###### PKCS #11 library

- Improved stability and bug fixes.
- Now supported on ARM architecture with Amazon Linux 2.
- Algorithms
  - CKM_AES_CMAC (sign and verify)

###### OpenSSL Dynamic Engine

- Improved stability and bug fixes.
- Now supported on ARM architecture with Amazon Linux 2.

###### JCE provider

- Improved stability and bug fixes.
- Algorithms

      + AESCMAC

  Version 5.6.0 includes new mechanism support for PKCS #11 library and JCE provider.
  Additionally, version 5.6 supports Ubuntu 20.04.

###### PKCS #11 library

- Improved stability and bug fixes.
- Mechanisms
  - CKM_RSA_X_509, for encrypt, decrypt, sign, and verify
    modes

###### OpenSSL Dynamic Engine

- Improved stability and bug fixes.

###### JCE provider

- Improved stability and bug fixes.
- Ciphers
  - RSA/ECB/NoPadding, for encrypt and decrypt modes

###### Supported keys

- EC with curves secp224r1 and secp521r1

###### Platform support

- Added support for Ubuntu 20.04.
  Version 5.5.0 adds support for OpenJDK 11, Keytool and Jarsigner
  integration, and additional mechanisms to the JCE provider. Resolves a [known issue](ki-jce-sdk.md#ki-jce-6 "ki-jce-sdk.md#ki-jce-6") regarding
  a KeyGenerator class incorrectly interpreting key size parameter as number
  of bytes instead of bits.

###### PKCS #11 library

- Improved stability and bug fixes.

###### OpenSSL Dynamic Engine

- Improved stability and bug fixes.

###### JCE provider

- Support for the Keytool and Jarsigner utilities
- Support for OpenJDK 11 on all platforms
- Ciphers
  - AES/CBC/NoPadding Encrypt and Decrypt mode
  - AES/ECB/PKCS5Padding Encrypt and Decrypt mode
  - AES/CTR/NoPadding Encrypt and Decrypt mode
  - AES/GCM/NoPadding Wrap and Unwrap mode
  - DESede/ECB/PKCS5Padding Encrypt and Decrypt mode
  - DESede/CBC/NoPadding Encrypt and Decrypt mode
  - AESWrap/ECB/NoPadding Wrap and Unwrap mode
  - AESWrap/ECB/PKCS5Padding Wrap and Unwrap mode
  - AESWrap/ECB/ZeroPadding Wrap and Unwrap mode
  - RSA/ECB/PKCS1Padding Wrap and Unwrap mode
  - RSA/ECB/OAEPPadding Wrap and Unwrap mode
  - RSA/ECB/OAEPWithSHA-1ANDMGF1Padding Wrap and Unwrap mode
  - RSA/ECB/OAEPWithSHA-224ANDMGF1Padding Wrap and Unwrap mode
  - RSA/ECB/OAEPWithSHA-256ANDMGF1Padding Wrap and Unwrap mode
  - RSA/ECB/OAEPWithSHA-384ANDMGF1Padding Wrap and Unwrap mode
  - RSA/ECB/OAEPWithSHA-512ANDMGF1Padding Wrap and Unwrap mode
  - RSAAESWrap/ECB/OAEPPadding Wrap and Unwrap mode
  - RSAAESWrap/ECB/OAEPWithSHA-1ANDMGF1Padding Wrap and Unwrap
    mode
  - RSAAESWrap/ECB/OAEPWithSHA-224ANDMGF1Padding Wrap and
    Unwrap mode
  - RSAAESWrap/ECB/OAEPWithSHA-256ANDMGF1Padding Wrap and
    Unwrap mode
  - RSAAESWrap/ECB/OAEPWithSHA-384ANDMGF1Padding Wrap and
    Unwrap mode
  - RSAAESWrap/ECB/OAEPWithSHA-512ANDMGF1Padding Wrap and
    Unwrap mode

- KeyFactory and SecretKeyFactory
  - RSA – 2048-bit to 4096-bit RSA keys, in increments of 256
    bits
  - AES – 128, 192, and 256-bit AES keys
  - EC key pairs for NIST curves secp256r1 (P-256), secp384r1
    (P-384), and secp256k1
  - DESede (3DES)
  - GenericSecret
  - HMAC – with SHA1, SHA224, SHA256, SHA384, SHA512 hash
    support

- Sign/Verify

      + RSASSA-PSS
      + SHA1withRSA/PSS
      + SHA224withRSA/PSS
      + SHA256withRSA/PSS
      + SHA384withRSA/PSS
      + SHA512withRSA/PSS
      + SHA1withRSAandMGF1
      + SHA224withRSAandMGF1
      + SHA256withRSAandMGF1
      + SHA384withRSAandMGF1
      + SHA512withRSAandMGF1

  Version 5.4.2 includes improved stability and bug fixes for all SDKs. This
  is also the last release for the CentOS 8 platform. For more information,
  see the [CentOS website](https://www.centos.org/centos-linux-eol/ "https://www.centos.org/centos-linux-eol/")
  .

###### PKCS #11 library

- Improved stability and bug fixes.

###### OpenSSL Dynamic Engine

- Improved stability and bug fixes.

###### JCE provider

- Improved stability and bug fixes.
  Version 5.4.1 resolves a [known issue](ki-pkcs11-sdk.md#ki-pkcs11-14 "ki-pkcs11-sdk.md#ki-pkcs11-14")
  with the PKCS #11 library. This is also the last release for the CentOS 8 platform.
  For more information, see the [CentOS website](https://www.centos.org/centos-linux-eol/ "https://www.centos.org/centos-linux-eol/").

###### PKCS #11 library

- Improved stability and bug fixes.

###### OpenSSL Dynamic Engine

- Improved stability and bug fixes.

###### JCE provider

- Improved stability and bug fixes.
  Version 5.4.0 adds initial support for the JCE provider for all platforms. The
  JCE provider is compatible with OpenJDK 8.

###### PKCS #11 library

- Improved stability and bug fixes.

###### OpenSSL Dynamic Engine

- Improved stability and bug fixes.

###### JCE provider

- ###### Key types
  - RSA – 2048-bit to 4096-bit RSA keys, in
    increments of 256 bits.
  - AES – 128, 192, and 256-bit AES keys.
  - ECC key pairs for NIST curves secp256r1
    (P-256), secp384r1 (P-384), and secp256k1.
  - DESede (3DES)
  - HMAC – with SHA1, SHA224, SHA256, SHA384, SHA512
    hash support.

- ###### Ciphers (encrypt and decrypt only)
  - AES/GCM/NoPadding
  - AES/ECB/NoPadding
  - AES/CBC/PKCS5Padding
  - DESede/ECB/NoPadding
  - DESede/CBC/PKCS5Padding
  - AES/CTR/NoPadding
  - RSA/ECB/PKCS1Padding
  - RSA/ECB/OAEPPadding
  - RSA/ECB/OAEPWithSHA-1ANDMGF1Padding
  - RSA/ECB/OAEPWithSHA-224ANDMGF1Padding
  - RSA/ECB/OAEPWithSHA-256ANDMGF1Padding
  - RSA/ECB/OAEPWithSHA-384ANDMGF1Padding
  - RSA/ECB/OAEPWithSHA-512ANDMGF1Padding

- ###### Digests
  - SHA-1
  - SHA-224
  - SHA-256
  - SHA-384
  - SHA-512

- ###### Sign/Verify
  - NONEwithRSA
  - SHA1withRSA
  - SHA224withRSA
  - SHA256withRSA
  - SHA384withRSA
  - SHA512withRSA
  - NONEwithECDSA
  - SHA1withECDSA
  - SHA224withECDSA
  - SHA256withECDSA
  - SHA384withECDSA
  - SHA512withECDSA

- Integration with the Java KeyStore

**PKCS #11 library**

- Improved stability and bug fixes.

**OpenSSL Dynamic Engine**

- Add support for ECDSA sign/verify with curves P-256, P-384, and
  secp256k1.
- Add support for the platforms: Amazon Linux, Amazon Linux 2, CentOS 7.8+, RHEL 7 (7.8+).
- Add support for OpenSSL version 1.0.2.
- Improved stability and bug fixes.

###### JCE provider

- ###### Key types
  - RSA – 2048-bit to 4096-bit RSA keys, in
    increments of 256 bits.
  - AES – 128, 192, and 256-bit AES keys.
  - EC key pairs for NIST curves secp256r1
    (P-256), secp384r1 (P-384), and secp256k1.
  - DESede (3DES)
  - HMAC – with SHA1, SHA224, SHA256, SHA384, SHA512
    hash support.

- ###### Ciphers (encrypt and decrypt only)
  - AES/GCM/NoPadding
  - AES/ECB/NoPadding
  - AES/CBC/PKCS5Padding
  - DESede/ECB/NoPadding
  - DESede/CBC/PKCS5Padding
  - AES/CTR/NoPadding
  - RSA/ECB/PKCS1Padding
  - RSA/ECB/OAEPPadding
  - RSA/ECB/OAEPWithSHA-1ANDMGF1Padding
  - RSA/ECB/OAEPWithSHA-224ANDMGF1Padding
  - RSA/ECB/OAEPWithSHA-256ANDMGF1Padding
  - RSA/ECB/OAEPWithSHA-384ANDMGF1Padding
  - RSA/ECB/OAEPWithSHA-512ANDMGF1Padding

- ###### Digests
  - SHA-1
  - SHA-224
  - SHA-256
  - SHA-384
  - SHA-512

- ###### Sign/Verify
  - NONEwithRSA
  - SHA1withRSA
  - SHA224withRSA
  - SHA256withRSA
  - SHA384withRSA
  - SHA512withRSA
  - NONEwithECDSA
  - SHA1withECDSA
  - SHA224withECDSA
  - SHA256withECDSA
  - SHA384withECDSA
  - SHA512withECDSA

- Integration with the Java KeyStore

**PKCS #11 library**

- Improved stability and bug fixes.

**OpenSSL Dynamic Engine**

- Improved stability and bug fixes.
  Version 5.2.0 adds support additional key types and mechanisms to the
  PKCS #11 library.

**PKCS #11 library**

Key Types

- ECDSA– P-224, P-256, P-384, P-521 and secp256k1 curves
- Triple DES (3DES)
  Mechanisms

- CKM_EC_KEY_PAIR_GEN
- CKM_DES3_KEY_GEN
- CKM_DES3_CBC
- CKM_DES3_CBC_PAD
- CKM_DES3_ECB
- CKM_ECDSA
- CKM_ECDSA_SHA1
- CKM_ECDSA_SHA224
- CKM_ECDSA_SHA256
- CKM_ECDSA_SHA384
- CKM_ECDSA_SHA512
- CKM_RSA_PKCS for Encrypt/Decrypt

**OpenSSL Dynamic Engine**

- Improved stability and bug fixes.
  Version 5.1.0 adds support for additional mechanisms to the PKCS #11 library.

**PKCS #11 library**

Mechanisms

- CKM_RSA_PKCS for Wrap/Unwrap
- CKM_RSA_PKCS_PSS
- CKM_SHA1_RSA_PKCS_PSS
- CKM_SHA224_RSA_PKCS_PSS
- CKM_SHA256_RSA_PKCS_PSS
- CKM_SHA384_RSA_PKCS_PSS
- CKM_SHA512_RSA_PKCS_PSS
- CKM_AES_ECB
- CKM_AES_CTR
- CKM_AES_CBC
- CKM_AES_CBC_PAD
- CKM_SP800_108_COUNTER_KDF
- CKM_GENERIC_SECRET_KEY_GEN
- CKM_SHA_1_HMAC
- CKM_SHA224_HMAC
- CKM_SHA256_HMAC
- CKM_SHA384_HMAC
- CKM_SHA512_HMAC
- CKM_RSA_PKCS_OAEP Wrap/Unwrap only
- CKM_RSA_AES_KEY_WRAP
- CKM_CLOUDHSM_AES_KEY_WRAP_NO_PAD
- CKM_CLOUDHSM_AES_KEY_WRAP_PKCS5_PAD
- CKM_CLOUDHSM_AES_KEY_WRAP_ZERO_PAD
  API Operations

- C_CreateObject
- C_DeriveKey
- C_WrapKey
- C_UnWrapKey

**OpenSSL Dynamic Engine**

- Improved stability and bug fixes.
  Version 5.0.1 adds initial support for OpenSSL Dynamic Engine.

**PKCS #11 library**

- Improved stability and bug fixes.

**OpenSSL Dynamic Engine**

- Initial release of OpenSSL Dynamic Engine.
- This release offers introductory support for key types and OpenSSL
  APIs:

      + RSA key generation for 2048, 3072, and 4096-bit keys
      + OpenSSL APIs:




      	- [RSA
      	 Sign](https://www.openssl.org/docs/man1.1.1/man3/EVP_DigestSignInit.html "https://www.openssl.org/docs/man1.1.1/man3/EVP_DigestSignInit.html") using RSA PKCS with
      	 SHA1/224/256/384/512 & RSA PSS
      	- [RSA
      	 Key Generation](https://www.openssl.org/docs/man1.1.1/man1/genrsa.html "https://www.openssl.org/docs/man1.1.1/man1/genrsa.html")

  For more information, see [OpenSSL Dynamic Engine](openssl-library.md "openssl-library.md")
  .

- Platforms supported: CentOS 8.3+, Red Hat Enterprise Linux (RHEL)
  8.3+,
  and Ubuntu 18.04 LTS

      + Requires: OpenSSL 1.1.1

  For more information, see [Supported Platforms](client-supported-platforms.md "client-supported-platforms.md").

- Support for SSL/TLS Offload on CentOS 8.3+, Red Hat Enterprise
  Linux
  (RHEL) 8.3, and Ubuntu 18.04 LTS, including NGINX 1.19 (for select
  cipher
  suites).

For more information, see [SSL/TLS
Offload
on Linux using Tomcat](third-offload-linux-jsse.md "third-offload-linux-jsse.md") or [SSL/TLS Offload
on Linux using NGINX or Apache](third-offload-linux-openssl.md "third-offload-linux-openssl.md").
Version 5.0.0 is the first release.

**PKCS #11 library**

- This is the initial release.

#### Introductory PKCS #11 library

support in client SDK version 5.0.0

This section details support for key types, mechanisms, API operations
and
attributes Client SDK version 5.0.0.

**Key Types**:

- **AES**– 128, 192, and 256-bit
  AES keys
- **RSA**– 2048-bit to 4096-bit RSA
  keys, in increments of 256 bits

**Mechanisms**:

- CKM_AES_GCM
- CKM_AES_KEY_GEN
- CKM_CLOUDHSM_AES_GCM
- CKM_RSA_PKCS
- CKM_RSA_X9_31_KEY_PAIR_GEN
- CKM_SHA1
- CKM_SHA1_RSA_PKCS
- CKM_SHA224
- CKM_SHA224_RSA_PKCS
- CKM_SHA256
- CKM_SHA256_RSA_PKCS
- CKM_SHA384
- CKM_SHA384_RSA_PKCS
- CKM_SHA512
- CKM_SHA512_RSA_PKCS

[Show moreShow less](# "#")
**API Operations**:

- C_CloseAllSessions
- C_CloseSession
- C_Decrypt
- C_DecryptFinal
- C_DecryptInit
- C_DecryptUpdate
- C_DestroyObject
- C_Digest
- C_DigestFinal
- C_DigestInit
- C_DigestUpdate
- C_Encrypt
- C_EncryptFinal
- C_EncryptInit
- C_EncryptUpdate
- C_Finalize
- C_FindObjects
- C_FindObjectsFinal
- C_FindObjectsInit
- C_GenerateKey
- C_GenerateKeyPair
- C_GenerateRandom
- C_GetAttributeValue
- C_GetFunctionList
- C_GetInfo
- C_GetMechanismInfo
- C_GetMechanismList
- C_GetSessionInfo
- C_GetSlotInfo
- C_GetSlotList
- C_GetTokenInfo
- C_Initialize
- C_Login
- C_Logout
- C_OpenSession
- C_Sign
- C_SignFinal
- C_SignInit
- C_SignUpdate
- C_Verify
- C_VerifyFinal
- C_VerifyInit
- C_VerifyUpdate

[Show moreShow less](# "#")
**Attributes**:

- GenerateKeyPair
  - All RSA Key attributes

- GenerateKey
  - All AES Key attributes

- GetAttributeValue
  - All RSA Key attributes
  - All AES Key attributes

**Samples**:

- [Generate
  keys (AES, RSA, EC)](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/generate "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/generate")
- [List
  key attributes](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/attributes/ "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/attributes/")
- [Encrypt
  and decrypt data with AES GCM](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/encrypt/aes_gcm.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/encrypt/aes_gcm.c")
- [Sign
  and verify data with RSA](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/sign/rsa_sign.c "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples/blob/master/src/sign/rsa_sign.c")

## Deprecated Client SDK 3 releases

This section lists deprecated Client SDK 3 releases.

Version 3.4.4 adds updates to JCE provider.

**AWS CloudHSM Client Software**

- Updated the version for consistency.

**PKCS #11 library**

- Updated the version for consistency.

**OpenSSL Dynamic Engine**

- Updated the version for consistency.

**JCE provider**

- Update log4j to version 2.17.1.

**Windows (CNG and KSP providers)**

- Updated the version for consistency.
  Version 3.4.3 adds updates to JCE provider.

**AWS CloudHSM Client Software**

- Updated the version for consistency.

**PKCS #11 library**

- Updated the version for consistency.

**OpenSSL Dynamic Engine**

- Updated the version for consistency.

**JCE provider**

- Update log4j to version 2.17.0.

**Windows (CNG and KSP providers)**

- Updated the version for consistency.
  Version 3.4.2 adds updates to JCE provider.

**AWS CloudHSM Client Software**

- Updated the version for consistency.

**PKCS #11 library**

- Updated the version for consistency.

**OpenSSL Dynamic Engine**

- Updated the version for consistency.

**JCE provider**

- Update log4j to version 2.16.0.

**Windows (CNG and KSP providers)**

- Updated the version for consistency.
  Version 3.4.1 adds updates to JCE provider.

**AWS CloudHSM Client Software**

- Updated the version for consistency.

**PKCS #11 library**

- Updated the version for consistency.

**OpenSSL Dynamic Engine**

- Updated the version for consistency.

**JCE provider**

- Update log4j to version 2.15.0.

**Windows (CNG and KSP providers)**

- Updated the version for consistency.
  Version 3.4.0 adds updates to all components.

**AWS CloudHSM Client Software**

- Improved stability and bug fixes.

**PKCS #11 library**

- Improved stability and bug fixes.

**OpenSSL Dynamic Engine**

- Improved stability and bug fixes.

**JCE provider**

- Improved stability and bug fixes.

**Windows (CNG and KSP providers)**

- Improved stability and bug fixes.
  Version 3.3.2 resolves an [issue](ki-all.md#ki-all-9 "ki-all.md#ki-all-9") with the client_info script.

**AWS CloudHSM Client Software**

- Updated the version for consistency.

**PKCS #11 library**

- Updated the version for consistency.

**OpenSSL Dynamic Engine**

- Updated the version for consistency.

**JCE provider**

- Updated the version for consistency.

**Windows (CNG and KSP providers)**

- Updated the version for consistency.
  Version 3.3.1 adds updates to all components.

**AWS CloudHSM Client Software**

- Improved stability and bug fixes.

**PKCS #11 library**

- Improved stability and bug fixes.

**OpenSSL Dynamic Engine**

- Improved stability and bug fixes.

**JCE provider**

- Improved stability and bug fixes.

**Windows (CNG and KSP providers)**

- Improved stability and bug fixes.
  Version 3.3.0 adds two-factor authentication (2FA) and other
  improvements.

**AWS CloudHSM Client Software**

- Added 2FA authentication for crypto officers (CO). For more
  information, see [Managing Two-Factor
  Authentication for Crypto
  Officers](manage-2fa.md "manage-2fa.md").
- Removed platform support for RedHat Enterprise Linux 6 and CentOS

6.  For more information, see [Linux
    Support](sdk3-linux.md "sdk3-linux.md").

- Added a standalone version of CMU for use with Client SDK 5 or
  Client SDK 3.
  This is the same version of CMU included with the client daemon of
  version
  3.3.0, and now you can download CMU without downloading the client
  daemon.

**PKCS #11 library**

- Improved stability and bug fixes.
- Removed platform support for RedHat Enterprise Linux 6 and CentOS

6.  For more information, see [Linux
    Support](sdk3-linux.md "sdk3-linux.md").

**OpenSSL Dynamic Engine**

- Updated the version for consistency
- Removed platform support for RedHat Enterprise Linux 6 and CentOS

6.  For more information, see [Linux
    Support](sdk3-linux.md "sdk3-linux.md").

**JCE provider**

- Improved stability and bug fixes.
- Removed platform support for RedHat Enterprise Linux 6 and CentOS

6.  For more information, see [Linux
    Support](sdk3-linux.md "sdk3-linux.md").

**Windows (CNG and KSP providers)**

- Updated the version for consistency
  Version 3.2.1 adds a compliance analysis between the AWS CloudHSM implementation
  of the PKCS #11 library and
  the PKCS #11 standard, new platforms, and other improvements.

**AWS CloudHSM Client Software**

- Add platform support for CentOS 8, RHEL 8, and Ubuntu 18.04 LTS.
  For more information, see [AWS CloudHSM Client SDK 5 supported platforms](client-supported-platforms.md "client-supported-platforms.md")
  .

**PKCS #11 library**

- [PKCS #11 library
  compliance report for client SDK 3.2.1](https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/PKCS11ComplianceReportSDK3-2-1.pdf "https://s3.amazonaws.com/cloudhsmv2-software/CloudHsmClient/Docs/PKCS11ComplianceReportSDK3-2-1.pdf")
- Add platform support for CentOS 8, RHEL 8, and Ubuntu 18.04 LTS.
  For more information, see [AWS CloudHSM Client SDK 5 supported platforms](client-supported-platforms.md "client-supported-platforms.md")
  .

**OpenSSL Dynamic Engine**

- No support for CentOS 8, RHEL 8, and Ubuntu 18.04 LTS. For more
  information, see [Known issues for the OpenSSL Dynamic Engine for AWS CloudHSM](ki-openssl-sdk.md "ki-openssl-sdk.md").

**JCE provider**

- Add platform support for CentOS 8, RHEL 8, and Ubuntu 18.04 LTS.
  For more information, see [AWS CloudHSM Client SDK 5 supported platforms](client-supported-platforms.md "client-supported-platforms.md")
  .

**Windows (CNG and KSP providers)**

- Improved stability and bug fixes.
  Version 3.2.0 adds support for masking passwords and other improvements.

**AWS CloudHSM Client Software**

- Adds support for hiding your password when using command-line
  tools. For more information, see [loginHSM and logoutHSM](cloudhsm_mgmt_util-loginLogout.md "cloudhsm_mgmt_util-loginLogout.md") (cloudhsm_mgmt_util) and [loginHSM
  and logoutHSM](key_mgmt_util-loginHSM.md "key_mgmt_util-loginHSM.md") (key_mgmt_util).

**PKCS #11 library**

- Adds support for hashing large data in software for some PKCS #11
  mechanisms that were previously unsupported. For more information,
  see [Supported Mechanisms](pkcs11-mechanisms.md "pkcs11-mechanisms.md").

**OpenSSL Dynamic Engine**

- Improved stability and bug fixes.

**JCE provider**

- Updated the version for consistency.

**Windows (CNG and KSP providers)**

- Improved stability and bug fixes.
  Version 3.1.2 adds updates to JCE provider.

**AWS CloudHSM Client Software**

- Updated the version for consistency

**PKCS #11 library**

- Updated the version for consistency

**OpenSSL Dynamic Engine**

- Updated the version for consistency

**JCE provider**

- Update log4j to version 2.13.3

**Windows (CNG and KSP providers)**

- Updated the version for consistency

**AWS CloudHSM Client Software**

- Updated the version for consistency.

**PKCS #11 Library**

- Updated the version for consistency.

**OpenSSL Dynamic Engine**

- Updated the version for consistency.

**JCE provider**

- Bug fixes and performance improvements.

**Windows (CNG, KSP)**

- Updated the version for consistency.
  Version 3.1.0 adds [standards-compliant
  AES key
  wrapping](manage-aes-key-wrapping.md "manage-aes-key-wrapping.md").

**AWS CloudHSM Client Software**

- A new requirement for upgrade: the version of your client must
  match the version of any software libraries you are using. To
  upgrade, you must use a batch command that upgrades the client and
  all the libraries at the same time. For more information, see [Client SDK 3 Upgrade](client-upgrade.md "client-upgrade.md").
- Key_mgmt_util (KMU) includes the following updates:
  - Added two new AES key wrap methods – standards-compliant
    AES key wrap with zero padding and AES key wrap with no
    padding. For more information, see [wrapKey](key_mgmt_util-wrapKey.md "key_mgmt_util-wrapKey.md") and [unwrapKey](key_mgmt_util-unwrapKey.md "key_mgmt_util-unwrapKey.md").
  - Disabled ability to specify custom IV when wrapping a key
    using AES_KEY_WRAP_PAD_PKCS5. For more information, see [AES Key
    Wrapping](manage-aes-key-wrapping.md "manage-aes-key-wrapping.md").

**PKCS #11 Library**

- Added two new AES key wrap methods – standards-compliant AES key
  wrap with zero padding and AES key wrap with no padding. For more
  information, see [AES Key Wrapping](manage-aes-key-wrapping.md "manage-aes-key-wrapping.md").
- You can configure salt length for RSA-PSS signatures. To learn how
  to use this feature, see [Configurable
  salt length for RSA-PSS signatures](https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples "https://github.com/aws-samples/aws-cloudhsm-pkcs11-examples") on GitHub.

**OpenSSL Dynamic Engine**

- **BREAKING CHANGE**: TLS 1.0 and 1.2
  cipher suites with SHA1 are not available in OpenSSL Engine 3.1.0.
  This issue will be resolved shortly.
- If you intend to install the OpenSSL Dynamic Engine library on
  RHEL 6 or CentOS 6, see a [known
  issue](ki-openssl-sdk.md#openssl-default-version "ki-openssl-sdk.md#openssl-default-version") about the default OpenSSL version installed on those
  operating systems.
- Improved stability and bug fixes

**JCE provider**

- **BREAKING CHANGE**: To address an
  issue with Java Cryptography Extension (JCE) compliance, AES wrap
  and unwrap now properly use the AESWrap algorithm instead of the AES
  algorithm. This means `Cipher.WRAP_MODE` and `Cipher.UNWRAP_MODE` no longer succeed for AES/ECB and AES/CBC
  mechanisms.

To upgrade to client version 3.1.0, you must update your code. If
you have existing wrapped keys, you must pay particular attention to
the mechanism you use to unwrap and how IV defaults have changed. If
you wrapped keys with client version 3.0.0 or earlier, then in 3.1.1
you must use AESWrap/ECB/PKCS5Padding to unwrap your existing keys.
For more information, see [AES Key Wrapping](manage-aes-key-wrapping.md "manage-aes-key-wrapping.md").

- You can list multiple keys with the same label from the
  JCE provider. To learn how to iterate through all available keys, see [Find
  all keys](https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java "https://github.com/aws-samples/aws-cloudhsm-jce-examples/blob/master/src/main/java/com/amazonaws/cloudhsm/examples/KeyUtilitiesRunner.java") on GitHub.
- You can set more restrictive values for attributes during key
  creation, including specifying different labels for public and
  private keys. For more information, see [Supported Java Attributes](java-lib-attributes.md "java-lib-attributes.md").

**Windows (CNG, KSP)**

- Improved stability and bug fixes.
