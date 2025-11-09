# Supported mechanisms for the PKCS #11 library for AWS CloudHSM

Client SDK 5

The PKCS #11 library is compliant with version 2.40 of the PKCS #11 specification. To invoke a
cryptographic feature using PKCS #11, call a function with a given mechanism. The following
sections summarize the combinations of functions and mechanisms supported by AWS CloudHSM Client SDK 5.

The PKCS #11 library supports the following algorithms:

- **Encryption and decryption** – AES-CBC, AES-CTR, AES-ECB,
  AES-GCM, DES3-CBC, DES3-ECB, RSA-OAEP, and RSA-PKCS
- **Sign and verify** – RSA, HMAC, and ECDSA; with
  and without hashing
- **Hash/digest** – SHA1, SHA224, SHA256, SHA384, and
  SHA512
- **Key wrap** – AES Key Wrap[1](#mech1 "#mech1"), AES-GCM, RSA-AES, and
  RSA-OAEP
- **Key derivation** – SP800-108 Counter KDF and ECDH with KDF (Supported KDF algorithms are X9.63 with SHA1, SHA224, SHA256, SHA384, SHA512)

###### Topics

- [Generate key and key pair functions](#pkcs11-mech-function-genkey "#pkcs11-mech-function-genkey")
- [Sign and verify functions](#pkcs11-mech-function-signverify "#pkcs11-mech-function-signverify")
- [Sign recover and verify recover functions](#pkcs11-mech-function-sr-vr "#pkcs11-mech-function-sr-vr")
- [Digest functions](#pkcs11-mech-function-digest "#pkcs11-mech-function-digest")
- [Encrypt and decrypt functions](#pkcs11-mech-function-enc-dec "#pkcs11-mech-function-enc-dec")
- [Derive key functions](#pkcs11-mech-function-derive-key "#pkcs11-mech-function-derive-key")
- [Wrap and Unwrap functions](#pkcs11-mech-function-wrap-unwrap "#pkcs11-mech-function-wrap-unwrap")
- [Maximum data size for each mechanism](#pkcs11-mech-max "#pkcs11-mech-max")
- [Mechanism annotations](#pkcs11-mech-annotations "#pkcs11-mech-annotations")

## Generate key and key pair functions

The AWS CloudHSM software library for PKCS #11 library allows you to use the following mechanisms for Generate Key and Key Pair functions.

- `CKM_RSA_PKCS_KEY_PAIR_GEN`
- `CKM_RSA_X9_31_KEY_PAIR_GEN` – This mechanism is functionally identical to the `CKM_RSA_PKCS_KEY_PAIR_GEN` mechanism,
  but offers stronger guarantees for `p` and `q` generation.
- `CKM_EC_KEY_PAIR_GEN`
- `CKM_GENERIC_SECRET_KEY_GEN`
- `CKM_AES_KEY_GEN`
- `CKM_DES3_KEY_GEN` – upcoming change listed in footnote [5](#mech5 "#mech5").

## Sign and verify functions

The AWS CloudHSM software library for PKCS #11 library allows you to use the following mechanisms for Sign and Verify functions. With Client SDK 5,
the data is hashed locally in software. This means there is no limit on the size of the data that can be hashed by the SDK.

With Client SDK 5 RSA and ECDSA hashing is done locally so there is no data limit. With HMAC, there is a data limit. See footnote [2](#mech2 "#mech2") for more info.

**RSA**

- `CKM_RSA_X_509`
- `CKM_RSA_PKCS` – single-part operations only.
- `CKM_RSA_PKCS_PSS` – single-part operations only.
- `CKM_SHA1_RSA_PKCS`
- `CKM_SHA224_RSA_PKCS`
- `CKM_SHA256_RSA_PKCS`
- `CKM_SHA384_RSA_PKCS`
- `CKM_SHA512_RSA_PKCS`
- `CKM_SHA512_RSA_PKCS`
- `CKM_SHA1_RSA_PKCS_PSS`
- `CKM_SHA224_RSA_PKCS_PSS`
- `CKM_SHA256_RSA_PKCS_PSS`
- `CKM_SHA384_RSA_PKCS_PSS`
- `CKM_SHA512_RSA_PKCS_PSS`

**ECDSA**

- `CKM_ECDSA` – single-part operations only.
- `CKM_ECDSA_SHA1`
- `CKM_ECDSA_SHA224`
- `CKM_ECDSA_SHA256`
- `CKM_ECDSA_SHA384`
- `CKM_ECDSA_SHA512`

**HMAC**

- `CKM_SHA_1_HMAC`[2](#mech2 "#mech2")
- `CKM_SHA224_HMAC`[2](#mech2 "#mech2")
- `CKM_SHA256_HMAC`[2](#mech2 "#mech2")
- `CKM_SHA384_HMAC`[2](#mech2 "#mech2")
- `CKM_SHA512_HMAC`[2](#mech2 "#mech2")

**CMAC**

- `CKM_AES_CMAC`

## Sign recover and verify recover functions

Client SDK 5 does not support Sign Recover and Verify Recover functions.

## Digest functions

The AWS CloudHSM software library for PKCS #11 library allows you to use the following mechanisms for Digest functions. With
Client SDK 5, the data is hashed locally in software. This means there is no limit on the size of the data that
can be hashed by the SDK.

- `CKM_SHA_1`
- `CKM_SHA224`
- `CKM_SHA256`
- `CKM_SHA384`
- `CKM_SHA512`

## Encrypt and decrypt functions

The AWS CloudHSM software library for PKCS #11 library allows you to use the following mechanisms for Encrypt and Decrypt functions.

- `CKM_RSA_X_509`
- `CKM_RSA_PKCS` – single-part operations only. Upcoming change listed in footnote [5](#mech5 "#mech5").
- `CKM_RSA_PKCS_OAEP` – single-part operations only.
- `CKM_AES_ECB`
- `CKM_AES_CTR`
- `CKM_AES_CBC`
- `CKM_AES_CBC_PAD`
- `CKM_DES3_CBC` – upcoming change listed in footnote [5](#mech5 "#mech5").
- `CKM_DES3_ECB` – upcoming change listed in footnote [5](#mech5 "#mech5").
- `CKM_DES3_CBC_PAD` – upcoming change listed in footnote [5](#mech5 "#mech5").
- `CKM_AES_GCM` [1](#mech1 "#mech1"), [2](#mech2 "#mech2")
- `CKM_CLOUDHSM_AES_GCM`[3](#mech3 "#mech3")

## Derive key functions

The AWS CloudHSM software library for PKCS #11 library supports the following key derivation mechanisms:

- `CKM_SP800_108_COUNTER_KDF`
- `CKM_ECDH1_DERIVE` - Supports ECDH key derivation with the following vendor-defined KDF types[6](#kdf6 "#kdf6"):
  - `CKD_CLOUDHSM_X963_SHA1_KDF` - X9.63 KDF with SHA1[7](#kdf7 "#kdf7")
  - `CKD_CLOUDHSM_X963_SHA224_KDF` - X9.63 KDF with SHA224[7](#kdf7 "#kdf7")
  - `CKD_CLOUDHSM_X963_SHA256_KDF` - X9.63 KDF with SHA256[7](#kdf7 "#kdf7")
  - `CKD_CLOUDHSM_X963_SHA384_KDF` - X9.63 KDF with SHA384[7](#kdf7 "#kdf7")
  - `CKD_CLOUDHSM_X963_SHA512_KDF` - X9.63 KDF with SHA512[7](#kdf7 "#kdf7")

## Wrap and Unwrap functions

The AWS CloudHSM software library for PKCS #11 library allows you to use the following mechanisms for Wrap and Unwrap functions.

For additional information regarding AES key wrapping, see [AES Key Wrapping](manage-aes-key-wrapping.md "manage-aes-key-wrapping.md").

- `CKM_RSA_PKCS` – single-part operations only. An upcoming change is listed in footnote [5](#mech5 "#mech5").
- `CKM_RSA_PKCS_OAEP`[4](#mech4 "#mech4")
- `CKM_AES_GCM`[1](#mech1 "#mech1"), [3](#mech3 "#mech3")
- `CKM_CLOUDHSM_AES_GCM`[3](#mech3 "#mech3")
- `CKM_RSA_AES_KEY_WRAP`
- `CKM_CLOUDHSM_AES_KEY_WRAP_NO_PAD`[3](#mech3 "#mech3")
- `CKM_CLOUDHSM_AES_KEY_WRAP_PKCS5_PAD`[3](#mech3 "#mech3")
- `CKM_CLOUDHSM_AES_KEY_WRAP_ZERO_PAD`[3](#mech3 "#mech3")

## Maximum data size for each mechanism

The following table lists the maximum data size set for each mechanism:

| Maximum data set size  | **Mechanism** | **Maximum data size in bytes** |
| ---------------------- | ------------- | ------------------------------ |
| `CKM_SHA_1_HMAC`       | 16288         |
| `CKM_SHA224_HMAC`      | 16256         |
| `CKM_SHA256_HMAC`      | 16288         |
| `CKM_SHA384_HMAC`      | 16224         |
| `CKM_SHA512_HMAC`      | 16224         |
| `CKM_AES_CBC`          | 16272         |
| `CKM_AES_GCM`          | 16224         |
| `CKM_CLOUDHSM_AES_GCM` | 16224         |
| `CKM_DES3_CBC`         | 16280         |

## Mechanism annotations

- [1] When performing AES-GCM encryption, the HSM does not
  accept initialization vector (IV) data from the application. You must use an IV that it generates.
  The 12-byte IV provided by the HSM is written into the memory reference pointed to by the pIV element of
  the `CK_GCM_PARAMS` parameters structure that you supply. To prevent user confusion, PKCS #11 SDK in
  version 1.1.1 and later ensures that pIV points to a zeroized buffer when AES-GCM encryption is initialized.

[Show moreShow less](# "#")

- [2] When operating on data by using any of
  the following mechanisms, if the data buffer exceeds the maximum data size, the
  operation results in an error. For these mechanisms, all the data processing must occur inside the HSM.
  For information on maximum data size sets for each mechanism, refer to [Maximum data size for each mechanism](#pkcs11-mech-max "#pkcs11-mech-max").

[Show moreShow less](# "#")

- [3] Vendor-defined mechanism. In order to use the CloudHSM
  vendor defined mechanisms, PKCS#11 applications must include `/opt/cloudhsm/include/pkcs11t.h` during compilation.

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

`**CKM\_CLOUDHSM\_AES\_KEY\_WRAP\_PKCS5\_PAD**`: AES Key Wrap with PKCS #5 Padding.

`**CKM\_CLOUDHSM\_AES\_KEY\_WRAP\_ZERO\_PAD**`: AES Key Wrap with Zero Padding.

- [4] The following `CK_MECHANISM_TYPE`
  and `CK_RSA_PKCS_MGF_TYPE` are supported as
  `CK_RSA_PKCS_OAEP_PARAMS` for `CKM_RSA_PKCS_OAEP`:

      + `CKM_SHA_1` using `CKG_MGF1_SHA1`
      + `CKM_SHA224` using `CKG_MGF1_SHA224`
      + `CKM_SHA256` using `CKG_MGF1_SHA256`
      + `CKM_SHA384` using `CKM_MGF1_SHA384`
      + `CKM_SHA512` using `CKM_MGF1_SHA512`

  [Show moreShow less](# "#")

- [5] In accordance with NIST guidance, this is disallowed for clusters in FIPS mode after 2023. For clusters in non-FIPS mode, it is still allowed after 2023. See [FIPS 140 Compliance: 2024 Mechanism Deprecation](compliance-dep-notif.md#compliance-dep-notif-1 "compliance-dep-notif.md#compliance-dep-notif-1") for details.

[Show moreShow less](# "#")

- [6] Vendor defined types. In order to use CloudHSM vendor defined types, PKCS#11 applications must include `cloudhsm_pkcs11_vendor_defs.h` during compilation. This is found in `/opt/cloudhsm/include/pkcs11/cloudhsm_pkcs11_vendor_defs.h` for Linux based platforms
  and `C:\Program Files\Amazon\CloudHSM\include\pkcs11\cloudhsm_pkcs11_vendor_defs.h` for Windows based platforms

[Show moreShow less](# "#")

- [7] Key derivation functions (KDFs) are specified in [RFC 8418, Section 2.1](https://datatracker.ietf.org/doc/html/rfc8418 "https://datatracker.ietf.org/doc/html/rfc8418").

[Show moreShow less](# "#")
