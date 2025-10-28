# Understanding key attributes for AWS Payment Cryptography key

A tenet of proper key management is that keys are appropriately scoped and
can only be used for permitted operations. As such, certain keys can only be created with
certain key modes of use. Whenever possible, this aligns with the available modes of use
as defined by [TR-31](terminology.md#terms.tr31 "terminology.md#terms.tr31").

Although AWS Payment Cryptography will prevent you from creating invalid keys,
valid combinations are provided here for your convenience.

## Symmetric Keys

- TR31_B0_BASE_DERIVATION_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { DeriveKey = true },{ NoRestrictions = true }

- TR31_C0_CARD_VERIFICATION_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**:
    { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true } ,{ NoRestrictions = true }

- TR31_D0_SYMMETRIC_DATA_ENCRYPTION_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } ,
    { Encrypt = true, Wrap = true } ,{ Decrypt = true, Unwrap = true } ,{ NoRestrictions = true }

- TR31_E0_EMV_MKEY_APP_CRYPTOGRAMS
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }

- TR31_E1_EMV_MKEY_CONFIDENTIALITY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }

- TR31_E2_EMV_MKEY_INTEGRITY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }

- TR31_E4_EMV_MKEY_DYNAMIC_NUMBERS
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }

- TR31_E5_EMV_MKEY_CARD_PERSONALIZATION
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }

- TR31_E6_EMV_MKEY_OTHER
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { DeriveKey = true }, { NoRestrictions = true }

- TR31_K0_KEY_ENCRYPTION_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } ,
    { Encrypt = true, Wrap = true } ,{ Decrypt = true, Unwrap = true } ,{ NoRestrictions = true }

- TR31_K1_KEY_BLOCK_PROTECTION_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } ,
    { Encrypt = true, Wrap = true } ,{ Decrypt = true, Unwrap = true } ,{ NoRestrictions = true }

- TR31_M1_ISO_9797_1_MAC_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY

  - **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true }
    ,{ NoRestrictions = true }

- TR31_M3_ISO_9797_3_MAC_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY

  - **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true }
    ,{ NoRestrictions = true }

- TR31_M6_ISO_9797_5_CMAC_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true }
    ,{ NoRestrictions = true }

- TR31_M7_HMAC_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true } ,{ Generate = true, Verify= true }
    ,{ NoRestrictions = true }

- TR31_P0_PIN_ENCRYPTION_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } ,{ Encrypt = true, Wrap = true }
    ,{ Decrypt = true, Unwrap = true } ,{ NoRestrictions = true }

- TR31_V1_IBM3624_PIN_VERIFICATION_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true }
    ,{ Generate = true, Verify= true } ,{ NoRestrictions = true }

- TR31_V2_VISA_PIN_VERIFICATION_KEY
  - **Allowed Key Algorithms**: TDES_2KEY ,TDES_3KEY ,AES_128 ,AES_192 ,AES_256

  - **Allowed combination of key modes of use**: { Generate = true } ,{ Verify = true }
    ,{ Generate = true, Verify= true } ,{ NoRestrictions = true }

## Asymmetric Keys

- TR31_D1_ASYMMETRIC_KEY_FOR_DATA_ENCRYPTION
  - **Allowed Key Algorithms**: RSA_2048 ,RSA_3072 ,RSA_4096
  - **Allowed combination of key modes of use**: { Encrypt = true, Decrypt = true, Wrap = true, Unwrap = true } ,{ Encrypt = true, Wrap = true } ,{ Decrypt = true, Unwrap = true }
  - **NOTE:**: { Encrypt = true, Wrap = true } is the only valid option when importing a public key that is intended for encrypting data or wrapping a key

- TR31_S0_ASYMMETRIC_KEY_FOR_DIGITAL_SIGNATURE
  - **Allowed Key Algorithms**: RSA_2048 ,RSA_3072 ,RSA_4096
  - **Allowed combination of key modes of use**: { Sign = true } ,{ Verify = true }
  - **NOTE:**: { Verify = true } is the only valid option when importing a key meant for signing, such as root certificate, intermediate certificate or signing certificates for TR-34.
