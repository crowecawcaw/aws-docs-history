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
- [GenerateMacEmvPinChange](#crypto-ops-validkeys.generatemacemvpinchange "#crypto-ops-validkeys.generatemacemvpinchange")
- [VerifyAuthRequestCryptogram](#w2aac15c31c51 "#w2aac15c31c51")
- [Import/Export Key](#crypto-ops-validkeys.importexport "#crypto-ops-validkeys.importexport")
- [Unused key types](#w2aac15c31c57 "#w2aac15c31c57")

## GenerateCardData

| API Endpoint     | Cryptographic Operation or Algorithm                                                 | Allowed Key Usage                     | Allowed Key Algorithm        | Allowed combination of key modes of use                |
| ---------------- | ------------------------------------------------------------------------------------ | ------------------------------------- | ---------------------------- | ------------------------------------------------------ |
| GenerateCardData | • AMEX\_CARD\_SECURITY\_CODE\_VERSION\_1<br>• AMEX\_CARD\_SECURITY\_CODE\_VERSION\_2 | TR31\_C0\_CARD\_VERIFICATION\_KEY     | • TDES\_2KEY<br>• TDES\_3KEY | { Generate = true },{ Generate = true, Verify = true } |
| GenerateCardData | • CARD\_VERIFICATION\_VALUE\_1<br>• CARD\_VERIFICATION\_VALUE\_2                     | TR31\_C0\_CARD\_VERIFICATION\_KEY     | • TDES\_2KEY                 | { Generate = true },{ Generate = true, Verify = true } |
| GenerateCardData | • CARDHOLDER\_AUTHENTICATION\_VERIFICATION\_VALUE                                    | TR31\_E6\_EMV\_MKEY\_OTHER            | • TDES\_2KEY                 | { DeriveKey = true }                                   |
| GenerateCardData | • DYNAMIC\_CARD\_VERIFICATION\_CODE                                                  | TR31\_E4\_EMV\_MKEY\_DYNAMIC\_NUMBERS | • TDES\_2KEY                 | { DeriveKey = true }                                   |
| GenerateCardData | • DYNAMIC\_CARD\_VERIFICATION\_VALUE                                                 | TR31\_E6\_EMV\_MKEY\_OTHER            | • TDES\_2KEY                 | { DeriveKey = true }                                   |

## VerifyCardData

| Cryptographic Operation or Algorithm                                                 | Allowed Key Usage                     | Allowed Key Algorithm        | Allowed combination of key modes of use                |
| ------------------------------------------------------------------------------------ | ------------------------------------- | ---------------------------- | ------------------------------------------------------ |
| • AMEX\_CARD\_SECURITY\_CODE\_VERSION\_1<br>• AMEX\_CARD\_SECURITY\_CODE\_VERSION\_2 | TR31\_C0\_CARD\_VERIFICATION\_KEY     | • TDES\_2KEY<br>• TDES\_3KEY | { Generate = true },{ Generate = true, Verify = true } |
| • CARD\_VERIFICATION\_VALUE\_1<br>• CARD\_VERIFICATION\_VALUE\_2                     | TR31\_C0\_CARD\_VERIFICATION\_KEY     | • TDES\_2KEY                 | { Generate = true },{ Generate = true, Verify = true } |
| • CARDHOLDER\_AUTHENTICATION\_VERIFICATION\_VALUE                                    | TR31\_E6\_EMV\_MKEY\_OTHER            | • TDES\_2KEY                 | { DeriveKey = true }                                   |
| • DYNAMIC\_CARD\_VERIFICATION\_CODE                                                  | TR31\_E4\_EMV\_MKEY\_DYNAMIC\_NUMBERS | • TDES\_2KEY                 | { DeriveKey = true }                                   |
| • DYNAMIC\_CARD\_VERIFICATION\_VALUE                                                 | TR31\_E6\_EMV\_MKEY\_OTHER            | • TDES\_2KEY                 | { DeriveKey = true }                                   |

## GeneratePinData (for VISA/ABA schemes)

`VISA_PIN or VISA_PIN_VERIFICATION_VALUE`

| Key Type           | Allowed Key Usage                      | Allowed Key Algorithm        | Allowed combination of key modes of use                                                                                              |
| ------------------ | -------------------------------------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| PIN Encryption Key | TR31\_P0\_PIN\_ENCRYPTION\_KEY         | • TDES\_2KEY<br>• TDES\_3KEY | • { Encrypt = true, Wrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| PIN Generation Key | TR31\_V2\_VISA\_PIN\_VERIFICATION\_KEY | • TDES\_2KEY<br>• TDES\_3KEY | • { Generate = true }<br>• { Generate = true, Verify = true }                                                                        |

## GeneratePinData (for `IBM3624`)

`IBM3624_PIN_OFFSET,IBM3624_NATURAL_PIN,IBM3624_RANDOM_PIN, IBM3624_PIN_FROM_OFFSET)`

| Key Type           | Allowed Key Usage                         | Allowed Key Algorithm        | Allowed combination of key modes of use                                                                                                                                                                                                                                                                                                                                                   |
| ------------------ | ----------------------------------------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PIN Encryption Key | TR31\_P0\_PIN\_ENCRYPTION\_KEY            | • TDES\_2KEY<br>• TDES\_3KEY | For IBM3624\_NATURAL\_PIN, IBM3624\_RANDOM\_PIN, IBM3624\_PIN\_FROM\_OFFSET<br>• { Encrypt = true, Wrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true }<br>For IBM3624\_PIN\_OFFSET<br>• { Encrypt = true, Unwrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| PIN Generation Key | TR31\_V1\_IBM3624\_PIN\_VERIFICATION\_KEY | • TDES\_3KEY                 | • { Generate = true }<br>• { Generate = true, Verify = true }                                                                                                                                                                                                                                                                                                                             |

## VerifyPinData (for VISA/ABA schemes)

`VISA_PIN`

| Key Type           | Allowed Key Usage                      | Allowed Key Algorithm        | Allowed combination of key modes of use                                                                                                |
| ------------------ | -------------------------------------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| PIN Encryption Key | TR31\_P0\_PIN\_ENCRYPTION\_KEY         | • TDES\_2KEY<br>• TDES\_3KEY | • { Decrypt = true, Unwrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| PIN Generation Key | TR31\_V2\_VISA\_PIN\_VERIFICATION\_KEY | • TDES\_2KEY<br>• TDES\_3KEY | • { Verify = true }<br>• { Generate = true, Verify = true }                                                                            |

## VerifyPinData (for `IBM3624`)

`IBM3624_PIN_OFFSET,IBM3624_NATURAL_PIN,IBM3624_RANDOM_PIN, IBM3624_PIN_FROM_OFFSET)`

| Key Type             | Allowed Key Usage                         | Allowed Key Algorithm        | Allowed combination of key modes of use                                                                                                                                                                               |
| -------------------- | ----------------------------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PIN Encryption Key   | TR31\_P0\_PIN\_ENCRYPTION\_KEY            | • TDES\_2KEY<br>• TDES\_3KEY | For IBM3624\_NATURAL\_PIN, IBM3624\_RANDOM\_PIN, IBM3624\_PIN\_FROM\_OFFSET<br>• { Decrypt = true, Unwrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| PIN Verification Key | TR31\_V1\_IBM3624\_PIN\_VERIFICATION\_KEY | • TDES\_3KEY                 | • { Verify = true }<br>• { Generate = true, Verify = true }                                                                                                                                                           |

## Decrypt Data

| Key Type       | Allowed Key Usage                                                  | Allowed Key Algorithm                                                  | Allowed combination of key modes of use                                                                                   |
| -------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| DUKPT          | TR31\_B0\_BASE\_DERIVATION\_KEY                                    | • TDES\_2KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256                 | • { DeriveKey = true }<br>• { NoRestrictions = true }                                                                     |
| EMV            | TR31\_E1\_EMV\_MKEY\_CONFIDENTIALITY<br>TR31\_E6\_EMV\_MKEY\_OTHER | • TDES\_2KEY                                                           | • { DeriveKey = true }                                                                                                    |
| RSA            | TR31\_D1\_ASYMMETRIC\_KEY\_FOR\_DATA\_ENCRYPTION                   | • RSA\_2048<br>• RSA\_3072<br>• RSA\_4096                              | • { Decrypt = true, Unwrap=true}<br>• {Encrypt=true, Wrap=true,Decrypt = true, Unwrap=true}                               |
| Symmetric keys | TR31\_D0\_SYMMETRIC\_DATA\_ENCRYPTION\_KEY                         | • TDES\_2KEY<br>• TDES\_3KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256 | • {Decrypt = true, Unwrap=true}<br>• {Encrypt=true, Wrap=true,Decrypt = true, Unwrap=true}<br>• { NoRestrictions = true } |

## Encrypt Data

| Key Type       | Allowed Key Usage                                                  | Allowed Key Algorithm                                                  | Allowed combination of key modes of use                                                                                 |
| -------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| DUKPT          | TR31\_B0\_BASE\_DERIVATION\_KEY                                    | • TDES\_2KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256                 | • { DeriveKey = true }<br>• { NoRestrictions = true }                                                                   |
| EMV            | TR31\_E1\_EMV\_MKEY\_CONFIDENTIALITY<br>TR31\_E6\_EMV\_MKEY\_OTHER | • TDES\_2KEY                                                           | • { DeriveKey = true }                                                                                                  |
| RSA            | TR31\_D1\_ASYMMETRIC\_KEY\_FOR\_DATA\_ENCRYPTION                   | • RSA\_2048<br>• RSA\_3072<br>• RSA\_4096                              | • { Encrypt = true, Wrap=true}<br>• {Encrypt=true, Wrap=true,Decrypt = true, Unwrap=true}                               |
| Symmetric keys | TR31\_D0\_SYMMETRIC\_DATA\_ENCRYPTION\_KEY                         | • TDES\_2KEY<br>• TDES\_3KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256 | • {Encrypt = true, Wrap=true}<br>• {Encrypt=true, Wrap=true,Decrypt = true, Unwrap=true}<br>• { NoRestrictions = true } |

## Translate Pin Data

| Direction            | Key Type                       | Allowed Key Usage               | Allowed Key Algorithm                                                  | Allowed combination of key modes of use                                                                                                |
| -------------------- | ------------------------------ | ------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Inbound Data Source  | DUKPT                          | TR31\_B0\_BASE\_DERIVATION\_KEY | • TDES\_2KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256                 | • { DeriveKey = true }<br>• { NoRestrictions = true }                                                                                  |
| Inbound Data Source  | non-DUKPT (PEK, AWK, IWK, etc) | TR31\_P0\_PIN\_ENCRYPTION\_KEY  | • TDES\_2KEY<br>• TDES\_3KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256 | • { Decrypt = true, Unwrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| Outbound Data Target | DUKPT                          | TR31\_B0\_BASE\_DERIVATION\_KEY | • TDES\_2KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256                 | • { DeriveKey = true }<br>• { NoRestrictions = true }                                                                                  |
| Outbound Data Target | non-DUKPT (PEK, IWK, AWK, etc) | TR31\_P0\_PIN\_ENCRYPTION\_KEY  | • TDES\_2KEY<br>• TDES\_3KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256 | • { Encrypt = true, Wrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true }   |

## Generate/Verify MAC

MAC keys are used for creating cryptographic hashes of a message/body of data. It is not recommended to create a key
with limited key modes of use as you will be unable to perform the matching operation. However, you may import/export a key with only one operation if the other system is intended
to perform the other half of the operation pair.

| Allowed Key Usage    | Allowed Key Usage                 | Allowed Key Algorithm                                                  | Allowed combination of key modes of use                                                                       |
| -------------------- | --------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| MAC Key              | TR31\_M1\_ISO\_9797\_1\_MAC\_KEY  | • TDES\_2KEY<br>• TDES\_3KEY                                           | • { Generate = true }<br>• { Generate = true, Verify = true }<br>• { Verify = true }<br>• { Generate = true } |
| MAC Key (Retail MAC) | TR31\_M1\_ISO\_9797\_3\_MAC\_KEY  | • TDES\_2KEY<br>• TDES\_3KEY                                           | • { Generate = true }<br>• { Generate = true, Verify = true }<br>• { Verify = true }<br>• { Generate = true } |
| MAC Key (CMAC)       | TR31\_M6\_ISO\_9797\_5\_CMAC\_KEY | • TDES\_2KEY<br>• TDES\_3KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256 | • { Generate = true }<br>• { Generate = true, Verify = true }<br>• { Verify = true }<br>• { Generate = true } |
| MAC Key (HMAC)       | TR31\_M7\_HMAC\_KEY               | • TDES\_2KEY<br>• TDES\_3KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256 | • { Generate = true }<br>• { Generate = true, Verify = true }<br>• { Verify = true }                          |
| MAC Key (AS2805)     | TR31\_M0\_ISO\_16609\_MAC\_KEY    | • TDES\_2KEY<br>• TDES\_3KEY                                           | • { Generate = true }<br>• { Generate = true, Verify = true }<br>• { Verify = true }                          |

## GenerateMacEmvPinChange

GenerateMacEmvPinChange combines MAC generation and PIN encryption for EMV offline PIN change operations.
This operation requires two different key types: an integrity key for MAC generation and a confidentiality key for PIN encryption.

| Key Type                                                           | Allowed Key Usage                     | Allowed Key Algorithm                                                  | Allowed combination of key modes of use                                                                                                |
| ------------------------------------------------------------------ | ------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Secure Messaging Integrity Key                                     | TR31\_E2\_EMV\_MKEY\_INTEGRITY        | • TDES\_2KEY                                                           | • { NoRestrictions = true }                                                                                                            |
| Secure Messaging Confidentiality Key                               | TR31\_E1\_EMV\_MKEY\_CONFIDENTIALITY  | • TDES\_2KEY                                                           | • { DeriveKey = true }                                                                                                                 |
| Current PIN PEK (PIN Encryption Key)                               | TR31\_P0\_PIN\_ENCRYPTION\_KEY        | • TDES\_2KEY<br>• TDES\_3KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256 | • { Decrypt = true, Unwrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| New PIN PEK (PIN Encryption Key)                                   | TR31\_P0\_PIN\_ENCRYPTION\_KEY        | • TDES\_2KEY<br>• TDES\_3KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256 | • { Decrypt = true, Unwrap = true }<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true }<br>• { NoRestrictions = true } |
| ARQC Key<br>NoteOnly applies for Visa and Amex derivation schemes. | TR31\_E0\_EMV\_MKEY\_APP\_CRYPTOGRAMS | • TDES\_2KEY                                                           | • { DeriveKey = true }                                                                                                                 |

## VerifyAuthRequestCryptogram

| Allowed Key Usage        | EMV Option                            | Allowed Key Algorithm | Allowed combination of key modes of use |
| ------------------------ | ------------------------------------- | --------------------- | --------------------------------------- |
| • OPTION A<br>• OPTION B | TR31\_E0\_EMV\_MKEY\_APP\_CRYPTOGRAMS | • TDES\_2KEY          | • { DeriveKey = true }                  |

## Import/Export Key

| Operation Type                                             | Allowed Key Usage                                                       | Allowed Key Algorithm                                                  | Allowed combination of key modes of use                                                                                                                                  |
| ---------------------------------------------------------- | ----------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| TR-31 Wrapping Key                                         | TR31\_K1\_KEY\_BLOCK\_PROTECTION\_KEY<br>TR31\_K0\_KEY\_ENCRYPTION\_KEY | • TDES\_2KEY<br>• TDES\_3KEY<br>• AES\_128<br>• AES\_192<br>• AES\_256 | • { Encrypt = true, Wrap = true } (export only)<br>• { Decrypt = true, Unwrap = true } (import only)<br>• { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } |
| Import of trusted CA                                       | TR31\_S0\_ASYMMETRIC\_KEY\_FOR\_DIGITAL\_SIGNATURE                      | • RSA\_2048<br>• RSA\_3072<br>• RSA\_4096                              | • { Verify = true }                                                                                                                                                      |
| Import of public key certificate for asymmetric encryption | TR31\_D1\_ASYMMETRIC\_KEY\_FOR\_DATA\_ENCRYPTION                        | • RSA\_2048<br>• RSA\_3072<br>• RSA\_4096                              | • { Encrypt=true,Wrap=true }                                                                                                                                             |
| Key used to key agreement algorithms such as ECDH          | TR31\_K3\_ASYMMETRIC\_KEY\_FOR\_KEY\_AGREEMENT                          | • ECC\_NIST\_P256<br>• ECC\_NIST\_P384<br>• ECC\_NIST\_P521            | • { DeriveKey = true }                                                                                                                                                   |

## Unused key types

The following key types are not currently used by AWS Payment Cryptography

- TR31\_P1\_PIN\_GENERATION\_KEY
