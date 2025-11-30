# Supported mechanisms for AWS CloudHSM Client SDK 3

The PKCS #11 library supports the following algorithms for AWS CloudHSM Client SDK 3:

- **Encryption and decryption** – AES-CBC, AES-CTR, AES-ECB,
  AES-GCM, DES3-CBC, DES3-ECB, RSA-OAEP, and RSA-PKCS
- **Sign and verify** – RSA, HMAC, and ECDSA; with
  and without hashing
- **Hash/digest** – SHA1, SHA224, SHA256, SHA384, and
  SHA512
- **Key wrap** – AES Key Wrap,[4](#pkcs11-v3-mech4 "#pkcs11-v3-mech4") AES-GCM, RSA-AES, and
  RSA-OAEP
- **Key derivation** – ECDH,[5](#pkcs11-v3-mech5 "#pkcs11-v3-mech5") SP800-108 CTR KDF

## The PKCS #11 library mechanism-function table

The PKCS #11 library is compliant with version 2.40 of the PKCS #11 specification. To invoke
a cryptographic feature using PKCS #11, call a function with a given mechanism. The
following table summarizes the combinations of functions and mechanisms supported by
AWS CloudHSM.

###### Interpreting the supported PKCS #11 mechanism-function table

A ✔ mark indicates that AWS CloudHSM supports the mechanism for the function. We do not
support all possible functions listed in the PKCS #11 specification. A ✖ mark
indicates that AWS CloudHSM does not yet support the mechanism for the given function, even
though the PKCS #11 standard allows it. Empty cells indicate that PKCS #11 standard does
not support the mechanism for the given function.

| Supported PKCS #11 library mechanisms and functions                      | Mechanism                                     | Functions                                                                                    |
| ------------------------------------------------------------------------ | --------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------- |
|                                                                          | **Generate Key\*<br>• or **Key Pair\*\*       | **Sign & Verify**                                                                            | **SR & VR** | **Digest**                                          | **Encrypt & Decrypt**                                                                         | **Derive Key**                                | **Wrap & UnWrap**                                   |
| `CKM_RSA_PKCS_KEY_PAIR_GEN`                                              | **✔**                                         |                                                                                              |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_RSA_X9_31_KEY_PAIR_GEN`                                             | **✔**[2](#pkcs11-v3-mech2 "#pkcs11-v3-mech2") |                                                                                              |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_RSA_X_509`                                                          |                                               | **✔**                                                                                        |             |                                                     | **✔**                                                                                         |                                               |                                                     |
| `CKM_RSA_PKCS`**see note [8](#pkcs11-v3-mech8 "#pkcs11-v3-mech8")**      |                                               | **✔**[1](#pkcs11-v3-mech1 "#pkcs11-v3-mech1")                                                | ✖           |                                                     | **✔**[1](#pkcs11-v3-mech1 "#pkcs11-v3-mech1")                                                 |                                               | **✔**[1](#pkcs11-v3-mech1 "#pkcs11-v3-mech1")       |
| `CKM_RSA_PKCS_OAEP`                                                      |                                               |                                                                                              |             |                                                     | **✔**[1](#pkcs11-v3-mech1 "#pkcs11-v3-mech1")                                                 |                                               | **✔**[6](#pkcs11-v3-mech6 "#pkcs11-v3-mech6")       |
| `CKM_SHA1_RSA_PKCS`                                                      |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA224_RSA_PKCS`                                                    |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA256_RSA_PKCS`                                                    |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA384_RSA_PKCS`                                                    |                                               | **✔**[2](#pkcs11-v3-mech2 "#pkcs11-v3-mech2"),[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2") |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA512_RSA_PKCS`                                                    |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_RSA_PKCS_PSS`                                                       |                                               | **✔**[1](#pkcs11-v3-mech1 "#pkcs11-v3-mech1")                                                |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA1_RSA_PKCS_PSS`                                                  |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA224_RSA_PKCS_PSS`                                                |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA256_RSA_PKCS_PSS`                                                |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA384_RSA_PKCS_PSS`                                                |                                               | **✔**[2](#pkcs11-v3-mech2 "#pkcs11-v3-mech2"),[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2") |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA512_RSA_PKCS_PSS`                                                |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_EC_KEY_PAIR_GEN`                                                    | **✔**                                         |                                                                                              |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_ECDSA`                                                              |                                               | **✔**[1](#pkcs11-v3-mech1 "#pkcs11-v3-mech1")                                                |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_ECDSA_SHA1`                                                         |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_ECDSA_SHA224`                                                       |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_ECDSA_SHA256`                                                       |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_ECDSA_SHA384`                                                       |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_ECDSA_SHA512`                                                       |                                               | **✔**[3.2](#pkcs11-v3-mech3-2 "#pkcs11-v3-mech3-2")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_ECDH1_DERIVE`                                                       |                                               |                                                                                              |             |                                                     |                                                                                               | **✔**[5](#pkcs11-v3-mech5 "#pkcs11-v3-mech5") |                                                     |
| `CKM_SP800_108_COUNTER_KDF`                                              |                                               |                                                                                              |             |                                                     |                                                                                               | **✔**                                         |                                                     |
| `CKM_GENERIC_SECRET_KEY_GEN`                                             | **✔**                                         |                                                                                              |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_AES_KEY_GEN`                                                        | **✔**                                         |                                                                                              |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_AES_ECB`                                                            |                                               |                                                                                              |             |                                                     | **✔**                                                                                         |                                               | ✖                                                   |
| `CKM_AES_CTR`                                                            |                                               |                                                                                              |             |                                                     | **✔**                                                                                         |                                               | ✖                                                   |
| `CKM_AES_CBC`                                                            |                                               |                                                                                              |             |                                                     | **✔**[3.3](#pkcs11-v3-mech3-3 "#pkcs11-v3-mech3-3")                                           |                                               | ✖                                                   |
| `CKM_AES_CBC_PAD`                                                        |                                               |                                                                                              |             |                                                     | **✔**                                                                                         |                                               | ✖                                                   |
| `CKM_DES3_KEY_GEN` **see note [8](#pkcs11-v3-mech8 "#pkcs11-v3-mech8")** | **✔**                                         |                                                                                              |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_DES3_CBC` **see note [8](#pkcs11-v3-mech8 "#pkcs11-v3-mech8")**     |                                               |                                                                                              |             |                                                     | **✔**[3.3](#pkcs11-v3-mech3-3 "#pkcs11-v3-mech3-3")                                           |                                               | ✖                                                   |
| `CKM_DES3_CBC_PAD` **see note [8](#pkcs11-v3-mech8 "#pkcs11-v3-mech8")** |                                               |                                                                                              |             |                                                     | **✔**                                                                                         |                                               | ✖                                                   |
| `CKM_DES3_ECB` **see note [8](#pkcs11-v3-mech8 "#pkcs11-v3-mech8")**     |                                               |                                                                                              |             |                                                     | **✔**                                                                                         |                                               | ✖                                                   |
| `CKM_AES_GCM`                                                            |                                               |                                                                                              |             |                                                     | **✔**[3.3](#pkcs11-v3-mech3-3 "#pkcs11-v3-mech3-3"), [4](#pkcs11-v3-mech4 "#pkcs11-v3-mech4") |                                               | **✔**[7.1](#pkcs11-v3-mech7-1 "#pkcs11-v3-mech7-1") |
| `CKM_CLOUDHSM_AES_GCM`                                                   |                                               |                                                                                              |             |                                                     | **✔**[7.1](#pkcs11-v3-mech7-1 "#pkcs11-v3-mech7-1")                                           |                                               | **✔**[7.1](#pkcs11-v3-mech7-1 "#pkcs11-v3-mech7-1") |
| `CKM_SHA_1`                                                              |                                               |                                                                                              |             | **✔**[3.1](#pkcs11-v3-mech3-1 "#pkcs11-v3-mech3-1") |                                                                                               |                                               |                                                     |
| `CKM_SHA_1_HMAC`                                                         |                                               | **✔**[3.3](#pkcs11-v3-mech3-3 "#pkcs11-v3-mech3-3")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA224`                                                             |                                               |                                                                                              |             | **✔**[3.1](#pkcs11-v3-mech3-1 "#pkcs11-v3-mech3-1") |                                                                                               |                                               |                                                     |
| `CKM_SHA224_HMAC`                                                        |                                               | **✔**[3.3](#pkcs11-v3-mech3-3 "#pkcs11-v3-mech3-3")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA256`                                                             |                                               |                                                                                              |             | **✔**[3.1](#pkcs11-v3-mech3-1 "#pkcs11-v3-mech3-1") |                                                                                               |                                               |                                                     |
| `CKM_SHA256_HMAC`                                                        |                                               | **✔**[3.3](#pkcs11-v3-mech3-3 "#pkcs11-v3-mech3-3")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA384`                                                             |                                               |                                                                                              |             | **✔**[3.1](#pkcs11-v3-mech3-1 "#pkcs11-v3-mech3-1") |                                                                                               |                                               |                                                     |
| `CKM_SHA384_HMAC`                                                        |                                               | **✔**[3.3](#pkcs11-v3-mech3-3 "#pkcs11-v3-mech3-3")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_SHA512`                                                             |                                               |                                                                                              |             | **✔**[3.1](#pkcs11-v3-mech3-1 "#pkcs11-v3-mech3-1") |                                                                                               |                                               |                                                     |
| `CKM_SHA512_HMAC`                                                        |                                               | **✔**[3.3](#pkcs11-v3-mech3-3 "#pkcs11-v3-mech3-3")                                          |             |                                                     |                                                                                               |                                               |                                                     |
| `CKM_RSA_AES_KEY_WRAP`                                                   |                                               |                                                                                              |             |                                                     |                                                                                               |                                               | **✔**                                               |
| `CKM_AES_KEY_WRAP`                                                       |                                               |                                                                                              |             |                                                     |                                                                                               |                                               | **✔**                                               |
| `CKM_AES_KEY_WRAP_PAD`                                                   |                                               |                                                                                              |             |                                                     |                                                                                               |                                               | **✔**                                               |
| `CKM_CLOUDHSM_AES_KEY_WRAP_NO_PAD`                                       |                                               |                                                                                              |             |                                                     |                                                                                               |                                               | **✔**[7.1](#pkcs11-v3-mech7-1 "#pkcs11-v3-mech7-1") |
| `CKM_CLOUDHSM_AES_KEY_WRAP_PKCS5_PAD`                                    |                                               |                                                                                              |             |                                                     |                                                                                               |                                               | **✔**[7.1](#pkcs11-v3-mech7-1 "#pkcs11-v3-mech7-1") |
| `CKM_CLOUDHSM_AES_KEY_WRAP_ZERO_PAD`                                     |                                               |                                                                                              |             |                                                     |                                                                                               |                                               | **✔**[7.1](#pkcs11-v3-mech7-1 "#pkcs11-v3-mech7-1") |

**Mechanism annotations**

- [1] Single-part operations only.
- [2] Mechanism is functionally identical to the
  `CKM_RSA_PKCS_KEY_PAIR_GEN` mechanism, but offers stronger guarantees for
  `p` and `q` generation.
- [3.1] AWS CloudHSM approaches hashing differently
  based on the Client SDK. For Client SDK 3, where we do the hashing depends on data size and whether you’re using single-part
  or multipart operations.

**Single-part operations in Client SDK 3**

Table 3.1 lists the maximum data set size for each mechanism for Client SDK 3. The entire hash is
computed inside the HSM. No support for data sizes greater than 16KB.

| Table 3.1, Maximum data set size for single-part operations | **Mechanism** | **Maximum Data Size** |
| ----------------------------------------------------------- | ------------- | --------------------- |
| `CKM_SHA_1`                                                 | 16296         |
| `CKM_SHA224`                                                | 16264         |
| `CKM_SHA256`                                                | 16296         |
| `CKM_SHA384`                                                | 16232         |
| `CKM_SHA512`                                                | 16232         |

**Multipart operations Client SDK 3**

Support for data sizes greater than 16 KB, but data size determines where the
hashing takes place. Data buffers less than 16 KB are hashed inside the HSM. Buffers
between 16 KB and the maximum data size for your system are hashed locally in software.
_Remember_: Hash functions do not require
cryptographic secrets, so you can safely compute them outside of the HSM.

[Show moreShow less](# "#")

- [3.2] AWS CloudHSM approaches hashing differently
  based on the Client SDK. For Client SDK 3, where we do the hashing depends on data size and whether you’re using single-part
  or multipart operations.

**Single-part operations Client SDK 3**

Table 3.2 lists the maximum data set size for each mechanism for Client SDK 3. No support for data
sizes greater than 16KB.

| Table 3.2, Maximum data set size for single-part operations | **Mechanism** | **Maximum Data Size** |
| ----------------------------------------------------------- | ------------- | --------------------- |
| `CKM_SHA1_RSA_PKCS`                                         | 16296         |
| `CKM_SHA224_RSA_PKCS`                                       | 16264         |
| `CKM_SHA256_RSA_PKCS`                                       | 16296         |
| `CKM_SHA384_RSA_PKCS`                                       | 16232         |
| `CKM_SHA512_RSA_PKCS`                                       | 16232         |
| `CKM_SHA1_RSA_PKCS_PSS`                                     | 16296         |
| `CKM_SHA224_RSA_PKCS_PSS`                                   | 16264         |
| `CKM_SHA256_RSA_PKCS_PSS`                                   | 16296         |
| `CKM_SHA384_RSA_PKCS_PSS`                                   | 16232         |
| `CKM_SHA512_RSA_PKCS_PSS`                                   | 16232         |
| `CKM_ECDSA_SHA1`                                            | 16296         |
| `CKM_ECDSA_SHA224`                                          | 16264         |
| `CKM_ECDSA_SHA256`                                          | 16296         |
| `CKM_ECDSA_SHA384`                                          | 16232         |
| `CKM_ECDSA_SHA512`                                          | 16232         |

**Multipart operations Client SDK 3**

Support for data sizes greater than 16 KB, but data size determines where the
hashing takes place. Data buffers less than 16 KB are hashed inside the HSM. Buffers
between 16 KB and the maximum data size for your system are hashed locally in software.
_Remember_: Hash functions do not require
cryptographic secrets, so you can safely compute them outside of the HSM.

[Show moreShow less](# "#")

- [3.3] When operating on data by using any of
  the following mechanisms, if the data buffer exceeds the maximum data size, the
  operation results in an error. For these mechanisms, all the data processing must occur inside the HSM.
  The following table lists maximum data size set for each mechanism:

| Table 3.3, Maximum data set size | **Mechanism** | **Maximum Data Size** |
| -------------------------------- | ------------- | --------------------- |
| `CKM_SHA_1_HMAC`                 | 16288         |
| `CKM_SHA224_HMAC`                | 16256         |
| `CKM_SHA256_HMAC`                | 16288         |
| `CKM_SHA384_HMAC`                | 16224         |
| `CKM_SHA512_HMAC`                | 16224         |
| `CKM_AES_CBC`                    | 16272         |
| `CKM_AES_GCM`                    | 16224         |
| `CKM_CLOUDHSM_AES_GCM`           | 16224         |
| `CKM_DES3_CBC`                   | 16280         |

[Show moreShow less](# "#")

- [4] When performing AES-GCM encryption, the HSM
  does not accept initialization vector (IV) data from the application. You must use an IV
  that it generates. The 12-byte IV provided by the HSM is written into the memory
  reference pointed to by the pIV element of the `CK_GCM_PARAMS` parameters
  structure that you supply. To prevent user confusion, PKCS #11 SDK in version 1.1.1 and
  later ensures that pIV points to a zeroized buffer when AES-GCM encryption is
  initialized.

[Show moreShow less](# "#")

- [5] **Client SDK 3 only**.
  Mechanism is implemented to support SSL/TLS
  offload cases and is executed only partially within the HSM. Before using this
  mechanism, see "Issue: ECDH key derivation is executed only partially within the HSM" in
  [Known issues for the PKCS #11 library for AWS CloudHSM](ki-pkcs11-sdk.md "ki-pkcs11-sdk.md"). `CKM_ECDH1_DERIVE`
  does not support the secp521r1 (P-521) curve.
- [6] The following `CK_MECHANISM_TYPE`
  and `CK_RSA_PKCS_MGF_TYPE` are supported as
  `CK_RSA_PKCS_OAEP_PARAMS` for `CKM_RSA_PKCS_OAEP`:

      + `CKM_SHA_1` using `CKG_MGF1_SHA1`
      + `CKM_SHA224` using `CKG_MGF1_SHA224`
      + `CKM_SHA256` using `CKG_MGF1_SHA256`
      + `CKM_SHA384` using `CKM_MGF1_SHA384`
      + `CKM_SHA512` using `CKM_MGF1_SHA512`

  [Show moreShow less](# "#")

- [7.1] Vendor-defined mechanism. In order to use the
  CloudHSM vendor defined mechanisms, PKCS#11 applications must include
  `/opt/cloudhsm/include/pkcs11t.h` during compilation.

`**CKM\_CLOUDHSM\_AES\_GCM**`: This proprietary
mechanism is a programmatically safer alternative to the standard
`CKM_AES_GCM`. It prepends the IV generated by the HSM to the ciphertext
instead of writing it back into the `CK_GCM_PARAMS` structure that is
provided during cipher initialization. You can use this mechanism with
`C_Encrypt`, `C_WrapKey`, `C_Decrypt`, and
`C_UnwrapKey` functions. When using this mechanism, the pIV variable in the
`CK_GCM_PARAMS` struct must be set to `NULL`. When using this
mechanism with `C_Decrypt` and `C_UnwrapKey`, the IV is expected
to be prepended to the ciphertext that is being unwrapped.

`**CKM\_CLOUDHSM\_AES\_KEY\_WRAP\_PKCS5\_PAD**`: AES Key Wrap with PKCS #5 Padding

`**CKM\_CLOUDHSM\_AES\_KEY\_WRAP\_ZERO\_PAD**`: AES Key Wrap with Zero Padding

For additional information regarding AES key wrapping, see [AES Key Wrapping](manage-aes-key-wrapping.md "manage-aes-key-wrapping.md").

[Show moreShow less](# "#")

- [8] In accordance with NIST guidance, this is disallowed for clusters in FIPS mode after 2023. For clusters in non-FIPS mode, it is still allowed after 2023. See [FIPS 140 Compliance: 2024 Mechanism Deprecation](compliance-dep-notif.md#compliance-dep-notif-1 "compliance-dep-notif.md#compliance-dep-notif-1") for details.

[Show moreShow less](# "#")
