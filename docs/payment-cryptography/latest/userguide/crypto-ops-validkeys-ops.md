# Valid keys for cryptographic operations

Certain keys can only be used for certain operations. Additionally,
some operations may limit the key modes of use for keys. Please see the following table
for allowed combinations.

###### Note

Certain combinations, although permitted, may create unusable situations such as generating
CVV codes `(generate)` but then unable to verify them `(verify)`.

###### Topics

- [GenerateCardData](#w2aac15c31b9 "#w2aac15c31b9")
- [VerifyCardData](#w2aac15c31c11 "#w2aac15c31c11")
- [GeneratePinData (for VISA/ABA schemes)](#w2aac15c31c15 "#w2aac15c31c15")
- [GeneratePinData (for IBM3624)](#w2aac15c31c17 "#w2aac15c31c17")
- [VerifyPinData (for VISA/ABA schemes)](#w2aac15c31c21 "#w2aac15c31c21")
- [VerifyPinData (for IBM3624)](#w2aac15c31c23 "#w2aac15c31c23")
- [Decrypt Data](#w2aac15c31c27 "#w2aac15c31c27")
- [Encrypt Data](#w2aac15c31c33 "#w2aac15c31c33")
- [Translate Pin Data](#w2aac15c31c39 "#w2aac15c31c39")
- [Generate/Verify MAC](#crypto-ops-validkeys.generatemac "#crypto-ops-validkeys.generatemac")
- [VerifyAuthRequestCryptogram](#w2aac15c31c47 "#w2aac15c31c47")
- [Import/Export Key](#crypto-ops-validkeys.importexport "#crypto-ops-validkeys.importexport")
- [Unused key types](#w2aac15c31c53 "#w2aac15c31c53")

## GenerateCardData

| API Endpoint     | Cryptographic Operation or Algorithm                                       | Allowed Key Usage                | Allowed Key Algorithm      | Allowed combination of key modes of use                |
| ---------------- | -------------------------------------------------------------------------- | -------------------------------- | -------------------------- | ------------------------------------------------------ |
| GenerateCardData | • AMEX_CARD_SECURITY_CODE_VERSION_1<br>• AMEX_CARD_SECURITY_CODE_VERSION_2 | TR31_C0_CARD_VERIFICATION_KEY    | • TDES_2KEY<br>• TDES_3KEY | { Generate = true },{ Generate = true, Verify = true } |
| GenerateCardData | • CARD_VERIFICATION_VALUE_1<br>• CARD_VERIFICATION_VALUE_2                 | TR31_C0_CARD_VERIFICATION_KEY    | • TDES_2KEY                | { Generate = true },{ Generate = true, Verify = true } |
| GenerateCardData | • CARDHOLDER_AUTHENTICATION_VERIFICATION_VALUE                             | TR31_E6_EMV_MKEY_OTHER           | • TDES_2KEY                | { DeriveKey = true }                                   |
| GenerateCardData | • DYNAMIC_CARD_VERIFICATION_CODE                                           | TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS | • TDES_2KEY                | { DeriveKey = true }                                   |
| GenerateCardData | • DYNAMIC_CARD_VERIFICATION_VALUE                                          | TR31_E6_EMV_MKEY_OTHER           | • TDES_2KEY                | { DeriveKey = true }                                   |

## VerifyCardData

| Cryptographic Operation or Algorithm                                       | Allowed Key Usage                | Allowed Key Algorithm      | Allowed combination of key modes of use                |
| -------------------------------------------------------------------------- | -------------------------------- | -------------------------- | ------------------------------------------------------ |
| • AMEX_CARD_SECURITY_CODE_VERSION_1<br>• AMEX_CARD_SECURITY_CODE_VERSION_2 | TR31_C0_CARD_VERIFICATION_KEY    | • TDES_2KEY<br>• TDES_3KEY | { Generate = true },{ Generate = true, Verify = true } |
| • CARD_VERIFICATION_VALUE_1<br>• CARD_VERIFICATION_VALUE_2                 | TR31_C0_CARD_VERIFICATION_KEY    | • TDES_2KEY                | { Generate = true },{ Generate = true, Verify = true } |
| • CARDHOLDER_AUTHENTICATION_VERIFICATION_VALUE                             | TR31_E6_EMV_MKEY_OTHER           | • TDES_2KEY                | { DeriveKey = true }                                   |
| • DYNAMIC_CARD_VERIFICATION_CODE                                           | TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS | • TDES_2KEY                | { DeriveKey = true }                                   |
| • DYNAMIC_CARD_VERIFICATION_VALUE                                          | TR31_E6_EMV_MKEY_OTHER           | • TDES_2KEY                | { DeriveKey = true }                                   |

## GeneratePinData (for VISA/ABA schemes)

`VISA_PIN or VISA_PIN_VERIFICATION_VALUE`

| Key Type           | Allowed Key Usage                 | Allowed Key Algorithm      | Allowed combination of key modes of use                                                                                              |
| ------------------ | --------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| PIN Encryption Key | TR31_P0_PIN_ENCRYPTION_KEY        | • TDES_2KEY<br>• TDES_3KEY | • { Encrypt = true, Wrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| PIN Generation Key | TR31_V2_VISA_PIN_VERIFICATION_KEY | • TDES_3KEY                | • { Generate = true }<br>• { Generate = true, Verify = true }                                                                        |

## GeneratePinData (for `IBM3624`)

`IBM3624_PIN_OFFSET,IBM3624_NATURAL_PIN,IBM3624_RANDOM_PIN, IBM3624_PIN_FROM_OFFSET)`

| Key Type           | Allowed Key Usage                    | Allowed Key Algorithm      | Allowed combination of key modes of use                                                                                                                                                                                                                                                                                                                                          |
| ------------------ | ------------------------------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PIN Encryption Key | TR31_P0_PIN_ENCRYPTION_KEY           | • TDES_2KEY<br>• TDES_3KEY | For IBM3624_NATURAL_PIN, IBM3624_RANDOM_PIN, IBM3624_PIN_FROM_OFFSET<br>• { Encrypt = true, Wrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true }<br>For IBM3624_PIN_OFFSET<br>• { Encrypt = true, Unwrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| PIN Generation Key | TR31_V1_IBM3624_PIN_VERIFICATION_KEY | • TDES_3KEY                | • { Generate = true }<br>• { Generate = true, Verify = true }                                                                                                                                                                                                                                                                                                                    |

## VerifyPinData (for VISA/ABA schemes)

`VISA_PIN`

| Key Type           | Allowed Key Usage                 | Allowed Key Algorithm      | Allowed combination of key modes of use                                                                                                |
| ------------------ | --------------------------------- | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| PIN Encryption Key | TR31_P0_PIN_ENCRYPTION_KEY        | • TDES_2KEY<br>• TDES_3KEY | • { Decrypt = true, Unwrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| PIN Generation Key | TR31_V2_VISA_PIN_VERIFICATION_KEY | • TDES_3KEY                | • { Verify = true }<br>• { Generate = true, Verify = true }                                                                            |

## VerifyPinData (for `IBM3624`)

`IBM3624_PIN_OFFSET,IBM3624_NATURAL_PIN,IBM3624_RANDOM_PIN, IBM3624_PIN_FROM_OFFSET)`

| Key Type             | Allowed Key Usage                    | Allowed Key Algorithm      | Allowed combination of key modes of use                                                                                                                                                                        |
| -------------------- | ------------------------------------ | -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PIN Encryption Key   | TR31_P0_PIN_ENCRYPTION_KEY           | • TDES_2KEY<br>• TDES_3KEY | For IBM3624_NATURAL_PIN, IBM3624_RANDOM_PIN, IBM3624_PIN_FROM_OFFSET<br>• { Decrypt = true, Unwrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| PIN Verification Key | TR31_V1_IBM3624_PIN_VERIFICATION_KEY | • TDES_3KEY                | • { Verify = true }<br>• { Generate = true, Verify = true }                                                                                                                                                    |

## Decrypt Data

| Key Type       | Allowed Key Usage                                          | Allowed Key Algorithm                                             | Allowed combination of key modes of use                                                                                   |
| -------------- | ---------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| DUKPT          | TR31_B0_BASE_DERIVATION_KEY                                | • TDES_2KEY<br>• AES_128<br>• AES_192<br>• AES_256                | • { DeriveKey = true }<br>• { NoRestrictions = true }                                                                     |
| EMV            | TR31_E1_EMV_MKEY_CONFIDENTIALITY<br>TR31_E6_EMV_MKEY_OTHER | • TDES_2KEY                                                       | • { DeriveKey = true }                                                                                                    |
| RSA            | TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION                 | • RSA_2048<br>• RSA_3072<br>• RSA_4096                            | • { Decrypt = true, Unwrap=true}<br>• {Encrypt=true, Wrap=true,Decrypt = true, Unwrap=true}                               |
| Symmetric keys | TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY                      | • TDES_2KEY<br>• TDES_3KEY<br>• AES_128<br>• AES_192<br>• AES_256 | • {Decrypt = true, Unwrap=true}<br>• {Encrypt=true, Wrap=true,Decrypt = true, Unwrap=true}<br>• { NoRestrictions = true } |

## Encrypt Data

| Key Type       | Allowed Key Usage                                          | Allowed Key Algorithm                                             | Allowed combination of key modes of use                                                                                 |
| -------------- | ---------------------------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| DUKPT          | TR31_B0_BASE_DERIVATION_KEY                                | • TDES_2KEY<br>• AES_128<br>• AES_192<br>• AES_256                | • { DeriveKey = true }<br>• { NoRestrictions = true }                                                                   |
| EMV            | TR31_E1_EMV_MKEY_CONFIDENTIALITY<br>TR31_E6_EMV_MKEY_OTHER | • TDES_2KEY                                                       | • { DeriveKey = true }                                                                                                  |
| RSA            | TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION                 | • RSA_2048<br>• RSA_3072<br>• RSA_4096                            | • { Encrypt = true, Wrap=true}<br>• {Encrypt=true, Wrap=true,Decrypt = true, Unwrap=true}                               |
| Symmetric keys | TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY                      | • TDES_2KEY<br>• TDES_3KEY<br>• AES_128<br>• AES_192<br>• AES_256 | • {Encrypt = true, Wrap=true}<br>• {Encrypt=true, Wrap=true,Decrypt = true, Unwrap=true}<br>• { NoRestrictions = true } |

## Translate Pin Data

| Direction            | Key Type                       | Allowed Key Usage           | Allowed Key Algorithm                                             | Allowed combination of key modes of use                                                                                                |
| -------------------- | ------------------------------ | --------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Inbound Data Source  | DUKPT                          | TR31_B0_BASE_DERIVATION_KEY | • TDES_2KEY<br>• AES_128<br>• AES_192<br>• AES_256                | • { DeriveKey = true }<br>• { NoRestrictions = true }                                                                                  |
| Inbound Data Source  | non-DUKPT (PEK, AWK, IWK, etc) | TR31_P0_PIN_ENCRYPTION_KEY  | • TDES_2KEY<br>• TDES_3KEY<br>• AES_128<br>• AES_192<br>• AES_256 | • { Decrypt = true, Unwrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| Outbound Data Target | DUKPT                          | TR31_B0_BASE_DERIVATION_KEY | • TDES_2KEY<br>• AES_128<br>• AES_192<br>• AES_256                | • { DeriveKey = true }<br>• { NoRestrictions = true }                                                                                  |
| Outbound Data Target | non-DUKPT (PEK, IWK, AWK, etc) | TR31_P0_PIN_ENCRYPTION_KEY  | • TDES_2KEY<br>• TDES_3KEY<br>• AES_128<br>• AES_192<br>• AES_256 | • { Encrypt = true, Wrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true }   |

## Generate/Verify MAC

MAC keys are used for creating cryptographic hashes of a message/body of data. It is not recommended to create a key
with limited key modes of use as you will be unable to perform the matching operation. However, you may import/export a key with only one operation if the other system is intended
to perform the other half of the operation pair.

| Allowed Key Usage    | Allowed Key Usage           | Allowed Key Algorithm                                             | Allowed combination of key modes of use                                                                       |
| -------------------- | --------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| MAC Key              | TR31_M1_ISO_9797_1_MAC_KEY  | • TDES_2KEY<br>• TDES_3KEY                                        | • { Generate = true }<br>• { Generate = true, Verify = true }<br>• { Verify = true }<br>• { Generate = true } |
| MAC Key (Retail MAC) | TR31_M1_ISO_9797_3_MAC_KEY  | • TDES_2KEY<br>• TDES_3KEY                                        | • { Generate = true }<br>• { Generate = true, Verify = true }<br>• { Verify = true }<br>• { Generate = true } |
| MAC Key (CMAC)       | TR31_M6_ISO_9797_5_CMAC_KEY | • TDES_2KEY<br>• TDES_3KEY<br>• AES_128<br>• AES_192<br>• AES_256 | • { Generate = true }<br>• { Generate = true, Verify = true }<br>• { Verify = true }<br>• { Generate = true } |
| MAC Key (HMAC)       | TR31_M7_HMAC_KEY            | • TDES_2KEY<br>• TDES_3KEY<br>• AES_128<br>• AES_192<br>• AES_256 | • { Generate = true }<br>• { Generate = true, Verify = true }<br>• { Verify = true }<br>• { Generate = true } |

## VerifyAuthRequestCryptogram

| Allowed Key Usage        | EMV Option                       | Allowed Key Algorithm | Allowed combination of key modes of use |
| ------------------------ | -------------------------------- | --------------------- | --------------------------------------- |
| • OPTION A<br>• OPTION B | TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS | • TDES_2KEY           | • { DeriveKey = true }                  |

## Import/Export Key

| Operation Type                                             | Allowed Key Usage                                              | Allowed Key Algorithm                   | Allowed combination of key modes of use                                                                                                                                  |
| ---------------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| TR-31 Wrapping Key                                         | TR31_K1_KEY_BLOCK_PROTECTION_KEY<br>TR31_K0_KEY_ENCRYPTION_KEY | • TDES_2KEY<br>• TDES_3KEY<br>• AES_128 | • { Encrypt = true, Wrap = true } (export only)<br>• { Decrypt = true, Unwrap = true } (import only)<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } |
| Import of trusted CA                                       | TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE                   | • RSA_2048<br>• RSA_3072<br>• RSA_4096  | • { Verify = true }                                                                                                                                                      |
| Import of public key certificate for asymmetric encryption | TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION                     | • RSA_2048<br>• RSA_3072<br>• RSA_4096  | • { Encrypt=true,Wrap=true }                                                                                                                                             |

## Unused key types

The following key types are not currently used by AWS Payment Cryptography

- TR31_P1_PIN_GENERATION_KEY
- TR31_K3_ASYMMETRIC_KEY_FOR_KEY_AGREEMENT
